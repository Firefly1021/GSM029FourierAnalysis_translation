"""Persist the relocation/duplicate mapping without altering historical records."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'shared/qa/completed-view-20261022'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths
from mathbook.workflow import verify_book_context

def main():
    plan=json.loads((REPORT/'plan.json').read_text(encoding='utf8'))
    for item in plan['books']:
        book,_=verify_book_context(ProjectPaths(ROOT),item['book_id'],writable=True)
        assert book.delivered
        path=book.assert_write_path(book.records/'path-map.json')
        result={'book_id':book.book_id,'layout':'completed-edition','moved':item['path_map'],
            'note':'Original records retain their original bytes and source-page metadata. Longest matching path prefix wins; exact duplicate aliases resolve to the surviving file.'}
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        print(book.book_id,flush=True)

if __name__=='__main__':main()
