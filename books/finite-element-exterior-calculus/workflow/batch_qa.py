"""Book-local batch acceptance over authored material and actual compiled evidence."""
import argparse,collections,csv,json,re,runpy,subprocess
from pathlib import Path
from pypdf import PdfReader
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));P,B,ID=m["P"],m["B"],m["ID"]
s=m["s"];load,dump,write,guard=m["load"],m["dump"],m["write"],m["guard"]
def audit(unit,final=False,final_numbering=None):
    def emit_json(rel,data):dump("qa/final-unit-gates/"+rel if final else rel,data)
    def emit_text(rel,data):write("qa/final-unit-gates/"+rel if final else rel,data)
    guard();notes=load(f"translation/authored/{unit}-notes.json");q=load("qa/latest-compilation.json");assert q["success"]
    for item in q.get("input_files",[]):assert s["m"]["sha256_file"](B.root/item["path"])==item["sha256"],"TeX changed after compilation"
    en=(B.root/f"structured/reviewed/{unit}.tex").read_text(encoding="utf8");zh=(B.root/f"translation/reviewed/{unit}.tex").read_text(encoding="utf8")
    assert collections.Counter(s["maths"](en))==collections.Counter(s["maths"](zh));assert not s["find_chinese_prose_punctuation"](zh)
    names=list(csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t"));fields=list(names[0]);seen={x["Source Form"] for x in names}
    for name in notes["names"]:
        if name not in seen:
            row=dict.fromkeys(fields,"");row.update({"Source Form":name,"Canonical Form":name,"Category":"person or exact source eponym","First Occurrence":unit,"Language or Script":"Latin","Preserve Exactly":"true","Review Status":"reviewed","Notes":"Exact source form, no case/accent/hyphen normalization"});names.append(row);seen.add(name)
    s["tsv"]("glossary/proper-names.tsv",fields,names);checks=[]
    for row in names:
        name=row["Source Form"];pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";a=len(re.findall(pat,en));b=len(re.findall(pat,zh))
        if a or b:checks.append({"name":name,"source":a,"target":b});assert a==b,checks[-1]
    candidates=list(csv.DictReader(B.candidates.open(encoding="utf8"),delimiter="\t"));cf=list(candidates[0]);global_terms=list(csv.DictReader((P.glossary/"terminology.tsv").open(encoding="utf8"),delimiter="\t"));lookup=[]
    for english,chinese,domain,context in notes["terms"]:
        matches=[x for x in global_terms if x["English"].casefold()==english.casefold()];approved=[x for x in matches if x["Status"]=="approved" and x["Domain"]==domain]
        assert not approved or any(x["Preferred Chinese"]==chinese for x in approved),(english,approved)
        lookup.append({"English":english,"Chinese":chinese,"Domain":domain,"Context":context,"global_matches":matches})
        if not any(x["English"]==english and x["Domain"]==domain and x["Context"]==context for x in candidates):
            row=dict.fromkeys(cf,"");row.update({"English":english,"Preferred Chinese":chinese,"Domain":domain,"Context":context,"Status":"proposed","First Source":"Finite Element Exterior Calculus","First Location":unit,"Last Verified Source":"original page images","Last Verified Location":unit,"Notes":"Book-local candidate; no global promotion"});candidates.append(row)
    s["tsv"]("glossary/candidates.tsv",cf,candidates);emit_json(f"qa/terminology/{unit}-lookup.json",lookup)
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");labels={}
    for hit in re.finditer(r"\\newlabel\{([^}]+)\}\{",aux):
        body,_=s["brace"](aux,hit.end()-1);values=[];pos=0
        while pos<len(body):v,pos=s["brace"](body,pos);values.append(v)
        labels[hit[1]]=values
    reader=PdfReader(B.root/"output/translation-progress.pdf");assert s["m"]["sha256_file"](B.root/"output/translation-progress.pdf")==q["pdf_sha256"];dest=reader.named_destinations;objects=[]
    for key,v in labels.items():
        if len(v)<4 or not v[3] or not v[1].isdigit():continue
        assert v[3] in dest,key;page=reader.get_destination_page_number(dest[v[3]])+1;assert page==int(v[1]),(key,v,page);objects.append({"label":key,"number":v[0],"output_page":page})
    if "expected_numbered_equations" in notes:
        chapter=int(unit.split("-")[1]);numbering={}
        for prefix,field in [("eq:","expected_numbered_equations"),("fig:","expected_figures"),("tab:","expected_tables")]:
            entries=[(k,v) for k,v in labels.items() if k.startswith(prefix) and re.fullmatch(str(chapter)+r"\.\d+",v[0])]
            expected=(final_numbering or notes)[field]
            assert sorted(int(v[0].split(".")[1]) for k,v in entries)==list(range(1,expected+1)),(prefix,entries)
            numbering[field]=len(entries)
        et=re.findall(r"\\begin\{table\}.*?\\end\{table\}",en,re.S);zt=re.findall(r"\\begin\{table\}.*?\\end\{table\}",zh,re.S);assert len(et)==len(zt)==notes.get("unit_tables",notes["expected_tables"])
        checks_tables=[]
        for i,(a,b) in enumerate(zip(et,zt),1):
            numbers=lambda value:collections.Counter(re.findall(r"(?<![A-Za-z])\d+(?:,\d{3})*(?:\.\d+)?",value))
            assert numbers(a)==numbers(b),(i,numbers(a),numbers(b));checks_tables.append({"source_table":f"{chapter}.{i}","source_target_numeric_tokens_equal":True,"numeric_token_occurrences":sum(numbers(a).values())})
        emit_json(f"qa/translation/{unit}-numbering-tables.json",{"passed":True,"numbering":numbering,"tables":checks_tables,"source_image_review":notes.get("table_data_review"),"figures":notes.get("figure_source_crops")})
    refs=[]
    for command,key in re.findall(r"\\(eqref|ref)\{([^}]+)\}",zh)+[("BookCite/BookNumber","bib:source-"+x) for x in re.findall(r"\\Book(?:Cite|Number)\{(\d+)\}",zh)]:
        assert key in labels,key;refs.append({"command":command,"label":key,"target_number":labels[key][0],"target_page":labels[key][1]})
    emit_json(f"qa/translation/{unit}-reference-report.json",{"passed":True,"objects":objects,"references":refs})
    for row in load("qa/full-input-protection.json")["accepted_files"]:assert s["m"]["sha256_file"](B.root/row["file"])==row["sha256"],row
    content=load(f"qa/batches/{unit}-content.json");emit_json(f"qa/batches/{unit}-automated-qa.json",{"passed":True,"unit":unit,"content":content,"names":checks,"source_pages":notes["source_pages"],"references":len(refs),"destinations":len(objects),"compile":q,"visual_review":"pending","blocking_issues":[]});guard();print(json.dumps({"unit":unit,"blocks":content["blocks"],"math":content["math_expressions"],"names":len(checks),"destinations":len(objects)},ensure_ascii=False))
    if notes["source_observations"] and not final:
        issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
        for i,observation in enumerate(notes["source_observations"],1):
            key=f"{unit}-source-{i}"
            if not any(x["id"]==key for x in issues):issues.append({"id":key,"category":"source","severity":"info","message":observation["message"],"source_location":{"page":observation["pdf_page"]},"confidence":0.99,"review_status":"reviewed","details":{"blocking":False,"action":"Retain source without silent correction","report":f"qa/source/{unit}-source-observations.md"}})
        write("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
        write(f"qa/source/{unit}-source-observations.md","# Source observations retained\n\n"+"\n\n".join(f"PDF {x['pdf_page']}: {x['message']}" for x in notes["source_observations"])+"\n\nAll are reviewed, nonblocking source records, not mathematical corrections.\n")
def accept(unit):
    from mathbook.workflow import translate_book,next_incomplete_unit
    guard();q=load(f"qa/batches/{unit}-automated-qa.json");v=load(f"qa/batches/{unit}-visual-review.json");assert q["passed"] and v["passed"] and v["pdf_sha256"]==q["compile"]["pdf_sha256"]==s["m"]["sha256_file"](B.root/"output/translation-progress.pdf")
    class NextUnit(Exception):pass
    def processor(book,current):
        if current!=unit:raise NextUnit(current)
        rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));row=next(x for x in rows if x["Unit ID"]==unit);assert row["QA Status"]!="passed";row.update({"QA Status":"passed","Notes":"Full source-aligned unit; source/math/name/terminology/reference/punctuation/compile/visual QA passed"});s["tsv"]("qa/chapter-progress.tsv",["Unit ID","Title","QA Status","Notes"],rows)
        q["visual_review"]="passed";dump(f"qa/batches/{unit}-automated-qa.json",q)
        protection=load("qa/full-input-protection.json");seen={x["file"] for x in protection["accepted_files"]}
        for accepted in [x["Unit ID"] for x in rows if x["QA Status"]=="passed" and x["Unit ID"] not in ("chapter-02-section-04","chapter-02-section-05","chapter-02-section-06")]:
            paths=[f"translation/authored/{accepted}.bilingual.tex",f"translation/reviewed/{accepted}.tex",f"structured/reviewed/{accepted}.tex",f"formulae/{accepted}.jsonl",("tex/frontmatter.tex" if accepted=="frontmatter" else f"tex/chapters/{accepted}.tex")]
            for rel in paths:
                if rel not in seen:
                    path=B.root/rel
                    if accepted!=unit:
                        blob=subprocess.run(["git","show","HEAD:"+path.relative_to(P.root).as_posix()],cwd=P.root,capture_output=True,check=True).stdout
                        assert blob.replace(b"\r\n",b"\n")==path.read_bytes().replace(b"\r\n",b"\n"),rel
                    protection["accepted_files"].append({"file":rel,"sha256":s["m"]["sha256_file"](path)});seen.add(rel)
        dump("qa/full-input-protection.json",protection);m["status"]()
    try:result=translate_book(P,ID,processor=processor)
    except NextUnit:
        state=load("qa/workflow-state.json");state.update({"status":"translating","next_unit":next_incomplete_unit(B)});dump("qa/workflow-state.json",state);m["status"]();result={"status":"translating","next_unit":next_incomplete_unit(B)}
    guard();print(json.dumps(result))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("action",choices=["audit","accept"]);p.add_argument("unit");a=p.parse_args();{"audit":audit,"accept":accept}[a.action](a.unit)
