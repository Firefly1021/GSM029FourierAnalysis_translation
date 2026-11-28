# Beginning in Algebraic Geometry — recovered sample

Source: PDF pages 15–18, printed pages 2–5. Running headings are page metadata. Side notes are recorded after their anchored prose in reading order; source visual placement is retained in the Chinese layout.

## PDF 15 / printed 2 — Section 0.1 Polynomials

Polynomials and their solutions are some of the first objects we encounter in our mathematical lives. For example, you may even remember the first time you learned that the solutions in $\mathbb{R}^{2}$ of the two-variable polynomial equation
\[
  x^{2}+y^{2}-1=0
\]
describe the unit circle. However, if our goal is to study the unit circle, then there are many other polynomials that one might choose to describe it; for example, the unit circle is also equal to the solutions of either
\[
  2x^{2}+2y^{2}-2=0\quad\text{or}\quad(x^{2}+y^{2}-1)^{2}=0.
\]
This leads to a natural question: is there a best polynomial that describes the unit circle? The answer proposed by algebraic geometry is, in some sense, the most egalitarian: all of the polynomials that describe the unit circle are equally important, and we should study them together as a set. What does it mean, then, to study a set of polynomials?

The unnumbered, uncaptioned unit-circle diagram is at the right of this opening paragraph, source PDF crop in top-left coordinates [267, 67, 372, 174] bp.

As we will soon learn, the set of polynomials describing the unit circle is much more than just a set; it has important algebraic structure that reflects the geometry of the circle. To be able to describe this algebraic structure in this example and beyond, we must first establish precise notation and terminology regarding sets of polynomials and their algebraic structure. To begin our formal discussion of polynomials, we start with the notion of a monomial.

### Definition 0.1 — Monomials

A monomial in the variables $x_{1},\ldots,x_{n}$ is an expression of the form
\[
  x^{\alpha}=x_{1}^{\alpha_{1}}\cdots x_{n}^{\alpha_{n}},
\]
where $\alpha=(\alpha_{1},\ldots,\alpha_{n})\in\mathbb{N}^{n}$ is the exponent vector. Two monomials are equal if and only if they have the same exponent vector.

### Body

The variables $x_{1},\ldots,x_{n}$ should be viewed as formal symbols, and their role is simply to serve as placeholders for $\alpha_{1},\ldots,\alpha_{n}$. The data of a monomial in $x_{1},\ldots,x_{n}$ is equivalent to the data of an exponent vector $(\alpha_{1},\ldots,\alpha_{n})$; however, placing each $\alpha_{i}$ as the exponent of $x_{i}$ will prove useful when multiplication of monomials is defined below. Variables that appear with an exponent of $0$ are typically omitted; for example,
\[
  x^{2}y^{3}z^{0}=x^{2}y^{3}\quad\text{and}\quad x^{0}y^{0}z^{0}=1.
\]

> Side note, anchored to “The variables”: When there are only a few variables, they are often represented with distinct letters such as $x$, $y$, and $z$.

As in the case of $f(x,y)=x^{2}+y^{2}-1$, polynomials are built by taking linear combinations of monomials. In the most general setting, the coefficients of these linear combinations belong to an arbitrary ring $R$, as in the following definition.

## PDF 16 / printed 3

### Definition 0.2 — Polynomials over $R$

A polynomial in the variables $x_{1},\ldots,x_{n}$ over $R$ is an expression of the form
\[
  f=f(x_{1},\ldots,x_{n})=\sum_{\alpha\in\mathbb{N}^{n}}a_{\alpha}x^{\alpha},
\]
where $a_{\alpha}\in R$ for each $\alpha\in\mathbb{N}^{n}$ and $a_{\alpha}=0$ for all but finitely many $\alpha$. Two polynomials
\[
  f=\sum_{\alpha}a_{\alpha}x^{\alpha}\quad\text{and}\quad g=\sum_{\alpha}b_{\alpha}x^{\alpha}
\]
are equal if and only if $a_{\alpha}=b_{\alpha}$ for all $\alpha\in\mathbb{N}^{n}$.

### Example 0.3 — Polynomials

The following are two examples of polynomials in the variables $x$ and $y$ over the ring of integers $\mathbb{Z}$:

> Side note, anchored to the example introduction: Polynomials are typically written as finite sums, omitting all summands that have a coefficient of zero.

\[
  f=xy^{2}+3xy+2\quad\text{and}\quad g=-xy+4.
\]
The polynomials $f$ and $g$ can also be viewed as having coefficients in $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ or any other ring containing $\mathbb{Z}$. Observe that we can create new polynomials from $f$ and $g$ by adding them and multiplying them in the familiar way:
\[
  \begin{gathered}
    f+g=xy^{2}+2xy+6,\\
    fg=-x^{2}y^{3}-3x^{2}y^{2}+4xy^{2}+10xy+8.
  \end{gathered}
\]

### Body

As the reader is encouraged to verify in Exercise 0.1.1, the operations of addition and multiplication, formalized in the next definition, endow the set of polynomials with the structure of a ring.

### Definition 0.4 — Polynomial rings

The polynomial ring $R[x_{1},\ldots,x_{n}]$ is the set of all polynomials in variables $x_{1},\ldots,x_{n}$ over $R$. Polynomial addition and multiplication are defined by
\[
  \left(\sum_{\alpha}a_{\alpha}x^{\alpha}\right)
  +\left(\sum_{\alpha}b_{\alpha}x^{\alpha}\right)
  =\sum_{\alpha}(a_{\alpha}+b_{\alpha})x^{\alpha}
\]
and
\[
  \left(\sum_{\alpha}a_{\alpha}x^{\alpha}\right)
  \left(\sum_{\alpha}b_{\alpha}x^{\alpha}\right)
  =\sum_{\alpha}\left(\sum_{\alpha_{1}+\alpha_{2}=\alpha}
  a_{\alpha_{1}}b_{\alpha_{2}}\right)x^{\alpha}.
\]

### Body

The additive identity $0\in R[x_{1},\ldots,x_{n}]$ is the polynomial for which $a_{\alpha}=0$ for all $\alpha$, and the multiplicative identity $1\in R[x_{1},\ldots,x_{n}]$ is the polynomial for which
\[
  a_{\alpha}=
  \begin{cases}
    1 & \text{if }(\alpha_{1},\ldots,\alpha_{n})=(0,\ldots,0),\\
    0 & \text{if }(\alpha_{1},\ldots,\alpha_{n})\ne(0,\ldots,0).
  \end{cases}
\]

## PDF 17 / printed 4

When working with polynomial rings, it can be useful to leverage their recursive nature in order to utilize proofs by induction on the number of variables. The next result is somewhat self-evident, but we state it carefully as it will be used often.

### Proposition 0.5 — Recursive nature of polynomial rings

There is a canonical isomorphism of rings
\[
  R[x_{1},\ldots,x_{n}]=R[x_{1},\ldots,x_{n-1}][x_{n}],
\]
where the right-hand side is the ring of polynomials in one variable $x_{n}$ with coefficients in the ring $R[x_{1},\ldots,x_{n-1}]$.

### Body

The next example illustrates the main idea behind Proposition 0.5.

### Example 0.6 — $\mathbb{Z}[x,y]$ versus $\mathbb{Z}[x][y]$

Consider the polynomial
\[
  f=x^{3}y^{2}+xy^{2}-2xy-x+1\in\mathbb{Z}[x,y].
\]
We can view $f$ as an element of $\mathbb{Z}[x][y]$ by grouping all terms that have the same exponent in $y$. In doing so, we write
\[
  f=(x^{3}+x)y^{2}+(-2x)y+(-x+1)\in\mathbb{Z}[x][y].
\]
As a polynomial in $y$, the coefficients of $f$ are $x^{3}+x$, $-2x$, and $-x+1$, all of which are elements of $\mathbb{Z}[x]$.

### Proof of Proposition 0.5

To prove the proposition, we describe the canonical ring isomorphism, which, as illustrated in Example 0.6, simply groups all terms of a polynomial in $R[x_{1},\ldots,x_{n}]$ for which $x_{n}$ appears with the same exponent. To make this more precise, consider the following function:

> Side note, anchored to the proof opening: When two rings are isomorphic, there will often be a multitude of possible isomorphisms. The word “canonical” means that there is one natural choice among all possible isomorphisms. The symbol $\cong$ is used to denote isomorphisms, while $=$ is used for canonical isomorphisms.

\[
  \begin{aligned}
    \phi:R[x_{1},\ldots,x_{n}]&\to R[x_{1},\ldots,x_{n-1}][x_{n}]\\
    \sum_{\alpha\in\mathbb{N}^{n}}a_{\alpha}x_{1}^{\alpha_{1}}\cdots x_{n}^{\alpha_{n}}
    &\mapsto
    \sum_{d\ge0}\left(\sum_{\substack{\alpha\in\mathbb{N}^{n}\\\alpha_{n}=d}}
      a_{\alpha}x_{1}^{\alpha_{1}}\cdots x_{n-1}^{\alpha_{n-1}}\right)x_{n}^{d}.
  \end{aligned}
\]
The verification that $\phi$ is a ring isomorphism is Exercise 0.1.3. [End of proof.]

### Body

The following result concerning polynomial rings over integral domains is a first application of Proposition 0.5.

## PDF 18 / printed 5

### Proposition 0.7 — Polynomials over integral domains

If $R$ is an integral domain, then $R[x_{1},\ldots,x_{n}]$ is an integral domain.

### Proof

We proceed by induction on the number of variables.

(Base case) Let $f,g\in R[x_{1}]$ be nonzero. We must prove that $fg\ne0$. Write
\[
  f=a_{d}x_{1}^{d}+a_{d-1}x_{1}^{d-1}+\cdots+a_{0}
  \quad\text{and}\quad
  g=b_{e}x_{1}^{e}+b_{e-1}x_{1}^{e-1}+\cdots+b_{0},
\]
where $a_{d}\ne0$ and $b_{e}\ne0$. By definition of multiplication in $R[x_{1}]$,
\[
  fg=(a_{d}b_{e})x_{1}^{d+e}
  +(a_{d}b_{e-1}+a_{d-1}b_{e})x_{1}^{d+e-1}+\cdots+a_{0}b_{0}.
\]
Since $R$ is an integral domain, $a_{d}b_{e}\ne0$. Since $fg$ has at least one nonzero coefficient, we conclude that $fg\ne0$.

(Induction step) Assume $S=R[x_{1},\ldots,x_{n-1}]$ is an integral domain; we must show that $R[x_{1},\ldots,x_{n}]$ is an integral domain. By Proposition 0.5,
\[
  R[x_{1},\ldots,x_{n}]=S[x_{n}].
\]
Since $S$ is an integral domain, the argument used in the base case immediately implies that $S[x_{n}]$, and thus $R[x_{1},\ldots,x_{n}]$, is an integral domain. [End of proof.]

### Body

The numbers $d$ and $e$ appearing in the proof of Proposition 0.7 are important attributes of the polynomials $f$ and $g$, called their degrees. The next definition generalizes the notion of degree to polynomials with any number of variables.

### Definition 0.8 — Monomial and polynomial degree

The degree of a monomial $x^{\alpha}=x_{1}^{\alpha_{1}}\cdots x_{n}^{\alpha_{n}}$ is
\[
  \deg(x^{\alpha})=\alpha_{1}+\cdots+\alpha_{n}\in\mathbb{N}.
\]
The degree of a nonzero polynomial $f=\sum a_{\alpha}x^{\alpha}\in R[x_{1},\ldots,x_{n}]$ is
\[
  \deg(f)=\max\{\deg(x^{\alpha})\mid a_{\alpha}\ne0\}.
\]

### Example 0.9 — Degree

The monomials $x^{2}yz$, $z^{4}$, $x$, and $1$ have degrees $4$, $4$, $1$, and $0$, respectively, and
\[
  \deg(x^{2}yz+z^{4}+x+1)=4.
\]

### Body

The reader may have noticed that the zero polynomial has not been assigned a degree, which is intentional. One of the most useful properties of degree is additivity, described in the next result, which fails for any choice of $\deg(0)\in\mathbb{N}$.
