"""Architecture regressions and fresh builds; no final-PDF publication."""
import argparse,io,json,os,sys,time,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SYSTEM=ROOT/'shared'
sys.path.insert(0,str(SYSTEM/'src'))
from mathbook.project import ProjectPaths,sha256_file
from mathbook.workflow import read_projects

REPORT=Path(os.environ.get('MATHBOOK_INTEGRATION_REPORT',str(SYSTEM/'qa/integration-20261022')))
REPORT.mkdir(parents=True,exist_ok=True)
def save(name,value):
    (REPORT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def tests():
    stream=io.StringIO();started=time.time()
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.discover(str(SYSTEM/'tests')))
    (REPORT/'tests.log').write_text(stream.getvalue(),encoding='utf8')
    save('tests.json',{'passed':result.wasSuccessful(),'tests':result.testsRun,'errors':len(result.errors),
        'failures':len(result.failures),'skipped':len(result.skipped),'seconds':time.time()-started,
        'head':ProjectPaths(ROOT).git_head()})
    print(stream.getvalue(),flush=True)
    assert result.wasSuccessful()

def builds():
    from pypdf import PdfReader
    from mathbook.library import build_book
    project=ProjectPaths(ROOT);results=[]
    driver=Path(r'C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py')
    assert driver.is_file()
    for row in read_projects(project):
        book=project.book(row.book_id)
        binding=json.loads(book.binding_file.read_text(encoding='utf8'))
        original=book.root/binding['final_output'];oldhash=sha256_file(original)
        oldpages=len(PdfReader(original).pages)
        print('CLEAN BUILD',row.book_id,flush=True)
        try:
            result=build_book(project,row.book_id,driver=driver)
            newpages=len(PdfReader(result['candidate_pdf']).pages)
            result.update(original_pdf_pages=oldpages,candidate_pdf_pages=newpages,
                final_output_unchanged=sha256_file(original)==oldhash,final_output_sha256=oldhash,
                page_count_unchanged=newpages==oldpages)
            result['integration_passed']=result['success'] and result['final_output_unchanged'] and result['page_count_unchanged']
        except Exception as exc:
            result={'book_id':row.book_id,'integration_passed':False,'error':str(exc),
                'final_output_unchanged':sha256_file(original)==oldhash}
        results.append(result);save('builds.json',{'passed':all(r['integration_passed'] for r in results),'results':results})
        print(json.dumps(result,ensure_ascii=False),flush=True)
    assert len(results)==7 and all(r['integration_passed'] for r in results),'See preserved per-book logs; do not publish candidates.'

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['tests','builds']);args=parser.parse_args()
    {'tests':tests,'builds':builds}[args.action]()
