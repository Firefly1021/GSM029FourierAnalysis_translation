"""Book-local QA for the complete first natural section of Chapter 3."""
import argparse,collections,csv,json,re,runpy,subprocess
from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));B,P,R=m["B"],m["P"],m["R"]
units=["chapter-03-introduction","chapter-03-section-01"];prefix="chapter-03-section-01"

def audit():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["success"]
    blocks=[];checks=[]
    with (B.root/"glossary/proper-names.tsv").open(encoding="utf8") as f:
        r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;names=list(r)
    extras=["Golub","O’Leary","Chebyshev","Paige","Saunders","Givens","Fridman","Bank","Chan"]
    known=sorted({r["Source Form"] for r in names}|set(extras))
    for unit in units:
        en=[json.loads(x) for x in (B.root/f"structured/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        zh=[json.loads(x) for x in (B.root/f"translation/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        for a,b in zip(en,zh):
            assert a["id"]==b["id"]
            assert collections.Counter(m["math"](a["source_latex"]))==collections.Counter(m["math"](b["target_latex"]))
            blocks.append(a)
            for name in known:
                pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])"
                se=len(re.findall(pat,a["source_latex"]));tz=len(re.findall(pat,b["target_latex"]))
                if se or tz:checks.append({"name":name,"block_id":a["id"],"source_count":se,"target_count":tz,"passed":se==tz})
    failures=[x for x in checks if not x["passed"]]
    m["dump"](f"qa/translation/{prefix}-names.json",{"passed":not failures,"checks":checks,"failures":failures});assert not failures,failures
    for name in extras:
        hit=next(x for x in checks if x["name"]==name)
        if any(x["Source Form"]==name for x in names):continue
        row=dict.fromkeys(fields,"");row.update({"Source Form":name,"Canonical Form":name,"Category":"person-or-eponym","First Occurrence":hit["block_id"],"Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed","Notes":"Exact source name preserved, including the internal apostrophe in O’Leary."});names.append(row)
    m["tsv"]("glossary/proper-names.tsv",fields,names)
    with (P.glossary/"terminology.tsv").open(encoding="utf8") as f:global_terms=list(csv.DictReader(f,delimiter="\t"))
    with (B.root/"glossary/candidates.tsv").open(encoding="utf8") as f:
        r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;terms=list(r)
    termdata=[("Conjugate Gradient","共轭梯度","CG method"),("Conjugate Residual","共轭残差","CR method"),
      ("residual vector","残差向量","b minus A times approximate solution"),
      ("Minimal Residual","最小残差","MINRES method"),("preconditioned CG method","预条件 CG 方法","Hermitian positive definite preconditioned iteration"),
      ("preconditioned CR method","预条件 CR 方法","preconditioned conjugate residual iteration"),
      ("near breakdown","近中断","a denominator close to zero causes numerical instability"),
      ("Givens rotation","Givens 旋转","unitary rotation in the projected least-squares problem"),
      ("composite step","复合步","one-by-one or two-by-two block factorization to avoid breakdown"),
      ("hyperbolic pairs","双曲对","related remedy for indefinite projected systems")]
    lookups=[]
    for english,chinese,context in termdata:
        domain="numerical linear algebra"
        global_matches=[x for x in global_terms if x["English"].casefold()==english.casefold()]
        approved=[x for x in global_matches if x["Domain"]==domain and x["Context"]==context and x["Status"]=="approved"]
        assert not approved or all(x["Preferred Chinese"]==chinese for x in approved)
        local=[x for x in terms if x["English"]==english and x["Domain"]==domain and x["Context"]==context]
        assert not local or all(x["Preferred Chinese"]==chinese for x in local)
        lookups.append({"English":english,"Domain":domain,"Context":context,"global_matches":global_matches,"reused_book_records":local})
        if not local:
            row=dict.fromkeys(fields,"");row.update({"English":english,"Preferred Chinese":chinese,"Domain":domain,"Context":context,"Status":"proposed","First Source":m["ID"],"First Location":"Section 3.1 / PDF 85-102","Last Verified Source":m["ID"],"Last Verified Location":"Section 3.1 / PDF 85-102","Notes":"Book-local proposal; no global promotion."});terms.append(row)
    m["tsv"]("glossary/candidates.tsv",fields,terms);m["dump"](f"qa/terminology/{prefix}-lookup.json",lookups)
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");labels={}
    for h in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=m["brace"](aux,h.end()-1);row=[];pos=0
        while pos<len(body):v,pos=m["brace"](body,pos);row.append(v)
        labels[h[1]]=row
    objects=[]
    for kind,count in [("eq:",39),("alg:",5)]:
        entries=[(k,v) for k,v in labels.items() if k.startswith(kind) and re.fullmatch(r"3\.\d+",v[0])]
        assert sorted(int(v[0].split(".")[1]) for k,v in entries)==list(range(1,count+1)),entries
        for k,v in entries:
            block=next(x for x in blocks if r"\label{"+k+"}" in x["source_latex"])
            objects.append({"label":k,"source_number":v[0],"rendered_number":v[0],"output_page":int(v[1]),"destination":v[3],"source_block":block["id"],"source_pages":block["source_pages"]})
    original={"prop:cg-orthogonality":"Proposition 3.1","cor:cg-krylov-orthogonality":"Corollary 3.1","thm:cg-energy-optimality":"Theorem 3.1","thm:cg-condition-number-bound":"Theorem 3.2"}
    for key,value in original.items():
        v=labels[key];objects.append({"label":key,"source_number":value,"rendered_number":v[0],"output_page":int(v[1]),"destination":v[3]})
    pdf=B.root/"output/translation-progress.pdf";reader=PdfReader(pdf);dest=reader.named_destinations
    assert m["sha256_file"](pdf)==q["pdf_sha256"]
    for obj in objects:assert obj["destination"] in dest,obj
    links=[]
    for i,page in enumerate(reader.pages,1):
        for a in page.get("/Annots",[]):
            action=a.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":
                key=str(action["/D"]);assert key in dest,key
                links.append({"page":i,"destination":key,"target_page":reader.get_destination_page_number(dest[key])+1})
    refs=[{"block_id":b["id"],"source_pages":b["source_pages"],"command":c,"label":k,"output_target_page":int(labels[k][1])} for b in blocks for c,k in re.findall(r"\\(eqref|ref)\{([^}]+)\}",b["source_latex"])]
    m["dump"](f"qa/translation/{prefix}-references.json",{"passed":True,"objects":objects,"references":refs,"pdf_links":links,"external_citation_locators":[{"reference_key":"160","section":"2.4"},{"reference_key":"16","theorem":"2.2"}],"note":"External publication locators are citation metadata, not hard-coded local book object references."})
    for x in m["load"]("qa/batches/chapter-02-protected-inputs.json")["accepted_files"]:
        assert m["sha256_file"](B.root/x["path"])==x["sha256"],x["path"]
    formulas=sum(m["load"](f"qa/batches/{u}-content.json")["math_expressions"] for u in units)
    m["dump"](f"qa/batches/{prefix}-automated-qa.json",{"passed":True,"units":units,"blocks":len(blocks),"math_expressions":formulas,"numbered_equations":39,"algorithms":5,"name_checks":len(checks),"compile":q,"visual_review":"pending","whole_chapter_three_complete":False,"whole_book_complete":False})
    start=int(labels["chap:krylov-classification"][1]);out=B.assert_write_path(B.root/"workspace/pages"/(prefix+"-review")/q["pdf_sha256"][:16]);out.mkdir(parents=True,exist_ok=True)
    files=sorted(Path(q["render_directory"]).glob("page-*.png"),key=lambda p:int(re.search(r"(\d+)\.png",p.name)[1]))
    for n in range(start-1,len(files),6):
        sheet=Image.new("RGB",(1200,1700),"white");draw=ImageDraw.Draw(sheet)
        for i,file in enumerate(files[n:n+6]):
            im=Image.open(file);im.thumbnail((390,810));x=i%3*400;y=i//3*850;draw.text((x,y+4),f"Output page {n+i+1}",fill="black");sheet.paste(im,(x,y+25))
        sheet.save(out/f"sheet-{n+1:02}.png")
    print(json.dumps({"blocks":len(blocks),"math":formulas,"names":len(checks),"pages":len(reader.pages),"start_page":start,"sheets":str(out)},ensure_ascii=False))

def accept():
    m["guard"]();q=m["load"](f"qa/batches/{prefix}-automated-qa.json");v=m["load"](f"qa/batches/{prefix}-visual-review.json")
    assert q["passed"] and v["passed"] and v["pdf_sha256"]==q["compile"]["pdf_sha256"]==m["sha256_file"](B.root/"output/translation-progress.pdf")
    q["visual_review"]="passed";m["dump"](f"qa/batches/{prefix}-automated-qa.json",q)
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    issueid=prefix+"-source-observations"
    if not any(x["id"]==issueid for x in issues):
        issues.append({"id":issueid,"category":"source","severity":"warning","message":"Source inconsistencies and notation preserved without silent correction; see detailed report.","source_location":{"page":85},"confidence":1.0,"review_status":"reviewed","details":{"blocking":False,"report":f"qa/source/{prefix}-source-observations.md"}})
    m["write"]("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    cfg=B.load_config();cfg.update({"status":"translating","last_batch_report":f"qa/batches/{prefix}-report.md"});m["dump"]("config/book.yaml",cfg)
    from mathbook.workflow import translate_book,next_incomplete_unit
    def status():
        m["write"]("PROJECT_STATUS.md",f"Book ID: {m['ID']}\nTitle: Krylov Subspace Methods for Linear Systems\nBranch: {R.branch}\nWorktree: {P.root}\nPhase: translation\nStatus: translating\nSource SHA-256: {cfg['source']['sha256']}\nTemplate version: {cfg['template_version']}\nSample approved: Yes\nApproved terminology: grade -> 阶\nCompleted content: Preface, Acknowledgements, Chapters 1 and 2, Chapter 3 introduction and Section 3.1\nLast integrated batch: chapter-03-section-01\nProgress output: output/translation-progress.pdf\nNext incomplete unit: {next_incomplete_unit(B)}\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation complete: No\nRemote push: No\n")
    class NeedNextUnit(Exception):pass
    def processor(book,unit):
        if unit not in units:raise NeedNextUnit(unit)
        with B.chapter_progress.open(encoding="utf8") as f:
            r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;rows=list(r)
        row=next(x for x in rows if x["Unit ID"]==unit);assert row["QA Status"]=="pending"
        row.update({"QA Status":"passed","Notes":"Complete Chapter 3 introductory material / Section 3.1; source/math/name/reference/punctuation/compile/visual QA passed"})
        m["tsv"]("qa/chapter-progress.tsv",fields,rows);status()
    try:result=translate_book(P,m["ID"],processor=processor)
    except NeedNextUnit:
        state=m["load"]("qa/workflow-state.json");state.update({"status":"translating","next_unit":next_incomplete_unit(B)})
        m["dump"]("qa/workflow-state.json",state);status();result={"status":"translating","next_unit":next_incomplete_unit(B)}
    m["guard"]();print(json.dumps(result))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("action",choices=["audit","accept"],default="audit",nargs="?");args=p.parse_args()
    audit() if args.action=="audit" else accept()
