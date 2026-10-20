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

NOTES.update({
"chapter-08-section-06":{"names":["Maxwell","Hodge"],"terms":[["slack variable","松弛变量","Maxwell mixed formulation","auxiliary zero-form vanishing when electromagnetic source data are compatible"]],"source_pages":[113,114],"source_observations":[{"pdf_page":114,"message":"The reconstruction sentence prints H=star_{mu=1} B, with an equals sign, not mu^{-1}. Confirmed in the 400-dpi original crop workspace/pages/source-crops/maxwell-weighted-star.png. Preserve this printed subscript."}]},
"chapter-08-section-07":{"names":["Stokes","Neumann","Poisson","de Rham","Galerkin","Hilbert","Navier–Stokes","Taylor–Hood","Mardal","Tai","Winther","Guzmán","Neilan","Falk","Fu"],"terms":[["mass conservative element","质量守恒单元","Stokes finite elements","discrete velocity satisfies divergence-free constraint exactly"],["nonconforming discretization","非协调离散化","finite elements","trial functions do not form a true subspace of the continuous domain"]],"source_pages":[114,115,116,117],"source_observations":[{"pdf_page":116,"message":"Equation 8.21 prints inf_{p in S_h} ||p-q||_0, not inf_{q in S_h}. Preserve the printed infimum variable."},{"pdf_page":116,"message":"The two-dimensional Stokes complex prints R^n, not R^2, in the middle H^1 space. Preserve R^n."}]}
})

NOTES["chapter-08-section-08"]={"names":["Hodge","Hilbert","de Rham","Stokes","Dirichlet","Airy","St. Venant","Hessian","Hermite","Argyris","Lagrange"],"terms":[["compliance tensor","柔度张量","linear elasticity","positive definite stress-to-strain constitutive tensor"],["elasticity complex","弹性复形","finite element exterior calculus","Hilbert complex for symmetric-stress elasticity"],["weak symmetry","弱对称性","mixed elasticity","stress symmetry imposed through a Lagrange multiplier"]],"source_pages":[117,118,119,120,121,122],"source_observations":[{"pdf_page":119,"message":"The three-dimensional asym display prints its last component as tau_12-tau_12. Retain both printed 12 subscripts, not an inferred 21."},{"pdf_page":119,"message":"The proof says no constraint on the symmetry of f, not rho. Retain the source f."},{"pdf_page":120,"message":"Both off-diagonal Airy tensor entries are printed -partial^2 phi/partial x_2^2, not mixed derivatives. Preserve both displayed entries."},{"pdf_page":121,"message":"The Airy-stress paragraph explicitly references (8.8), whose numbered source object is the Faraday equation, while the Airy display is unnumbered. Retain the printed reference through its actual numbered label, flag the source mismatch, and do not guess the intended replacement."},{"pdf_page":121,"message":"The final weak-symmetry complex prints R^{2x2} in the domain above its arrow, while its base matrix space uses R^{nxn}. Preserve both printed dimensions."},{"pdf_page":122,"message":"Blank production leaf with printer marks; retained in the source PDF, not missing mathematical content."}],"expected_numbered_equations":26,"expected_figures":0,"expected_tables":1,"unit_tables":0}

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
