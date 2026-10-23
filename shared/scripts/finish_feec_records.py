"""Finish administrative evidence outside the production book directory."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];AUDIT=ROOT/'shared/qa/feec-production-20261023'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import read_projects,write_projects

project=ProjectPaths(ROOT);book=project.book('finite-element-exterior-calculus')
plan=json.loads((AUDIT/'plan.json').read_text(encoding='utf8'))
polish=json.loads((AUDIT/'polish-plan.json').read_text(encoding='utf8'))
verification=json.loads((AUDIT/'verification.json').read_text(encoding='utf8'))
publication=json.loads((AUDIT/'publication.json').read_text(encoding='utf-8-sig'))
assert verification['passed'] and not book.build_cache.exists()
for row in polish['effective_prepared_files']:assert sha256_file(book.root/row['path'])==row['sha256']
originals={row['path']:row for row in plan['inventory']}
retained_upstream=[]
for name in plan['upstream_files_kept_byte_exact']:
    old='template/collections/aljabr-1/upstream/'+name
    assert sha256_file(book.template/name)==originals[old]['sha256']
    retained_upstream.append(name)
for path in (book.template/'fonts/noto-sans-cjk-sc').iterdir():
    old='template/collections/aljabr-1/fonts/noto-sans-cjk-sc/'+path.name
    assert sha256_file(path)==originals[old]['sha256']
config=book.load_config();config.update(template_manifest_hash=directory_manifest_hash(book.template),template_version='AJbook-feec-production-20261023')
book.config_file.write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
rows=read_projects(project)
for row in rows:
    if row.book_id==book.book_id:row.template_version=config['template_version']
write_projects(project,rows)
record=json.loads((book.qa/'unified-build.json').read_text(encoding='utf8'))
record.update(published=True,published_pdf=str(book.root/'output/book-aljabr-zh.pdf'),verification_cache_removed=True,candidate_and_log_paths_are_historical=True)
(book.qa/'unified-build.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
verification.update(upstream_class_font_and_titles_files_byte_unchanged=retained_upstream,
    official_noto_files_byte_unchanged=True,publication=publication,
    formatting_totals={key:sum(row[key] for row in polish['formatting']) for key in polish['formatting'][0] if key not in {'old','new'}},
    final_book_root=sorted(p.name for p in book.root.iterdir()),
    final_book_files=sum(p.is_file() for p in book.root.rglob('*')),
    uncommitted_legacy_edit_discarded_per_user=True,remote_push=False)
(AUDIT/'verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'files':verification['final_book_files'],'root':verification['final_book_root'],'pdf_sha256':publication['sha256'],'upstream_preserved':retained_upstream},ensure_ascii=False),flush=True)
