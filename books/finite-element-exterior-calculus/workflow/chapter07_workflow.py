"""Stage only explicit, source-reviewed, unaccepted Chapter 7 natural units."""
import argparse,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-07-introduction":{"names":["Lipschitz","de Rham","Hodge","Laplace","Galerkin","Laplacian","Lagrange"],"terms":[["trimmed polynomial space","修剪多项式空间","finite element differential forms","intermediate polynomial differential-form space defined using the Koszul differential"],["shape function","形函数","finite elements","element-local functions spanning the shape space"]],"source_pages":[91,92],"source_observations":[{"pdf_page":91,"message":"The introduction prints the adjoint pair (delta, ring H* Lambda^k), whereas Theorem 6.5 has degree k+1 for the adjoint domain. Retain the source index k in this introductory sentence."},{"pdf_page":92,"message":"The notation paragraph says the spaces will be defined in the next section even though the chapter outline names Section 7.4. Preserve both source statements."}]},
"chapter-07-section-01":{"names":["de Rham","Koszul"],"terms":[["degree of freedom","自由度","finite elements","basis functional of the element-local dual shape space"],["finite element assembly","有限元组装","finite elements","matching shared face degrees of freedom between elements"]],"source_pages":[92,93],"source_observations":[]},
"chapter-07-section-02":{"names":["Koszul","Leibniz","Euler","Cartan","de Rham"],"terms":[["Koszul differential","Koszul 微分","polynomial differential forms","contraction with the identity vector field"],["homotopy formula","同伦公式","polynomial differential forms","relation between the exterior and Koszul differentials"],["homogeneous polynomial","齐次多项式","polynomial differential forms","polynomial with terms of one total degree"]],"source_pages":[93,94,95],"source_observations":[{"pdf_page":93,"message":"The identity-vector-field sentence prints 'is display'. Reconstructed English retains the source spelling; Chinese translates its meaning."}],"figure_source_crops":[{"label":"fig:identity-vector-field","pdf_page":94,"bbox_top_origin_pt":[150,62,368,281],"original_image_bbox":[151.097,63.543,367.097,279.543],"original_arrows_not_redrawn":True}]}}

NOTES.update({
"chapter-07-section-03":{"names":["Koszul","de Rham"],"terms":[["trimmed polynomial space","修剪多项式空间","finite element differential forms","intermediate polynomial differential-form space defined using the Koszul differential"]],"source_pages":[95,96],"source_observations":[{"pdf_page":96,"message":"The inclusion chain ends with P_r^- Lambda^k after P_{r-1} Lambda^{k+1}. Preserve the printed final degree k, rather than silently changing it to k+1."}]},
"chapter-07-section-04":{"names":["Koszul","Vandermonde","Stokes"],"terms":[["unisolvence","唯一可解性","finite elements","degrees of freedom uniquely determining an element of the shape space"],["barycentric coordinate","重心坐标","finite element geometry","affine coordinates relative to simplex vertices"]],"source_pages":[96,97,98],"source_observations":[]}
})

NOTES.update({
"chapter-07-section-05":{"names":["Bramble–Hilbert","Sobolev","Galerkin","de Rham"],"terms":[["mollifier","磨光算子","functional analysis","smoothing operator applied before finite element interpolation"]],"source_pages":[98,99,100],"source_observations":[{"pdf_page":99,"message":"The mixed complete/trimmed canonical commutation relation prints degree k on both Pi operators. Retain this printed degree, rather than replacing the left k by k-1."}],"table_data_review":"Table 7.1: four choices, four L2 rate columns, all polynomial degrees and r+1/r/r-1 entries checked against PDF 100."},
"chapter-07-section-06":{"names":["Whitney","Hassler Whitney","de Rham","De Rham"],"terms":[],"source_pages":[100,101],"source_observations":[{"pdf_page":100,"message":"Equation 7.11 prints degree 1 on its final Whitney space, not n. Preserve the printed degree 1."},{"pdf_page":101,"message":"The DOF paragraph prints 'uniquely determine an element of phi'. Preserve this wording in reconstructed English and its literal meaning in Chinese, without replacing phi by a space."}],"figure_source_crops":[{"label":"fig:whitney-form-dofs","pdf_page":101,"bbox_top_origin_pt":[112,62,401,139],"original_diagrams_not_redrawn":True}]}
})

NOTES.update({
"chapter-07-section-07":{"names":["de Rham","Cockburn","Qiu","Gillette","Kloefkorn","Arbogast"],"terms":[["serendipity family","Serendipity 族","finite element differential forms","cubical family with superlinear-degree-based shape space"],["tensor product","张量积","finite elements","product of interval polynomial spaces and chain complexes"]],"source_pages":[101,102,103],"source_observations":[{"pdf_page":102,"message":"The constant-degree comparison names the complete P_r Lambda^k sequence, not the trimmed sequence. Preserve the source comparison."},{"pdf_page":103,"message":"The serendipity DOF display uses u as the mapped argument, omega and mu in the integral, and q in the test-space membership. Preserve all four printed symbols without normalizing their names."}]},
"chapter-07-section-08":{"names":["Lagrange","Courant","Galerkin","Reed","Hill","Raviart","Thomas","Nédélec","Brezzi–Douglas–Marini","Whitney","Bossavit","Sullivan","Baker","Sullivan–Whitney","Hodge","Hiptmair","Arnold","Falk","Winther","Koszul","Raviart–Thomas","de Rham"],"terms":[],"source_pages":[103,104,105,106],"source_observations":[{"pdf_page":104,"message":"The source lists H(div) then H(curl), followed by P_r^- Lambda^1 then P_r^- Lambda^2 'respectively'. Retain this order without silently reversing either pair."},{"pdf_page":105,"message":"Box 7.1 starts 'Give an n-dimension ...'. Reconstructed English retains this wording; Chinese translates its meaning."},{"pdf_page":106,"message":"This is a blank production leaf with registration/color marks and an InDesign timestamp, not omitted mathematical content. Original PDF retained."}],"expected_numbered_equations":12,"expected_figures":2,"expected_tables":1,"unit_tables":0}
})

def prepare(units):
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for unit in units:
        assert next(x for x in rows if x["Unit ID"]==unit)["QA Status"]!="passed"
        rel=f"translation/authored/{unit}.bilingual.tex";text=(B.root/rel).read_text(encoding="utf8").replace("、",", ");m["write"](rel,text)
        en=m["s"]["language"](text,0);zh=m["s"]["language"](text,1)
        names={x["Source Form"] for x in csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t")}|{v for n in NOTES.values() for v in n["names"]}
        for name in names:
            pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";assert len(re.findall(pat,en))==len(re.findall(pat,zh)),(unit,name)
        assert not m["s"]["find_chinese_prose_punctuation"](zh)
        m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
    glyphs=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n in range(91,107):
            for ch in doc.pages[n-1].chars:
                if "EUFM" in ch["fontname"]:
                    assert ch["text"] in ("B","Z","H"),ch
                    glyphs.append({"pdf_page":n,"printed_page":str(n-10),"letter":ch["text"],"font":ch["fontname"],"bbox":[ch["x0"],ch["top"],ch["x1"],ch["bottom"]],"display_family":"mathsf" if ch["text"]=="H" else "mathcal"})
    m["dump"]("qa/formula/chapter-07-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","source_glyphs":glyphs,"glyph_family_identity_not_claimed":True})
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("units",nargs="+",choices=list(NOTES));a=p.parse_args();prepare(a.units)
