"""Book-local QA for explicitly selected complete natural sections of Chapter 5."""
import argparse,collections,csv,json,re,runpy,subprocess
from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageDraw
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));B,P,R=m["B"],m["P"],m["R"]
units=["chapter-05-section-03"];prefix="chapter-05-section-03"

def audit():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["success"]
    blocks=[];checks=[]
    with (B.root/"glossary/proper-names.tsv").open(encoding="utf8") as f:
        r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;names=list(r)
    extras=["Schur","Raphson","Fréchet","Gröbner"]
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
    expected_lines={"alg:schur-matrix-square-root":10,"alg:newton-matrix-square-root":4,"alg:incremental-newton-square-root":5,"alg:schur-matrix-pth-root":14,"alg:newton-matrix-pth-root":4,"alg:incremental-newton-pth-root":5}
    line_checks=[]
    for key,total in expected_lines.items():
        block=next(x for x in blocks if r"\label{"+key+"}" in x["source_latex"])
        count=len(re.findall(r"\\(?:State(?!x)|For|EndFor|While|EndWhile|If|EndIf|Else)\b",block["source_latex"]))
        assert count==total,(key,count,total)
        line_checks.append({"label":key,"source_numbered_lines":total,"restored_numbered_lines":count,"passed":True})
    m["dump"](f"qa/formula/{prefix}-algorithm-lines.json",line_checks)
    m["dump"](f"qa/translation/{prefix}-names.json",{"passed":not failures,"checks":checks,"failures":failures});assert not failures,failures
    for name in extras:
        hit=next((x for x in checks if x["name"]==name),None)
        if not hit:continue
        if any(x["Source Form"]==name for x in names):continue
        row=dict.fromkeys(fields,"");row.update({"Source Form":name,"Canonical Form":name,"Category":"person-or-eponym","First Occurrence":hit["block_id"],"Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed","Notes":"Exact original spelling, initials, punctuation and diacritics preserved."});names.append(row)
    m["tsv"]("glossary/proper-names.tsv",fields,names)
    with (P.glossary/"terminology.tsv").open(encoding="utf8") as f:global_terms=list(csv.DictReader(f,delimiter="\t"))
    with (B.root/"glossary/candidates.tsv").open(encoding="utf8") as f:
        r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;terms=list(r)
    termdata=[("principal matrix square root","矩阵主平方根","unique square root with spectrum in the right half-plane"),
      ("principal matrix pth root","矩阵主 p 次根","unique pth root with spectrum in the indicated sector"),
      ("incremental Newton iteration","增量 Newton 迭代","numerically stable correction iteration for matrix roots")]
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
            loc="Section 5.3 / PDF 206-210"
            row=dict.fromkeys(fields,"");row.update({"English":english,"Preferred Chinese":chinese,"Domain":domain,"Context":context,"Status":"proposed","First Source":m["ID"],"First Location":loc,"Last Verified Source":m["ID"],"Last Verified Location":loc,"Notes":"Book-local proposal; no global promotion."});terms.append(row)
    m["tsv"]("glossary/candidates.tsv",fields,terms);m["dump"](f"qa/terminology/{prefix}-lookup.json",lookups)
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");labels={}
    for h in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=m["brace"](aux,h.end()-1);row=[];pos=0
        while pos<len(body):v,pos=m["brace"](body,pos);row.append(v)
        labels[h[1]]=row
    objects=[]
    for kind,first,last in [("alg:",1,6)]:
        entries=[(k,v) for k,v in labels.items() if k.startswith(kind) and re.fullmatch(r"5\.\d+",v[0]) and first<=int(v[0].split(".")[1])<=last]
        assert sorted(int(v[0].split(".")[1]) for k,v in entries)==list(range(first,last+1)),entries
        for k,v in entries:
            block=next(x for x in blocks if r"\label{"+k+"}" in x["source_latex"])
            objects.append({"label":k,"source_number":v[0],"rendered_number":v[0],"output_page":int(v[1]),"destination":v[3],"source_block":block["id"],"source_pages":block["source_pages"]})
    original={"thm:principal-matrix-square-root":"Theorem 5.3","thm:principal-matrix-pth-root":"Theorem 5.4"}
    for key,value in original.items():
        v=labels[key];objects.append({"label":key,"source_number":value,"rendered_number":v[0],"output_page":int(v[1]),"destination":v[3]})
    pdf=B.root/"output/translation-progress.pdf";reader=PdfReader(pdf);dest=reader.named_destinations
    assert m["sha256_file"](pdf)==q["pdf_sha256"]
    for obj in objects:
        assert obj["destination"] in dest,obj
        assert reader.get_destination_page_number(dest[obj["destination"]])+1==obj["output_page"],obj
    links=[]
    for i,page in enumerate(reader.pages,1):
        for a in page.get("/Annots",[]):
            action=a.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":
                key=str(action["/D"]);assert key in dest,key
                links.append({"page":i,"destination":key,"target_page":reader.get_destination_page_number(dest[key])+1})
    refs=[{"block_id":b["id"],"source_pages":b["source_pages"],"command":c,"label":k,"output_target_page":int(labels[k][1])} for b in blocks for c,k in re.findall(r"\\(eqref|ref)\{([^}]+)\}",b["source_latex"])]
    external=[]
    m["dump"](f"qa/translation/{prefix}-references.json",{"passed":True,"objects":objects,"references":refs,"pdf_links":links,"external_citation_locators":external,"note":"External publication locators are citation metadata, not hard-coded local book object references."})
    for x in m["load"]("qa/batches/chapter-02-protected-inputs.json")["accepted_files"]:
        assert m["sha256_file"](B.root/x["path"])==x["sha256"],x["path"]
    with B.chapter_progress.open(encoding="utf8") as f:accepted=[x["Unit ID"] for x in csv.DictReader(f,delimiter="\t") if x["QA Status"]=="passed"]
    protected=[]
    for unit in accepted:
        for folder,suffix in [("translation/authored",".bilingual.tex"),("structured/reviewed",".tex"),("translation/reviewed",".tex"),("tex/chapters",".tex")]:
            file=B.root/folder/(unit+suffix)
            if not file.is_file():continue
            repo_path=file.relative_to(P.root).as_posix()
            blob=subprocess.run(["git","show","HEAD:"+repo_path],cwd=P.root,capture_output=True,check=True).stdout
            current=file.read_bytes()
            assert current.replace(b"\r\n",b"\n")==blob.replace(b"\r\n",b"\n"),repo_path
            protected.append({"path":file.relative_to(B.root).as_posix(),"sha256":m["sha256_file"](file),"git_canonical_text_unchanged":True})
    assert m["sha256_file"](B.root/"output/sample-zh.pdf")=="53b6521644665c795c44ab1227f0ad2d381a0d97f1d5fbe6af32f01228e149b7"
    m["dump"](f"qa/batches/{prefix}-protected-inputs.json",{"accepted_files":protected,"sample_pdf_unchanged":True,"source_and_template_guards_passed":True})
    formulas=sum(m["load"](f"qa/batches/{u}-content.json")["math_expressions"] for u in units)
    m["dump"](f"qa/batches/{prefix}-automated-qa.json",{"passed":True,"units":units,"blocks":len(blocks),"math_expressions":formulas,"numbered_equations":0,"algorithms":6,"figures":0,"tables":0,"name_checks":len(checks),"compile":q,"visual_review":"pending","whole_chapter_five_complete":False,"whole_book_complete":False})
    start=int(labels["sec:matrix-roots"][1]);out=B.assert_write_path(B.root/"workspace/pages"/(prefix+"-review")/q["pdf_sha256"][:16]);out.mkdir(parents=True,exist_ok=True)
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
        issues.append({"id":issueid,"category":"source","severity":"warning","message":"Source inconsistencies and notation preserved without silent correction; see detailed report.","source_location":{"page":206},"confidence":1.0,"review_status":"reviewed","details":{"blocking":False,"report":f"qa/source/{prefix}-source-observations.md"}})
    m["write"]("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    cfg=B.load_config();cfg.update({"status":"translating","last_batch_report":f"qa/batches/{prefix}-report.md"});m["dump"]("config/book.yaml",cfg)
    from mathbook.workflow import translate_book,next_incomplete_unit
    def status():
        m["write"]("PROJECT_STATUS.md",f"Book ID: {m['ID']}\nTitle: Krylov Subspace Methods for Linear Systems\nBranch: {R.branch}\nWorktree: {P.root}\nPhase: translation\nStatus: translating\nSource SHA-256: {cfg['source']['sha256']}\nTemplate version: {cfg['template_version']}\nSample approved: Yes\nApproved terminology: grade -> 阶\nCompleted content: Preface, Acknowledgements, Chapters 1-4 in full; Chapter 5 introduction and Sections 5.1-5.3\nLast integrated batch: chapter-05-section-03\nProgress output: output/translation-progress.pdf\nNext incomplete unit: {next_incomplete_unit(B)}\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation complete: No\nRemote push: No\n")
    class NeedNextUnit(Exception):pass
    def processor(book,unit):
        if unit not in units:raise NeedNextUnit(unit)
        with B.chapter_progress.open(encoding="utf8") as f:
            r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;rows=list(r)
        row=next(x for x in rows if x["Unit ID"]==unit);assert row["QA Status"]=="pending"
        row.update({"QA Status":"passed","Notes":f"Complete {unit}; source/math/name/reference/punctuation/compile/visual QA passed"})
        m["tsv"]("qa/chapter-progress.tsv",fields,rows);status()
    try:result=translate_book(P,m["ID"],processor=processor)
    except NeedNextUnit:
        state=m["load"]("qa/workflow-state.json");state.update({"status":"translating","next_unit":next_incomplete_unit(B)})
        m["dump"]("qa/workflow-state.json",state);status();result={"status":"translating","next_unit":next_incomplete_unit(B)}
    m["guard"]();print(json.dumps(result))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("action",choices=["audit","accept"],default="audit",nargs="?");args=p.parse_args()
    audit() if args.action=="audit" else accept()
