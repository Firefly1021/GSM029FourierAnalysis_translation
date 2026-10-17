"""Lossless source provenance and rendered figure derivatives for Chapter 2."""
import runpy
import subprocess,shutil
from pypdf import PdfReader
from pathlib import Path

m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
B=m["B"]
m["guard"]()
figures=[
 ("laplace-grid",45,[240,396,389,534]),
 ("helmholtz-grid",51,[265,57,389,172]),
 ("helmholtz-ghost-grid",51,[244,181,389,322]),
 ("poisson-domain",55,[234,56,389,194]),
 ("triangular-domain-decomposition",57,[249,56,389,182]),
 ("triangle-node-order",57,[250,188,389,294]),
 ("square-poisson-domain",59,[240,425,389,557]),
 ("eight-triangle-mesh",60,[244,57,389,197]),
 ("two-triangle-types",60,[225,205,389,310]),
 ("regression-data",69,[241,57,389,177]),
 ("regression-fit",70,[53,56,385,196]),
 ("regularized-regression-fit",72,[53,55,385,201]),
 ("classification-result",75,[53,55,385,186]),
]
records=[]
source=PdfReader(B.require_source_pdf())
if source:
    for name,page,box in figures:
        target=B.assert_write_path(B.root/f"tex/figures/{name}.png")
        target.parent.mkdir(parents=True,exist_ok=True)
        x0,y0,x1,y1=box
        subprocess.run([shutil.which("pdftoppm"),"-f",str(page),"-l",str(page),"-r","216","-singlefile","-png",
            "-x",str(x0*3),"-y",str(y0*3),"-W",str((x1-x0)*3),"-H",str((y1-y0)*3),
            str(B.require_source_pdf()),str(target.with_suffix(""))],check=True)
        records.append({"name":name,"pdf_page":page,"printed_page":source.page_labels[page-1],"bbox":box,"path":str(target.relative_to(B.root)),"operation":"render original source figure, unchanged labels; caption translated separately"})
m["dump"]("qa/source/chapter-02-figure-provenance.json",records)
m["guard"]()
