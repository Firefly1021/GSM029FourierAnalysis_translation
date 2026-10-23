"""Prepare a single AJbook edition; no semantic math/text rewriting."""
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];BOOK=ROOT/'books/finite-element-exterior-calculus'
AUDIT=ROOT/'shared/qa/feec-production-20261023';STAGE=AUDIT/'prepared'
sys.path.insert(0,str(ROOT/'shared/src'))
from mathbook.project import sha256_file

MATH_ENV=r'(?:equation|align|alignat|gather|multline|flalign|displaymath|math)\*?'
DECLARATION=re.compile(r'\\(?:tiny|small|footnotesize|scriptsize|large|Large|LARGE|huge|Huge|normalsize|bfseries|mdseries|itshape|upshape|sffamily|rmfamily|ttfamily|color|fontsize|selectfont|kaishu|songti|heiti|fangsong|emergencystretch|setlength|addtolength|def|let|renewcommand|newcommand)\b')

def math_spans(source):
    spans=[];i=0
    while i<len(source):
        if source[i]=='%' and (i==0 or source[i-1]!='\\'):
            end=source.find('\n',i);i=len(source) if end<0 else end+1;continue
        marker=None;end=None
        if source.startswith('\\[',i):marker='\\[';end='\\]'
        elif source.startswith('\\(',i):marker='\\(';end='\\)'
        elif source[i]=='$' and (i==0 or source[i-1]!='\\'):
            marker='$$' if source.startswith('$$',i) else '$';end=marker
        else:
            match=re.match(r'\\begin\{('+MATH_ENV+r')\}',source[i:])
            if match:marker=match.group(0);end='\\end{'+match.group(1)+'}'
        if marker:
            j=i+len(marker)
            while True:
                j=source.find(end,j)
                assert j>=0,'Unclosed math region at '+str(i)
                if end not in {'$','$$'} or j==0 or source[j-1]!='\\':break
                j+=len(end)
            spans.append((i,j+len(end),source[i:j+len(end)]));i=j+len(end)
        else:i+=1
    return spans

def strip_comments(source):
    return '\n'.join(re.sub(r'(?<!\\)%.*$','',line) for line in source.splitlines())

def strip_comment_lines(source):
    # End-of-line % controls TeX whitespace and is not a provenance annotation.
    return '\n'.join(line for line in source.splitlines() if not line.lstrip().startswith('%'))

def projection(source):
    value=strip_comments(source)
    value=re.sub(r'(?<!\\)[{}]','',value)
    return re.sub(r'\s+','',value)

def close_group(text,start):
    assert text[start]=='{';depth=0;i=start
    while i<len(text):
        if text[i]=='\\':
            i+=2;continue
        if text[i]=='{':depth+=1
        elif text[i]=='}':
            depth-=1
            if not depth:return i
        i+=1
    return -1

def clean(source):
    source=source.replace('\r\n','\n');spans=math_spans(source)
    protected=source
    for n,(start,end,payload) in reversed(list(enumerate(spans))):
        protected=protected[:start]+f'\x00M{n}\x00'+protected[end:]
    stats={'comment_lines_removed':0,'paragraph_groups_removed':0,'argument_groups_removed':0,'cell_or_text_groups_removed':0,'declaration_argument_groups_removed':0,'display_leading_blank_lines_removed':0}
    lines=[]
    for line in protected.splitlines():
        if line.lstrip().startswith('%'):
            stats['comment_lines_removed']+=1;continue
        value=line.strip();suffix=''
        if value.endswith('%') and not value.endswith('\\%'):
            value=value[:-1].rstrip();suffix='%'
        while value.startswith('{') and close_group(value,0)==len(value)-1 and not DECLARATION.search(value[1:-1]):
            value=value[1:-1];stats['paragraph_groups_removed']+=1
        value,n=re.subn(r'(^|&)\{([^{}\\\n]+)\}(?=&|\\\\|\\par\b|$)',r'\1\2',value)
        stats['cell_or_text_groups_removed']+=n
        value,n=re.subn(r'\\(LARGE|Large|large)\{([^{}\\]+)\}',r'\\\1 \2',value)
        stats['declaration_argument_groups_removed']+=n
        # Strip only the redundant group enclosing a whole heading/caption argument.
        offset=0
        while True:
            match=re.search(r'\\(?:chapter|section|subsection|subsubsection|paragraph|caption|indexprologue)\*?(?:\[[^\]]*\])?\s*\{',value[offset:])
            if not match:break
            start=offset+match.end()-1;end=close_group(value,start)
            if end<0:break
            inner=value[start+1:end]
            if inner.startswith('{') and close_group(inner,0)==len(inner)-1 and not DECLARATION.search(inner[1:-1]):
                value=value[:start+1]+inner[1:-1]+value[end:];stats['argument_groups_removed']+=1
            offset=start+1
        if value.startswith('\x00M'):
            n=int(re.match(r'\x00M(\d+)\x00',value).group(1));payload=spans[n][2]
            if payload.startswith(('\\[','\\begin{')):
                while lines and not lines[-1].strip():
                    lines.pop();stats['display_leading_blank_lines_removed']+=1
        lines.append(value+suffix)
    value='\n'.join(lines)
    value=re.sub(r'\n{3,}','\n\n',value).strip()+'\n'
    for n,(_,_,payload) in enumerate(spans):value=value.replace(f'\x00M{n}\x00',payload)
    assert projection(source)==projection(value),'Non-formatting token change'
    before=[p for _,_,p in spans];after=[p for _,_,p in math_spans(value)]
    assert before==after,'Math region changed'
    stats['math_regions_unchanged']=len(before)
    return value,stats

def put(relative,data):
    target=STAGE/relative;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(data if isinstance(data,bytes) else data.encode('utf8'))

def prepare():
    AUDIT.mkdir(parents=True,exist_ok=True)
    baseline=json.loads((AUDIT/'baseline-build.json').read_text(encoding='utf8'))
    assert baseline['success']
    source=BOOK/'tex/generated/aljabr-layout';mapping={};stats=[]
    for path in sorted(source.glob('*.tex')):
        name=path.name
        if name=='frontmatter.tex':relative='tex/frontmatter/preface.tex'
        elif name=='publication.tex':relative='tex/frontmatter/publication.tex'
        elif name in {'bibliography.tex','index.tex'}:relative='tex/backmatter/'+name
        else:
            if name=='sample.tex':name='chapter-02-sections-04-06.tex'
            relative='tex/chapters/'+name
        original=path.read_text(encoding='utf8')
        formatted,record=clean(original)
        put(relative,formatted);mapping[path.relative_to(BOOK/'tex').as_posix()]=relative[len('tex/'):]
        stats.append({'old':path.relative_to(BOOK).as_posix(),'new':relative,**record})
    figure=BOOK/'tex/figures/cohomology-geometry.tex'
    if figure.is_file():
        formatted,record=clean(figure.read_text(encoding='utf8'));put('tex/figures/'+figure.name,formatted)
        stats.append({'old':figure.relative_to(BOOK).as_posix(),'new':'tex/figures/'+figure.name,**record})
    master=(BOOK/'tex/aljabr-main.tex').read_text(encoding='utf8')
    # Remove the non-source implementation/translation-workflow colophon; retain attribution in README and PDF metadata.
    footer=master.index('\\clearpage\\thispagestyle{empty}\\vspace*{\\fill}')
    master=master[:footer]+'\\end{document}\n'
    master=master.replace('\\input{generated/orthogonal-sum-macro.tex}','\\input{macros.tex}')
    master=master.replace('\\input{translation-macros.tex}\n','')
    for old,new in mapping.items():master=master.replace('\\input{'+old+'}','\\input{'+new+'}')
    master=master.replace('pdfauthor={Douglas N. Arnold}',
        'pdfauthor={Douglas N. Arnold},pdfsubject={AJbook template by Wen-Wei Li; CC BY 4.0; https://github.com/wenweili/AlJabr-1}')
    master,_=clean(master);put('tex/main.tex',master)
    macros=(BOOK/'tex/generated/orthogonal-sum-macro.tex').read_text(encoding='utf8')
    put('tex/macros.tex',strip_comments(macros).strip()+'\n')
    upstream=BOOK/'template/collections/aljabr-1/upstream'
    # Read the actual clean-build recorder, rather than retaining unrelated sample books.
    fls=Path(baseline['build_directory'])/'aljabr-main.fls';used=set()
    for line in fls.read_text(encoding='utf8',errors='replace').splitlines():
        if line.startswith('INPUT '):
            path=Path(line[6:])
            if not path.is_absolute():path=BOOK/'tex'/path
            path=path.resolve()
            if path.is_relative_to(upstream) and path.is_file():used.add(path)
    used.add(upstream/'LICENSE')
    # Bibliography databases are read by biber, not the TeX .fls recorder.
    used.add(upstream/'Al-jabr.bib')
    for path in sorted(used):put('template/'+path.relative_to(upstream).as_posix(),path.read_bytes())
    for name in ('feec-aljabr.sty','feec-fonts.tex'):
        original=(BOOK/'template/adapter/aljabr-1'/name).read_text(encoding='utf8')
        cleaned=strip_comment_lines(original)
        cleaned=re.sub(r'^\\providecommand\{\\MathBook(?:SourcePage|FormulaID|ReviewStatus)\}\[1\]\{\}\s*\n','',cleaned,flags=re.M)
        put('template/'+name,re.sub(r'\n{3,}','\n\n',cleaned).strip()+'\n')
    fonts=BOOK/'template/collections/aljabr-1/fonts/noto-sans-cjk-sc'
    for path in fonts.iterdir():
        if path.is_file():put('template/fonts/noto-sans-cjk-sc/'+path.name,path.read_bytes())
    inventory=[]
    for path in sorted(BOOK.rglob('*')):
        if path.is_file() and '.build' not in path.relative_to(BOOK).parts:
            inventory.append({'path':path.relative_to(BOOK).as_posix(),'bytes':path.stat().st_size,'sha256':sha256_file(path)})
    plan={'book_id':'finite-element-exterior-calculus','book_root':str(BOOK),'source_baseline_head':
        __import__('subprocess').check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'discard_user_modified_legacy_chapter':True,'inventory':inventory,'formatting':stats,
        'upstream_files_kept_byte_exact':[p.name for p in sorted(used)],
        'prepared_files':[{'path':p.relative_to(STAGE).as_posix(),'bytes':p.stat().st_size,'sha256':sha256_file(p)} for p in sorted(STAGE.rglob('*')) if p.is_file()]}
    (AUDIT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'body_files':len(stats),'prepared_files':len(plan['prepared_files']),
        'totals':{key:sum(r[key] for r in stats) for key in stats[0] if key not in {'old','new'}},
        'upstream_files':plan['upstream_files_kept_byte_exact']},ensure_ascii=False),flush=True)

if __name__=='__main__':prepare()
