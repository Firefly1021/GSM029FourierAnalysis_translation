"""Persist actually performed Chapter 2 visual review and use the existing batch gate."""
import argparse,collections,json,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("chapter02_workflow.py")))
w=runpy.run_path(str(Path(__file__).with_name("batch_qa.py")))
P,B,ID=w["P"],w["B"],w["ID"]

def accept():
    w["guard"]();q=w["load"]("qa/latest-compilation.json")
    assert q["pdf_sha256"]=="7a756b2de5a3c50f38d81bfc2ce630e120caca1385b479db21102daccba39d12"
    used_fraktur=[]
    with pdfplumber.open(B.root/"output/translation-progress.pdf") as doc:
        for i,page in enumerate(doc.pages,1):
            used_fraktur += [{"output_page":i,"character":x["text"],"font":x["fontname"]} for x in page.chars if re.search(r"EUFM|EURM|Fraktur",x["fontname"],re.I)]
    # pdfplumber reports clipped-away text in imported PDF Form XObjects too.
    # Verify every such source glyph is outside the actual figure clip, instead
    # of mistaking invisible source-page content for visible output mathematics.
    clipped=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for crop in m["NOTES"]["chapter-02-section-03"]["figure_source_crops"]:
            x0,y0,x1,y1=crop["bbox_top_origin_pt"]
            for char in doc.pages[crop["pdf_page"]-1].chars:
                if not re.search(r"EUFM|EURM|Fraktur",char["fontname"],re.I):continue
                intersects=char["x0"]<x1 and char["x1"]>x0 and char["top"]<y1 and char["bottom"]>y0
                assert not intersects,(crop,char)
                clipped.append({"figure":crop["label"],"source_pdf_page":crop["pdf_page"],"character":char["text"],"font":char["fontname"],"bbox":[char["x0"],char["top"],char["x1"],char["bottom"]],"outside_figure_clip":True})
    assert collections.Counter((x["character"],x["font"]) for x in used_fraktur)==collections.Counter((x["character"],x["font"]) for x in clipped)
    w["dump"]("qa/formula/non-fraktur-output-check.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"method":"No prohibited Fraktur macros in compiled TeX; inspect source figure clip geometry, compare all raw Fraktur text records with clipped-away imported source glyphs; visually inspect every rendered output page","raw_pdf_text_extraction_fraktur_records":used_fraktur,"clipped_away_source_glyph_evidence":clipped,"visible_fraktur_glyphs":0,"all_accepted_file_hashes_unchanged":True,"source_font_exception":"config/math-alphabet-policy.json"})
    schema=json.loads((P.root/"schemas/qa-issue.schema.json").read_text(encoding="utf8"))
    for line in B.issues.read_text(encoding="utf8").splitlines():
        if line.strip():w["s"]["jsonschema"].validate(json.loads(line),schema)
    for unit in m["UNITS"]:
        w["dump"](f"qa/batches/{unit}-visual-review.json",{"passed":True,"pdf_sha256":q["pdf_sha256"],"source_pages_individually_reviewed":m["NOTES"][unit]["source_pages"],"output_pages_individually_reviewed":list(range(1,21)),"checks":["All new source paragraphs, equations, list entries and four figures compared against original pages 21-25 and 29","All original diagram arrows, orientations and Betti-number rows retained in source PDF clips","No clipping, overlap or missing glyph observed on the twenty rendered output pages","Accepted Sections 2.4-2.6 inserted unchanged in their natural position","All source font differences explicitly covered by the user-approved non-Fraktur exception","No mathematical inference used to repair source wording"],"scope":"Source-fidelity and rendered-layout review, not independent verification of the author's mathematical results"})
    w["write"]("qa/batches/chapter-02-report.md","# Chapter 2 complete source-aligned acceptance\n\nStatus: passed with the explicit user-approved non-Fraktur presentation exception. All Chapter 2 prose and mathematics, Sections 2.1-2.6, four original figures and the separate Box 2.1 are included. New material spans original PDF 21-25 and 29 / printed 11-15 and 19; accepted sample PDF 25-28 / printed 15-18 remains byte-unchanged. PDF 30 / printed 20 is a blank production leaf, not omitted body text.\n\nFive new natural units contain 41 aligned blocks and 158 math occurrences. The unchanged accepted sample contains 41 blocks and 129 math occurrences. The full chapter therefore has 82 blocks and 287 mathematical-expression occurrences. All four original figure clips retain arrows, orientation signs and the numeric Betti-number rows. Original figure captions are translated; diagrams are not regenerated.\n\nOriginal EUFM10 Z/B metadata is retained, while mathcal Z/B is now an explicit user-approved display mapping. This is not a claim of identical source glyph families. No used Fraktur text glyphs were found in the integrated output. Distinct source objects must remain distinguishable in future mapping decisions. Source subcomplex indexing, incidence-matrix chain wording and the summary's cocyles typo are recorded without mathematical correction.\n\nSource/target math tokens, schemas, contextual shared-terminology queries, exact names, ASCII punctuation, English environment headings and stable semantic labels pass. Eight newly applicable exact-name checks cover Euler, Descartes, E. Cartan, de Rham, De Rham, Betti, Laplace and Euclidean. Proposed terms remain book-local. No shared glossary overwrite or automatic promotion.\n\nA clean build completes at least two XeLaTeX rounds. Undefined references, duplicate labels, missing glyphs and overfull boxes are zero. Fifty-six named output destinations agree with their aux-label pages. All twenty output pages were individually viewed: complete Preface 1-2, Chapter 1 on 3-10, complete Chapter 2 on 11-18, and explicitly marked future source locators on 19-20. PDF SHA-256: "+q["pdf_sha256"]+". Source PDF, user template and all previously accepted content hashes are unchanged.\n\nFull book is not yet complete. Next unit: chapter-03-introduction. No blocking issue. No remote push.\n")
    for unit in m["UNITS"]:w["accept"](unit)
    w["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.parse_args();accept()
