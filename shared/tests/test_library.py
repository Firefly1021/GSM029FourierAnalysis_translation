"""Consolidated layout must retain the explicit-book and read-only boundaries."""
import json
import tempfile
import unittest
from pathlib import Path
from mathbook.project import ProjectPaths,ProjectError,run_git
from mathbook.workflow import verify_book_context,ProjectRecord,write_projects

class UnifiedLibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'library'
        (self.root/'shared/config').mkdir(parents=True);(self.root/'books').mkdir()
        (self.root/'shared/config/library-layout.json').write_text('{"mode":"unified"}',encoding='utf8')
        self.project=ProjectPaths(self.root)
        run_git(self.root,['init','-b','main']);run_git(self.root,['config','user.name','Test'])
        run_git(self.root,['config','user.email','test@example.invalid'])
        for name in ('a','b'):
            book=self.project.book(name);book.ensure_structure()
            (book.root/'config/library-binding.json').write_text(json.dumps({'book_id':name,'book_root':'books/'+name}),encoding='utf8')
        write_projects(self.project,[ProjectRecord(n,n,'main',str(self.root),'registered','registered','','','','') for n in ('a','b')])
        run_git(self.root,['add','.']);run_git(self.root,['commit','-m','Fixture'])
    def tearDown(self):self.temp.cleanup()
    def test_shared_and_book_roots_resolve_without_external_worktree(self):
        self.assertEqual(self.project.system,self.root/'shared')
        self.assertEqual(ProjectPaths(self.root/'shared').root,self.root)
        self.assertEqual(self.project.projects_file,self.root/'shared/PROJECTS.md')
        self.assertEqual(self.project.book('a').root,self.root/'books/a')
    def test_explicit_context_accepts_main_and_rejects_cross_book_write(self):
        book,_=verify_book_context(self.project,'a',writable=True)
        with self.assertRaises(ProjectError):book.assert_write_path(self.root/'books/b/tex/main.tex')
        with self.assertRaises(ProjectError):book.assert_write_path(self.root/'shared/README.md')
    def test_mismatched_binding_is_refused(self):
        (self.root/'books/a/config/library-binding.json').write_text('{"book_id":"b","book_root":"books/b"}',encoding='utf8')
        with self.assertRaises(ProjectError):verify_book_context(self.project,'a',writable=True)
    def test_historical_book_branch_is_not_an_active_unified_checkout(self):
        run_git(self.root,['checkout','-b','book/a'])
        with self.assertRaises(ProjectError):verify_book_context(self.project,'a',writable=True)
    def test_book_template_snapshot_prevents_implicit_shared_update(self):
        snapshot=self.root/'books/a/template';snapshot.mkdir()
        self.assertEqual(self.project.book('a').template,snapshot)
    def test_new_book_does_not_create_a_second_external_container(self):
        from pypdf import PdfWriter
        from mathbook.library import new_unified_book
        from mathbook.terminology import initialize_tsv,TERM_COLUMNS,HISTORY_COLUMNS
        (self.project.template/'style').mkdir(parents=True)
        (self.project.template/'style/test.sty').write_bytes(b'% pinned fixture\n')
        (self.project.config/'default.yaml').write_text('{"template":{"version":"fixture"}}',encoding='utf8')
        (self.project.config/'template-manifest.json').write_text('{"files":[]}',encoding='utf8')
        initialize_tsv(self.project.glossary/'terminology.tsv',TERM_COLUMNS)
        initialize_tsv(self.project.glossary/'terminology-history.tsv',HISTORY_COLUMNS)
        run_git(self.root,['add','.']);run_git(self.root,['commit','-m','Shared fixtures'])
        source=Path(self.temp.name)/'source.pdf';writer=PdfWriter();writer.add_blank_page(width=72,height=72)
        with source.open('wb') as handle:writer.write(handle)
        result=new_unified_book(self.project,'new-book',source)
        self.assertEqual(result['active_branch'],'main')
        self.assertEqual(result['checkpoint_branch'],'book/new-book')
        self.assertEqual(self.project.git_branch(),'main')
        self.assertEqual((self.project.book('new-book').template/'style/test.sty').read_bytes(),b'% pinned fixture\n')
        self.assertFalse((self.root.parent/'library-worktrees').exists())
        self.assertEqual(len(self.project.git_worktree_map()),1)
        verify_book_context(self.project,'new-book',writable=True)

if __name__=='__main__':unittest.main()
