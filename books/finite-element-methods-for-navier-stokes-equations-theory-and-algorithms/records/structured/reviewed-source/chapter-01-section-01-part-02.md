<!-- PDF page 19 / printed page 5 -->

**Theorem 1.2.** *Let $\Omega$ be an open Lipschitz-continuous subset of $\mathbb R^N$.*

$1^\circ)$ *The space $\mathcal D(\bar\Omega)$ is dense in $W^{m,p}(\Omega)$ for all integers $m\geq0$ and real $p$ with $1\leq p<\infty$.*

$2^\circ)$ *Let $u\in W^{m,p}(\Omega)$ and let $\tilde u$ denote its extension by zero outside $\Omega$. If $\tilde u\in W^{m,p}(\mathbb R^N)$ then $u\in W_0^{m,p}(\Omega)$.*

$3^\circ)$ *If in addition $\Gamma$ is bounded and $m\geq1$, there exists a continuous linear extension operator $P$ from $W^{m,p}(\Omega)$ into $W^{m,p}(\mathbb R^N)$:*

$$
Pu|_\Omega=u\qquad\forall u\in W^{m,p}(\Omega).
$$

We now come to the fundamental Sobolev Imbedding Theorem which essentially relates different Sobolev spaces and spaces of smooth functions.

**Theorem 1.3.** *Let $\Omega$ be an open Lipschitz-continuous subset of $\mathbb R^N$ and let $p\in\mathbb R$ with $1\leq p<\infty$ and $m$ and $n\in\mathbb N$ with $n\leq m$. The following imbeddings hold algebraically and topologically:*

$$
W^{m,p}(\Omega)\subset
\begin{cases}
W^{n,q}(\Omega),&\text{if }1/q=1/p-(m-n)/N>0,\\
W_{\mathrm{loc}}^{n,q}(\Omega),&\forall q\in[1,\infty)\text{ if }1/p=(m-n)/N,\\
\mathcal C^n(\Omega),&\text{provided }1/p<(m-n)/N.
\end{cases} \tag{1.7}
$$

*Moreover, if $\Omega$ is bounded, the last inclusion holds in $\mathcal C^n(\bar\Omega)$ and the imbedding of $W^{m,p}(\Omega)$ into $W^{n,q'}(\Omega)$ is compact for all real $q'$ that satisfy:*

$$
\text{or}\quad
\begin{cases}
1\leq q'<Np/(N-(m-n)p),&\text{whenever }N>(m-n)p,\\
1\leq q'<\infty,&\text{when }N=(m-n)p.
\end{cases} \tag{1.8}
$$

*In addition, these compact imbeddings are also valid for negative $n$ or $m$.*

This theorem will be used constantly in the sequel. For instance, in the next paragraph we shall use the fact that $L^2(\Omega)$ is compactly imbedded in $H^{-1}(\Omega)$. As an immediate application, we have the following corollary about multiplication in $W^{m,p}(\Omega)$.

**Corollary 1.1.** *Assume that $\Omega$ is a bounded Lipschitz-continuous open subset of $\mathbb R^N$. Let $m_1,m_2$ and $m$ be three non negative integers and $p_1,p_2$ and $p$ be three real numbers in $[1,\infty)$ such that $m_1\geq m$, $m_2\geq m$ and either*

$$
m_1+m_2-m\geq N(1/p_1+1/p_2-1/p)\geq0,
\qquad m_i-m>N(1/p_i-1/p)\quad i=1,2
$$

*or*

$$
m_1+m_2-m>N(1/p_1+1/p_2-1/p)\geq0,
\qquad m_i-m\geq N(1/p_i-1/p)\quad i=1,2.
$$

*Then the mapping $u,v\mapsto u\cdot v$ is a continuous bilinear map from $W^{m_1,p_1}(\Omega)\times W^{m_2,p_2}(\Omega)$ into $W^{m,p}(\Omega)$.*

<!-- PDF page 20 / printed page 6 -->

Before studying the trace of functions of $W^{m,p}(\Omega)$, it is convenient to extend the notion of Sobolev spaces to nonintegral values of $m$. There are several definitions of fractional Sobolev spaces which unfortunately are not equivalent. Here we shall use mostly the following one.

**Definition 1.2.** Let $\Omega$ be an open subset of $\mathbb R^N$, $m\geq0$ be an integer and $s$ and $p$ be two real numbers with $1\leq p<\infty$ and $s=m+\sigma$ where $\sigma\in\mathbb R$ with $0<\sigma<1$. We denote by $W^{s,p}(\Omega)$ the space of all distributions $u$ defined in $\Omega$ such that

$$
u\in W^{m,p}(\Omega)
$$

and

$$
\int_\Omega\int_\Omega
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|^p}
{\|x-y\|^{N+\sigma p}}\,dx\,dy<+\infty
\qquad\forall|\alpha|=m.
$$

Likewise, we denote by $W^{s,\infty}(\Omega)$ the subspace of functions $u$ in $W^{m,\infty}(\Omega)$ such that

$$
\max_{|\alpha|=m}\operatorname*{ess\,sup}_{\substack{x,y\in\Omega\\x\neq y}}
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|}
{\|x-y\|^\sigma}\leq+\infty.
$$

It can be shown that $W^{s,p}(\Omega)$ is a Banach space for the norm:

$$
\|u\|_{s,p,\Omega}=\left\{\|u\|_{m,p,\Omega}^p+
\sum_{|\alpha|=m}\int_\Omega\int_\Omega
\frac{|\partial^\alpha u(x)-\partial^\alpha u(y)|^p}
{\|x-y\|^{N+\sigma p}}\,dx\,dy\right\}^{1/p} \tag{1.9}
$$

with the obvious modification when $p=\infty$. Like in the integral case, we define for $s>0$:

$$
W_0^{s,p}(\Omega)=\overline{\mathcal D(\Omega)}^{W^{s,p}(\Omega)}
$$

and we denote by $W^{-s,p'}(\Omega)$ the dual space of $W_0^{s,p}(\Omega)$ with $p$ and $p'$ related by (1.6). It turns out that several previous results carry over to fractional Sobolev spaces with few modifications. More precisely, the statements of Sobolev's Imbedding Theorem 1.3 and that of its Corollary 1.1 are valid for fractional-order Sobolev spaces. The density part of Theorem 1.2 carries over without modification to $s>0$, while the extension part is valid for $s>0$ when $\Omega$ is bounded. In addition, we have the following outstanding Interpolation Theorem of Lions & Peetre [54] which we shall use over and over.

**Theorem 1.4.** *Let $\Omega$ be a bounded Lipschitz-continuous open subset of $\mathbb R^N$. Let $\theta\in[0,1]$ and let $s_i$ and $t_i$ be two pairs of real numbers with $0\leq t_i\leq s_i$ for $i=1,2$ and let $\mathcal L_i$ and $\mathcal L_\theta$ denote respectively $\mathcal L(W^{s_i,p}(\Omega);W^{t_i,p}(\Omega))$ and $\mathcal L(W^{(1-\theta)s_1+\theta s_2,p}(\Omega);W^{(1-\theta)t_1+\theta t_2,p}(\Omega))$ for some real $p$ with $1<p<\infty$. Let $\pi$ be an operator in $\mathcal L_1\cap\mathcal L_2$; then $\pi$ also belongs to $\mathcal L_\theta$ and there exists a constant $C$ such that*

$$
\|\pi\|_{\mathcal L_\theta}
\leq C\|\pi\|_{\mathcal L_1}^{1-\theta}
\|\pi\|_{\mathcal L_2}^{\theta}. \tag{1.10}
$$

<!-- PDF page 21 / printed page 7 -->

Also, when $p=2$ there is an alternate definition of $W^{s,2}(\Omega)$ using Fourier transforms which yields algebraically and topologically the same space as Definition 1.2.

**Definition 1.3.** $1^\circ)$ For real $s>0$ we set:

$$
H^s(\mathbb R^N)=\{v\in L^2(\mathbb R^N);\ (1+\|\sigma\|^2)^{s/2}\hat v(\sigma)\in L^2(\mathbb R_\sigma^N)\} \tag{1.11}
$$

with the norm:

$$
\|v\|_{s,\mathbb R^N}=\{\|v\|_{0,\mathbb R^N}^2+
\|(1+\|\sigma\|^2)^{s/2}\hat v(\sigma)\|_{0,\mathbb R_\sigma^N}^2\}^{1/2}, \tag{1.12}
$$

where $\hat v$ denotes the Fourier transform of $v$.

$2^\circ)$ When $\Omega$ is an open subset of $\mathbb R^N$, we define

$$
H^s(\Omega)=\{v\in L^2(\Omega);\ \exists\tilde v\in H^s(\mathbb R^N)\text{ with }\tilde v|_\Omega=v\} \tag{1.13}
$$

with the norm:

$$
\|v\|_{s,\Omega}=
\inf_{\substack{\tilde v\in H^s(\mathbb R^N)\\\tilde v|_\Omega=v}}
\|\tilde v\|_{s,\mathbb R^N}. \tag{1.14}
$$

As mentioned above, we have the following relation between $H^s(\Omega)$ and $W^{s,2}(\Omega)$.

**Lemma 1.3.** *Let $\Omega$ be a bounded Lipschitz-continuous open subset of $\mathbb R^N$. Then algebraically and topologically, we have*

$$
W^{s,2}(\Omega)=H^s(\Omega)\qquad\forall s>0.
$$

*In addition, when $s$ is an integer (1.11) defines the classical Sobolev space $H^m(\Omega)$ with an equivalent norm.*

Now, we are in a position to examine the boundary values of functions in $W^{s,p}(\Omega)$. We assume that $\Omega$ is a bounded open subset of $\mathbb R^N$ with a boundary $\Gamma$ that is at least Lipschitz-continuous. Let us first define what we mean by the space $W^{s,p}(\Gamma)$. According to Definition 1.1, we can view $\Gamma$ locally as an $N-1$ dimensional submanifold of $\mathbb R^N$ by means of the mapping

$$
\Phi(y')=(y',\phi(y'))
$$

from $\mathcal O'$ onto $\Gamma\cap\mathcal O$. Then we set the following definition.

**Definition 1.4.** Let $\Omega$ be a bounded open subset of $\mathbb R^N$ with a boundary $\Gamma$ of class $\mathcal C^{k,1}$ for some integer $k\geq0$. A distribution $u$ on $\Gamma$ belongs to $W^{s,p}(\Gamma)$ for $s\leq k+1$ if $u\circ\Phi$ belongs to $W^{s,p}(\mathcal O'\cap\Phi^{-1}(\Gamma\cap\mathcal O))$ for all possible $\mathcal O$ and $\phi$ fulfilling the assumptions of Definition 1.1.

Let $(\mathcal O_j,\Phi_j)_{1\leq j\leq J}$ be any atlas of $\Gamma$ such that each pair $(\mathcal O_j,\Phi_j)$ satisfies the hypotheses of the above definition. Then one possible Banach norm for $W^{s,p}(\Gamma)$

<!-- PDF page 22 / printed page 8 -->

is the functional:

$$
u\mapsto\left\{\sum_{j=1}^J
\|u\circ\Phi_j\|_{s,p,\mathcal O'_j\cap\Phi_j^{-1}(\Gamma\cap\mathcal O_j)}^p
\right\}^{1/p}. \tag{1.15}
$$

However, this norm is clumsy and we shall replace it by more convenient equivalent norms. For example, when $s=0$ we shall use the more familiar $L^p$-norm:

$$
\|u\|_{0,p,\Gamma}=\left\{\int_\Gamma|u(x)|^p\,ds(x)\right\}^{1/p}
$$

where $ds$ denotes the surface measure of $\Gamma$. At this stage, it is worthwhile to point out that the density result of Theorem 1.2 as well as the Sobolev's Imbedding Theorem 1.3 (with dimension $N-1$) are also valid on $\Gamma$.

Now, let $u$ be a function of $\mathcal D(\bar\Omega)$ and let us denote its boundary values by $\gamma_0u$. The following trace theorem extends the operator $\gamma_0$ to functions in $W^{s,p}(\Omega)$.

**Theorem 1.5.** *Let $\Omega$ be like in Definition 1.4 and let $p\geq1$ and $s\geq0$ be two real numbers such that $s\leq k+1$, $s-1/p=l+\sigma$ where $l\geq0$ is an integer and $0<\sigma<1$. Then the mapping $u\mapsto\gamma_0u$ defined on $\mathcal D(\bar\Omega)$ has a unique linear continuous extension as an operator from*

$$
W^{s,p}(\Omega)\quad\text{onto }W^{s-1/p,p}(\Gamma).
$$

*Moreover, in $W^{1,p}(\Omega)$ we have:*

$$
\operatorname{Ker}(\gamma_0)=W_0^{1,p}(\Omega).
$$

For such $s$ and $p$, this theorem suggests the following norm on $W^{s-1/p,p}(\Gamma)$ which can be proved to be equivalent to (1.15):

$$
\|f\|_{s-1/p,p,\Gamma}=
\inf_{\substack{v\in W^{s,p}(\Omega)\\\gamma_0v=f}}
\|v\|_{s,p,\Omega}. \tag{1.16}
$$

When $p=2$, (1.16) is a Hilbert norm. In this text, we shall mainly use the spaces $H^{1/2}(\Gamma)$ and $H^{3/2}(\Gamma)$ corresponding to $p=2$ and respectively $s=1$ or $2$. We shall also be interested in $H^{-1/2}(\Gamma)$, the dual space of $H^{1/2}(\Gamma)$ equipped with the obvious dual norm:

$$
\|f^*\|_{-1/2,\Gamma}=
\sup_{\substack{f\in H^{1/2}(\Gamma)\\f\neq0}}
\frac{\langle f^*,f\rangle}{\|f\|_{1/2,\Gamma}}, \tag{1.17}
$$

where again $\langle\cdot,\cdot\rangle$ denotes the duality pairing between $H^{-1/2}(\Gamma)$ and $H^{1/2}(\Gamma)$. Here again, we observe that $\langle\cdot,\cdot\rangle$ is an extension of the scalar product of $L^2(\Gamma)$ in the sense that when $f^*\in L^2(\Gamma)$, we can identify $\langle f^*,f\rangle$ with

$$
\int_\Gamma f^*(x)f(x)\,ds(x).
$$
