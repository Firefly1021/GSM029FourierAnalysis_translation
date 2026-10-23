"""Final mechanical pass from the committed AJbook baseline, not the retired user-edited source."""
import json,subprocess,sys
from pathlib import Path
from prepare_feec_production import clean,BOOK,AUDIT,STAGE,ROOT
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import sha256_file

plan=json.loads((AUDIT/'plan.json').read_text(encoding='utf8'));rows=[]
for row in plan['formatting']:
    original=subprocess.check_output(['git','-C',str(ROOT),'show',plan['source_baseline_head']+':books/finite-element-exterior-calculus/'+row['old']]).decode('utf8')
    cleaned,stats=clean(original)
    (BOOK/row['new']).write_bytes(cleaned.encode('utf8'))
    (STAGE/row['new']).write_bytes(cleaned.encode('utf8'))
    rows.append({'old':row['old'],'new':row['new'],**stats})
result={'formatting':rows,'effective_prepared_files':[{'path':p.relative_to(STAGE).as_posix(),'bytes':p.stat().st_size,'sha256':sha256_file(p)} for p in sorted(STAGE.rglob('*')) if p.is_file()]}
(AUDIT/'polish-plan.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({key:sum(row[key] for row in rows) for key in rows[0] if key not in {'old','new'}},ensure_ascii=False),flush=True)
