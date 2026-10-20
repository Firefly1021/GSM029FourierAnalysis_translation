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
