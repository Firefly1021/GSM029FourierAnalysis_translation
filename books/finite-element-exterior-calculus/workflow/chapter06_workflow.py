"""Guarded staging for independently source-reviewed Chapter 6 material only."""
import argparse,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-06-introduction":{"names":["Hilbert","de Rham","Riemannian","Hodge","Laplace"],"terms":[],"source_pages":[73],"source_observations":[]},
"chapter-06-section-01":{"names":["Grassman","Riesz","Hodge","Euclidean"],"terms":[["exterior algebra","外代数","differential forms","algebra of alternating multilinear forms"],["alternating multilinear form","交错多重线性形式","exterior algebra","multilinear form changing sign on interchange of variables"],["covector","余向量","linear algebra","element of a dual vector space"],["exterior product","外积","exterior algebra","alternating product of forms"],["contraction","缩并","exterior algebra","interior product with a vector"],["volume form","体积形式","exterior algebra","normalized top-degree alternating form on an oriented inner product space"],["Hodge star","Hodge 星算子","exterior algebra","metric and orientation dependent duality"],["vector proxy","向量代理","differential forms","vector representing a differential form through the established isomorphism"],["pullback","拉回","differential forms","contravariant map induced on forms"]],"source_pages":[73,74,75,76,77,78],"source_observations":[{"pdf_page":73,"message":"The source spells the personal name Grassman with one final n. Preserve that exact printed form, do not normalize it to Grassmann."},{"pdf_page":74,"message":"The alternating-form identity prints 1<=i<j<=n although its argument list ends at v_k. Preserve n as printed."},{"pdf_page":75,"message":"The determinant in the inner-product definition has index range i,j=1 to n although the forms are k-forms. Preserve n as printed."},{"pdf_page":76,"message":"The source writes the star on the first factor of the unparenthesized wedge expression and uses (-) without an explicit 1 in its sign powers. Preserve the printed expression, not a silently parenthesized or normalized replacement."}],"expected_numbered_equations":5,"expected_figures":0,"expected_tables":1,"table_data_review":"Original PDF 78 Table 6.1 independently read cell by cell, retaining contraction signs, all domain/codomain degrees, the transpose and adjugate pullbacks"}}

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
