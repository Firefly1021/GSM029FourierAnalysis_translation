"""Consolidated layout must retain the explicit-book and read-only boundaries."""
import json
import tempfile
import unittest
import shutil
from unittest.mock import patch
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

    def deliver_fixture(self):
        book=self.project.book('a')
        (book.root/'records').mkdir()
        shutil.move(str(book.root/'config'),str(book.root/'records/config'))
        (book.qa).mkdir(parents=True)
        (book.root/'records/glossary').mkdir()
        book.workflow_state.write_text(json.dumps({'status':'completed','completed_units':['one']}),encoding='utf8')
        book.chapter_progress.write_text('Unit ID\tQA Status\none\tpassed\ntwo\tnot-started\n',encoding='utf8')
        write_projects(self.project,[ProjectRecord('a','a','main',str(self.root),'completed','completed','','','','')])
        return book

    def test_completed_records_resolve_without_changing_active_book_layout(self):
        book=self.deliver_fixture()
        self.assertTrue(book.delivered)
        self.assertEqual(book.config_file,book.root/'records/config/book.yaml')
        self.assertEqual(book.issues,book.root/'records/qa/issues.jsonl')
        self.assertEqual(book.candidates,book.root/'records/glossary/candidates.tsv')
        self.assertEqual(book.build_cache,book.root/'.build')
        self.assertFalse(self.project.book('b').delivered)
        self.assertEqual(self.project.book('b').config_file,self.root/'books/b/config/book.yaml')
        verify_book_context(self.project,'a',writable=True)

    def test_completed_structure_does_not_resurrect_retired_folders(self):
        book=self.deliver_fixture()
        for name in ('workspace','logs','translation','structured','formulae','glossary'):
            shutil.rmtree(book.root/name)
        book.ensure_structure()
        for name in ('workspace','logs','translation','structured','formulae','glossary','config'):
            self.assertFalse((book.root/name).exists(),name)

    def test_completed_resume_finish_and_status_do_not_regenerate_units(self):
        from mathbook.workflow import resume_book,finish_book,book_status
        book=self.deliver_fixture();before=book.workflow_state.read_bytes()
        processor=lambda *args:self.fail('A completed book must not invoke a translation processor')
        self.assertIsNone(book_status(self.project,'a')['progress']['next_unit'])
        self.assertFalse(resume_book(self.project,'a',processor=processor)['resumed'])
        self.assertTrue(finish_book(self.project,'a',processor=processor)['already_completed'])
        self.assertEqual(before,book.workflow_state.read_bytes())

    def test_completed_restart_translation_and_ambiguous_binding_are_refused(self):
        from mathbook.workflow import start_book,translate_book,approve_sample
        book=self.deliver_fixture()
        with self.assertRaises(ProjectError):start_book(self.project,'a')
        with self.assertRaises(ProjectError):translate_book(self.project,'a')
        with self.assertRaises(ProjectError):approve_sample(self.project,'a')
        (book.root/'config').mkdir()
        (book.root/'config/library-binding.json').write_text('{}',encoding='utf8')
        with self.assertRaises(ProjectError):verify_book_context(self.project,'a',writable=True)

    def test_completed_legacy_compile_uses_registered_builder(self):
        from mathbook.build import compile_book
        book=self.deliver_fixture()
        with patch('mathbook.library.build_book',return_value={'candidate_pdf':'selected-master.pdf','success':True}) as builder:
            result=compile_book(book)
            self.assertEqual(result['pdf'],'selected-master.pdf')
            builder.assert_called_once_with(self.project,'a')

    def test_completed_provenance_paths_resolve_without_rewriting_records(self):
        book=self.deliver_fixture()
        (book.root/'records/path-map.json').write_text(json.dumps({'moved':{
            'qa':'records/qa','workspace/crops':'records/crops',
            'translation/draft/one.tex':'tex/chapters/one.tex'}}),encoding='utf8')
        self.assertEqual(book.resolve_recorded_path('qa/issues.jsonl'),book.issues)
        self.assertEqual(book.resolve_recorded_path('translation/draft/one.tex'),book.root/'tex/chapters/one.tex')
        with self.assertRaises(ProjectError):book.resolve_recorded_path('../b/config/book.yaml')

    def test_completed_low_level_processors_cannot_recreate_old_workspace(self):
        from mathbook.script_context import selected_book_paths
        self.deliver_fixture()
        with patch.dict('os.environ',{'MATHBOOK_BOOK_ID':'a'}),patch('mathbook.script_context.ProjectPaths',return_value=self.project):
            with self.assertRaises(ProjectError):selected_book_paths()
            self.assertTrue(selected_book_paths(allow_completed=True).delivered)

    def test_completed_qa_reads_actual_master_inputs_not_old_template_edition(self):
        from mathbook.build import canonical_tex_files
        book=self.deliver_fixture()
        (book.root/'tex/main.tex').write_text('old-template-edition',encoding='utf8')
        (book.root/'tex/current.tex').write_text('\\input{chapters/current-body}',encoding='utf8')
        (book.root/'tex/chapters/current-body.tex').write_text('accepted current body',encoding='utf8')
        binding=json.loads(book.binding_file.read_text(encoding='utf8'));binding['entry']='tex/current.tex'
        book.binding_file.write_text(json.dumps(binding),encoding='utf8')
        self.assertEqual(canonical_tex_files(book),[book.root/'tex/current.tex',book.root/'tex/chapters/current-body.tex'])

if __name__=='__main__':unittest.main()
