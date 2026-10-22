<!-- PDF page 19 / printed page 5 -->

**Theorem 1.2.** *设 $\Omega$ 是 $\mathbb R^N$ 的一个 Lipschitz 连续开子集.*

$1^\circ)$ *对所有整数 $m\geq0$ 以及满足 $1\leq p<\infty$ 的实数 $p$, 空间 $\mathcal D(\bar\Omega)$ 在 $W^{m,p}(\Omega)$ 中稠密.*

$2^\circ)$ *设 $u\in W^{m,p}(\Omega)$, 并以 $\tilde u$ 表示 $u$ 在 $\Omega$ 外的零延拓. 如果 $\tilde u\in W^{m,p}(\mathbb R^N)$, 则 $u\in W_0^{m,p}(\Omega)$.*

$3^\circ)$ *如果进一步假设 $\Gamma$ 有界且 $m\geq1$, 则存在从 $W^{m,p}(\Omega)$ 到 $W^{m,p}(\mathbb R^N)$ 的连续线性延拓算子 $P$:*

$$
Pu|_\Omega=u\qquad\forall u\in W^{m,p}(\Omega).
$$

下面讨论基本的 Sobolev 嵌入定理, 它从本质上联系不同的 Sobolev 空间与光滑函数空间.

**Theorem 1.3.** *设 $\Omega$ 是 $\mathbb R^N$ 的一个 Lipschitz 连续开子集, $p\in\mathbb R$ 且 $1\leq p<\infty$, 并设 $m,n\in\mathbb N$ 且 $n\leq m$. 在代数意义和拓扑意义下都有如下嵌入:*

$$
W^{m,p}(\Omega)\subset
\begin{cases}
W^{n,q}(\Omega),&\text{if }1/q=1/p-(m-n)/N>0,\\
W_{\mathrm{loc}}^{n,q}(\Omega),&\forall q\in[1,\infty)\text{ if }1/p=(m-n)/N,\\
\mathcal C^n(\Omega),&\text{provided }1/p<(m-n)/N.
\end{cases} \tag{1.7}
$$

*此外, 如果 $\Omega$ 有界, 则最后一个包含关系在 $\mathcal C^n(\bar\Omega)$ 中成立, 而且对满足下列条件的所有实数 $q'$, 从 $W^{m,p}(\Omega)$ 到 $W^{n,q'}(\Omega)$ 的嵌入是紧的:*

$$
\text{or}\quad
\begin{cases}
1\leq q'<Np/(N-(m-n)p),&\text{whenever }N>(m-n)p,\\
1\leq q'<\infty,&\text{when }N=(m-n)p.
\end{cases} \tag{1.8}
$$

*另外, 这些紧嵌入对于负的 $n$ 或 $m$ 也成立.*

这个 Theorem 在后文中将反复使用. 例如, 下一节将使用 $L^2(\Omega)$ 紧嵌入 $H^{-1}(\Omega)$ 这一事实. 作为一个直接应用, 有如下关于 $W^{m,p}(\Omega)$ 中乘法的 Corollary.

**Corollary 1.1.** *假设 $\Omega$ 是 $\mathbb R^N$ 的一个有界 Lipschitz 连续开子集. 设 $m_1,m_2,m$ 是三个非负整数, $p_1,p_2,p$ 是 $[1,\infty)$ 中的三个实数, 满足 $m_1\geq m$, $m_2\geq m$, 并且或者*

$$
m_1+m_2-m\geq N(1/p_1+1/p_2-1/p)\geq0,
\qquad m_i-m>N(1/p_i-1/p)\quad i=1,2,
$$

*或者*

$$
m_1+m_2-m>N(1/p_1+1/p_2-1/p)\geq0,
\qquad m_i-m\geq N(1/p_i-1/p)\quad i=1,2.
$$

*则映射 $u,v\mapsto u\cdot v$ 是从 $W^{m_1,p_1}(\Omega)\times W^{m_2,p_2}(\Omega)$ 到 $W^{m,p}(\Omega)$ 的连续双线性映射.*

<!-- PDF page 20 / printed page 6 -->

在研究 $W^{m,p}(\Omega)$ 中函数的迹之前, 先把 Sobolev 空间的概念推广到 $m$ 的非整数值较为方便. 分数阶 Sobolev 空间有若干种定义, 遗憾的是它们并不等价. 这里主要采用下面的定义.

**Definition 1.2.** 设 $\Omega$ 是 $\mathbb R^N$ 的开子集, $m\geq0$ 是整数, $s$ 和 $p$ 是满足 $1\leq p<\infty$ 的两个实数, 且 $s=m+\sigma$, 其中 $\sigma\in\mathbb R$ 并满足 $0<\sigma<1$. 用 $W^{s,p}(\Omega)$ 表示定义在 $\Omega$ 上且满足下列条件的所有分布 $u$ 所成的空间:

$$
u\in W^{m,p}(\Omega),
$$

并且

$$
\int_\Omega\int_\Omega
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|^p}
{\|x-y\|^{N+\sigma p}}\,dx\,dy<+\infty
\qquad\forall|\alpha|=m.
$$

类似地, 用 $W^{s,\infty}(\Omega)$ 表示 $W^{m,\infty}(\Omega)$ 中满足下列条件的函数 $u$ 所成的子空间:

$$
\max_{|\alpha|=m}\operatorname*{ess\,sup}_{\substack{x,y\in\Omega\\x\neq y}}
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|}
{\|x-y\|^\sigma}\leq+\infty.
$$

可以证明, $W^{s,p}(\Omega)$ 关于如下范数是 Banach 空间:

$$
\|u\|_{s,p,\Omega}=\left\{\|u\|_{m,p,\Omega}^p+
\sum_{|\alpha|=m}\int_\Omega\int_\Omega
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|^p}
{\|x-y\|^{N+\sigma p}}\,dx\,dy\right\}^{1/p}. \tag{1.9}
$$

当 $p=\infty$ 时作显然的修改. 与整数阶情形一样, 对 $s>0$ 定义

$$
W_0^{s,p}(\Omega)=\overline{\mathcal D(\Omega)}^{W^{s,p}(\Omega)},
$$

并用 $W^{-s,p'}(\Omega)$ 表示 $W_0^{s,p}(\Omega)$ 的对偶空间, 其中 $p$ 和 $p'$ 由式 (1.6) 联系. 原来若干结果只需少量修改便可推广到分数阶 Sobolev 空间. 更确切地说, Sobolev 嵌入 Theorem 1.3 及其 Corollary 1.1 的陈述对分数阶 Sobolev 空间仍然成立. Theorem 1.2 的稠密性部分不作修改即可推广到 $s>0$, 而当 $\Omega$ 有界时, 延拓部分对 $s>0$ 成立. 此外, 还有下面这个重要的 Lions & Peetre [54] 插值 Theorem, 后文将反复使用它.

**Theorem 1.4.** *设 $\Omega$ 是 $\mathbb R^N$ 的一个有界 Lipschitz 连续开子集. 设 $\theta\in[0,1]$, 并设 $s_i,t_i$ 是两对满足 $0\leq t_i\leq s_i$ 的实数, $i=1,2$. 对某个满足 $1<p<\infty$ 的实数 $p$, 令 $\mathcal L_i$ 和 $\mathcal L_\theta$ 分别表示 $\mathcal L(W^{s_i,p}(\Omega);W^{t_i,p}(\Omega))$ 和 $\mathcal L(W^{(1-\theta)s_1+\theta s_2,p}(\Omega);W^{(1-\theta)t_1+\theta t_2,p}(\Omega))$. 设 $\pi$ 是 $\mathcal L_1\cap\mathcal L_2$ 中的算子; 则 $\pi$ 也属于 $\mathcal L_\theta$, 并且存在常数 $C$, 使得*

$$
\|\pi\|_{\mathcal L_\theta}
\leq C\|\pi\|_{\mathcal L_1}^{1-\theta}
\|\pi\|_{\mathcal L_2}^{\theta}. \tag{1.10}
$$

<!-- PDF page 21 / printed page 7 -->

此外, 当 $p=2$ 时, 还可以用 Fourier 变换给出 $W^{s,2}(\Omega)$ 的另一种定义; 在代数意义和拓扑意义下, 它得到的空间与 Definition 1.2 相同.

**Definition 1.3.** $1^\circ)$ 对实数 $s>0$, 令:

$$
H^s(\mathbb R^N)=\{v\in L^2(\mathbb R^N);\ (1+\|\sigma\|^2)^{s/2}\hat v(\sigma)\in L^2(\mathbb R_\sigma^N)\}. \tag{1.11}
$$

其范数为:

$$
\|v\|_{s,\mathbb R^N}=\{\|v\|_{0,\mathbb R^N}^2+
\|(1+\|\sigma\|^2)^{s/2}\hat v(\sigma)\|_{0,\mathbb R_\sigma^N}^2\}^{1/2}, \tag{1.12}
$$

其中 $\hat v$ 表示 $v$ 的 Fourier 变换.

$2^\circ)$ 当 $\Omega$ 是 $\mathbb R^N$ 的开子集时, 定义

$$
H^s(\Omega)=\{v\in L^2(\Omega);\ \exists\tilde v\in H^s(\mathbb R^N)\text{ with }\tilde v|_\Omega=v\}. \tag{1.13}
$$

其范数为:

$$
\|v\|_{s,\Omega}=
\inf_{\substack{\tilde v\in H^s(\mathbb R^N)\\\tilde v|_\Omega=v}}
\|\tilde v\|_{s,\mathbb R^N}. \tag{1.14}
$$

如上所述, $H^s(\Omega)$ 与 $W^{s,2}(\Omega)$ 之间有如下关系.

**Lemma 1.3.** *设 $\Omega$ 是 $\mathbb R^N$ 的一个有界 Lipschitz 连续开子集. 则在代数意义和拓扑意义下都有*

$$
W^{s,2}(\Omega)=H^s(\Omega)\qquad\forall s>0.
$$

*此外, 当 $s$ 是整数时, 式 (1.11) 以一个等价范数定义经典 Sobolev 空间 $H^m(\Omega)$.*

现在可以考察 $W^{s,p}(\Omega)$ 中函数的边界值. 假设 $\Omega$ 是 $\mathbb R^N$ 的有界开子集, 其边界 $\Gamma$ 至少是 Lipschitz 连续的. 首先定义空间 $W^{s,p}(\Gamma)$ 的含义. 根据 Definition 1.1, 可以通过映射

$$
\Phi(y')=(y',\phi(y'))
$$

把 $\Gamma$ 局部看作 $\mathbb R^N$ 的一个 $N-1$ 维子流形, 该映射把 $\mathcal O'$ 映到 $\Gamma\cap\mathcal O$ 上. 于是给出如下定义.

**Definition 1.4.** 设 $\Omega$ 是 $\mathbb R^N$ 的有界开子集, 其边界 $\Gamma$ 对某个整数 $k\geq0$ 属于 $\mathcal C^{k,1}$ 类. 对 $s\leq k+1$, 如果对满足 Definition 1.1 假设的所有可能的 $\mathcal O$ 和 $\phi$, $u\circ\Phi$ 都属于 $W^{s,p}(\mathcal O'\cap\Phi^{-1}(\Gamma\cap\mathcal O))$, 则称 $\Gamma$ 上的分布 $u$ 属于 $W^{s,p}(\Gamma)$.

设 $(\mathcal O_j,\Phi_j)_{1\leq j\leq J}$ 是 $\Gamma$ 的任一图册, 其中每一对 $(\mathcal O_j,\Phi_j)$ 都满足上述 Definition 的假设. 则 $W^{s,p}(\Gamma)$ 的一个可用 Banach 范数是如下泛函:

<!-- PDF page 22 / printed page 8 -->

$$
u\mapsto\left\{\sum_{j=1}^J
\|u\circ\Phi_j\|_{s,p,\mathcal O'_j\cap\Phi_j^{-1}(\Gamma\cap\mathcal O_j)}^p
\right\}^{1/p}. \tag{1.15}
$$

不过这个范数很繁琐, 后文将用更方便的等价范数代替它. 例如, 当 $s=0$ 时采用更熟悉的 $L^p$ 范数:

$$
\|u\|_{0,p,\Gamma}=\left\{\int_\Gamma|u(x)|^p\,ds(x)\right\}^{1/p},
$$

其中 $ds$ 表示 $\Gamma$ 的曲面测度. 此处值得指出, Theorem 1.2 的稠密性结果以及 Sobolev 嵌入 Theorem 1.3(其中维数取 $N-1$)在 $\Gamma$ 上也成立.

现在令 $u$ 是 $\mathcal D(\bar\Omega)$ 中的函数, 并用 $\gamma_0u$ 表示其边界值. 下述迹 Theorem 把算子 $\gamma_0$ 延拓到 $W^{s,p}(\Omega)$ 中的函数.

**Theorem 1.5.** *设 $\Omega$ 如 Definition 1.4 所述, 并设 $p\geq1$ 和 $s\geq0$ 是两个实数, 满足 $s\leq k+1$, $s-1/p=l+\sigma$, 其中 $l\geq0$ 是整数且 $0<\sigma<1$. 则定义在 $\mathcal D(\bar\Omega)$ 上的映射 $u\mapsto\gamma_0u$ 存在唯一的线性连续延拓, 该延拓是从下列空间到下列空间的满射算子:*

$$
W^{s,p}(\Omega)\quad\text{onto }W^{s-1/p,p}(\Gamma).
$$

*此外, 在 $W^{1,p}(\Omega)$ 中有:*

$$
\operatorname{Ker}(\gamma_0)=W_0^{1,p}(\Omega).
$$

对于这样的 $s$ 和 $p$, 该 Theorem 给出 $W^{s-1/p,p}(\Gamma)$ 上的如下范数, 可以证明它与式 (1.15) 等价:

$$
\|f\|_{s-1/p,p,\Gamma}=
\inf_{\substack{v\in W^{s,p}(\Omega)\\\gamma_0v=f}}
\|v\|_{s,p,\Omega}. \tag{1.16}
$$

当 $p=2$ 时, 式 (1.16) 是 Hilbert 范数. 本书主要使用 $H^{1/2}(\Gamma)$ 和 $H^{3/2}(\Gamma)$, 它们对应于 $p=2$ 以及分别取 $s=1$ 或 $2$. 还将使用 $H^{-1/2}(\Gamma)$, 即赋予显然的对偶范数的 $H^{1/2}(\Gamma)$ 对偶空间:

$$
\|f^*\|_{-1/2,\Gamma}=
\sup_{\substack{f\in H^{1/2}(\Gamma)\\f\neq0}}
\frac{\langle f^*,f\rangle}{\|f\|_{1/2,\Gamma}}. \tag{1.17}
$$

这里 $\langle\cdot,\cdot\rangle$ 仍表示 $H^{-1/2}(\Gamma)$ 与 $H^{1/2}(\Gamma)$ 之间的对偶配对. 同样, $\langle\cdot,\cdot\rangle$ 是 $L^2(\Gamma)$ 标量积的一个延拓, 其含义是, 当 $f^*\in L^2(\Gamma)$ 时, 可以把 $\langle f^*,f\rangle$ 与下式等同:

$$
\int_\Gamma f^*(x)f(x)\,ds(x).
$$
