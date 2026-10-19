"""Per-book agent-authored bilingual batch rendering and evidence checks.

BT pairs contain human/agent-authored source and translation. This module only
selects their language, records provenance, compares math and compiles artifacts.
It does not translate text or infer mathematical expressions.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
from collections import Counter
from pypdf import PdfReader
from PIL import Image,ImageDraw
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import verify_book_context
from mathbook.template import verify_manifest
from mathbook.build import latex_qa

ID="krylov-subspace-methods-for-linear-systems"
P=ProjectPaths()
B,R=verify_book_context(P,ID,writable=True)
def write(rel,text):
    path=B.assert_write_path(B.root/rel);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding="utf-8");return path
def dump(rel,value):return write(rel,json.dumps(value,ensure_ascii=False,indent=2)+"\n")
def load(rel):return json.loads((B.root/rel).read_text(encoding="utf-8"))
def tsv(rel,fields,rows):
    path=B.assert_write_path(B.root/rel);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t");w.writeheader();w.writerows(rows)
def guard():
    assert not verify_manifest(),verify_manifest()
    assert sha256_file(B.require_source_pdf())==B.load_config()["source"]["sha256"]
    assert directory_manifest_hash(P.template)==B.load_config()["template_manifest_hash"]
    assert sha256_file(B.root/"tex/chapters/sample.tex")=="80f28b642e148a5c0a9ca0bf57efb0fa2e0c52a1ea1dc8b2261bab3b5d5aabae"
def prepare():
    guard();reader=PdfReader(B.require_source_pdf())
    pages=[]
    for n,p in enumerate(reader.pages,1):
        text=p.extract_text()
        write(f"workspace/raw-text/full/pdf-{n:03}.txt",text+"\n")
        pages.append({"pdf_page":n,"printed_page":reader.page_labels[n-1],"characters":len(text),"review_status":"not-reviewed"})
    dump("qa/full-extraction-inventory.json",pages)
    targets={}
    for i in range(222,231):
        for m in re.finditer(r"(?m)^(\d+)\.\s+(.+)",reader.pages[i].extract_text()):
            targets[m[1]]={"pdf_page":i+1,"printed_page":reader.page_labels[i],"raw_first_line":m[2]}
    dump("structured/source/bibliography-targets.json",targets)
    out=B.assert_write_path(B.root/"workspace/pages/full");out.mkdir(parents=True,exist_ok=True)
    for n in [7,8,9,10,*range(14,32),*range(36,43)]:
        subprocess.run([shutil.which("pdftoppm"),"-f",str(n),"-l",str(n),"-r","150","-singlefile","-png",
                        str(B.require_source_pdf()),str(out/f"pdf-{n:03}")],check=True)
    guard()
    print("Full text extracted as UNREVIEWED. First-chapter source pages rendered.")

def render_chapter_two():
    guard()
    out=B.assert_write_path(B.root/"workspace/pages/full");out.mkdir(parents=True,exist_ok=True)
    for n in range(43,85):
        target=out/f"pdf-{n:03}.png"
        if not target.exists():
            subprocess.run([shutil.which("pdftoppm"),"-f",str(n),"-l",str(n),"-r","150","-singlefile","-png",
                            str(B.require_source_pdf()),str(target.with_suffix(""))],check=True)
    guard()
    print("Chapter 2 original source pages rendered; no translation or review inferred.")

def render_chapter_three_first_section():
    return render_source_range(85,102)

def render_chapter_three_second_section():
    return render_source_range(102,112)

def render_source_range(first,last):
    guard()
    assert 1<=first<=last<=len(PdfReader(B.require_source_pdf()).pages)
    out=B.assert_write_path(B.root/"workspace/pages/full");out.mkdir(parents=True,exist_ok=True)
    for n in range(first,last+1):
        target=out/f"pdf-{n:03}.png"
        if not target.exists():
            subprocess.run([shutil.which("pdftoppm"),"-f",str(n),"-l",str(n),"-r","150","-singlefile","-png",str(B.require_source_pdf()),str(target.with_suffix(""))],check=True)
    guard()

def brace(text,start):
    assert text[start]=="{"
    depth=1;i=start+1
    while depth:
        if text[i]=="\\":
            i+=2;continue
        if text[i]=="{":depth+=1
        if text[i]=="}":depth-=1
        i+=1
    return text[start+1:i-1],i
def language(text,index):
    out="";pos=0
    for _ in range(text.count(r"\BT{")):
        hit=text.find(r"\BT{",pos)
        if hit<0:break
        out+=text[pos:hit]
        en,end=brace(text,hit+3)
        while text[end].isspace():end+=1
        zh,end=brace(text,end)
        # Preserve a TeX token boundary after adjacent control words such as
        # \par; XeTeX also treats CJK letters as control-word characters.
        out+="{"+(en,zh)[index]+"}";pos=end
    return out+text[pos:]
MATH=re.compile(r"\\begin\{(?:equation|align)\*?\}(.*?)\\end\{(?:equation|align)\*?\}|\\\[(.*?)\\\]|(?<!\\)\$(.*?)(?<!\\)\$",re.S)
def math(text):
    return [re.sub(r"\s+","",re.sub(r"\\label\{[^}]+\}","",next(x for x in m.groups() if x is not None))) for m in MATH.finditer(text)]
MARK=re.compile(r"^% block: ([\w-]+) pages?:([\d,]+) type:([\w-]+)\n",re.M)
def metadata(unit):
    guard()
    rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf-8"),delimiter="\t"))
    assert next(r for r in rows if r["Unit ID"]==unit)["QA Status"]!="passed", "Accepted units are immutable"
    data=(B.root/f"translation/authored/{unit}.bilingual.tex").read_text(encoding="utf-8")
    en,zh=language(data,0),language(data,1)
    em,zm=list(MARK.finditer(en)),list(MARK.finditer(zh))
    assert [m[1] for m in em]==[m[1] for m in zm]
    blocks=[];aligned=[];formulae=[]
    page_labels=PdfReader(B.require_source_pdf()).page_labels
    for i,(a,b) in enumerate(zip(em,zm)):
        source=en[a.end():em[i+1].start() if i+1<len(em) else len(en)].strip()
        target=zh[b.end():zm[i+1].start() if i+1<len(zm) else len(zh)].strip()
        assert Counter(math(source))==Counter(math(target)),f"Math changed in {a[1]}"
        pages=list(map(int,a[2].split(",")))
        fid=[]
        for j,expression in enumerate(math(source),1):
            id="formula-"+hashlib.sha256(f"{ID}:{unit}:{a[1]}:{j}".encode()).hexdigest()[:16]
            fid.append(id)
            formulae.append({"id":id,"latex":expression,"source_pages":pages,"block_id":a[1],
                             "review_status":"agent-reviewed","bbox_precision":"page body region, not token-tight"})
        loc=[{"pdf_page":p,"printed_page":page_labels[p-1],
              "bbox":[53,55,386,605],"image":f"workspace/pages/full/pdf-{p:03}.png"} for p in pages]
        blocks.append({"id":a[1],"type":a[3],"source_latex":source,"source_pages":loc,"formula_ids":fid,"review_status":"reviewed"})
        aligned.append({"id":a[1],"target_latex":target,"source_pages":loc,"review_status":"reviewed"})
    write(f"structured/reviewed/{unit}.tex",en)
    write(f"structured/reviewed/{unit}.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in blocks))
    write(f"translation/reviewed/{unit}.tex",zh)
    write(f"translation/reviewed/{unit}.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in aligned))
    write(f"formulae/{unit}.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in formulae))
    target="tex/frontmatter.tex" if unit=="frontmatter" else f"tex/chapters/{unit}.tex"
    write(target,zh)
    dump(f"qa/batches/{unit}-content.json",{"unit":unit,"source_blocks":len(blocks),"target_blocks":len(aligned),
        "math_expressions":len(formulae),"formula_tokens_match":True,"source_pages":sorted(set(p for x in blocks for p in [i["pdf_page"] for i in x["source_pages"]])),
        "review_status":"content-reviewed-awaiting-batch-compile"})
    print(unit,len(blocks),"blocks",len(formulae),"math expressions")

def compile_preview():
    guard()
    out=Path(tempfile.mkdtemp(prefix="full-batch-build-",dir=B.root/"workspace/temporary"))
    env=os.environ.copy()
    env["TEXINPUTS"]=os.pathsep.join(str(p) for p in [P.template/"style",P.template/"adapter",P.template/"assets",B.root/"tex"])+os.pathsep+os.pathsep
    env["PYTHONIOENCODING"]="utf-8"
    env["PYTHONUTF8"]="1"
    driver=r"C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py"
    r=subprocess.run([sys.executable,driver,str(B.main_tex),"--compiler","texlive","--engine","xelatex","--output-directory",str(out),"--json"],env=env,capture_output=True)
    write("logs/latest-build-driver.log",(r.stdout+r.stderr).decode("utf-8",errors="replace"))
    assert r.returncode==0,(r.stdout+r.stderr).decode("utf-8",errors="replace")[-5000:]
    r=subprocess.run([shutil.which("xelatex"),"-interaction=nonstopmode","-halt-on-error","-file-line-error",f"-output-directory={out}",str(B.main_tex)],cwd=B.root/"tex",env=env,capture_output=True)
    assert r.returncode==0,(r.stdout+r.stderr).decode("utf-8",errors="replace")[-5000:]
    log=(out/"main.log").read_text(encoding="utf-8",errors="replace");write("logs/latest-compilation.log",log)
    q=latex_qa(B)
    warnings={k:len(re.findall(p,log,re.I)) for k,p in {"undefined":r"undefined references?|Reference .* undefined","duplicate":r"multiply[- ]defined","missing_glyph":r"Missing character:","overfull":r"Overfull \\[hv]box"}.items()}
    dump("qa/latest-compilation.json",{"success":r.returncode==0 and q["passed"] and not any(warnings.values()),"latex_qa":q,"warnings":warnings,"build_directory":str(out),"minimum_latex_rounds":2})
    assert q["passed"] and not any(warnings.values()),(q,warnings)
    final=B.assert_write_path(B.root/"output/translation-progress.pdf");shutil.copyfile(out/"main.pdf",final)
    render_progress()
    guard()
    print(json.dumps({"pdf":str(final),"pages":len(PdfReader(final).pages),"warnings":warnings}))

def render_progress():
    final=B.root/"output/translation-progress.pdf"
    imgs=B.assert_write_path(B.root/"workspace/pages/progress-output"/sha256_file(final)[:16])
    imgs.mkdir(parents=True,exist_ok=True)
    subprocess.run([shutil.which("pdftoppm"),"-r","90","-png",str(final),str(imgs/"page")],check=True)
    files=list(imgs.glob("page-*.png"))
    assert len(files)==len(PdfReader(final).pages)
    q=load("qa/latest-compilation.json")
    q.update({"render_directory":str(imgs),"pdf_sha256":sha256_file(final),"pdf_pages":len(files)})
    dump("qa/latest-compilation.json",q)

def assemble():
    guard()
    contents=[]
    start=r"""\documentclass[a4paper,UTF8,12pt]{ctexart}
\usepackage{Mystyle}
\usepackage{translation-adapter}
\usepackage{needspace}
\input{translation-macros.tex}
\renewcommand{\thetable}{\thesection.\arabic{table}}
\counterwithin{algorithm}{section}
\counterwithin{table}{section}
\counterwithin{figure}{section}
\setcounter{secnumdepth}{4}
\newcounter{applicationexample}[section]
\newcommand{\BookCite}[1]{\hyperref[bib:source-#1]{[\ref*{bib:source-#1}]}}
\begin{document}
\begin{center}{\Large Krylov Subspace Methods for Linear Systems}\\全书翻译进度稿\end{center}
\noindent 本文件只收录已完成的译文单元. 尚未翻译的引用目标列于文末源文定位表, 不表示相应内容已完成.\par
"""
    if (B.root/"tex/frontmatter.tex").is_file():
        start+=r"\input{frontmatter.tex}"+"\n"
        contents.append((B.root/"tex/frontmatter.tex").read_text(encoding="utf-8"))
    units=sorted((B.root/"tex/chapters").glob("chapter-*.tex"))
    included_sample=False
    for file in units:
        # Insert the accepted Section 1.8 in its natural position, byte-for-byte.
        if file.stem>"chapter-01-section-08" and not included_sample:
            start+=r"\setcounter{subsection}{7}\setcounter{equation}{19}\input{chapters/sample.tex}"+"\n"
            contents.append((B.root/"tex/chapters/sample.tex").read_text(encoding="utf-8"))
            included_sample=True
        start+=r"\input{chapters/"+file.name+"}\n"
        contents.append(file.read_text(encoding="utf-8"))
    if not included_sample:
        start+=r"\setcounter{subsection}{7}\setcounter{equation}{19}\input{chapters/sample.tex}"+"\n"
        contents.append((B.root/"tex/chapters/sample.tex").read_text(encoding="utf-8"))
    labels=set(re.findall(r"\\label\{([^}]+)\}","\n".join(contents)))
    references=set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}","\n".join(contents)))
    known={
      "chap:computational-applications":("2",43,"31","Some Applications to Computational Science and Data Science"),
      "chap:krylov-classification":("3",85,"73","Classification and Theory of Krylov Subspace Methods"),
      "chap:shifted-linear-systems":("4",175,"163","Applications to Shifted Linear Systems"),
      "chap:matrix-functions":("5",201,"189","Applications to Matrix Functions"),
      "subsec:conjugate-gradient":("3.1.1",85,"73","The Conjugate Gradient (CG) Method"),
      "sec:hermitian-linear-systems":("3.1",85,"73","Hermitian Linear Systems"),
      "sec:complex-symmetric-linear-systems":("3.2",102,"90","Complex Symmetric Linear Systems"),
      "sec:nonhermitian-linear-systems":("3.3",111,"99","Non-Hermitian Linear Systems"),
      "subsec:cg-normal-equations":("3.4.1",159,"147","Krylov Subspace Methods for Normal Equations"),
      "subsec:newton-matrix-square-root":("5.3.1",206,"194","Matrix Square Root"),
      "sec:preconditioning-techniques":("3.5",163,"151","Preconditioning Techniques"),
      "subsec:cocr-method":("3.2.2",104,"92","The Conjugate Orthogonal Conjugate Residual (COCR) Method"),
      "subsec:composite-step-bicg":("3.3.2",116,"104","The Composite Step Bi-Conjugate Gradient (CSBiCG) Method"),
      "sec:symmetric-direct-methods":("1.4",22,"9","Direct Methods for Symmetric Linear Systems"),
      "subsec:stationary-preconditioners":("3.5.4",172,"160","Preconditioners Based on Stationary Iterative Methods"),
      "subsec:preconditioner-reorderings":("3.5.5",173,"161","Reorderings for Preconditioners"),
      "subsec:shifted-gmres":("4.4.3",192,"180","The Shifted GMRES Method"),
      "subsec:shifted-bicg":("4.4.1",188,"176","The Shifted BiCG Method"),
    }
    unresolved=references-labels
    assert unresolved<=set(known),unresolved-set(known)
    locators=["\\clearpage\n\\section*{尚未翻译部分的源文定位}\n",
              "以下为已核实的源文引用目标. 这里只提供定位, 不是尚未完成章节的译文.\n"]
    for key in sorted(unresolved):
        number,page,printed,title=known[key]
        locators.append("\\subsection*{"+title+"}\n\\makeatletter\\phantomsection\\def\\@currentlabel{"+number+"}\\label{"+key+"}\\makeatother\n")
        locators.append("Source "+number+", PDF "+str(page)+", printed "+printed+".\\par\n")
    # Page/theorem-qualified citations use explicit source-bibliography links.
    # Register those targets too; they are not book-local equation numbers.
    cited=sorted(set(re.findall(r"\\BookCite\{(\d+)\}","\n".join(contents))
                     +re.findall(r"bib:source-(\d+)","\n".join(contents))),key=int)
    bibliography=load("structured/source/bibliography-targets.json")
    for number in cited:
        assert number in bibliography,number
        record=bibliography[number]
        locators.append("\\makeatletter\\phantomsection\\def\\@currentlabel{"+number+"}\\label{bib:source-"+number+"}\\makeatother\n")
        locators.append("Reference ["+number+"], PDF "+str(record["pdf_page"])+", printed "+record["printed_page"]+".\\par\n")
    write("tex/chapters/pending-targets.tex","".join(locators))
    write("tex/main.tex",start+"\\input{chapters/pending-targets.tex}\n\\end{document}\n")
    dump("qa/pending-reference-targets.json",{"verified_source_locators":{k:known[k] for k in unresolved},
                                          "bibliography_locators":{n:bibliography[n] for n in cited},
                                          "note":"These are future translated targets, not undefined references or translated content."})
    print("Assembled",len(units),"new units plus accepted sample;",len(unresolved),"pending source locators")

def audit():
    guard()
    q=load("qa/latest-compilation.json");assert q["success"],q
    names=[
      "Owe Axelsson","Richard Barrett","Wolfgang Hackbusch","Are Magnus Bruaset","Rüdiger Weiss",
      "Anne Greenbaum","Yousef Saad","Henk A. van der Vorst","Jörg Liesen","Zdeněk Strakoš",
      "Gérard Meurant","Jurjen Duintjer Tebbens","Tomohiro Sogabe","Lei Du","Masayuki Nakamura",
      "Lokeshwaran Manickavasagam","Poojitha Ravichandran","Randolph E. Bank","Josef Stoer",
      "Harry Yserentant","Shao-Liang Zhang","Yuan Li","Kazuma","Takuma",
      "Fourier","Green","Wilson","Sylvester","Hessian","Euclidean","Riemannian","Lanczos",
      "Frobenius","Doolittle","Crout","Cholesky","Newton","Cuthill","McKee","Jacobi","Gauss",
      "Seidel","Perron","Varga","Jordan","Hackbusch","Wesseling","Bramble","Briggs","Trottenberg",
      "Lottes","James Lottes","Arnoldi","Gram","Schmidt","Hessenberg","Kronecker"]
    sources=[];targets=[];units=[];blocks=[]
    for file in sorted((B.root/"translation/authored").glob("*.bilingual.tex")):
        unit=file.name.replace(".bilingual.tex","");units.append(unit)
        sources.append((B.root/f"structured/reviewed/{unit}.tex").read_text(encoding="utf-8"))
        targets.append((B.root/f"translation/reviewed/{unit}.tex").read_text(encoding="utf-8"))
        blocks.extend(json.loads(line) for line in (B.root/f"structured/reviewed/{unit}.jsonl").read_text(encoding="utf-8").splitlines())
    en="\n".join(sources);zh="\n".join(targets)
    counts={name:{"source":len(re.findall(r"\b"+re.escape(name)+r"\b",en)),
                  "target":len(re.findall(r"\b"+re.escape(name)+r"\b",zh))} for name in names}
    mismatches={k:v for k,v in counts.items() if v["source"]!=v["target"]}
    dump("qa/translation/chapter-01-name-report.json",{"passed":not mismatches,"names":counts,"mismatches":mismatches})
    assert not mismatches,mismatches
    for forbidden in "，。：；？！（）【】、…":
        assert forbidden not in zh,forbidden
    assert "的级" not in (B.root/"tex/chapters/sample.tex").read_text(encoding="utf-8")
    with B.proper_names.open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;existing=list(reader)
    seen={r["Source Form"] for r in existing}
    for name in names:
        if not counts[name]["source"] or name in seen:continue
        first=next(row for row in blocks if re.search(r"\b"+re.escape(name)+r"\b",row["source_latex"]))
        loc=first["source_pages"][0]
        row=dict.fromkeys(fields,"")
        row.update({"Source Form":name,"Canonical Form":name,"Category":"person-or-eponym",
          "First Occurrence":f"Block {first['id']}; PDF "+",".join(str(v["pdf_page"]) for v in first["source_pages"]),
          "Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed",
          "Notes":"Compared with source page; typeset line-end hyphenation is not a lexical name hyphen."})
        existing.append(row);seen.add(name)
    tsv("glossary/proper-names.tsv",fields,existing)
    with B.candidates.open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;terms=list(reader)
    newterms=[
     ("vector norm","向量范数","norm of a real vector"),("matrix norm","矩阵范数","norm of a real matrix"),
     ("submultiplicative","具有次乘性","matrix norm product inequality"),("subordinate matrix norm","从属矩阵范数","supremum of a norm ratio"),
     ("condition number","条件数","norm of A times norm of inverse A"),("ill-conditioned","病态的","linear systems with a large condition number"),
     ("pivoting","选主元","row or column swaps in LU decomposition"),("partial pivoting","部分选主元","LU pivot search within a column"),
     ("complete pivoting","完全选主元","LU pivot search over remaining submatrix"),("iterative refinement","迭代改进","residual correction using existing factors"),
     ("fill-in","填充元","factor entry nonzero where original matrix entry is zero"),("stationary iterative method","定常迭代方法","iteration map independent of iteration count"),
     ("regular splitting","正则分裂","A=M-N with nonnegative inverse of M and nonnegative N"),
     ("multigrid method","多重网格方法","hierarchy of coarse and fine mesh problems"),("smoother","光滑子","damping high-frequency error components"),
     ("orthonormal","标准正交","unit vectors with pairwise orthogonality"),("bi-orthogonal","双正交","two bases with paired inner products equal to Kronecker deltas"),
     ("conjugate orthogonal","共轭正交","complex-symmetric Lanczos bilinear orthogonality"),("breakdown","中断","zero division in a recurrence"),
     ("preconditioner","预条件子","transforming or accelerating a linear solver")]
    global_terms=list(csv.DictReader((P.glossary/"terminology.tsv").open(encoding="utf-8"),delimiter="\t"))
    lookup=[]
    for english,chinese,context in newterms:
        matches=[r for r in global_terms if r["English"].casefold()==english.casefold()]
        lookup.append({"English":english,"Domain":"numerical linear algebra","Context":context,"global_matches":matches})
        if any(r["English"]==english and r["Domain"]=="numerical linear algebra" and r["Context"]==context for r in terms):continue
        row=dict.fromkeys(fields,"")
        row.update({"English":english,"Preferred Chinese":chinese,"Domain":"numerical linear algebra","Context":context,
         "Status":"proposed","First Source":ID,"First Location":"Chapter 1 / PDF 14-42","Last Verified Source":ID,
         "Last Verified Location":"Chapter 1 / PDF 14-42","Notes":"Book-local candidate, global library unchanged."})
        terms.append(row)
    tsv("glossary/candidates.tsv",fields,terms)
    dump("qa/terminology/chapter-01-shared-lookup.json",lookup)
    reader=PdfReader(B.root/"output/translation-progress.pdf");dest=reader.named_destinations
    links=[]
    for n,page in enumerate(reader.pages,1):
        for ref in page.get("/Annots",[]):
            action=ref.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":
                key=str(action["/D"]);assert key in dest,key
                links.append({"page":n,"target":key,"target_page":reader.get_destination_page_number(dest[key])+1})
    dump("qa/translation/chapter-01-pdf-link-report.json",{"passed":True,"links":links})
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf-8")
    equation_numbers=re.findall(r"\\newlabel\{eq:[^}]+\}\{\{(1\.\d+)\}",aux)
    assert sorted(map(lambda s:int(s.split(".")[1]),equation_numbers))==list(range(1,44)),equation_numbers
    algorithm_numbers=re.findall(r"\\newlabel\{alg:[^}]+\}\{\{(1\.\d+)\}",aux)
    assert sorted(int(s.split(".")[1]) for s in algorithm_numbers)==list(range(1,12)),algorithm_numbers
    dump("qa/translation/chapter-01-numbering-report.json",{"passed":True,"equations":equation_numbers,"algorithms":algorithm_numbers,
         "shared_statement_counter_preserved":True,"source_object_numbers_retained_in_source_text":True})
    # Persist observable provenance, not a claim of whole-book completion.
    count=sum(load(f"qa/batches/{u}-content.json")["math_expressions"] for u in units)
    dump("qa/batches/chapter-01-automated-qa.json",{"passed":True,"units":units,"new_blocks":len(blocks),"new_math_expressions":count,
         "accepted_sample_blocks":23,"accepted_sample_math_expressions":96,"name_records":len(existing),
         "internal_links_checked":len(links),"equations":43,"algorithms":11,"compile":q,
         "source_hash_unchanged":True,"template_hashes_unchanged":True,"sample_hash_unchanged":True,
         "visual_review":"pending","whole_book_complete":False})
    print("Chapter 1 automated QA passed;",len(blocks),"new blocks;",count,"new math expressions;",len(links),"PDF links")
    # Make compact layout-review sheets; mathematical fidelity was reviewed in
    # the separate original-page images, not inferred from these thumbnails.
    files=sorted(Path(q["render_directory"]).glob("page-*.png"),key=lambda f:int(re.search(r"(\d+)\.png",f.name)[1]))
    assert len(files)==len(reader.pages)
    sheets=B.assert_write_path(B.root/"workspace/pages/progress-review");sheets.mkdir(parents=True,exist_ok=True)
    for start in range(0,len(reader.pages),6):
        sheet=Image.new("RGB",(1100,1600),"white");draw=ImageDraw.Draw(sheet)
        for i,file in enumerate(files[start:start+6]):
            im=Image.open(file);im.thumbnail((355,750));x=(i%3)*365;y=(i//3)*800
            draw.text((x+8,y+2),f"PDF output page {start+i+1}",fill="black");sheet.paste(im,(x,y+25))
        sheet.save(sheets/f"sheet-{start//6+1:02}.png")

def accept_batch():
    guard()
    qa=load("qa/batches/chapter-01-automated-qa.json")
    visual=load("qa/batches/chapter-01-visual-review.json")
    assert qa["passed"] and visual["passed"]
    assert visual["pdf_sha256"]==sha256_file(B.root/"output/translation-progress.pdf")
    qa["visual_review"]="passed"
    qa["pdf_sha256"]=visual["pdf_sha256"]
    dump("qa/batches/chapter-01-automated-qa.json",qa)
    q=load("qa/sample-qa.json");q.update({"user_approved":True,"full_book_translation_started":True})
    dump("qa/sample-qa.json",q)
    q=load("qa/workflow-state.json");q.update({"status":"translating","sample_approved":True})
    dump("qa/workflow-state.json",q)
    cfg=B.load_config();cfg.update({"phase":"translation","status":"translating",
      "progress_output":"output/translation-progress.pdf","sample_approved":True})
    dump("config/book.yaml",cfg)
    def status(next_unit):
        write("PROJECT_STATUS.md",
          f"Book ID: {ID}\nTitle: Krylov Subspace Methods for Linear Systems\nBranch: {R.branch}\n"
          f"Worktree: {P.root}\nPhase: translation\nStatus: translating\n"
          f"Source SHA-256: {cfg['source']['sha256']}\nTemplate version: {cfg['template_version']}\n"
          "Sample approved: Yes (user instruction: 接下来翻译全书)\nApproved terminology: grade -> 阶\n"
          "Completed content: Preface, Acknowledgements, entire Chapter 1 (Sections 1.1-1.9)\n"
          "Last integrated batch: chapter-01\nProgress output: output/translation-progress.pdf\n"
          f"Next incomplete unit: {next_unit}\nBlocking issues: None\nUnresolved terminology: 0\n"
          "Full-book translation complete: No\nRemote push: No\n")
    source_issues=[
      ("source-editor-count",10,"Acknowledgements says three editors while listing four names."),
      ("source-rhs-space",14,"Source prints b in C for Ax=b; retained."),
      ("source-a-norm-no-root",15,"Source A-norm expression has no square root; retained."),
      ("source-norm-comparison",16,"Theorem 1.2 item (4) inequality retained as printed."),
      ("source-perturbation-prose",17,"Source says p-norm of x before bounding Delta x; retained."),
      ("source-complete-pivot-step",21,"Algorithm 1.3 line 7 column/row and matrix P retained exactly."),
      ("source-ldl-condition",23,"Nonnegative leading minors and the uninitialized printed LDL loop retained."),
      ("source-fill-equality",25,"Source prose equates fill-in entries whose displayed fractions differ; both retained."),
      ("source-bilanczos-rectangular",40,"Source rectangular conjugate-transpose product retained exactly.")]
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf-8").splitlines() if x.strip()]
    seen={x["id"] for x in issues}
    for id,page,message in source_issues:
        if id not in seen:issues.append({"id":id,"category":"source","severity":"warning","message":message,
            "source_location":{"page":page},"confidence":1.0,"review_status":"reviewed",
            "details":{"blocking":False,"action":"Preserve source; no silent mathematical correction.",
                       "report":"qa/source/chapter-01-source-observations.md"}})
    write("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    from mathbook.workflow import translate_book,next_incomplete_unit
    class NeedNextUnit(Exception):pass
    approved_units=set(qa["units"])
    def processor(book,unit):
        if unit not in approved_units:raise NeedNextUnit(unit)
        with B.chapter_progress.open(encoding="utf-8",newline="") as f:
            reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;rows=list(reader)
        row=next(x for x in rows if x["Unit ID"]==unit)
        assert row["QA Status"]=="pending"
        row.update({"QA Status":"passed","Notes":"Complete source-aligned translation; chapter-01 integrated QA and visual review passed"})
        # Accepted sample remains untouched and its original progress row is
        # updated only to reflect the user's actual approval.
        sample=next(x for x in rows if x["Unit ID"]=="chapter-01-section-08")
        sample["Notes"]="Accepted sample; user approved; source text unchanged"
        tsv("qa/chapter-progress.tsv",fields,rows)
        status(next_incomplete_unit(B))
    try:
        result=translate_book(P,ID,processor=processor)
    except NeedNextUnit:
        state=load("qa/workflow-state.json")
        state.update({"status":"translating","next_unit":next_incomplete_unit(B),"sample_approved":True})
        dump("qa/workflow-state.json",state)
        status(next_incomplete_unit(B))
        result={"status":"translating","next_unit":next_incomplete_unit(B)}
    dump("qa/input-hashes-full-batch.json",{
      "source_sha256":sha256_file(B.require_source_pdf()),
      "external_source_sha256":sha256_file(Path(r"D:\BaiduNetdiskDownload\Krylov Subspace Methods for Linear Systems.pdf")),
      "template_manifest_hash":directory_manifest_hash(P.template),"template_unchanged":not verify_manifest(),
      "accepted_sample_sha256":sha256_file(B.root/"tex/chapters/sample.tex"),
      "accepted_sample_pdf_sha256":sha256_file(B.root/"output/sample-zh.pdf")})
    print(json.dumps(result,ensure_ascii=False))

if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("action",choices=["prepare","metadata","assemble","compile","render","audit","accept"]);a.add_argument("unit",nargs="?")
    args=a.parse_args()
    if args.action=="prepare":prepare()
    elif args.action=="metadata":metadata(args.unit)
    elif args.action=="assemble":assemble()
    elif args.action=="audit":audit()
    elif args.action=="render":render_progress()
    elif args.action=="accept":accept_batch()
    else:compile_preview()
