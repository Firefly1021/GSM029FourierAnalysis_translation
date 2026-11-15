"""Book-local sample processor using the established shared workflow extension.

No global processor, policy, template or other book is changed. Source review
is an explicit agent visual review, not a claim of independent human approval.
"""
from __future__ import annotations

import collections
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'shared/src'))
from mathbook.project import ProjectPaths, directory_manifest_hash, sha256_file
from mathbook.workflow import (start_book, verify_book_context, _write_json,
    _book_status_text, update_project_record, project_record, TERM_COLUMNS,
    PROPER_NAME_COLUMNS, NOTATION_COLUMNS)
from mathbook.qa import find_chinese_prose_punctuation
from mathbook.structure import StructureBlock
from mathbook.formula import FormulaRegistry
from mathbook.template import verify_manifest
from sample_content import BLOCKS
from pypdf import PdfReader
from PIL import Image, ImageEnhance

BOOK_ID = 'an-introduction-to-partial-differential-equations'
project = ProjectPaths(ROOT)
book, record = verify_book_context(project, BOOK_ID, writable=True)
PAGES = [12, 13, 14]
MATH = re.compile(r'\\begin\{equation\}.*?\\end\{equation\}|\\\[.*?\\\]|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$', re.S)
DISPLAY_REGIONS = {
    'ode-existence': [(12, 320, 904, 1040, 974), (12, 380, 1080, 1040, 1168), (12, 390, 1195, 1040, 1253)],
    'equivalent-integral-equation': [(12, 350, 1448, 1040, 1541)],
    'picard-iteration': [(13, 320, 205, 1040, 448)],
    'inverse-function': [(13, 150, 848, 1040, 913), (13, 390, 947, 800, 1008),
                         (13, 260, 1038, 960, 1197), (13, 400, 1311, 800, 1374)],
    'implicit-function': [(13, 160, 1540, 1040, 1605), (13, 360, 1653, 850, 1714),
                          (14, 200, 210, 960, 363), (14, 400, 448, 870, 510),
                          (14, 380, 560, 870, 614)],
    'nonunique-example': [(14, 390, 1422, 850, 1523)],
    'nonunique-family': [(14, 250, 1580, 1040, 1710)],
}


def write(path: Path, text: str):
    path = book.assert_write_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def tsv(path, columns, rows):
    path = book.assert_write_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as handle:
        w = csv.DictWriter(handle, fieldnames=columns, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def emit(block, language):
    text = block['english' if language == 'en' else 'chinese']
    label = r'\label{' + block['label'] + '}' if block['label'] else ''
    if block['type'] == 'section':
        return r'\subsection{' + text + '}' + label
    if block['type'] == 'subsection':
        return (r'\subsubsection{' + text + '}' + label) if label else r'\paragraph*{' + text + '}'
    if block['type'] == 'theorem':
        title = block['title_en' if language == 'en' else 'title_zh']
        return r'\begin{Theorem}{' + title + '}\n' + label + '\n' + text + '\n' + r'\end{Theorem}'
    return text


def bbox(region, reader, image):
    page, x0, y0, x1, y1 = region
    iw, ih = image.size
    media = reader.pages[page-1].mediabox
    return [round(x0/iw*float(media.width), 3), round(y0/ih*float(media.height), 3),
            round(x1/iw*float(media.width), 3), round(y1/ih*float(media.height), 3)]


def prepare():
    source = book.require_source_pdf()
    reader = PdfReader(source)
    images = {p: Image.open(book.root / f'workspace/pages/source-{p:03d}.png') for p in PAGES}
    for p in PAGES:
        write(book.root / f'workspace/raw-text/pdf-{p:04d}.txt', reader.pages[p-1].extract_text() or '')
        out = book.root / f'workspace/pages/preprocessed/pdf-{p:04d}-contrast.png'
        out.parent.mkdir(parents=True, exist_ok=True)
        ImageEnhance.Contrast(images[p].convert('L')).enhance(1.12).save(out)
    formulae, structures = [], []
    registry = FormulaRegistry()
    en, zh = [], []
    for block in BLOCKS:
        english, chinese = block['english'], block['chinese']
        # Translated prose may legitimately reorder inline expressions, but not
        # change their tokens. Displayed formula order must remain identical.
        emath, zmath = MATH.findall(english), MATH.findall(chinese)
        assert collections.Counter(emath) == collections.Counter(zmath), block['id']
        ed = [m for m in emath if not m.startswith('$')]
        zd = [m for m in zmath if not m.startswith('$')]
        assert ed == zd, block['id']
        locations = []
        for region in block['regions']:
            p, *coords = region
            crop = book.root / f'workspace/crops/structure/{block["id"]}-p{p:04d}.png'
            crop.parent.mkdir(parents=True, exist_ok=True)
            images[p].crop(tuple(coords)).save(crop)
            locations.append({'pdf_page': p, 'printed_page': p-10,
                              'bbox': bbox(region, reader, images[p]),
                              'bbox_convention': 'PDF points, top-left origin',
                              'image_crop': crop.relative_to(book.root).as_posix(),
                              'raw_ocr': f'workspace/raw-text/pdf-{p:04d}.txt'})
        math_ids = []
        display_index = 0
        for ordinal, math in enumerate(emath, 1):
            region = block['regions'][0]
            display = not math.startswith('$')
            if display:
                region = DISPLAY_REGIONS[block['id']][display_index]
                display_index += 1
            p, *coords = region
            formula_id = f'math:{block["id"]}:{ordinal:03d}'
            math_ids.append(formula_id)
            key = re.search(r'\\label\{([^}]+)\}', math)
            label = key.group(1) if key else None
            crop = book.root / f'workspace/crops/formula/{block["id"]}-{ordinal:03d}.png'
            crop.parent.mkdir(parents=True, exist_ok=True)
            images[p].crop(tuple(coords)).save(crop)
            tokens = tuple(re.findall(r'\\[A-Za-z]+|\\.|[^\s]', math))
            base = registry.register(math, tokens, p, tuple(bbox(region, reader, images[p])),
                                     .98, 'reviewed', label=label)
            formulae.append({'formula_id': formula_id, 'registry_id': base.id,
                'block_id': block['id'], 'pdf_page': p, 'printed_page': p-10,
                'bbox': list(base.bbox), 'kind': 'display' if display else 'inline',
                'bbox_precision': 'visually selected formula crop' if display else 'parent block region; not token-level localization',
                'equation_number': {'eq:uniform-lipschitz-bound':'1.1',
                    'eq:ode-initial-value-dynamics':'1.2', 'eq:ode-initial-value-data':'1.3',
                    'eq:ode-integral-equation':'1.4', 'eq:picard-iteration':'1.5'}.get(label),
                'latex_label': label, 'reconstructed_latex': math,
                'tokens': tokens, 'image_crop': crop.relative_to(book.root).as_posix(),
                'confidence': 'high', 'confidence_score': .98,
                'verification_status': 'agent-reviewed-against-scan',
                'verification_limit': 'Not independent human approval. Source scan is authoritative.'})
        assert display_index == len(DISPLAY_REGIONS.get(block['id'], []))
        StructureBlock(block['id'], block['type'], locations[0]['pdf_page'],
                       tuple(locations[0]['bbox']), .98, 'reviewed')
        structures.append({**block, 'source_locations': locations, 'formula_ids': math_ids,
            'confidence': 'high', 'review_status': 'agent-reviewed-against-scan',
            'translation_review_status': 'agent-reviewed-awaiting-user-sample-approval'})
        en.append(emit(block, 'en'))
        zh.append(emit(block, 'zh'))
    _write_json(book.root / 'structured/source/sample.json', {'book_id': BOOK_ID, 'blocks': structures})
    _write_json(book.root / 'structured/reviewed/sample.json', {'book_id': BOOK_ID, 'blocks': structures})
    _write_json(book.root / 'formulae/sample-registry.json', {'formulae': formulae})
    _write_json(book.root / 'formulae/shared-registry.json', {'formulae': registry.records()})
    write(book.root / 'structured/reviewed/sample-restored-en.tex', '\n\n'.join(en)+'\n')
    write(book.root / 'translation/reviewed/sample.tex', '\n\n'.join(zh)+'\n')
    write(book.root / 'tex/chapters/sample.tex', '\n\n'.join(zh)+'\n')
    write(book.main_tex, r'''\makeatletter
\def\input@path{{../template/style/}{../template/adapter/}{../template/assets/}}
\makeatother
\documentclass[a4paper,UTF8,12pt]{ctexart}
\usepackage{Mystyle}
\usepackage{translation-adapter}
\input{translation-macros.tex}
\title{偏微分方程引论\\代表性试译样本}
\author{Michael Renardy \and Robert C. Rogers}
\date{}
\hypersetup{pdftitle={偏微分方程引论: 代表性试译样本},pdfauthor={Michael Renardy; Robert C. Rogers}}
\begin{document}
\maketitle
\color{ZhengWen}
\section{引言}\label{chap:introduction}
\input{chapters/sample.tex}
\end{document}
''')
    _write_json(book.qa / 'sample-plan.json', {
        'book_id': BOOK_ID, 'representative_pages': PAGES, 'printed_pages': [2,3,4],
        'scope': 'All body text on these three pages; no running headers or printed page numbers in prose.',
        'chapter_heading_context_only': 'Introduction is a context heading from PDF 11, not a claim to translate its introductory paragraphs.',
        'coverage': ['prose','four theorem environments','proof discussion (not a formal Proof block)',
                     'inline mathematics','display mathematics','matrices','numbered equations',
                     'equation references','theorem reference','cross-page theorem and paragraph'],
        'not_present': ['formal Proof heading','figure','table','footnote'],
        'selection_reason': 'A compact continuous sample with a theorem crossing a page, poor math OCR, accented names, and locally resolvable references.'})
    names = [('Picard-Lindelöf','eponym','PDF 12 / printed 2'),
             ('Lipschitz','eponym','PDF 12 / printed 2'),('Gronwall','eponym','PDF 14 / printed 4'),
             ('Michael Renardy','author','PDF 1 / title page'),('Robert C. Rogers','author','PDF 1 / title page')]
    tsv(book.proper_names, PROPER_NAME_COLUMNS,
        [{'Source Form':n, 'Canonical Form':n, 'Category':c, 'First Occurrence':p,
          'Language or Script':'Latin', 'Preserve Exactly':'Yes', 'Review Status':'reviewed',
          'Notes':'Verified against source image; no expansion or transliteration.'} for n,c,p in names])
    terms = [('initial-value problem','初值问题','ordinary differential equations'),
             ('existence','存在性','solution existence'),('multiplicity','多解性','number of solutions'),
             ('uniqueness','唯一性','at most one solution'),
             ('uniformly Lipschitz','一致 Lipschitz 连续','uniform condition in second variable'),
             ('inverse function theorem','反函数定理','Theorem 1.2'),
             ('implicit function theorem','隐函数定理','Theorem 1.3'),
             ('nonsingular','非奇异','derivative matrix'),('linearization','线性化','local nonlinear systems')]
    global_terms = project.system / 'glossary/terminology.tsv'
    with global_terms.open(encoding='utf-8-sig', newline='') as handle:
        global_rows = list(csv.DictReader(handle, delimiter='\t'))
    candidates, lookups = [], []
    for en, cn, context in terms:
        matches = [r for r in global_rows if r['English'].casefold() == en.casefold()]
        approved = [r for r in matches if r['Status'] == 'approved']
        # No exact approved sample term exists in the checked global library.
        # Any future conflicting approval must be reviewed, not overridden.
        assert not approved or any(r['Preferred Chinese'] == cn for r in approved), (en, approved)
        lookups.append({'english':en,'matches':matches,'selected_chinese':cn,
                        'action':'reuse-approved-if-context-matches' if approved else 'book-candidate'})
        if not approved:
            candidates.append(dict(zip(TERM_COLUMNS, [en,cn,'ODE / calculus',context,'','proposed',
                        record.title,'PDF 12--14 / printed 2--4',record.title,'sample','Not globally approved.'])))
    tsv(book.candidates, TERM_COLUMNS, candidates)
    _write_json(book.qa / 'terminology-lookup.json', {'global_file':'shared/glossary/terminology.tsv',
        'global_sha256':sha256_file(global_terms), 'lookups':lookups})
    tsv(book.notation, NOTATION_COLUMNS, [dict(zip(NOTATION_COLUMNS, row)) for row in [
        [r'\mathbf F, \mathbf y, \mathbf x',r'\mathbf F, \mathbf y, \mathbf x','Bold vectors and vector-valued functions','sample','PDF 12--14','Yes','reviewed','Preserved from scan; not Fraktur.'],
        [r'\hat{\mathbf y}',r'\hat{\mathbf y}','Implicit function','Theorem 1.3','PDF 14','Yes','reviewed','Hat and boldface retained.'],
        [r'\gamma',r'\gamma','Lipschitz constant or parameter, according to context','sample','PDF 12 / 14','Yes','reviewed','Do not merge distinct contexts.']]])
    _write_json(book.qa / 'source-review.json', {
        'reviewer':'Codex agent visual comparison, not independent human approval',
        'pdf_pages':PAGES,'printed_pages':[2,3,4], 'blocks':len(BLOCKS),
        'display_formulae':sum(f['kind']=='display' for f in formulae),
        'inline_math_regions':sum(f['kind']=='inline' for f in formulae),
        'checks':['all page-body paragraphs accounted for','running headers removed',
                  'cross-page iteration paragraph joined','Theorem 1.3 joined across PDF 13/14',
                  'Theorem headings retained in English','all matrices restored from images',
                  'bold vectors distinguished from scalar components','1/3 and 3/2 exponents checked',
                  'strict and non-strict inequalities checked','five printed equation numbers checked'],
        'low_confidence_formulae':0,'low_confidence_prose':0,
        'source_quirks_preserved':[r'The piecewise solution prints 0<t<=gamma, not 0<=t<=gamma; not silently changed.'],
        'forward_prose_pointers':['smoothness below','later chapters','Gronwall proof below'],
        'forward_pointer_policy':'Retained as prose; these are not invented numbered cross-references.',
        'limitations':'Only these three pages are visually verified, not all 444 source pages.'})
    mapping = json.loads((book.root / 'structured/source/page-map.json').read_text(encoding='utf-8'))
    for p in mapping['pages']:
        if p['pdf_page'] in PAGES:
            p.update(printed_page_verified=p['pdf_page']-10, mapping_status='agent-visually-verified', chapter=1, section='1.1')
    _write_json(book.root / 'structured/source/page-map.json', mapping)
    write(book.qa / 'scan-restoration-report.md', '''# Scan restoration sample

The authoritative source is the unmodified scan, not the hidden OCR layer.
All 444 pages were inspected for image coverage, hidden-text rendering modes,
text quantity, rotation and image resolution. Tiled image coverage is unioned.
PDF 12--14 correspond to printed 2--4, visually checked. The global -10 offset
is only a candidate outside the sample; frontmatter is not assigned Arabic pages.

The sample scans are approximately 200 dpi. Original PDF pixels are not replaced.
1800-pixel-high render derivatives and a mild 1.12 contrast grayscale alternative
are retained. No aggressive binarization, denoising or speculative symbol repair.
Existing hidden OCR is retained verbatim as the raw OCR. Prose was corrected
against the page images. Mathematics was transcribed independently from images,
with separate crops for 16 displayed formula regions and block-level provenance
for inline regions. Raw OCR omission is not evidence that an equation is absent.

OCR defects include Picard-LindelGf, lost display mathematics, damaged membership
and arrow signs, scan-induced word splits and collapsed matrix structure.
The reconstructed English permanently retains the restored formulas and prose.
Confidence reflects agent review, not independent human acceptance.
''')
    write(book.root / 'README.md', '''# An Introduction to Partial Differential Equations

Authors: Michael Renardy and Robert C. Rogers. Second Edition, as printed on the source title page.

This is a sample-only active book in the unified books/shared library. Active
branch: main. The book/... branch is a local registration checkpoint, not a worktree.

- Edit or compile: `tex/main.tex` (XeLaTeX; pinned Mystyle and shared English-heading adapter).
- Sample scope: original PDF 12--14, printed 2--4. All body material on these pages is included.
- Reconstructed English: `structured/reviewed/sample-restored-en.tex`.
- Chinese source: `tex/chapters/sample.tex`; aligned record: `structured/reviewed/sample.json`.
- Sample PDF: `output/sample-zh.pdf`.
- Page diagnosis and mapping: `qa/page-diagnosis.json`, `structured/source/page-map.json`.
- Integrity and sample QA: `qa/registration-integrity.json`, `qa/sample-qa.json`.

The scan has hidden OCR; its text is not mathematically authoritative. Only the
sample is restored and translated. No full-book OCR or translation has begun.
Template files are read-only. Existing other-book pending changes are preserved.
New terms are proposed book-local candidates, not global approvals.

The normal new-book command refused a dirty main checkout. The book-local
registration helper reused BookPaths/config/registry helpers with narrower,
user-authorized conflict checks; its first commit excludes existing edits.
The normal start-book entry uses an unconfigured global processor. This book
uses the existing `start_book(..., processor=...)` extension instead, without
changing shared automation. See `workflow/sample_workflow.py`.
''')
    print(json.dumps({'blocks':len(BLOCKS),'display_math':sum(f['kind']=='display' for f in formulae),
                      'inline_math':sum(f['kind']=='inline' for f in formulae),'candidates':len(candidates)}))


def processor(selected):
    assert selected.book_id == BOOK_ID
    source = book.require_source_pdf()
    source_before = sha256_file(source)
    template_before = directory_manifest_hash(book.template)
    body = (book.root / 'tex/chapters/sample.tex').read_text(encoding='utf-8')
    assert body == (book.root / 'translation/reviewed/sample.tex').read_text(encoding='utf-8')
    assert not find_chinese_prose_punctuation(body)
    labels = re.findall(r'\\label\{([^}]+)\}', body)
    refs = re.findall(r'\\(eqref|ref)\{([^}]+)\}', body)
    assert len(labels) == len(set(labels))
    assert all(label in labels for _, label in refs)
    assert not re.search(r'(?:Theorem|Lemma|Definition)\s+\d|\(1\.\d+\)', body)
    assert 'Picard-Lindelöf' in body and 'Lipschitz' in body and 'Gronwall' in body
    stage = Path(tempfile.mkdtemp(prefix='sample-build-', dir=book.root/'workspace/temporary'))
    env = os.environ.copy()
    env['TEXINPUTS'] = os.pathsep.join(str(book.template / p) for p in ['style','adapter','assets']) + os.pathsep
    env['BIBINPUTS'] = str(book.template / 'assets') + os.pathsep
    command = ['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
               '-jobname=sample-zh','-output-directory='+str(stage),'main.tex']
    runs = []
    for number in [1,2,3]:
        result = subprocess.run(command, cwd=book.root/'tex', env=env, capture_output=True)
        (book.root / f'logs/sample-pass-{number}.log').write_bytes(result.stdout+result.stderr)
        runs.append({'pass':number,'exit_code':result.returncode})
        assert result.returncode == 0, 'LaTeX failed; see logs and native sample-build log.'
    log = (stage / 'sample-zh.log').read_text(encoding='utf-8', errors='replace')
    failures = {key:re.findall(pattern, log, re.I) for key,pattern in {
        'undefined_references':r'LaTeX Warning: (?:Reference .* undefined|There were undefined references)',
        'duplicate_labels':r'multiply[- ]defined|destination with the same identifier',
        'missing_characters':r'Missing character:[^\n]*',
        'overfull_boxes':r'Overfull \\[hv]box[^\n]*'}.items()}
    assert not any(failures.values()), failures
    aux = (stage / 'sample-zh.aux').read_text(encoding='utf-8')
    expected = {'thm:ode-existence':'1.1','thm:inverse-function':'1.2',
        'thm:implicit-function':'1.3','thm:ode-uniqueness':'1.4',
        'eq:uniform-lipschitz-bound':'1.1','eq:ode-initial-value-dynamics':'1.2',
        'eq:ode-initial-value-data':'1.3','eq:ode-integral-equation':'1.4','eq:picard-iteration':'1.5'}
    for key,num in expected.items():
        assert r'\newlabel{'+key+'}{{'+num+'}' in aux, (key,num)
    pdf = PdfReader(stage / 'sample-zh.pdf')
    destinations = pdf.named_destinations
    links = []
    for page in pdf.pages:
        for ref in page.get('/Annots', []):
            annotation = ref.get_object()
            action = annotation.get('/A')
            if action and action.get('/S') == '/GoTo':
                target = str(action.get('/D'))
                assert target in destinations, target
                links.append(target)
    expected_anchors = []
    for _, label in refs:
        match = re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{[^{}]*\}\{[^{}]*\}\{[^{}]*\}\{([^{}]+)\}', aux)
        assert match, label
        expected_anchors.append(match.group(1))
    assert links == expected_anchors, (links, expected_anchors)
    assert all(re.search(r'\\newlabel\{'+re.escape(label)+r'\}.*',aux) for _,label in refs)
    assert source_before == sha256_file(source) == book.load_config()['source']['sha256']
    assert template_before == directory_manifest_hash(book.template) == book.load_config()['template_manifest_hash']
    assert not verify_manifest()
    baseline = json.loads((book.qa / 'registration-integrity.json').read_text(encoding='utf-8'))
    for name, digest in baseline['pending_files_before'].items():
        if name != 'shared/PROJECTS.md':
            assert sha256_file(ROOT/name) == digest, 'Unrelated pending file changed: '+name
    shutil.copy2(stage / 'sample-zh.pdf', book.root / 'output/sample-zh.pdf')
    target_rows = []
    for use in BLOCKS:
        rendered = emit(use, 'zh')
        block_offset = body.index(rendered)
        for match in re.finditer(r'\\(eqref|ref)\{([^}]+)\}', rendered):
            command_name, target = match.groups()
            owner = next(b for b in BLOCKS if b['label'] == target or (r'\label{'+target+'}') in b['english'])
            target_rows.append({'original_reference':expected[target], 'latex_label':target,
                'command':command_name,'target_object':owner['id'],'translation_block':use['id'],
                'translation_file':'tex/chapters/sample.tex',
                'translation_line':body.count('\n', 0, block_offset+match.start())+1})
    _write_json(book.qa / 'cross-reference-registry.json', {'references':target_rows,'expected_numbers':expected})
    _write_json(book.qa / 'compile-report.json', {'passes':runs,'checks':failures,
        'page_count':len(pdf.pages),'goto_links':links,'expected_anchors':expected_anchors,
        'link_sequence_matches_reference_sequence':True,'native_log':str(stage/'sample-zh.log'),
        'source_unchanged':True,'template_unchanged':True,'unrelated_pending_files_unchanged':True,
        'warnings':re.findall(r'(?:LaTeX|Package [^\n]+) Warning:[^\n]*',log),
        'scope':'Compilation, label values and named destination existence; visual formula review is a separate source review.'})
    # Visual output review is an explicit final step outside this processor.
    _write_json(book.qa / 'sample-qa.json', {'book_id':BOOK_ID,'passed':False,
        'source_review':'agent compared all three source-page images with reconstruction',
        'math_token_comparison':'source and translation math multisets equal per block; display sequence equal',
        'punctuation_violations':0,'name_violations':0,'unresolved_numbered_references':0,
        'blocking_issues':[], 'visual_output_review':'pending final render inspection',
        'scope':'Sample only. User approval not yet granted.'})


def run():
    selected_plan = json.loads((book.qa/'sample-plan.json').read_text(encoding='utf-8'))
    outcome = start_book(project, BOOK_ID, processor=processor)
    selected_plan['generic_page_suggestions_superseded'] = outcome['sample_pages']
    _write_json(book.qa/'sample-plan.json', selected_plan)
    # start_book's generic category-first page suggestions are deliberately
    # superseded by the visually selected continuous sample, not treated as QA.
    state = json.loads(book.workflow_state.read_text(encoding='utf-8'))
    state.update(sample_pages=PAGES, generic_page_suggestions=outcome['sample_pages'],
                 status='sample-visual-review', completed_units=[], blocking_issues=[])
    _write_json(book.workflow_state, state)
    write(book.status_file, _book_status_text(BOOK_ID,'sample','sample-visual-review',
                                             book.load_config()['source']['sha256'],[]))
    config = book.load_config()
    config.update(phase='sample', status='sample-visual-review')
    _write_json(book.config_file, config)
    current = project_record(project, BOOK_ID)
    current.phase, current.status = 'sample', 'sample-visual-review'
    update_project_record(project, current)
    print(json.dumps({'book_id':BOOK_ID,'sample_pages':PAGES,'status':'sample-visual-review',
                      'pdf':str(book.root/'output/sample-zh.pdf')},indent=2))


if __name__ == '__main__':
    if '--prepare' in sys.argv:
        prepare()
    elif '--rebuild' in sys.argv:
        processor(book)
    else:
        run()
