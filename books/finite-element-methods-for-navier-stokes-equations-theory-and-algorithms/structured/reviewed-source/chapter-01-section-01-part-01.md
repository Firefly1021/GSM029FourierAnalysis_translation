# Chapter I. Mathematical Foundation of the Stokes Problem

## §1. Generalities on Some Elliptic Boundary Value Problems

This paragraph contains a short survey on the Dirichlet's and Neumann's problems for the harmonic and biharmonic operators.

### 1.1. Basic Concepts on Sobolev Spaces

<!-- PDF page 15 / printed page 1 -->

Our purpose here is to recall the main notions and results, concerning the classical Sobolev spaces, which we shall use later on. Although they are stated without proof, these results are complete, rigorous and fairly general. Some of them, like the trace theorems, will only play a small part as theoretical tools in subsequent proofs and readers who are not familiar with such specialized mathematics need not dwell on them. But others, like the Sobolev Imbedding Theorem will be of constant use. The reader will find more details in references like Nečas [58] or Adams [1].

To simplify the discussion, we shall work from now on with real-valued functions, but of course every result stated here will carry on to complex-valued functions.

Let $\Omega$ denote an open subset of $\mathbb R^N$ with boundary $\Gamma$. We define $\mathcal D(\Omega)$ to be the linear space of infinitely differentiable functions, with compact support on $\Omega$. Then, we set

$$
\mathcal D(\Omega)=\{\phi|_\Omega;\ \phi\in\mathcal D(\mathbb R^N)\}
$$

or equivalently, if $\mathcal O$ denotes any open subset of $\mathbb R^N$ such that $\bar\Omega\subset\mathcal O$,

$$
\mathcal D(\bar\Omega)=\{\phi|_\Omega;\ \phi\in\mathcal D(\mathcal O)\}.
$$

Now, let $\mathcal D'(\Omega)$ denote the dual space of $\mathcal D(\Omega)$, often called the space of distributions on $\Omega$. We denote by $\langle\cdot,\cdot\rangle$ the duality pairing between $\mathcal D'(\Omega)$ and $\mathcal D(\Omega)$ and we remark that when $f$ is a locally integrable function, then $f$ can be identified with a distribution by

$$
\langle f,\phi\rangle=\int_\Omega f(x)\phi(x)\,dx\qquad\forall\phi\in\mathcal D(\Omega).
$$

<!-- PDF page 16 / printed page 2 -->

In other words, $\langle\cdot,\cdot\rangle$ is an extension of the scalar product of $L^2(\Omega)$. Now, we can define the derivatives of distributions. Let $\alpha=(\alpha_1,\ldots,\alpha_N)\in\mathbb N^N$ and set

$$
|\alpha|=\sum_{i=1}^N\alpha_i.
$$

For $u$ in $\mathcal D'(\Omega)$, we define $\partial^\alpha u$ in $\mathcal D'(\Omega)$ by:

$$
\langle\partial^\alpha u,\phi\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha\phi\rangle
\qquad\forall\phi\in\mathcal D(\Omega);
$$

when $u$ is $\alpha$ times differentiable, $\partial^\alpha u$ coincides with the usual notion of derivative:

$$
\partial^\alpha u=
\frac{\partial^{|\alpha|}u}
{\partial x_1^{\alpha_1}\cdots\partial x_N^{\alpha_N}}.
$$

For each integer $m\geq0$ and real $p$ with $1\leq p\leq\infty$, we define the Sobolev space:

$$
W^{m,p}(\Omega)=\{v\in L^p(\Omega);\ \partial^\alpha v\in L^p(\Omega)\quad\forall|\alpha|\leq m\},
$$

which is a Banach space for the norm:

$$
\|u\|_{m,p,\Omega}=\left(\sum_{|\alpha|\leq m}\int_\Omega|\partial^\alpha u(x)|^p\,dx\right)^{1/p}
\qquad p<\infty \tag{1.1}
$$

or

$$
\|u\|_{m,\infty,\Omega}=\max_{|\alpha|\leq m}\left(\operatorname*{ess\,sup}_{x\in\Omega}|\partial^\alpha u(x)|\right),
\qquad p=\infty.
$$

The space $W^{m,p}(\Omega)$ is separable for $1\leq p<\infty$ and reflexive for $1<p<\infty$. We also provide $W^{m,p}(\Omega)$ with the following seminorm

$$
|u|_{m,p,\Omega}=\left(\sum_{|\alpha|=m}\int_\Omega|\partial^\alpha u(x)|^p\,dx\right)^{1/p},
\qquad\text{for }p<\infty, \tag{1.2}
$$

and we make the above modification when $p=\infty$. If $u$ belongs to $W^{m,p}(\mathcal O)$ for every measurable, compact proper subset $\mathcal O$ of $\Omega$ we say that $u$ is locally in $W^{m,p}(\Omega)$ and we write

$$
u\in W^{m,p}_{\mathrm{loc}}(\Omega).
$$

When $p=2$, $W^{m,2}(\Omega)$ is usually denoted by $H^m(\Omega)$, and if there is no ambiguity, we drop the subscript $p=2$ when referring to its norm and seminorm. $H^m(\Omega)$ is a Hilbert space for the scalar product:

$$
(u,v)_{m,\Omega}=\sum_{|\alpha|\leq m}\int_\Omega\partial^\alpha u(x)\partial^\alpha v(x)\,dx. \tag{1.3}
$$

In particular, we write the scalar product of $L^2(\Omega)$ with no subscript at all.

Parallel to the Sobolev spaces, we recall the familiar definition of $\mathcal C^m$-functions:

$\mathcal C^0(\Omega)$ denotes the space of continuous functions defined in $\Omega$ and

<!-- PDF page 17 / printed page 3 -->

$$
\mathcal C^m(\Omega)=\{u\in\mathcal C^0(\Omega);\ \partial^\alpha u\in\mathcal C^0(\Omega)\quad\forall|\alpha|\leq m\}.
$$

As the $\mathcal C^m$-functions are not necessarily bounded we also introduce the space

$$
\mathcal C^m(\bar\Omega)=\{u\in\mathcal C^m(\Omega);\ \partial^\alpha u\text{ are bounded and uniformly continuous on }\Omega
\quad\forall0\leq|\alpha|\leq m\}.
$$

Likewise, we define the space $\mathcal C^{m,1}(\bar\Omega)$:

$$
\mathcal C^{m,1}(\bar\Omega)=\{u\in\mathcal C^m(\bar\Omega);\ \partial^\alpha u\text{ are Lipschitz-continuous in }\bar\Omega
\quad\forall0\leq|\alpha|\leq m\}.
$$

For $m\geq0$, $\mathcal C^m(\bar\Omega)$ and $\mathcal C^{m,1}(\bar\Omega)$ are Banach spaces for the respective norms:

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

where $\|x\|$ denotes the Euclidean norm of $\mathbb R^N$.

As $\mathcal D(\Omega)\subset W^{m,p}(\Omega)$, we define

$$
W_0^{m,p}(\Omega)=\overline{\mathcal D(\Omega)}^{W^{m,p}(\Omega)},
$$

i.e. $W_0^{m,p}(\Omega)$ is the closure of $\mathcal D(\Omega)$ for the norm $\|\cdot\|_{m,p,\Omega}$. When $m\geq1$ and $\Omega$ is a proper subset of $\mathbb R^N$ then $W_0^{m,p}(\Omega)$ is generally a proper subspace of $W^{m,p}(\Omega)$ and we shall characterize its functions further on. On the other hand, when $m=0$ we have the following result.

**Lemma 1.1.** *The space $\mathcal D(\Omega)$ is dense in $L^p(\Omega)$ for $1\leq p<\infty$.*

The next theorem, called the Poincaré-Friedrichs inequality, asserts that the mapping $v\mapsto|v|_{m,\Omega}$ is a norm on $H_0^m(\Omega)$, equivalent to $\|\cdot\|_{m,\Omega}$.

**Theorem 1.1.** *If $\Omega$ is connected and bounded at least in one direction, then for each integer $m\geq0$, there exists a constant $K=K(m,\Omega)>0$ such that*

$$
\|v\|_{m,\Omega}\leq K|v|_{m,\Omega}qquad\forall v\in H_0^m(\Omega). \tag{1.4}
$$

For $1\leq p<\infty$, we denote by $W^{-m,p'}(\Omega)$ the dual space of $W_0^{m,p}(\Omega)$ normed by:

$$
\|f\|_{-m,p',\Omega}=
\sup_{\substack{v\in W_0^{m,p}(\Omega)\\v\neq0}}
\frac{\langle f,v\rangle}{\|v\|_{m,p,\Omega}}, \tag{1.5}
$$

where $p'$ satisfies

$$
\frac1p+\frac1{p'}=1. \tag{1.6}
$$

The following lemma characterizes the functionals of $W^{-m,p'}(\Omega)$.

<!-- PDF page 18 / printed page 4 -->

**Lemma 1.2.** *Let $p$ and $p'$ satisfy (1.6) with $1\leq p<\infty$. A distribution $f$ belongs to $W^{-m,p'}(\Omega)$ if and only if there exist functions $f_\alpha\in L^{p'}(\Omega)$, for $|\alpha|\leq m$, such that*

$$
f=\sum_{|\alpha|\leq m}\partial^\alpha f_\alpha.
$$

Nearly all properties of Sobolev spaces on a domain $\Omega$ require some regularity of the boundary $\Gamma$: It is important to define this concept of regularity with precision. The following definition is taken from Grisvard [42].

**Definition 1.1.** Let $\Omega$ be an open subset of $\mathbb R^N$. We say that its boundary $\Gamma$ is continuous (resp. Lipschitz-continuous, of class $\mathcal C^m$, of class $\mathcal C^{m,1}$ for some integer $m>0$) if for every $x\in\Gamma$ there exists a neighborhood $\mathcal O$ of $x$ in $\mathbb R^N$ and new orthogonal coordinates $y=(y',y_N)$ where $y'=(y_1,\ldots,y_{N-1})$, such that:

i) $\mathcal O$ is a hypercube in the new coordinates:

$$
\mathcal O=\{y;\ -a_j<y_j<a_j,\ 1\leq j\leq N\}.
$$

ii) There exists a continuous (resp. Lipschitz-continuous, $\mathcal C^m$, $\mathcal C^{m,1}$) function $\phi$ defined in

$$
\mathcal O'=\{y';\ -a_j<y_j<a_j,\ 1\leq j\leq N-1\}
$$

that satisfies:

$$
|\phi(y')|\leq a_N/2\qquad\forall y'\in\mathcal O',
$$

$$
\Omega\cap\mathcal O=\{y;\ y_N<\phi(y')\},
\qquad
\Gamma\cap\mathcal O=\{y;\ y_N=\phi(y')\}.
$$

Essentially, this definition means that locally $\Omega$ is below the graph of some function $\phi$, $\Gamma$ is represented by the graph of $\phi$ and the regularity of $\Gamma$ is determined by that of $\phi$. It is important to point out that, with this definition, a domain with a continuous boundary is never on both sides of $\Gamma$ at any point of $\Gamma$. In particular, domains with cuts or cusps are forbidden, but boundaries with corners are allowed. The most straightforward example of domain with a Lipschitz-continuous boundary is a bounded polyhedron in $\mathbb R^3$ or a bounded polygon in $\mathbb R^2$.

To shorten the text, we shall say that $\Omega$ is Lipschitz-continuous when it has a Lipschitz-continuous boundary.

Note that a Lipschitz-continuous boundary has almost everywhere a unit normal vector $\mathbf n$. Furthermore, for $m\geq1$ a $\mathcal C^{m,1}$ boundary $\Gamma$ has a normal vector that belongs to $\mathcal C^{m-1,1}(\Gamma)^N$; if $\Omega$ is bounded, this normal vector can be extended to a vector field that belongs to $\mathcal C^{m-1,1}(\bar\Omega)^N$. Likewise, if $\Omega$ is a bounded domain with a Lipschitz-continuous boundary $\Gamma$, the distance function:

$$
d(x,\Gamma)=\inf_{y\in\Gamma}\|x-y\|
$$

belongs to $W^{1,\infty}(\Omega)$.

The next theorem shows that smooth functions are dense in $W^{m,p}(\Omega)$.
