"""Book-local index provenance and navigation copies; accepted TeX is read-only."""
import collections,hashlib,json,re,runpy,sys
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")));B=m["B"]

def source_rows():
    rows=[];pending="";group=""
    for page in (232,233,234):
        for line in (B.root/f"workspace/raw-text/full/pdf-{page:03}.txt").read_text(encoding="utf8").splitlines():
            line=line.strip()
            if line.startswith("©"):break
            if not line or line=="Index" or re.fullmatch(r"(?:\d+ Index|Index \d+)",line):continue
            if re.fullmatch("[A-Z]",line):group=line;continue
            pending=(pending+" "+line).strip();hit=re.fullmatch(r"(.+?),\s*(\d+(?:,\s*\d+)*)",pending)
            if hit:
                raw=hit[1];text=raw.strip().replace("ﬁ","fi").replace("V ec","Vec").replace("V ector","Vector")
                rows.append({"group":group,"source_term_raw":raw,"source_term":text,"source_printed_pages":[int(v) for v in hit[2].split(",")],"index_pdf_page":page});pending=""
    assert len(rows)==179 and not pending
    return rows

def input_files():
    files=sorted((B.root/"tex/chapters").glob("chapter-*.tex"));result=[];sample=False
    for file in files:
        if file.stem>"chapter-01-section-08" and not sample:result.append(B.root/"tex/chapters/sample.tex");sample=True
        result.append(file)
    return result

def page_targets(entries):
    by_pdf=collections.defaultdict(list);page_map={int(x["printed_page"]):x["pdf_page"] for x in m["load"]("structured/source/page-map.json") if str(x["printed_page"]).isdigit() and x["logical_book_position"] not in ("references","index")}
    # Walk the existing compile order. Metadata is read, never regenerated.
    for file in input_files():
        text=file.read_text(encoding="utf8");marks=list(m["MARK"].finditer(text))
        english=(B.root/("structured/reviewed/sample-english.tex" if file.name=="sample.tex" else "structured/reviewed/"+file.name)).read_text(encoding="utf8")
        enmarks=list(m["MARK"].finditer(english));enbodies={h[1]:english[h.end():enmarks[i+1].start() if i+1<len(enmarks) else len(english)] for i,h in enumerate(enmarks)}
        for i,mark in enumerate(marks):
            body=text[mark.end():marks[i+1].start() if i+1<len(marks) else len(text)]
            row={"file":file.relative_to(B.root).as_posix(),"block_id":mark[1],"type":mark[3],"source_pdf_pages":list(map(int,mark[2].split(","))),"body":body,"english":enbodies[mark[1]]}
            for page in row["source_pdf_pages"]:by_pdf[page].append(row)
    result={}
    def words(text):
        text=text.lower().replace("–"," ").replace("--"," ").replace("ﬁ","fi")
        text=re.sub(r"\\(?:label|ref|eqref|BookCite)\{[^}]+\}","",text)
        text=re.sub(r"\\[a-zA-Z]+"," ",text)
        return [w for w in re.findall(r"[a-z]+|\d+",text) if w not in {"the","a","an","of","on","and","for","to","some","method","methods","process"}]
    selections=[(entry,printed) for entry in entries for printed in entry["source_printed_pages"]]
    reviewed_labels={"Left and right preconditioning":"eq:split-preconditioned-system","Left preconditioning":"eq:left-preconditioned-system","Right preconditioning":"eq:right-preconditioned-system","Submultiplicative":"cond:matrix-norm-product","Regular splitting":"def:regular-splitting","Newton’s method":"eq:euclidean-newton-system","Minimal residual approach":"eq:minimal-residual-problem","Petrov–Galerkin approach":"eq:petrov-galerkin-orthogonality","Krylov subspace":"def:krylov-subspace","Conjugate A-orthogonalization process":"eq:cocr-a-orthogonality"}
    for entry,printed in selections:
        pdf=page_map[printed];options=by_pdf[pdf];assert options,(printed,pdf)
        terms=set(words(entry["source_term"]))
        def score(row):
            normalized=words(row["english"]);tokens=set(normalized);ratio=len(terms&tokens)/max(1,len(terms))
            # Exact original terms within the indexed source page take priority;
            # source headings/definitions disambiguate incidental occurrences.
            phrase=" ".join(words(entry["source_term"])) in " ".join(normalized)
            heading=row["type"] in ("section","subsection","definition","theorem")
            title_exact=False
            h=re.search(r"\\(?:section|subsection|subsubsection|paragraph)\{|\\begin\{(?:Definition|Theorem)\}\{",row["english"])
            if h:
                title,_=m["brace"](row["english"],h.end()-1)
                title_exact=words(title)==words(entry["source_term"])
            return (ratio,title_exact,phrase,heading,-len(normalized))
        forced=reviewed_labels.get(entry["source_term"])
        if forced:
            relevant=[x for x in options if r"\label{"+forced+"}" in x["body"]];assert relevant,(entry["source_term"],printed,forced)
            chosen=relevant[0].copy()
        else:chosen=max(options,key=score).copy()
        body=chosen.pop("body");english=chosen.pop("english")
        found=list(re.finditer(r"\\label\{([^}]+)\}",body))
        label=max(found,key=lambda h:(len(terms&set(words(h[1].replace(":"," ").replace("-"," ")))),-len(h[1]))) if found else None
        if forced:label=next(h for h in found if h[1]==forced)
        chosen.update({"source_printed_page":printed,"source_pdf_page":pdf,"label":f"idx:{Path(chosen['file']).stem}:{chosen['block_id']}","granularity":"reviewed concept block on the original indexed source page; not token-tight","source_sha256":m["sha256_file"](B.root/chosen["file"]),"matching_score":score(max(options,key=score)),"english_excerpt":english[:260],"index_entry":entry["id"]})
        if label:chosen.update({"insertion":"reuse-existing-label","existing_label":label[1],"label":label[1]})
        elif body.lstrip().startswith("{"):chosen.update({"insertion":"inside-prose-group"})
        elif body.lstrip().startswith(r"\begin{Proof}"):chosen.update({"insertion":"inside-proof"})
        elif re.match(r"[\u3400-\u9fffA-Za-z$]",body.lstrip()):chosen.update({"insertion":"prose-start"})
        else:raise AssertionError((printed,chosen,body[:200]))
        result[entry["id"]+"-p"+str(printed)]=chosen
    return result

def term_latex(text):
    text=text.replace("–","--").replace("_",r"\_")
    replacements={"BiCGSTAB2":"BiCGSTAB$^2$","BiCGSTAB(ℓ)":r"BiCGSTAB($\ell$)","IDR(s)":"IDR($s$)","Conjugate A-":"Conjugate $A$-","GBiCGSTAB(s, L)":"GBiCGSTAB($s,L$)","GCR(k)":"GCR($k$)","GMRES(m)":"GMRES($m$)","GPBiCG(m,ℓ )":r"GPBiCG($m,\ell$)","GPBiCGstab(L)":"GPBiCGstab($L$)","ILU( p)":"ILU($p$)","ILUT( p,τ)":r"ILUT($p,\tau$)","LDL ⊤":r"$LDL^{\top}$","Matrix pth":"Matrix $p$th","matrix pth":"matrix $p$th","n-mode":"$n$-mode","Orthomin(k)":"Orthomin($k$)"}
    for a,b in replacements.items():text=text.replace(a,b)
    return text

def prepare():
    m["guard"]();rows=source_rows();translations=(B.root/"translation/authored/index-translations.txt").read_text(encoding="utf8").splitlines();assert len(translations)==len(rows)
    for n,row in enumerate(rows,1):row["id"]=f"index-term-{n:03}"
    targets=page_targets(rows)
    lines=[r"% block: index-heading page:232 type:chapter",r"\clearpage\section*{\BT{Index}{索引}}\phantomsection",r"\makeatletter\def\@currentlabel{Index}\label{chap:index}\makeatother",r"\begin{description}",""]
    last=None
    for n,(row,zh) in enumerate(zip(rows,translations),1):
        en=term_latex(row["source_term"]);assert collections.Counter(m["math"](en))==collections.Counter(m["math"](zh)),(n,en,zh)
        row.update({"source_latex":en,"target_latex":zh,"target_labels":[targets[row["id"]+"-p"+str(p)]["label"] for p in row["source_printed_pages"]]})
        lines.append(f"% block: {row['id']} page:{row['index_pdf_page']} type:ordinary-paragraph")
        if row["group"]!=last:lines.append(r"\item["+row["group"]+"]");last=row["group"]
        source=", ".join(map(str,row["source_printed_pages"]));target=", ".join(r"\pageref{"+key+"}" for key in row["target_labels"])
        lines.append(r"\BT{"+en+"}{"+zh+"}, \\BT{"+source+"}{"+target+r"}\par")
        lines.append("")
    lines.append(r"\end{description}")
    m["guard"]()
    if "--write-registry" in sys.argv:
        m["dump"]("structured/source/index-registry.json",{"entries":rows,"source_page_targets":targets})
        print(json.dumps([{"id":row["id"],"term":row["source_term"],"targets":[{"printed":p,"block":targets[row["id"]+"-p"+str(p)]["block_id"],"label":targets[row["id"]+"-p"+str(p)]["label"],"score":targets[row["id"]+"-p"+str(p)]["matching_score"]} for p in row["source_printed_pages"]]} for row in rows],ensure_ascii=False))
        return
    result={"authored":"\n".join(lines)+"\n"} if "--source" in sys.argv else {"registry":{"entries":rows,"source_page_targets":targets}}
    print(json.dumps(result,ensure_ascii=False))

def linked_copies():
    registry=m["load"]("structured/source/index-registry.json");grouped=collections.defaultdict(list)
    seen=set()
    for row in registry["source_page_targets"].values():
        if row["insertion"]!="reuse-existing-label" and row["label"] not in seen:grouped[row["file"]].append(row);seen.add(row["label"])
    # Whole-book destination regression found the unchanged Chapter 1 box
    # starting a page after its pre-box refstepcounter anchor. Pagination only;
    # never patch an accepted translation file to repair this integration issue.
    guard_file="tex/chapters/chapter-01-section-06.tex"
    grouped.setdefault(guard_file,[])
    contents_entries={"tex/chapters/software.tex":"软件","tex/chapters/references.tex":"参考文献","tex/chapters/index.tex":"索引"}
    for rel in contents_entries:grouped.setdefault(rel,[])
    copies={};evidence=[]
    for rel,rows in grouped.items():
        original=(B.root/rel).read_text(encoding="utf8");marks=list(m["MARK"].finditer(original));byid={h[1]:h for h in marks};edits=[]
        for row in rows:
            mark=byid[row["block_id"]];end=next((h.start() for h in marks if h.start()>mark.start()),len(original));body=original[mark.end():end]
            anchor=r"\phantomsection\label{"+row["label"]+"}"
            if row["insertion"]=="after-existing-label":
                hit=re.search(r"\\label\{"+re.escape(row["existing_label"])+r"\}",body);offset=hit.end()
                # Share the existing object's destination: no extra phantom section.
                anchor=r"\label{"+row["label"]+"}"
            elif row["insertion"]=="inside-prose-group":offset=body.index("{")+1;anchor=r"\leavevmode"+anchor
            elif row["insertion"]=="inside-proof":offset=body.index(r"\begin{Proof}")+len(r"\begin{Proof}");anchor=r"\leavevmode"+anchor
            else:offset=len(body)-len(body.lstrip());anchor=r"\leavevmode"+anchor
            edits.append((mark.end()+offset,anchor,row))
        result=original
        for pos,anchor,row in sorted(edits,key=lambda x:x[0],reverse=True):result=result[:pos]+anchor+result[pos:]
        pagination_guard=""
        if rel==guard_file:
            token=r"\begin{Theorem}\label{thm:regular-splitting-convergence}"
            assert result.count(token)==1
            pagination_guard=r"\Needspace{14\baselineskip}"+"\n"
            result=result.replace(token,pagination_guard+token,1)
        contents_entry=""
        if rel in contents_entries:
            contents_entry=r"\addcontentsline{toc}{section}{"+contents_entries[rel]+"}"
            result=result.replace(r"\makeatother",r"\makeatother"+contents_entry,1)
        stripped=result
        if contents_entry:stripped=stripped.replace(contents_entry,"",1)
        if pagination_guard:
            stripped=stripped.replace(pagination_guard+token,token,1)
        for pos,anchor,row in sorted(edits,key=lambda x:x[0]):
            assert stripped.count(anchor)==1,(rel,anchor)
            stripped=stripped.replace(anchor,"",1)
        assert stripped==original,rel
        generated="tex/generated/index-linked/"+Path(rel).name;m["write"](generated,result);copies[rel]=generated
        evidence.append({"original":rel,"generated":generated,"source_sha256":m["sha256_file"](B.root/rel),"generated_sha256":m["sha256_file"](B.root/generated),"anchors_added":len(rows),"pagination_guard":pagination_guard,"contents_entry":contents_entry,"removing_only_inserted_navigation_and_pagination_tokens_recovers_original":True})
    m["dump"]("qa/translation/index-linked-copies.json",{"passed":True,"files":evidence,"accepted_source_text_unchanged":True})
    return copies

if __name__=="__main__":prepare()
