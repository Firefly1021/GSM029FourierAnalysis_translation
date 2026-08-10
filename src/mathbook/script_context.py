"""Explicit book selection for shared low-level debugging scripts."""

from __future__ import annotations

import os

from .project import BookPaths, ProjectError, ProjectPaths


def selected_book_paths() -> BookPaths:
    book_id = os.environ.get("MATHBOOK_BOOK_ID", "").strip()
    if not book_id:
        raise ProjectError(
            "MATHBOOK_BOOK_ID is required for a book-specific low-level script; implicit book selection is forbidden."
        )
    book = ProjectPaths().book(book_id)
    if not book.root.is_dir():
        raise ProjectError(f"Selected book does not exist: {book_id}")
    return book


def selected_book_root():
    return selected_book_paths().root
