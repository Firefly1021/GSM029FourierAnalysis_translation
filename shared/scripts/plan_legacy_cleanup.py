"""Audit redundant migration copies and archive caches before native cleanup."""
import hashlib,json,os,subprocess,sys,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'shared/qa/integration-20261022'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths
from mathbook.workflow import verify_book_context

def digest(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def main():
    targets=[];notes=[]
    backup=ROOT/'shared/.migration-backup/main-books'
    removable=[];retained=[]
    if backup.is_dir():
        tracked=set(subprocess.check_output(['git','-C',str(ROOT),'ls-tree','-r','--name-only','e70714f','--','books'],text=True).splitlines())
        for path in backup.rglob('*'):
            if not path.is_file():continue
            relative=path.relative_to(backup).as_posix();parts=relative.split('/')
            original='books/'+relative;canonical=ROOT/original
            reason=None
            if len(parts)>1 and parts[1] in {'workspace','logs'}:reason='Reproducible historical cache/log.'
            elif canonical.is_file() and digest(path)==digest(canonical):reason='Exact duplicate of current retained book file.'
            elif original in tracked:
                data=subprocess.check_output(['git','-C',str(ROOT),'show','e70714f:'+original])
                variants=[data,data.replace(b'\r\n',b'\n'),data.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')]
                if digest(path) in {hashlib.sha256(v).hexdigest() for v in variants}:reason='Exact historical Git content recoverable at e70714f.'
            if reason is None:
                book,_=verify_book_context(ProjectPaths(ROOT),parts[0],writable=True)
                destination=book.assert_write_path(book.root/'archive/pre-integration-main'/Path(*parts[1:]))
                destination.parent.mkdir(parents=True,exist_ok=True)
                original_hash=digest(path)
                if destination.exists():assert digest(destination)==original_hash
                else:shutil.copy2(path,destination)
                assert digest(path)==digest(destination)==original_hash
                reason='Unique original-main file preserved byte-exact under '+destination.relative_to(ROOT).as_posix()
                retained.append({'path':destination.relative_to(ROOT).as_posix(),'sha256':original_hash})
            row={'path':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'reason':reason}
            (removable if reason else retained).append(row)
        if all(r['reason'] for r in removable):
            targets.append({'path':backup.relative_to(ROOT).as_posix(),'files':len(removable),'bytes':sum(r['bytes'] for r in removable)})
        else:
            targets.extend({'path':r['path'],'files':1,'bytes':r['bytes']} for r in removable)
        notes.append({'backup_files_removable':len(removable),'unique_files_preserved_in_own_book':retained})
    for archive in sorted((ROOT/'shared/.legacy-worktrees').iterdir()):
        if not archive.is_dir():continue
        status=subprocess.check_output(['git','-C',str(archive),'status','--porcelain=v1'],text=True)
        assert status.strip() in {'','?? uv.lock'},(archive,status)
        notes.append({'worktree':archive.name,'status':status,'head':subprocess.check_output(['git','-C',str(archive),'rev-parse','HEAD'],text=True).strip()})
        # Only ignored caches/virtual environments, never the real worktree or tracked source.
        candidates=[archive/'.venv',archive/'out']
        book=archive/'books'/archive.name
        for name in ('pages','raw-text','layout','formula-images','temporary'):
            base=book/'workspace'/name
            if base.is_dir():candidates.extend(base.iterdir())
        for target in candidates:
            if not target.exists():continue
            relative=target.relative_to(archive).as_posix()
            if target.name=='.gitkeep':continue
            tracked=subprocess.check_output(['git','-C',str(archive),'ls-files','--',relative],text=True)
            if tracked.strip():continue
            ignored=subprocess.run(['git','-C',str(archive),'check-ignore','-q','--',relative])
            if ignored.returncode:continue
            files=[p for p in target.rglob('*') if p.is_file()] if target.is_dir() else [target]
            if not files:continue
            targets.append({'path':target.relative_to(ROOT).as_posix(),'files':len(files),'bytes':sum(p.stat().st_size for p in files)})
    plan={'library_root':str(ROOT),'authorization':'user-request-20261022-remove-completed-book-intermediates',
          'allowed_prefixes':['shared/.migration-backup/main-books','shared/.legacy-worktrees/'],
          'targets':targets,'notes':notes}
    (REPORT/'legacy-cleanup-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'targets':len(targets),'files':sum(t['files'] for t in targets),'bytes':sum(t['bytes'] for t in targets),'notes':notes},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
