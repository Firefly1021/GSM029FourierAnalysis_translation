"""Record completed agent sample QA; explicitly do NOT approve full translation."""
from __future__ import annotations

import base64
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths, sha256_file, directory_manifest_hash
from mathbook.workflow import (verify_book_context, _write_json, _book_status_text,
                              read_projects, update_project_record, project_record)
from mathbook.qa import find_chinese_prose_punctuation
from mathbook.template import verify_manifest

BOOK_ID = 'an-introduction-to-partial-differential-equations'
project = ProjectPaths(ROOT)
book, record = verify_book_context(project, BOOK_ID, writable=True)


def text(relative, content):
    path = book.assert_write_path(book.root/relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def finalize():
    # Explicit attestation follows visual inspection of all three rendered output
    # pages and all three original scan pages, performed in the active task.
    assert '--visual-review-completed' in sys.argv
    assert '--renders-identical-to-reviewed' in sys.argv
    compile_report = json.loads((book.qa/'compile-report.json').read_text(encoding='utf-8'))
    assert len(compile_report['passes']) >= 2
    assert all(p['exit_code']==0 for p in compile_report['passes'])
    assert not any(compile_report['checks'].values())
    assert compile_report['link_sequence_matches_reference_sequence']
    source = book.require_source_pdf()
    config = book.load_config()
    assert sha256_file(source) == sha256_file(Path(config['source']['original_path'])) == config['source']['sha256']
    assert not verify_manifest()
    assert directory_manifest_hash(book.template) == config['template_manifest_hash']
    for rel in ['style/Mystyle.sty','reference/main.tex']:
        assert sha256_file(book.template/rel) == sha256_file(project.template/rel)
    baseline = json.loads((book.qa/'registration-integrity.json').read_text(encoding='utf-8'))
    for name, digest in baseline['pending_files_before'].items():
        if name != 'shared/PROJECTS.md':
            assert sha256_file(ROOT/name) == digest, name
    old_registry = base64.b64decode(baseline['registry_working_copy_before_base64']).decode('utf-8')
    old_rows = {line.split('|')[1].strip(): line.strip() for line in old_registry.splitlines()
                if line.startswith('|') and 'Book ID' not in line and not line.startswith('|---')}
    for row in read_projects(project):
        if row.book_id != BOOK_ID:
            assert '| ' + ' | '.join(row.cells()) + ' |' == old_rows[row.book_id]
    qa = json.loads((book.qa/'sample-qa.json').read_text(encoding='utf-8'))
    qa.update(passed=True, visual_output_review={
        'reviewer':'Codex agent', 'pages':[1,2,3],
        'result':'All output pages rendered and visually inspected; final clean-build raster hashes match reviewed renders.',
        'checks':['no clipped text','no overlapping equations','matrix diagonal ellipses present',
                  'Theorem headings in English','source numbering retained',
                  'Theorem 1.3 continues on next page without lost text']},
        user_approved=False, status='awaiting-sample-approval')
    _write_json(book.qa/'sample-qa.json', qa)
    state = json.loads(book.workflow_state.read_text(encoding='utf-8'))
    state.update(status='awaiting-sample-approval', sample_pages=[12,13,14],
                 completed_units=['representative-sample-only'], blocking_issues=[],
                 sample_approved=False, full_translation_started=False)
    _write_json(book.workflow_state, state)
    text('PROJECT_STATUS.md', _book_status_text(BOOK_ID, 'sample', 'awaiting-sample-approval',
                                              config['source']['sha256'], [])+
         'Active branch: main\nCheckpoint branch: book/'+BOOK_ID+
         '\nSample source: PDF 12--14 / printed 2--4\nSample PDF: output/sample-zh.pdf\n'
         'User sample approval: Not yet granted\nFull translation started: No\n')
    config.update(phase='sample', status='awaiting-sample-approval',
                  sample_output='output/sample-zh.pdf', sample_source_pdf_pages=[12,13,14],
                  source_type='predominantly scanned with hidden OCR', sample_approved=False)
    _write_json(book.config_file, config)
    record = project_record(project, BOOK_ID)
    record.phase, record.status = 'sample', 'awaiting-sample-approval'
    # A sample is not the final full-book output.
    record.final_output = ''
    update_project_record(project, record)
    text('PLANS.md', '''# Sample checkpoint

Completed: local registration, source/template SHA-256 binding, all-page PDF
diagnosis, sample page mapping, raw hidden OCR retention, scan-based English
restoration, formula/provenance registration, terminology lookup, faithful Chinese
sample, label/reference QA, ASCII punctuation/name QA, clean three-pass XeLaTeX
build, and visual inspection of all three output pages.

Stop: awaiting-sample-approval. Do not translate the rest of Chapter 1 or any
other chapter until the user explicitly approves the sample.

After approval: retain the scan-aware source-restoration layer. Inspect ambiguous
PDF pages 71, 73, 114 and 341 and scan pages 90 and 122 before using their OCR.
The page-minus-10 mapping is verified only in the sample, not presumed globally.
Do not regenerate accepted material, edit templates, silently approve terms,
translate environment names, change mathematical notation, or push remotely.
''')
    with book.chapter_progress.open('w', encoding='utf-8', newline='') as handle:
        writer=csv.writer(handle, delimiter='\t', lineterminator='\n')
        writer.writerow(['Unit','Source PDF pages','Printed pages','Status','Scope'])
        writer.writerow(['sample','12--14','2--4','qa-passed-awaiting-user-approval','sample only'])
        for ch in range(1,13):
            writer.writerow([f'chapter-{ch:02d}','','','not-started' if ch!=1 else 'sample-only-not-complete','No full chapter accepted'])
    issues = [
        {'id':'scan-ocr-reliability','severity':'warning','category':'extraction',
         'review_status':'open','scope':'full-book','message':'Hidden OCR is not authoritative; every translated block requires scan verification.'},
        {'id':'deferred-problem-pages','severity':'warning','category':'extraction',
         'review_status':'open','scope':'outside-sample','pdf_pages':[71,73,90,114,122,341],
         'message':'Four partial-image/mixed candidates and two pages without extracted text require targeted diagnosis before their translation.'},
        {'id':'printed-page-map','severity':'warning','category':'provenance','review_status':'open',
         'scope':'outside-sample','message':'Only PDF 12--14 <-> printed 2--4 verified. Other body offsets are candidates; frontmatter needs its own mapping.'},
        {'id':'source-piecewise-open-endpoint','severity':'info','category':'formula','review_status':'recorded',
         'pdf_page':14,'printed_page':4,'message':'Preserved source 0<t<=gamma exactly; no mathematical correction inferred.'},
        {'id':'source-acroform-metadata','severity':'info','category':'source-pdf','review_status':'recorded',
         'message':'Poppler reports missing AcroForm Fields array while rendering original PDF. Sample pages and title rendered successfully; source not repaired.'},
    ]
    text('qa/issues.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in issues))
    blocks=json.loads((book.root/'structured/reviewed/sample.json').read_text(encoding='utf-8'))['blocks']
    count=0
    for block in blocks:
        assert not find_chinese_prose_punctuation(block['chinese'])
        count+=1
    references=json.loads((book.qa/'cross-reference-registry.json').read_text(encoding='utf-8'))['references']
    text('qa/translation/punctuation-report.md', f'''# Chinese prose punctuation

Shared protected-context checker applied to {count} aligned blocks and final TeX.
Forbidden full-width prose punctuation: 0. No templates, mathematics, label keys,
reference keys, paths or source English were rewritten by punctuation QA.
''')
    text('qa/translation/cross-reference-report.md', f'''# Cross-reference QA

Five numbered equations and four Theorem objects retain source numbering through
LaTeX counters, never literal reference numbers in the Chinese prose. References
use eqref/ref. The registry records every occurrence, target and translation line.
All {len(references)} GoTo link targets match the expected aux anchors in reading order.
Undefined references: 0. Duplicate labels: 0. Unresolved numbered targets: 0.
Unnumbered original displays remain unnumbered; they have stable formula registry
IDs rather than fabricated equation numbers. Generic prose pointers to later
discussion remain prose and are not converted into guessed numbered targets.
''')
    text('qa/formula/restoration-report.md', '''# Formula restoration

16 displayed formula regions and 38 inline math regions registered. All were
agent-reviewed against the scan. High confidence: 54; low confidence: 0.
Inline crop bounding boxes identify their parent blocks, not individual tokens.
Checks include bold vectors versus scalar components, both Jacobian matrices,
diagonal and vertical ellipses, upper/lower integral limits, t-minus/t-plus,
membership/subset signs, hats, strict versus weak inequalities, 1/3 and 3/2
exponents, and all five equation numbers. No mathematical error correction made.
Source/translation math multisets match per block; displayed formulas match in
order. These automated comparisons do not replace the recorded scan inspection.
Independent human sample approval is pending.
''')
    text('qa/structure-report.md', '''# Structure review

The OCR contents on PDF 5--10 identify twelve chapters: Introduction;
Characteristics; Conservation Laws and Shocks; Maximum Principles; Distributions;
Function Spaces; Sobolev Spaces; Operator Theory; Linear Elliptic Equations;
Nonlinear Elliptic Equations; Energy Methods for Evolution Problems; Semigroup
Methods; followed by References. This is an outline, not restored chapter text.
All-page section-heading candidates retain OCR uncertainty in
structured/source/heading-candidates.json.

Sample: 24 aligned source/translation blocks, four Theorem environments, one
cross-page theorem, one cross-page iterative-construction paragraph. No formal
Proof, Definition, Lemma, Proposition, Corollary, Example, Remark, Exercise,
figure, table or footnote heading occurs in this sample; none was invented.
The two proof-discussion paragraphs remain ordinary prose, not formal Proof.
''')
    text('qa/problem-page-report.md', '''# Problem pages and limitations

Sample PDF 12--14 / printed 2--4: all body material reconstructed and visually
checked. No blocking unreadable sample formula or prose remains.
Outside sample, PDF 90 and 122 have no extracted text; PDF 71, 73, 114 and 341
have partial-image/mixed candidates. These six pages are NOT cleared for future
translation. Whole-book diagnostics are not whole-book source reconstruction.
''')
    text('qa/sample-report.md', '''# Representative sample QA

Status: awaiting-sample-approval. Agent sample QA passed; no human approval yet.

- Source: PDF 12--14, printed 2--4; 24 aligned blocks.
- Source type: scan with hidden, unreliable OCR, not reliable native text.
- English reconstruction: structured/reviewed/sample-restored-en.tex.
- Chinese source: tex/chapters/sample.tex; compiled sample: output/sample-zh.pdf.
- 16 displayed / 38 inline math regions; no low-confidence sample regions.
- Four English Theorem headings. No invented formal Proof or Example headings.
- Five numbered equations and four Theorem numbers checked in aux data.
- Six actual PDF links match their expected equation/Theorem anchors.
- Final clean build: three successful XeLaTeX passes; no undefined references,
  duplicate labels, missing glyphs or overfull boxes. See compile-report.json.
- All three output pages visually inspected, including cross-page Theorem 1.3.
- Nine book-local proposed terms; zero ambiguous unresolved terms. Global glossary unchanged.
- Original PDF and pinned/shared templates unchanged; pre-existing dirty files preserved.

Non-blocking warnings outside the sample remain in issues.jsonl. Review does not
claim all 444 pages have correct OCR or verified page-number mapping. No full
chapter translation or remote push was performed.
''')
    receipts = [book.main_tex,book.root/'tex/chapters/sample.tex',
                book.root/'structured/reviewed/sample-restored-en.tex',
                book.root/'structured/reviewed/sample.json',book.root/'formulae/sample-registry.json',
                book.root/'output/sample-zh.pdf']
    _write_json(book.qa/'sample-receipt.json', {'source_sha256':config['source']['sha256'],
        'files':{p.relative_to(book.root).as_posix():sha256_file(p) for p in receipts},
        'template_manifest_hash':config['template_manifest_hash'],'other_pending_files_preserved':True,
        'old_registry_rows_preserved':True,'remote_write':False,'full_translation_started':False})
    print(json.dumps({'book_id':BOOK_ID,'status':'awaiting-sample-approval',
                      'blocking_issues':0,'unresolved_terminology':0,'proposed_terms':9}))


def checkpoint():
    def git(*args,data=None):
        return subprocess.run(['git','-C',str(ROOT),*args],input=data,
                              capture_output=True,check=True).stdout
    assert not git('diff','--cached','--name-only').strip()
    git('add','--','books/'+BOOK_ID)
    head=git('show','HEAD:shared/PROJECTS.md').decode('utf-8')
    current=next(row for row in read_projects(project) if row.book_id==BOOK_ID)
    line='| '+' | '.join(current.cells())+' |'
    pattern=r'^\| '+re.escape(BOOK_ID)+r' \|.*$'
    staged,number=re.subn(pattern,lambda m:line,head,flags=re.M)
    assert number==1
    blob=git('hash-object','-w','--stdin',data=staged.encode('utf-8')).decode().strip()
    git('update-index','--cacheinfo','100644,'+blob+',shared/PROJECTS.md')
    paths=git('diff','--cached','--name-only').decode().splitlines()
    assert all(p.startswith('books/'+BOOK_ID+'/') or p=='shared/PROJECTS.md' for p in paths)
    git('commit','-m','Complete scan-verified PDE sample and await sample approval')
    print('Sample checkpoint:',git('rev-parse','HEAD').decode().strip())


if __name__=='__main__':
    finalize()
    if '--checkpoint' in sys.argv:
        checkpoint()
