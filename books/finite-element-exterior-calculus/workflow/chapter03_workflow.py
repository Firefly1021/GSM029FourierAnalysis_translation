"""Guarded staging for the complete, manually source-verified Chapter 3."""
import argparse,csv,re,runpy
from pathlib import Path
m=runpy.run_path(str(Path(__file__).with_name("full_workflow.py")))
P,B,ID=m["P"],m["B"],m["ID"]
UNITS=["chapter-03-introduction"]+[f"chapter-03-section-{i:02}" for i in range(1,5)]
NOTES={
UNITS[0]:{"names":["Hilbert","Banach","de Rham"],"terms":[],"source_pages":[31],"source_observations":[]},
UNITS[1]:{"names":["Hilbert","Sobolev"],"terms":[["unbounded operator","无界算子","functional analysis","linear map with possibly proper domain, not necessarily unbounded"],["densely defined","稠密定义","functional analysis","operator domain is dense in its ambient space"],["graph norm","图范数","functional analysis","square root of squared domain norm plus squared image norm"]],"source_pages":[31,32],"source_observations":[{"pdf_page":32,"message":"The source prints 'restriction to T(D) of the X norm'. Preserve T(D) rather than silently changing it to D(T)."}]},
UNITS[2]:{"names":["Hilbert","Banach","Cauchy"],"terms":[["closed operator","闭算子","functional analysis","operator whose graph is closed in the product space"]],"source_pages":[32,33],"source_observations":[]},
UNITS[3]:{"names":["Riesz","Hilbert","Banach","Cauchy"],"terms":[["adjoint","伴随","functional analysis","adjoint of a densely defined linear operator"],["rotated graph","旋转图","functional analysis","graph of the adjoint with swapped components and a sign"],["closed range theorem","闭值域定理","functional analysis","range closed for an operator exactly when closed for its adjoint"],["finite codimensional","有限余维","functional analysis","finite-dimensional quotient by an operator range"]],"source_pages":[33,34,35,36,37],"source_observations":[]},
UNITS[4]:{"names":["de Rham","Hilbert","Sobolev","Lipschitz","Neumann"],"terms":[["normal trace","法向迹","Sobolev spaces","gamma_n maps H(div) to H^(-1/2) of the boundary"],["tangential trace","切向迹","Sobolev spaces","gamma_tau extends the cross product of boundary value and normal"],["annihilator","零化子","functional analysis","dual functionals vanishing on a subspace"],["mollification","磨光","functional analysis","argument used for smooth density in H(curl)"]],"source_pages":[37,38,39,40,41,42],"source_observations":[{"pdf_page":38,"message":"Lemma 3.10 is stated for normed linear spaces without an explicit completeness or open-mapping hypothesis. Preserve the source's stated assumptions; do not add Banach-space assumptions to the translation."},{"pdf_page":39,"message":"The source uses R^3 in the classical normal trace discussion and Theorem 3.12 after beginning the section with a domain in R^n. Preserve each printed dimension, not silently normalize n and 3."},{"pdf_page":41,"message":"The source uses gamma_tau w in the restriction paragraph but v in the following smoothness sentence. Preserve these source letters exactly."},{"pdf_page":42,"message":"Box 3.1 floats above the concluding main text on the original page. In the translation it follows the completed section; all summary and main-text content is retained."}]}
}

def prepare():
    m["guard"]();progress=list(csv.DictReader(B.chapter_progress.open(encoding="utf8"),delimiter="\t"))
    for unit in UNITS:
        assert next(x for x in progress if x["Unit ID"]==unit)["QA Status"]!="passed"
        rel=f"translation/authored/{unit}.bilingual.tex";path=B.assert_write_path(B.root/rel)
        text=path.read_text(encoding="utf8").replace("、",", ").replace(r"\ref*{bib:source-",r"\BookNumber{")
        for env in ("Theorem","Definition","Lemma","Proposition","Corollary","Example","Remark","Exercise"):
            marker="\\Needspace{6\\baselineskip}\n\\begin{"+env+"}"
            text=text.replace(marker,"\\begin{"+env+"}").replace("\\begin{"+env+"}",marker)
        text=text.replace(r"\begin{Theorem}[\BT{closed range theorem}{闭值域定理}]",r"\begin{Theorem}{\BT{closed range theorem}{闭值域定理}}")
        text=text.replace("}\n\n% block: graph-norm-footnote","}%\n% block: graph-norm-footnote")
        text=text.replace("线性算子; $D(T)$ 称为 $T$ 的定义域.","线性算子, 其中该子空间称为 $T$ 的定义域.")
        text=text.replace("无界算子 $T$ 的\\emph{零空间}, \\emph{像空间}和\\emph{图}","无界算子 $T$ 的\\emph{零空间}, $T$ 的\\emph{像空间}和 $T$ 的\\emph{图}")
        text=text.replace("元素 $(x,w)\\in X\\times Y$ 属于", "$X\\times Y$ 中的元素 $(x,w)$ 属于")
        text=text.replace("对所有 $v\\in D(T)=D(\\overline T)$ 有", "对 $D(T)=D(\\overline T)$ 中的所有 $v$ 有")
        text=text.replace("满足 $Tx_n$ 在 $Y$ 中趋于 $y$", "满足在 $Y$ 中有 $Tx_n\\to y$")
        text=text.replace("将此引理用于迹算子 $\\gamma=\\operatorname{tr}:H^1(\\Omega)\\to H^{1/2}(\\partial\\Omega)$", "将此引理用于 $\\gamma$ 等于迹算子 $\\operatorname{tr}:H^1(\\Omega)\\to H^{1/2}(\\partial\\Omega)$ 的情形")
        text=text.replace("对 $u\\in C_0^\\infty(\\Omega)$ 有 $L_w(u)=0$, 从而由稠密性, 对 $u\\in\\mathring H^1(\\Omega)$ 也有 $L_w(u)=0$", "对 $u\\in C_0^\\infty(\\Omega)$, $L_w(u)$ 为零, 从而由稠密性, 对 $u\\in\\mathring H^1(\\Omega)$ 也为零")
        text=text.replace("从 Hilbert 空间 $X$ 到另一个 Hilbert 空间 $Y$", "从 Hilbert 空间 $X$ 到另一个空间 $Y$")
        m["write"](rel,text);m["dump"](f"translation/authored/{unit}-notes.json",NOTES[unit]);m["metadata"](unit)
        en=m["s"]["language"](text,0);zh=m["s"]["language"](text,1)
        names={x["Source Form"] for x in csv.DictReader(B.proper_names.open(encoding="utf8"),delimiter="\t")}|{n for note in NOTES.values() for n in note["names"]}
        for name in names:
            pat=r"(?<![A-Za-z])"+re.escape(name)+r"(?![A-Za-z])"
            assert len(re.findall(pat,en))==len(re.findall(pat,zh)),(unit,name)
        assert not m["s"]["find_chinese_prose_punctuation"](zh)
    m["assemble"]();m["guard"]()

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("book_id",choices=[ID]);p.parse_args();prepare()
