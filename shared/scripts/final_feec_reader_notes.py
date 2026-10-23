"""Remove only two non-source process notes, then verify final publication."""
import hashlib,json,sys,subprocess,io,shutil
from pathlib import Path
from PIL import Image,ImageChops
from pypdf import PdfReader
from prepare_feec_production import BOOK,AUDIT,ROOT,math_spans
from audit_feec_production import link_audit,labels,raster
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import sha256_file,ProjectPaths
from mathbook.library import build_book

notes={
 'tex/backmatter/bibliography.tex':'文献条目及原书引页元数据保留原文. 以下括号中 Cited on 的页码为原书印刷页码, 不是译本页码.',
 'tex/backmatter/index.tex':r'\indexprologue{保留原书条目的次序和层级. 链接定位译本中包含相应内容的章节或具名对象; 原书印刷页码另存于结构化索引登记表, 不充作译本页码.}'
}
polish=json.loads((AUDIT/'polish-plan.json').read_text(encoding='utf8'))
for name,note in notes.items():
    path=BOOK/name;after=path.read_bytes();lines=after.decode('utf8').splitlines(keepends=True)
    reconstructed=''.join(lines[:1]+[note+'\n']+lines[1:]).encode('utf8')
    row=next(r for r in polish['effective_prepared_files'] if r['path']==name)
    assert hashlib.sha256(reconstructed).hexdigest()==row['sha256'],'Unexpected additional source edit'
    assert [v for _,_,v in math_spans(reconstructed.decode('utf8'))]==[v for _,_,v in math_spans(after.decode('utf8'))]
    row.update(bytes=len(after),sha256=sha256_file(path))
polish['explicit_process_notes_removed']=notes
(AUDIT/'polish-plan.json').write_text(json.dumps(polish,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
result=build_book(ProjectPaths(),'finite-element-exterior-calculus',driver=Path(r'C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py'))
(AUDIT/'production-build.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for name in ('undefined_references','duplicate_labels','missing_glyphs','overfull_boxes'):assert not result['warnings'][name]
before=PdfReader(AUDIT/'intermediate-reader-notes.pdf');after=PdfReader(result['candidate_pdf'])
assert len(before.pages)==len(after.pages)==139
assert set(before.named_destinations)==set(after.named_destinations)
links=link_audit(after);assert links['internal_links']==753 and not links['unresolved_named_destinations']
numbers=labels(Path(result['build_directory'])/'main.aux');assert len(numbers)==537
verification=json.loads((AUDIT/'verification.json').read_text(encoding='utf8'))
verification.update(explicit_process_notes_removed=notes,production_links=links,new_pdf_sha256=sha256_file(Path(result['candidate_pdf'])),
    reference_anchor_set_unchanged_after_non_counter_note_removal=True,reference_label_number_map=numbers,warnings=result['warnings'])
samples=[1,23,24,69,138,139]
for page in samples:
    image=raster(result['candidate_pdf'],page);image.save(AUDIT/f'visual/production-{page}.png')
    if page in (1,23,24,69):
        old=raster(AUDIT/'intermediate-reader-notes.pdf',page)
        assert old.size==image.size and ImageChops.difference(old,image).getbbox() is None
(AUDIT/'verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Verified: only the two explicit process notes removed; original body/math/anchors unchanged.',flush=True)
