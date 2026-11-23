"""Record and verify the move to the book's existing tex/build directory."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'shared/src'))
from mathbook.project import ProjectPaths, sha256_file, validate_project_structure
from mathbook.workflow import read_projects, write_projects

BOOK = ROOT/'books/finite-element-exterior-calculus'
AUDIT = ROOT/'shared/qa/feec-build-directory-20261023'


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf8')


def prepare():
    AUDIT.mkdir(parents=True, exist_ok=True)
    assert not (AUDIT/'before.json').exists(), 'Do not replace the baseline.'
    files = {p.relative_to(BOOK).as_posix(): sha256_file(p)
             for folder in ('tex', 'template', 'input')
             for p in (BOOK/folder).rglob('*') if p.is_file() and '/build/' not in p.as_posix()}
    pdf = BOOK/'output/book-aljabr-zh.pdf'
    assert pdf.is_file() and not (BOOK/'tex/build/main.pdf').exists()
    cache = [p for p in (BOOK/'.build').rglob('*') if p.is_file()]
    save(AUDIT/'before.json', {
        'preserved_files': files, 'pdf_sha256': sha256_file(pdf),
        'old_pdf': 'output/book-aljabr-zh.pdf', 'new_pdf': 'tex/build/main.pdf',
        'removed_cache_files': len(cache), 'removed_cache_bytes': sum(p.stat().st_size for p in cache),
        'user_main_tex_edit_preserved': True})
    print('Inventoried source/template hashes, final PDF and disposable build files.', flush=True)


def finish():
    before = json.loads((AUDIT/'before.json').read_text(encoding='utf8'))
    retired = [name for name in ('output', '.build') if (BOOK/name).exists()]
    for name, digest in before['preserved_files'].items():
        assert sha256_file(BOOK/name) == digest, name
    assert sha256_file(BOOK/'tex/build/main.pdf') == before['pdf_sha256']
    project = ProjectPaths(ROOT)
    book = project.book('finite-element-exterior-calculus')
    binding = json.loads(book.binding_file.read_text(encoding='utf8'))
    binding.update(build_directory='tex/build', final_output='tex/build/main.pdf')
    save(book.binding_file, binding)
    config = book.load_config()
    config['final_output'] = 'tex/build/main.pdf'
    config['typesetting'].update(entry='tex/main.tex', output='tex/build/main.pdf')
    save(book.config_file, config)
    mapping_file = book.records/'path-map.json'
    mapping = json.loads(mapping_file.read_text(encoding='utf8'))
    mapping['moved']['output/book-aljabr-zh.pdf'] = 'tex/build/main.pdf'
    save(mapping_file, mapping)
    rows = read_projects(project)
    for row in rows:
        if row.book_id == book.book_id:
            row.final_output = 'books/finite-element-exterior-calculus/tex/build/main.pdf'
    write_projects(project, rows)
    current_build = book.qa/'unified-build.json'
    report = json.loads(current_build.read_text(encoding='utf8'))
    report.update(published_pdf=str(BOOK/'tex/build/main.pdf'),
                  historical_candidate_cache_removed=not (BOOK/'.build').exists())
    save(current_build, report)
    assert book.build_cache == BOOK/'tex/build'
    assert not validate_project_structure(), validate_project_structure()
    save(AUDIT/'verification.json', {
        'passed': True, 'build_directory': 'tex/build', 'final_pdf': 'tex/build/main.pdf',
        'pdf_sha256': before['pdf_sha256'], 'all_source_template_and_input_hashes_unchanged': True,
        'user_main_tex_edit_preserved': True, 'output_and_dot_build_removed': not retired,
        'retired_directories_remaining': retired,
        'cleanup_status': 'blocked by execution safety policy' if retired else 'complete',
        'cache_files_pending_removal': before['removed_cache_files'] if retired else 0,
        'cache_bytes_pending_removal': before['removed_cache_bytes'] if retired else 0,
        'remote_push': False})
    print('Verified new active build directory and unchanged source/PDF; retired directory cleanup status recorded.', flush=True)


if __name__ == '__main__':
    {'prepare': prepare, 'finish': finish}[sys.argv[1]]()
