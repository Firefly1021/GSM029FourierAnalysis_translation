<!-- Restored against original 360 dpi scan. PDF pages 32--36 / printed pages 18--22. -->

<!-- PDF page 32 / printed page 18 -->

## 2 Function Spaces for the Stokes Problem

A rigorous analysis of the Stokes problem requires special function spaces involving the divergence and curl of vector fields. In almost all publications, the crucial properties of these spaces stem from a powerful and difficult theorem proved by De Rham [68] which says essentially:

$$
\left\{\begin{minipage}{0.78\linewidth}
if a distribution vector field $\mathbf u$ satisfies $\langle\mathbf u,\boldsymbol\phi\rangle=0$ for all divergence-free functions of $\mathcal D$ then $\mathbf u=\mathbf{grad}\,S$ for some distribution $S$.
\end{minipage}\right. \tag{2.0}
$$

However, this theorem is far from necessary and we present in this paragraph a different approach inspired from Tartar [78].

### 2.1 Preliminary Results

The following theorem, due to Peetre [63] and Tartar [78], will be used several times in this text.

**Theorem 2.1.** *Let $E_1,E_2,E_3$ be three Banach spaces, $A\in\mathcal L(E_1;E_2)$ and $B$ a compact operator in $\mathcal L(E_1;E_3)$ such that*

$$
\|u\|_{E_1}\cong\|Au\|_{E_2}+\|Bu\|_{E_3}\qquad\forall u\in E_1. \tag{2.1}
$$

*Then the following properties hold.*

$1^\circ)$ *The dimension of $\operatorname{Ker}(A)$ is finite; the mapping $A$ is an isomorphism from $E_1/\operatorname{Ker}(A)$ onto $\mathcal R(A)$; $\mathcal R(A)$ is a closed subspace of $E_2$.*

$2^\circ)$ *There exists a constant $C_0$ such that, if $F$ is a Banach space and $L\in\mathcal L(E_1;F)$ vanishes on $\operatorname{Ker}(A)$, then*

$$
\|Lu\|_F\leq C_0\|L\|_{\mathcal L(E_1;F)}\|Au\|_{E_2}\qquad\forall u\in E_1. \tag{2.2}
$$

$3^\circ)$ *If $G$ is a Banach space and $M\in\mathcal L(E_1;G)$ satisfies*

$$
Mu\neq0\qquad\forall u\in\operatorname{Ker}(A)-\{0\}, \tag{2.3}
$$

*then*

$$
\|u\|_{E_1}\cong\|Au\|_{E_2}+\|Mu\|_G. \tag{2.4}
$$

**Proof.** $1^\circ)$ Here we are going to use a well known result (cf. Taylor [80]) which says that if the unit sphere is compact in a normed linear space $V$ then $V$ is finite-dimensional. Let us apply this result to $\operatorname{Ker}(A)$. First observe that by virtue of (2.1), $\|u\|_{E_1}$ and $\|Bu\|_{E_3}$ are two equivalent norms on $\operatorname{Ker}(A)$. Now, let $(u_n)$ be a bounded sequence of $\operatorname{Ker}(A)$. Since $B$ is compact, we can extract a subsequence $(u_\mu)$ such that $Bu_\mu$ converges in $E_3$. Therefore $(u_\mu)$ is a Cauchy sequence in $E_1$, and hence a convergent sequence in $\operatorname{Ker}(A)$. Thus the unit sphere is compact in $\operatorname{Ker}(A)$ and hence the dimension of $\operatorname{Ker}(A)$ is finite.

<!-- PDF page 33 / printed page 19 -->

Now that we know that $\operatorname{Ker}(A)$ is a finite-dimensional subspace of $E_1$, we can introduce the quotient space

$$
X=E_1/\operatorname{Ker}(A),
$$

which is a Banach space for the familiar quotient norm

$$
\|\dot u\|_X=\inf_{u\in\dot u}\|u\|_{E_1}.
$$

In addition, because $\operatorname{Ker}(A)$ is finite-dimensional, the above infimum is attained, i.e. each class $\dot u$ has a representative $\tilde u$ such that

$$
\|\dot u\|_X=\|\tilde u\|_{E_1}\qquad\forall\dot u\in X.
$$

As $A$ is a linear, continuous and one-to-one mapping from $X$ onto $\mathcal R(A)$, to establish the announced isomorphism it suffices to prove that $A$ has a continuous inverse, i.e. there exists a constant $C>0$ such that

$$
\|\dot u\|_X\leq C\|A\dot u\|_{E_2}\qquad\forall\dot u\in X. \tag{2.5}
$$

This is achieved by contradiction: assume that there exists a sequence $(\dot u_n)$ in $X$ such that

$$
\|\dot u_n\|_X=1,\qquad\lim_{n\to\infty}A\dot u_n=0\quad\text{in }E_2.
$$

Hence

$$
\|\tilde u_n\|_{E_1}=1,\qquad\lim_{n\to\infty}\|A\tilde u_n\|_{E_2}=0.
$$

Therefore, we can extract a subsequence $(\tilde u_\mu)$ such that $(B\tilde u_\mu)$ converges in $E_3$. Then (2.1) implies that $(\tilde u_\mu)$ is a Cauchy sequence in $E_1$. Thus, there exists $u$ in $\operatorname{Ker}(A)$ such that $\tilde u_\mu\to u$ in $E_1$. This implies that $\dot u_\mu\to0$, which contradicts our hypothesis.

Finally, since $A$ is an isomorphism from $X$ onto $\mathcal R(A)$ and since $X$ is a Banach space, it follows immediately that $\mathcal R(A)$ is also a Banach space. Therefore $\mathcal R(A)$ is a closed subspace of $E_2$.

$2^\circ)$ Since $L$ vanishes on $\operatorname{Ker}(A)$, we can write

$$
Lu=L\dot u=LA^{-1}Au\qquad\forall u\in E_1.
$$

Therefore

$$
\|Lu\|_F\leq\|L\|_{\mathcal L(E_1;F)}\|A^{-1}\|_{\mathcal L(\mathcal R(A);X)}\|Au\|_{E_2}\qquad\forall u\in E_1,
$$

thus yielding (2.2) with $C_0=\|A^{-1}\|_{\mathcal L(\mathcal R(A);X)}$.

$3^\circ)$ Finally, let us prove that there exists a constant $C>0$ such that

$$
\|Au\|_{E_2}+\|Mu\|_G\geq C\|u\|_{E_1}\qquad\forall u\in E_1.
$$

Again, we proceed by contradiction. Let $(u_n)$ be a sequence in $E_1$ such that

$$
\lim_{n\to\infty}(\|Au_n\|_{E_2}+\|Mu_n\|_G)=0,\qquad\|u_n\|_{E_1}=1.
$$

<!-- PDF page 34 / printed page 20 -->

Then, there is a subsequence $(u_\mu)$ such that $(Bu_\mu)$ converges in $E_3$. Hence $(u_\mu)$ is a Cauchy sequence in $E_1$ and therefore

$$
\lim_{\mu\to\infty}u_\mu=u,
$$

with

$$
Au=0,\qquad Mu=0,\qquad\|u\|_{E_1}=1.
$$

But then, (2.3) implies that $u=0$; this leads to a contradiction.

Now, let $\Omega$ be a bounded subset of $\mathbb R^N$ with a Lipschitz-continuous boundary $\Gamma$. From now on, we shall often deal with vector-valued functions. We shall distinguish vectors by means of bold-face characters and extend naturally all the previous norms to vectors as follows: if $\mathbf v=(v_1,\ldots,v_N)$ then

$$
\|\mathbf v\|_{m,p,\Omega}=\left(\sum_{i=1}^N\|v_i\|_{m,p,\Omega}^p\right)^{1/p}.
$$

The next theorem is part of a general result of functional analysis due to Nečas [57]. Its proof is long and delicate because it only assumes the Lipschitz-continuity of the boundary. When the boundary is smooth there is an alternate, easier proof that can be found in Duvaut & Lions [26]. Here we omit either proof for they are both outside the scope of this book.

**Theorem 2.2.** *Let $\Omega$ be a bounded, Lipschitz-continuous open set. There exists a constant $C>0$, depending only on $\Omega$, such that*

$$
\|p\|_{0,\Omega}\leq C\{\|p\|_{-1,\Omega}+\|\mathbf{grad}\,p\|_{-1,\Omega}\}\qquad\forall p\in L^2(\Omega). \tag{2.6}
$$

As an immediate consequence, we have:

**Corollary 2.1.** $1^\circ)$ *Under the assumptions of Theorem 2.2, the range of the gradient operator $\mathbf{grad}\in\mathcal L(L^2(\Omega);H^{-1}(\Omega)^N)$ is a closed subspace of $H^{-1}(\Omega)^N$.*

$2^\circ)$ *If in addition $\Omega$ is connected, there exists a constant $C>0$, depending only on $\Omega$, such that*

$$
\|\dot p\|_{L^2(\Omega)/\mathbb R}\leq C\|\mathbf{grad}\,\dot p\|_{-1,\Omega}\qquad\forall\dot p\in L^2(\Omega)/\mathbb R. \tag{2.7}
$$

$3^\circ)$ *Let $\omega$ be an open subset of $\Omega$ with positive measure. There exists a constant $C_\omega>0$ depending only on $\Omega$ and $\omega$ such that*

$$
\|p\|_{0,\Omega}\leq C_\omega\{\|p\|_{0,\omega}+\|\mathbf{grad}\,p\|_{-1,\Omega}\}\qquad\forall p\in L^2(\Omega). \tag{2.8}
$$

**Proof.** The idea is to apply Theorem 2.1 with $E_1=L^2(\Omega)$, $E_2=H^{-1}(\Omega)^N$, $E_3=H^{-1}(\Omega)$, $A=\mathbf{grad}$ and $B$ the canonical imbedding of $L^2(\Omega)$ into $H^{-1}(\Omega)$ which is compact according to Theorem 1.3. Clearly,

$$
\|p\|_{-1,\Omega}+\|\mathbf{grad}\,p\|_{-1,\Omega}\leq C_1\|p\|_{0,\Omega}\qquad\forall p\in L^2(\Omega).
$$

<!-- PDF page 35 / printed page 21 -->

Therefore, (2.1) follows immediately from (2.6), thus proving the first conclusion.

Likewise, since $\Omega$ is connected, $\mathbb R=\operatorname{Ker}(\mathbf{grad})$ and (2.5) proves (2.7).

Finally, let $G=L^2(\omega)$ and $M:L^2(\Omega)\to L^2(\omega)$ be the identity mapping. Because $\omega$ has positive measure, $Mc\neq0$ for all constants $c\neq0$, and (2.4) implies (2.8).

The second Corollary gives an important result of regularity.

**Corollary 2.2.** *Let $\Omega$ be connected and satisfy the assumptions of Theorem 2.2. If*

$$
p\in L^2_{\mathrm{loc}}(\Omega),\qquad\mathbf{grad}\,p\in H^{-1}(\Omega)^N,
$$

*then $p\in L^2(\Omega)$.*

**Proof.** We set

$$
X=\{p\in L^2_{\mathrm{loc}}(\Omega);\ \mathbf{grad}\,p\in H^{-1}(\Omega)^N\}
$$

and

$$
\llbracket p\rrbracket_\omega=\|p\|_{0,\omega}+\|\mathbf{grad}\,p\|_{-1,\Omega},
$$

where $\omega\Subset\Omega$ has positive measure. Then $\llbracket\cdot\rrbracket_\omega$ is a norm on $X$ and we infer from (2.8) that $\llbracket\cdot\rrbracket_\omega$ and $\|\cdot\|_{0,\Omega}$ are two equivalent norms on $L^2(\Omega)$. Thus $L^2(\Omega)$ is a Banach space for the norm $\llbracket\cdot\rrbracket_\omega$ and hence it suffices to prove that $L^2(\Omega)$ is dense in $X$ for $\llbracket\cdot\rrbracket_\omega$.

$1^\circ)$ Assume for the moment that $\Omega$ is strictly star-shaped with respect to one of its points, say $y$. This amounts to say that, by taking $y$ as origin,

$$
\theta\bar\Omega\subset\Omega\quad\forall\theta\in[0,1),\qquad\bar\Omega\subset\theta\Omega\quad\forall\theta>1.
$$

Here, we take $\theta>1$ and set $\Omega_\theta=\theta\Omega$. For a continuous function $\phi$ on $\Omega$ we make the change of variable $\phi\mapsto\phi_\theta$ defined on $\Omega_\theta$ by

$$
\phi_\theta(x)=\phi(x/\theta)\qquad\forall x\in\Omega_\theta,
$$

which we extend to distributions, $u\in\mathcal D'(\Omega)\mapsto u_\theta\in\mathcal D'(\Omega_\theta)$ by

$$
\langle u_\theta,\phi\rangle=\theta^N\langle u,\phi_{1/\theta}\rangle\qquad\forall\phi\in\mathcal D(\Omega_\theta).
$$

Then it is easy to check that

$$
\mathbf{grad}(u_\theta)=(1/\theta)(\mathbf{grad}\,u)_\theta\qquad\forall u\in\mathcal D'(\Omega),
$$

$$
\lim_{\theta\to1}\|u_\theta-u\|_{0,\Omega}=0\qquad\forall u\in L^2(\Omega),
$$

$$
\lim_{\theta\to1}\|u_\theta-u\|_{-1,\Omega}=0\qquad\forall u\in H^{-1}(\Omega).
$$

Hence, if $p\in X$ then $p_\theta\in L^2(\Omega)$ for all $\theta>1$ and in view of the above remarks, we readily derive that

<!-- PDF page 36 / printed page 22 -->

$$
\lim_{\theta\to1}\llbracket p_\theta-p\rrbracket_\omega=0.
$$

Therefore $p\in L^2(\Omega)$.

$2^\circ)$ In the general case, we use the following property (cf. for example Bernardi [8]):

*A bounded, Lipschitz-continuous open set is the union of a finite number of star-shaped, Lipschitz-continuous open sets.*

Clearly, it suffices to apply the above argument to each of these sets to derive the desired result on the entire domain.

### 2.2 Some Properties of Spaces Related to the Divergence Operator

Unless otherwise specified, we assume in this section that $\Omega$ is a bounded subset of $\mathbb R^N$ with a Lipschitz-continuous boundary $\Gamma$.

For $\mathbf v=(v_1,\ldots,v_N)$, we define the divergence operator by

$$
\operatorname{div}\mathbf v=\sum_{i=1}^N(\partial v_i/\partial x_i).
$$

Note the identity

$$
\operatorname{div}(\mathbf{grad}\,v)=\Delta v.
$$

Let us introduce the following spaces of divergence-free functions:

$$
\mathcal V=\{\boldsymbol\phi\in\mathcal D(\Omega)^N;\ \operatorname{div}\boldsymbol\phi=0\},\qquad V=\{\mathbf v\in H_0^1(\Omega)^N;\ \operatorname{div}\mathbf v=0\}.
$$

Here we equip $H_0^1(\Omega)^N$ with the norm $|\cdot|_{1,\Omega}$, equivalent to $\|\cdot\|_{1,\Omega}$ by virtue of Poincaré's Theorem 1.1. Since $V$ is a closed subspace of $H_0^1(\Omega)^N$, we have the decomposition

$$
H_0^1(\Omega)^N=V\oplus V^\perp,
$$

where $V^\perp$ denotes the orthogonal of $V$ in $H_0^1(\Omega)^N$ for the scalar product $(\mathbf{grad}\,\mathbf u,\mathbf{grad}\,\mathbf v)$ associated with $|\cdot|_{1,\Omega}$.

The following lemma establishes a first coarse version of De Rham's Theorem (2.0).

**Lemma 2.1.** *If $\mathbf f\in H^{-1}(\Omega)^N$ satisfies*

$$
\langle\mathbf f,\mathbf v\rangle=0\qquad\forall\mathbf v\in V, \tag{2.9}
$$

*then there exists $p\in L^2(\Omega)$ such that*

$$
\mathbf f=\mathbf{grad}\,p.
$$

*When $\Omega$ is connected, $p$ is unique up to an additive constant.*

<!-- The proof continues on PDF page 37 / printed page 23 in the immutable approved sample. -->
