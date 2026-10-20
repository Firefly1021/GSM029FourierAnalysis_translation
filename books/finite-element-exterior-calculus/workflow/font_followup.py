"""Record a verified font-family defect without modifying accepted content."""
import json,re,runpy,subprocess
from pathlib import Path
import pdfplumber
from mathbook.workflow import resume_book,project_record,update_project_record
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));P,B,ID=m["P"],m["B"],m["ID"]
def record():
    m["guard"]();evidence=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n in (25,26):
            for c in doc.pages[n-1].chars:
                if "EUFM10" in c["fontname"] and c["text"] in ("Z","B"):
                    evidence.append({"pdf_page":n,"printed_page":str(n-10),"source_character":c["text"],"embedded_font":c["fontname"],"bbox":[c["x0"],c["top"],c["x1"],c["bottom"]]})
    assert len(evidence)==3,evidence
    affected=[x for x in [json.loads(line) for line in (B.root/"formulae/sample.jsonl").read_text(encoding="utf8").splitlines()] if re.search(r"\\mathcal\s*[ZB]",x["source_latex"])]
    assert len(affected)==3,affected
    ams=Path(subprocess.run(["kpsewhich","amsfonts.sty"],capture_output=True,text=True,check=True).stdout.strip());definition=ams.read_text(encoding="utf8")
    assert r"\DeclareMathAlphabet{\mathfrak}{U}{euf}{m}{n}" in definition
    m["dump"]("qa/formula/accepted-sample-font-followup.json",{"passed":False,"blocking":True,"defect_origin":"agent source reconstruction, not an original-book error","source_glyphs":evidence,"affected_accepted_formula_ids":[x["id"] for x in affected],"affected_reconstructed_expressions":[x["source_latex"] for x in affected],"source_family":"EUFM10 / Euler Fraktur","currently_authored_family":"mathcal","proposed_source_faithful_family":"mathfrak","local_primary_definition":{"file":str(ams),"declaration":r"\DeclareMathAlphabet{\mathfrak}{U}{euf}{m}{n}"},"accepted_files_modified":False,"correction_authorized":False,"unchanged_other_alphabets":"Do not change mathcal H or mathcal S; this evidence concerns only Z and B","previous_token_check_limitation":"Both reconstructed English and Chinese contained the same transcription error, so source-target token equality did not detect the wrong source font family."})
    issue={"id":"accepted-sample-cycle-boundary-font-family","category":"formula","severity":"blocking","message":"Three accepted sample symbols use mathcal Z/B, but original PDF 25-26 embeds EUFM10 Fraktur Z/B. Accepted text must not be corrected without explicit user authorization.","source_location":{"page":25},"confidence":1.0,"review_status":"needs-review","details":{"blocking":True,"origin":"agent source reconstruction","report":"qa/formula/accepted-sample-font-followup.md","affected_formula_ids":[x["id"] for x in affected],"authorization_needed":"Correct only the three logical Z/B expressions from mathcal to mathfrak in the accepted source/translation/registry and regenerate verified output; do not change H or other content."}}
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    if not any(x["id"]==issue["id"] for x in issues):issues.append(issue)
    m["write"]("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    result=resume_book(P,ID);assert result["status"]=="blocked" and result.get("processed",[])==[],result
    # The shared controller returns blocked but leaves its in-memory status as
    # translating on this early-return path. Persist truthful book-local state.
    state=m["load"]("qa/workflow-state.json");state["status"]="blocked";state["blocking_issues"]=[issue["id"]];m["dump"]("qa/workflow-state.json",state)
    qa=m["load"]("qa/sample-qa.json");qa.update({"status":"needs-review","formula":"needs-review","blocking_issues":[issue["id"]],"historical_technical_qa":"Previously passed; superseded for these three source symbols by the font-family follow-up","sample_user_approved":True});m["dump"]("qa/sample-qa.json",qa)
    cfg=B.load_config();cfg["status"]="blocked";m["dump"]("config/book.yaml",cfg)
    rec=project_record(P,ID);rec.phase="translation";rec.status="blocked";rec.blocking_issues=issue["id"];update_project_record(P,rec)
    m["write"]("PROJECT_STATUS.md",f"Book ID: {ID}\nTitle: Finite Element Exterior Calculus\nBranch: {P.git_branch()}\nWorktree: {P.root}\nPhase: translation\nStatus: blocked\nSample user approved: Yes, before the newly discovered defect\nCompleted new units: Complete Preface and Chapter 1 (PDF 9-20)\nAccepted sample text: Unchanged\nNext incomplete unit: chapter-02-introduction\nBlocking issues: {issue['id']}\nRequired user decision: Authorize the narrowly scoped correction of three Z/B font-family expressions in the accepted sample\nProgress inventory: Preserved, not reset\nFull-book translation complete: No\nSource and user templates: Hashes unchanged\nRemote push: No\n")
    m["guard"]();print(json.dumps(result,ensure_ascii=False))
if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);a=p.parse_args();record()
