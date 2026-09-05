# Chapter I. Stokes 问题的数学基础

## §1. 某些椭圆边值问题的一般论述

本节简要概述调和算子与双调和算子的 Dirichlet 问题和 Neumann 问题.

### 1.1. Sobolev 空间的基本概念

这里的目的是回顾后文将要使用的经典 Sobolev 空间的主要概念和结果. 尽管这里只陈述而不证明, 这些结果仍是完整的, 严格的并且相当一般. 其中有些结果, 例如迹定理, 在后续证明中只会作为理论工具发挥较小的作用, 不熟悉这类专门数学内容的读者不必在此深究. 但另一些结果, 例如 Sobolev 嵌入定理, 将会反复使用. 读者可以在 Nečas [58] 或 Adams [1] 等参考文献中找到更多细节.

为简化讨论, 从现在起我们将使用实值函数, 但这里陈述的每个结果当然也都适用于复值函数.

设 $\Omega$ 是 $\mathbb R^N$ 的一个开子集, 其边界为 $\Gamma$. 定义 $\mathcal D(\Omega)$ 为在 $\Omega$ 上具有紧支集的无穷次可微函数所成的线性空间. 然后令

$$
\mathcal D(\Omega)=\{\phi|_\Omega;\ \phi\in\mathcal D(\mathbb R^N)\},
$$

或者等价地, 若 $\mathcal O$ 表示 $\mathbb R^N$ 中满足 $\bar\Omega\subset\mathcal O$ 的任一开子集, 则

$$
\mathcal D(\bar\Omega)=\{\phi|_\Omega;\ \phi\in\mathcal D(\mathcal O)\}.
$$

现在, 令 $\mathcal D'(\Omega)$ 表示 $\mathcal D(\Omega)$ 的对偶空间, 通常称为 $\Omega$ 上的分布空间. 用 $\langle\cdot,\cdot\rangle$ 表示 $\mathcal D'(\Omega)$ 与 $\mathcal D(\Omega)$ 之间的对偶配对. 注意, 当 $f$ 是局部可积函数时, 可以借助下式把 $f$ 与一个分布等同:

$$
\langle f,\phi\rangle=\int_\Omega f(x)\phi(x)\,dx\qquad\forall\phi\in\mathcal D(\Omega).
$$

换言之, $\langle\cdot,\cdot\rangle$ 是 $L^2(\Omega)$ 标量积的一个延拓. 现在可以定义分布的导数. 令 $\alpha=(\alpha_1,\ldots,\alpha_N)\in\mathbb N^N$, 并置

$$
|\alpha|=\sum_{i=1}^N\alpha_i.
$$

对 $\mathcal D'(\Omega)$ 中的 $u$, 按下式在 $\mathcal D'(\Omega)$ 中定义 $\partial^\alpha u$:

$$
\langle\partial^\alpha u,\phi\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha\phi\rangle
\qquad\forall\phi\in\mathcal D(\Omega);
$$

当 $u$ 可作 $\alpha$ 次微分时, $\partial^\alpha u$ 与通常意义下的导数一致:

$$
\partial^\alpha u=
\frac{\partial^{|\alpha|}u}
{\partial x_1^{\alpha_1}\cdots\partial x_N^{\alpha_N}}.
$$

对每个整数 $m\geq0$ 以及满足 $1\leq p\leq\infty$ 的实数 $p$, 定义 Sobolev 空间:

$$
W^{m,p}(\Omega)=\{v\in L^p(\Omega);\ \partial^\alpha v\in L^p(\Omega)\quad\forall|\alpha|\leq m\}.
$$

它关于下列范数是 Banach 空间:

$$
\|u\|_{m,p,\Omega}=\left(\sum_{|\alpha|\leq m}\int_\Omega|\partial^\alpha u(x)|^p\,dx\right)^{1/p}
\qquad p<\infty. \tag{1.1}
$$

或者

$$
\|u\|_{m,\infty,\Omega}=\max_{|\alpha|\leq m}\left(\operatorname*{ess\,sup}_{x\in\Omega}|\partial^\alpha u(x)|\right),
\qquad p=\infty.
$$

当 $1\leq p<\infty$ 时, 空间 $W^{m,p}(\Omega)$ 是可分的; 当 $1<p<\infty$ 时, 它是自反的. 还在 $W^{m,p}(\Omega)$ 上赋予如下半范数:

$$
|u|_{m,p,\Omega}=\left(\sum_{|\alpha|=m}\int_\Omega|\partial^\alpha u(x)|^p\,dx\right)^{1/p},
\qquad\text{for }p<\infty. \tag{1.2}
$$

当 $p=\infty$ 时作上述相应修改. 如果对 $\Omega$ 的每个可测的紧真子集 $\mathcal O$, 函数 $u$ 都属于 $W^{m,p}(\mathcal O)$, 则称 $u$ 局部属于 $W^{m,p}(\Omega)$, 并写成

$$
u\in W^{m,p}_{\mathrm{loc}}(\Omega).
$$

当 $p=2$ 时, $W^{m,2}(\Omega)$ 通常记作 $H^m(\Omega)$. 如果不存在歧义, 在提及其范数和半范数时省略下标 $p=2$. 关于如下标量积, $H^m(\Omega)$ 是 Hilbert 空间:

$$
(u,v)_{m,\Omega}=\sum_{|\alpha|\leq m}\int_\Omega\partial^\alpha u(x)\partial^\alpha v(x)\,dx. \tag{1.3}
$$

特别地, 书写 $L^2(\Omega)$ 的标量积时完全省略下标.

与 Sobolev 空间相对应, 下面回顾熟知的 $\mathcal C^m$ 函数定义:

$\mathcal C^0(\Omega)$ 表示定义在 $\Omega$ 上的连续函数空间, 并且

$$
\mathcal C^m(\Omega)=\{u\in\mathcal C^0(\Omega);\ \partial^\alpha u\in\mathcal C^0(\Omega)\quad\forall|\alpha|\leq m\}.
$$

由于 $\mathcal C^m$ 函数未必有界, 还引入空间

$$
\mathcal C^m(\bar\Omega)=\{u\in\mathcal C^m(\Omega);\ \partial^\alpha u\text{ 在 }\Omega\text{ 上有界且一致连续}
\quad\forall0\leq|\alpha|\leq m\}.
$$

类似地, 定义空间 $\mathcal C^{m,1}(\bar\Omega)$:

$$
\mathcal C^{m,1}(\bar\Omega)=\{u\in\mathcal C^m(\bar\Omega);\ \partial^\alpha u\text{ 在 }\bar\Omega\text{ 上是 Lipschitz 连续的}
\quad\forall0\leq|\alpha|\leq m\}.
$$

对 $m\geq0$, $\mathcal C^m(\bar\Omega)$ 和 $\mathcal C^{m,1}(\bar\Omega)$ 关于各自的下列范数是 Banach 空间:

$$
\|u\|_{\mathcal C^m(\bar\Omega)}=
\max_{0\leq|\alpha|\leq m}\sup_{x\in\Omega}|\partial^\alpha u(x)|,
$$

$$
\|u\|_{\mathcal C^{m,1}(\bar\Omega)}=
\|u\|_{\mathcal C^m(\bar\Omega)}+
\max_{0\leq|\alpha|\leq m}\sup_{\substack{x,y\in\Omega\\x\neq y}}
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|}{\|x-y\|},
$$

其中 $\|x\|$ 表示 $\mathbb R^N$ 的 Euclidean 范数.

由于 $\mathcal D(\Omega)\subset W^{m,p}(\Omega)$, 定义

$$
W_0^{m,p}(\Omega)=\overline{\mathcal D(\Omega)}^{W^{m,p}(\Omega)}.
$$

也就是说, $W_0^{m,p}(\Omega)$ 是 $\mathcal D(\Omega)$ 关于范数 $\|\cdot\|_{m,p,\Omega}$ 的闭包. 当 $m\geq1$ 且 $\Omega$ 是 $\mathbb R^N$ 的真子集时, $W_0^{m,p}(\Omega)$ 通常是 $W^{m,p}(\Omega)$ 的真子空间, 后文将进一步刻画其中的函数. 另一方面, 当 $m=0$ 时有如下结果.

**Lemma 1.1.** *当 $1\leq p<\infty$ 时, 空间 $\mathcal D(\Omega)$ 在 $L^p(\Omega)$ 中稠密.*

下一个 Theorem 称为 Poincaré-Friedrichs 不等式. 它断言映射 $v\mapsto|v|_{m,\Omega}$ 是 $H_0^m(\Omega)$ 上的一个范数, 并且与 $\|\cdot\|_{m,\Omega}$ 等价.

**Theorem 1.1.** *如果 $\Omega$ 连通并且至少沿一个方向有界, 那么对每个整数 $m\geq0$, 存在常数 $K=K(m,\Omega)>0$, 使得*

$$
\|v\|_{m,\Omega}\leq K|v|_{m,\Omega}qquad\forall v\in H_0^m(\Omega). \tag{1.4}
$$

对 $1\leq p<\infty$, 用 $W^{-m,p'}(\Omega)$ 表示 $W_0^{m,p}(\Omega)$ 的对偶空间, 其范数定义为:

$$
\|f\|_{-m,p',\Omega}=
\sup_{\substack{v\in W_0^{m,p}(\Omega)\\v\neq0}}
\frac{\langle f,v\rangle}{\|v\|_{m,p,\Omega}}, \tag{1.5}
$$

其中 $p'$ 满足

$$
\frac1p+\frac1{p'}=1. \tag{1.6}
$$

下一个 Lemma 刻画 $W^{-m,p'}(\Omega)$ 的泛函.

**Lemma 1.2.** *设 $p$ 和 $p'$ 满足 (1.6), 且 $1\leq p<\infty$. 分布 $f$ 属于 $W^{-m,p'}(\Omega)$ 当且仅当存在函数 $f_\alpha\in L^{p'}(\Omega)$, $|\alpha|\leq m$, 使得*

$$
f=\sum_{|\alpha|\leq m}\partial^\alpha f_\alpha.
$$

定义域 $\Omega$ 上 Sobolev 空间的几乎所有性质都要求边界 $\Gamma$ 具有一定的正则性. 精确定义这一正则性概念十分重要. 下述 Definition 取自 Grisvard [42].

**Definition 1.1.** 设 $\Omega$ 是 $\mathbb R^N$ 的开子集. 如果对每个 $x\in\Gamma$, 都存在 $x$ 在 $\mathbb R^N$ 中的一个邻域 $\mathcal O$ 以及新的正交坐标 $y=(y',y_N)$, 其中 $y'=(y_1,\ldots,y_{N-1})$, 使得:

i) 在新坐标中, $\mathcal O$ 是超立方体:

$$
\mathcal O=\{y;\ -a_j<y_j<a_j,\ 1\leq j\leq N\}.
$$

ii) 存在定义在

$$
\mathcal O'=\{y';\ -a_j<y_j<a_j,\ 1\leq j\leq N-1\}
$$

上的连续函数(相应地为 Lipschitz 连续函数, $\mathcal C^m$ 函数或 $\mathcal C^{m,1}$ 函数) $\phi$, 满足:

$$
|\phi(y')|\leq a_N/2\qquad\forall y'\in\mathcal O',
$$

$$
\Omega\cap\mathcal O=\{y;\ y_N<\phi(y')\},
\qquad
\Gamma\cap\mathcal O=\{y;\ y_N=\phi(y')\}.
$$

则称 $\Omega$ 的边界 $\Gamma$ 是连续的(相应地为 Lipschitz 连续的, $\mathcal C^m$ 类的, 或对某个整数 $m>0$ 为 $\mathcal C^{m,1}$ 类的).

从本质上说, 该定义意味着局部地 $\Omega$ 位于某个函数 $\phi$ 的图像下方, $\Gamma$ 由 $\phi$ 的图像表示, 而 $\Gamma$ 的正则性由 $\phi$ 的正则性确定. 需要指出的是, 按照这个定义, 具有连续边界的定义域在 $\Gamma$ 的任一点都不会位于 $\Gamma$ 的两侧. 特别地, 不允许有割缝或尖点的定义域, 但允许边界带有角点. 具有 Lipschitz 连续边界的定义域最直接的例子是 $\mathbb R^3$ 中的有界多面体或 $\mathbb R^2$ 中的有界多边形.

为简化文字, 当 $\Omega$ 具有 Lipschitz 连续边界时, 称 $\Omega$ 是 Lipschitz 连续的.

注意, Lipschitz 连续边界几乎处处具有单位法向量 $\mathbf n$. 此外, 对 $m\geq1$, $\mathcal C^{m,1}$ 类边界 $\Gamma$ 的法向量属于 $\mathcal C^{m-1,1}(\Gamma)^N$; 如果 $\Omega$ 有界, 则该法向量可以延拓为属于 $\mathcal C^{m-1,1}(\bar\Omega)^N$ 的向量场. 类似地, 如果 $\Omega$ 是具有 Lipschitz 连续边界 $\Gamma$ 的有界定义域, 则距离函数

$$
d(x,\Gamma)=\inf_{y\in\Gamma}\|x-y\|
$$

属于 $W^{1,\infty}(\Omega)$.

下一个 Theorem 表明光滑函数在 $W^{m,p}(\Omega)$ 中稠密.
