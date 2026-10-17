"""Book-local Chapter 2 evidence checks, not a translation generator."""
import argparse,collections,csv,json,re,runpy,subprocess
from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw

m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
B,P,R=m["B"],m["P"],m["R"]
units=["chapter-02-introduction",*[f"chapter-02-section-{i:02}" for i in range(1,6)]]

def names_and_terms():
    m["guard"]()
    with (B.root/"glossary/proper-names.tsv").open(encoding="utf8") as f:
        reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;names=list(reader)
    extra="Taylor Laplace Kronecker Helmholtz Neumann Dirichlet Toeplitz Poisson Gauss Green Fermi Hamiltonian Planck Wilson Pauli Lanczos Arnoldi Lagrange Lagrangian Gaussian Sylvester Newton Euclidean Riemannian Grassmann Grassman Stiefel Rayleigh Hessian Hermitian Laplacian".split()
    known=sorted({r["Source Form"] for r in names}|set(extra))
    report=[];blocks=[]
    for unit in units:
        source=[json.loads(x) for x in (B.root/f"structured/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        target=[json.loads(x) for x in (B.root/f"translation/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        assert [x["id"] for x in source]==[x["id"] for x in target]
        for a,b in zip(source,target):
            assert collections.Counter(m["math"](a["source_latex"]))==collections.Counter(m["math"](b["target_latex"]))
            blocks.append(a)
            for name in known:
                pattern=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])"
                en=len(re.findall(pattern,a["source_latex"]));zh=len(re.findall(pattern,b["target_latex"]))
                if en or zh:
                    report.append({"unit":unit,"block_id":a["id"],"name":name,"source":en,"translation":zh,"passed":en==zh})
    failures=[x for x in report if not x["passed"]]
    m["dump"]("qa/translation/chapter-02-name-report.json",{"passed":not failures,"checks":report,"failures":failures})
    assert not failures,failures
    existing={x["Source Form"] for x in names}
    for name in known:
        hit=next((x for x in report if x["name"]==name and x["source"]),None)
        if hit and name not in existing:
            block=next(x for x in blocks if x["id"]==hit["block_id"])
            row=dict.fromkeys(fields,"");row.update({"Source Form":name,"Canonical Form":name,"Category":"person-or-eponym",
                "First Occurrence":hit["block_id"]+" / PDF "+",".join(str(x["pdf_page"]) for x in block["source_pages"]),
                "Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed",
                "Notes":"Source spelling retained; Grassman and Grassmann are separate literal source spellings."})
            names.append(row)
    m["tsv"]("glossary/proper-names.tsv",fields,names)
    termdata=[
      ("finite difference method","有限差分方法","numerical PDE","approximating derivatives on a grid"),
      ("forward difference","向前差分","numerical PDE","first derivative from f(x+h) and f(x)"),
      ("backward difference","向后差分","numerical PDE","first derivative from f(x) and f(x-h)"),
      ("central difference","中心差分","numerical PDE","centered first or second derivative approximation"),
      ("Kronecker product","Kronecker 积","numerical linear algebra","block matrix product A tensor B"),
      ("Kronecker sum","Kronecker 和","numerical linear algebra","A tensor I plus I tensor B"),
      ("finite element method","有限元方法","numerical PDE","piecewise approximation of weak-form equations"),
      ("weak form","弱形式","numerical PDE","integral formulation of the Poisson problem"),
      ("test function","检验函数","numerical PDE","weight v in the weak formulation"),
      ("weight function","权函数","numerical PDE","alternative name of test function v"),
      ("one-body density matrix","单体密度矩阵","computational physics","electronic structure calculation"),
      ("hopping matrix","跃迁矩阵","computational physics","Wilson fermion matrix I minus kappa D"),
      ("shifted linear systems","移位线性方程组","numerical linear algebra","systems A plus scalar times identity"),
      ("least-squares regression","最小二乘回归","machine learning","fit model by squared residual minimization"),
      ("overfitting","过拟合","machine learning","fitting the noise in the training data"),
      ("regularization","正则化","machine learning","norm penalty in least-squares learning"),
      ("class-posterior probability","类别后验概率","machine learning","probability p(y given x)"),
      ("Gaussian kernel","Gaussian 核","machine learning","exponential squared-distance kernel"),
      ("vec operator","vec 算子","numerical linear algebra","stack columns of a matrix into a vector"),
      ("T-congruence Sylvester equation","T-合同 Sylvester 方程","matrix equations","AX plus transpose X times B equals C"),
      ("mode product","模乘积","tensor algebra","tensor times matrix along one index"),
      ("contracted product","缩并乘积","tensor algebra","summation over paired tensor indices"),
      ("retraction","回缩","manifold optimization","map an update back to the manifold"),
      ("thick-restart","厚重启","numerical linear algebra","Lanczos-type eigenvalue method"),
    ]
    with (P.glossary/"terminology.tsv").open(encoding="utf8") as f:global_terms=list(csv.DictReader(f,delimiter="\t"))
    with (B.root/"glossary/candidates.tsv").open(encoding="utf8") as f:
        reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;rows=list(reader)
    lookup=[]
    for en,zh,domain,context in termdata:
        matches=[x for x in global_terms if x["English"].casefold()==en.casefold()]
        exact=[x for x in matches if x["Domain"]==domain and x["Context"]==context and x["Status"]=="approved"]
        assert not exact or all(x["Preferred Chinese"]==zh for x in exact),(en,exact)
        lookup.append({"English":en,"Domain":domain,"Context":context,"global_english_matches":matches,"approved_context_matches":exact})
        if any(x["English"]==en and x["Domain"]==domain and x["Context"]==context for x in rows):continue
        row=dict.fromkeys(fields,"");row.update({"English":en,"Preferred Chinese":zh,"Domain":domain,"Context":context,"Status":"proposed",
          "First Source":m["ID"],"First Location":"Chapter 2 / PDF 43-84","Last Verified Source":m["ID"],"Last Verified Location":"Chapter 2 / PDF 43-84",
          "Notes":"Book-local contextual candidate; authoritative shared glossary unchanged."});rows.append(row)
    m["tsv"]("glossary/candidates.tsv",fields,rows)
    m["dump"]("qa/terminology/chapter-02-shared-lookup.json",lookup)
    print("Names and terms passed:",len(report),"name checks;",len(termdata),"contextual lookups")

def audit():
    names_and_terms();q=m["load"]("qa/latest-compilation.json");assert q["success"]
    pdf=B.root/"output/translation-progress.pdf"
    assert m["sha256_file"](pdf)==q["pdf_sha256"]
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8")
    auxrows={}
    for hit in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=m["brace"](aux,hit.end()-1);fields=[];pos=0
        while pos<len(body):
            value,pos=m["brace"](body,pos);fields.append(value)
        auxrows[hit[1]]=fields
    nums=[(key,value[0],value[1],value[3]) for key,value in auxrows.items() if key.startswith("eq:") and re.fullmatch(r"2\.\d+",value[0])]
    assert sorted(int(x[1].split(".")[1]) for x in nums)==list(range(1,76)),nums
    for prefix,end in [("fig:",13),("tab:",1)]:
        values=re.findall(r"\\newlabel\{"+prefix+r"[^}]+\}\{\{(2\.\d+)\}",aux)
        assert sorted(int(x.split(".")[1]) for x in values)==list(range(1,end+1)),values
    reader=PdfReader(pdf);dest=reader.named_destinations;links=[]
    for i,key in enumerate(["laplace-difference","helmholtz-difference","nonsymmetric-difference"],1):
        fields=auxrows["ex:"+key];assert fields[0]==str(i),fields
        page=reader.pages[int(fields[1])-1].extract_text()
        assert re.search(r"Example\s+"+str(i)+r"\s*\(",page),(key,page)
    for i,page in enumerate(reader.pages,1):
        for a in page.get("/Annots",[]):
            action=a.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":
                key=str(action["/D"]);assert key in dest,key
                links.append({"page":i,"target":key,"target_page":reader.get_destination_page_number(dest[key])+1})
    m["dump"]("qa/translation/chapter-02-pdf-link-report.json",{"passed":True,"links":links})
    blockdata=[]
    for unit in units:
        for line in (B.root/f"structured/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines():blockdata.append(json.loads(line))
    registry=[]
    auxlabels={x[0]:{"rendered_number":x[1],"output_page":int(x[2]),"destination":x[3]} for x in nums}
    for number,(label,*_) in enumerate(nums,1):
        block=next(x for x in blockdata if r"\label{"+label+"}" in x["source_latex"])
        registry.append({"original_object":"Equation 2."+str(number),"target_label":label,"block_id":block["id"],"source_pages":block["source_pages"],**auxlabels[label]})
    statement_sources={"thm:kronecker-product-properties":"Theorem 2.1","thm:kronecker-permutation":"Theorem 2.2","thm:vectorization-properties":"Theorem 2.3",
      "cor:kronecker-inverse":"Corollary 2.1","cor:kronecker-eigenpairs":"Corollary 2.2","cor:kronecker-sum-eigenpairs":"Corollary 2.3"}
    for label,original in statement_sources.items():
        hit=auxrows[label]
        block=next(x for x in blockdata if r"\label{"+label+"}" in x["source_latex"])
        registry.append({"original_object":original,"target_label":label,"rendered_number":hit[0],"output_page":int(hit[1]),"destination":hit[3],"source_pages":block["source_pages"],"block_id":block["id"]})
    for obj in registry:assert obj["destination"] in dest,obj
    references=[]
    targets={x["target_label"]:x for x in registry}
    for block in blockdata:
        for command,key in re.findall(r"\\(eqref|ref)\{([^}]+)\}",block["source_latex"]):
            if key in targets:references.append({"original_reference_target":targets[key]["original_object"],"label":key,"command":command,"translation_block":block["id"],"source_pages":block["source_pages"],"output_target_page":targets[key]["output_page"]})
    m["dump"]("qa/translation/chapter-02-cross-reference-registry.json",{"objects":registry,"references":references,"statement_numbering":"Accepted shared statement counter; source theorem/corollary series numbers preserved as metadata, not hard-coded body references."})
    m["dump"]("qa/translation/chapter-02-punctuation-report.json",{"passed":not q["latex_qa"]["punctuation_violations"],"violations":q["latex_qa"]["punctuation_violations"],"scope":"Translated body only, excluding protected mathematics/commands/keys/inputs"})
    formulas=sum(m["load"](f"qa/batches/{u}-content.json")["math_expressions"] for u in units)
    m["dump"]("qa/batches/chapter-02-automated-qa.json",{"passed":True,"units":units,"blocks":len(blockdata),"math_expressions":formulas,"numbered_equations":75,"figures":13,"tables":1,
      "internal_links":len(links),"source_pdf_pages":[43,84],"source_printed_pages":[31,72],"compile":q,"visual_review":"pending","whole_book_complete":False})
    files=sorted(Path(q["render_directory"]).glob("page-*.png"),key=lambda f:int(re.search(r"(\d+)\.png",f.name)[1]))
    out=B.assert_write_path(B.root/"workspace/pages/chapter-02-review"/q["pdf_sha256"][:16]);out.mkdir(parents=True,exist_ok=True)
    for start in range(24,len(files),6):
        sheet=Image.new("RGB",(1200,1700),"white");draw=ImageDraw.Draw(sheet)
        for i,f in enumerate(files[start:start+6]):
            im=Image.open(f);im.thumbnail((390,810));x=(i%3)*400;y=(i//3)*850
            draw.text((x+5,y+5),f"Output page {start+i+1}",fill="black");sheet.paste(im,(x,y+25))
        sheet.save(out/f"sheet-{start//6+1:02}.png")
    print(json.dumps({"blocks":len(blockdata),"math_expressions":formulas,"links":len(links),"review_sheets":str(out)}))

def accept():
    m["guard"]()
    q=m["load"]("qa/batches/chapter-02-automated-qa.json")
    v=m["load"]("qa/batches/chapter-02-visual-review.json")
    assert q["passed"] and v["passed"] and v["pdf_sha256"]==m["sha256_file"](B.root/"output/translation-progress.pdf")
    assert q["compile"]["pdf_sha256"]==v["pdf_sha256"]
    # Git stores canonical LF text while existing Python-written Windows files
    # can use CRLF. Compare canonical text without rewriting accepted files;
    # persist raw working-tree hashes for future byte-level checks.
    protected=[]
    first=m["load"]("qa/batches/chapter-01-automated-qa.json")["units"]
    for unit in first:
        for rel in [f"structured/reviewed/{unit}.tex",f"translation/reviewed/{unit}.tex", "tex/frontmatter.tex" if unit=="frontmatter" else f"tex/chapters/{unit}.tex"]:
            gitrel=f"books/{m['ID']}/{rel}"
            before=subprocess.run(["git","show","44a35c5:"+gitrel],cwd=P.root,capture_output=True,check=True).stdout
            actual=(B.root/rel).read_bytes();assert before.replace(b"\r\n",b"\n")==actual.replace(b"\r\n",b"\n"),rel
            protected.append({"path":rel,"sha256":m["hashlib"].sha256(actual).hexdigest(),"git_canonical_text_unchanged":True,
                "raw_bytes_match_git_blob":before==actual,"working_tree_crlf_count":actual.count(b"\r\n")})
    m["dump"]("qa/batches/chapter-02-protected-inputs.json",{"accepted_files":protected,
      "source_pdf_sha256":m["sha256_file"](B.require_source_pdf()),"template_manifest_hash":m["directory_manifest_hash"](P.template),
      "accepted_sample_sha256":m["sha256_file"](B.root/"tex/chapters/sample.tex"),"accepted_sample_pdf_sha256":m["sha256_file"](B.root/"output/sample-zh.pdf")})
    q["visual_review"]="passed";m["dump"]("qa/batches/chapter-02-automated-qa.json",q)
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    if not any(x["id"]=="chapter-02-source-observations" for x in issues):
        issues.append({"id":"chapter-02-source-observations","category":"source","severity":"warning","message":"Original-source mathematical and wording inconsistencies preserved; 24 observations documented, none silently repaired.","source_location":{"page":43},"confidence":1.0,"review_status":"reviewed","details":{"blocking":False,"report":"qa/source/chapter-02-source-observations.md"}})
    m["write"]("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    from mathbook.workflow import translate_book,next_incomplete_unit
    def status():
        m["write"]("PROJECT_STATUS.md",f"Book ID: {m['ID']}\nTitle: Krylov Subspace Methods for Linear Systems\nBranch: {R.branch}\nWorktree: {P.root}\nPhase: translation\nStatus: translating\n"
          f"Source SHA-256: {B.load_config()['source']['sha256']}\nTemplate version: {B.load_config()['template_version']}\n"
          "Sample approved: Yes\nApproved terminology: grade -> 阶\nCompleted content: Preface, Acknowledgements, Chapters 1 and 2\nLast integrated batch: chapter-02\nProgress output: output/translation-progress.pdf\n"
          f"Next incomplete unit: {next_incomplete_unit(B)}\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation complete: No\nRemote push: No\n")
    cfg=B.load_config();cfg.update({"status":"translating","last_batch_report":"qa/batches/chapter-02-report.md"});m["dump"]("config/book.yaml",cfg)
    class NeedNextUnit(Exception):pass
    def processor(book,unit):
        if unit not in units:raise NeedNextUnit(unit)
        with B.chapter_progress.open(encoding="utf8") as f:
            reader=csv.DictReader(f,delimiter="\t");fields=reader.fieldnames;rows=list(reader)
        row=next(x for x in rows if x["Unit ID"]==unit);assert row["QA Status"]=="pending"
        row.update({"QA Status":"passed","Notes":"Complete source-aligned Chapter 2; formula/name/reference/punctuation/compile/visual QA passed"})
        m["tsv"]("qa/chapter-progress.tsv",fields,rows);status()
    try:result=translate_book(P,m["ID"],processor=processor)
    except NeedNextUnit:
        state=m["load"]("qa/workflow-state.json");state.update({"status":"translating","next_unit":next_incomplete_unit(B)})
        m["dump"]("qa/workflow-state.json",state);status();result={"status":"translating","next_unit":next_incomplete_unit(B)}
    m["guard"]();print(json.dumps(result))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("action",choices=["names","audit","accept"]);a=p.parse_args()
    if a.action=="names":names_and_terms()
    elif a.action=="audit":audit()
    else:accept()
