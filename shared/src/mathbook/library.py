"""Unified-library setup and isolated, non-publishing book compilation."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from .project import ProjectError, ProjectPaths, directory_manifest_hash, sha256_file, run_git, validate_book_id


def new_unified_book(project: ProjectPaths, book_id: str, source: Path) -> dict:
    """Create one contained book, without recreating a sibling workspace tree."""
    from .workflow import (read_projects, update_project_record, ProjectRecord,
        _pdf_signature_is_valid, _write_json, _write_empty_tsv, _book_status_text,
        TERM_COLUMNS, PROPER_NAME_COLUMNS, NOTATION_COLUMNS)
    validate_book_id(book_id)
    project.require_clean_main()
    source = source.resolve(strict=True)
    if source.suffix.lower() != '.pdf' or not _pdf_signature_is_valid(source):
        raise ProjectError('A valid source PDF is required.')
    book = project.book(book_id)
    if book.root.exists() or any(r.book_id == book_id for r in read_projects(project)):
        raise ProjectError('Book identity already exists; nothing was overwritten.')
    branch = 'book/' + book_id
    if run_git(project.root, ['show-ref', '--verify', '--quiet', 'refs/heads/'+branch], check=False).returncode == 0:
        raise ProjectError('A historical branch already uses this book identity.')
    book.ensure_structure()
    original_hash = sha256_file(source)
    shutil.copy2(source, book.source/source.name)
    assert original_hash == sha256_file(source) == sha256_file(book.source/source.name)
    shutil.copytree(project.template, book.root/'template')
    shutil.copy2(project.config/'template-manifest.json', book.root/'config/template-snapshot-manifest.json')
    defaults = json.loads((project.config/'default.yaml').read_text(encoding='utf8'))
    config = {'schema_version': 1, 'book_id': book_id, 'title': '', 'branch': branch,
        'worktree': str(project.root), 'phase': 'registration', 'status': 'registered',
        'source': {'path': 'input/source/'+source.name, 'sha256': original_hash},
        'template_version': defaults['template']['version'],
        'template_manifest_hash': directory_manifest_hash(book.template), 'final_output': ''}
    _write_json(book.config_file, config)
    _write_json(book.root/'config/library-binding.json', {'mode':'unified','book_id':book_id,
        'book_root':'books/'+book_id,'entry':'tex/main.tex','checkpoint_branch':branch})
    for path, columns in [(book.candidates,TERM_COLUMNS),(book.unresolved,TERM_COLUMNS),
                          (book.proper_names,PROPER_NAME_COLUMNS),(book.notation,NOTATION_COLUMNS)]:
        _write_empty_tsv(path, columns)
    book.issues.write_text('',encoding='utf8')
    _write_json(book.workflow_state, {'book_id':book_id,'status':'registered','completed_units':[],'blocking_issues':[]})
    book.status_file.write_text(_book_status_text(book_id,'registration','registered',original_hash,[]),encoding='utf8')
    book.plans_file.write_text('# Plan\n\nRun start-book with this explicit book-id; review its sample before full translation.\n',encoding='utf8')
    book.main_tex.write_text('\\documentclass[a4paper,UTF8,12pt]{ctexart}\n\\usepackage{Mystyle}\n\\usepackage{translation-adapter}\n\\input{translation-macros.tex}\n\\begin{document}\n\\end{document}\n',encoding='utf8')
    book.root.joinpath('README.md').write_text('# '+book_id+'\n\nEdit tex/main.tex and tex/chapters/. Source: input/source/. Pinned template: template/. Outputs: output/. Shared rules: ../../shared/AGENTS.md.\n',encoding='utf8')
    update_project_record(project,ProjectRecord(book_id,'','main',str(project.root),'registration','registered',original_hash,config['template_version'],'',''))
    run_git(project.root,['add','--','books/'+book_id,project.relative(project.projects_file)])
    run_git(project.root,['commit','-m','Register consolidated book '+book_id])
    run_git(project.root,['branch',branch])
    return {'book_id':book_id,'mode':'unified','workspace':str(project.root),
        'book_root':str(book.root),'active_branch':'main','checkpoint_branch':branch,'source_sha256':original_hash}


def build_book(project: ProjectPaths, book_id: str, *, driver: Path | None = None) -> dict:
    """Compile a copy into a new book-local directory; never replace final PDFs."""
    from .workflow import verify_book_context, _write_json
    book, _ = verify_book_context(project,book_id,writable=True)
    binding=json.loads((book.root/'config/library-binding.json').read_text(encoding='utf8'))
    entry=book.assert_write_path(book.root/binding['entry'])
    if not entry.is_file():raise ProjectError('Registered TeX entry is missing: '+str(entry))
    source=book.require_source_pdf();before=sha256_file(source)
    template_hash=directory_manifest_hash(book.template)
    env=os.environ.copy()
    # Entries with basename-only inputs need both chapter and generated paths.
    inputs=[book.template/'style',book.template/'reference',book.template/'assets',book.template/'adapter',
        book.template/'adapter/aljabr-1',book.template/'collections/aljabr-1/upstream',
        book.root/'tex',book.root/'tex/chapters',book.root/'tex/generated']
    env['TEXINPUTS']=os.pathsep.join(str(p) for p in inputs)+os.pathsep+os.pathsep
    env['BIBINPUTS']=os.pathsep.join(str(p) for p in inputs)+os.pathsep+os.pathsep
    stage=book.assert_write_path(Path(tempfile.mkdtemp(prefix='unified-build-',dir=book.root/'workspace/temporary')))
    fonts=book.template/'collections/aljabr-1/fonts/noto-sans-cjk-sc'
    if fonts.is_dir():
        fontconfig=stage/'fonts.conf'
        from xml.sax.saxutils import escape
        texvar=subprocess.check_output(['kpsewhich','--var-value=TEXMFSYSVAR'],text=True).strip()
        system=Path(texvar)/'fonts/conf/fonts.conf'
        if not system.is_file():raise ProjectError('TeX Live font configuration is unavailable.')
        fontconfig.write_text('<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><include ignore_missing="no">'+escape(system.as_posix())+'</include><dir>'+escape(fonts.as_posix())+'</dir><cachedir>'+escape((stage/'font-cache').as_posix())+'</cachedir></fontconfig>',encoding='utf8')
        env['FONTCONFIG_FILE']=str(fontconfig)
        manifest=json.loads((fonts/'manifest.json').read_text(encoding='utf8'))
        for row in manifest['files']:
            found=subprocess.check_output(['fc-match','-f','%{file}',f'Noto Sans CJK SC:style={row["weight"]}'],env=env,text=True,encoding='utf8')
            if sha256_file(Path(found))!=row['sha256']:raise ProjectError('Pinned Noto font did not resolve exactly.')
    if driver:
        command=[os.sys.executable,str(driver),str(entry),'--compiler','texlive','--engine','xelatex','--output-directory',str(stage),'--json']
    else:
        executable=shutil.which('latexmk')
        if not executable:raise ProjectError('latexmk is required for bibliography-aware clean builds.')
        command=[executable,'-xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-outdir='+str(stage),entry.name]
    # Compile in the master directory so graphics paths retain original meaning.
    result=subprocess.run(command,cwd=entry.parent,env=env,capture_output=True)
    log=stage/'build-driver.log';log.write_bytes(result.stdout+result.stderr)
    pdf=stage/(entry.stem+'.pdf')
    native_log=stage/(entry.stem+'.log')
    text=native_log.read_text(encoding='utf8',errors='replace') if native_log.exists() else ''
    warnings={name:re.findall(pattern,text,re.I) for name,pattern in {
        'undefined_references':r'LaTeX Warning: (?:Reference .* undefined|There were undefined references)',
        'duplicate_labels':r'multiply[- ]defined|destination with the same identifier',
        'missing_glyphs':r'Missing character:[^\n]*',
        'overfull_boxes':r'Overfull \\[hv]box[^\n]*'}.items()}
    if before!=sha256_file(source) or template_hash!=directory_manifest_hash(book.template):
        raise ProjectError('Read-only input integrity changed during build.')
    report={'book_id':book_id,'entry':binding['entry'],'success':result.returncode==0 and pdf.is_file(),
        'exit_code':result.returncode,'build_directory':str(stage),'candidate_pdf':str(pdf),
        'source_sha256':before,'template_hash':template_hash,'published':False,
        'log':str(log),'warnings':warnings,
        'scope':'Compilation and input integrity only; not translation/math/visual acceptance.'}
    _write_json(book.assert_write_path(book.root/'qa/unified-build.json'),report)
    if not report['success']:raise ProjectError('Book build failed; preserved log: '+str(log))
    return report
