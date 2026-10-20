"""Book-only final integration and evidence gates; never bypass the natural-unit ledger."""
import argparse,collections,csv,hashlib,json,re,runpy,shutil,subprocess
from pathlib import Path
from pypdf import PdfReader
from PIL import Image
w=runpy.run_path(str(Path(__file__).with_name("batch_qa.py")))
m=w["m"];P,B,ID=w["P"],w["B"],w["ID"]

def prepare():
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));assert len(rows)==47 and all(x["QA Status"]=="passed" for x in rows)
    assert not m["load"]("qa/pending-reference-targets.json")
    m["dump"]("translation/authored/publication-notes.json",{"names":["Douglas N. Arnold","Arnold, Douglas N.","Kivmars H. Bowling","Paula Callaghan","Gina Rinelli Harris","Kelly Thomas","Lisa Briggeman","Susan Fleshman","Donna Witzleben","Cally A. Shrader","Cheryl Hufnagle","Doug Smock"],"terms":[],"source_pages":[1,2,3,4,5,6],"source_observations":[{"pdf_page":2,"message":"Blank leaf retained in original PDF, not missing prose."}],"catalogue_preservation":{"pages":[3,4],"method":"Unmodified clipped vector PDF source; no transcription or normalization of catalogue names and titles","crop_top_origin_pt":{"3":[60,60,475,705],"4":[60,98,475,705]},"bibliographic_titles_remain_in_original_language":True}})
    m["metadata"]("publication");m["assemble"](final=True);m["guard"]()

def index_coverage():
    records=m["load"]("structured/source/index-register.json");assert len(records)==178
    raw="\n".join((B.root/f"workspace/raw-text/full/pdf-{n}.txt").read_text(encoding="utf8") for n in (129,130))
    raw=raw.replace("grading, see vector space,\ngraded","grading, see vector space, graded").replace("Hille–Yosida–Phillips theory,\n101, 102","Hille–Yosida–Phillips theory, 101, 102").replace("integration of differential forms,\n72","integration of differential forms, 72")
    def norm(t):return re.sub(r"[^a-zA-Z0-9é–]+","",t.replace("ﬁ","fi").replace("ﬂ","fl").replace("’","'").replace("\x03","Lambda").replace("operatorname","")).lower()
    source=[];restored=[]
    for line in raw.splitlines():
        line=line.strip()
        if not line or line in ("Index","120 Index","119","120"):continue
        source.append(norm(re.sub(r",\s*\d+(?:,\s*\d+)*$","",line)))
    for row in records:
        value=row["english"]
        if row["targets"] and row["targets"][0].startswith("see:"):
            value+=", see "+row["targets"][0][4:].replace("/",", ").replace(" (DOF)","")
        restored.append(norm(value))
    assert len(source)==178 and collections.Counter(source)==collections.Counter(restored),(collections.Counter(source)-collections.Counter(restored),collections.Counter(restored)-collections.Counter(source))
    m["dump"]("qa/translation/index-source-coverage.json",{"passed":True,"source_entries":178,"translated_entries":178,"hierarchy_and_order_checked_against_original_images":[129,130],"mechanical_flat_entry_multiset_equal_after_documented_native_font_and_linewrap_handling":True,"original_printed_pages_retained":True,"translation_targets":"Actual containing section/object labels, not fabricated page equivalences"})

def audit():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["success"]
    main=B.main_tex.read_text(encoding="utf8");assert "中文翻译进度稿" not in main and "尚未翻译部分" not in main and not m["load"]("qa/pending-reference-targets.json")
    rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));assert len(rows)==47 and all(x["QA Status"]=="passed" for x in rows)
    checks=[]
    for row in rows:
        unit=row["Unit ID"]
        if unit in ("chapter-02-section-04","chapter-02-section-05","chapter-02-section-06"):continue
        override={"expected_numbered_equations":18,"expected_figures":1,"expected_tables":1} if unit.startswith("chapter-06-") else None
        w["audit"](unit,final=True,final_numbering=override);checks.append(m["load"](f"qa/batches/{unit}-content.json"))
    w["audit"]("publication",final=True);index_coverage()
    bib=m["load"]("structured/source/bibliography-entries.json");assert [x["number"] for x in bib]==list(range(1,72))
    aux=(Path(q["build_directory"])/"main.aux").read_text(encoding="utf8");eqs=re.findall(r"\\newlabel\{(eq:[^}]+)\}\{\{([^}]*)\}",aux)
    expected={1:6,2:4,3:12,4:33,5:21,6:18,7:12,8:26}
    for chapter,count in expected.items():assert sorted(int(v.split(".")[1]) for key,v in eqs if re.fullmatch(str(chapter)+r"\.\d+",v))==list(range(1,count+1)),chapter
    issues=[json.loads(x) for x in B.issues.read_text(encoding="utf8").splitlines() if x.strip()];blockers=[x for x in issues if x.get("details",{}).get("blocking") and x.get("review_status") not in ("resolved","reviewed","closed")];assert not blockers,blockers
    pages=set()
    for file in (B.root/"structured/source").glob("*-provenance.json"):
        for block in json.loads(file.read_text(encoding="utf8")):
            source_pages=block.get("source_pdf_pages",block.get("pdf_pages"));assert source_pages,file
            pages.update(source_pages)
    # The accepted representative sample's individual Sections 2.4-2.6 use its original provenance.
    pages.update((25,26,27,28));blanks={2,30,90,106,122,128};toc={7,8};assert set(range(1,131))<=pages|blanks|toc,sorted(set(range(1,131))-pages-blanks-toc)
    m["dump"]("qa/final-integration-automated.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"source_pages_accounted":130,"source_content_pages":sorted(pages-blanks-toc),"blank_or_production_leaves":sorted(blanks),"original_toc_pages_replaced_by_generated_translation_toc":sorted(toc),"passed_natural_units":47,"bibliography_entries":71,"index_entries":178,"numbered_equations":expected,"chapter_2_numbering_note":"Four equation numbers are established by the immutable user-approved sample; original displays are unnumbered.","content_blocks_excluding_accepted_sample":sum(x["blocks"] for x in checks),"math_occurrences_excluding_accepted_sample":sum(x["math_expressions"] for x in checks),"compile":q,"blocking_issues":[],"template_source_and_prior_accepted_hashes_unchanged":True,"source_observations_retained":len([x for x in issues if x.get("category")=="source"]),"visual_review":"pending","remote_push":False})
    m["guard"]();print("Final automated integration gates passed; visual acceptance remains pending")

def visual():
    """Record only pages actually viewed and exact inherited body renders, with a footer-only exclusion."""
    m["guard"]();q=m["load"]("qa/latest-compilation.json");assert q["pdf_sha256"]=="957802db5a638180f65af0c4937b193d88e0ce3d8b0e226031e21ab72fafca0a"
    previous="de1623ef05982eba6af666ffb94c05bfa28b91c500fef5107d20bbf6b279371d"
    old=B.root/"workspace/pages/progress-output"/previous[:16];current=Path(q["render_directory"])
    def body_hash(path):
        with Image.open(path) as im:
            return hashlib.sha256(im.crop((0,0,im.width,im.height-35)).tobytes()).hexdigest()
    prior=collections.defaultdict(list)
    for path in old.glob("page-*.png"):prior[body_hash(path)].append(int(path.stem.split("-")[-1]))
    matches=[];unmatched=[]
    for path in sorted(current.glob("page-*.png")):
        number=int(path.stem.split("-")[-1]);digest=body_hash(path)
        if digest in prior:matches.append({"final_page":number,"previous_pages":prior[digest],"body_pixel_sha256":digest})
        else:unmatched.append(number)
    viewed=[1,2,3,4,5,6,7,8,9,102];assert unmatched==viewed and len(matches)==103
    reader=PdfReader(B.root/"output/translation-progress.pdf");assert len(reader.pages)==113
    footer_checks=[];links=[]
    for number,page in enumerate(reader.pages,1):
        lines=(page.extract_text() or "").strip().splitlines();assert lines[-1]==str(number),(number,lines[-1]);footer_checks.append(number)
        for ref in page.get("/Annots",[]):
            annot=ref.get_object();action=annot.get("/A",{})
            if action.get("/S")=="/GoTo":
                target=action["/D"];assert isinstance(target,str) and target in reader.named_destinations,(number,target)
                landing=reader.get_destination_page_number(reader.named_destinations[target])+1;assert 1<=landing<=113
                links.append({"from_page":number,"destination":target,"target_page":landing})
    m["dump"]("qa/final-visual-review.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"pdf_pages":113,"individually_viewed_final_pages":viewed,"body_render_inheritance":matches,"inherited_render_baseline_sha256":previous,"inherited_review_report":"qa/batches/backmatter-complete-report.md","comparison_exclusion":"Only bottom 35 pixels at 100 dpi, containing the renumbered footer; all remaining pixels are identical.","footer_numbers_verified":footer_checks,"new_page_findings":"Publication catalogue clipping corrected with explicit PDF MediaBox. All source catalogue rows visible. Generated contents order and pagination checked. Preface reflow and Chapter 8 last page reviewed. No clipping, overlaps or missing glyphs observed.","review_scope":"Rendering regression and new-page inspection; source/math fidelity has separate per-unit original-image evidence, not inferred from compile success."})
    m["dump"]("qa/translation/final-pdf-link-audit.json",{"passed":True,"links_checked":len(links),"links":links,"semantic_label_number_page_agreement":"qa/final-unit-gates/qa/translation/*-reference-report.json"})
    print("Final visual and PDF link audit passed",len(matches),"inherited body renders;",len(links),"valid internal links")

def publish():
    m["guard"]();q=m["load"]("qa/latest-compilation.json");a=m["load"]("qa/final-integration-automated.json");v=m["load"]("qa/final-visual-review.json");t=m["load"]("qa/final-regression-tests.json")
    assert a["passed"] and v["passed"] and t["passed"] and a["pdf_sha256"]==v["pdf_sha256"]==q["pdf_sha256"]
    assert m["s"]["m"]["sha256_file"](B.root/"output/translation-progress.pdf")==q["pdf_sha256"]
    target=B.assert_write_path(B.root/"output/book-zh.pdf");assert not target.exists(),"Never replace a published final artifact implicitly"
    shutil.copyfile(B.root/"output/translation-progress.pdf",target);assert m["s"]["m"]["sha256_file"](target)==q["pdf_sha256"]
    terms=list(csv.DictReader(B.candidates.open(encoding="utf8"),delimiter="\t"));unresolved=list(csv.DictReader(B.unresolved.open(encoding="utf8"),delimiter="\t"))
    assert not unresolved and all(x["Status"]=="proposed" and "[safe-to-promote]" not in x["Notes"] for x in terms)
    a.update({"visual_review":"passed","regression_tests":t,"final_output":"output/book-zh.pdf","pdf_pages":113,"terminology_candidates":len(terms),"unresolved_terminology":0,"terminology_promotion":"Deferred: preserve book-local proposals and authoritative global library exactly; no promotion authorized.","font_policy":"User-approved non-Fraktur presentation; source font provenance retained; not a claim of original-font identity.","all_gates_passed":True})
    m["dump"]("qa/final-report.json",a)
    m["write"]("qa/final-report.md",f"# Finite Element Exterior Calculus final acceptance\n\nStatus: passed. All 47 natural units, Chapters 1-8, 71 bibliography entries and 178 hierarchical index entries are complete. The final translated PDF has 113 pages and SHA-256 `{q['pdf_sha256']}`.\n\nSource PDF pages 1-130 are accounted for by source-aligned content, retained bibliographic facsimiles, blank/production leaves and the regenerated translated contents. Blank leaves are not invented translated content.\n\nAll accepted translations and the approved sample remain byte-preserved. Source PDF and read-only template hashes match registration. English environment headings, exact names, documented non-Fraktur math alphabets, source-target math tokens, configured ASCII punctuation, schemas and semantic references pass their separate gates. Source-image checks are recorded in batch reports; compilation alone is not evidence of mathematical correctness. Known original-print anomalies are retained with reviewed QA observations, never silently repaired.\n\nClean XeLaTeX build has at least two rounds, zero undefined references, duplicate labels, missing glyphs or overfull boxes. 537 labels and 566 explicit references pass static checks. Actual PDF destinations and internal links pass. All 113 rendered pages are covered: 103 identical reviewed body renders (excluding only footer numbers) plus 10 individually inspected final pages. All final footer numbers are checked.\n\nRepository regression tests: 34/34 passed. The first reference-template test failed with an excessively deep external-runtime temporary path; the successful rerun retained book-local Python fixtures and the normal Windows TEMP for Biber. Original inputs were not modified. Both attempt records are retained.\n\nTerminology proposals remain book-local; no global promotion. No blocking issue and no unresolved terminology. No remote push. Final evidence: final-integration-automated.json, final-visual-review.json, final-regression-tests.json and translation/final-pdf-link-audit.json.\n")
    protection=m["load"]("qa/full-input-protection.json");seen={x["file"] for x in protection["accepted_files"]}
    for rel in ["translation/authored/publication.bilingual.tex","translation/reviewed/publication.tex","structured/reviewed/publication.tex","formulae/publication.jsonl","tex/chapters/publication.tex"]:
        if rel not in seen:protection["accepted_files"].append({"file":rel,"sha256":m["s"]["m"]["sha256_file"](B.root/rel)})
    m["dump"]("qa/full-input-protection.json",protection);m["guard"]();print("Published verified final PDF; lifecycle completion pending")

def complete():
    """Use existing identity/registry operations, without finish_book's unrequested shared-term mutation."""
    from mathbook.workflow import main_worktree_project,project_record,update_project_record,read_projects,verify_book_context,next_incomplete_unit
    m["guard"]();verify_book_context(P,ID,writable=True);assert next_incomplete_unit(B) is None
    report=m["load"]("qa/final-report.json");assert report["all_gates_passed"] and not report["blocking_issues"]
    assert m["s"]["m"]["sha256_file"](B.root/"output/book-zh.pdf")==report["pdf_sha256"]
    main_project=main_worktree_project(P);assert main_project.git_branch()=="main" and not main_project.git_status().strip()
    def git(root,args):return subprocess.run(["git",*args],cwd=root,capture_output=True,text=True,encoding="utf8",check=True).stdout.rstrip("\r\n")
    def branches():return dict(line.split(" ",1) for line in git(P.root,["for-each-ref","--format=%(refname) %(objectname)","refs/heads/"]).splitlines())
    before_refs=branches();before_remote=git(P.root,["remote","-v"]);global_hash=m["s"]["m"]["sha256_file"](P.glossary/"terminology.tsv")
    candidate_hash=m["s"]["m"]["sha256_file"](B.candidates)
    foreign_records={x.book_id:x.cells() for x in read_projects(main_project) if x.book_id!=ID}
    history_changes=git(P.root,["diff","--name-only","main","HEAD"]).splitlines()
    assert all(x=="PROJECTS.md" or x.startswith(f"books/{ID}/") for x in history_changes),history_changes
    status=git(P.root,["status","--porcelain=v1","--untracked-files=all"]).splitlines()
    assert all(x[3:].startswith(f"books/{ID}/") for x in status),status
    git(P.root,["merge-base","--is-ancestor","main","HEAD"])
    cfg=B.load_config();cfg.update({"phase":"completed","status":"completed","final_output":"output/book-zh.pdf"});m["dump"]("config/book.yaml",cfg)
    state=m["load"]("qa/workflow-state.json");state.update({"status":"completed","next_unit":None,"blocking_issues":[]});m["dump"]("qa/workflow-state.json",state)
    m["write"]("PROJECT_STATUS.md",f"Book ID: {ID}\nTitle: Finite Element Exterior Calculus\nBranch: {P.git_branch()}\nWorktree: {P.root}\nPhase: completed\nStatus: completed\nSource SHA-256: {cfg['source']['sha256']}\nPassed units: 47/47\nChapters completed: 1-8\nBibliography entries: 71\nIndex entries: 178\nNext incomplete unit: None\nBlocking issues: None\nUnresolved terminology: 0\nFull-book translation complete: Yes\nFinal output: output/book-zh.pdf\nFinal PDF pages: 113\nFinal PDF SHA-256: {report['pdf_sha256']}\nFinal QA: qa/final-report.json\nRemote push: No\n")
    plan=(B.root/"PLANS.md").read_text(encoding="utf8");assert "## Final completion" not in plan
    m["write"]("PLANS.md",plan+"\n## Final completion\n\nAll 47 natural units, the supplementary publication front matter, generated contents, eight chapters, bibliography and index are complete. Final whole-book source coverage, mathematical alignment, names, configured punctuation, real cross-references, clean compilation, rendered regression and 34 repository tests pass. See qa/final-report.md. Prior phase stops and font blockers above are historical, not current. No further translation unit remains. Keep terminology proposals book-local and the approved non-Fraktur mapping; do not auto-promote or push.\n")
    m["dump"]("qa/completion-receipt.json",{"book_id":ID,"status":"completed","final_pdf":"output/book-zh.pdf","pdf_sha256":report["pdf_sha256"],"pdf_pages":113,"passed_natural_units":47,"blocking_issues":[],"source_sha256":cfg["source"]["sha256"],"template_manifest_hash":cfg["template_manifest_hash"],"global_terminology_sha256":global_hash,"book_candidate_sha256":candidate_hash,"git_heads_before_completion":before_refs,"completion_policy":"Existing book-context, registry and fast-forward lifecycle operations; shared terminology promotion intentionally deferred. Shared code and other books remain unchanged.","remote_push":False})
    m["guard"]();git(P.root,["add","--",f"books/{ID}"]);git(P.root,["commit","-m",f"Complete translation and final acceptance of {ID}"])
    git(main_project.root,["merge","--ff-only",f"book/{ID}"])
    record=project_record(main_project,ID);record.phase="completed";record.status="completed";record.final_output=f"books/{ID}/output/book-zh.pdf";record.blocking_issues=""
    update_project_record(main_project,record)
    assert {x.book_id:x.cells() for x in read_projects(main_project) if x.book_id!=ID}==foreign_records
    git(main_project.root,["add","--","PROJECTS.md"]);git(main_project.root,["commit","-m",f"Record completion of {ID}"]);git(P.root,["merge","--ff-only","main"])
    after_refs=branches()
    assert {k:v for k,v in before_refs.items() if k not in ("refs/heads/main",f"refs/heads/book/{ID}")}=={k:v for k,v in after_refs.items() if k not in ("refs/heads/main",f"refs/heads/book/{ID}")}
    assert before_remote==git(P.root,["remote","-v"]) and global_hash==m["s"]["m"]["sha256_file"](P.glossary/"terminology.tsv") and candidate_hash==m["s"]["m"]["sha256_file"](B.candidates)
    assert not P.git_status().strip() and not main_project.git_status().strip() and P.git_head()==main_project.git_head()
    m["guard"]();print(json.dumps({"status":"completed","local_head":P.git_head(),"main_and_book_clean_and_equal":True,"other_book_branches_and_registry_rows_unchanged":True,"global_terminology_and_candidates_unchanged":True,"remote_push":False}))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("action",choices=["prepare","audit","visual","publish","complete"]);a=p.parse_args();{"prepare":prepare,"audit":audit,"visual":visual,"publish":publish,"complete":complete}[a.action]()
