"""Book-local, source-image-checked bibliography transcription; no guessed references."""
import argparse,csv,json,re,runpy
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]

def bibliography():
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));assert next(x for x in rows if x["Unit ID"]=="bibliography")["QA Status"]!="passed"
    raw=[];page_by_number={}
    for page in range(123,128):
        text=(B.root/f"workspace/raw-text/full/pdf-{page}.txt").read_text(encoding="utf8")
        text=re.sub(r"(?m)^(?:Bibliography(?:\s+\d+)?|\d+\s+Bibliography|113)\s*$","",text)
        for hit in re.finditer(r"(?m)^\[(\d+)\]",text):page_by_number[int(hit[1])]=page
        raw.append(text)
    text="\n".join(raw)
    # Explicit original-page-reviewed line-end joins, not universal dehyphenation.
    joins=[("opera-\ntor","operator"),("El-\nements","Elements"),("differen-\ntial","differential"),("sym-\nmetry","symmetry"),("Differen-\ntial","Differential"),("Hei-\ndelberg","Heidelberg"),("com-\nputations","computations"),("Ele-\nment","Element"),("Equa-\ntions","Equations"),("re-\nlated","related"),("Ap-\nplied","Applied"),("As-\nsociates","Associates"),("Ba-\nnach","Banach"),("bub-\nble","bubble"),("Poly-\nnomial","Polynomial"),("ele-\nments","elements"),("Reb-\nholz","Rebholz"),("Univer-\nsity","University"),("di-\nmensions","dimensions"),("Gen-\neral","General"),("Prince-\nton","Princeton")]
    for a,b in joins:assert a in text,a;text=text.replace(a,b)
    # These two printed hyphens are intrinsic, not typesetting hyphenation.
    text=text.replace("Pseudo-\ndifferential","Pseudo-differential").replace("90-\n9020969","90-9020969")
    for a,b in [("ﬁ","fi"),("ﬂ","fl"),("V ol.","Vol."),("V olker","Volker"),("Jind ˇrich Neˇcas","Jindřich Nečas"),("K ¯osaku","Kōsaku"),("Anal.51","Anal. 51"),("Numer.19","Numer. 19"),("Review59","Review 59"),("Part A(1988)","Part A (1988)"),("for2nd","for 2nd")]:text=text.replace(a,b)
    hits=list(re.finditer(r"(?m)^\[(\d+)\]",text));assert [int(x[1]) for x in hits]==list(range(1,72));entries=[]
    tex=r"\clearpage\section*{\BT{Bibliography}{参考文献}}\phantomsection\label{back:bibliography}"+"\n"
    tex+=r"\BT{Bibliographic entries and original citation-page metadata are retained in their source languages. The parenthetical Cited on numbers below refer to the original printed pagination, not the pagination of this translation.}{文献条目及原书引页元数据保留原文. 以下括号中 Cited on 的页码为原书印刷页码, 不是译本页码.}"+"\n"
    tex+=r"\newcounter{bookreference}\begin{list}{[\arabic{bookreference}]}{\usecounter{bookreference}\setlength{\leftmargin}{2.7em}\setlength{\labelwidth}{2.2em}}\small"+"\n"
    for i,hit in enumerate(hits):
        number=int(hit[1]);value=re.sub(r"\s+"," ",text[hit.end():hits[i+1].start() if i+1<len(hits) else len(text)]).strip()
        if number in (6,12,13,68):assert value.startswith(","),value;value="—"+value
        if number==26:value="Annalisa Buffa, Martin Costabel, and Dongwoo Sheen, On traces for @@Hcurl@@ in Lipschitz domains, J. Math. Anal. Appl. 276 (2002), no. 2, 845–867. MR 1944792 (Cited on p. 31)"
        if number in (3,4):value=value.replace("ofH(div)","of @@Hdiv@@")
        if number in (53,54):value=value.replace("Rn:","@@Rn@@:")
        if number==59:value=value.replace("R3,","@@Rthree@@,")
        if number==66:value=value.replace("H(curl)","@@Hcurlplain@@")
        assert not any(ord(c)<32 for c in value),number
        cited=re.search(r"\(Cited on pp?\. ([^)]+)\)",value);assert cited,number
        refs=[x.strip() for x in cited[1].split(",")]
        entries.append({"number":number,"pdf_page":page_by_number[number],"printed_page":str(page_by_number[number]-10),"text":value,"original_cited_printed_pages":refs,"review_status":"source-image-verified","names_titles_publication_data_retained_in_original_language":True})
        safe=value.replace("&",r"\&").replace("%",r"\%").replace("#",r"\#").replace("_",r"\_")
        for key,math in {"Hcurl":r"$\mathbf H(\operatorname{curl},\Omega)$","Hdiv":r"$H(\operatorname{div})$","Rn":r"$\mathbb R^n$","Rthree":r"$\mathbb R^3$","Hcurlplain":r"$H(\operatorname{curl})$"}.items():safe=safe.replace("@@"+key+"@@",math)
        tex+=f"\n% block: bibliography-entry-{number:02} page:{page_by_number[number]} type:ordinary-paragraph\n"+r"\item\label{bib:source-"+str(number)+"}"
        if number==27:tex+=r"\label{bib:cartan-differential-expressions}"
        tex+=safe+"\n"
    tex+=r"\end{list}"+"\n% Original PDF 128 is a blank production leaf, retained in the source.\n"
    m["write"]("translation/authored/bibliography.bilingual.tex",tex)
    m["dump"]("structured/source/bibliography-entries.json",entries)
    m["dump"]("translation/authored/bibliography-notes.json",{"names":["Jindřich Nečas","Kōsaku Yosida","Élie Cartan","Jochen Brüning","Lars Hörmander","Owren Brynjulf","Jean-Luc Guermond","Vincent Quenneville-Belair","J.-C. Nédélec"],"terms":[],"source_pages":list(range(123,129)),"source_observations":[{"pdf_page":125,"message":"The bibliography prints the author form Owren Brynjulf. Preserve its original order rather than normalizing it."},{"pdf_page":127,"message":"Original image confirms Jindřich Nečas and Kōsaku Yosida. Native text accent placement artifacts are repaired to these actual printed spellings; raw extraction retained."},{"pdf_page":128,"message":"Blank production leaf, original PDF retained."}]})
    m["metadata"]("bibliography");m["assemble"]();m["guard"]()

def index():
    m["guard"]();rows=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"));assert next(x for x in rows if x["Unit ID"]=="index")["QA Status"]!="passed"
    lines=(B.root/"translation/authored/index-map.txt").read_text(encoding="utf8").splitlines();records=[];parents=[];page=129
    for line in lines:
        if not line.strip():continue
        fields=line.split("|");assert len(fields)==4,line
        level=len(fields[0])-len(fields[0].lstrip());en=fields[0].strip();zh=fields[1];printed=[v.strip() for v in fields[2].split(",") if v.strip()];targets=[fields[3]] if fields[3].startswith("see:") else [v.strip() for v in fields[3].split(",") if v.strip()]
        assert level<=len(parents),(en,level,parents);parents=parents[:level];path="/".join(parents+[en]);parents.append(en)
        if path=="Laplacian":page=130
        key="index:"+re.sub(r"[^a-z0-9]+","-",path.lower()).strip("-")
        records.append({"id":key,"path":path,"level":level,"english":en,"chinese":zh,"original_printed_pages":printed,"source_pdf_page":page,"targets":targets,"target_resolution":"containing section or named object, not an assertion of identical source/translation pagination","review_status":"source-image-verified"})
    assert len({x["id"] for x in records})==len(records)
    bypath={x["path"]:x for x in records};alltex="\n".join(p.read_text(encoding="utf8") for p in (B.root/"tex/chapters").glob("*.tex"));labels=set(re.findall(r"\\label\{([^}]+)\}",alltex))
    tex=r"\clearpage\section*{\BT{Index}{索引}}\phantomsection\label{back:index}"+"\n"
    tex+=r"\BT{The original entry order and hierarchy are retained. Links locate the containing section or named object in this translation; the original printed page numbers are retained separately in the structured index register and are not substituted for translation page numbers.}{保留原书条目的次序和层级. 链接定位译本中包含相应内容的章节或具名对象; 原书印刷页码另存于结构化索引登记表, 不充作译本页码.}"+"\n"
    tex+=r"\begingroup\small\setlength{\parindent}{0pt}"+"\n"
    prefixes={"chap":"Chapter","sec":"Section","subsec":"Section","thm":"Theorem","lem":"Lemma","prop":"Proposition","cor":"Corollary","def":"Definition","fig":"Figure","tab":"Table","rem":"Remark"}
    for row in records:
        links=[]
        for key in row["targets"]:
            if key.startswith("see:"):
                target=bypath[key[4:]]["id"]
                aliases={"operator/adjoint":("operator, adjoint","算子, 伴随"),"degree of freedom (DOF)":("degree of freedom","自由度"),"vector space, graded":("vector space, graded","向量空间, 分次")}
                english,chinese=aliases[key[4:]]
                links.append(r"\hyperref["+target+r"]{\BT{see "+english+"}{见 "+chinese+"}}")
            else:
                assert key in labels,(row["english"],key)
                links.append((r"\eqref{"+key+"}") if key.startswith("eq:") else prefixes[key.split(":")[0]]+r"~\ref{"+key+"}")
        tex+=f"\n% block: {row['id'].replace(':','-')} page:{row['source_pdf_page']} type:ordinary-paragraph\n"+r"\par\noindent\hspace*{"+str(row["level"])+r"em}\phantomsection\label{"+row["id"]+r"}\BT{"+row["english"]+"}{"+row["chinese"]+"}"
        if links:tex+=r"\quad "+", ".join(links)
        tex+="\n"
    tex+=r"\par\endgroup"+"\n"
    m["write"]("translation/authored/index.bilingual.tex",tex);m["dump"]("structured/source/index-register.json",records)
    m["dump"]("translation/authored/index-notes.json",{"names":["Airy","Betti","de Rham","Hilbert","Fredholm","Koszul","Stokes","Poincaré–Lefschetz","Hodge","Laplace","Maxwell","Laplace–Beltrami","Lagrange","Whitney","Galerkin","Hille–Yosida–Phillips","Leibniz","Piola","Poincaré","St. Venant"],"terms":[],"source_pages":[129,130],"source_observations":[]})
    m["metadata"]("index");m["assemble"]();m["guard"]();print("Index entries",len(records))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.add_argument("action",choices=["bibliography","index"]);a=p.parse_args();{"bibliography":bibliography,"index":index}[a.action]()
