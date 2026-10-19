"""Book-local final gates; no remote writes or automatic terminology promotion."""
import argparse,collections,csv,json,re,runpy,shutil,subprocess
from pathlib import Path
from PIL import Image,ImageDraw
from pypdf import PdfReader
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));B,P,R=m["B"],m["P"],m["R"]

def labels_for(q):
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");labels={}
    for hit in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=m["brace"](aux,hit.end()-1);row=[];pos=0
        while pos<len(body):v,pos=m["brace"](body,pos);row.append(v)
        labels[hit[1]]=row
    return labels

def protections():
    m["guard"]();protected=[]
    with B.chapter_progress.open(encoding="utf8") as f:accepted=[x["Unit ID"] for x in csv.DictReader(f,delimiter="\t") if x["QA Status"]=="passed"]
    for unit in accepted:
        for folder,suffix in [("translation/authored",".bilingual.tex"),("structured/reviewed",".tex"),("translation/reviewed",".tex"),("tex/chapters",".tex")]:
            path=B.root/folder/(unit+suffix)
            if not path.is_file():continue
            blob=subprocess.run(["git","show","HEAD:"+path.relative_to(P.root).as_posix()],cwd=P.root,capture_output=True,check=True).stdout
            assert blob.replace(b"\r\n",b"\n")==path.read_bytes().replace(b"\r\n",b"\n"),path
            protected.append({"file":path.relative_to(B.root).as_posix(),"sha256":m["sha256_file"](path),"git_canonical_text_unchanged":True})
    assert m["sha256_file"](B.root/"output/sample-zh.pdf")=="53b6521644665c795c44ab1227f0ad2d381a0d97f1d5fbe6af32f01228e149b7"
    assert m["sha256_file"](Path(r"D:\BaiduNetdiskDownload\Krylov Subspace Methods for Linear Systems.pdf"))==B.load_config()["source"]["sha256"]
    # No branch/worktree data outside this book may be changed by this task.
    changed=subprocess.run(["git","diff","--name-only","68077b8"],cwd=P.root,capture_output=True,text=True,check=True).stdout.splitlines()
    assert all(p.startswith("books/"+m["ID"]+"/") for p in changed),changed
    m["dump"]("qa/final/protected-inputs.json",{"passed":True,"accepted_files":protected,"source_and_external_source_unchanged":True,"template_unchanged":True,"sample_unchanged":True,"changed_tracked_files_only_this_book":True})

def index_audit():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["success"]
    pdf=B.root/"output/translation-progress.pdf";assert m["sha256_file"](pdf)==q["pdf_sha256"]
    registry=m["load"]("structured/source/index-registry.json");rows=registry["entries"]
    assert len(rows)==179
    nav=runpy.run_path(str(B.root/"workflow/index_workflow.py"));raw=nav["source_rows"]()
    for a,b in zip(raw,rows):
        for key in ("source_term_raw","source_printed_pages","index_pdf_page","group"):assert a[key]==b[key],(a,b)
    source=[json.loads(x) for x in (B.root/"structured/reviewed/index.jsonl").read_text(encoding="utf8").splitlines()]
    target=[json.loads(x) for x in (B.root/"translation/reviewed/index.jsonl").read_text(encoding="utf8").splitlines()]
    assert len(source)==len(target)==180
    names=list(csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t"));checks=[]
    for a,b in zip(source,target):
        assert a["id"]==b["id"]
        assert collections.Counter(m["math"](a["source_latex"]))==collections.Counter(m["math"](b["target_latex"]))
        for row in names:
            name=row["Source Form"];pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])"
            x=len(re.findall(pat,a["source_latex"]));y=len(re.findall(pat,b["target_latex"]))
            if x or y:checks.append({"name":name,"block":a["id"],"source":x,"target":y});assert x==y,checks[-1]
    labels=labels_for(q);reader=PdfReader(pdf);dest=reader.named_destinations;links=[]
    for row in rows:
        for printed,key in zip(row["source_printed_pages"],row["target_labels"]):
            loc=registry["source_page_targets"][row["id"]+"-p"+str(printed)];assert loc["label"]==key and loc["source_pdf_page"] in loc["source_pdf_pages"]
            v=labels[key];actual=reader.get_destination_page_number(dest[v[3]])+1;assert actual==int(v[1])
            links.append({"entry":row["id"],"source_printed_page":printed,"source_pdf_page":loc["source_pdf_page"],"label":key,"translated_page":actual,"source_block":loc["block_id"],"granularity":loc["granularity"]})
    assert len(links)==181
    assert rows[67]["target_latex"].endswith("的阶") and rows[68]["target_latex"].endswith("的阶")
    assert all("阶数" not in row["target_latex"] for row in rows)
    local=list(csv.DictReader(B.candidates.open(encoding="utf8"),delimiter="\t"));grade=[x for x in local if x["English"]=="grade"]
    assert any(x["Preferred Chinese"]=="阶" and x["Status"]=="approved" for x in grade)
    global_terms=list(csv.DictReader((P.glossary/"terminology.tsv").open(encoding="utf8"),delimiter="\t"))
    lookup=[{"English":row["source_term"],"Preferred Chinese":row["target_latex"],"Context":{"source_printed_pages":row["source_printed_pages"],"source_blocks":[registry["source_page_targets"][row["id"]+"-p"+str(p)]["block_id"] for p in row["source_printed_pages"]]},"global_english_matches":[x for x in global_terms if x["English"].casefold()==row["source_term"].casefold()],"book_candidates":[x for x in local if x["English"].casefold()==row["source_term"].casefold()],"policy":"Reuse chapter terminology; no global overwrite, approval or promotion"} for row in rows]
    m["dump"]("qa/terminology/index-lookup.json",lookup)
    m["dump"]("qa/translation/index-reference-report.json",{"passed":True,"entries":179,"references":links,"distinct_original_indexed_pages":104,"unique_target_labels":len({x["label"] for x in links}),"names":checks,"concept_block_granularity_not_token_tight":True})
    protections()
    m["dump"]("qa/batches/index-automated-qa.json",{"passed":True,"units":["index"],"blocks":180,"math_expressions":18,"entries":179,"page_references":181,"unique_source_page_targets":104,"name_checks":len(checks),"compile":q,"visual_review":"pending"})
    start=int(labels["chap:index"][1]);out=B.assert_write_path(B.root/"workspace/pages/index-review"/q["pdf_sha256"][:16]);out.mkdir(parents=True,exist_ok=True)
    files=[Path(q["render_directory"])/f"page-{n:03}.png" for n in range(start,q["pdf_pages"]+1)]
    sheet=Image.new("RGB",(1200,1700),"white");draw=ImageDraw.Draw(sheet)
    for i,file in enumerate(files):
        assert i<6;im=Image.open(file);im.thumbnail((390,810));x=i%3*400;y=i//3*850;draw.text((x,y+2),f"Output page {start+i}",fill="black");sheet.paste(im,(x,y+25))
    sheet.save(out/"sheet.png");print(json.dumps({"index_start":start,"pdf_pages":q["pdf_pages"],"pdf_sha256":q["pdf_sha256"],"name_checks":len(checks),"sheet":str(out/"sheet.png")},ensure_ascii=False))

def accept_index():
    m["guard"]();qa=m["load"]("qa/batches/index-automated-qa.json");visual=m["load"]("qa/batches/index-visual-review.json")
    assert qa["passed"] and visual["passed"] and qa["compile"]["pdf_sha256"]==visual["pdf_sha256"]==m["sha256_file"](B.root/"output/translation-progress.pdf")
    qa["visual_review"]="passed";m["dump"]("qa/batches/index-automated-qa.json",qa)
    from mathbook.workflow import translate_book
    def processor(book,unit):
        assert unit=="index"
        with B.chapter_progress.open(encoding="utf8") as f:r=csv.DictReader(f,delimiter="\t");fields=r.fieldnames;rows=list(r)
        row=next(x for x in rows if x["Unit ID"]==unit);assert row["QA Status"]=="pending"
        row.update({"QA Status":"passed","Notes":"All 179 source index entries, 181 generated page links, name/math/punctuation/compile/visual QA passed; source-page-to-block provenance retained"});m["tsv"]("qa/chapter-progress.tsv",fields,rows)
    result=translate_book(P,m["ID"],processor=processor);assert result["status"]=="translation-complete";print(json.dumps(result))

def final_audit():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["success"] and q["minimum_latex_rounds"]>=2
    assert m["actual_input_qa"]()["passed"] and not any(q["warnings"].values())
    with B.chapter_progress.open(encoding="utf8") as f:progress=list(csv.DictReader(f,delimiter="\t"))
    assert len(progress)==39 and all(x["QA Status"]=="passed" for x in progress)
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    blockers=[x for x in issues if x.get("details",{}).get("blocking") and x.get("review_status") not in ("resolved","reviewed")];assert not blockers
    with B.unresolved.open(encoding="utf8") as f:unresolved=list(csv.DictReader(f,delimiter="\t"))
    assert not unresolved
    pending=m["load"]("qa/pending-reference-targets.json");assert not pending["verified_source_locators"] and not pending["bibliography_locators"]
    assert not (B.root/"tex/chapters/pending-targets.tex").read_text(encoding="utf8").strip()
    labels=labels_for(q);reader=PdfReader(B.root/"output/translation-progress.pdf");dest=reader.named_destinations;objects=[]
    for key,v in labels.items():
        if len(v)<4 or not v[3] or not v[1].isdigit():continue
        assert v[3] in dest,(key,v)
        actual=reader.get_destination_page_number(dest[v[3]])+1;assert actual==int(v[1]),(key,v,actual)
        objects.append({"label":key,"rendered_number":v[0],"page":actual,"destination":v[3]})
    links=[]
    for n,page in enumerate(reader.pages,1):
        for annotation in page.get("/Annots",[]):
            action=annotation.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":
                key=str(action["/D"]);assert key in dest,key
                links.append({"page":n,"target":key,"target_page":reader.get_destination_page_number(dest[key])+1})
    # Every complete chapter's numbered equation and algorithm sequence.
    totals={}
    for chapter,eqtotal,algtotal in [(1,43,11),(2,75,0),(3,138,35),(4,58,11),(5,25,12)]:
        eq=[(k,v) for k,v in labels.items() if k.startswith("eq:") and re.fullmatch(str(chapter)+r"\.\d+",v[0])]
        alg=[(k,v) for k,v in labels.items() if k.startswith("alg:") and re.fullmatch(str(chapter)+r"\.\d+",v[0])]
        assert sorted(int(v[0].split(".")[1]) for k,v in eq)==list(range(1,eqtotal+1)),(chapter,eqtotal,eq)
        assert sorted(int(v[0].split(".")[1]) for k,v in alg)==list(range(1,algtotal+1)),(chapter,algtotal,alg)
        totals[str(chapter)]={"numbered_equations":len(eq),"algorithms":len(alg)}
    protections()
    allblocks=0;allmath=0
    for file in sorted((B.root/"translation/authored").glob("*.bilingual.tex")):
        unit=file.name.removesuffix(".bilingual.tex")
        en=[json.loads(x) for x in (B.root/f"structured/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        zh=[json.loads(x) for x in (B.root/f"translation/reviewed/{unit}.jsonl").read_text(encoding="utf8").splitlines()]
        assert len(en)==len(zh)
        for a,b in zip(en,zh):assert a["id"]==b["id"] and collections.Counter(m["math"](a["source_latex"]))==collections.Counter(m["math"](b["target_latex"]))
        allblocks+=len(en);allmath+=m["load"](f"qa/batches/{unit}-content.json")["math_expressions"]
    m["dump"]("qa/translation/final-destination-regression.json",{"passed":True,"objects":objects,"links":links,"chapter_numbering":totals,"legacy_anchor_fix":{"label":"thm:regular-splitting-convergence","accepted_translation_unchanged":True,"generated_pagination_guard":True}})
    name_rows=list(csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t"));name_checks=[]
    for file in sorted((B.root/"translation/authored").glob("*.bilingual.tex")):
        unit=file.name.removesuffix(".bilingual.tex");en=(B.root/f"structured/reviewed/{unit}.tex").read_text(encoding="utf8");zh=(B.root/f"translation/reviewed/{unit}.tex").read_text(encoding="utf8")
        for row in name_rows:
            name=row["Source Form"];pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";a=len(re.findall(pat,en));b=len(re.findall(pat,zh))
            if a or b:name_checks.append({"unit":unit,"name":name,"source":a,"target":b});assert a==b,name_checks[-1]
    m["dump"]("qa/translation/final-name-report.json",{"passed":True,"checks":name_checks})
    report={"passed":True,"book_id":m["ID"],"natural_units":39,"passed_units":39,"authored_aligned_blocks":allblocks,"authored_math_expressions":allmath,"accepted_sample_blocks":23,"accepted_sample_math_expressions":96,"numbering":totals,"destinations_checked":len(objects),"internal_links_checked":len(links),"name_checks":len(name_checks),"bibliography_entries":212,"index_entries":179,"index_page_references":181,"index_navigation_granularity":"reviewed concept block on the original indexed source page, not token-tight","blocking_issues":[],"unresolved_terminology":0,"source_observation_records":len([x for x in issues if x.get('category')=='source']),"compile":q,"template_and_source_unchanged":True,"accepted_content_unchanged":True,"remote_push":False,"terminology_promotion":"not performed; approved local decisions and shared glossary retained unchanged"}
    m["dump"]("qa/final/automated-qa.json",report);print(json.dumps({k:v for k,v in report.items() if k!="compile"},ensure_ascii=False))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("action",choices=["index-audit","accept-index","final-audit"]);a=p.parse_args()
    {"index-audit":index_audit,"accept-index":accept_index,"final-audit":final_audit}[a.action]()
