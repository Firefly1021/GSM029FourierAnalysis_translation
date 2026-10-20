"""Persist explicit performed visual review, then invoke existing natural-unit gates."""
import argparse,hashlib,json,runpy
from pathlib import Path
w=runpy.run_path(str(Path(__file__).with_name("batch_qa.py")))
P,B,ID=w["P"],w["B"],w["ID"]

def accept(a):
    w["guard"]();q=w["load"]("qa/latest-compilation.json");assert q["success"] and q["pdf_sha256"]==a.sha
    assert w["s"]["m"]["sha256_file"](B.root/"output/translation-progress.pdf")==a.sha
    old=B.root/"workspace/pages/progress-output"/a.previous_sha[:16];current=Path(q["render_directory"])
    identical=[]
    for n in range(1,a.unchanged_through+1):
        name=f"page-{n:02}.png";h=hashlib.sha256((old/name).read_bytes()).hexdigest();assert h==hashlib.sha256((current/name).read_bytes()).hexdigest(),n;identical.append({"page":n,"png_sha256":h})
    reviewed=list(range(a.unchanged_through+1,q["pdf_pages"]+1));assert reviewed==a.output_reviewed_pages,"Explicitly enumerate actually viewed new pages"
    source=set(a.source_reviewed_pages);blocks=math=0
    for unit in a.units:
        note=w["load"](f"translation/authored/{unit}-notes.json");assert set(note["source_pages"])<=source
        w["audit"](unit);content=w["load"](f"qa/batches/{unit}-content.json");blocks+=content["blocks"];math+=content["math_expressions"]
        w["dump"](f"qa/batches/{unit}-visual-review.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"source_pages_individually_reviewed":note["source_pages"],"output_pages_individually_reviewed":reviewed,"prior_visual_review_inherited_after_exact_png_equality":identical,"checks":["Complete selected natural unit compared against every listed original page image","Mathematical tokens and source hypotheses preserved, except explicit user-approved alphabet presentation","Original environment headings and personal names retained","Rendered pages show no clipping, overlap or missing glyph","Reference destination pages agree with labels","Untranslated targets remain clearly identified source locators, not fabricated translation"]})
    w["dump"](f"qa/batches/{a.report}-visual-regression.json",{"passed":True,"pdf_sha256":a.sha,"prior_build_sha256":a.previous_sha,"byte_identical_previously_reviewed_pages":identical,"new_pages_individually_reviewed":reviewed,"source_pages_individually_reviewed":a.source_reviewed_pages})
    w["write"](f"qa/batches/{a.report}-report.md",f"# {a.report} source-aligned batch acceptance\n\nStatus: passed. Units: {', '.join(a.units)}. All selected source content is retained, with {blocks} aligned blocks and {math} mathematical-expression occurrences. Original PDF pages individually compared: {', '.join(map(str,a.source_reviewed_pages))}.\n\nNew rendered output pages individually viewed: {', '.join(map(str,reviewed))}. Earlier pages 1-{a.unchanged_through} are byte-identical PNG renders to the previously reviewed build {a.previous_sha}. Current integrated PDF SHA-256: {a.sha}; {q['pdf_pages']} pages. This remains a progress PDF, not a completed book.\n\nSchemas, source-target math alignment, exact names, contextual terminology, ASCII punctuation, semantic references and actual PDF destination pages pass. Clean compilation uses at least two XeLaTeX rounds. Undefined references, duplicate labels, missing glyphs and overfull boxes: zero. User-approved non-Fraktur display mapping is documented; original font evidence is not discarded. Shared terminology is not overwritten or promoted.\n\nSource PDF, template manifest and earlier accepted translation hashes remain unchanged. No blocking issue. No remote push.\n")
    cfg=B.load_config();cfg["last_batch_report"]=f"qa/batches/{a.report}-report.md";w["dump"]("config/book.yaml",cfg)
    protection=w["load"]("qa/full-input-protection.json");seen={x["file"] for x in protection["accepted_files"]}
    for unit in a.units:
        note=w["load"](f"translation/authored/{unit}-notes.json");dependencies=[]
        if "figure_font_derivative" in note:dependencies.append(note["figure_font_derivative"]["derivative"])
        if "orthogonal_sum_symbol" in note:dependencies.append("tex/generated/orthogonal-sum-macro.tex")
        for rel in dependencies:
            path=B.assert_write_path(B.root/rel)
            if rel not in seen:protection["accepted_files"].append({"file":rel,"sha256":w["s"]["m"]["sha256_file"](path)});seen.add(rel)
    w["dump"]("qa/full-input-protection.json",protection)
    for unit in a.units:w["accept"](unit)
    w["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("--sha",required=True);p.add_argument("--previous-sha",required=True);p.add_argument("--unchanged-through",type=int,required=True);p.add_argument("--output-reviewed-pages",type=int,nargs="+",required=True);p.add_argument("--source-reviewed-pages",type=int,nargs="+",required=True);p.add_argument("--report",required=True);p.add_argument("--units",nargs="+",required=True);accept(p.parse_args())
