"""Formatting cleanup must preserve math payloads and meaningful TeX scope."""
import importlib.util
import unittest
from mathbook.project import ProjectPaths

spec=importlib.util.spec_from_file_location('feec_cleanup',ProjectPaths().system/'scripts/prepare_feec_production.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class ProductionTexCleanupTests(unittest.TestCase):
    def test_provenance_and_plain_paragraph_groups_are_removed(self):
        source='% block: fixture\n{Plain text $x_1$:}\n\n\\[\nx_1=x_1.\n\\]\n'
        result,stats=module.clean(source)
        self.assertNotIn('% block:',result)
        self.assertIn('Plain text $x_1$:\n\\[',result)
        self.assertEqual([v for _,_,v in module.math_spans(source)],[v for _,_,v in module.math_spans(result)])
        self.assertEqual(stats['paragraph_groups_removed'],1)

    def test_comment_terminated_wrappers_and_cell_groups_are_unwrapped(self):
        source='{Text $x$.}%\n{Cell}&{$x$}\\\\\n'
        result,stats=module.clean(source)
        self.assertIn('Text $x$.%',result)
        self.assertIn('Cell&$x$\\\\',result)
        self.assertEqual(stats['cell_or_text_groups_removed'],2)

    def test_scoped_font_declarations_and_command_arguments_survive(self):
        source='{\\small Text $x$.}\n\\textbf{Label}\n\\section{{Title $x$}}\n'
        result,_=module.clean(source)
        self.assertIn('{\\small Text $x$.}',result)
        self.assertIn('\\textbf{Label}',result)
        self.assertIn('\\section{Title $x$}',result)

    def test_macro_end_of_line_percent_is_not_a_process_annotation(self):
        source='% comment only\n\\newcommand{\\Fixture}{%\n  text%\n}\n'
        result=module.strip_comment_lines(source)
        self.assertIn('{%',result);self.assertIn('text%',result)
        self.assertNotIn('comment only',result)

if __name__=='__main__':unittest.main()
