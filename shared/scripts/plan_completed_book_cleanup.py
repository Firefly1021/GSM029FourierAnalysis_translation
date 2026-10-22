"""Inventory completed-project caches; planning only, never deletes files."""
import collections
import json
import os
import sys
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'shared/qa/integration-20261022'


def inventory():
    rows = []
    totals = collections.defaultdict(lambda: [0, 0])
    for base in [ROOT/'books', ROOT/'shared/.migration-backup', ROOT/'shared/.legacy-worktrees']:
        for current, dirs, files in os.walk(base):
            for directory in dirs:
                assert not Path(current, directory).is_symlink(), 'Unexpected link'
            for name in files:
                path = Path(current, name)
                assert not path.is_symlink(), 'Unexpected link'
                info = path.stat()
                relative = path.relative_to(ROOT).as_posix()
                parts = relative.split('/')
                group = '/'.join(parts[:3] if parts[0]=='books' else parts[:4])
                totals[group][0] += 1
                totals[group][1] += info.st_size
                rows.append({'path': relative, 'bytes': info.st_size, 'mtime_ns': info.st_mtime_ns})
    (REPORT/'cleanup-inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
    summary = {key: {'files':value[0], 'bytes':value[1]} for key,value in sorted(totals.items())}
    (REPORT/'cleanup-size-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    for key,value in sorted(totals.items(),key=lambda kv:kv[1][1],reverse=True)[:35]:
        print(f'{value[1]/1e9:.4f} GB {value[0]:7d} files {key}',flush=True)


def scratch():
    rows=json.loads((REPORT/'cleanup-inventory.json').read_text(encoding='utf8'))
    prefix='shared/.migration-backup/partial-cache-copies/'
    selected=[r for r in rows if r['path'].startswith(prefix)]
    assert selected and (ROOT/prefix).is_dir()
    plan={'library_root':str(ROOT),'authorization':'user-request-20261022-remove-completed-book-intermediates',
          'reason':'Task-created incomplete duplicate copies of derivative caches; authoritative originals already migrated and verified.',
          'allowed_prefixes':[prefix.rstrip('/')],
          'targets':[{'path':prefix.rstrip('/'),'files':len(selected),'bytes':sum(r['bytes'] for r in selected)}]}
    (REPORT/'scratch-cleanup-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(plan,ensure_ascii=False))


def completed():
    builds=json.loads((REPORT/'builds.json').read_text(encoding='utf8'))
    assert builds['passed'] and len(builds['results'])==7,'All seven clean builds must pass first.'
    protected=set();dependencies={};targets=[];removed=[];retained=[]
    for row in builds['results']:
        book=ROOT/'books'/row['book_id']
        stage=Path(row['build_directory'])
        entry=book/row['entry']
        fls=stage/(entry.stem+'.fls')
        assert fls.is_file(),fls
        dependency=set();cwd=entry.parent
        for line in fls.read_text(encoding='utf8',errors='replace').splitlines():
            if line.startswith('PWD '):cwd=Path(line[4:])
            if not line.startswith('INPUT '):continue
            path=Path(line[6:]);path=path if path.is_absolute() else cwd/path
            path=path.resolve()
            if path.is_relative_to(stage) or not path.is_relative_to(ROOT/'books'):continue
            assert path.is_relative_to(book),'Cross-book input: '+str(path)
            assert path.is_file(),path
            dependency.add(path)
        dependency.update(book.rglob('*.bib'))
        dependency.add(entry)
        protected.update(dependency)
        dependencies[row['book_id']]=[str(p.relative_to(ROOT)).replace('\\','/') for p in sorted(dependency)]
    (REPORT/'retained-build-dependencies.json').write_text(json.dumps(dependencies,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    intermediates={'.aux','.bcf','.blg','.fdb_latexmk','.fls','.idx','.ilg','.ind','.lof','.lot','.log','.nav','.out','.snm','.toc','.vrb','.xdv','.pyc'}
    for book in sorted((ROOT/'books').iterdir()):
        if not book.is_dir():continue
        binding=json.loads((book/'config/library-binding.json').read_text(encoding='utf8'))
        keep_outputs={binding['final_output']}
        if book.name=='finite-element-exterior-calculus':keep_outputs.add('output/book-zh.pdf')
        for current,dirs,files in os.walk(book):
            for name in files:
                path=Path(current,name);relative=path.relative_to(book).as_posix()
                assert not path.is_symlink()
                reason=None
                if relative.startswith(('input/','template/','template-accepted/')):pass
                elif path in protected:pass
                elif relative.startswith('workspace/') and not relative.startswith('workspace/crops/') and name!='.gitkeep':reason='Reproducible page/OCR/layout/build cache; restored English source retained.'
                elif relative.startswith(('workflow/','scripts/')):reason='Completed-book translation-only script; shared tools retained.'
                elif path.suffix in {'.py','.pyc'}:reason='Completed-book process script; not a recorded final-build input.'
                elif relative.startswith('output/') and relative not in keep_outputs and name!='.gitkeep':reason='Superseded sample, chapter preview, duplicate or rejected layout output.'
                elif path.suffix in intermediates or name.endswith(('.run.xml','.synctex.gz')):reason='Regenerable LaTeX or process intermediate.'
                elif relative.startswith('logs/') and name!='.gitkeep':reason='Historical process log; final QA retained.'
                elif relative.startswith('tex/generated/') and path.suffix in {'.tex','.pdf'}:reason='Unreferenced generated build wrapper or preview; actual macro inputs protected.'
                elif relative.startswith('tex/batch-') or relative=='tex/sample-main.tex':reason='Unused sample/batch master wrapper; complete chapter content retained.'
                if reason:
                    info=path.stat();removed.append({'path':path.relative_to(ROOT).as_posix(),'bytes':info.st_size,'reason':reason})
                else:
                    digest=hashlib.file_digest(path.open('rb'),'sha256').hexdigest()
                    retained.append({'path':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'sha256':digest})
        # Collapse fully selected cache directories to make native deletion efficient.
    selected={r['path']:r for r in removed}
    for book in sorted((ROOT/'books').iterdir()):
        if not book.is_dir():continue
        for relative in ['workspace/pages','workspace/raw-text','workspace/layout','workspace/formula-images','workspace/temporary','workspace/ocr','workflow','logs','output/archive','output/sample']:
            folder=book/relative
            if not folder.is_dir():continue
            files=[p for p in folder.rglob('*') if p.is_file()]
            # Directory markers are deliberately retained, so delete children instead.
            for child in sorted(folder.iterdir()):
                child_files=[p for p in child.rglob('*') if p.is_file()] if child.is_dir() else [child]
                keys=[p.relative_to(ROOT).as_posix() for p in child_files]
                if keys and all(key in selected for key in keys):
                    targets.append({'path':child.relative_to(ROOT).as_posix(),'files':len(keys),'bytes':sum(selected[k]['bytes'] for k in keys)})
                    for key in keys:selected.pop(key)
    targets.extend({'path':r['path'],'files':1,'bytes':r['bytes']} for r in selected.values())
    plan={'library_root':str(ROOT),'authorization':'user-request-20261022-remove-completed-book-intermediates',
          'allowed_prefixes':['books/'],'targets':targets,'files':len(removed),'bytes':sum(r['bytes'] for r in removed),
          'preserved_files':len(retained),'preserved_bytes':sum(r['bytes'] for r in retained),
          'recovery':'Tracked removed files are in local integration checkpoint 538012e. Derivative untracked caches must be regenerated from unchanged original PDFs.'}
    for name,value in [('completed-cleanup-plan.json',plan),('completed-cleanup-files.json',removed),('retained-core-manifest.json',retained)]:
        (REPORT/name).write_text(json.dumps(value,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in plan.items() if k!='targets'},ensure_ascii=False),flush=True)


def verification_cache():
    builds=json.loads((REPORT/'builds.json').read_text(encoding='utf8'))
    assert builds['passed'] and len(builds['results'])==7
    targets=[]
    for row in builds['results']:
        stage=Path(row['build_directory']).resolve()
        assert stage.is_relative_to(ROOT/'books'/row['book_id']/'workspace/temporary')
        files=[p for p in stage.rglob('*') if p.is_file()]
        targets.append({'path':stage.relative_to(ROOT).as_posix(),'files':len(files),'bytes':sum(p.stat().st_size for p in files)})
    for base in [ROOT/'shared/src',ROOT/'shared/tests',ROOT/'shared/scripts',ROOT/'shared/.pytest_cache']:
        candidates=[base] if base.name=='.pytest_cache' and base.is_dir() else list(base.rglob('__pycache__'))
        for folder in candidates:
            if not folder.is_dir():continue
            files=[p for p in folder.rglob('*') if p.is_file()]
            targets.append({'path':folder.relative_to(ROOT).as_posix(),'files':len(files),'bytes':sum(p.stat().st_size for p in files)})
    for archive in (ROOT/'shared/.legacy-worktrees').iterdir():
        if not archive.is_dir():continue
        ignored=subprocess.check_output(['git','-C',str(archive),'ls-files','--others','--ignored','--exclude-standard','-z']).decode('utf8').split('\0')
        for name in ignored:
            if not name:continue
            path=archive/name
            if path.is_file() and (path.suffix in {'.pyc','.log','.aux','.out','.bcf','.xdv'} or '/__pycache__/' in '/'+name or name.startswith(('.pytest_cache/','$build/','$out/'))):
                targets.append({'path':path.relative_to(ROOT).as_posix(),'files':1,'bytes':path.stat().st_size})
    plan={'library_root':str(ROOT),'authorization':'user-request-20261022-remove-completed-book-intermediates',
          'allowed_prefixes':['books/','shared/src/','shared/tests/','shared/scripts/','shared/.pytest_cache','shared/.legacy-worktrees/'],'targets':targets}
    (REPORT/'verification-cache-cleanup-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'targets':len(targets),'files':sum(t['files'] for t in targets),'bytes':sum(t['bytes'] for t in targets)}),flush=True)


if __name__=='__main__':
    {'inventory':inventory,'scratch':scratch,'completed':completed,'verification-cache':verification_cache}[sys.argv[1] if len(sys.argv)>1 else 'inventory']()
