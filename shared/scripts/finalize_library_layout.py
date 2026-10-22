"""Finish migration metadata; never rewrite accepted source, prose, or math."""
import csv, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SYSTEM=ROOT/'shared';REPORT=SYSTEM/'qa/integration-20261022'
sys.path.insert(0,str(SYSTEM/'src'))
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import read_projects,write_projects,ProjectRecord

def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

def main():
    rows=json.loads((REPORT/'copied-books.json').read_text(encoding='utf8'))
    assert len(rows)==7 and (REPORT/'shared-relocation.json').is_file()
    save(SYSTEM/'config/library-layout.json',{'schema_version':1,'mode':'unified',
        'shared':'shared','books':'books','active_branch':'main','historical_book_branches':'preserved',
        'legacy_worktrees':'shared/.legacy-worktrees','migration_report':'shared/qa/integration-20261022'})
    save(SYSTEM/'config/runtime.local.json',{'python':sys.executable,'note':'Local runtime selection; not committed or required on another machine.'})
    project=ProjectPaths(ROOT);old={r.book_id:r for r in read_projects(project)};records=[]
    bindings=[]
    for row in rows:
        book=project.book(row['id']);book.ensure_structure();cfg=book.load_config();prior=old[row['id']]
        entry='tex/main.tex'
        if cfg.get('typesetting',{}).get('entry'):entry=cfg['typesetting']['entry']
        elif row['id']=='finite-element-methods-for-navier-stokes-equations-theory-and-algorithms':entry='tex/generated/full-book.tex'
        assert (book.root/entry).is_file(),entry
        # The full-book driver of this scanned book was wrongly only a cache.
        # Pin its exact bytes as an ordinary source entry, without editing it.
        if entry=='tex/generated/full-book.tex':
            from shutil import copy2
            pinned=book.assert_write_path(book.root/'tex/full-book.tex')
            if not pinned.exists():copy2(book.root/entry,pinned)
            assert sha256_file(pinned)==sha256_file(book.root/entry)
            entry='tex/full-book.tex'
        binding={'mode':'unified','book_id':row['id'],'book_root':row['book_root'],'entry':entry,'active_branch':'main',
            'template':'template','template_hash':directory_manifest_hash(book.template),
            'historical_config_template_hash':cfg.get('template_manifest_hash'),
            'snapshot_matches_historical_config_hash':directory_manifest_hash(book.template)==cfg.get('template_manifest_hash'),
            'original_branch':row['branch'],'original_worktree':row['checkout'],
            'original_config_sha256':row['original_config_sha256'],
            'legacy_worktree':'shared/.legacy-worktrees/'+row['id'],
            'final_output':cfg.get('final_output') or (prior.final_output.split(row['book_root']+'/',1)[-1] if prior.final_output else ''),
            'note':'Original config/status/QA paths are historical evidence; this binding governs current locations.'}
        if binding['final_output']:assert (book.root/binding['final_output']).is_file()
        save(book.assert_write_path(book.root/'config/library-binding.json'),binding);bindings.append(binding)
        blocks=cfg.get('blocking_issues',prior.blocking_issues)
        if isinstance(blocks,list):blocks='; '.join(blocks)
        final=(row['book_root']+'/'+binding['final_output']) if binding['final_output'] else ''
        records.append(ProjectRecord(row['id'],row['title'],'main',str(ROOT),row['phase'],row['status'],
            row['source_sha256'],row['template_version'],final,str(blocks or '')))
        guide=book.assert_write_path(book.root/'OPEN-THIS-BOOK.md')
        guide.write_text('# '+row['title']+'\n\n'
            '这是本书唯一的日常编辑目录. 用 VS Code 打开本目录即可, 不再打开历史 worktree.\n\n'
            '- 正式 TeX 入口: ['+entry+']('+entry+').\n'
            '- 章节: [tex/chapters/](tex/chapters/). 图片: [tex/figures/](tex/figures/); 保留原有图片引用方式.\n'
            '- 原始 PDF: [input/source/](input/source/), 只读.\n'
            '- 本书实际模板快照: [template/](template/), 不自动跟随共享模板更新.\n'
            '- 当前正式输出: ['+binding['final_output']+']('+binding['final_output']+').\n'
            '- 恢复原稿、译文、公式、术语、QA、日志和扫描缓存各在原有同名目录, 没有删节或重新翻译.\n\n'
            '编译: VS Code 运行“编译本书”任务, 或在总目录运行:\n\n'
            '```powershell\n.\\shared\\scripts\\mathbook.ps1 build-book '+row['id']+'\n```\n\n'
            '新构建只写本书临时目录, 不自动覆盖正式 PDF. 历史 config/book.yaml、PROJECT_STATUS 和 QA 中的旧绝对路径保留为证据; 当前位置以 config/library-binding.json 和共享 PROJECTS.md 为准.\n\n'
            '共享规则: [../../shared/AGENTS.md](../../shared/AGENTS.md). Git 提交与推送在总目录统一进行; 不自动推送.\n',encoding='utf8') if not guide.exists() else None
        task={'version':'2.0.0','tasks':[{'label':'编译本书','type':'process','command':'powershell.exe',
            'args':['-NoProfile','-ExecutionPolicy','Bypass','-File','${workspaceFolder}/../../shared/scripts/mathbook.ps1','build-book',row['id']],
            'options':{'cwd':'${workspaceFolder}'},'problemMatcher':[], 'group':{'kind':'build','isDefault':True}}]}
        tasks=book.assert_write_path(book.root/'.vscode/tasks.json')
        if tasks.exists():assert json.loads(tasks.read_text(encoding='utf8'))==task,'Preserve user editor task changes.'
        else:save(tasks,task)
    write_projects(project,records)
    save(REPORT/'current-bindings.json',bindings)
    workspace={'folders':[{'name':r.title,'path':'../books/'+r.book_id} for r in records]+[{'name':'共享项目','path':'.'}],
        'settings':{'files.exclude':{'.legacy-worktrees':True,'.migration-backup':True}}}
    save(SYSTEM/'BOOKTRANSLATION.code-workspace',workspace)
    # Preserve the original guide instead of replacing it without a history copy.
    readme=SYSTEM/'README.md';original=REPORT/'README-before.md'
    if not original.exists():original.write_bytes(readme.read_bytes())
    print('Bindings and registry updated for',len(records),'books; old reports remain byte-exact.')

if __name__=='__main__':main()
