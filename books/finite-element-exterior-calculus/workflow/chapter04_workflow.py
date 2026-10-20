"""Stage only unaccepted Chapter 4 units with explicit alphabet provenance."""
import argparse,collections,csv,re,runpy
from pathlib import Path
import pdfplumber
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
NOTES={
"chapter-04-introduction":{"names":["Hilbert","de Rham","Brüning","Lesch","Hodge","Riemannian","Laplacian"],"terms":[["Hilbert complex","Hilbert 复形","Hilbert complexes","closed densely defined differentials with consecutive composition zero"]],"source_pages":[43],"source_observations":[{"pdf_page":43,"message":"Original footnote prints 'occured'. Reconstructed English retains the spelling; Chinese preserves its meaning without inventing content."}]},
"chapter-04-section-01":{"names":["Hilbert","Fredholm"],"terms":[["base space","基空间","Hilbert complexes","ambient Hilbert space W^k"],["domain complex","定义域复形","Hilbert complexes","spaces V^k with graph norms and bounded differentials"],["Fredholm complex","Fredholm 复形","Hilbert complexes","cohomology spaces finite dimensional"],["reduced cohomology","约化上同调","Hilbert complexes","cycles modulo closure of coboundaries"]],"source_pages":[43,44],"source_observations":[]}
}

def prepare(units):
    m["guard"]();progress=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    policy=m["load"]("config/math-alphabet-policy.json")
    if not any(x["source_letters"]==["H"] for x in policy["mappings"]):
        policy["mappings"].append({"source_family":"EUFM10 / EUFM7 Fraktur","source_letters":["H"],"source_meaning":"harmonic form space, not the calligraphic cohomology space","display_family":"mathsf","status":"non-Fraktur rendering under the user's explicit no-Fraktur instruction","distinction":"Keep source mathcal H for cohomology and display source Fraktur H as mathsf H; do not merge the two"});m["dump"]("config/math-alphabet-policy.json",policy)
    for unit in units:
        assert unit in NOTES
        assert next(x for x in progress if x["Unit ID"]==unit)["QA Status"]!="passed"
        rel=f"translation/authored/{unit}.bilingual.tex";path=B.assert_write_path(B.root/rel)
        text=path.read_text(encoding="utf8").replace("、",", ")
        m["write"](rel,text);en=m["s"]["language"](text,0);zh=m["s"]["language"](text,1)
        names={x["Source Form"] for x in csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t")}|{n for note in NOTES.values() for n in note["names"]}
        for name in names:
            pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])";assert len(re.findall(pat,en))==len(re.findall(pat,zh)),(unit,name,len(re.findall(pat,en)),len(re.findall(pat,zh)))
        assert not m["s"]["find_chinese_prose_punctuation"](zh)
        m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
    glyphs=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n in range(43,61):
            for ch in doc.pages[n-1].chars:
                if "EUFM" in ch["fontname"]:
                    assert ch["text"] in ("B","Z","H")
                    glyphs.append({"pdf_page":n,"printed_page":str(n-10),"letter":ch["text"],"font":ch["fontname"],"bbox":[ch["x0"],ch["top"],ch["x1"],ch["bottom"]],"display_family":"mathsf" if ch["text"]=="H" else "mathcal"})
    m["dump"]("qa/formula/chapter-04-alphabet-provenance.json",{"policy":"config/math-alphabet-policy.json","source_glyphs":glyphs,"source_harmonic_and_cohomology_spaces_remain_distinct":True,"glyph_family_identity_not_claimed":True})
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("units",nargs="+",choices=list(NOTES));a=p.parse_args();prepare(a.units)
