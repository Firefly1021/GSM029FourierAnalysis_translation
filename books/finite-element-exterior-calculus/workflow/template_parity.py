"""Compare original AJbook settings against FEEC, without touching accepted text."""
import argparse, collections, io, json, os, re, runpy, shutil, subprocess, sys, tempfile, time, unittest
from pathlib import Path
from PIL import Image, ImageDraw
from pypdf import PdfReader

W=runpy.run_path(str(Path(__file__).with_name('aljabr_workflow.py')))
B,P=W['B'],W['P']
write,dump,load,sha=W['write'],W['dump'],W['load'],W['sha256_file']

PROBE=r'''
\makeatletter
\newcommand\MBProbe{%
\setbox0=\hbox{$\Gamma(T)^\perp=\widetilde\Gamma(T^*)$}% Exact accepted equation, only to initialize fonts.
\typeout{PARITY|body-size|\f@size}
\typeout{PARITY|baseline|\the\baselineskip}
\typeout{PARITY|baseline-stretch|\baselinestretch}
\typeout{PARITY|par-indent|\the\parindent}
\typeout{PARITY|par-skip|\the\parskip}
\typeout{PARITY|text-width|\the\textwidth}
\typeout{PARITY|text-height|\the\textheight}
\typeout{PARITY|paper-width|\the\paperwidth}
\typeout{PARITY|paper-height|\the\paperheight}
\typeout{PARITY|odd-margin|\the\oddsidemargin}
\typeout{PARITY|even-margin|\the\evensidemargin}
\typeout{PARITY|head-height|\the\headheight}
\typeout{PARITY|head-sep|\the\headsep}
\typeout{PARITY|top-skip|\the\topskip}
\typeout{PARITY|array-stretch|\arraystretch}
\typeout{PARITY|jot|\the\jot}
\typeout{PARITY|above-display|\the\abovedisplayskip}
\typeout{PARITY|below-display|\the\belowdisplayskip}
\typeout{PARITY|above-short-display|\the\abovedisplayshortskip}
\typeout{PARITY|below-short-display|\the\belowdisplayshortskip}
\typeout{PARITY|thin-math-skip|\the\thinmuskip}
\typeout{PARITY|medium-math-skip|\the\medmuskip}
\typeout{PARITY|thick-math-skip|\the\thickmuskip}
\typeout{PARITY|theorem-pre|\the\theorempreskipamount}
\typeout{PARITY|theorem-post|\the\theorempostskipamount}
\typeout{PARITY|heading-depth|\the\c@secnumdepth}
\typeout{PARITY|contents-depth|\the\c@tocdepth}
\typeout{PARITY|emergency-stretch|\the\emergencystretch}
\typeout{PARITY|tolerance|\the\tolerance}
\typeout{PARITY|pretolerance|\the\pretolerance}
\typeout{PARITY|float-sep|\the\floatsep}
\typeout{PARITY|text-float-sep|\the\textfloatsep}
\typeout{PARITY|intext-sep|\the\intextsep}
\typeout{PARITY|math-roman|\fontname\textfont0}
\typeout{PARITY|math-italic|\fontname\textfont1}
\typeout{PARITY|math-symbols|\fontname\textfont2}
\typeout{PARITY|math-extension|\fontname\textfont3}
\typeout{PARITY|integral-operator|\meaning\intop}
\typeout{PARITY|integral-limits|\meaning\ilimits@}
}
\makeatother
'''

def compare():
    W['guard']()
    root=B.assert_write_path(B.root/'workspace/temporary');stage=Path(tempfile.mkdtemp(prefix='template-parity-',dir=root))
    env=os.environ.copy();env['TEXINPUTS']=os.pathsep.join(str(p) for p in [P.template/'adapter/aljabr-1',P.template/'collections/aljabr-1/upstream',P.template/'adapter',B.root/'tex'])+os.pathsep+os.pathsep
    W['noto_environment'](P.template,stage,env)
    common=r'\usepackage[xindy,splitindex]{imakeidx}'+'\n'+r'\usepackage[unicode,bookmarksnumbered]{hyperref}'+'\n'
    outputs={}
    for kind,font,extra in [('control','font-setup-open.tex',r'\renewcommand*\arraystretch{1.5}'),('integration','feec-fonts.tex',r'\usepackage{feec-aljabr}')]:
        smoke=''
        if kind=='integration':
            source=(B.root/'tex/chapters/bibliography.tex').read_text(encoding='utf8')
            entry_line=next(line for line in source.splitlines() if line.startswith(r'\item\label{bib:source-1}'))
            smoke=r'\newcounter{bookreference}\begin{MBSourceBibliography}{71}'+'\n'+entry_line+'\n'+r'\end{MBSourceBibliography}\renewcommand{\indexname}{索引}\begin{theindex}\item 伴随\end{theindex}'
        content=r'\documentclass[draftmark=false,colors=true,fontsetup='+font+r',titlesetup=titles-setup.tex]{AJbook}'+'\n'+common+extra+'\n'+PROBE+r'\begin{document}\MBProbe\null'+smoke+r'\end{document}'
        entry=write(stage.relative_to(B.root).as_posix()+'/'+kind+'.tex',content)
        result=subprocess.run([shutil.which('xelatex'),'-interaction=nonstopmode','-halt-on-error','-file-line-error',entry.name],cwd=stage,env=env,capture_output=True)
        log=(stage/(kind+'.log')).read_text(encoding='utf8',errors='replace')
        write('logs/template-parity-'+kind+'.log',log)
        assert result.returncode==0,log[-2400:]
        outputs[kind]=dict(re.findall(r'^PARITY\|([^|]+)\|([^\n]*)',log,re.M))
        assert len(outputs[kind])==39,outputs[kind]
    differences={k:{'control':v,'integration':outputs['integration'].get(k)} for k,v in outputs['control'].items() if outputs['integration'].get(k)!=v}
    dump('qa/template/aljabr-settings-parity.json',{'passed':not differences,'parameter_count':len(outputs['control']),'differences':differences,'runtime_values':outputs,'control_reference':'Original AJbook.cls, font-setup-open.tex, titles-setup.tex; exact arraystretch from Template-AJbook.tex; final draftmark=false mode documented by template','semantic_exceptions':['English environment names','original FEEC chapter-based object numbers and stable labels','book-specific metadata, contents entries, original source figures, index and bibliography content','approved non-Fraktur symbol distinctions and exact rare source operator','source summary heading retained instead of adding the template fixed reading-hint title'],'template_hash':W['directory_manifest_hash'](P.template),'stage':str(stage)})
    W['guard']();assert not differences,differences;print('Template runtime parameters match:',len(outputs['control']))

def regression():
    W['guard']();stage=B.assert_write_path(B.root/'workspace/temporary/parity-regression');stage.mkdir(exist_ok=True);tempfile.tempdir=str(stage)
    stream=io.StringIO();start=time.time();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.discover('tests'))
    write('logs/aljabr-parity-regression.log',stream.getvalue())
    dump('qa/template/aljabr-parity-regression.json',{'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'elapsed_seconds':time.time()-start,'head':P.git_head()})
    W['guard']();print(stream.getvalue());assert result.wasSuccessful()

def sheets():
    q=load('qa/template/aljabr-compilation.json');root=Path(q['render_directory']);files=[]
    for start in range(1,q['pdf_pages']+1,4):
        canvas=Image.new('RGB',(1260,1830),'#cccccc');draw=ImageDraw.Draw(canvas);pages=list(range(start,min(start+4,q['pdf_pages']+1)))
        for n,page in enumerate(pages):
            im=Image.open(root/f'page-{page:03}.png').convert('RGB');im.thumbnail((610,870));x,y=n%2*630+10,n//2*915+30;canvas.paste(im,(x,y));draw.text((x,y-20),f'Physical page {page}',fill='black')
        path=B.assert_write_path(root/f'review-{start:03}.jpg');canvas.save(path,quality=93);files.append({'file':str(path),'pages':pages,'sha256':sha(path)})
    dump('qa/template/aljabr-parity-review-sheets.json',{'pdf_sha256':q['pdf_sha256'],'sheets':files,'review_status':'pending actual agent viewing'})
    print(json.dumps({'pdf_sha256':q['pdf_sha256'],'pages':q['pdf_pages'],'sheets':len(files),'root':str(root)}))

def publish():
    """Publish only the exact 140-page build actually viewed by the agent."""
    W['guard']()
    expected='350efa80d552271e47e8ec39e2ec773df531cf4afb2e54cd52d671662a481870'
    previous='b938856105d0e70b1a2e4bb44723ec7e4f88cc816fd7c9db221245b3f3b095e7'
    q=load('qa/template/aljabr-compilation.json')
    parity=load('qa/template/aljabr-settings-parity.json')
    regression=load('qa/template/aljabr-parity-regression.json')
    review=load('qa/template/aljabr-parity-review-sheets.json')
    assert q['success'] and q['pdf_sha256']==expected and q['pdf_pages']==140
    assert q['minimum_latex_rounds']>=2 and not any(q['warnings'].values())
    assert parity['passed'] and parity['parameter_count']==39 and not parity['differences']
    assert parity['template_hash']==W['directory_manifest_hash'](P.template)
    assert regression['passed'] and regression['tests']==39 and regression['head']==P.git_head()
    assert review['pdf_sha256']==expected
    assert sorted(p for row in review['sheets'] for p in row['pages'])==list(range(1,141))
    for row in review['sheets']: assert sha(Path(row['file']))==row['sha256']
    # These exact images, not a different candidate, were viewed in this turn.
    details=[14,37,118,131,137]
    detail_records=[{'page':p,'file':str(Path(q['render_directory'])/f'detail-{p}.png'),
                     'sha256':sha(Path(q['render_directory'])/f'detail-{p}.png')} for p in details]
    for row in load('qa/template/aljabr-layout-provenance.json'):
        assert sha(B.root/row['accepted_input'])==row['input_sha256']
        assert sha(B.root/row['generated'])==row['generated_sha256']
        text=(B.root/row['generated']).read_text(encoding='utf8')
        assert not W['s']['find_chinese_prose_punctuation'](text)
        assert not re.search(r'\\(?:mathfrak|frak)\b',text)
    for path,h in q['template_input_hashes'].items(): assert sha(Path(path))==h
    assert sha(B.root/'tex/aljabr-main.tex')==q['main_tex_sha256']
    upstream=P.template/'collections/aljabr-1/upstream'
    manifest=json.loads((upstream.parent/'upstream-manifest.json').read_text(encoding='utf8'))
    assert len(manifest['files'])==36
    for row in manifest['files']: assert sha(upstream/row['path'])==row['sha256']
    baseline=load('qa/template/aljabr-baseline.json')
    refs=subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)','refs/heads/book/'],cwd=P.root,text=True).splitlines()
    other=lambda rows:[r for r in rows if not r.startswith('refs/heads/book/'+W['ID']+' ')]
    assert other(refs)==other(baseline['other_book_refs'])
    assert subprocess.check_output(['git','remote','-v'],cwd=P.root,text=True).splitlines()==baseline['remote']
    source=Path(q['build_directory'])/'aljabr-main.pdf';assert sha(source)==expected
    reader=PdfReader(source);dest=reader.named_destinations;actions=collections.Counter()
    for page in reader.pages:
        for item in page.get('/Annots',[]):
            action=item.get_object().get('/A',{});kind=action.get('/S')
            if kind: actions[str(kind)]+=1
            if kind=='/GoTo': assert action['/D'] in dest
    refs_report=load('qa/template/aljabr-cross-references.json')
    assert len(refs_report['objects'])==537 and not refs_report['number_changes']
    for row in refs_report['objects']:
        assert reader.get_destination_page_number(dest[row['destination']])+1==row['physical_output_page']
    fonts=subprocess.run([shutil.which('pdffonts'),str(source)],capture_output=True,check=True)
    font_text=fonts.stdout.decode('utf8',errors='replace')
    write('logs/aljabr-parity-pdffonts.log',font_text)
    assert 'esint' not in font_text.lower()
    assert all(name in font_text for name in ['CMEX10','CMMI10','CMSY10','NotoSansCJKsc-Regular','NotoSansCJKsc-Bold'])
    archive=B.assert_write_path(B.root/'output/archive/book-aljabr-noto-before-parity-20261021.pdf')
    assert sha(archive)==previous
    target=B.assert_write_path(B.root/'output/book-aljabr-zh.pdf');assert sha(target)==previous
    # Withdraw the rejected enlargement without deleting its files.
    retired=[]
    for old,new in [
        ('output/readability-preview.pdf','output/archive/book-readability-12pt-rejected-20261021.pdf'),
        ('tex/readability-preview.tex','workspace/temporary/rejected-readability-20261021/readability-preview.tex'),
        ('workflow/readability_preview.py','workspace/temporary/rejected-readability-20261021/readability_preview.py')]:
        src=B.assert_write_path(B.root/old);dst=B.assert_write_path(B.root/new)
        assert src.is_file() and not dst.exists();h=sha(src)
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(src),str(dst));assert sha(dst)==h
        retired.append({'from':old,'archive':new,'sha256':h})
    preview=load('qa/template/readability-preview.json')
    preview.update(status='withdrawn-user-rejected',output=retired[0]['archive'],
        withdrawal_reason='User requested all settings follow the upstream template; 12pt/21pt preview is not production.',
        retired_artifacts=retired,external_links='Historical preview links are not current-edition acceptance evidence.')
    dump('qa/template/readability-preview.json',preview)
    write('qa/template/readability-preview.md',(B.root/'qa/template/readability-preview.md').read_text(encoding='utf8')+
        '\n## Withdrawn, 2026-10-21\n\nThe user rejected this enlargement and requested the original template settings. The PDF is recoverably archived, and experimental entry/build scripts are retired to book-local temporary storage. This report is historical, not current acceptance. See aljabr-template-parity-acceptance.json.\n')
    visual={'passed':True,'pdf_sha256':expected,'pages_directly_viewed':list(range(1,141)),
        'overview_dpi':85,'sheets':review['sheets'],'detail_dpi':150,'detail_images':detail_records,
        'findings':'All 140 pages viewed in four-page sheets; five enlarged pages inspected. No visible clipping, overlap, missing glyph or display overflow. Native recto openings, title wrapping, integral limits, source-box page splits, bibliography and two-column index checked. This is visual layout QA, not a new mathematical proof or aesthetic approval by the user.'}
    dump('qa/template/aljabr-parity-visual-review.json',visual)
    review['review_status']='passed; all 140 pages actually viewed';dump('qa/template/aljabr-parity-review-sheets.json',review)
    q['visual_review']='passed';q['visual_review_report']='qa/template/aljabr-parity-visual-review.json'
    dump('qa/template/aljabr-compilation.json',q)
    shutil.copyfile(source,target);assert sha(target)==expected
    report={'passed':True,'book_id':W['ID'],'scope':'User-requested original-template visual settings; no retranslation.',
        'pdf':'output/book-aljabr-zh.pdf','pdf_sha256':expected,'pdf_pages':140,
        'previous_edition_archive':archive.relative_to(B.root).as_posix(),'previous_sha256':previous,
        'template_manifest_hash':parity['template_hash'],'upstream_files_byte_exact':36,
        'protected_source_templates_and_accepted_inputs_unchanged':True,'translation_units_unchanged':'47/47',
        'other_book_refs_unchanged':True,'remote_configuration_unchanged':True,'remote_push':False,
        'runtime_parity':parity,'regression':regression,'compile':q,
        'pdf_link_actions':dict(actions),'all_internal_destinations_valid':True,'label_numbers_unchanged':537,
        'font_audit':{'esint_absent':True,'native_integrals':True,'log':'logs/aljabr-parity-pdffonts.log',
            'scope':'Raw upstream font setup. Rare source orthogonal-sum operator retains its existing isolated font; original figures retain embedded source fonts.'},
        'layout_provenance':'qa/template/aljabr-layout-provenance.json','visual_review':'qa/template/aljabr-parity-visual-review.json',
        'retired_readability_artifacts':retired,'semantic_exceptions':parity['semantic_exceptions'],
        'limits':'Settings match the pinned template source, not a claim of pixel identity to the upstream prebuilt PDF across OS/font discovery. Ten prose-only newlines avoid overflow without changing source characters or global settings.'}
    dump('qa/template/aljabr-template-parity-acceptance.json',report)
    cfg=B.load_config();cfg['typesetting']['qa']='qa/template/aljabr-template-parity-acceptance.json'
    cfg['typesetting']['settings_policy']='Original AJbook source settings; no readability enlargement or esint override'
    dump('config/book.yaml',cfg)
    status=(B.root/'PROJECT_STATUS.md').read_text(encoding='utf8')
    status=status.replace('Final PDF pages: 138','Final PDF pages: 140').replace('Final PDF SHA-256: '+previous,'Final PDF SHA-256: '+expected)
    status=status.replace('Final QA: qa/template/aljabr-noto-acceptance.json','Final QA: qa/template/aljabr-template-parity-acceptance.json')
    write('PROJECT_STATUS.md',status+'\nVisual settings: original AJbook source settings; 39/39 runtime parameters matched\nRegression: 39/39 passed\nVisual QA: all 140 pages, plus five 150-DPI details inspected\nReadability enlargement: withdrawn and recoverably archived\nPrior Noto report: historical; current authority is Final QA above\n')
    W['guard']();print(json.dumps({'passed':True,'pages':140,'sha256':expected,'links':dict(actions),'remote_push':False}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('book_id',choices=[W['ID']]);parser.add_argument('action',choices=['compare','regression','sheets','publish']);args=parser.parse_args()
    {'compare':compare,'regression':regression,'sheets':sheets,'publish':publish}[args.action]()
