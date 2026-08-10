"""Render an explicit page range for the explicitly selected book."""

import argparse

import pdfplumber

from mathbook.script_context import selected_book_paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("start_page", type=int)
    parser.add_argument("end_page", type=int)
    parser.add_argument("--resolution", type=int, default=200)
    args = parser.parse_args()
    if args.start_page < 1 or args.end_page < args.start_page:
        raise SystemExit("invalid page range")
    book = selected_book_paths()
    output = book.assert_write_path(book.root / "workspace" / "pages" / args.batch_id)
    output.mkdir(parents=True, exist_ok=True)
    with pdfplumber.open(book.require_source_pdf()) as pdf:
        if args.end_page > len(pdf.pages):
            raise SystemExit(f"end page {args.end_page} exceeds PDF length {len(pdf.pages)}")
        for page_number in range(args.start_page, args.end_page + 1):
            pdf.pages[page_number - 1].to_image(resolution=args.resolution).save(output / f"page-{page_number:03d}.png")
    print(output)
    return 0


raise SystemExit(main())
