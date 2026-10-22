"""Compile the explicitly selected book from a clean directory."""
import json
from mathbook.build import compile_book
from mathbook.script_context import selected_book_paths

print(json.dumps(compile_book(selected_book_paths()), ensure_ascii=False, indent=2))
