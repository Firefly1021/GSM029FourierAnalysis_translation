"""Guarded book-local final packaging, preserving approved terminology and inputs.

Uses existing ProjectPaths, BookPaths and registry functions. No promotion,
translation, shared-system edits or remote writes are performed here.
"""
import argparse,json,re,runpy,shutil,subprocess
from pathlib import Path
from pypdf import PdfReader

m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
B,P,ID=m["B"],m["P"],m["ID"]

def regression():
    m["guard"]();q=m["load"]("qa/latest-compilation.json")
    baseline=B.root/"workspace/temporary/full-batch-build-m_pcc8xd/main.pdf"
    assert m["sha256_file"](baseline)=="3319175e59d8eb22ea848342ea9ff7e2f1a7413338178586a7f0d51c3aedf77c"
    a=PdfReader(baseline);z=PdfReader(B.root/"output/translation-progress.pdf")
    normalize=lambda s:re.sub(r"\s+","",re.sub(r"\n\d+\s*$","",s))
    checks=[]
    for n in range(3,193):
        equal=normalize(a.pages[n-1].extract_text())==normalize(z.pages[n+2].extract_text())
        checks.append({"accepted_page":n,"final_page":n+3,"body_text_identical_ignoring_whitespace_and_page_footer":equal});assert equal,checks[-1]
    assert m["load"]("qa/translation/index-linked-copies.json")["accepted_source_text_unchanged"]
    m["dump"]("qa/final/accepted-output-regression.json",{"passed":True,"baseline_sha256":m["sha256_file"](baseline),"final_sha256":q["pdf_sha256"],"pages":checks,"scope":"190 accepted body/bibliography pages; final contents adds three pages; front banner change and index addition separately reviewed","pixel_identity_claimed":False,"prior_one_glyph_subpixel_variation_reviewed":True})
    print("190 accepted output pages preserve extracted body text at their final page offset")

def package():
    m["guard"]();a=m["load"]("qa/final/automated-qa.json");v=m["load"]("qa/final/visual-review.json");r=m["load"]("qa/final/accepted-output-regression.json")
    q=a["compile"];source=B.root/"output/translation-progress.pdf"
    assert a["passed"] and v["passed"] and r["passed"]
    assert m["sha256_file"](source)==q["pdf_sha256"]==v["pdf_sha256"]==r["final_sha256"]
    destination=B.assert_write_path(B.root/"output/book-zh.pdf")
    if destination.exists():assert m["sha256_file"](destination)==q["pdf_sha256"],"Refuse to replace a different final artifact"
    else:shutil.copyfile(source,destination)
    assert m["sha256_file"](destination)==q["pdf_sha256"]
    report=dict(a);report.update({"status":"completed","final_output":"output/book-zh.pdf","final_pdf_sha256":q["pdf_sha256"],"final_pdf_pages":q["pdf_pages"],"visual_review":"qa/final/visual-review.json","accepted_output_regression":"qa/final/accepted-output-regression.json","full_book_report":"qa/final/full-book-report.md"})
    m["dump"]("qa/final-report.json",report)
    cfg=B.load_config();cfg.update({"phase":"completed","status":"completed","final_output":"output/book-zh.pdf","last_batch_report":"qa/batches/index-report.md","final_qa_report":"qa/final/full-book-report.md"});m["dump"]("config/book.yaml",cfg)
    state=m["load"]("qa/workflow-state.json");assert len(state["completed_units"])==39 and not state["blocking_issues"] and state["next_unit"] is None
    state["status"]="completed";m["dump"]("qa/workflow-state.json",state)
    m["write"]("PROJECT_STATUS.md",f"Book ID: {ID}\nTitle: Krylov Subspace Methods for Linear Systems\nBranch: {m['R'].branch}\nWorktree: {P.root}\nPhase: completed\nStatus: completed\nSource SHA-256: {cfg['source']['sha256']}\nTemplate version: {cfg['template_version']}\nSample approved: Yes\nApproved terminology: grade -> 阶\nCompleted content: Preface, Acknowledgements, Chapters 1-5 in full, Software, all 212 References and all 179 Index entries\nPassed natural units: 39/39\nLast integrated batch: index\nFinal output: output/book-zh.pdf\nFinal PDF pages: {q['pdf_pages']}\nFinal PDF SHA-256: {q['pdf_sha256']}\nFinal QA: qa/final/full-book-report.md\nNext incomplete unit: None\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation complete: Yes\nSource observations: Retained in QA; no silent correction\nShared glossary: Unchanged; no terminology promotion performed\nRemote push: No\n")
    plans=(B.root/"PLANS.md").read_text(encoding="utf8")
    completion="## Full-book completion record"
    if completion not in plans:m["write"]("PLANS.md",plans.rstrip()+"\n\n"+completion+"\n\n- All 39 natural units passed; no next translation unit remains.\n- The accepted sample and all earlier accepted chapter text remain unchanged.\n- The final 201-page PDF, generated contents and concept-block index passed final integrity, numbering, destination, name, punctuation, compilation and visual gates.\n- Detailed evidence: qa/final/full-book-report.md and qa/final-report.json.\n- Source anomalies are retained in QA, not silently repaired.\n- Approved grade -> 阶 and the shared glossary are unchanged. No automatic terminology promotion or remote push is performed.\n")
    m["guard"]();print(json.dumps({"status":"completed","output":str(destination),"sha256":q["pdf_sha256"],"pages":q["pdf_pages"]}))

def register():
    """The normal completion registry integration, without candidate promotion."""
    from mathbook.workflow import main_worktree_project,project_record,update_project_record
    m["guard"]();assert m["load"]("qa/final-report.json")["status"]=="completed"
    assert not P.git_status().strip(),"Book worktree must be clean"
    main=main_worktree_project(P);assert main.git_branch()=="main" and not main.git_status().strip()
    def git(root,*args):return subprocess.run(["git",*args],cwd=root,check=True,capture_output=True,text=True,encoding="utf8").stdout
    git(P.root,"merge-base","--is-ancestor","main","HEAD")
    git(main.root,"merge","--ff-only","book/"+ID)
    before=main.projects_file.read_text(encoding="utf8");record=project_record(main,ID)
    record.title=B.load_config()["title"];record.phase="completed";record.status="completed";record.final_output=f"books/{ID}/output/book-zh.pdf";record.blocking_issues=""
    update_project_record(main,record)
    after=main.projects_file.read_text(encoding="utf8")
    other=lambda s:[line for line in s.splitlines() if not line.startswith("| "+ID+" |")]
    assert other(before)==other(after),"Other project rows must remain unchanged"
    git(main.root,"add","--","PROJECTS.md");git(main.root,"commit","-m","Record completion of "+ID)
    git(P.root,"merge","--ff-only","main")
    assert not P.git_status().strip() and not main.git_status().strip()
    assert P.git_head()==main.git_head()
    m["guard"]();print(json.dumps({"status":"completed","main_and_book_head":P.git_head(),"remote_push":False,"shared_glossary_promotion":False}))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("action",choices=["regression","package","register"]);args=p.parse_args()
    {"regression":regression,"package":package,"register":register}[args.action]()
