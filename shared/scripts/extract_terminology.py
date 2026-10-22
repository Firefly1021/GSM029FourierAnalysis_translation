"""Review per-book terminology candidates against the shared terminology library."""
import json
from mathbook.project import ProjectPaths
from mathbook.script_context import selected_book_paths
from mathbook.terminology import review_candidates

book = selected_book_paths()
print(json.dumps(review_candidates(ProjectPaths(), book), ensure_ascii=False, indent=2))
