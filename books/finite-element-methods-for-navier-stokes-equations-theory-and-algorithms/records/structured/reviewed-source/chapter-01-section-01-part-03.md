<!-- Restored against original 360 dpi scan. PDF pages 23--31 / printed pages 9--17. -->

<!-- PDF page 23 / printed page 9 -->

Apart from the boundary value operator $\gamma_0$, we shall also require the trace of the normal derivative $\gamma_1u$ defined for $u$ in $\mathcal D(\bar\Omega)$ by

$$
\gamma_1u=\partial u/\partial n=\sum_{i=1}^N\gamma_0(\partial u/\partial x_i)n_i. \tag{1.18}
$$

where $\mathbf n=(n_1,\ldots,n_N)$ denotes the unit outward normal to $\Gamma$. Then we can complete as follows the statement of Theorem 1.5.

**Theorem 1.6.** *We keep the assumptions of Theorem 1.5 with $l\geq1$. The mapping*

$$
u\mapsto\{\gamma_0u,\gamma_1u\}
$$

*defined on $\mathcal D(\bar\Omega)$ has a unique linear continuous extension as an operator from*

$$
W^{s,p}(\Omega)\quad\text{onto }W^{s-1/p,p}(\Gamma)\times W^{s-1-1/p,p}(\Gamma).
$$

*Moreover, in $W^{2,p}(\Omega)$ we have the following characterization:*

$$
\operatorname{Ker}\gamma_0\cap\operatorname{Ker}\gamma_1=W_0^{2,p}(\Omega).
$$

**Remark 1.1.** If the boundary of $\Omega$ has corners, its normal vector has jumps and it is obvious that $\partial u/\partial n$ is rough no matter how smooth $u$ can be. Nevertheless, it is possible to extend slightly the statement of Theorem 1.6. Assume that $\Omega$ is a bounded two-dimensional polygon; let $\Gamma_j$ denote the sides of $\Gamma$ and $\mathbf n_j$ the corresponding exterior unit normal, $1\leq j\leq J$. Then the mapping

$$
u\mapsto(\partial u/\partial n_j;\ 1\leq j\leq J)
$$

is linear, continuous and surjective from $W^{k+2,p}(\Omega)$ onto

$$
\prod_{j=1}^J W^{k+1-1/p,p}(\Gamma_j),
$$

for each integer $k\geq0$ and real $p\in(1,\infty)$. Note that there is no matching condition for $\partial u/\partial n$ at the vertices of $\Gamma$.

The situation of the boundary values of $u$ is a bit more complicated because there is usually a matching condition at the vertices of $\Gamma$. For the sake of simplicity, we shall just take $u$ in $W^{2,p}(\Omega)$. Denote the vertices of $\Gamma$ by $S_j$ with the convention that $S_{J+1}=S_1$. The mapping

$$
u\mapsto(h_j=u|_{\Gamma_j};\ 1\leq j\leq J)
$$

is linear, continuous and surjective from $W^{2,p}(\Omega)$ onto the subspace of

$$
\prod_{j=1}^J W^{2-1/p,p}(\Gamma_j)
$$

defined by the compatibility conditions

$$
h_j(S_{j+1})=h_{j+1}(S_{j+1}),\qquad1\leq j\leq J.
$$

<!-- PDF page 24 / printed page 10 -->

We close this section with two useful applications of Green's formula.

**Lemma 1.4.** *Let $\Omega$ be a bounded open subset of $\mathbb R^N$ with a Lipschitz-continuous boundary $\Gamma$.*

$1^\circ)$ *For $u$ and $v$ in $H^1(\Omega)$ and for $1\leq i\leq N$, we have:*

$$
\int_\Omega u(\partial v/\partial x_i)\,dx=-\int_\Omega(\partial u/\partial x_i)v\,dx+\int_\Gamma\gamma_0(uv)n_i\,ds. \tag{1.19}
$$

$2^\circ)$ *If in addition $u\in H^2(\Omega)$ we have:*

$$
\sum_{i=1}^N\int_\Omega\frac{\partial u}{\partial x_i}\frac{\partial v}{\partial x_i}\,dx=-\sum_{i=1}^N\int_\Omega\frac{\partial^2u}{\partial x_i^2}v\,dx+\sum_{i=1}^N\int_\Gamma\gamma_0\left(\frac{\partial u}{\partial x_i}v\right)n_i\,ds. \tag{1.20}
$$

Adopting the usual notations

$$
\Delta u=\sum_{i=1}^N\frac{\partial^2u}{\partial x_i^2},\qquad \mathbf{grad}\,u=(\partial u/\partial x_1,\ldots,\partial u/\partial x_N),
$$

(1.20) becomes

$$
(\mathbf{grad}\,u,\mathbf{grad}\,v)=-(\Delta u,v)+\int_\Gamma(\partial u/\partial n)\gamma_0v\,ds. \tag{1.21}
$$

## 1.2 Abstract Elliptic Theory

This section gives a brief account of a fundamental tool used in studying linear partial differential equations of elliptic type.

Let $V$ be a real Hilbert space with norm denoted by $\|\cdot\|_V$; let $V'$ be its dual space and let $\langle\cdot,\cdot\rangle$ denote the duality pairing between $V'$ and $V$. Let $(u,v)\mapsto a(u,v)$ be a real bilinear form on $V\times V$, $l$ an element of $V'$ and consider the following problem:

$$
\text{Find }u\in V\text{ such that}\qquad a(u,v)=\langle l,v\rangle\quad\forall v\in V. \tag{P}
$$

The following theorem is due to Lax & Milgram [49].

**Theorem 1.7.** *We assume that $a$ is continuous and elliptic on $V$, i.e. there exist two constants $M$ and $\alpha>0$ such that*

$$
|a(u,v)|\leq M\|u\|_V\|v\|_V\qquad\forall u,v\in V \tag{1.22}
$$

*and*

$$
a(v,v)\geq\alpha\|v\|_V^2\qquad\forall v\in V. \tag{1.23}
$$

*Then Problem (P) has one and only one solution $u$ in $V$. Moreover, the mapping $l\mapsto u$ is an isomorphism from $V'$ onto $V$.*

<!-- PDF page 25 / printed page 11 -->

**Corollary 1.2.** *When $a$ is symmetric---i.e. $a(u,v)=a(v,u)$ $\forall u,v\in V$---then the solution $u$ of (P) is also the only element of $V$ that minimizes the following quadratic functional (also called energy functional) on $V$:*

$$
J(v)=(1/2)a(v,v)-\langle l,v\rangle. \tag{1.24}
$$

## 1.3 Example 1: Dirichlet's Problem for the Laplace Operator

In all the examples, we assume that $\Omega$ is bounded and $\Gamma$ Lipschitz-continuous. Consider the following non-homogeneous Dirichlet's problem:

Given $f$ in $H^{-1}(\Omega)$ and $g$ in $H^{1/2}(\Gamma)$, find a function $u$ such that

$$
(D)\quad\begin{cases}
-\Delta u=f&\text{in }\Omega, \tag{1.25}\\
u=g&\text{on }\Gamma. \tag{1.26}
\end{cases}
$$

Let us formulate this problem in terms of Problem (P). We set $V=H_0^1(\Omega)$ and

$$
a(u,v)=(\mathbf{grad}\,u,\mathbf{grad}\,v).
$$

It is clear that $a$ is continuous in $H_0^1(\Omega)^2$, and owing to Theorem 1.1,

$$
a(v,v)=\|\mathbf{grad}\,v\|_{0,\Omega}^2=|v|_{1,\Omega}^2\geq C\|v\|_{1,\Omega}^2.
$$

Besides that, since $H^{1/2}(\Gamma)$ is the range space of $\gamma_0$ in $H^1(\Omega)$, let $u_0$ in $H^1(\Omega)$ satisfy $u_0=g$ on $\Gamma$, and examine the following problem:

$$
(D')\quad\begin{cases}
\text{Find }u\in H^1(\Omega)\text{ such that}\\
u-u_0\in H_0^1(\Omega), \tag{1.27}\\
a(u-u_0,v)=\langle f,v\rangle-a(u_0,v)&\forall v\in H_0^1(\Omega). \tag{1.28}
\end{cases}
$$

Since $a$ is continuous, the mapping $v\mapsto\langle f,v\rangle-a(u_0,v)$ belongs to $H^{-1}(\Omega)$. Therefore, thanks to the Lax & Milgram's Theorem, Problem $(D')$ has one and only one solution $u$ in $H^1(\Omega)$.

It remains only to prove that $u$ may be characterized as the unique solution of Problem $(D)$. Taking $v\in\mathcal D(\Omega)$ in (1.28) gives

$$
a(u,v)=-\langle\Delta u,v\rangle=\langle f,v\rangle\qquad\forall v\in\mathcal D(\Omega).
$$

Hence $u$ satisfies (1.27) and (1.25). Conversely, every solution of $(D_1)$ is a solution of $(D')$ by the density of $\mathcal D(\Omega)$ in $H_0^1(\Omega)$. But

$$
u-u_0\in H_0^1(\Omega)\quad\text{iff }u=g\quad\text{on }\Gamma,
$$

therefore Problems $(D_1)$ and $(D)$ are the same.

<!-- PDF page 26 / printed page 12 -->

As far as the regularity of $u$ is concerned, we know from the Lax & Milgram's Theorem that the mapping $l\mapsto u-u_0$ is an isomorphism from $H^{-1}(\Omega)$ onto $H_0^1(\Omega)$. Therefore,

$$
\|u-u_0\|_{1,\Omega}\leq C_2\|l\|_{-1,\Omega}.
$$

Clearly,

$$
\|l\|_{-1,\Omega}\leq\|f\|_{-1,\Omega}+\|u_0\|_{1,\Omega}.
$$

Hence

$$
\|u\|_{1,\Omega}\leq C_3\{\|f\|_{-1,\Omega}+\|u_0\|_{1,\Omega}\}\quad\forall u_0\in H^1(\Omega)\text{ such that }u_0=g\text{ on }\Gamma.
$$

From definition (1.16) this implies that

$$
\|u\|_{1,\Omega}\leq C_3\{\|f\|_{-1,\Omega}+\|g\|_{1/2,\Gamma}\}.
$$

Thus, we have proved the following proposition:

**Proposition 1.1.** *Problem (D) has one and only one solution $u$ in $H^1(\Omega)$ and there exists a constant $C=C(\Omega)$ such that*

$$
\|u\|_{1,\Omega}\leq C\{\|f\|_{-1,\Omega}+\|g\|_{1/2,\Gamma}\}, \tag{1.29}
$$

*i.e. $u$ depends continuously upon the data of (D).*

When $f$ and $g$ are more regular, it is natural to expect that the solution $u$ of Problem (D) is also smoother. The next theorem states the precise regularity of $u$. Its proof, which is far outside the scope of this book, can be found for example in Grisvard [42].

**Theorem 1.8.** $1^\circ)$ *Let $\Omega$ be a bounded open subset of $\mathbb R^N$ with a $\mathcal C^{k+1,1}$ boundary $\Gamma$ for some integer $k\geq0$. Suppose that the data $f$ and $g$ of Problem (1.25)--(1.26) satisfy*

$$
f\in W^{k,p}(\Omega),\qquad g\in W^{k+2-1/p,p}(\Gamma)
$$

*for some real $p$ with $1<p<\infty$. Then $u\in W^{k+2,p}(\Omega)$ and there exists a constant $C=C(k,p,\Omega)$ such that*

$$
\|u\|_{k+2,p,\Omega}\leq C\{\|f\|_{k,p,\Omega}+\|g\|_{k+2-1/p,p,\Gamma}\}. \tag{1.30}
$$

$2^\circ)$ *When $\Omega$ is a two-dimensional bounded polygon with no reentrant corner, there exists a real $p_\Omega>2$ depending on the greatest inner angle of $\Gamma$ such that*

$$
u\in W^{2,p}(\Omega),\qquad1<p<p_\Omega,
$$

*whenever $f\in L^p(\Omega)$ and $(g|_{\Gamma_j};\ 1\leq j\leq J)\in\prod_{j=1}^J W^{2-1/p,p}(\Gamma_j)$ satisfies the matching conditions of Remark 1.1.*

$3^\circ)$ *If $\Omega$ is a bounded, convex polyhedron in three dimensions, the conclusion of $2^\circ)$ is still valid for the homogeneous Dirichlet problem $(g=0)$.*

<!-- PDF page 27 / printed page 13 -->

**Remark 1.2.** As an immediate application of this theorem with $g=0$, we see that when $\Omega$ is a bounded convex polygon in $\mathbb R^2$ (or polyhedron in $\mathbb R^3$) then the mapping $u\mapsto\Delta u$ is an isomorphism from $W^{2,p}(\Omega)\cap W_0^{1,p}(\Omega)$ onto $L^p(\Omega)$ for all $p\in(1,2+\varepsilon]$ for some $\varepsilon>0$. When the boundary of $\Omega$ is $\mathcal C^{1,1}$, this isomorphism holds for all $p\in(1,\infty)$.

## 1.4 Example 2: Neumann's Problem for the Laplace Operator

Here, we assume in addition that $\Omega$ is connected and we deal with the non-homogeneous Neumann's problem:

Find $u$ such that

$$
(N)\quad\begin{cases}
-\Delta u=f&\text{in }\Omega, \tag{1.31}\\
\partial u/\partial n=g&\text{on }\Gamma, \tag{1.32}\\
\text{where }f\in L^2(\Omega)\text{ and }g\in H^{-1/2}(\Gamma)\text{ satisfy}\\
\displaystyle\int_\Omega f\,dx+\langle g,1\rangle_\Gamma=0. \tag{1.33}
\end{cases}
$$

Since Problem (N) only involves the derivatives of $u$, it is clear that its solution is never unique. We turn the difficulty by seeking $u$ in the quotient space $H^1(\Omega)/\mathbb R$ equipped with the quotient norm

$$
\|\dot v\|_{H^1(\Omega)/\mathbb R}=\inf_{v\in\dot v}\|v\|_{1,\Omega}. \tag{1.34}
$$

The theorem below states an important property of this space; its proof can be found in Nečas [58].

**Theorem 1.9.** *Let $\Omega$ be a bounded, connected and Lipschitz-continuous open subset of $\mathbb R^N$. The space $H^1(\Omega)/\mathbb R$ is a Hilbert space for the quotient norm (1.34). Moreover, on this space the functional $\dot v\mapsto|v|_{1,\Omega}$ is a norm equivalent to (1.34).*

With this space, we can put Problem (N) into the abstract setting of Problem (P). Let $V=H^1(\Omega)/\mathbb R$,

$$
a(\dot u,\dot v)=(\mathbf{grad}\,u,\mathbf{grad}\,v),
$$

and

$$
l:\dot v\mapsto(f,v)+\langle g,v\rangle_\Gamma\qquad\forall v\in\dot v. \tag{1.35}
$$

Note that the right-hand side of (1.35) is independent of the particular $v\in\dot v$ thanks to the compatibility condition (1.33). Furthermore, $l\in V'$ because, owing to (1.16), we have

$$
|(f,v)+\langle g,v\rangle_\Gamma|\leq(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma})\inf_{v\in\dot v}\|v\|_{1,\Omega}.
$$

<!-- PDF page 28 / printed page 14 -->

Thus

$$
\|l\|_{V'}\leq\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma}. \tag{1.36}
$$

Obviously, $a(\dot u,\dot v)$ is continuous on $V\times V$, and by virtue of Theorem 1.9

$$
a(\dot v,\dot v)=|v|_{1,\Omega}^2\geq C_1\|\dot v\|_{H^1(\Omega)/\mathbb R}^2.
$$

Hence, by the Lax & Milgram's Theorem, the following problem

$$
(N')\quad\text{Find }\dot u\in H^1(\Omega)/\mathbb R\text{ satisfying}\qquad a(\dot u,\dot v)=\langle l,\dot v\rangle\quad\forall\dot v\in H^1(\Omega)/\mathbb R \tag{1.37}
$$

has a unique solution $\dot u\in H^1(\Omega)/\mathbb R$.

Let us interpret Problem $(N')$. When $v$ is restricted to $\mathcal D(\Omega)$, (1.37) yields (1.31). Next, by taking the scalar product of (1.31) with $v$ and comparing with (1.37), we find

$$
(\mathbf{grad}\,u,\mathbf{grad}\,v)=-(\Delta u,v)+\langle g,v\rangle_\Gamma\qquad\forall v\in H^1(\Omega). \tag{1.38}
$$

Therefore, Problem $(N')$ is equivalent to finding $u$ in $H^1(\Omega)$ satisfying (1.31) and (1.38).

It remains to interpret (1.38) as a boundary condition. At the present stage this cannot be done without assuming that $u\in H^2(\Omega)$. Then Green's formula (1.21) yields

$$
\int_\Gamma(\partial u/\partial n)v\,ds=\langle g,v\rangle_\Gamma\qquad\forall v\in H^1(\Omega),
$$

i.e. $\partial u/\partial n=g$ on $\Gamma$. Therefore, Problems (N) and $(N')$ are equivalent. Of course, this is not entirely satisfactory inasmuch as the existence of a solution of Problem (N) is subjected to the regularity of the solution of $(N')$. Although this regularity does generally hold, the more powerful tools of the next paragraph will eliminate this extra smoothness assumption.

Now, let us examine the dependence of the solution $\dot u$ of Problem $(N')$. According to the Lax & Milgram's Theorem 1.7, (1.36) and the equivalence Theorem 1.9, we obtain

$$
|u|_{1,\Omega}\leq C_2(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma}).
$$

We have thus proved the following result.

**Proposition 1.2.** *Problem $(N')$ has a unique solution $\dot u$ in $H^1(\Omega)/\mathbb R$ and this solution is continuous with respect to the data:*

<!-- PDF page 29 / printed page 15 -->

$$
|u|_{1,\Omega}\leq C(\|f\|_{0,\Omega}+\|g\|_{-1/2,\Gamma})\qquad\forall u\in\dot u. \tag{1.39}
$$

*Moreover, when $\dot u\in H^2(\Omega)/\mathbb R$ then it is also the only solution of Problem (N).*

As for the Dirichlet's problem, the solution of Problem $(N')$ is more regular when its data has extra smoothness. The precise result, which is also given by Grisvard [42], closely resembles Theorem 1.8.

**Theorem 1.10.** $1^\circ)$ *Let $\Omega$ be like in Theorem 1.8 and assume that the data $f$ and $g$ of Problem (1.37) satisfy*

$$
f\in W^{k,p}(\Omega),\qquad g\in W^{k+1-1/p,p}(\Gamma),\qquad1<p<\infty.
$$

*Then $\dot u\in W^{k+2,p}(\Omega)/\mathbb R$ and there exists a constant $C=C(k,p,\Omega)$ such that*

$$
\|\dot u\|_{W^{k+2,p}(\Omega)/\mathbb R}\leq C\{\|f\|_{k,p,\Omega}+\|g\|_{k+1-1/p,p,\Gamma}\}. \tag{1.40}
$$

$2^\circ)$ *When $\Omega$ is a two-dimensional bounded polygon with no reentrant corner, there exists a real $p_\Omega>2$ depending on the maximum inner angle of $\Gamma$ such that*

$$
\dot u\in W^{2,p}(\Omega)/\mathbb R,\qquad1<p<p_\Omega,
$$

*provided $f\in L^p(\Omega)$ and $(g|_{\Gamma_j};\ 1\leq j\leq J)\in\prod_{j=1}^J W^{1-1/p,p}(\Gamma_j)$.*

$3^\circ)$ *If $\Omega$ is a bounded, convex polyhedron in $\mathbb R^3$ the conclusion of $2^\circ)$ is valid for the homogeneous Neumann problem $(g=0)$.*

## 1.5 Example 3: Dirichlet's Problem for the Biharmonic Operator

Consider the non-homogeneous problem:

For $f$ given in $H^{-2}(\Omega)$, $g_1$ given in $H^{3/2}(\Gamma)$ and $g_2$ in $H^{1/2}(\Gamma)$, find $u$ such that

$$
(B)\quad\begin{cases}
\Delta^2u=f&\text{in }\Omega, \tag{1.41}\\
u=g_1&\text{on }\Gamma, \tag{1.42}\\
\partial u/\partial n=g_2&\text{on }\Gamma. \tag{1.43}
\end{cases}
$$

The function space naturally attached to this problem is $H_0^2(\Omega)$ and the bilinear form is

$$
a(u,v)=(\Delta u,\Delta v).
$$

This form is elliptic on $H_0^2(\Omega)$ because the mapping $v\mapsto\|\Delta v\|_{0,\Omega}$ is a norm on $H_0^2(\Omega)$ equivalent to the norm $\|\cdot\|_{2,\Omega}$. Indeed, for $v$ in $\mathcal D(\Omega)$, we can easily show by integrating by parts and interchanging derivatives that

$$
\|\Delta v\|_{0,\Omega}^2=|v|_{2,\Omega}^2. \tag{1.44}
$$

By density, the same result holds for the functions of $H_0^2(\Omega)$. The equivalence follows from Poincaré's Theorem 1.1.

<!-- PDF page 30 / printed page 16 -->

According to Theorem 1.6, if $\Gamma$ is $\mathcal C^{1,1}$, there exists a function $u_0$ in $H^2(\Omega)$ such that

$$
u_0=g_1\quad\text{on }\Gamma,\qquad\partial u_0/\partial n=g_2\quad\text{on }\Gamma. \tag{1.45}
$$

Thus we turn to the following problem:

$$
(B')\quad\begin{cases}
\text{Find }u\in H^2(\Omega)\text{ such that}\\
u-u_0\in H_0^2(\Omega), \tag{1.46}\\
a(u-u_0,v)=\langle f,v\rangle-a(u_0,v)&\forall v\in H_0^2(\Omega). \tag{1.47}
\end{cases}
$$

By the Lax & Milgram's Theorem 1.7, Problem $(B')$ has exactly one solution $u$ in $H^2(\Omega)$. Owing to (1.45) and (1.46), $u$ satisfies the boundary conditions $u=g_1$ and $\partial u/\partial n=g_2$ on $\Gamma$. Besides that, by restricting the test functions of (1.47) to $\mathcal D(\Omega)$, we find $\Delta^2u=f$ in $H^{-2}(\Omega)$. Therefore, $u$ is a solution of (B).

Conversely, as in the case of the Laplace operator, we can show that Problem (B) has at most one solution in $H^2(\Omega)$. From (1.47) and the equivalence of norms, we derive the bound

$$
\|u\|_{2,\Omega}\leq C_1(\|f\|_{-2,\Omega}+\|u_0\|_{2,\Omega})\qquad\forall u_0\text{ satisfying (1.45)},
$$

i.e.

$$
\|u\|_{2,\Omega}\leq C_2(\|f\|_{-2,\Omega}+\|g_1\|_{3/2,\Gamma}+\|g_2\|_{1/2,\Gamma}).
$$

These results are summed up in the proposition below:

**Proposition 1.3.** *If $\Gamma$ is $\mathcal C^{1,1}$, Problem (B) has exactly one solution $u$ in $H^2(\Omega)$, bounded as follows:*

$$
\|u\|_{2,\Omega}\leq C(\|f\|_{-2,\Omega}+\|g_1\|_{3/2,\Gamma}+\|g_2\|_{1/2,\Gamma}). \tag{1.48}
$$

The above analysis does not allow for corners since it assumes that $\Gamma$ is $\mathcal C^{1,1}$. This hypothesis plays a crucial part in the lifting operator $(g_1,g_2)\mapsto u_0$. Of course, if these non-homogeneous data are given directly in the form of a function $u_0$ in $H^2(\Omega)$ such that

$$
u=u_0\quad\text{on }\Gamma\quad\text{and}\quad\partial u/\partial n=\partial u_0/\partial n\quad\text{on }\Gamma,
$$

then Proposition 1.3 applies to a Lipschitz-continuous domain with $u_0$ instead of $g_1$ and $g_2$. Otherwise, we must alter a little the statement of Problem (B). Suppose that $\Omega$ is a two-dimensional bounded polygon. In view of Remark 1.1, let $\Gamma_j$ and $S_j$, for $1\leq j\leq J$, denote respectively the sides and vertices of $\Gamma$. Let us take $J$ functions:

<!-- PDF page 31 / printed page 17 -->

$$
h_j\in H^{3/2}(\Gamma_j),\qquad1\leq j\leq J,
$$

satisfying the matching conditions $h_j(S_{j+1})=h_{j+1}(S_{j+1})$ and $J$ functions

$$
g_j\in H^{1/2}(\Gamma_j),\qquad1\leq j\leq J,
$$

and consider the problem

$$
(B'')\quad\begin{cases}
\Delta^2u=f&\text{in }H^{-2}(\Omega), \tag{1.41}\\
u=h_j&\text{on }\Gamma_j, \tag{1.49}\\
\partial u/\partial n=g_j&\text{on }\Gamma_j, \tag{1.50}
\end{cases}\qquad1\leq j\leq J.
$$

By virtue of Remark 1.1, we know that there exists a function $u_0$ in $H^2(\Omega)$ such that

$$
u_0=h_j,\qquad\partial u_0/\partial n=g_j\quad\text{on }\Gamma_j,\qquad1\leq j\leq J,
$$

and

$$
\|u_0\|_{2,\Omega}\leq C_3\left\{\sum_{j=1}^J(\|h_j\|_{3/2,\Gamma_j}^2+\|g_j\|_{1/2,\Gamma_j}^2)\right\}^{1/2}.
$$

Hence the conclusion of Proposition 1.3 (with the functions $h_j$ and $g_j$ instead of $g_1$ and $g_2$) applies also to Problem $(B'')$ in this case.

When the boundary of $\Omega$ is sufficiently smooth, it is possible to derive more information about the regularity of $u$.

**Theorem 1.11.** *Let $\Omega$ be a bounded open subset of $\mathbb R^N$ with a boundary $\Gamma$ of class $\mathcal C^{k+3,1}$ for an integer $k\geq-2$ and assume that the data $f,g_1$ and $g_2$ of the biharmonic Problem (B) satisfy*

$$
f\in H^k(\Omega),\qquad g_1\in H^{k+7/2}(\Gamma),\qquad g_2\in H^{k+5/2}(\Gamma).
$$

*Then $u\in H^{k+4}(\Omega)$ and there exists a constant $C=C(k,\Omega)$ such that*

$$
\|u\|_{k+4,\Omega}\leq C\{\|f\|_{k,\Omega}+\|g_1\|_{k+7/2,\Gamma}+\|g_2\|_{k+5/2,\Gamma}\}. \tag{1.51}
$$

But even when $\Gamma$ has corners, the conclusion of Proposition 1.3 can be refined for the biharmonic problem with homogeneous boundary conditions.

**Theorem 1.12.** *Assume that $\Omega$ is a two-dimensional bounded polygon with no reentrant corner. Then the mapping $u\mapsto\Delta^2u$ is an isomorphism from $H^3(\Omega)\cap H_0^2(\Omega)$ onto $H^{-1}(\Omega)$.*

This last result is fundamental to establish the regularity of the solution of the Stokes problem in a plane, convex polygon (cf. Grisvard [43]).
