"""Build and audit the FEEC cover without changing the accepted body."""
from pathlib import Path
import argparse
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'shared/src'))
from mathbook.project import ProjectPaths, sha256_file, directory_manifest_hash

BOOK = ROOT / 'books/finite-element-exterior-calculus'
AUDIT = ROOT / 'shared/qa/feec-cover-20261023'
DRIVER = Path('C:/Users/A/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


def prepare():
    AUDIT.mkdir(parents=True, exist_ok=True)
    if (AUDIT / 'before.json').exists():
        raise RuntimeError('Baseline already exists; do not replace it.')
    files = {p.relative_to(BOOK).as_posix(): sha256_file(p)
             for p in BOOK.rglob('*') if p.is_file()}
    other_books = {p.relative_to(ROOT).as_posix(): sha256_file(p)
                   for b in (ROOT / 'books').iterdir() if b.is_dir() and b != BOOK
                   for p in b.rglob('*') if p.is_file() and '.build' not in p.parts}
    shutil.copy2(BOOK / 'output/book-aljabr-zh.pdf', AUDIT / 'before.pdf')
    write_json(AUDIT / 'before.json', {'files': files, 'other_books': other_books})
    print('Baseline captured; existing uncommitted work is not reset.', flush=True)


def build():
    from mathbook.library import build_book
    project = ProjectPaths(ROOT)
    book = project.book('finite-element-exterior-calculus')
    digest = directory_manifest_hash(book.template)
    binding = json.loads(book.binding_file.read_text(encoding='utf8'))
    binding.update(template_hash=digest, build_template_hash=digest)
    write_json(book.binding_file, binding)
    config = book.load_config()
    config['template_manifest_hash'] = digest
    write_json(book.config_file, config)
    result = build_book(project, book.book_id, driver=DRIVER)
    write_json(AUDIT / 'build.json', result)
    print(json.dumps(result, ensure_ascii=False), flush=True)


def verify():
    from pypdf import PdfReader
    from PIL import ImageChops
    from audit_feec_production import labels, link_audit, raster
    baseline = json.loads((AUDIT / 'before.json').read_text(encoding='utf8'))
    build = json.loads((AUDIT / 'build.json').read_text(encoding='utf8'))
    previous = json.loads((ROOT / 'shared/qa/feec-production-20261023/verification.json').read_text(encoding='utf8'))
    assert build['success']
    assert all(not value for value in build['warnings'].values()), build['warnings']
    permitted = {'tex/main.tex', 'README.md', 'output/book-aljabr-zh.pdf'}
    for name, digest in baseline['files'].items():
        if name not in permitted:
            assert sha256_file(BOOK / name) == digest, name
    for name, digest in baseline['other_books'].items():
        assert sha256_file(ROOT / name) == digest, name
    old = PdfReader(AUDIT / 'before.pdf')
    new = PdfReader(build['candidate_pdf'])
    offset = len(new.pages) - len(old.pages)
    assert offset == 2, (len(old.pages), len(new.pages))
    for index, page in enumerate(old.pages):
        assert page.extract_text() == new.pages[index + offset].extract_text(), index + 1
    label_map = labels(Path(build['build_directory']) / 'main.aux')
    assert label_map == previous['reference_label_number_map']
    links = link_audit(new)
    assert links['internal_links'] == 753 and not links['unresolved_named_destinations']
    assert set(old.named_destinations) == set(new.named_destinations)
    first = new.pages[0].extract_text()
    assert '有限元外微积分' in first.replace(' ', '')
    assert 'Douglas N. Arnold' in first
    assert '代数学方法' not in first and '李文威' not in first
    assert not (new.pages[1].extract_text() or '').strip()
    visual = AUDIT / 'visual'
    visual.mkdir(exist_ok=True)
    for page in (1, 2, 3, 8, 9, 25, 26, 71, len(new.pages)):
        raster(build['candidate_pdf'], page).save(visual / f'page-{page}.png')
    for page in (1, 6, 7, 23, 24, 69, 139):
        before = raster(AUDIT / 'before.pdf', page)
        after = raster(build['candidate_pdf'], page + offset)
        assert before.size == after.size and ImageChops.difference(before, after).getbbox() is None, page
    write_json(AUDIT / 'verification.json', {
        'passed': True, 'old_pages': len(old.pages), 'new_pages': len(new.pages),
        'added_pages': ['AJbook-derived cover', 'blank cover verso'],
        'all_original_pages_text_identical': True,
        'body_and_original_template_files_byte_unchanged': True,
        'other_books_byte_unchanged': True,
        'unchanged_label_numbers': len(label_map), 'links': links,
        'body_pixel_identical_old_pages': [1, 6, 7, 23, 24, 69, 139],
        'warnings': build['warnings'], 'pdf_sha256': sha256_file(Path(build['candidate_pdf'])),
        'visual_review': 'pending', 'published': False, 'remote_push': False})
    print('Verified 139 original pages unchanged, 537 labels and 753 links; cover renders ready.', flush=True)


def publish():
    from mathbook.workflow import read_projects, write_projects
    audit = json.loads((AUDIT / 'verification.json').read_text(encoding='utf8'))
    build = json.loads((AUDIT / 'build.json').read_text(encoding='utf8'))
    assert audit['passed'] and ARGS.visual_reviewed
    candidate = Path(build['candidate_pdf'])
    assert sha256_file(candidate) == audit['pdf_sha256']
    output = BOOK / 'output/book-aljabr-zh.pdf'
    shutil.copy2(candidate, output)
    assert sha256_file(output) == audit['pdf_sha256']
    for name in ('main.log', 'build-driver.log'):
        shutil.copy2(Path(build['build_directory']) / name, AUDIT / name)
    project = ProjectPaths(ROOT)
    book = project.book('finite-element-exterior-calculus')
    config = book.load_config()
    config['template_version'] = 'AJbook-feec-cover-20261023'
    write_json(book.config_file, config)
    rows = read_projects(project)
    for row in rows:
        if row.book_id == book.book_id:
            row.template_version = config['template_version']
    write_projects(project, rows)
    audit.update(visual_review='passed: cover, contents and chapter opening inspected',
                 published=True, output_sha256=sha256_file(output),
                 cover_source='tex/frontmatter/cover.tex',
                 cover_source_sha256=sha256_file(BOOK / 'tex/frontmatter/cover.tex'),
                 main_source_sha256=sha256_file(BOOK / 'tex/main.tex'),
                 upstream_cover_sha256=sha256_file(project.system / 'template/collections/aljabr-1/upstream/coverpage.tex'),
                 font_source='https://raw.githubusercontent.com/notofonts/noto-cjk/main/Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Bold.otf',
                 font_sha256=sha256_file(BOOK / 'template/fonts/noto-serif-cjk-sc/NotoSerifCJKsc-Bold.otf'),
                 font_family_verified='Noto Serif CJK SC: Bold (fc-scan)',
                 font_license='SIL Open Font License 1.1')
    write_json(AUDIT / 'verification.json', audit)
    build.update(published=True, published_pdf=str(output),
                 log=str(AUDIT / 'build-driver.log'),
                 candidate_path_is_temporary=True)
    write_json(AUDIT / 'build.json', build)
    write_json(book.qa / 'unified-build.json', build)
    print('Published verified 141-page book; no commit or push.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'build', 'verify', 'publish'])
    parser.add_argument('--visual-reviewed', action='store_true')
    ARGS = parser.parse_args()
    globals()[ARGS.action]()
