"""Check compact-edition relocation, exact deduplication and immutable inputs."""
import json,sys,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'shared/qa/completed-view-20261022'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import verify_book_context,book_status,resume_book
from mathbook.template import verify_manifest

def verify():
    project=ProjectPaths(ROOT);plan=json.loads((REPORT/'plan.json').read_text(encoding='utf8'))
    results=[];total=0
    build_report=REPORT/'builds.json'
    if build_report.is_file() and (REPORT/'build-cache-cleanup-plan.receipt.json').is_file():
        builds=json.loads(build_report.read_text(encoding='utf8'))
        assert builds['passed'] and len(builds['results'])==7
        for row in builds['results']:
            book=project.book(row['book_id'])
            assert not book.build_cache.exists()
            row.update(verification_cache_removed=True,candidate_and_log_paths_are_historical=True)
            path=book.qa/'unified-build.json'
            report=json.loads(path.read_text(encoding='utf8'))
            report.update(verification_cache_removed=True,candidate_and_log_paths_are_historical=True)
            path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        build_report.write_text(json.dumps(builds,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    assert not verify_manifest(),verify_manifest()
    for item in plan['books']:
        book,_=verify_book_context(project,item['book_id'],writable=True)
        assert book.delivered
        deleted={r['from']:r for r in item['deletions']};verified=0;duplicates=0
        for original in item['inventory']:
            if original['from'] in deleted:
                removed=deleted[original['from']]
                assert not (book.root/original['to']).exists(),original['to']
                if removed['duplicate_of']:
                    survivor=book.resolve_recorded_path(original['from'])
                    assert sha256_file(survivor)==original['sha256'],survivor
                    duplicates+=1
                continue
            target=book.root/original['to']
            assert target.is_file(),target
            # This task's generated build report is intentionally refreshed.
            if original['from']=='qa/unified-build.json':continue
            assert sha256_file(target)==original['sha256'],target
            verified+=1
        binding=json.loads(book.binding_file.read_text(encoding='utf8'))
        assert directory_manifest_hash(book.template)==binding['template_hash']
        if binding.get('build_template'):
            assert directory_manifest_hash(book.root/binding['build_template'])==binding['build_template_hash']
        before=book.workflow_state.read_bytes()
        status=book_status(project,book.book_id)
        assert status['status'] in {'complete','completed'} and status['progress']['next_unit'] is None
        assert not resume_book(project,book.book_id)['resumed']
        assert before==book.workflow_state.read_bytes(),'Resume mutated a completed edition.'
        book.ensure_structure()
        for retired in ('config','formulae','glossary','qa','structured','translation','workspace','logs','workflow','.vscode','PLANS.md','PROJECT_STATUS.md','TYPESETTING.md','OPEN-THIS-BOOK.md','archive'):
            assert not (book.root/retired).exists(),'Retired root path recreated: '+retired
        assert (book.root/'README.md').is_file()
        roots=sorted(p.name for p in book.root.iterdir())
        expected={'input','tex','template','output','records','README.md'}
        if (book.root/'template-accepted').exists():expected.add('template-accepted')
        if (book.root/'.build').exists():expected.add('.build')
        assert set(roots)==expected,(book.book_id,roots)
        results.append({'book_id':book.book_id,'root_before_entries':len(item['root_before']),
            'root_after_entries':len(roots),'root_after':roots,'retained_files_sha256_verified':verified,
            'byte_identical_duplicates_removed':duplicates,'retired_root_not_recreated':True,
            'completed_status_and_resume_unchanged':True,'formal_tex_source_template_output_unchanged':True})
        total+=verified
    historical=json.loads((ROOT/'shared/qa/integration-20261022/before.json').read_text(encoding='utf8'))
    for line in historical['refs'].splitlines():
        ref,head=line.split(' ',1)
        if ref.startswith('refs/heads/book/'):
            assert subprocess.check_output(['git','-C',str(ROOT),'rev-parse',ref],text=True).strip()==head
    assert subprocess.check_output(['git','-C',str(ROOT),'remote','-v'],text=True).strip()==historical['remote']
    result={'passed':True,'books':results,'retained_files_sha256_verified':total,
        'deleted_files':sum(len(i['deletions']) for i in plan['books']),
        'deleted_bytes':sum(r['bytes'] for i in plan['books'] for r in i['deletions']),
        'byte_identical_duplicates_removed':sum(r['byte_identical_duplicates_removed'] for r in results),
        'book_branch_heads_unchanged':True,'remote_unchanged':True,'remote_push':False,
        'scope':'Completed-edition organization and exact-duplicate cleanup; no translation or mathematical reacceptance.'}
    receipt=json.loads((REPORT/'plan.receipt.json').read_text(encoding='utf-8-sig'))
    assert receipt['plan_sha256']==sha256_file(REPORT/'plan.json')
    result['execution_receipt_matches_plan']=True
    (REPORT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k!='books'},ensure_ascii=False),flush=True)

def cleanup_plan():
    builds=json.loads((REPORT/'builds.json').read_text(encoding='utf8'))
    assert builds['passed'] and len(builds['results'])==7
    targets=[]
    for row in builds['results']:
        book=ProjectPaths(ROOT).book(row['book_id']);cache=book.build_cache
        assert cache==book.root/'.build' and Path(row['build_directory']).is_relative_to(cache)
        files=[p for p in cache.rglob('*') if p.is_file()]
        targets.append({'path':cache.relative_to(ROOT).as_posix(),'files':len(files),'bytes':sum(p.stat().st_size for p in files)})
    result={'library_root':str(ROOT),'authorization':'user-request-20261022-remove-completed-book-intermediates',
            'allowed_prefixes':['books/'],'targets':targets}
    (REPORT/'build-cache-cleanup-plan.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'targets':len(targets),'bytes':sum(r['bytes'] for r in targets)}),flush=True)

if __name__=='__main__':{'verify':verify,'cleanup-plan':cleanup_plan}[sys.argv[1] if len(sys.argv)>1 else 'verify']()
