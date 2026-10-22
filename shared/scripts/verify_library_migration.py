"""Verify copied bytes, source PDFs, template snapshots, identities and refs."""
import hashlib,json,subprocess,sys,time,unittest,io
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[2];SYSTEM=ROOT/'shared'
sys.path.insert(0,str(SYSTEM/'src'))
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import read_projects,verify_book_context
from mathbook.template import verify_manifest

def main():
    project=ProjectPaths(ROOT);report_dir=SYSTEM/'qa/integration-20261022'
    copied=json.loads((report_dir/'copied-books.json').read_text(encoding='utf8'));results=[]
    before=json.loads((report_dir/'before.json').read_text(encoding='utf8'))
    assert not verify_manifest(),verify_manifest()
    for row in copied:
        book,record=verify_book_context(project,row['id'],writable=False)
        binding=json.loads((book.root/'config/library-binding.json').read_text(encoding='utf8'))
        assert binding['book_id']==row['id'] and binding['book_root']=='books/'+row['id']
        assert Path(record.worktree).resolve()==ROOT
        inventory=json.loads((report_dir/(row['id']+'-files.json')).read_text(encoding='utf8'))
        legacy=SYSTEM/'.legacy-worktrees'/row['id']/'books'/row['id']
        def check(item):
            path=book.root/item['path']
            assert path.is_file() and path.stat().st_size==item['bytes'] and sha256_file(path)==item['sha256'],str(path)
            if not item['path'].startswith(('workspace/','logs/')):
                assert sha256_file(legacy/item['path'])==item['sha256'],'Original working data changed: '+item['path']
            return True
        with ThreadPoolExecutor(max_workers=4) as pool:
            for index,_ in enumerate(pool.map(check,inventory),1):
                if index%10000==0:print('RECHECK',row['id'],index,flush=True)
        templates=json.loads((report_dir/(row['id']+'-template.json')).read_text(encoding='utf8'))
        for item in templates:assert sha256_file(book.template/item['path'])==item['sha256']
        assert directory_manifest_hash(book.template)==binding['template_hash']
        assert sha256_file(book.require_source_pdf())==row['source_sha256']
        assert sha256_file(book.config_file)==row['original_config_sha256']
        cache_journal=report_dir/(row['id']+'-cache-moves.json')
        cache_rows=json.loads(cache_journal.read_text(encoding='utf8')) if cache_journal.exists() else []
        for cache in cache_rows:
            for item in cache['files']:
                st=(book.root/cache['relative']/item['path']).stat()
                assert (st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)==(item['device'],item['file_id'],item['bytes'],item['mtime_ns'])
        final=book.root/binding['final_output'] if binding['final_output'] else None
        results.append({'book_id':row['id'],'files_verified':len(inventory),'bytes_verified':row['bytes'],
            'source_unchanged':True,'original_config_unchanged':True,'template_files_verified':len(templates),
            'cache_files_verified_by_identity':sum(r['count'] for r in cache_rows),
            'cache_bytes_verified_by_identity':sum(r['bytes'] for r in cache_rows),
            'entry':binding['entry'],'entry_exists':(book.root/binding['entry']).is_file(),
            'final_output':binding['final_output'],'final_sha256':sha256_file(final) if final else None,
            'historical_status_retained':record.status})
        print('VERIFIED ALL ORIGINAL BYTES',row['id'],len(inventory),flush=True)
    refs=dict(line.split(' ',1) for line in subprocess.check_output(['git','-C',str(ROOT),'for-each-ref','--format=%(refname) %(objectname)'],text=True).splitlines())
    for line in before['refs'].splitlines():
        ref,head=line.split(' ',1)
        if ref.startswith('refs/heads/book/'):assert refs[ref]==head
    assert subprocess.check_output(['git','-C',str(ROOT),'remote','-v'],text=True).strip()==before['remote']
    visible=sorted(p.name for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith('.'))
    assert visible==['books','shared'],visible
    assert not Path(r'D:\CelianFile\BOOKTRANSLATION-worktrees').exists()
    result={'passed':True,'date':'2026-10-22','scope':'Architecture/data relocation, not new translation or mathematical acceptance.',
        'visible_directories':visible,'books':results,'book_branches_unchanged':True,'remote_unchanged':True,
        'remote_push':False,'original_inputs_translation_tex_images_qa_logs_and_caches_preserved':True,
        'cache_verification':'Ignored caches were moved on the same volume and verified by file identity/size/mtime; not represented as a new SHA-256 content review.',
        'files_verified':sum(r['files_verified'] for r in results),'bytes_verified':sum(r['bytes_verified'] for r in results),
        'cache_files_verified_by_identity':sum(r['cache_files_verified_by_identity'] for r in results),
        'cache_bytes_verified_by_identity':sum(r['cache_bytes_verified_by_identity'] for r in results)}
    (report_dir/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'passed':True,'books':len(results),'files':result['files_verified'],'bytes':result['bytes_verified']}),flush=True)

if __name__=='__main__':main()
