"""Plan completed-book presentation; immutable content is fingerprinted first."""
import collections,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'shared/qa/completed-view-20261022'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths,sha256_file,run_git
from mathbook.workflow import read_projects

def main():
    project=ProjectPaths(ROOT);books=[]
    for record in read_projects(project):
        assert record.status in {'complete','completed'},'Only completed editions may be compacted.'
        book=project.book(record.book_id)
        assert not book.delivered,'Already delivered; refuse a second migration.'
        moves=[];mapping={};deletions=[];inventory=[]
        for name in ('config','formulae','glossary','qa','structured','translation','archive','PLANS.md','PROJECT_STATUS.md','TYPESETTING.md'):
            path=book.root/name
            if path.exists():
                moves.append({'from':name,'to':'records/'+name});mapping[name]='records/'+name
        if (book.root/'workspace/crops').is_dir():
            moves.append({'from':'workspace/crops','to':'records/crops'});mapping['workspace/crops']='records/crops'
        keep_hashes={}
        for base in (book.root/'tex',book.root/'translation/final',book.root/'translation/reviewed'):
            if base.is_dir():
                for path in sorted(base.rglob('*')):
                    if path.is_file() and path.name!='.gitkeep':
                        keep_hashes.setdefault(sha256_file(path),path.relative_to(book.root).as_posix())
        all_files=[]
        for current,dirs,files in os.walk(book.root):
            for name in dirs:assert not Path(current,name).is_symlink()
            all_files.extend(Path(current,name) for name in files)
        for path in sorted(all_files):
            assert not path.is_symlink()
            relative=path.relative_to(book.root).as_posix();new=relative
            for old,destination in sorted(mapping.items(),key=lambda kv:len(kv[0]),reverse=True):
                if relative==old or relative.startswith(old+'/'):
                    new=destination+relative[len(old):];break
            digest=sha256_file(path);reason=None;duplicate_of=None
            if relative.startswith(('logs/','workflow/','.vscode/')) or relative=='OPEN-THIS-BOOK.md':
                reason='Retired scaffold/editor wrapper; the new README/shared task is the single entry.'
            elif relative.startswith('workspace/') and not relative.startswith('workspace/crops/'):
                reason='Remaining retired cache/marker; no formal TeX content is stored here.'
            elif new.startswith('records/') and path.name=='.gitkeep':
                reason='Empty process-directory marker is unnecessary in a completed edition.'
            elif relative.startswith('translation/'):
                duplicate_of=keep_hashes.get(digest)
                if duplicate_of and duplicate_of!=relative:
                    reason='Byte-identical translation duplicate; canonical survivor retained.'
            row={'from':relative,'to':new,'bytes':path.stat().st_size,'sha256':digest}
            inventory.append(row)
            if reason:deletions.append({**row,'reason':reason,'duplicate_of':duplicate_of})
        delete_keys={r['from'] for r in deletions}
        # A survivor must never itself be selected for deletion.
        for row in deletions:
            if row['duplicate_of']:assert row['duplicate_of'] not in delete_keys,(row,delete_keys)
        removals=[]
        grouped=set()
        for name in ('workspace','logs','workflow','.vscode'):
            folder=book.root/name
            if not folder.is_dir():continue
            rows=[r for r in deletions if r['from'].startswith(name+'/') and not r['from'].startswith('workspace/crops/')]
            actual=[p.relative_to(book.root).as_posix() for p in folder.rglob('*') if p.is_file()]
            # Crops move first, so they are deliberately excluded from the workspace remainder.
            remaining=[name for name in actual if not name.startswith('workspace/crops/')]
            assert set(remaining)=={r['from'] for r in rows},folder
            removals.append({'path':name,'files':len(rows),'bytes':sum(r['bytes'] for r in rows)})
            grouped.update(r['from'] for r in rows)
        removals.extend({'path':r['to'],'files':1,'bytes':r['bytes']} for r in deletions if r['from'] not in grouped)
        for row in deletions:
            if row['duplicate_of']:
                survivor=row['duplicate_of']
                if survivor.startswith('translation/'):survivor='records/'+survivor
                mapping[row['from']]=survivor
                mapping[row['to']]=survivor
        books.append({'book_id':record.book_id,'moves':moves,'path_map':mapping,'inventory':inventory,
            'deletions':deletions,'removals':removals,'root_before':sorted(p.name for p in book.root.iterdir()),
            'binding':json.loads(book.binding_file.read_text(encoding='utf8'))})
    result={'library_root':str(ROOT),'checkpoint':project.git_head(),'books':books,
        'scope':'Completed-book presentation and exact-duplicate/cache cleanup; immutable TeX/source/template/output bytes preserved.'}
    REPORT.mkdir(parents=True,exist_ok=True)
    (REPORT/'plan.json').write_text(json.dumps(result,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
    print(json.dumps({'books':len(books),'delete_files':sum(len(b['deletions']) for b in books),
        'delete_bytes':sum(r['bytes'] for b in books for r in b['deletions']),
        'duplicates':sum(bool(r['duplicate_of']) for b in books for r in b['deletions'])},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
