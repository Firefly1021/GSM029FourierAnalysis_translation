"""Accept the actually inspected Chapter 3 build; preserve every earlier accepted byte."""
import argparse,hashlib,json,re,runpy
from pathlib import Path
w=runpy.run_path(str(Path(__file__).with_name("batch_qa.py")))
c=runpy.run_path(str(Path(__file__).with_name("chapter03_workflow.py")))
P,B,ID=w["P"],w["B"],w["ID"]

def accept():
    w["guard"]();q=w["load"]("qa/latest-compilation.json")
    assert q["pdf_sha256"]=="cb3919aec2636f7018b43a7df1d6b5210691217330147acef24be8a445949806"
    previous=B.root/"workspace/pages/progress-output/7a756b2de5a3c50f";current=Path(q["render_directory"])
    same=[]
    for n in range(1,19):
        name=f"page-{n:02}.png";a=hashlib.sha256((previous/name).read_bytes()).hexdigest();b=hashlib.sha256((current/name).read_bytes()).hexdigest();assert a==b,(n,a,b);same.append({"page":n,"png_sha256":a})
    w["dump"]("qa/batches/chapter-03-visual-regression.json",{"passed":True,"earlier_reviewed_render_directory":str(previous),"new_render_directory":str(current),"byte_identical_previously_reviewed_pages":same,"new_output_pages_individually_reviewed":list(range(19,33))})
    en="\n".join((B.root/f"structured/reviewed/{u}.tex").read_text(encoding="utf8") for u in c["UNITS"])
    assert len(re.findall(r"\\begin\{(?:Theorem|Proposition|Lemma)\}",en))==18
    assert len(re.findall(r"\\begin\{Proof\}",en))==12
    assert len(re.findall(r"\\begin\{equation\}",en))==12
    assert en.count(r"\footnote{")==1
    ref=w["load"]("qa/translation/chapter-03-section-04-reference-report.json")
    eqs=[x for x in ref["objects"] if x["label"].startswith("eq:") and re.fullmatch(r"3\.\d+",x["number"])]
    statements=[x for x in ref["objects"] if x["label"].startswith(("thm:","prop:","lem:")) and re.fullmatch(r"3\.\d+",x["number"])]
    assert sorted(int(x["number"].split(".")[1]) for x in eqs)==list(range(1,13))
    assert sorted(int(x["number"].split(".")[1]) for x in statements)==list(range(1,19))
    w["dump"]("qa/translation/chapter-03-numbering.json",{"passed":True,"numbered_equations":eqs,"statements":statements,"proof_environments":12,"footnotes":1,"box":"box:unbounded-operators-summary"})
    for unit in c["UNITS"]:
        a=w["load"](f"qa/batches/{unit}-automated-qa.json");assert a["passed"] and a["compile"]["pdf_sha256"]==q["pdf_sha256"]
        w["dump"](f"qa/batches/{unit}-visual-review.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"source_pages_individually_reviewed":c["NOTES"][unit]["source_pages"],"output_pages_individually_reviewed":list(range(19,33)),"earlier_pages_review_inherited_only_after_exact_png_hash_comparison":list(range(1,19)),"checks":["Complete source paragraphs, assumptions, conclusions, all twelve proofs, footnote and Box 3.1 retained","Closed-graph bars, adjoint stars, operator domains, integrals, normals and tangential cross products checked against original images","All eighteen statement labels and twelve equation labels retain source numbering","All 99 PDF destination pages agree with their aux label pages","Local Needspace before new theorem-like blocks prevents anchors from remaining on a preceding page; original template untouched","No clipping, overlap or missing glyph observed; Box 3.1 splits correctly across pages","No Fraktur introduced"],"scope":"Source fidelity, numbering, links and layout, not an independent proof audit"})
    cfg=B.load_config();cfg["last_batch_report"]="qa/batches/chapter-03-report.md";w["dump"]("config/book.yaml",cfg)
    w["write"]("qa/batches/chapter-03-report.md","# Complete Chapter 3 acceptance\n\nStatus: passed. All original PDF 31-42 / printed 21-32 is covered, including Sections 3.1-3.4, every proof, the graph-norm footnote and Box 3.1. The five natural units contain 97 aligned blocks and 604 math occurrences. There are twelve numbered equations 3.1-3.12, eighteen statement objects 3.1-3.18 and twelve Proof environments. No source content is summarized or omitted.\n\nOriginal page images were individually inspected. Mathematical tokens match reconstructed English and Chinese; graph closure bars, adjoint stars, norm powers, domains, traces, negative exponents, normals, signs and integrals were compared to the source. English environment headings, exact names, contextual terminology lookup, ASCII prose punctuation and schemas pass. Terms remain proposed locally. Source T(D), the R^3/n dimensional wording and Lemma 3.10's normed-space assumptions remain as printed, with explicit source QA records.\n\nAn actual cross-page anchor mismatch was detected before acceptance. Local Needspace guards in only these new translation files now keep refstepcounter anchors on the visible statement pages; no original or shared template was edited. All 99 label destination pages now agree. Twelve equation numbers and eighteen theorem-like numbers exactly match the original sequence.\n\nA clean build completes at least two XeLaTeX rounds, with zero undefined references, duplicate labels, missing glyphs and overfull boxes. Latest integrated PDF: 32 pages; SHA-256 "+q["pdf_sha256"]+". New output pages 19-32 were individually viewed. Earlier output pages 1-18 are byte-identical PNG renders to the previously individually reviewed accepted build. The first 29 output pages contain translation; the final three are explicitly marked verified source locators for unfinished targets. Box 3.1's original float is placed after the section text and breaks across output pages 28-29 without lost text.\n\nSource PDF, raw template manifest and every earlier accepted file hash remain unchanged. No Fraktur was introduced. No blocking issue. Next unit: chapter-04-introduction. Full-book translation continues; not complete. No remote push.\n")
    for unit in c["UNITS"]:w["accept"](unit)
    w["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.parse_args();accept()
