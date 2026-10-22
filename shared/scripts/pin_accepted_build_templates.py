"""Recover historical accepted templates, never edit supplied current templates."""
import hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import directory_manifest_hash

def main():
    results=[]
    for book_id in ('navier-stokes-equations-theory-and-numerical-analysis','the-mathematical-theory-of-finite-element-methods'):
        book=ROOT/'books'/book_id
        manifest=json.loads((book/'config/template-snapshot-manifest.json').read_text(encoding='utf8'))
        binding_path=book/'config/library-binding.json'
        binding=json.loads(binding_path.read_text(encoding='utf8'))
        recovered=[]
        for row in manifest['files']:
            data=subprocess.check_output(['git','-C',str(ROOT),'show','d012545:'+row['path']])
            candidates=[data,data.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')]
            matched=[value for value in candidates if hashlib.sha256(value).hexdigest()==row['sha256']]
            assert matched,'Cannot recover exact manifest bytes: '+row['path']
            target=book/'template-accepted'/Path(row['path']).relative_to('template')
            target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==matched[0]
            else:target.write_bytes(matched[0])
            recovered.append({'path':str(target.relative_to(book)),'sha256':row['sha256']})
        binding.update(build_template='template-accepted',build_template_hash=directory_manifest_hash(book/'template-accepted'),
            build_template_reason='Exact original acceptance-manifest bytes recovered from d012545; later user template remains untouched in template/.')
        binding_path.write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        results.append({'book_id':book_id,'original_manifest_fully_matched':True,'files':recovered,'build_template_hash':binding['build_template_hash']})
    (ROOT/'shared/qa/integration-20261022/accepted-template-recovery.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(results,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
