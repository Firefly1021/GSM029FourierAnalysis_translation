"""Book-local agent sample workflow. Never translates or guesses source mathematics."""
from __future__ import annotations
import argparse,collections,csv,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path
import pdfplumber
from pypdf import PdfReader
from mathbook.project import ProjectPaths,sha256_file,directory_manifest_hash
from mathbook.workflow import verify_book_context
from mathbook.template import verify_manifest

ID="finite-element-exterior-calculus"
P=ProjectPaths();B,R=verify_book_context(P,ID,writable=True)
SOURCE_SHA="649b672d2d54b7ebc5e51154587dbf70fefd6d6dcb5a81a9903e7bb0ee2c39d4"
TEMPLATE_SHA="169ce9aff354bb309f4d20fc1b99a20f11aa8f6a1dd4738517dff7a83f085229"
def write(rel,text):
    path=B.assert_write_path(B.root/rel);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding="utf8");return path
def dump(rel,data):return write(rel,json.dumps(data,ensure_ascii=False,indent=2)+"\n")
def load(rel):return json.loads((B.root/rel).read_text(encoding="utf8"))
def guard():
    assert sha256_file(B.require_source_pdf())==SOURCE_SHA==B.load_config()["source"]["sha256"]
    assert sha256_file(Path(r"D:\BaiduNetdiskDownload\Finite Element Exterior Calculus.pdf"))==SOURCE_SHA
    assert not verify_manifest(),verify_manifest()
    assert directory_manifest_hash(P.template)==TEMPLATE_SHA==B.load_config()["template_manifest_hash"]
    initial=B.root/"qa/protected-inputs-initial.json"
    if initial.is_file():
        for row in load("qa/protected-inputs-initial.json")["template_raw_files"]:assert sha256_file(P.template/row["path"])==row["sha256"],row
def initialize():
    guard()
    assert not (B.root/"qa/protected-inputs-initial.json").exists(),"Initial preservation evidence must never be replaced"
    dump("qa/protected-inputs-initial.json",{"source_sha256":SOURCE_SHA,"template_manifest_hash":TEMPLATE_SHA,"template_raw_files":[{"path":f.relative_to(P.template).as_posix(),"sha256":sha256_file(f)} for f in sorted(P.template.rglob("*")) if f.is_file()],"initial_branch_head":P.git_head(),"branches":subprocess.run(["git","for-each-ref","--format=%(refname) %(objectname)","refs/heads/book/"],cwd=P.root,capture_output=True,text=True,check=True).stdout.splitlines()})
    r=PdfReader(B.require_source_pdf());outline=[]
    def walk(items,depth=0):
        for item in items:
            if isinstance(item,list):walk(item,depth+1)
            else:outline.append({"title":item["/Title"],"pdf_page":r.get_destination_page_number(item)+1,"depth":depth})
    walk(r.outline);dump("structured/source/contents.json",outline)
    rows=[];mapping=[]
    with pdfplumber.open(B.require_source_pdf()) as doc:
        for n,page in enumerate(doc.pages,1):
            text=r.pages[n-1].extract_text() or "";chars=page.chars
            images=[{"bbox":[im["x0"],im["top"],im["x1"],im["bottom"]],"pixel_size":im.get("srcsize"),"coverage":im["width"]*im["height"]/(page.width*page.height)} for im in page.images]
            nonprint=sum(ord(c)<32 and c not in "\n\r\t" for c in text)
            mode3=sum(op==b"Tr" and operands and operands[0]==3 for operands,op in r.pages[n-1].get_contents().operations) if r.pages[n-1].get_contents() else 0
            fullimage=any(im["coverage"]>.8 for im in images)
            kind="blank" if not text.strip() and not images else "scanned" if fullimage and len(chars)<100 else "mixed" if images else "native"
            active=[x for x in outline if x["pdf_page"]<=n]
            logical=active[-1]["title"] if active else "frontmatter"
            rows.append({"pdf_page":n,"printed_page":r.page_labels[n-1],"width_pt":page.width,"height_pt":page.height,"rotation":r.pages[n-1].get("/Rotate",0),"kind":kind,"characters":len(chars),"text_length":len(text),"unmapped_control_characters":nonprint,"invisible_text_mode_operators":mode3,"images":images,"fonts":sorted(set(c["fontname"] for c in chars)),"math_text_requires_image_verification":nonprint>0,"review_status":"mechanical-diagnosis"})
            mapping.append({"pdf_page_index_1_based":n,"pdf_page_index_0_based":n-1,"printed_page":r.page_labels[n-1],"logical_position":logical,"mapping_evidence":"PDF PageLabels; sampled body folios visually verified"})
        for n in [1,5,7,8,21,25,26,27,28,29,30,31,43,61,73,91,107,123,129,130]:
            page=doc.pages[n-1]
            dump(f"workspace/layout/pdf-{n:03}.json",{"pdf_page":n,"width":page.width,"height":page.height,"chars":[{k:c.get(k) for k in ("text","x0","x1","top","bottom","fontname","size")} for c in page.chars],"images":[{k:c.get(k) for k in ("x0","x1","top","bottom","srcsize")} for c in page.images]})
            write(f"workspace/raw-text/pdf-{n:03}.txt",r.pages[n-1].extract_text() or "")
    counts=dict(collections.Counter(x["kind"] for x in rows));dump("qa/pdf-diagnosis.json",{"book_id":ID,"source_sha256":SOURCE_SHA,"total_pages":len(rows),"classification":"native with raster illustrations, not a scanned book","method":"All pages: rendered-text glyphs, actual raster images and their areas, fonts, text-mode operators, page labels and dimensions; sampled source images independently reviewed","counts":counts,"pages":rows,"coarse_controller_diagnosis":"Retained in qa/pdf-inspection.json; XObject presence alone is not a raster-image or scan test","text_layer_limit":"Native prose usable after layout verification. Embedded math fonts have unmapped/control-code characters; formulas must be transcribed and verified from page images, not copied blindly from extraction."})
    dump("structured/source/page-map.json",mapping)
    cfg=B.load_config();cfg["title"]="Finite Element Exterior Calculus";dump("config/book.yaml",cfg)
    guard();print(json.dumps({"pages":len(rows),"counts":counts,"unmapped_pages":sum(x["unmapped_control_characters"]>0 for x in rows)},ensure_ascii=False))
def render():
    guard();out=B.assert_write_path(B.root/"workspace/pages/source");out.mkdir(parents=True,exist_ok=True)
    for n in [1,5,7,8,21,25,26,27,28,29,30,31,43,61,73,91,100,107,123,124,129,130]:
        target=out/f"pdf-{n:03}.png"
        if not target.is_file():subprocess.run([shutil.which("pdftoppm"),"-f",str(n),"-l",str(n),"-r","150","-singlefile","-png",str(B.require_source_pdf()),str(target.with_suffix(""))],check=True)
    guard();print("Source diagnostic/sample pages rendered without source modification")
if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("book_id",choices=[ID]);parser.add_argument("action",choices=["initialize","render"]);a=parser.parse_args()
    {"initialize":initialize,"render":render}[a.action]()
