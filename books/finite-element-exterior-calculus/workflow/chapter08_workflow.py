"""Stage explicitly selected source-image-reviewed, unaccepted Chapter 8 units."""
import argparse,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-08-introduction":{"names":["Hilbert","de Rham","Hodge","Galerkin"],"terms":[],"source_pages":[107],"source_observations":[]},
"chapter-08-section-01":{"names":["Hodge","Krylov–Schur","Babuška","Osborn","Babuška–Osborn","Maxwell","Lagrange","Whitney","Galerkin","Hilbert"],"terms":[["spurious eigenvalue","伪特征值","finite element spectral approximation","discrete spectral pollution without corresponding continuous eigenvalue"]],"source_pages":[107,108],"source_observations":[]},
"chapter-08-section-02":{"names":["Hilbert","Hodge","de Rham","Dirichlet"],"terms":[["weighted inner product","加权内积","Hilbert complexes","inner product modified by a uniformly positive definite coefficient field"]],"source_pages":[108,109],"source_observations":[]},
"chapter-08-section-03":{"names":["Hodge","Hilbert","Helmholtz"],"terms":[["time-harmonic problem","时谐问题","electromagnetism","problem with fixed-frequency harmonic time dependence"]],"source_pages":[109,110],"source_observations":[{"pdf_page":110,"message":"The display Lu=[(d+l1)(delta+l2)+(delta+l3)(d+l4)+l5] has no trailing action on u on its right side. Retain the source display without inserting u."}],"table_data_review":"Every entry of Table 8.1 visually read on PDF 110, including l2/l3/l5 zero conditions and r+1/r/r-1 rates."},
"chapter-08-section-04":{"names":["Hodge","Riemannian","Laplace–Beltrami","Euclidean","Hilbert","Holst","Stern"],"terms":[],"source_pages":[111],"source_observations":[]},
"chapter-08-section-05":{"names":["Hodge","Hille–Yosida–Phillips","Galerkin","Hilbert"],"terms":[["elliptic projection","椭圆投影","evolution finite element analysis","projection used to transfer elliptic error estimates to time-dependent problems"]],"source_pages":[111,112],"source_observations":[{"pdf_page":111,"message":"Equation 8.3 prints u_t+(delta d+d delta u)=f, with u only on the second summand inside the parentheses. Preserve the printed placement, rather than moving u outside."},{"pdf_page":112,"message":"The concluding energy-conservation sentence is printed without explicitly restricting the source f to zero. Retain the original assertion without silently adding a source condition."}]}
}

def prepare(units):
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for unit in units:
        assert next(x for x in rows if x["Unit ID"]==unit)["QA Status"]!="passed"
        rel=f"translation/authored/{unit}.bilingual.tex";text=(B.root/rel).read_text(encoding="utf8");en=m["s"]["language"](text,0);zh=m["s"]["language"](text,1)
        names={x["Source Form"] for x in csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t")}|{v for n in NOTES.values() for v in n["names"]}
        for name in names:
            pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";assert len(re.findall(pat,en))==len(re.findall(pat,zh)),(unit,name)
        assert not m["s"]["find_chinese_prose_punctuation"](zh)
        m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
    glyphs=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n in range(107,123):
            for ch in doc.pages[n-1].chars:
                if "EUFM" in ch["fontname"]:
                    assert ch["text"] in ("B","Z","H"),ch
                    glyphs.append({"pdf_page":n,"printed_page":str(n-10),"letter":ch["text"],"font":ch["fontname"],"bbox":[ch["x0"],ch["top"],ch["x1"],ch["bottom"]],"display_family":"mathsf" if ch["text"]=="H" else "mathcal"})
    m["dump"]("qa/formula/chapter-08-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","source_glyphs":glyphs,"glyph_family_identity_not_claimed":True})
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("units",nargs="+",choices=list(NOTES));a=p.parse_args();prepare(a.units)
