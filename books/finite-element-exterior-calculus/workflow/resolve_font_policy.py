"""Record the user's non-Fraktur presentation decision without rewriting accepted text."""
import argparse,json,runpy
from pathlib import Path
from mathbook.workflow import project_record,update_project_record

m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]

def resolve():
    m["guard"]()
    key="accepted-sample-cycle-boundary-font-family"
    policy={"book_id":ID,"status":"user-approved","user_instruction":"不要,只要不是Fraktur 字体就行","scope":"This book's mathematical alphabet presentation, not source rewriting or permission to change mathematical objects","fraktur_in_translation":False,"accepted_sample_action":"Keep mathcal Z and mathcal B unchanged","mappings":[{"source_family":"EUFM10 / Fraktur","source_letters":["Z","B"],"display_family":"mathcal","status":"user-approved presentation exception"}],"collision_rule":"Never merge distinct source objects. Preserve original font metadata; if a new source alphabet would collide with an existing non-Fraktur symbol, choose and explicitly register a distinguishable non-Fraktur rendering before acceptance.","source_fidelity_claim":"Semantic identities and every other token remain unchanged; displayed font family is an explicit user exception, not a claim of original glyph identity.","evidence":"qa/formula/accepted-sample-font-followup.json"}
    m["dump"]("config/math-alphabet-policy.json",policy)
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()]
    issue=next(x for x in issues if x["id"]==key)
    issue["review_status"]="resolved"
    issue.pop("resolution",None)
    issue["details"].update({"blocking":False,"resolved_by":"explicit user presentation decision","resolution":"User rejected Fraktur and approved retaining the existing non-Fraktur Z/B. No accepted source or translation content was edited.","policy":"config/math-alphabet-policy.json"})
    m["write"]("qa/issues.jsonl","".join(json.dumps(x,ensure_ascii=False)+"\n" for x in issues))
    evidence=m["load"]("qa/formula/accepted-sample-font-followup.json")
    evidence.update({"passed":True,"blocking":False,"resolution":"User-approved non-Fraktur presentation exception; original font evidence retained","correction_authorized":False,"accepted_files_modified":False,"policy":"config/math-alphabet-policy.json","original_font_identity_preserved_in_display":False})
    m["dump"]("qa/formula/accepted-sample-font-followup.json",evidence)
    report=B.root/"qa/formula/accepted-sample-font-followup.md"
    old=report.read_text(encoding="utf8")
    if "## User decision superseding the historical blocker" not in old:
        m["write"](report.relative_to(B.root).as_posix(),old+"\n## User decision superseding the historical blocker\n\nThe user instructed: 不要,只要不是Fraktur 字体就行. Current status: resolved as a user-approved presentation exception, not corrected to source Fraktur. Keep the accepted mathcal Z/B, source reconstruction and PDF unchanged. Original EUFM10 evidence above remains true and permanently recorded. Do not claim original glyph-family identity. Preserve semantic distinctions if additional alphabets occur. See config/math-alphabet-policy.json.\n")
    qa=m["load"]("qa/sample-qa.json")
    qa.update({"status":"passed","formula":"passed","blocking_issues":[],"font_presentation_exception":"User-approved non-Fraktur Z/B; original font metadata retained","sample_user_approved":True})
    m["dump"]("qa/sample-qa.json",qa)
    remaining=[x["id"] for x in issues if x.get("severity")=="blocking" and x.get("review_status") not in ("resolved","rejected")]
    assert not remaining,remaining
    state=m["load"]("qa/workflow-state.json")
    state.update({"status":"translating","blocking_issues":[]})
    m["dump"]("qa/workflow-state.json",state)
    cfg=B.load_config();cfg.update({"status":"translating","phase":"translation"});m["dump"]("config/book.yaml",cfg)
    record=project_record(P,ID);record.phase="translation";record.status="translating";record.blocking_issues="";update_project_record(P,record)
    plan=(B.root/"PLANS.md").read_text(encoding="utf8")
    if "## Approved non-Fraktur presentation policy" not in plan:
        m["write"]("PLANS.md",plan+"\n## Approved non-Fraktur presentation policy\n\nThe user rejected the proposed Fraktur change: 不要,只要不是Fraktur 字体就行. This decision supersedes the historical blocker above. Preserve accepted mathcal Z/B and all accepted sample bytes; retain original font-family evidence and register the explicit presentation exception. Do not introduce Fraktur in translated mathematics. Preserve distinctions between different source objects with documented non-Fraktur mappings. Resume chapter-02-introduction without resetting progress. No push.\n")
    m["status"]();m["guard"]()
    m["dump"]("qa/formula/font-policy-resolution.json",{"passed":True,"issue":key,"resolution":"explicit user-approved presentation exception","accepted_files_unchanged":True,"source_template_hashes_unchanged":True,"progress_reset":False,"blocking_issues":remaining})
    print(json.dumps({"status":"translating","next_unit":state["next_unit"],"accepted_files_unchanged":True}))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.parse_args();resolve()
