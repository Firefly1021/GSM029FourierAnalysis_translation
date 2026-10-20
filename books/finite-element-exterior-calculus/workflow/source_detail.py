"""Render a guarded source-PDF region at 400 dpi without altering source bytes."""
import argparse,runpy,subprocess,shutil
from pathlib import Path
w=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[w["ID"]]);p.add_argument("page",type=int);p.add_argument("name");p.add_argument("bbox",nargs=4,type=float);a=p.parse_args();w["guard"]()
    assert all(c.isalnum() or c in "-_" for c in a.name)
    out=w["B"].assert_write_path(w["B"].root/"workspace/pages/source-crops"/a.name);out.parent.mkdir(parents=True,exist_ok=True)
    x0,y0,x1,y1=a.bbox;assert 0<=x0<x1<=486 and 0<=y0<y1<=711
    scale=400/72
    subprocess.run([shutil.which("pdftoppm"),"-f",str(a.page),"-l",str(a.page),"-r","400","-x",str(round(x0*scale)),"-y",str(round(y0*scale)),"-W",str(round((x1-x0)*scale)),"-H",str(round((y1-y0)*scale)),"-singlefile","-png",str(w["B"].require_source_pdf()),str(out)],check=True)
    w["guard"]();print(out.with_suffix(".png"))
