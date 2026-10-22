"""Verify retained bytes, dependency closure and history after explicit cleanup."""
import collections,hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'shared/qa/integration-20261022'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths,directory_manifest_hash,sha256_file
from mathbook.workflow import read_projects,verify_book_context
from mathbook.template import verify_manifest

def verify():
    rows=json.loads((REPORT/'retained-core-manifest.json').read_text(encoding='utf8'))
    own_mutable=[];checked=0;total=0
    for row in rows:
        path=ROOT/row['path']
        assert path.is_file(),path
        if row['path'].endswith(('/OPEN-THIS-BOOK.md','/qa/unified-build.json')):
            own_mutable.append(row['path']);continue
        assert path.stat().st_size==row['bytes'] and sha256_file(path)==row['sha256'],path
        checked+=1;total+=row['bytes']
    assert not verify_manifest(),verify_manifest()
    before=json.loads((REPORT/'before.json').read_text(encoding='utf8'))
    for line in before['refs'].splitlines():
        ref,head=line.split(' ',1)
        if ref.startswith('refs/heads/book/'):
            assert subprocess.check_output(['git','-C',str(ROOT),'rev-parse',ref],text=True).strip()==head
    assert subprocess.check_output(['git','-C',str(ROOT),'remote','-v'],text=True).strip()==before['remote']
    project=ProjectPaths(ROOT);books=[]
    builds=json.loads((REPORT/'builds.json').read_text(encoding='utf8'))
    assert builds['passed'] and len(builds['results'])==7
    cleanup_receipt=REPORT/'verification-cache-cleanup-plan.receipt.json'
    if cleanup_receipt.exists():
        for result in builds['results']:
            assert not Path(result['build_directory']).exists()
            result['verification_cache_removed']=True
            result['candidate_and_log_paths_are_historical']=True
            report_path=ROOT/'books'/result['book_id']/'qa/unified-build.json'
            report=json.loads(report_path.read_text(encoding='utf8'))
            report.update(verification_cache_removed=True,candidate_and_log_paths_are_historical=True)
            report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        (REPORT/'builds.json').write_text(json.dumps(builds,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    dependencies=json.loads((REPORT/'retained-build-dependencies.json').read_text(encoding='utf8'))
    for row in read_projects(project):
        book,_=verify_book_context(project,row.book_id,writable=False)
        binding=json.loads((book.root/'config/library-binding.json').read_text(encoding='utf8'))
        assert directory_manifest_hash(book.template)==binding['template_hash']
        if binding.get('build_template'):
            assert directory_manifest_hash(book.root/binding['build_template'])==binding['build_template_hash']
        copied=json.loads((REPORT/(row.book_id+'-files.json')).read_text(encoding='utf8'))
        originals={r['path']:r for r in copied}
        assert sha256_file(book.config_file)==originals['config/book.yaml']['sha256']
        assert sha256_file(book.root/'PROJECT_STATUS.md')==originals['PROJECT_STATUS.md']['sha256']
        assert sha256_file(book.issues)==originals['qa/issues.jsonl']['sha256']
        for name in dependencies[row.book_id]:assert (ROOT/name).is_file(),name
        result=next(r for r in builds['results'] if r['book_id']==row.book_id)
        assert sha256_file(book.root/binding['final_output'])==result['final_output_sha256']
        books.append({'book_id':row.book_id,'entry':binding['entry'],'pages':result['candidate_pdf_pages'],
            'source_unchanged':True,'current_user_template_unchanged':True,'final_pdf_unchanged':True,
            'original_status_and_issues_unchanged':True,'clean_build_after_cleanup':result['integration_passed'],
            'dependencies_preserved':len(dependencies[row.book_id]),'warnings':result['warnings']})
    receipts=[]
    for name in ('scratch-cleanup-plan.receipt.json','completed-cleanup-plan.receipt.json','legacy-cleanup-plan.receipt.json','verification-cache-cleanup-plan.receipt.json'):
        path=REPORT/name
        if path.exists():
            receipt=json.loads(path.read_text(encoding='utf-8-sig'))
            assert receipt['plan_sha256']==sha256_file(Path(receipt['plan']))
            receipts.append({'receipt':name,'files':int(receipt['files']),'bytes':int(receipt['bytes'])})
    sizes=collections.defaultdict(lambda:[0,0])
    for base in (ROOT/'books',ROOT/'shared'):
        for current,dirs,files in os.walk(base):
            for name in files:
                path=Path(current,name);key=path.relative_to(ROOT).parts[0]
                sizes[key][0]+=1;sizes[key][1]+=path.stat().st_size
    result={'passed':True,'scope':'Structural/build/input-integrity regression; no new mathematical or translation acceptance.',
        'retained_original_files_verified':checked,'retained_original_bytes_verified':total,
        'own_generated_guides_and_build_reports_excluded':own_mutable,'books':books,
        'book_branches_unchanged':True,'remote_unchanged':True,'remote_push':False,
        'deletion_receipts':receipts,'deleted_files':sum(r['files'] for r in receipts),'deleted_bytes':sum(r['bytes'] for r in receipts),
        'current_size_excluding_hidden_git':{k:{'files':v[0],'bytes':v[1]} for k,v in sizes.items()}}
    initial=json.loads((REPORT/'cleanup-inventory.json').read_text(encoding='utf8'))
    result['books_before_cleanup_bytes']=sum(r['bytes'] for r in initial if r['path'].startswith('books/'))
    (REPORT/'cleanup-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k not in {'books','own_generated_guides_and_build_reports_excluded'}},ensure_ascii=False),flush=True)

if __name__=='__main__':verify()
