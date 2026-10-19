"""Read-only serialization of the original bibliography, not title translation.

All nine bibliography pages have been visually inspected. The caller applies
the emitted source file and evidence using the normal patch mechanism.
"""
import hashlib,json,re,runpy,subprocess,sys
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));B=m["B"]
m["guard"]()
entries=[];joins=[];current=None
keep_hyphen={"rank","large","STAN-CS","many","non"}
for page in range(223,232):
    raw=subprocess.check_output(["pdftotext","-f",str(page),"-l",str(page),"-layout","-enc","UTF-8",str(B.require_source_pdf()),"-"]).decode("utf8").replace("\r\n","\n")
    for line in raw.splitlines():
        line=line.strip()
        if line.startswith("©"):break
        if not line or line=="References" or re.fullmatch(r"(?:\d+\s+References|References\s+\d+)",line):continue
        hit=re.match(r"(\d+)\.\s+(.+)",line)
        if hit:
            current={"number":int(hit[1]),"pdf_page":page,"printed_page":str(page-10),"raw_lines":[hit[2]]};entries.append(current)
        elif current:
            current["raw_lines"].append(line)
assert [x["number"] for x in entries]==list(range(1,213))

def serialize(text):
    # Four control glyphs are decoded only after original-page visual checks:
    # ell in refs 153/162/164 and transpose in ref 210.
    text=text.replace("\x02","ℓ").replace("\x03","⊤")
    for a,b in [("&",r"\&"),("%",r"\%"),("#",r"\#"),("_",r"\_")]:text=text.replace(a,b)
    text=text.replace("ℓ",r"$\ell$").replace("ω",r"$\omega$").replace("⊤",r"$\top$")
    text=text.replace("λ2 A + λ B + C",r"$\lambda^2 A+\lambda B+C$")
    assert "λ" not in text,text
    return text

lines=[r"% block: references-heading page:223 type:chapter",
 r"\clearpage\section*{\BT{References}{参考文献}}\phantomsection",
 r"\makeatletter\def\@currentlabel{References}\label{chap:references}\makeatother",
 r"\begin{enumerate}[label=\arabic*.,ref=\arabic*,leftmargin=3em]",""]
for entry in entries:
    text=entry["raw_lines"][0]
    for nextline in entry["raw_lines"][1:]:
        if text.endswith("-"):
            stem=re.search(r"(\S+)-$",text)[1]
            keep=stem in keep_hyphen
            joins.append({"entry":entry["number"],"left":stem,"right":nextline.split()[0],"lexical_hyphen_retained":keep})
            text=text+nextline if keep else text[:-1]+nextline
        elif text.endswith("–"):
            text+=nextline
        else:text+=" "+nextline
    entry["restored_text"]=text;entry["latex"]=serialize(text)
    # Whole author field is preserved byte-for-byte in the TeX text, including
    # source order, initials, accents, apostrophes and lexical hyphens.
    entry["author_field"]=text.split(":",1)[0]
    lines.extend([f"% block: reference-source-{entry['number']:03} page:{entry['pdf_page']} type:ordinary-paragraph",
                  r"\item\label{bib:source-"+str(entry["number"])+"}"+entry["latex"],""])
lines.append(r"\end{enumerate}")
m["guard"]()
if "--source" in sys.argv:
    print(json.dumps({"authored":"\n".join(lines)+"\n"},ensure_ascii=False))
else:
    for entry in entries:
        entry["restored_text_sha256"]=hashlib.sha256(entry.pop("restored_text").encode("utf8")).hexdigest()
        entry.pop("latex")
    print(json.dumps({"entries":entries,"line_end_joins":joins},ensure_ascii=False))
