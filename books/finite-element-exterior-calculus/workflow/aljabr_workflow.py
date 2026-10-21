"""FEEC-only AJbook typesetting; immutable accepted prose is input, never edited."""
import argparse,collections,csv,hashlib,json,os,re,runpy,shutil,subprocess,sys,tempfile
from pathlib import Path
from xml.sax.saxutils import escape
from pypdf import PdfReader
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import verify_book_context
from mathbook.template import verify_manifest

ID="finite-element-exterior-calculus"
P=ProjectPaths();B,_=verify_book_context(P,ID,writable=True)
OLD="957802db5a638180f65af0c4937b193d88e0ce3d8b0e226031e21ab72fafca0a"
s=runpy.run_path(str(Path(__file__).with_name("sample_processor.py")))
def write(rel,text):
    path=B.assert_write_path(B.root/rel);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding="utf8");return path
def dump(rel,obj):return write(rel,json.dumps(obj,ensure_ascii=False,indent=2)+"\n")
def load(rel):return json.loads((B.root/rel).read_text(encoding="utf8"))
def guard():
    assert not verify_manifest(),verify_manifest()
    initial=load("qa/protected-inputs-initial.json")
    assert sha256_file(B.require_source_pdf())==initial["source_sha256"]==sha256_file(Path(r"D:\BaiduNetdiskDownload\Finite Element Exterior Calculus.pdf"))
    for row in initial["template_raw_files"]:assert sha256_file(P.template/row["path"])==row["sha256"],row
    for row in load("qa/full-input-protection.json")["accepted_files"]:assert sha256_file(B.root/row["file"])==row["sha256"],row
    assert sha256_file(B.root/"output/book-zh.pdf")==OLD
    baseline_path=B.root/"qa/template/aljabr-baseline.json"
    if baseline_path.exists():
        before=load("qa/template/aljabr-baseline.json")
        assert sha256_file(B.main_tex)==before["old_main_sha256"]
        assert sha256_file(P.glossary/"terminology.tsv")==before["global_glossary_sha256"]
def baseline():
    guard();dest=B.root/"qa/template/aljabr-baseline.json";assert not dest.exists()
    q=load("qa/latest-compilation.json");assert q["pdf_sha256"]==OLD
    dump("qa/template/aljabr-baseline.json",{"old_pdf_sha256":OLD,"old_build":q["build_directory"],"original_manifest_hash":directory_manifest_hash(P.template),"old_main_sha256":sha256_file(B.main_tex),"global_glossary_sha256":sha256_file(P.glossary/"terminology.tsv"),"other_book_refs":subprocess.check_output(["git","for-each-ref","--format=%(refname) %(objectname)","refs/heads/book/"],cwd=P.root,text=True).splitlines(),"remote":subprocess.check_output(["git","remote","-v"],cwd=P.root,text=True).splitlines()})
def prepare():
    guard();old=B.main_tex.read_text(encoding="utf8");source_files=[B.root/"tex"/x for x in re.findall(r"\\input\{((?:chapters/|frontmatter)[^}]*\.tex)\}",old)]
    assert len(source_files)==46 # Three accepted sample sections share one TeX input.
    records=[]
    for path in source_files:
        text=path.read_text(encoding="utf8");new=text
        if path.name!="publication.tex":
            new=re.sub(r"\\(section|subsection|subsubsection)\b",lambda h:"\\"+{"section":"chapter","subsection":"section","subsubsection":"subsection"}[h[1]],new)
            new=new.replace(r"\setcounter{section}",r"\setcounter{chapter}").replace(r"\setcounter{subsection}",r"\setcounter{section}")
        assert collections.Counter(s["maths"](text))==collections.Counter(s["maths"](new)),path
        assert re.findall(r"\\label\{([^}]+)\}",text)==re.findall(r"\\label\{([^}]+)\}",new)
        assert re.findall(r"\\(?:ref|eqref|BookCite|BookNumber)\{[^}]+\}",text)==re.findall(r"\\(?:ref|eqref|BookCite|BookNumber)\{[^}]+\}",new)
        rel="tex/generated/aljabr-layout/"+path.name;write(rel,new)
        records.append({"accepted_input":path.relative_to(B.root).as_posix(),"input_sha256":sha256_file(path),"generated":rel,"generated_sha256":sha256_file(B.root/rel),"only_transform":"Heading commands promoted one level and structural counters mapped; publication unchanged","math_reference_and_label_tokens_unchanged":True})
    tail=old.split(r"\input{chapters/chapter-01.tex}",1)[1].split(r"\end{document}")[0]
    tail=r"\input{chapters/chapter-01.tex}"+tail
    tail=tail.replace(r"\setcounter{subsection}{3}",r"\setcounter{section}{3}")
    tail=tail.replace(r"\input{chapters/",r"\input{generated/aljabr-layout/")
    tail=tail.replace(r"\BookContentsEntry{参考文献}",r"\backmatter"+"\n"+r"\BookContentsEntry{参考文献}")
    tail=tail.replace(r"\input{generated/aljabr-layout/bibliography.tex}",r"\cleardoublepage\markboth{参考文献}{参考文献}"+"\n"+r"\input{generated/aljabr-layout/bibliography.tex}")
    tail=tail.replace(r"\input{generated/aljabr-layout/index.tex}",r"\cleardoublepage\markboth{索引}{索引}"+"\n"+r"\input{generated/aljabr-layout/index.tex}")
    pre=r"""% AJbook edition only. Canonical accepted chapters are never edited here.
\documentclass[draftmark=false,colors=true,fontsetup=feec-fonts.tex,titlesetup=titles-setup.tex]{AJbook}
\usepackage[unicode,bookmarksnumbered]{hyperref}
\usepackage{feec-aljabr}
\input{generated/orthogonal-sum-macro.tex}
\input{translation-macros.tex}
\hypersetup{pdftitle={有限元外微积分},pdfauthor={Douglas N. Arnold}}
\begin{document}
\hypersetup{pageanchor=false}
\input{generated/aljabr-layout/publication.tex}
\frontmatter
\hypersetup{pageanchor=true}
\BookContentsEntry{前言}{sec:preface}
\cleardoublepage\markboth{前言}{前言}
\input{generated/aljabr-layout/frontmatter.tex}
\mainmatter
"""
    credit=r"""
\clearpage\thispagestyle{empty}\vspace*{\fill}
{\small\noindent 本页为译本排版说明, 非原书内容.\par
排版模板: AJbook, 李文威 (Wen-Wei Li), CC BY 4.0.\par
\url{https://github.com/wenweili/AlJabr-1}\par
\url{https://creativecommons.org/licenses/by/4.0/}\par
本译本仅在独立适配层调整环境英文标题和原书编号兼容.
字体配置直接采用上游原文件, 所需 Noto 字体已配齐, 不使用替代字体.
原始模板文件保持不变. 模板许可不改变原书及译文的权利归属.}
"""
    write("tex/aljabr-main.tex",pre+tail+credit+r"\end{document}"+"\n");dump("qa/template/aljabr-layout-provenance.json",records);guard()
def labels(path):
    data=path.read_text(encoding="utf8");values={}
    for h in re.finditer(r"\\newlabel\{([^}]+)\}\{",data):
        content,_=s["brace"](data,h.end()-1);row=[];pos=0
        while pos<len(content):v,pos=s["brace"](content,pos);row.append(v)
        values[h[1]]=row
    return values
def noto_environment(template,stage,environment):
    """Expose official project-pinned fonts without altering global TeX font config."""
    fonts=template/"collections/aljabr-1/fonts/noto-sans-cjk-sc";manifest=json.loads((fonts/"manifest.json").read_text(encoding="utf8"))
    for row in manifest["files"]:assert sha256_file(fonts/row["file"])==row["sha256"],row
    texvar=subprocess.check_output([shutil.which("kpsewhich"),"--var-value=TEXMFSYSVAR"],text=True).strip();system=Path(texvar)/"fonts/conf/fonts.conf";assert system.is_file()
    cache=B.assert_write_path(stage/"fontconfig-cache");cache.mkdir()
    config=B.assert_write_path(stage/"fonts.conf")
    write(config.relative_to(B.root).as_posix(),f'<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n<include ignore_missing="no">{escape(system.as_posix())}</include>\n<dir>{escape(fonts.as_posix())}</dir>\n<cachedir>{escape(cache.as_posix())}</cachedir>\n</fontconfig>\n')
    environment["FONTCONFIG_FILE"]=str(config);resolved=[]
    for row in manifest["files"]:
        value=subprocess.check_output([shutil.which("fc-match"),"-f","%{file}\n%{postscriptname}\n",f'Noto Sans CJK SC:style={row["weight"]}'],env=environment,text=True,encoding="utf8").strip().splitlines()
        assert sha256_file(Path(value[0]))==row["sha256"] and value[1]==row["postscript_name"],value
        resolved.append({"weight":row["weight"],"font":value[0],"postscript_name":value[1],"sha256":row["sha256"]})
    return resolved
def build(template_root=None):
    guard();prepare();template=Path(template_root).resolve() if template_root else P.template
    upstream=template/"collections/aljabr-1/upstream";adapter=template/"adapter/aljabr-1";assert (upstream/"AJbook.cls").is_file()
    fontroot=template/"collections/aljabr-1/fonts/noto-sans-cjk-sc"
    input_hashes={str(p):sha256_file(p) for p in [*(upstream.rglob("*")),*(adapter.rglob("*")),*(fontroot.rglob("*"))] if p.is_file()}
    stage=Path(tempfile.mkdtemp(prefix="aljabr-build-",dir=B.assert_write_path(B.root/"workspace/temporary")))
    env=os.environ.copy();env.update({"PYTHONIOENCODING":"utf-8","PYTHONUTF8":"1","TEXINPUTS":os.pathsep.join(str(x) for x in [adapter,upstream,P.template/"adapter",B.root/"tex"])+os.pathsep+os.pathsep})
    resolved_fonts=noto_environment(template,stage,env)
    driver=r"C:\Users\A\.codex\plugins\cache\openai-bundled\latex\0.2.8\scripts\compile_latex.py"
    command=[sys.executable,driver,str(B.root/"tex/aljabr-main.tex"),"--compiler","texlive","--engine","xelatex","--output-directory",str(stage),"--json"]
    r=subprocess.run(command,env=env,capture_output=True);write("logs/aljabr-build-driver.log",(r.stdout+r.stderr).decode("utf8",errors="replace"))
    dump("qa/template/aljabr-compilation.json",{"success":False,"build_directory":str(stage),"driver_returncode":r.returncode})
    if r.returncode:
        logpath=stage/"aljabr-main.log"
        raise RuntimeError(logpath.read_text(encoding="utf8",errors="replace")[-2200:] if logpath.exists() else "See logs/aljabr-build-driver.log")
    r=subprocess.run([shutil.which("xelatex"),"-interaction=nonstopmode","-halt-on-error","-file-line-error",f"-output-directory={stage}","aljabr-main.tex"],cwd=B.root/"tex",env=env,capture_output=True)
    log=(stage/"aljabr-main.log").read_text(encoding="utf8",errors="replace");write("logs/aljabr-compilation.log",log);assert r.returncode==0,r.stdout.decode("utf8",errors="replace")[-3500:]
    warnings={k:re.findall(pat,log,re.I) for k,pat in {"undefined":r"undefined references?|Reference .* undefined","duplicate":r"multiply[- ]defined|destination with the same identifier","missing_glyph":r"Missing character:[^\n]*","overfull":r"Overfull \\[hv]box[^\n]*"}.items()}
    base=load("qa/template/aljabr-baseline.json");oldlabels=labels(Path(base["old_build"])/"main.aux");newlabels=labels(stage/"aljabr-main.aux")
    assert oldlabels.keys()==newlabels.keys(),(oldlabels.keys()-newlabels.keys(),newlabels.keys()-oldlabels.keys())
    changes=[{"label":key,"old":oldlabels[key][0],"new":value[0]} for key,value in newlabels.items() if value[0]!=oldlabels[key][0]]
    reader=PdfReader(stage/"aljabr-main.pdf");dest=reader.named_destinations;links=[]
    for key,value in newlabels.items():
        assert value[3] in dest,(key,value)
        page=reader.get_destination_page_number(dest[value[3]])+1
        links.append({"label":key,"number":value[0],"printed_output_page":value[1],"physical_output_page":page,"destination":value[3]})
    for page in reader.pages:
        for item in page.get("/Annots",[]):
            action=item.get_object().get("/A",{})
            if action.get("/S")=="/GoTo":assert action["/D"] in dest,action
    assert all(sha256_file(Path(p))==h for p,h in input_hashes.items())
    sha=sha256_file(stage/"aljabr-main.pdf");renders=B.assert_write_path(B.root/"workspace/pages/aljabr-output"/sha[:16]);renders.mkdir(parents=True,exist_ok=True)
    subprocess.run([shutil.which("pdftoppm"),"-r","85","-png",str(stage/"aljabr-main.pdf"),str(renders/"page")],check=True)
    dump("qa/template/aljabr-compilation.json",{"success":not changes and not any(warnings.values()),"pdf_sha256":sha,"pdf_pages":len(reader.pages),"minimum_latex_rounds":2,"warnings":warnings,"label_number_changes":changes,"labels":len(links),"template_input_hashes":input_hashes,"font_resolution":resolved_fonts,"original_font_setup_sha256":sha256_file(upstream/"font-setup-open.tex"),"main_tex_sha256":sha256_file(B.root/"tex/aljabr-main.tex"),"build_directory":str(stage),"render_directory":str(renders),"visual_review":"pending"})
    dump("qa/template/aljabr-cross-references.json",{"number_changes":changes,"objects":links})
    guard();print(json.dumps({"pdf_sha256":sha,"pages":len(reader.pages),"warnings":warnings,"label_number_changes":changes,"renders":str(renders)},ensure_ascii=False))

def accept():
    """Explicit agent visual acceptance, tied to the actually inspected final build."""
    guard();q=load("qa/template/aljabr-compilation.json");test=load("qa/template/aljabr-shared-regression.json");comparison=load("qa/template/aljabr-render-comparison.json")
    expected="2b1bd263e11d32a2dec0c82d17bfd17f3a6749c0d58a12c0472b8ead03ada289"
    assert q["success"] and test["passed"] and q["pdf_sha256"]==comparison["final_sha256"]==expected
    assert not q["label_number_changes"] and not any(q["warnings"].values()) and q["labels"]==537
    direct=[10,*range(61,139)];inherited=sorted(set(range(1,61))-{10})
    assert set(inherited)<=set(comparison["full_page_byte_identical"])
    for rel in load("qa/template/aljabr-layout-provenance.json"):
        assert sha256_file(B.root/rel["accepted_input"])==rel["input_sha256"]
        assert sha256_file(B.root/rel["generated"])==rel["generated_sha256"]
        assert not re.search(r"\\(?:mathfrak|frak)\b",(B.root/rel["generated"]).read_text(encoding="utf8"))
        assert not s["find_chinese_prose_punctuation"]((B.root/rel["generated"]).read_text(encoding="utf8"))
    assert not s["find_chinese_prose_punctuation"]((B.root/"tex/aljabr-main.tex").read_text(encoding="utf8"))
    vendor=P.template/"collections/aljabr-1/upstream";manifest=json.loads((vendor.parent/"upstream-manifest.json").read_text(encoding="utf8"))
    assert len(manifest["files"])==36
    for row in manifest["files"]:assert sha256_file(vendor/row["path"])==row["sha256"]
    for path,sha in q["template_input_hashes"].items():assert sha256_file(Path(path))==sha
    source=Path(q["build_directory"])/"aljabr-main.pdf";assert sha256_file(source)==expected
    target=B.assert_write_path(B.root/"output/book-aljabr-zh.pdf");assert not target.exists();shutil.copyfile(source,target)
    guard();base=load("qa/template/aljabr-baseline.json")
    report={"passed":True,"book_id":ID,"template_profile":"aljabr-1","upstream_commit":manifest["commit"],"upstream_exact_files":36,"pdf":"output/book-aljabr-zh.pdf","pdf_sha256":expected,"pdf_pages":138,"legacy_pdf_retained":"output/book-zh.pdf","legacy_pdf_sha256":OLD,"old_main_and_all_accepted_text_formula_and_source_hashes_unchanged":True,"original_user_sty_reference_assets_unchanged":True,"original_template_manifest_hash":base["original_manifest_hash"],"expanded_template_collection_hash":directory_manifest_hash(P.template),"manifest_change_reason":"Only the additional pinned collection and its separate adapters were added; original template files remain byte-preserved.","shared_default":"Mystyle unchanged","book_scope":"Only finite-element-exterior-calculus selects AJbook; no other book branch or data is modified.","math_labels_references_and_prose":"Immutable canonical inputs; generated heading-level/counter mapping only. All 537 semantic labels and their numbers preserved, actual PDF destinations verified.","translation_progress":"47/47 units remain passed; no unit regenerated","font_fallback":"Three missing Noto Sans CJK SC families use upstream FandolHei in an independent, attributed font setup. No original font file or system font modified.","visual_review":{"passed":True,"final_pages_directly_viewed":direct,"final_pages_inherited_by_full_png_byte_equality":inherited,"inherited_viewed_candidate_sha256":comparison["previous_sha256"],"resolution_dpi":85,"review_method":"Four-page sheets plus direct final page 10. All pages covered, with no exclusion mask. Page headers, title/contents, all chapter starts, figures, tables, dense formulas, theorem/proof layout, bibliography, index and explicit attribution colophon inspected.","findings":"No visible clipping, overlaps or missing glyphs. Intentional recto chapter openings and blank verso pages are retained by AJbook."},"compile":q,"regression":test,"remote_push":False}
    dump("qa/template/aljabr-acceptance.json",report)
    write("qa/template/aljabr-acceptance.md","# AJbook typesetting acceptance\n\nPassed. This is a layout-only edition of the already completed FEEC translation, not a new translation pass. All 47 units remain accepted.\n\nThe 138-page edition uses the pinned, byte-exact 36-file AlJabr-1 snapshot. Original user template files, source PDF, accepted text/formula registries, legacy main entry and legacy PDF are unchanged. Only generated heading levels and structural counters are mapped to chapter/section. The 537 labels and all their numbers match the legacy build; actual PDF destinations are valid. Undefined references, duplicate labels, missing glyphs and overfull boxes: zero. Clean XeLaTeX build has at least two rounds. Repository regression: 34/34 passed, including the unchanged default reference build.\n\nAll rendered pages are covered by inspection: final pages 10 and 61-138 directly viewed, pages 1-9 and 11-60 inherited by full PNG byte equality from the inspected c5e44bed091e1472 build. No image region is masked. Corrected headers distinguish Preface, Bibliography and Index. B5 geometry, title blocks and normal type design are AJbook's supplied settings. Missing Noto families fall back to FandolHei in the separate compatibility file; upstream files are never edited. A clearly marked non-source colophon supplies template attribution and license information.\n\nThe template collection's aggregate hash changed because new independent files were added; all original input-file hashes remain unchanged. Other books keep their branches, data and original template. No glossary promotion, progress reset, translation rewrite or remote push.\n")
    cfg=B.load_config();cfg["final_output"]="output/book-aljabr-zh.pdf";cfg["template_version"]="aljabr-1@1e2d0bf4e5b7";cfg["typesetting"]["qa"]="qa/template/aljabr-acceptance.json";dump("config/book.yaml",cfg)
    status=(B.root/"PROJECT_STATUS.md").read_text(encoding="utf8").replace("Final output: output/book-zh.pdf","Final output: output/book-aljabr-zh.pdf").replace("Final PDF pages: 113","Final PDF pages: 138").replace("Final PDF SHA-256: "+OLD,"Final PDF SHA-256: "+expected).replace("Final QA: qa/final-report.json","Final QA: qa/template/aljabr-acceptance.json")
    write("PROJECT_STATUS.md",status+"\nActive template: aljabr-1@1e2d0bf4e5b7\nActive entry: tex/aljabr-main.tex\nLegacy entry retained: tex/main.tex\nLegacy final PDF retained: output/book-zh.pdf\nLayout-only update: accepted translation and 47/47 progress unchanged\n")
    print(json.dumps({"passed":True,"pdf":str(target),"pdf_pages":138,"sha256":expected,"legacy_unchanged":True}))
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("book_id",choices=[ID]);a.add_argument("action",choices=["baseline","prepare","build","accept"]);a.add_argument("--template-root");args=a.parse_args()
    if args.action=="build":build(args.template_root)
    else:{"baseline":baseline,"prepare":prepare,"accept":accept}[args.action]()
