"""Prepare only unfinished Chapter 2 units; no accepted text is regenerated."""
import argparse,csv,json,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
UNITS=["chapter-02-introduction","chapter-02-section-01","chapter-02-section-02","chapter-02-section-03","chapter-02-summary"]
NOTES={
UNITS[0]:{"names":["Betti","Euler","Descartes","E. Cartan","de Rham"],"terms":[["topological invariant","拓扑不变量","homological algebra","invariants obtained by counting discrete structures"]],"source_pages":[21],"source_observations":[]},
UNITS[1]:{"names":["Laplace"],"terms":[["graded vector space","分次向量空间","homological algebra","direct sum indexed by integers"],["graded map of degree p","次数为 p 的分次映射","homological algebra","f maps V_k into W_(k+p)"],["subcomplex","子复形","homological algebra","graded subspace preserved by the differential"]],"source_pages":[21,22],"source_observations":[{"pdf_page":22,"message":"Source denotes the subcomplex itself by (S_k, partial_k restricted to S_k). Retain its indexing exactly rather than silently replacing it by a graded-space pair."}]},
UNITS[2]:{"names":[],"terms":[["cycle","闭链","homological algebra","kernel of a chain boundary operator; accepted sample baseline"],["boundary","边界链","homological algebra","range of the next chain boundary operator; accepted sample baseline"],["exact complex","正合复形","homological algebra","all homology spaces vanish"]],"source_pages":[22],"source_observations":[]},
UNITS[3]:{"names":["Euclidean","Betti"],"terms":[["simplicial complex","单纯复形","algebraic topology","finite face-closed collection with face intersections"],["pure simplicial complex","纯单纯复形","algebraic topology","each simplex contained in one of maximal dimension"],["oriented incidence matrix","定向关联矩阵","algebraic topology","matrix of the simplicial boundary operator"],["Betti number","Betti 数","algebraic topology","dimension of a homology space"]],"source_pages":[22,23,24,25],"source_observations":[{"pdf_page":23,"message":"The source describes incidence-matrix columns and rows as corresponding to k-chains and (k-1)-chains, not explicitly basis simplices. Preserve this wording without silently narrowing it."}],"figure_source_crops":[{"label":"fig:oriented-simplices","pdf_page":23,"bbox_top_origin_pt":[105,62,430,145]},{"label":"fig:boundaries-of-chains","pdf_page":24,"bbox_top_origin_pt":[104,62,430,246]},{"label":"fig:homologous-cycles","pdf_page":24,"bbox_top_origin_pt":[185,277,333,423]},{"label":"fig:betti-domain-examples","pdf_page":25,"bbox_top_origin_pt":[106,154,430,240]}]},
UNITS[4]:{"names":["Betti","de Rham","De Rham"],"terms":[],"source_pages":[29],"source_observations":[{"pdf_page":29,"message":"The original summary prints 'cocyles'. The reconstructed English retains this spelling; Chinese translates the intended cocycle term already defined in the chapter, without adding mathematical content."}]}
}

def prepare():
    m["guard"]()
    progress=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for unit in UNITS:
        assert next(x for x in progress if x["Unit ID"]==unit)["QA Status"]!="passed"
        path=B.assert_write_path(B.root/f"translation/authored/{unit}.bilingual.tex")
        # Pure punctuation formatting of these new unaccepted files only.
        m["write"](path.relative_to(B.root).as_posix(),path.read_text(encoding="utf8").replace("、",", "))
        m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
    glyphs=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for page in [22,24,29]:
            for char in doc.pages[page-1].chars:
                if "EUFM10" in char["fontname"] and char["text"] in ("Z","B"):
                    glyphs.append({"pdf_page":page,"printed_page":str(page-10),"source_letter":char["text"],"source_font":char["fontname"],"bbox":[char["x0"],char["top"],char["x1"],char["bottom"]],"presentation":r"\mathcal "+char["text"],"status":"user-approved non-Fraktur font exception"})
    assert glyphs
    m["dump"]("qa/formula/chapter-02-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","original_font_evidence":glyphs,"new_transcriptions_do_not_claim_original_glyph_family_identity":True,"distinct_symbols_merged":False})
    rows=list(csv.DictReader(B.notation.open(encoding="utf8"),delimiter="\t"))
    fields=list(rows[0])
    for row in rows:
        if r"\mathcal Z" in row["Source Notation"]:
            row["Notes"]="Original PDF uses EUFM10 Fraktur Z/B; displayed mathcal is the explicit user-approved non-Fraktur presentation exception. Original glyph metadata retained in QA."
    m["s"]["tsv"]("glossary/notation.tsv",fields,rows)
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.parse_args();prepare()
