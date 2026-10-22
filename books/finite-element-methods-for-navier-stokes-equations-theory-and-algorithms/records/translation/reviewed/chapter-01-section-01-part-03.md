<!-- PDF page 23 / printed page 9 -->

除了边界值算子 $\gamma_0$ 以外, 还需要法向导数的迹 $\gamma_1u$. 对 $\mathcal D(\bar\Omega)$ 中的 $u$, 它定义为

$$
\gamma_1u=\partial u/\partial n=\sum_{i=1}^N\gamma_0(\partial u/\partial x_i)n_i. \tag{1.18}
$$

其中 $\mathbf n=(n_1,\ldots,n_N)$ 表示 $\Gamma$ 的单位外法向量. 于是可以如下补充 Theorem 1.5 的陈述.

**Theorem 1.6.** *保持 Theorem 1.5 的假设, 并令 $l\geq1$. 定义在 $\mathcal D(\bar\Omega)$ 上的映射*

$$
u\mapsto\{\gamma_0u,\gamma_1u\}
$$

*存在唯一的线性连续延拓, 该延拓是从下列空间到下列空间的满射算子:*

$$
W^{s,p}(\Omega)\quad\text{onto }W^{s-1/p,p}(\Gamma)\times W^{s-1-1/p,p}(\Gamma).
$$

*此外, 在 $W^{2,p}(\Omega)$ 中有如下刻画:*

$$
\operatorname{Ker}\gamma_0\cap\operatorname{Ker}\gamma_1=W_0^{2,p}(\Omega).
$$

**Remark 1.1.** 如果 $\Omega$ 的边界有角点, 它的法向量会发生跳跃, 因而无论 $u$ 多么光滑, $\partial u/\partial n$ 显然都会比较粗糙. 尽管如此, 仍可将 Theorem 1.6 的陈述略作推广. 假设 $\Omega$ 是有界二维多边形; 以 $\Gamma_j$ 表示 $\Gamma$ 的各条边, 以 $\mathbf n_j$ 表示相应的单位外法向量, $1\leq j\leq J$. 则映射

$$
u\mapsto(\partial u/\partial n_j;\ 1\leq j\leq J)
$$

是从 $W^{k+2,p}(\Omega)$ 到

$$
\prod_{j=1}^J W^{k+1-1/p,p}(\Gamma_j)
$$

的线性连续满射, 其中 $k\geq0$ 是任意整数, $p\in(1,\infty)$ 是任意实数. 注意, $\partial u/\partial n$ 在 $\Gamma$ 的顶点处没有匹配条件.

$u$ 的边界值的情形稍微复杂一些, 因为在 $\Gamma$ 的顶点处通常存在匹配条件. 为简单起见, 只取 $u\in W^{2,p}(\Omega)$. 以 $S_j$ 表示 $\Gamma$ 的顶点, 并约定 $S_{J+1}=S_1$. 映射

$$
u\mapsto(h_j=u|_{\Gamma_j};\ 1\leq j\leq J)
$$

是从 $W^{2,p}(\Omega)$ 到

$$
\prod_{j=1}^J W^{2-1/p,p}(\Gamma_j)
$$

中由下列相容条件确定的子空间的线性连续满射:

$$
h_j(S_{j+1})=h_{j+1}(S_{j+1}),\qquad1\leq j\leq J.
$$

<!-- PDF page 24 / printed page 10 -->

最后给出 Green 公式的两个有用应用, 以此结束本节.

**Lemma 1.4.** *设 $\Omega$ 是 $\mathbb R^N$ 的有界开子集, 其边界 $\Gamma$ 是 Lipschitz 连续的.*

$1^\circ)$ *对 $H^1(\Omega)$ 中的 $u$ 和 $v$, 以及 $1\leq i\leq N$, 有:*

$$
\int_\Omega u(\partial v/\partial x_i)\,dx=-\int_\Omega(\partial u/\partial x_i)v\,dx+\int_\Gamma\gamma_0(uv)n_i\,ds. \tag{1.19}
$$

$2^\circ)$ *如果还有 $u\in H^2(\Omega)$, 则有:*

$$
\sum_{i=1}^N\int_\Omega\frac{\partial u}{\partial x_i}\frac{\partial v}{\partial x_i}\,dx=-\sum_{i=1}^N\int_\Omega\frac{\partial^2u}{\partial x_i^2}v\,dx+\sum_{i=1}^N\int_\Gamma\gamma_0\left(\frac{\partial u}{\partial x_i}v\right)n_i\,ds. \tag{1.20}
$$

采用通常的记号

$$
\Delta u=\sum_{i=1}^N\frac{\partial^2u}{\partial x_i^2},\qquad \mathbf{grad}\,u=(\partial u/\partial x_1,\ldots,\partial u/\partial x_N),
$$

式 (1.20) 变为

$$
(\mathbf{grad}\,u,\mathbf{grad}\,v)=-(\Delta u,v)+\int_\Gamma(\partial u/\partial n)\gamma_0v\,ds. \tag{1.21}
$$

## 1.2 抽象椭圆理论

本节简要介绍研究椭圆型线性偏微分方程时使用的一种基本工具.

设 $V$ 是实 Hilbert 空间, 其范数记作 $\|\cdot\|_V$; 设 $V'$ 是它的对偶空间, 并以 $\langle\cdot,\cdot\rangle$ 表示 $V'$ 与 $V$ 之间的对偶配对. 设 $(u,v)\mapsto a(u,v)$ 是 $V\times V$ 上的实双线性形式, $l$ 是 $V'$ 中的元素, 考虑如下问题:

$$
\text{Find }u\in V\text{ such that}\qquad a(u,v)=\langle l,v\rangle\quad\forall v\in V. \tag{P}
$$

下面这个 Theorem 由 Lax & Milgram [49] 给出.

**Theorem 1.7.** *假设 $a$ 在 $V$ 上连续且椭圆, 即存在两个常数 $M$ 和 $\alpha>0$, 使得*

$$
|a(u,v)|\leq M\|u\|_V\|v\|_V\qquad\forall u,v\in V \tag{1.22}
$$

*以及*

$$
a(v,v)\geq\alpha\|v\|_V^2\qquad\forall v\in V. \tag{1.23}
$$

*则 Problem (P) 在 $V$ 中存在唯一解 $u$. 此外, 映射 $l\mapsto u$ 是从 $V'$ 到 $V$ 的同构.*

<!-- PDF page 25 / printed page 11 -->

**Corollary 1.2.** *当 $a$ 对称时, 即 $a(u,v)=a(v,u)$ 对所有 $u,v\in V$ 成立, Problem (P) 的解 $u$ 也是 $V$ 中使下列二次泛函(也称为能量泛函)达到最小值的唯一元素:*

$$
J(v)=(1/2)a(v,v)-\langle l,v\rangle. \tag{1.24}
$$

## 1.3 Example 1: Laplace 算子的 Dirichlet 问题

在所有例子中, 都假设 $\Omega$ 有界且 $\Gamma$ 是 Lipschitz 连续的. 考虑如下非齐次 Dirichlet 问题:

给定 $H^{-1}(\Omega)$ 中的 $f$ 和 $H^{1/2}(\Gamma)$ 中的 $g$, 求函数 $u$, 使得

$$
(D)\quad\begin{cases}
-\Delta u=f&\text{in }\Omega, \tag{1.25}\\
u=g&\text{on }\Gamma. \tag{1.26}
\end{cases}
$$

把这个问题表述为 Problem (P) 的形式. 令 $V=H_0^1(\Omega)$, 并置

$$
a(u,v)=(\mathbf{grad}\,u,\mathbf{grad}\,v).
$$

显然, $a$ 在 $H_0^1(\Omega)^2$ 上连续, 并且由 Theorem 1.1,

$$
a(v,v)=\|\mathbf{grad}\,v\|_{0,\Omega}^2=|v|_{1,\Omega}^2\geq C\|v\|_{1,\Omega}^2.
$$

此外, 由于 $H^{1/2}(\Gamma)$ 是 $H^1(\Omega)$ 中 $\gamma_0$ 的值域空间, 取满足 $u_0=g$ on $\Gamma$ 的 $u_0\in H^1(\Omega)$, 并考察如下问题:

$$
(D')\quad\begin{cases}
\text{Find }u\in H^1(\Omega)\text{ such that}\\
u-u_0\in H_0^1(\Omega), \tag{1.27}\\
a(u-u_0,v)=\langle f,v\rangle-a(u_0,v)&\forall v\in H_0^1(\Omega). \tag{1.28}
\end{cases}
$$

由于 $a$ 连续, 映射 $v\mapsto\langle f,v\rangle-a(u_0,v)$ 属于 $H^{-1}(\Omega)$. 因此, 由 Lax & Milgram Theorem, Problem $(D')$ 在 $H^1(\Omega)$ 中存在唯一解 $u$.

只需再证明可以把 $u$ 刻画为 Problem $(D)$ 的唯一解. 在式 (1.28) 中取 $v\in\mathcal D(\Omega)$, 得到

$$
a(u,v)=-\langle\Delta u,v\rangle=\langle f,v\rangle\qquad\forall v\in\mathcal D(\Omega).
$$

因此 $u$ 满足 (1.27) 和 (1.25). 反过来, 由 $\mathcal D(\Omega)$ 在 $H_0^1(\Omega)$ 中的稠密性, $(D_1)$ 的每个解都是 $(D')$ 的解. 但

$$
u-u_0\in H_0^1(\Omega)\quad\text{iff }u=g\quad\text{on }\Gamma,
$$

因此 Problems $(D_1)$ 和 $(D)$ 相同.

<!-- PDF page 26 / printed page 12 -->

关于 $u$ 的正则性, 由 Lax & Milgram Theorem 可知, 映射 $l\mapsto u-u_0$ 是从 $H^{-1}(\Omega)$ 到 $H_0^1(\Omega)$ 的同构. 因此,

$$
\|u-u_0\|_{1,\Omega}\leq C_2\|l\|_{-1,\Omega}.
$$

显然,

$$
\|l\|_{-1,\Omega}\leq\|f\|_{-1,\Omega}+\|u_0\|_{1,\Omega}.
$$

从而

$$
\|u\|_{1,\Omega}\leq C_3\{\|f\|_{-1,\Omega}+\|u_0\|_{1,\Omega}\}\quad\forall u_0\in H^1(\Omega)\text{ such that }u_0=g\text{ on }\Gamma.
$$

根据 Definition (1.16), 这意味着

$$
\|u\|_{1,\Omega}\leq C_3\{\|f\|_{-1,\Omega}+\|g\|_{1/2,\Gamma}\}.
$$

于是证明了如下 Proposition.

**Proposition 1.1.** *Problem (D) 在 $H^1(\Omega)$ 中存在唯一解 $u$, 并且存在常数 $C=C(\Omega)$, 使得*

$$
\|u\|_{1,\Omega}\leq C\{\|f\|_{-1,\Omega}+\|g\|_{1/2,\Gamma}\}, \tag{1.29}
$$

*即 $u$ 连续依赖于 Problem (D) 的数据.*

当 $f$ 和 $g$ 具有更高正则性时, 自然可以预期 Problem (D) 的解 $u$ 也更光滑. 下一个 Theorem 给出 $u$ 的准确正则性. 它的证明远远超出本书范围, 例如可见 Grisvard [42].

**Theorem 1.8.** $1^\circ)$ *设 $\Omega$ 是 $\mathbb R^N$ 的有界开子集, 其边界 $\Gamma$ 对某个整数 $k\geq0$ 属于 $\mathcal C^{k+1,1}$ 类. 假设 Problem (1.25)--(1.26) 的数据 $f$ 和 $g$ 满足*

$$
f\in W^{k,p}(\Omega),\qquad g\in W^{k+2-1/p,p}(\Gamma),
$$

*其中实数 $p$ 满足 $1<p<\infty$. 则 $u\in W^{k+2,p}(\Omega)$, 并且存在常数 $C=C(k,p,\Omega)$, 使得*

$$
\|u\|_{k+2,p,\Omega}\leq C\{\|f\|_{k,p,\Omega}+\|g\|_{k+2-1/p,p,\Gamma}\}. \tag{1.30}
$$

$2^\circ)$ *当 $\Omega$ 是没有凹角的有界二维多边形时, 存在依赖于 $\Gamma$ 最大内角的实数 $p_\Omega>2$, 使得只要 $f\in L^p(\Omega)$, 并且 $(g|_{\Gamma_j};\ 1\leq j\leq J)\in\prod_{j=1}^J W^{2-1/p,p}(\Gamma_j)$ 满足 Remark 1.1 的匹配条件, 就有*

$$
u\in W^{2,p}(\Omega),\qquad1<p<p_\Omega.
$$

$3^\circ)$ *如果 $\Omega$ 是三维有界凸多面体, 则 $2^\circ)$ 的结论对于齐次 Dirichlet 问题 $(g=0)$ 仍然成立.*

<!-- PDF page 27 / printed page 13 -->

**Remark 1.2.** 令 $g=0$ 应用上述 Theorem, 立即可知: 当 $\Omega$ 是 $\mathbb R^2$ 中的有界凸多边形(或 $\mathbb R^3$ 中的多面体)时, 映射 $u\mapsto\Delta u$ 是从 $W^{2,p}(\Omega)\cap W_0^{1,p}(\Omega)$ 到 $L^p(\Omega)$ 的同构, 其中对某个 $\varepsilon>0$, $p\in(1,2+\varepsilon]$. 当 $\Omega$ 的边界属于 $\mathcal C^{1,1}$ 类时, 这个同构对所有 $p\in(1,\infty)$ 都成立.

## 1.4 Example 2: Laplace 算子的 Neumann 问题

这里进一步假设 $\Omega$ 连通, 并处理如下非齐次 Neumann 问题:

求 $u$, 使得

$$
(N)\quad\begin{cases}
-\Delta u=f&\text{in }\Omega, \tag{1.31}\\
\partial u/\partial n=g&\text{on }\Gamma, \tag{1.32}\\
\text{where }f\in L^2(\Omega)\text{ and }g\in H^{-1/2}(\Gamma)\text{ satisfy}\\
\displaystyle\int_\Omega f\,dx+\langle g,1\rangle_\Gamma=0. \tag{1.33}
\end{cases}
$$

由于 Problem (N) 只涉及 $u$ 的导数, 它的解显然不可能唯一. 为绕开这一困难, 在商空间 $H^1(\Omega)/\mathbb R$ 中求解 $u$, 并为该空间赋予商范数

$$
\|\dot v\|_{H^1(\Omega)/\mathbb R}=\inf_{v\in\dot v}\|v\|_{1,\Omega}. \tag{1.34}
$$

下面的 Theorem 给出该空间的一个重要性质; 其证明可见 Nečas [58].

**Theorem 1.9.** *设 $\Omega$ 是 $\mathbb R^N$ 的有界, 连通且 Lipschitz 连续的开子集. 对于商范数 (1.34), 空间 $H^1(\Omega)/\mathbb R$ 是 Hilbert 空间. 此外, 在这个空间上, 泛函 $\dot v\mapsto|v|_{1,\Omega}$ 是与 (1.34) 等价的范数.*

利用这个空间, 可以把 Problem (N) 化为 Problem (P) 的抽象形式. 令 $V=H^1(\Omega)/\mathbb R$,

$$
a(\dot u,\dot v)=(\mathbf{grad}\,u,\mathbf{grad}\,v),
$$

并令

$$
l:\dot v\mapsto(f,v)+\langle g,v\rangle_\Gamma\qquad\forall v\in\dot v. \tag{1.35}
$$

注意, 由于相容条件 (1.33), 式 (1.35) 的右端与所取的具体代表元 $v\in\dot v$ 无关. 此外, 由 (1.16) 有

$$
|(f,v)+\langle g,v\rangle_\Gamma|\leq(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma})\inf_{v\in\dot v}\|v\|_{1,\Omega},
$$

因此 $l\in V'$.

<!-- PDF page 28 / printed page 14 -->

从而

$$
\|l\|_{V'}\leq\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma}. \tag{1.36}
$$

显然, $a(\dot u,\dot v)$ 在 $V\times V$ 上连续, 并且由 Theorem 1.9,

$$
a(\dot v,\dot v)=|v|_{1,\Omega}^2\geq C_1\|\dot v\|_{H^1(\Omega)/\mathbb R}^2.
$$

因此, 由 Lax & Milgram Theorem, 如下问题

$$
(N')\quad\text{Find }\dot u\in H^1(\Omega)/\mathbb R\text{ satisfying}\qquad a(\dot u,\dot v)=\langle l,\dot v\rangle\quad\forall\dot v\in H^1(\Omega)/\mathbb R \tag{1.37}
$$

在 $H^1(\Omega)/\mathbb R$ 中存在唯一解 $\dot u$.

下面解释 Problem $(N')$. 把 $v$ 限制在 $\mathcal D(\Omega)$ 中时, 式 (1.37) 给出 (1.31). 接着, 将式 (1.31) 与 $v$ 作标量积, 并与 (1.37) 比较, 得到

$$
(\mathbf{grad}\,u,\mathbf{grad}\,v)=-(\Delta u,v)+\langle g,v\rangle_\Gamma\qquad\forall v\in H^1(\Omega). \tag{1.38}
$$

因此, Problem $(N')$ 等价于在 $H^1(\Omega)$ 中求满足 (1.31) 和 (1.38) 的 $u$.

还需把 (1.38) 解释为边界条件. 在这一阶段, 如果不假设 $u\in H^2(\Omega)$, 就无法做到这一点. 此时 Green 公式 (1.21) 给出

$$
\int_\Gamma(\partial u/\partial n)v\,ds=\langle g,v\rangle_\Gamma\qquad\forall v\in H^1(\Omega),
$$

即 $\partial u/\partial n=g$ on $\Gamma$. 因此, Problems (N) 和 $(N')$ 等价. 当然, 这并不完全令人满意, 因为 Problem (N) 的解是否存在取决于 $(N')$ 的解的正则性. 虽然这种正则性通常确实成立, 但下一段中更强有力的工具将消除这个额外的光滑性假设.

现在考察 Problem $(N')$ 的解 $\dot u$ 对数据的依赖性. 根据 Lax & Milgram Theorem 1.7, 式 (1.36) 以及 Theorem 1.9 的范数等价性, 得到

$$
|u|_{1,\Omega}\leq C_2(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma}).
$$

于是证明了如下结果.

**Proposition 1.2.** *Problem $(N')$ 在 $H^1(\Omega)/\mathbb R$ 中存在唯一解 $\dot u$, 并且这个解连续依赖于数据:*

<!-- PDF page 29 / printed page 15 -->

$$
|u|_{1,\Omega}\leq C(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma})\qquad\forall u\in\dot u. \tag{1.39}
$$

*此外, 当 $\dot u\in H^2(\Omega)/\mathbb R$ 时, 它也是 Problem (N) 的唯一解.*

与 Dirichlet 问题类似, 当 Problem $(N')$ 的数据具有额外光滑性时, 它的解具有更高正则性. 由 Grisvard [42] 给出的准确结果与 Theorem 1.8 十分相似.

**Theorem 1.10.** $1^\circ)$ *设 $\Omega$ 如 Theorem 1.8 中所述, 并假设 Problem (1.37) 的数据 $f$ 和 $g$ 满足*

$$
f\in W^{k,p}(\Omega),\qquad g\in W^{k+1-1/p,p}(\Gamma),\qquad1<p<\infty.
$$

*则 $\dot u\in W^{k+2,p}(\Omega)/\mathbb R$, 并且存在常数 $C=C(k,p,\Omega)$, 使得*

$$
\|\dot u\|_{W^{k+2,p}(\Omega)/\mathbb R}\leq C\{\|f\|_{k,p,\Omega}+\|g\|_{k+1-1/p,p,\Gamma}\}. \tag{1.40}
$$

$2^\circ)$ *当 $\Omega$ 是没有凹角的有界二维多边形时, 存在依赖于 $\Gamma$ 最大内角的实数 $p_\Omega>2$, 使得只要 $f\in L^p(\Omega)$, 并且 $(g|_{\Gamma_j};\ 1\leq j\leq J)\in\prod_{j=1}^J W^{1-1/p,p}(\Gamma_j)$, 就有*

$$
\dot u\in W^{2,p}(\Omega)/\mathbb R,\qquad1<p<p_\Omega.
$$

$3^\circ)$ *如果 $\Omega$ 是 $\mathbb R^3$ 中的有界凸多面体, 则 $2^\circ)$ 的结论对齐次 Neumann 问题 $(g=0)$ 成立.*

## 1.5 Example 3: 双调和算子的 Dirichlet 问题

考虑如下非齐次问题:

给定 $H^{-2}(\Omega)$ 中的 $f$, $H^{3/2}(\Gamma)$ 中的 $g_1$ 以及 $H^{1/2}(\Gamma)$ 中的 $g_2$, 求 $u$, 使得

$$
(B)\quad\begin{cases}
\Delta^2u=f&\text{in }\Omega, \tag{1.41}\\
u=g_1&\text{on }\Gamma, \tag{1.42}\\
\partial u/\partial n=g_2&\text{on }\Gamma. \tag{1.43}
\end{cases}
$$

与这个问题自然对应的函数空间是 $H_0^2(\Omega)$, 双线性形式为

$$
a(u,v)=(\Delta u,\Delta v).
$$

该形式在 $H_0^2(\Omega)$ 上是椭圆的, 因为映射 $v\mapsto\|\Delta v\|_{0,\Omega}$ 是 $H_0^2(\Omega)$ 上与范数 $\|\cdot\|_{2,\Omega}$ 等价的范数. 事实上, 对 $\mathcal D(\Omega)$ 中的 $v$, 通过分部积分并交换导数, 很容易证明

$$
\|\Delta v\|_{0,\Omega}^2=|v|_{2,\Omega}^2. \tag{1.44}
$$

由稠密性, 同样的结果对 $H_0^2(\Omega)$ 中的函数成立. 范数等价性来自 Poincaré Theorem 1.1.

<!-- PDF page 30 / printed page 16 -->

根据 Theorem 1.6, 如果 $\Gamma$ 属于 $\mathcal C^{1,1}$ 类, 则存在函数 $u_0\in H^2(\Omega)$, 使得

$$
u_0=g_1\quad\text{on }\Gamma,\qquad\partial u_0/\partial n=g_2\quad\text{on }\Gamma. \tag{1.45}
$$

于是转而考虑如下问题:

$$
(B')\quad\begin{cases}
\text{Find }u\in H^2(\Omega)\text{ such that}\\
u-u_0\in H_0^2(\Omega), \tag{1.46}\\
a(u-u_0,v)=\langle f,v\rangle-a(u_0,v)&\forall v\in H_0^2(\Omega). \tag{1.47}
\end{cases}
$$

由 Lax & Milgram Theorem 1.7, Problem $(B')$ 在 $H^2(\Omega)$ 中恰有一个解 $u$. 由 (1.45) 和 (1.46), $u$ 满足边界条件 $u=g_1$ 和 $\partial u/\partial n=g_2$ on $\Gamma$. 此外, 把 (1.47) 的测试函数限制到 $\mathcal D(\Omega)$, 得到 $\Delta^2u=f$ in $H^{-2}(\Omega)$. 因此 $u$ 是 (B) 的解.

反过来, 与 Laplace 算子的情形一样, 可以证明 Problem (B) 在 $H^2(\Omega)$ 中至多有一个解. 由 (1.47) 和范数等价性得到估计

$$
\|u\|_{2,\Omega}\leq C_1(\|f\|_{-2,\Omega}+\|u_0\|_{2,\Omega})\qquad\forall u_0\text{ satisfying (1.45)},
$$

即

$$
\|u\|_{2,\Omega}\leq C_2(\|f\|_{-2,\Omega}+\|g_1\|_{3/2,\Gamma}+\|g_2\|_{1/2,\Gamma}).
$$

这些结果概括为下面的 Proposition.

**Proposition 1.3.** *如果 $\Gamma$ 属于 $\mathcal C^{1,1}$ 类, 则 Problem (B) 在 $H^2(\Omega)$ 中恰有一个解 $u$, 并且满足如下估计:*

$$
\|u\|_{2,\Omega}\leq C(\|f\|_{-2,\Omega}+\|g_1\|_{3/2,\Gamma}+\|g_2\|_{1/2,\Gamma}). \tag{1.48}
$$

上述分析假设 $\Gamma$ 属于 $\mathcal C^{1,1}$ 类, 因而不允许有角点. 这个假设在提升算子 $(g_1,g_2)\mapsto u_0$ 中起关键作用. 当然, 如果这些非齐次数据直接以函数 $u_0\in H^2(\Omega)$ 的形式给出, 且

$$
u=u_0\quad\text{on }\Gamma\quad\text{and}\quad\partial u/\partial n=\partial u_0/\partial n\quad\text{on }\Gamma,
$$

那么 Proposition 1.3 也适用于 Lipschitz 连续定义域, 其中用 $u_0$ 代替 $g_1$ 和 $g_2$. 否则, 必须略微修改 Problem (B) 的陈述. 假设 $\Omega$ 是有界二维多边形. 按照 Remark 1.1, 以 $\Gamma_j$ 和 $S_j$, $1\leq j\leq J$, 分别表示 $\Gamma$ 的边和顶点. 取 $J$ 个函数:

<!-- PDF page 31 / printed page 17 -->

$$
h_j\in H^{3/2}(\Gamma_j),\qquad1\leq j\leq J,
$$

它们满足匹配条件 $h_j(S_{j+1})=h_{j+1}(S_{j+1})$, 再取 $J$ 个函数

$$
g_j\in H^{1/2}(\Gamma_j),\qquad1\leq j\leq J,
$$

并考虑如下问题:

$$
(B'')\quad\begin{cases}
\Delta^2u=f&\text{in }H^{-2}(\Omega), \tag{1.41}\\
u=h_j&\text{on }\Gamma_j, \tag{1.49}\\
\partial u/\partial n=g_j&\text{on }\Gamma_j, \tag{1.50}
\end{cases}\qquad1\leq j\leq J.
$$

由 Remark 1.1, 存在函数 $u_0\in H^2(\Omega)$, 使得

$$
u_0=h_j,\qquad\partial u_0/\partial n=g_j\quad\text{on }\Gamma_j,\qquad1\leq j\leq J,
$$

并且

$$
\|u_0\|_{2,\Omega}\leq C_3\left\{\sum_{j=1}^J(\|h_j\|_{3/2,\Gamma_j}^2+\|g_j\|_{1/2,\Gamma_j}^2)\right\}^{1/2}.
$$

因此, Proposition 1.3 的结论(用函数 $h_j$ 和 $g_j$ 代替 $g_1$ 和 $g_2$)在这种情形下也适用于 Problem $(B'')$.

当 $\Omega$ 的边界充分光滑时, 可以得到关于 $u$ 的正则性的更多信息.

**Theorem 1.11.** *设 $\Omega$ 是 $\mathbb R^N$ 的有界开子集, 其边界 $\Gamma$ 对某个整数 $k\geq-2$ 属于 $\mathcal C^{k+3,1}$ 类, 并假设双调和 Problem (B) 的数据 $f,g_1,g_2$ 满足*

$$
f\in H^k(\Omega),\qquad g_1\in H^{k+7/2}(\Gamma),\qquad g_2\in H^{k+5/2}(\Gamma).
$$

*则 $u\in H^{k+4}(\Omega)$, 并且存在常数 $C=C(k,\Omega)$, 使得*

$$
\|u\|_{k+4,\Omega}\leq C\{\|f\|_{k,\Omega}+\|g_1\|_{k+7/2,\Gamma}+\|g_2\|_{k+5/2,\Gamma}\}. \tag{1.51}
$$

即使 $\Gamma$ 有角点, 对于具有齐次边界条件的双调和问题, Proposition 1.3 的结论仍可加强.

**Theorem 1.12.** *假设 $\Omega$ 是没有凹角的有界二维多边形. 则映射 $u\mapsto\Delta^2u$ 是从 $H^3(\Omega)\cap H_0^2(\Omega)$ 到 $H^{-1}(\Omega)$ 的同构.*

最后这个结果对于建立平面凸多边形上 Stokes 问题解的正则性是基本的(参见 Grisvard [43]).
