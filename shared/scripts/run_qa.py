"""Run deterministic LaTeX and punctuation QA for the explicitly selected book."""
import json
from mathbook.build import latex_qa
from mathbook.script_context import selected_book_paths

result = latex_qa(selected_book_paths())
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["passed"] else 1)
