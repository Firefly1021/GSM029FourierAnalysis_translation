"""Audit and publish FEEC's explicitly authorized original-font correction."""
import argparse, collections, json, re, runpy, shutil, subprocess, winreg
import pdfplumber
from pathlib import Path
from PIL import Image, ImageDraw
from pypdf import PdfReader

W = runpy.run_path(str(Path(__file__).with_name('aljabr_workflow.py')))
B, P = W['B'], W['P']
load, dump, write, sha = W['load'], W['dump'], W['write'], W['sha256_file']
PREVIOUS = '2b1bd263e11d32a2dec0c82d17bfd17f3a6749c0d58a12c0472b8ead03ada289'

def inspect():
    W['guard']()
    q = load('qa/template/aljabr-compilation.json')
    assert q['success'] and not any(q['warnings'].values())
    stage, render = Path(q['build_directory']), Path(q['render_directory'])
    pdf = stage/'aljabr-main.pdf'
    assert sha(pdf) == q['pdf_sha256']
    probe = subprocess.run([shutil.which('pdffonts'), str(pdf)], text=True, capture_output=True, check=True)
    raw_fonts = probe.stdout
    write('logs/aljabr-noto-pdffonts.log', raw_fonts)
    write('logs/aljabr-noto-poppler-diagnostics.log', probe.stderr)
    assert 'NotoSansCJKsc-Regular' in raw_fonts and 'NotoSansCJKsc-Black' in raw_fonts
    manifest = json.loads((P.template/'collections/aljabr-1/fonts/noto-sans-cjk-sc/manifest.json').read_text(encoding='utf8'))
    installed = []
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows NT\CurrentVersion\Fonts') as key:
        for row in manifest['files']:
            name = 'Noto Sans CJK SC' + ('' if row['weight']=='Regular' else ' '+row['weight']) + ' (OpenType)'
            value, _ = winreg.QueryValueEx(key, name)
            assert sha(Path(value)) == row['sha256']
            installed.append({'registry_name':name, 'file':value, 'sha256':row['sha256']})
    fls = (stage/'aljabr-main.fls').read_text(encoding='utf8', errors='replace')
    assert 'font-setup-open.tex' in fls
    assert not re.search(r'INPUT .*[/\\](Mystyle\.sty|translation-adapter\.sty)', fls)
    log = (stage/'aljabr-main.log').read_text(encoding='utf8', errors='replace')
    assert not re.search(r'Font shape .* undefined|Some font shapes were not available|fontspec Warning',log,re.I)
    previous = load('qa/template/archive/fandol-20261021/aljabr-compilation.json')
    old_render = Path(previous['render_directory'])
    same, changed = [], []
    for i in range(1, q['pdf_pages']+1):
        f = render/f'page-{i:03}.png'
        old = old_render/f.name
        (same if old.exists() and sha(f)==sha(old) else changed).append(i)
    sheets = []
    for start in range(1, q['pdf_pages']+1, 4):
        numbers = list(range(start, min(start+4, q['pdf_pages']+1)))
        canvas = Image.new('RGB', (1260,1830), '#cccccc')
        draw = ImageDraw.Draw(canvas)
        for n, page in enumerate(numbers):
            im = Image.open(render/f'page-{page:03}.png').convert('RGB');im.thumbnail((610,870))
            x,y = (n%2)*630+10,(n//2)*915+30
            canvas.paste(im,(x,y));draw.text((x,y-20), f'Physical page {page}',fill='black')
        path = B.assert_write_path(render/f'review-{start:03}.jpg');canvas.save(path,quality=93)
        sheets.append({'image':str(path),'pages':numbers,'sha256':sha(path)})
    old_pdf = B.root/'output/archive/book-aljabr-fandol-20261021.pdf'
    assert sha(old_pdf)==PREVIOUS
    normalize = lambda p: re.sub(r'\s+','',p.extract_text())
    old, new = PdfReader(old_pdf), PdfReader(pdf)
    changed_text = [i+1 for i,(a,b) in enumerate(zip(old.pages,new.pages)) if normalize(a)!=normalize(b)]
    # pypdf's fallback mapping cannot decode the legacy GB1 CJK font correctly.
    # pdfminer's installed CMaps decode both old Fandol and new Noto reliably.
    with pdfplumber.open(old_pdf) as a, pdfplumber.open(pdf) as b:
        pairs = [(normalize(x),normalize(y)) for x,y in zip(a.pages,b.pages)]
        verified_text_differences = [i+1 for i,(x,y) in enumerate(pairs) if x!=y]
        inventory_differences = [i+1 for i,(x,y) in enumerate(pairs)
                                 if collections.Counter(x)!=collections.Counter(y)]
    report = {'pdf_sha256':q['pdf_sha256'],'pdf_pages':q['pdf_pages'],'previous_pdf_sha256':PREVIOUS,
              'font_source':manifest,'windows_user_install':installed,'scoped_font_resolution':q['font_resolution'],
              'pdf_font_listing':raw_fonts,'original_upstream_font_setup_loaded':True,'no_font_substitution_warning':True,
              'byte_identical_pages_to_previous':same,'visually_changed_pages':changed,
              'pypdf_pages_with_unicode_mapping_differences':changed_text,
              'pages_with_changed_normalized_extracted_text':verified_text_differences,
              'pages_with_changed_character_inventory':inventory_differences,
              'page_66_extraction_order_note':'Embedded source figure PDF contains clipped source-page text. Font-dependent sorting changes extraction order, not glyph inventory or visible source/translation. Both rendered page 66 editions inspected; accepted figure/input hashes unchanged.',
              'text_comparison_engine':'pdfplumber/pdfminer with GB1 CMaps; pypdf fallback differences separately recorded',
              'poppler_diagnostics':probe.stderr,'review_sheets':sheets,
              'note':'Four official faces resolve exactly. Only faces actually used by the document are embedded; English Proof does not force embedding unused CJK Medium.'}
    dump('qa/template/aljabr-noto-inspection.json',report)
    W['guard']()
    print(json.dumps({'pages':q['pdf_pages'],'changed_text_pages':verified_text_differences,'changed_character_inventory':inventory_differences,'sheets':len(sheets)}))

def publish():
    W['guard']()
    q = load('qa/template/aljabr-compilation.json')
    info = load('qa/template/aljabr-noto-inspection.json')
    visual = load('qa/template/aljabr-noto-visual-review.json')
    regression = load('qa/template/aljabr-noto-regression.json')
    assert q['success'] and q['labels']==537 and not q['label_number_changes'] and not any(q['warnings'].values())
    assert regression['passed'] and regression['tests']==36
    assert visual['passed'] and visual['pdf_sha256']==info['pdf_sha256']==q['pdf_sha256']
    assert set(visual['directly_viewed_pages'])==set(range(1,q['pdf_pages']+1))
    assert info['pages_with_changed_normalized_extracted_text']==[66,138], info['pages_with_changed_normalized_extracted_text']
    assert info['pages_with_changed_character_inventory']==[138]
    for row in load('qa/template/aljabr-layout-provenance.json'):
        assert sha(B.root/row['accepted_input'])==row['input_sha256']
        assert sha(B.root/row['generated'])==row['generated_sha256']
        data=(B.root/row['generated']).read_text(encoding='utf8')
        assert not W['s']['find_chinese_prose_punctuation'](data)
        assert not re.search(r'\\(?:mathfrak|frak)\b',data)
    assert not W['s']['find_chinese_prose_punctuation']((B.root/'tex/aljabr-main.tex').read_text(encoding='utf8'))
    upstream=P.template/'collections/aljabr-1/upstream'
    manifest=json.loads((upstream.parent/'upstream-manifest.json').read_text(encoding='utf8'))
    assert len(manifest['files'])==36
    for row in manifest['files']: assert sha(upstream/row['path'])==row['sha256']
    for path,digest in q['template_input_hashes'].items():assert sha(Path(path))==digest
    baseline=load('qa/template/aljabr-baseline.json')
    refs=subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)','refs/heads/book/'],cwd=P.root,text=True).splitlines()
    other=lambda lines: [x for x in lines if not x.startswith('refs/heads/book/finite-element-exterior-calculus ')]
    assert other(refs)==other(baseline['other_book_refs'])
    assert subprocess.check_output(['git','remote','-v'],cwd=P.root,text=True).splitlines()==baseline['remote']
    source=Path(q['build_directory'])/'aljabr-main.pdf';assert sha(source)==q['pdf_sha256']
    archive=B.root/'output/archive/book-aljabr-fandol-20261021.pdf';assert sha(archive)==PREVIOUS
    dest=B.assert_write_path(B.root/'output/book-aljabr-zh.pdf')
    assert sha(dest) in [PREVIOUS,q['pdf_sha256']], 'Refuse replacing any unexpected output'
    if sha(dest)==PREVIOUS:shutil.copyfile(source,dest)
    assert sha(dest)==q['pdf_sha256']
    q['visual_review']='passed';q['visual_review_report']='qa/template/aljabr-noto-visual-review.json'
    dump('qa/template/aljabr-compilation.json',q)
    report={'passed':True,'book_id':W['ID'],'scope':'Font-only correction authorized by user; no accepted translation edits.',
            'pdf':'output/book-aljabr-zh.pdf','pdf_sha256':q['pdf_sha256'],'pdf_pages':q['pdf_pages'],
            'previous_edition_archive':'output/archive/book-aljabr-fandol-20261021.pdf','previous_sha256':PREVIOUS,
            'font_policy':'Original upstream font-setup-open.tex, official pinned Noto faces, no fallback.',
            'upstream_files_byte_exact':36,'protected_inputs_unchanged':True,'legacy_pdf_unchanged':True,
            'translation_units_unchanged':'47/47','other_book_refs_unchanged':True,'remote_configuration_unchanged':True,
            'template_collection_hash':W['directory_manifest_hash'](P.template),'compile':q,
            'font_inspection':info,'visual_review':visual,'regression':regression,'remote_push':False}
    dump('qa/template/aljabr-noto-acceptance.json',report)
    cfg=B.load_config();cfg['typesetting']['qa']='qa/template/aljabr-noto-acceptance.json'
    cfg['typesetting']['font_revision']='Noto Sans CJK SC Sans2.004; upstream font setup unchanged'
    dump('config/book.yaml',cfg)
    status=(B.root/'PROJECT_STATUS.md').read_text(encoding='utf8')
    status=status.replace('Final PDF SHA-256: '+PREVIOUS,'Final PDF SHA-256: '+q['pdf_sha256']).replace('Final QA: qa/template/aljabr-acceptance.json','Final QA: qa/template/aljabr-noto-acceptance.json')
    if 'Font correction: Original AJbook Noto setup' not in status:
        status+='\nFont correction: Original AJbook Noto setup, no fallback; Sans2.004 installed and pinned\nFont QA: qa/template/aljabr-noto-acceptance.json\nPrevious fallback edition archived: output/archive/book-aljabr-fandol-20261021.pdf\n'
    write('PROJECT_STATUS.md',status)
    W['guard']()
    print(json.dumps({'published':True,'sha256':sha(dest),'pages':q['pdf_pages']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('book_id',choices=[W['ID']]);parser.add_argument('action',choices=['inspect','publish']);args=parser.parse_args()
    {'inspect':inspect,'publish':publish}[args.action]()
