"""Stage explicitly authored, unaccepted Chapter 5 units with book-local provenance."""
import argparse,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-05-introduction":{"names":["Hilbert","Hodge","Laplacian","Laplace","Galerkin","de Rham"],"terms":[["consistency","相容性","Galerkin methods","compatibility of the discrete equations with the continuous solution"]],"source_pages":[61],"source_observations":[{"pdf_page":61,"message":"The introduction prints occuring; retain the original English spelling and translate its meaning without new content."}]},
"chapter-05-section-01":{"names":["Hodge","Laplacian","Galerkin","Sobolev","de Rham","Neumann","Poisson"],"terms":[["reentrant corner","凹角","elliptic regularity","nonconvex corner causing singularities"],["codimension","余维","functional analysis","dimension of a quotient space"],["trial function","试探函数","Galerkin methods","function sought in the trial space"],["test function","检验函数","Galerkin methods","function testing the variational equation"]],"source_pages":[61,62,63,64],"source_observations":[{"pdf_page":63,"message":"The source prints 'the any nonzero harmonic forms'. Preserve the reconstructed English literally; Chinese conveys the statement without added assumptions."}],"figure_source_crops":[{"label":"fig:primal-lagrange-failure","pdf_page":63,"bbox_top_origin_pt":[95,62,429,204],"original_image_bboxes":[[96.27,63.54,260.61,202.50],[260.61,63.54,427.36,202.50]],"plot_and_color_scale_unchanged":True},{"label":"fig:primal-harmonic-failure","pdf_page":64,"bbox_top_origin_pt":[96,62,423,198],"original_image_bboxes":[[97.10,63.54,259.10,196.78],[259.10,63.54,421.10,196.78]],"plot_and_color_scale_unchanged":True}]}}

NOTES["chapter-05-section-02"]={"names":["Galerkin","Hodge","Laplace","Laplacian","Hilbert","Poincaré","Pythagorean","de Rham","Poisson","Aubin–Nitsche"],"terms":[["nonconforming method","非协调方法","Galerkin methods","discrete harmonic spaces need not lie in continuous harmonic spaces"],["bounded cochain projection","有界上链投影","Hilbert complexes","bounded linear projections commuting with the differentials"],["quasi-optimal approximation","拟最优逼近","Galerkin methods","projection error bounded by best approximation up to a constant"],["gap","间隙","closed subspaces","symmetric distance between two closed Hilbert subspaces"]],"source_pages":list(range(64,73)),"source_observations":[{"pdf_page":66,"message":"The W-to-V boundedness display prints c||v||^2+||dv||^2=c||v||_V^2, without c multiplying the derivative term. Preserve the printed factors."},{"pdf_page":66,"message":"The source names the harmonic space H_h^k while the surrounding paragraph uses index j. Retain the displayed index k, not silently normalize it."},{"pdf_page":67,"message":"The text calls these homology spaces, not cohomology spaces, after Theorem 5.1. Preserve the wording, as in the source."},{"pdf_page":69,"message":"Theorem 5.3 and the final proof line use ||dv||_V while the first use of continuous Poincare in the proof uses ||dv||. Keep all subscripts exactly as printed."},{"pdf_page":70,"message":"Equation 5.16 has a final unmatched right parenthesis after the V norm. The 400-dpi source crop confirms it; retain it without inventing an opening parenthesis."},{"pdf_page":72,"message":"Equation 5.21 ends in an extra square closing bracket before the final parenthesis. Confirmed in a 400-dpi source crop, retained without silent mathematical correction."}],"expected_numbered_equations":21,"expected_figures":2,"expected_tables":0,"orthogonal_sum_symbol":"Reuse accepted U+29B9 BookOrthSum under the non-Fraktur presentation policy","logical_float_placement":"Box 5.1 is retained in full after the section, rather than inside the interrupted paragraph before Theorem 5.6","verified_source_detail_crops":["workspace/pages/source-crops/ch5-mu-proof.png","workspace/pages/source-crops/ch5-improved-estimates.png"]}

def prepare(units):
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for unit in units:
        assert next(x for x in rows if x["Unit ID"]==unit)["QA Status"]!="passed"
        rel=f"translation/authored/{unit}.bilingual.tex";text=(B.root/rel).read_text(encoding="utf8").replace("、",", ")
        if unit=="chapter-05-section-02":
            # Mechanical block relocation: keep the entire source sequence, not a rewritten proof.
            first=text.index("% block: mixed-basic-error-introduction")
            proof=text.index("% block: discrete-cohomology-isomorphism-proof")
            if first<proof:text=text[:first]+text[proof:]+"\n"+text[first:proof]
            text=text.replace("thm:hilbert-poincare}","thm:hilbert-complex-poincare}")
        m["write"](rel,text)
        en=m["s"]["language"](text,0);zh=m["s"]["language"](text,1)
        names={x["Source Form"] for x in csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t")}|{v for n in NOTES.values() for v in n["names"]}
        for name in names:
            pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";assert len(re.findall(pat,en))==len(re.findall(pat,zh)),(unit,name)
        assert not m["s"]["find_chinese_prose_punctuation"](zh)
        m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
    glyphs=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n in range(61,73):
            for ch in doc.pages[n-1].chars:
                if "EUFM" in ch["fontname"]:
                    assert ch["text"] in ("B","Z","H"),ch
                    glyphs.append({"pdf_page":n,"printed_page":str(n-10),"letter":ch["text"],"font":ch["fontname"],"bbox":[ch["x0"],ch["top"],ch["x1"],ch["bottom"]],"display_family":"mathsf" if ch["text"]=="H" else "mathcal"})
    m["dump"]("qa/formula/chapter-05-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","source_glyphs":glyphs,"glyph_family_identity_not_claimed":True})
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("units",nargs="+",choices=list(NOTES));a=p.parse_args();prepare(a.units)
