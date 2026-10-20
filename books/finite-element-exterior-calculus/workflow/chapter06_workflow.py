"""Guarded staging for independently source-reviewed Chapter 6 material only."""
import argparse,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-06-introduction":{"names":["Hilbert","de Rham","Riemannian","Hodge","Laplace"],"terms":[],"source_pages":[73],"source_observations":[]},
"chapter-06-section-01":{"names":["Grassman","Riesz","Hodge","Euclidean"],"terms":[["exterior algebra","外代数","differential forms","algebra of alternating multilinear forms"],["alternating multilinear form","交错多重线性形式","exterior algebra","multilinear form changing sign on interchange of variables"],["covector","余向量","linear algebra","element of a dual vector space"],["exterior product","外积","exterior algebra","alternating product of forms"],["contraction","缩并","exterior algebra","interior product with a vector"],["volume form","体积形式","exterior algebra","normalized top-degree alternating form on an oriented inner product space"],["Hodge star","Hodge 星算子","exterior algebra","metric and orientation dependent duality"],["vector proxy","向量代理","differential forms","vector representing a differential form through the established isomorphism"],["pullback","拉回","differential forms","contravariant map induced on forms"]],"source_pages":[73,74,75,76,77,78],"source_observations":[{"pdf_page":73,"message":"The source spells the personal name Grassman with one final n. Preserve that exact printed form, do not normalize it to Grassmann."},{"pdf_page":74,"message":"The alternating-form identity prints 1<=i<j<=n although its argument list ends at v_k. Preserve n as printed."},{"pdf_page":75,"message":"The determinant in the inner-product definition has index range i,j=1 to n although the forms are k-forms. Preserve n as printed."},{"pdf_page":76,"message":"The source writes the star on the first factor of the unparenthesized wedge expression and uses (-) without an explicit 1 in its sign powers. Preserve the printed expression, not a silently parenthesized or normalized replacement."}],"expected_numbered_equations":5,"expected_figures":0,"expected_tables":1,"table_data_review":"Original PDF 78 Table 6.1 independently read cell by cell, retaining contraction signs, all domain/codomain degrees, the transpose and adjugate pullbacks"}}

NOTES["chapter-06-section-02"]={"names":["Maxwell","Riemannian","Euclidean","Hodge","Möbius","Leibniz","de Rham","Lebesgue","Stokes","Piola","Sobolev","Hilbert","Lipschitz","Picard","Fredholm","Neumann","Dirichlet"],"terms":[["tangent bundle","切丛","differential geometry","pairs of points and tangent vectors"],["section","截面","differential geometry","assignment of one fibre element at every base point"],["codifferential","余微分","differential forms","formal adjoint delta defined through the Hodge star"],["Piola transform","Piola 变换","mixed finite elements","vector proxy of pullback on two-forms"],["orientation-preserving diffeomorphism","保定向微分同胚","differential geometry","diffeomorphism preserving the assigned orientation"]],"source_pages":list(range(78,91)),"source_observations":[{"pdf_page":80,"message":"The pullback paragraph introduces phi:M->N but says a differential k-form on Omega. Retain Omega in that source sentence and M in the following formula."},{"pdf_page":81,"message":"After the k=0 formula df, the source says the exterior derivative on a 1-form is the gradient. Retain its printed degree 1, not silently change it to 0."},{"pdf_page":82,"message":"The chart-definition paragraph prints d omega in Lambda^k(M), not Lambda^{k+1}(M). Retain k as printed."},{"pdf_page":82,"message":"The integration construction starts with k tangent vectors but the approximation display ends in v_n^(i). Retain n in that display."},{"pdf_page":86,"message":"The set called a half ball is explicitly printed with |x|=1, not |x|<=1. Preserve the equality and the source description."},{"pdf_page":86,"message":"The prose calls source object 3.11 Lemma, although its actual environment is Proposition. Preserve the English prefix Lemma in this sentence while linking to the true semantic target prop:trace-functional-representation."},{"pdf_page":87,"message":"The trace-extension derivation uses (-)^k, unlike (-)^{k+1} in the preceding integration-by-parts identity. Equation 6.17 additionally reverses the order of the two trace factors. Preserve every printed sign, exponent and factor order."},{"pdf_page":88,"message":"The source says u and du belong to the domain d*, without D(d*). Retain d* rather than inserting a repaired operator-domain expression."},{"pdf_page":89,"message":"Box 6.1 says a differential n-form satisfies the displayed Stokes formula integrating d omega. Retain its printed degree n and do not add a new hypothesis."},{"pdf_page":90,"message":"Source page is a blank production leaf containing only printer calibration/registration marks and an InDesign timestamp. No mathematical prose is omitted; the original page remains in the immutable PDF."}],"expected_numbered_equations":18,"expected_figures":1,"expected_tables":1,"table_data_review":"Previously accepted Table 6.1 remains unchanged; this section adds no table","figure_source_crops":[{"label":"fig:integration-parallelograms","pdf_page":83,"bbox_top_origin_pt":[102,62,434,217],"original_raster_bboxes":[[103.7660065,144.3169251,273.9035034,214.8999939],[261.0302429,144.3169251,431.1677398,214.8999939]],"includes_original_vector_diagram_and_labels":True}]}

NOTES["chapter-06-section-02"]["unit_tables"]=0

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
        for n in range(73,91):
            for ch in doc.pages[n-1].chars:
                if "EUFM" in ch["fontname"]:
                    assert ch["text"] in ("B","Z","H"),ch
                    glyphs.append({"pdf_page":n,"printed_page":str(n-10),"letter":ch["text"],"font":ch["fontname"],"bbox":[ch["x0"],ch["top"],ch["x1"],ch["bottom"]],"display_family":"mathsf" if ch["text"]=="H" else "mathcal"})
    m["dump"]("qa/formula/chapter-06-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","source_glyphs":glyphs,"glyph_family_identity_not_claimed":True})
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("units",nargs="+",choices=list(NOTES));a=p.parse_args();prepare(a.units)
