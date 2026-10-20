"""Explicit agent sample processor for this book; no machine translation.

All content comes from the authored bilingual file and inspected original pages.
Shared system files and other book data are never inputs to this processor.
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,json,os,re,runpy,shutil,subprocess,sys,tempfile
from pathlib import Path
from pypdf import PdfReader
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"workspace/temporary/python-deps"))
import jsonschema
from mathbook.qa import find_chinese_prose_punctuation
from mathbook.build import latex_qa
from mathbook.terminology import TERM_COLUMNS
from mathbook.workflow import PROPER_NAME_COLUMNS,NOTATION_COLUMNS
m=runpy.run_path(str(Path(__file__).with_name("sample_workflow.py")));P,B,ID=m["P"],m["B"],m["ID"]
R=m["R"]
write,dump,load,guard=m["write"],m["dump"],m["load"],m["guard"]
MARK=re.compile(r"^% block: ([\w-]+) pages?:([\d,]+) type:([\w-]+)\n",re.M)
MATH=re.compile(r"\\begin\{equation\}(.*?)\\end\{equation\}|\\\[(.*?)\\\]|(?<!\\)\$(.*?)(?<!\\)\$",re.S)
def brace(text,pos):
    assert text[pos]=="{";start=pos+1;level=1;pos=start
    while level:
        if text[pos]=="\\":pos+=2;continue
        if text[pos]=="{":level+=1
        if text[pos]=="}":level-=1
        pos+=1
    return text[start:pos-1],pos
def language(text,index):
    result="";pos=0
    while True:
        i=text.find(r"\BT{",pos)
        if i<0:return result+text[pos:]
        result+=text[pos:i];en,end=brace(text,i+3)
        while text[end].isspace():end+=1
        zh,end=brace(text,end);result+="{"+(en,zh)[index]+"}";pos=end
def formula_normalize(text):
    # Translate prose annotations, never the mathematical expressions inside them.
    result="";pos=0
    while True:
        i=text.find(r"\text{",pos)
        if i<0:result+=text[pos:];break
        result+=text[pos:i];body,end=brace(text,i+5)
        result+=" ".join(re.findall(r"\$(.*?)\$",body,re.S));pos=end
    return re.sub(r"\s+","",re.sub(r"\\label\{[^}]+\}","",result))
def maths(text):return [formula_normalize(next(x for x in h.groups() if x is not None)) for h in MATH.finditer(text)]
def tsv(rel,fields,rows):
    path=B.assert_write_path(B.root/rel);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t");w.writeheader();w.writerows(rows)
def prepare():
    guard()
    state=load("qa/workflow-state.json")
    assert state["status"] in ("registered","sample-processing","awaiting-sample-approval") and not B.load_config().get("sample_approved"),"Accepted sample is immutable; do not regenerate after user approval"
    authored=(B.root/"translation/draft/sample.bilingual.tex").read_text(encoding="utf8");en,zh=language(authored,0),language(authored,1)
    source=[];target=[];formulae=[];provenance=[];alignment=[]
    em,zm=list(MARK.finditer(en)),list(MARK.finditer(zh));assert len(em)==len(zm)
    schema=json.loads((P.root/"schemas/text-block.schema.json").read_text(encoding="utf8"));fschema=json.loads((P.root/"schemas/formula.schema.json").read_text(encoding="utf8"))
    for j,(a,b) in enumerate(zip(em,zm)):
        assert a.groups()==b.groups();s=en[a.end():em[j+1].start() if j+1<len(em) else len(en)].strip();t=zh[b.end():zm[j+1].start() if j+1<len(zm) else len(zh)].strip()
        sm,tm=maths(s),maths(t);assert collections.Counter(sm)==collections.Counter(tm),(a[1],sm,tm)
        pages=list(map(int,a[2].split(",")));bbox=[64,273,430,650] if pages[0]==25 else [55,54,430,671];ids=[]
        for k,(raw,norm) in enumerate(zip(MATH.finditer(s),sm),1):
            latex=next(x for x in raw.groups() if x is not None);key="formula-"+hashlib.sha256(f"{ID}:{a[1]}:{k}".encode()).hexdigest()[:16];ids.append(key)
            label=re.search(r"\\label\{([^}]+)\}",latex)
            source_numbers={"eq:simplicial-cochain-complex":"2.1","eq:differential-forms-de-rham-complex":"2.2","eq:vector-calculus-de-rham-complex":"2.3","eq:de-rham-commuting-map":"2.4"}
            record={"id":key,"source_latex":latex,"tokens":re.findall(r"\\[A-Za-z]+|\\.|[^\s]",norm),"source_location":{"page":pages[0],"bbox":bbox},"confidence":0.99,"review_status":"reviewed","label":label[1] if label else None,"number":source_numbers.get(label[1]) if label else None}
            jsonschema.validate(record,fschema);formulae.append(record)
        row={"id":a[1],"block_type":a[3],"source_text":s,"source_location":{"page":pages[0],"bbox":bbox},"confidence":0.99,"review_status":"reviewed","formula_ids":ids};jsonschema.validate(row,schema);source.append(row)
        translated=dict(row);translated["translated_text"]=t;jsonschema.validate(translated,schema);target.append(translated)
        provenance.append({"id":a[1],"pdf_pages":pages,"printed_pages":[str(p-10) for p in pages],"image_paths":[f"workspace/pages/source/pdf-{p:03}.png" for p in pages],"bbox":bbox,"bbox_precision":"selected page-body region, not token-tight","extraction":"native text/layout plus agent transcription from original page image","formula_ids":ids,"review_status":"reviewed","confidence":0.99})
        alignment.append({"block":a[1],"math_expressions":len(sm),"source_target_math_tokens_equal":True})
    for rel,value in [("structured/reviewed/sample.jsonl",source),("translation/reviewed/sample.jsonl",target),("formulae/sample.jsonl",formulae)]:write(rel,"".join(json.dumps(x,ensure_ascii=False)+"\n" for x in value))
    write("structured/reviewed/sample.tex",en);write("translation/reviewed/sample.tex",zh);write("tex/chapters/sample.tex",zh)
    dump("structured/source/sample-provenance.json",provenance);dump("qa/formula/sample-alignment.json",{"passed":True,"blocks":alignment,"formula_records":len(formulae),"annotation_policy":"Only prose inside text annotations is translated; mathematical annotation tokens retained","original_image_review_pages":[25,26,27,28]})
    terms=[("chain map","链映射"),("chain complex","链复形"),("cochain complex","上链复形"),("graded linear map","分次线性映射"),("differential","微分"),("boundary","边界链"),("cycle","闭链"),("homology","同调"),("homology class","同调类"),("subcomplex","子复形"),("chain projection","链投影"),("cohomology","上同调"),("cocycle","闭上链"),("coboundary","上边界链"),("simplicial cochain complex","单纯上链复形"),("oriented incidence matrix","定向关联矩阵"),("Betti number","Betti 数"),("differential form","微分形式"),("exterior derivative","外微分"),("de Rham map","de Rham 映射"),("trace","迹"),("singular homology","奇异同调"),("simplicial homology","单纯同调"),("functorial","具有函子性")]
    global_rows=list(csv.DictReader((P.glossary/"terminology.tsv").open(encoding="utf8"),delimiter="\t"));lookups=[];candidates=[]
    for eng,chinese in terms:
        matches=[x for x in global_rows if x["English"].casefold()==eng.casefold()]
        context="Sections 2.4-2.6: chain/cochain complexes and the de Rham map";domain="homological algebra" if eng not in ("trace","differential form","exterior derivative") else "differential geometry"
        approved=[x for x in matches if x["Status"]=="approved" and x["Domain"]==domain]
        assert not approved,"An approved contextual term needs explicit reuse review before adding a candidate"
        lookups.append({"English":eng,"Domain":domain,"Context":context,"global_matches":matches,"selection":chinese,"status":"proposed; sample terminology awaiting user review"})
        row=dict.fromkeys(TERM_COLUMNS,"");row.update({"English":eng,"Preferred Chinese":chinese,"Domain":domain,"Context":context,"Status":"proposed","First Source":"Finite Element Exterior Calculus","First Location":"PDF 25-28 / printed 15-18","Last Verified Source":"original page images","Last Verified Location":"Sections 2.4-2.6","Notes":"Book-local candidate; no global approval or promotion"});candidates.append(row)
    tsv("glossary/candidates.tsv",TERM_COLUMNS,candidates);dump("qa/terminology/sample-lookup.json",lookups)
    names=[]
    for name in ("de Rham","De Rham","Élie Cartan","Betti","Stokes"):
        row=dict.fromkeys(PROPER_NAME_COLUMNS,"");row.update({"Source Form":name,"Canonical Form":name,"Category":"person","First Occurrence":"sample / PDF 25-28","Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed","Notes":"Case and accents preserved exactly as printed, including sentence-initial De Rham"});names.append(row)
    tsv("glossary/proper-names.tsv",PROPER_NAME_COLUMNS,names)
    notation=[]
    for symbol,meaning in [(r"\partial","chain/cochain differential, according to index position"),(r"\xi,\zeta","other chain differentials"),(r"\mathcal H_k,\mathcal H^k","homology and cohomology spaces"),(r"\mathcal Z^k,\mathcal B^k","cocycles and coboundaries"),(r"C^k:=C'_k","dual simplicial cochains"),(r"F^k","de Rham map components"),(r"\Lambda^k(\Omega)","smooth differential k-forms")]:
        row=dict.fromkeys(NOTATION_COLUMNS,"");row.update({"Source Notation":symbol,"Canonical Notation":symbol,"Meaning":meaning,"Scope":"Sections 2.4-2.6","First Occurrence":"PDF 25-28 / printed 15-18","Preserve Exactly":"true","Review Status":"reviewed","Notes":"No notation normalization performed"});notation.append(row)
    tsv("glossary/notation.tsv",NOTATION_COLUMNS,notation)
    write("tex/main.tex",r"""\documentclass[a4paper,UTF8,12pt]{ctexart}
\usepackage{Mystyle}
\usepackage{translation-adapter}
\usepackage{tikz-cd}
\input{translation-macros.tex}
\setcounter{secnumdepth}{3}
\begin{document}
\begin{center}{\Large Finite Element Exterior Calculus}\\代表性样本: Section 2.4--2.6 正文\end{center}
\noindent 原文定位: PDF 25--28, 印刷页 15--18. 本样本不包含之前的 Section 2.3 或之后独立的 Box 2.1. 文末仅提供已核实的样本外引用定位, 不表示那些章节已经翻译.\par
\setcounter{section}{1}
\section{同调代数的基本概念}\label{chap:homological-algebra}
\setcounter{subsection}{3}
\input{chapters/sample.tex}
\clearpage
\section*{样本外引用定位}
\noindent 以下只登记原书引用目标, 并非这些部分的译文.\par
\subsection*{Chapter 6: Basic notions of exterior calculus}
\makeatletter\phantomsection\def\@currentlabel{6}\label{chap:exterior-calculus}\makeatother
\noindent Source PDF 73 / printed page 63.\par
\subsection*{Section 7.6: The Whitney forms $\mathcal P^-_1\Lambda^k$ and de Rham's theorem}
\makeatletter\phantomsection\def\@currentlabel{7.6}\label{sec:whitney-forms-de-rham}\makeatother
\noindent Source PDF 100 / printed page 90.\par
\subsection*{Reference [27]}
\makeatletter\phantomsection\def\@currentlabel{27}\label{bib:cartan-differential-expressions}\makeatother
\noindent Élie Cartan, Sur certaines expressions différentielles et le problème de Pfaff, Ann. Sci. École Norm. Sup. (3) 16 (1899), 239--332. MR 1508969. Source PDF 124 / printed page 114.\par
\end{document}
""")
    dump("qa/sample-selection.json",{"book_id":ID,"source_pdf_pages":[25,26,27,28],"printed_pages":[15,16,17,18],"scope":"Sections 2.4-2.6 main text, ending before separate Box 2.1","exclusions":"Preceding Section 2.3 material on PDF 25 and separate chapter summary Box 2.1 on PDF 29 are outside the selected sample","coverage":["prose","implicit definitions","two commuting diagrams","numbered/unnumbered mathematics","Proposition 2.1 and Proof","Theorem 2.2","Remark 2.3","cross-page paragraph","chapter and section references","bibliographic reference"],"blocks":len(source),"math_expressions":len(formulae),"OCR_used":False,"full_book_translation_started":False})
    guard();print(json.dumps({"blocks":len(source),"formulas":len(formulae),"candidates":len(candidates)},ensure_ascii=False))
def compile_sample():
    guard();out=Path(tempfile.mkdtemp(prefix="sample-build-",dir=B.assert_write_path(B.root/"workspace/temporary")))
    env=os.environ.copy();env["TEXINPUTS"]=os.pathsep.join(str(p) for p in [P.template/"style",P.template/"adapter",P.template/"assets",B.root/"tex"])+os.pathsep+os.pathsep
    driver=r"C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py"
    r=subprocess.run([sys.executable,driver,str(B.main_tex),"--compiler","texlive","--engine","xelatex","--output-directory",str(out),"--json"],env=env,capture_output=True)
    write("logs/compile-driver.log",(r.stdout+r.stderr).decode("utf8",errors="replace"));assert r.returncode==0,(r.stdout+r.stderr).decode("utf8",errors="replace")[-5000:]
    r=subprocess.run([shutil.which("xelatex"),"-interaction=nonstopmode","-halt-on-error","-file-line-error",f"-output-directory={out}",str(B.main_tex)],cwd=B.root/"tex",env=env,capture_output=True)
    write("logs/latest-compilation.log",(out/"main.log").read_text(encoding="utf8",errors="replace"));assert r.returncode==0,r.stdout.decode("utf8",errors="replace")[-3000:]
    log=(out/"main.log").read_text(encoding="utf8",errors="replace");qa=latex_qa(B)
    warnings={k:len(re.findall(pattern,log,re.I)) for k,pattern in {"undefined":r"undefined references?|Reference .* undefined","duplicate":r"multiply[- ]defined","missing_glyph":r"Missing character:","overfull":r"Overfull \\[hv]box"}.items()}
    assert qa["passed"] and not any(warnings.values()),(qa,warnings)
    destination=B.assert_write_path(B.root/"output/sample-zh.pdf");shutil.copyfile(out/"main.pdf",destination)
    renders=B.assert_write_path(B.root/"workspace/pages/sample-output"/m["sha256_file"](destination)[:16]);renders.mkdir(parents=True,exist_ok=True)
    subprocess.run([shutil.which("pdftoppm"),"-r","110","-png",str(destination),str(renders/"page")],check=True)
    report={"success":True,"minimum_latex_rounds":2,"build_directory":str(out),"pdf":"output/sample-zh.pdf","pdf_sha256":m["sha256_file"](destination),"pdf_pages":len(PdfReader(destination).pages),"render_directory":str(renders),"warnings":warnings,"latex_qa":qa}
    dump("qa/latest-compilation.json",report);guard();print(json.dumps(report,ensure_ascii=False))
def audit():
    guard();q=load("qa/latest-compilation.json");assert q["success"]
    assert m["sha256_file"](B.root/"output/sample-zh.pdf")==q["pdf_sha256"]
    en=(B.root/"structured/reviewed/sample.tex").read_text(encoding="utf8");zh=(B.root/"translation/reviewed/sample.tex").read_text(encoding="utf8")
    assert collections.Counter(maths(en))==collections.Counter(maths(zh));assert not find_chinese_prose_punctuation(zh)
    names=list(csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t"));checks=[]
    for row in names:
        name=row["Source Form"];pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";a=len(re.findall(pat,en));b=len(re.findall(pat,zh));checks.append({"name":name,"source":a,"target":b});assert a==b,checks[-1]
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");labels={}
    for hit in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=brace(aux,hit.end()-1);v=[];pos=0
        while pos<len(body):x,pos=brace(body,pos);v.append(x)
        labels[hit[1]]=v
    expected={"sec:chain-maps":"2.4","sec:cochain-complexes":"2.5","sec:de-rham-complex":"2.6","prop:chain-projection-homology-surjection":"2.1","thm:de-rham-isomorphism":"2.2","rem:singular-simplicial-de-rham":"2.3","eq:simplicial-cochain-complex":"2.1","eq:differential-forms-de-rham-complex":"2.2","eq:vector-calculus-de-rham-complex":"2.3","eq:de-rham-commuting-map":"2.4","chap:exterior-calculus":"6","sec:whitney-forms-de-rham":"7.6","bib:cartan-differential-expressions":"27"}
    reader=PdfReader(B.root/"output/sample-zh.pdf");dest=reader.named_destinations;objects=[]
    for key,num in expected.items():
        v=labels[key];assert v[0]==num,(key,v,num);actual=reader.get_destination_page_number(dest[v[3]])+1;assert actual==int(v[1]),(key,v,actual)
        objects.append({"label":key,"number":num,"output_page":actual,"destination":v[3]})
    refs=[];provenance={x["id"]:x for x in load("structured/source/sample-provenance.json")}
    for row in [json.loads(s) for s in (B.root/"translation/reviewed/sample.jsonl").read_text(encoding="utf8").splitlines()]:
        for command,key in re.findall(r"\\(eqref|ref)\{([^}]+)\}",row["translated_text"]):
            original=("("+labels[key][0]+")") if command=="eqref" else "Chapter "+labels[key][0] if key.startswith("chap:") else "Section "+labels[key][0] if key.startswith("sec:") else "["+labels[key][0]+"]"
            refs.append({"original_reference":original,"source_block":row["id"],"source_pages":provenance[row["id"]]["pdf_pages"],"source_printed_pages":provenance[row["id"]]["printed_pages"],"command":command,"label":key,"target_object":key.split(":",1)[1],"target_number":labels[key][0],"output_page":int(labels[key][1]),"translation_location":"translation/reviewed/sample.tex / block "+row["id"]})
    links=[]
    for page,n in zip(reader.pages,range(1,len(reader.pages)+1)):
        for annotation in page.get("/Annots",[]):
            action=annotation.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":assert str(action["/D"]) in dest;links.append({"page":n,"target":str(action["/D"])})
    dump("qa/translation/cross-reference-report.json",{"passed":True,"objects":objects,"references":refs,"pdf_links":links,"sample_external_locators_verified":True,"external_locators_are_not_translated_chapters":True})
    dump("qa/translation/name-report.json",{"passed":True,"checks":checks})
    dump("qa/translation/punctuation-report.json",{"passed":True,"violations":[],"scope":"Chinese sample prose; shared checker excludes protected math, commands, labels, keys and source inputs"})
    dump("qa/sample-automated-qa.json",{"passed":True,"sample":load("qa/sample-selection.json"),"names":checks,"objects_checked":len(objects),"links_checked":len(links),"schema_validation":"passed","compile":q,"visual_review":"pending","blocking_issues":[],"unresolved_terminology":0})
    guard();print(json.dumps({"passed":True,"objects":len(objects),"links":len(links),"names":checks},ensure_ascii=False))
def accept_sample():
    """Finish start-book through its existing processor callback, not approval."""
    from mathbook.workflow import start_book
    guard();a=load("qa/sample-automated-qa.json");v=load("qa/sample-visual-review.json")
    assert a["passed"] and v["passed"] and v["pdf_sha256"]==a["compile"]["pdf_sha256"]==m["sha256_file"](B.root/"output/sample-zh.pdf")
    def processor(book):
        assert book.book_id==ID
        report={"book_id":ID,"status":"passed",**{key:"passed" for key in ("template","source","extraction","structure","formula","cross_references","proper_names","punctuation","compile","schema","visual_review")},"blocking_issues":[],"unresolved_terminology":0,"source_pages":[25,26,27,28],"printed_pages":[15,16,17,18],"sample_scope":load("qa/sample-selection.json")["scope"],"source_blocks":a["sample"]["blocks"],"math_expressions":a["sample"]["math_expressions"],"pdf":"output/sample-zh.pdf","pdf_sha256":v["pdf_sha256"],"sample_user_approved":False,"full_book_translation_started":False}
        dump("qa/sample-qa.json",report)
    result=start_book(P,ID,processor=processor)
    state=load("qa/workflow-state.json");state.update({"sample_pages":[25,26,27,28],"sample_approved":False,"status":"awaiting-sample-approval"});dump("qa/workflow-state.json",state)
    plan=load("qa/sample-plan.json");plan.update({"representative_pages":[25,26,27,28],"selection_report":"qa/sample-selection.json","page_classification_counts":load("qa/pdf-diagnosis.json")["counts"]});dump("qa/sample-plan.json",plan)
    cfg=B.load_config();cfg.update({"phase":"sample","status":"awaiting-sample-approval","sample_output":"output/sample-zh.pdf","sample_scope":load("qa/sample-selection.json")["scope"],"sample_approved":False,"last_batch_report":"qa/sample-report.md"});dump("config/book.yaml",cfg)
    # Progress is an inventory, not permission to start full-book translation.
    progress=B.chapter_progress
    rows=[{"Unit ID":"frontmatter","Title":"Preface and frontmatter","QA Status":"pending","Notes":"Not translated; sample-only scope"}]
    chapter=None
    for item in load("structured/source/contents.json"):
        title=item["title"]
        ch=re.match(r"Chapter (\d+) (.+)",title)
        sec=re.match(r"(\d+)\.(\d+) (.+)",title)
        if ch:
            chapter=int(ch[1]);unit=f"chapter-{chapter:02}"+("-introduction" if chapter!=1 else "")
        elif sec:unit=f"chapter-{int(sec[1]):02}-section-{int(sec[2]):02}"
        elif title in ("Bibliography","Index"):unit=title.lower()
        else:continue
        passed=unit in {"chapter-02-section-04","chapter-02-section-05","chapter-02-section-06"}
        rows.append({"Unit ID":unit,"Title":title,"QA Status":"passed" if passed else "pending","Notes":"Sample technical QA passed; user approval pending; content is in reviewed/sample.tex; Section 2.6 excludes separate Box 2.1" if passed else "Not translated; sample-only scope"})
        if unit=="chapter-02-section-06":rows.append({"Unit ID":"chapter-02-summary","Title":"Box 2.1 / chapter summary","QA Status":"pending","Notes":"Explicitly excluded from sample"})
    if progress.exists():
        existing=list(csv.DictReader(progress.open(encoding="utf8"),delimiter="\t"))
        assert existing==rows,"Refuse to replace an existing progress inventory with different state"
    else:tsv("qa/chapter-progress.tsv",["Unit ID","Title","QA Status","Notes"],rows)
    from mathbook.workflow import project_record,update_project_record
    record=project_record(P,ID);record.title=cfg["title"];record.phase="sample";record.status="awaiting-sample-approval";record.blocking_issues="";update_project_record(P,record)
    write("PROJECT_STATUS.md",f"Book ID: {ID}\nTitle: Finite Element Exterior Calculus\nBranch: {R.branch}\nWorktree: {P.root}\nPhase: sample\nStatus: awaiting-sample-approval\nSource SHA-256: {m['SOURCE_SHA']}\nTemplate version: {cfg['template_version']}\nPDF type: native with illustrations; not scanned\nSource pages: 130\nSample: Sections 2.4-2.6 main text / PDF 25-28 / printed 15-18\nSample output: output/sample-zh.pdf\nSample QA: passed\nSample user approved: No\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation started: No\nRemote push: No\n")
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    issue={"id":"sample-source-homology-class-wording","category":"source","severity":"info","message":"Original PDF 25 speaks of the homology class of v in V_k without restating the cycle condition; preserved verbatim in meaning without adding an assumption.","source_location":{"page":25},"confidence":0.99,"review_status":"reviewed","details":{"blocking":False,"report":"qa/source/sample-source-observations.md"}}
    jsonschema.validate(issue,json.loads((P.root/"schemas/qa-issue.schema.json").read_text(encoding="utf8")))
    if not any(x["id"]==issue["id"] for x in issues):issues.append(issue)
    write("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    initial=load("qa/protected-inputs-initial.json");oldbranches=dict(line.split(" ",1) for line in initial["branches"])
    newbranches=dict(line.split(" ",1) for line in subprocess.run(["git","for-each-ref","--format=%(refname) %(objectname)","refs/heads/book/"],cwd=P.root,capture_output=True,text=True,check=True).stdout.splitlines())
    for key,value in oldbranches.items():
        if key!="refs/heads/book/"+ID:assert newbranches.get(key)==value,key
    changed=subprocess.run(["git","diff","--name-only",initial["initial_branch_head"]],cwd=P.root,capture_output=True,text=True,check=True).stdout.splitlines()
    changed+=subprocess.run(["git","ls-files","--others","--exclude-standard"],cwd=P.root,capture_output=True,text=True,check=True).stdout.splitlines()
    assert all(x.startswith("books/"+ID+"/") or x=="PROJECTS.md" for x in changed),changed
    registry_before=subprocess.run(["git","show",initial["initial_branch_head"]+":PROJECTS.md"],cwd=P.root,capture_output=True,text=True,encoding="utf8",check=True).stdout
    other=lambda text:[line for line in text.splitlines() if not line.startswith("| "+ID+" |")]
    assert other(registry_before)==other(P.projects_file.read_text(encoding="utf8"))
    visible=sorted(x.name for x in P.books.iterdir() if x.is_dir());assert visible==[ID],visible
    dump("qa/isolation-and-integrity.json",{"passed":True,"branch":P.git_branch(),"registered_worktree":R.worktree,"physical_worktree":str(P.root),"book_id":ID,"source_path":str(B.require_source_pdf()),"source_sha256":m['SOURCE_SHA'],"template_manifest_hash":m['TEMPLATE_SHA'],"raw_template_hashes_match_initial":True,"other_book_branches_unchanged":True,"visible_books":visible,"tracked_and_untracked_changes_only_this_book_and_its_registry_row":True,"other_registry_rows_unchanged":True,"shared_code_and_glossary_unchanged":True,"sample_user_approved":False,"full_book_translation_started":False,"remote_push":False})
    guard();print(json.dumps({"book_id":ID,"status":"awaiting-sample-approval","sample_pages":[25,26,27,28]}))
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("book_id",choices=[ID]);parser.add_argument("action",choices=["prepare","compile","audit","accept"]);args=parser.parse_args()
    {"prepare":prepare,"compile":compile_sample,"audit":audit,"accept":accept_sample}[args.action]()
