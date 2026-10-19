"""Render original Chapter 3 figures, with book-local provenance and hash guards."""
import runpy,shutil,subprocess
from pathlib import Path
from pypdf import PdfReader

m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
B=m["B"];m["guard"]()
figures=[("bicg-bicr-near-symmetric",121,[53,54,389,257]),
         ("bicg-bicr-far-symmetric",122,[53,54,389,257]),
         ("gmres-restarts",128,[53,54,389,252]),
         ("product-methods-moderate",142,[53,54,389,255]),
         ("product-methods-difficult",143,[53,54,389,255]),
         ("idr-comparison",151,[53,331,389,529])]
records=[];source=PdfReader(B.require_source_pdf())
for name,page,box in figures:
    target=B.assert_write_path(B.root/f"tex/figures/{name}.png")
    target.parent.mkdir(parents=True,exist_ok=True)
    x0,y0,x1,y1=box
    subprocess.run([shutil.which("pdftoppm"),"-f",str(page),"-l",str(page),"-r","216","-singlefile","-png",
        "-x",str(x0*3),"-y",str(y0*3),"-W",str((x1-x0)*3),"-H",str((y1-y0)*3),str(B.require_source_pdf()),str(target.with_suffix(""))],check=True)
    records.append({"name":name,"pdf_page":page,"printed_page":source.page_labels[page-1],"bbox":box,
        "path":str(target.relative_to(B.root)),"operation":"render original source plot without changing curves, values or labels; caption translated separately"})
m["dump"]("qa/source/chapter-03-figure-provenance.json",records);m["guard"]()
