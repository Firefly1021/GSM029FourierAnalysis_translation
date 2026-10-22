"""One-shot, journaled relocation; preserve every input byte and all Git refs."""
import argparse, hashlib, json, os, shutil, subprocess, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

ROOT=Path(r'D:\CelianFile\BOOKTRANSLATION')
OLD=Path(r'D:\CelianFile\BOOKTRANSLATION-worktrees')
SHARED=ROOT/'shared'
REPORT=SHARED/'qa/integration-20261022'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args],text=True,encoding='utf8').strip()

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(4*1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def inside(path,parent):
    path=path.resolve();path.relative_to(parent.resolve());return path

def copy_verified(src,dst,label):
    assert src.is_dir(),src
    rows=[];files=sorted(p for p in src.rglob('*') if p.is_file())
    print('COPY',label,len(files),'files',flush=True)
    dst=inside(dst,ROOT)
    def one(path):
        assert not path.is_symlink(),path
        rel=path.relative_to(src);target=dst/rel
        assert '..' not in rel.parts
        target.parent.mkdir(parents=True,exist_ok=True)
        before=sha(path)
        if not target.is_file() or path.stat().st_size!=target.stat().st_size or sha(target)!=before:
            shutil.copy2(path,target)
        assert before==sha(target)==sha(path),path
        return {'path':rel.as_posix(),'bytes':path.stat().st_size,'sha256':before}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for index,row in enumerate(pool.map(one,files),1):
            rows.append(row)
            if index%5000==0:print('VERIFIED',label,index,'/',len(files),flush=True)
    # Preserve empty directories too, without fabricating data.
    for directory,_,_ in os.walk(src):
        inside(dst/Path(directory).relative_to(src),ROOT).mkdir(parents=True,exist_ok=True)
    return rows

def relocate_caches(checkout,book_id,dest):
    """Rename ignored caches on one volume; preserve NTFS file identities."""
    journal=REPORT/(book_id+'-cache-moves.json')
    rows=json.loads(journal.read_text(encoding='utf8')) if journal.exists() else []
    for name in ('pages','temporary','raw-text','layout','formula-images'):
        relative='workspace/'+name
        if any(row['relative']==relative for row in rows):continue
        prefix='books/'+book_id+'/'+relative
        tracked=subprocess.check_output(['git','-C',str(checkout),'ls-files','--',prefix],text=True).splitlines()
        if any(path!=prefix+'/.gitkeep' for path in tracked):continue
        source=checkout/'books'/book_id/relative;target=dest/relative
        if not source.is_dir():continue
        assert source.stat().st_dev==ROOT.stat().st_dev
        files=[]
        for directory,_,names in os.walk(source):
            for filename in names:
                path=Path(directory)/filename
                if path==source/'.gitkeep':continue
                assert not path.is_symlink(),path
                st=path.stat();assert st.st_ino,'Filesystem has no stable identity; use verified copying.'
                files.append({'path':path.relative_to(source).as_posix(),'bytes':st.st_size,
                    'device':st.st_dev,'file_id':st.st_ino,'mtime_ns':st.st_mtime_ns})
        quarantine=inside(SHARED/'.migration-backup/partial-cache-copies'/book_id/name,ROOT)
        if target.exists():
            assert not quarantine.exists();quarantine.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(target),str(quarantine))
        target.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(source),str(target))
        source.mkdir()
        if (target/'.gitkeep').exists():shutil.copy2(target/'.gitkeep',source/'.gitkeep')
        for item in files:
            st=(target/item['path']).stat()
            assert (st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)==(item['device'],item['file_id'],item['bytes'],item['mtime_ns'])
        rows.append({'relative':relative,'method':'Same-volume rename; stable file identity/size/mtime verified; tracked directory marker restored in historical checkout',
            'files':files,'count':len(files),'bytes':sum(r['bytes'] for r in files)})
        save(journal,rows);print('CACHE RELOCATED',book_id,name,len(files),'files',flush=True)
    return rows

def prepare():
    assert git('branch','--show-current')=='codex/consolidate-library'
    resuming=(REPORT/'before.json').exists()
    entries=[]
    for line in git('worktree','list','--porcelain').splitlines():
        if line.startswith('worktree '):entries.append(Path(line[9:]))
    books=[]
    for checkout in entries:
        branch=subprocess.check_output(['git','-C',str(checkout),'branch','--show-current'],text=True).strip()
        if branch.startswith('book/'):
            book_id=branch[5:];assert checkout.resolve()==(OLD/book_id).resolve()
            status=subprocess.check_output(['git','-C',str(checkout),'status','--porcelain=v1','--untracked-files=all'],text=True)
            assert not status.strip() or status.strip()=='?? uv.lock',(book_id,status)
            books.append({'id':book_id,'checkout':str(checkout),'branch':branch,'status':status})
    assert len(books)==7
    if not resuming:save(REPORT/'before.json',{'date':'2026-10-22','head':git('rev-parse','HEAD'),
        'refs':git('for-each-ref','--format=%(refname) %(objectname)'),
        'remote':git('remote','-v'),'books':books,
        'reference_directory':r'D:\CelianFile\CelianFile\数学基础',
        'policy':'Copy latest per-book working data byte-exact; preserve old main copies and real worktrees; no source or translation rewriting.'})
    if resuming:
        previous=json.loads((REPORT/'before.json').read_text(encoding='utf8'))
        assert previous['books']==books and previous['head']==git('rev-parse','HEAD')
    records=json.loads((REPORT/'copied-books.json').read_text(encoding='utf8')) if (REPORT/'copied-books.json').exists() else []
    for item in books:
        book_id=item['id'];checkout=Path(item['checkout']);dest=ROOT/'books'/book_id
        if any(row['id']==book_id for row in records):continue
        # The old main version is recoverable, including its ignored files.
        backup=inside(SHARED/'.migration-backup/main-books'/book_id,ROOT)
        if not backup.exists():
            assert dest.is_dir();backup.parent.mkdir(parents=True,exist_ok=True)
            shutil.move(str(dest),str(backup))
        caches=relocate_caches(checkout,book_id,dest)
        rows=copy_verified(checkout/'books'/book_id,dest,book_id)
        save(REPORT/(book_id+'-files.json'),rows)
        template_rows=copy_verified(checkout/'template',dest/'template',book_id+' template')
        save(REPORT/(book_id+'-template.json'),template_rows)
        cfg=json.loads((dest/'config/book.yaml').read_text(encoding='utf8'))
        manifest=checkout/'config/template-manifest.json'
        if manifest.is_file():shutil.copy2(manifest,dest/'config/template-snapshot-manifest.json')
        records.append({**item,'book_root':'books/'+book_id,'files':len(rows),
            'bytes':sum(row['bytes'] for row in rows),'template_files':len(template_rows),
            'cache_files_relocated':sum(row['count'] for row in caches),'cache_bytes_relocated':sum(row['bytes'] for row in caches),
            'source_sha256':cfg['source']['sha256'],'title':cfg.get('title') or book_id,
            'phase':cfg.get('phase',''),'status':cfg.get('status',''),'final_output':cfg.get('final_output',''),
            'template_version':cfg.get('template_version',''),'original_config_sha256':sha(dest/'config/book.yaml')})
        save(REPORT/'copied-books.json',records)
    # Move all shared visible content under shared/, leaving only Git metadata
    # and the two requested top-level directories in the library root.
    moved=[]
    for source in list(ROOT.iterdir()):
        if source.name in {'.git','.gitignore','.gitattributes','books','shared'}:continue
        target=inside(SHARED/source.name,ROOT)
        if target.exists():
            assert source.name=='qa' and source.is_dir() and target.is_dir(),target
            for child in list(source.iterdir()):
                dest_child=target/child.name;assert not dest_child.exists(),dest_child
                shutil.move(str(child),str(dest_child))
            assert not any(source.iterdir());source.rmdir()
        else:shutil.move(str(source),str(target))
        moved.append(source.name)
    save(REPORT/'shared-relocation.json',moved)
    print('PREPARE COMPLETE; original worktrees are still in place until code verification.',flush=True)

def archive():
    before=json.loads((REPORT/'before.json').read_text(encoding='utf8'))
    for item in before['books']:
        source=Path(item['checkout']);target=inside(SHARED/'.legacy-worktrees'/item['id'],ROOT)
        assert source.resolve()==(OLD/item['id']).resolve() and source.is_dir() and not target.exists()
        untracked=subprocess.check_output(['git','-C',str(source),'ls-files','--others','--exclude-standard'],text=True).splitlines()
        untracked_hashes={name:sha(source/name) for name in untracked if (source/name).is_file()}
        target.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run(['git','-C',str(ROOT),'worktree','move',str(source),str(target)],check=True)
        subprocess.run(['git','-C',str(ROOT),'worktree','lock','--reason','Historical pre-consolidation snapshot; edit canonical books/ instead',str(target)],check=True)
        for name,digest in untracked_hashes.items():assert sha(target/name)==digest
        print('ARCHIVED WORKTREE',item['id'],flush=True)
    # Any extra sibling data is moved intact, not recursively removed.
    for source in list(OLD.iterdir()):
        target=inside(SHARED/'.migration-backup/sibling-residue'/source.name,ROOT)
        assert not target.exists();target.parent.mkdir(parents=True,exist_ok=True)
        shutil.move(str(source),str(target))
    assert OLD.resolve()==Path(r'D:\CelianFile\BOOKTRANSLATION-worktrees').resolve()
    assert not any(OLD.iterdir());OLD.rmdir() # only the verified empty container
    assert git('remote','-v')==before['remote']
    current=dict(line.split(' ',1) for line in git('for-each-ref','--format=%(refname) %(objectname)').splitlines())
    for line in before['refs'].splitlines():
        ref,head=line.split(' ',1)
        if ref.startswith('refs/heads/book/'):assert current[ref]==head,(ref,head)
    save(REPORT/'worktree-relocation.json',{'passed':True,'old_container_removed_only_when_empty':True,
        'book_branches_unchanged':True,'remote_unchanged':True,'legacy_worktree_parent':'shared/.legacy-worktrees'})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['prepare','archive']);args=parser.parse_args()
    {'prepare':prepare,'archive':archive}[args.action]()
