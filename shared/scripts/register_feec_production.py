"""Register the audited, AJbook-only publication profile."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths,directory_manifest_hash

book=ProjectPaths(ROOT).book('finite-element-exterior-calculus')
assert book.records==ROOT/'shared/book-records/finite-element-exterior-calculus'
binding=json.loads(book.binding_file.read_text(encoding='utf8'))
binding.update(entry='tex/main.tex',fonts='template/fonts/noto-sans-cjk-sc',
    template_hash=directory_manifest_hash(book.template),build_template_hash=directory_manifest_hash(book.template),
    note='AJbook-only production sources. Translation-process metadata is kept outside books; the former Mystyle source was explicitly removed by the user.')
book.binding_file.write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
mapping_path=book.records/'path-map.json'
mapping=json.loads(mapping_path.read_text(encoding='utf8'))
plan=json.loads((ROOT/'shared/qa/feec-production-20261023/plan.json').read_text(encoding='utf8'))
for item in plan['formatting']:
    mapping['moved'][item['old']]=item['new']
mapping['moved']['tex/aljabr-main.tex']='tex/main.tex'
mapping_path.write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Registered AJbook-only production source:',binding['entry'],flush=True)
