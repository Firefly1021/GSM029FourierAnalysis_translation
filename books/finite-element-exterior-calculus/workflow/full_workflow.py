"""Per-book full translation orchestration. Content is authored, never inferred here."""
from __future__ import annotations
import argparse,collections,csv,hashlib,json,os,re,runpy,shutil,subprocess,sys,tempfile
from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw
s=runpy.run_path(str(Path(__file__).with_name("sample_processor.py")))
P,B,ID=s["P"],s["B"],s["ID"]
write,dump,load=s["write"],s["dump"],s["load"]
SAMPLE_TEX="778a5d245fa48042936a180078150ac27e02fa6a52becfccd9218a711a1bc432"
SAMPLE_PDF="af2e58b629a6be9dbde698544d4c2a6419c2545a6b7c8295c63b9868179a366c"
def guard():
    s["guard"]()
    assert s["m"]["sha256_file"](B.root/"tex/chapters/sample.tex")==SAMPLE_TEX
    assert s["m"]["sha256_file"](B.root/"output/sample-zh.pdf")==SAMPLE_PDF
    if (B.root/"qa/full-input-protection.json").exists():
        for item in load("qa/full-input-protection.json")["accepted_files"]:assert s["m"]["sha256_file"](B.root/item["file"])==item["sha256"],item["file"]
def begin():
    guard();cfg=B.load_config();cfg.update({"phase":"translation","status":"translating","sample_approved":True});dump("config/book.yaml",cfg)
    qa=load("qa/sample-qa.json");qa.update({"sample_user_approved":True,"approval_evidence":"User: 可以, 接下来进入全书翻译"});dump("qa/sample-qa.json",qa)
    state=load("qa/workflow-state.json");assert state["status"] in ("ready-for-full-translation","translating")
    state.update({"status":"translating","sample_approved":True,"next_unit":"frontmatter"})
    for unit in ("chapter-02-section-04","chapter-02-section-05","chapter-02-section-06"):
        if unit not in state["completed_units"]:state["completed_units"].append(unit)
    dump("qa/workflow-state.json",state)
    rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for row in rows:
        if row["QA Status"]=="passed":row["Notes"]="User-approved sample; preserve reviewed/sample.tex unchanged; Section 2.6 excludes separate Box 2.1"
        elif "sample-only scope" in row["Notes"]:row["Notes"]="Not translated; authorized full-book workflow pending"
    s["tsv"]("qa/chapter-progress.tsv",["Unit ID","Title","QA Status","Notes"],rows)
    dump("qa/full-input-protection.json",{"source_sha256":cfg["source"]["sha256"],"template_hash":cfg["template_manifest_hash"],"sample_tex_sha256":SAMPLE_TEX,"sample_pdf_sha256":SAMPLE_PDF,"accepted_files":[{"file":str(f.relative_to(B.root)).replace("\\","/"),"sha256":s["m"]["sha256_file"](f)} for f in [B.root/"translation/draft/sample.bilingual.tex",B.root/"translation/reviewed/sample.tex",B.root/"structured/reviewed/sample.tex",B.root/"tex/chapters/sample.tex",B.root/"formulae/sample.jsonl"]]})
    status()
def status():
    from mathbook.workflow import next_incomplete_unit
    rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));passed=[x["Unit ID"] for x in rows if x["QA Status"]=="passed"]
    write("PROJECT_STATUS.md",f"Book ID: {ID}\nTitle: Finite Element Exterior Calculus\nBranch: {P.git_branch()}\nWorktree: {P.root}\nPhase: translation\nStatus: translating\nSource SHA-256: {B.load_config()['source']['sha256']}\nSample approved: Yes\nPassed units: {len(passed)}/{len(rows)}\nCompleted units: {', '.join(passed)}\nNext incomplete unit: {next_incomplete_unit(B)}\nBlocking issues: None\nProgress output: output/translation-progress.pdf\nFull-book translation complete: No\nRemote push: No\n")
def extract(first,last):
    guard();r=PdfReader(B.require_source_pdf());out=B.assert_write_path(B.root/"workspace/pages/source");out.mkdir(parents=True,exist_ok=True)
    for n in range(first,last+1):
        write(f"workspace/raw-text/full/pdf-{n:03}.txt",r.pages[n-1].extract_text() or "")
        img=out/f"pdf-{n:03}.png"
        if not img.exists():subprocess.run([shutil.which("pdftoppm"),"-f",str(n),"-l",str(n),"-r","150","-singlefile","-png",str(B.require_source_pdf()),str(img.with_suffix(""))],check=True)
    guard();print("Source pages rendered and raw text saved as unreviewed input",first,last)
def metadata(unit):
    guard();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    if unit=="publication":
        assert not any(x["file"]=="translation/authored/publication.bilingual.tex" for x in load("qa/full-input-protection.json")["accepted_files"]),"Never regenerate accepted publication supplement"
    else:assert next(x for x in rows if x["Unit ID"]==unit)["QA Status"]!="passed","Never regenerate passed content"
    text=(B.root/f"translation/authored/{unit}.bilingual.tex").read_text(encoding="utf8");en,zh=s["language"](text,0),s["language"](text,1);em,zm=list(s["MARK"].finditer(en)),list(s["MARK"].finditer(zh))
    source=[];target=[];formulae=[];provenance=[]
    for j,(a,b) in enumerate(zip(em,zm)):
        assert a.groups()==b.groups();e=en[a.end():em[j+1].start() if j+1<len(em) else len(en)].strip();z=zh[b.end():zm[j+1].start() if j+1<len(zm) else len(zh)].strip();assert collections.Counter(s["maths"](e))==collections.Counter(s["maths"](z)),a[1]
        pages=list(map(int,a[2].split(",")));ids=[]
        for k,(h,norm) in enumerate(zip(s["MATH"].finditer(e),s["maths"](e)),1):
            key="formula-"+hashlib.sha256(f"{ID}:{unit}:{a[1]}:{k}".encode()).hexdigest()[:16];ids.append(key);latex=next(x for x in h.groups() if x is not None);label=re.search(r"\\label\{([^}]+)\}",latex)
            formulae.append({"id":key,"source_latex":latex,"tokens":re.findall(r"\\[A-Za-z]+|\\.|[^\s]",norm),"source_location":{"page":pages[0],"bbox":[55,54,430,675]},"confidence":0.99,"review_status":"reviewed","label":label[1] if label else None,"number":None})
        row={"id":a[1],"block_type":a[3],"source_text":e,"source_location":{"page":pages[0],"bbox":[55,54,430,675]},"confidence":0.99,"review_status":"reviewed","formula_ids":ids};source.append(row);target.append({**row,"translated_text":z});provenance.append({"id":a[1],"source_pdf_pages":pages,"printed_pages":[PdfReader(B.require_source_pdf()).page_labels[p-1] for p in pages],"image_paths":[f"workspace/pages/source/pdf-{p:03}.png" for p in pages],"bbox_precision":"page-body region, not token-tight","formula_ids":ids})
    assert len(em)==len(zm)==len(source)>0
    for rel,value in [(f"structured/reviewed/{unit}.jsonl",source),(f"translation/reviewed/{unit}.jsonl",target),(f"formulae/{unit}.jsonl",formulae)]:write(rel,"".join(json.dumps(x,ensure_ascii=False)+"\n" for x in value))
    for rel,value in [(f"structured/reviewed/{unit}.tex",en),(f"translation/reviewed/{unit}.tex",zh),("tex/frontmatter.tex" if unit=="frontmatter" else f"tex/chapters/{unit}.tex",zh)]:write(rel,value)
    for record in source+target:s["jsonschema"].validate(record,json.loads((P.root/"schemas/text-block.schema.json").read_text(encoding="utf8")))
    for record in formulae:s["jsonschema"].validate(record,json.loads((P.root/"schemas/formula.schema.json").read_text(encoding="utf8")))
    dump(f"structured/source/{unit}-provenance.json",provenance);dump(f"qa/batches/{unit}-content.json",{"unit":unit,"blocks":len(source),"math_expressions":len(formulae),"passed":True,"visual_review":"pending"});print(unit,len(source),"blocks",len(formulae),"math")
CHAPTERS={1:("introduction",11),2:("homological-algebra",21),3:("unbounded-operators",31),4:("hilbert-complexes",43),5:("approximation-hilbert-complexes",61),6:("exterior-calculus",73),7:("finite-element-differential-forms",91),8:("further-directions",107)}
def assemble(final=False):
    guard();text=r"""\documentclass[a4paper,UTF8,12pt]{ctexart}
\usepackage{Mystyle}
\usepackage{translation-adapter}
\usepackage{tikz-cd}
\usepackage{needspace}
\usetikzlibrary{matrix,decorations.pathreplacing,calc}
\input{generated/orthogonal-sum-macro.tex}
\input{translation-macros.tex}
\setcounter{secnumdepth}{3}
\counterwithin{figure}{section}
\counterwithin{table}{section}
\newcounter{booksummary}[section]
\renewcommand{\thebooksummary}{\thesection.\arabic{booksummary}}
\newcommand{\BookCite}[1]{\hyperref[bib:source-#1]{[\ref*{bib:source-#1}]}}
\newcommand{\BookNumber}[1]{\hyperref[bib:source-#1]{\ref*{bib:source-#1}}}
\begin{document}
\begin{center}{\Large Finite Element Exterior Calculus}\\中文翻译进度稿\end{center}
\noindent 本稿只收录已通过内容核验并纳入当前编译批次的译文. 文末源文定位表不表示相应内容已经译完.\par
"""
    if final:
        text=text.split(r"\begin{document}")[0]+r"""\usepackage{refcount}
\setcounter{tocdepth}{2}
\newcommand{\BookContentsEntry}[2]{\addtocontents{toc}{\protect\contentsline{section}{#1}{\protect\pageref*{#2}}{\getrefbykeydefault{#2}{anchor}{}}}}
\begin{document}
\input{chapters/publication.tex}
\tableofcontents\clearpage
\BookContentsEntry{前言}{sec:preface}
"""
    contents=[]
    if final:contents.append((B.root/"tex/chapters/publication.tex").read_text(encoding="utf8"))
    if (B.root/"tex/frontmatter.tex").exists():text+=r"\input{frontmatter.tex}"+"\n";contents.append((B.root/"tex/frontmatter.tex").read_text(encoding="utf8"))
    chapter_files=sorted((B.root/"tex/chapters").glob("chapter-*.tex"))
    sample_inserted=False
    def insert_sample():
        nonlocal text,sample_inserted
        if not (B.root/"tex/chapters/chapter-02-introduction.tex").exists():
            text+=r"\clearpage\setcounter{section}{1}\section{同调代数的基本概念}\label{chap:homological-algebra}"+"\n"
        text+=r"\setcounter{subsection}{3}\setcounter{equation}{0}\setcounter{statement}{0}\input{chapters/sample.tex}"+"\n"
        contents.append((B.root/"tex/chapters/sample.tex").read_text(encoding="utf8"));sample_inserted=True
    for file in chapter_files:
        # Preserve the sample bytes and place Sections 2.4-2.6 after 2.3, before
        # Box 2.1 or Chapter 3, rather than appending them after later chapters.
        if not sample_inserted and (file.name=="chapter-02-summary.tex" or file.name[:10]>"chapter-02"):
            insert_sample()
        text+=r"\input{chapters/"+file.name+"}\n";contents.append(file.read_text(encoding="utf8"))
    if not sample_inserted:insert_sample()
    for name in ("bibliography","index"):
        file=B.root/f"tex/chapters/{name}.tex"
        if file.exists():
            if final:text+=r"\BookContentsEntry{"+{"bibliography":"参考文献","index":"索引"}[name]+"}{back:"+name+"}\n"
            text+=r"\input{chapters/"+file.name+"}\n";contents.append(file.read_text(encoding="utf8"))
    labels=set(re.findall(r"\\label\{([^}]+)\}","\n".join(contents)))|{"chap:homological-algebra"}
    refs=set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}","\n".join(contents)))
    cited=set(re.findall(r"\\Book(?:Cite|Number)\{(\d+)\}","\n".join(contents)));refs|={"bib:source-"+x for x in cited}
    known={"chap:"+key:(str(n),page,"Chapter "+str(n)) for n,(key,page) in CHAPTERS.items()}
    known.update({"sec:whitney-forms-de-rham":("7.6",100,"The Whitney forms and de Rham's theorem"),"bib:cartan-differential-expressions":("27",124,"Reference [27]")})
    known.update({"sec:complete-polynomial-forms":("7.1",92,"The complete polynomial spaces of differential forms"),"sec:primal-galerkin":("5.1",61,"Galerkin discretization of the primal formulation"),"sec:mixed-methods":("5.2",64,"Mixed methods of discretization"),"sec:eigenvalue-problems":("8.1",107,"Eigenvalue problems"),"fig:primal-lagrange-failure":("5.1",63,"Figure 5.1")})
    known["sec:l2-de-rham-complex"]=("4.3",47,"The L2 de Rham complex")
    known["sec:maxwell-equations"]=("8.6",113,"Maxwell's equations")
    known["box:hilbert-complexes-summary"]=("4.1",60,"Box 4.1: Summary of Hilbert complexes")
    known["box:approximation-hilbert-summary"]=("5.1",72,"Box 5.1: Summary of approximation of Hilbert complexes")
    known.update({"sec:finite-element-differential-forms":("7.4",96,"Finite element differential forms"),"sec:koszul-complex":("7.2",93,"The Koszul complex"),"sec:trimmed-polynomial-forms":("7.3",95,"The trimmed polynomial spaces of differential forms"),"sec:finite-element-space-properties":("7.5",98,"Properties of the finite element spaces"),"sec:cubical-elements":("7.7",101,"Cubical elements"),"sec:historical-antecedents":("7.8",103,"Historical antecedents")})
    r=PdfReader(B.require_source_pdf())
    for p in range(123,129):
        for h in re.finditer(r"(?m)^\[(\d+)\]",r.pages[p-1].extract_text() or ""):known["bib:source-"+h[1]]=(h[1],p,"Reference ["+h[1]+"]")
    missing=sorted(refs-labels);assert set(missing)<=set(known),set(missing)-set(known)
    if final:assert not missing,missing
    else:text+=r"\clearpage\section*{尚未翻译部分的源文定位}"+"\n"+r"以下仅登记已核实的原文引用目标, 并非这些部分的译文."+"\n"
    records=[]
    for key in missing:
        num,page,title=known[key];text+=r"\subsection*{"+title+"}\n"+r"\makeatletter\phantomsection\def\@currentlabel{"+num+r"}\label{"+key+r"}\makeatother"+"\n"+f"Source PDF {page}, printed {r.page_labels[page-1]}.\\par\n";records.append({"label":key,"source_number":num,"pdf_page":page,"printed_page":r.page_labels[page-1],"verified_source_locator_not_translation":True})
    text+=r"\end{document}"+"\n";write("tex/main.tex",text);dump("qa/pending-reference-targets.json",records)
def compile_batch():
    guard()
    if (B.root/"config/math-alphabet-policy.json").exists():
        from mathbook.build import canonical_tex_files
        for file in canonical_tex_files(B):assert not re.search(r"\\(?:mathfrak|frak)\b",file.read_text(encoding="utf8")),f"User prohibits Fraktur: {file}"
    out=Path(tempfile.mkdtemp(prefix="full-build-",dir=B.assert_write_path(B.root/"workspace/temporary")));env=os.environ.copy();env["PYTHONUTF8"]="1";env["PYTHONIOENCODING"]="utf-8";env["TEXINPUTS"]=os.pathsep.join(str(p) for p in [P.template/"style",P.template/"adapter",P.template/"assets",B.root/"tex"])+os.pathsep+os.pathsep
    dump("qa/latest-compilation.json",{"success":False,"status":"building","build_directory":str(out),"published_progress_pdf_updated":False})
    driver=r"C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py";r=subprocess.run([sys.executable,driver,str(B.main_tex),"--compiler","texlive","--engine","xelatex","--output-directory",str(out),"--json"],env=env,capture_output=True);write("logs/latest-build-driver.log",(r.stdout+r.stderr).decode("utf8",errors="replace"));assert r.returncode==0,(r.stdout+r.stderr).decode("utf8",errors="replace")[-4000:]
    r=subprocess.run([shutil.which("xelatex"),"-interaction=nonstopmode","-halt-on-error","-file-line-error",f"-output-directory={out}",str(B.main_tex)],cwd=B.root/"tex",env=env,capture_output=True);log=(out/"main.log").read_text(encoding="utf8",errors="replace");write("logs/latest-compilation.log",log);assert r.returncode==0,r.stdout.decode("utf8",errors="replace")[-3000:]
    qa=s["latex_qa"](B);warnings={k:len(re.findall(pattern,log,re.I)) for k,pattern in {"undefined":r"undefined references?|Reference .* undefined","duplicate":r"multiply[- ]defined","missing_glyph":r"Missing character:","overfull":r"Overfull \\[hv]box"}.items()}
    from mathbook.build import canonical_tex_files
    input_files=[{"path":f.relative_to(B.root).as_posix(),"sha256":s["m"]["sha256_file"](f)} for f in canonical_tex_files(B)]
    dump("qa/latest-compilation.json",{"success":qa["passed"] and not any(warnings.values()),"build_directory":str(out),"minimum_latex_rounds":2,"warnings":warnings,"latex_qa":qa,"input_files":input_files,"candidate_pdf":str(out/"main.pdf"),"published_progress_pdf_updated":False})
    assert qa["passed"] and not any(warnings.values()),(qa,warnings)
    pdf=B.assert_write_path(B.root/"output/translation-progress.pdf");shutil.copyfile(out/"main.pdf",pdf);sha=s["m"]["sha256_file"](pdf);renders=B.assert_write_path(B.root/"workspace/pages/progress-output"/sha[:16]);renders.mkdir(parents=True,exist_ok=True);subprocess.run([shutil.which("pdftoppm"),"-r","100","-png",str(pdf),str(renders/"page")],check=True)
    dump("qa/latest-compilation.json",{"success":True,"pdf_sha256":sha,"pdf_pages":len(PdfReader(pdf).pages),"minimum_latex_rounds":2,"build_directory":str(out),"render_directory":str(renders),"warnings":warnings,"latex_qa":qa,"input_files":input_files,"published_progress_pdf_updated":True});guard();print(sha,"pages",len(PdfReader(pdf).pages))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("action",choices=["begin","extract","metadata","assemble","compile"]);p.add_argument("args",nargs="*");a=p.parse_args()
    if a.action=="extract":extract(*map(int,a.args))
    elif a.action=="metadata":metadata(a.args[0])
    else:{"begin":begin,"assemble":assemble,"compile":compile_batch}[a.action]()
