# §3.3 Levi-Civita Connection

Source: Leonor Godinho and José Natário, *An Introduction to Riemannian Geometry*. This record ends before §3.4. Display transcriptions are keyed to the book-local formula registry. Printed pages are distinguished from the PDF's one-based page indices.

## PDF 114 / printed 104

In the case of a Riemannian manifold, there is a particular choice of connection, called the **Levi-Civita connection**, with special geometric properties.

**Definition 3.1.** A connection \(\nabla\) in a Riemannian manifold \((M,\langle\cdot,\cdot\rangle)\) is said to be **compatible** with the metric if

[rg-p114-d01]

for all \(X,Y,Z\in\mathfrak X(M)\).

If \(\nabla\) is compatible with the metric, then the inner product of two vector fields \(V_1\) and \(V_2\), parallel along a curve, is constant along the curve:

[rg-p114-d02]

In particular, parallel transport preserves lengths of vectors and angles between vectors. Therefore, if \(c:I\to M\) is a geodesic, then \(\|\dot c(t)\|=k\) is constant. If \(a\in I\), the length \(s\) of the geodesic between \(a\) and \(t\) is

[rg-p114-d03]

In other words, \(t\) is an affine function of the arclength \(s\) (and is therefore called an **affine parameter**). In particular, this shows that the parameters of two geodesics with the same image are affine functions of each other).

**Theorem 3.2 (Levi–Civita).** If \((M,\langle\cdot,\cdot\rangle)\) is a Riemannian manifold then there exists a unique connection \(\nabla\) on \(M\) which is symmetric and compatible with \(\langle\cdot,\cdot\rangle\). In local coordinates \((x^1,\ldots,x^n)\), the Christoffel symbols for this connection are

[rg-p114-d04, original (3.5)]

where \((g^{ij})=(g_{ij})^{-1}\).

**Proof.** Let \(X,Y,Z\in\mathfrak X(M)\). If the Levi-Civita connection exists then we must have

[rg-p114-d05]

## PDF 115 / printed 105

as \(\nabla\) is compatible with the metric. Moreover, since \(\nabla\) is symmetric, we must also have

[rg-p115-d01]

Adding these six equalities, we obtain the **Koszul formula**

[rg-p115-d02]

Since \(\langle\cdot,\cdot\rangle\) is nondegenerate and \(Z\) is arbitrary, this formula determines \(\nabla_XY\). Thus, if the Levi-Civita connection exists, it must be unique.

To prove existence, we **define** \(\nabla_XY\) through the Koszul formula. It is not difficult to show that this indeed defines a connection [cf. Exercise 3.3(1)]. Also, using this formula, we obtain

[rg-p115-d03]

for all \(X,Y,Z\in\mathfrak X(M)\), and hence \(\nabla\) is symmetric. Finally, again using the Koszul formula, we have

[rg-p115-d04]

and therefore the connection defined by this formula is compatible with the metric.

Choosing local coordinates \((x^1,\ldots,x^n)\), we have

[rg-p115-d05]

Therefore the Koszul formula yields

[rg-p115-d06]

This linear system is easily solved to give (3.5). □

## PDF 116 / printed 106

**Exercise 3.3**

(1) Show that the Koszul formula defines a connection.

(2) We introduce in \(\mathbb R^3\), with the usual Euclidean metric \(\langle\cdot,\cdot\rangle\), the connection \(\nabla\) defined in Cartesian coordinates \((x^1,x^2,x^3)\) by

[rg-p116-d01]

where \(\omega:\mathbb R^3\to\mathbb R\) is a smooth function and

[rg-p116-d02; cases: even permutation, odd permutation, otherwise]

Show that:

- (a) \(\nabla\) is compatible with \(\langle\cdot,\cdot\rangle\);
- (b) the geodesics of \(\nabla\) are straight lines;
- (c) the torsion of \(\nabla\) is not zero in all points where \(\omega\ne0\) (therefore \(\nabla\) is not the Levi-Civita connection unless \(\omega\equiv0\));
- (d) the parallel transport equation is [rg-p116-d03] (where \(\times\) is the cross product in \(\mathbb R^3\)); therefore, a vector parallel along a straight line rotates about it with angular velocity \(-\omega\dot x\).

(3) Let \((M,g)\) and \((N,\widetilde g)\) be isometric Riemannian manifolds with Levi-Civita connections \(\nabla\) and \(\widetilde\nabla\), and let \(f:M\to N\) be an isometry. Show that:

- (a) \(f_*\nabla_XY=\widetilde\nabla_{f_*X}f_*Y\) for all \(X,Y\in\mathfrak X(M)\);
- (b) if \(c:I\to M\) is a geodesic then \(f\circ c:I\to N\) is also a geodesic.

(4) Consider the usual local coordinates \((\theta,\varphi)\) in \(S^2\subset\mathbb R^3\) defined by the parameterization \(\phi:(0,\pi)\times(0,2\pi)\to\mathbb R^3\) given by [rg-p116-d04].

- (a) Using these coordinates, determine the expression of the Riemannian metric induced on \(S^2\) by the Euclidean metric of \(\mathbb R^3\).
- (b) Compute the Christoffel symbols for the Levi-Civita connection in these coordinates.
- (c) Show that the equator is the image of a geodesic.
- (d) Show that any rotation about an axis through the origin in \(\mathbb R^3\) induces an isometry of \(S^2\).

## PDF 117 / printed 107

- (4e) Show that the images of geodesics of \(S^2\) are great circles.
- (4f) Find a **geodesic triangle** (i.e. a triangle whose sides are images of geodesics) whose internal angles add up to \(\frac{3\pi}{2}\).
- (4g) Let \(c:\mathbb R\to S^2\) be given by \(c(t)=(\sin\theta_0\cos t,\sin\theta_0\sin t,\cos\theta_0)\), where \(\theta_0\in(0,\frac{\pi}{2})\) (therefore \(c\) is not a geodesic). Let \(V\) be a vector field parallel along \(c\) such that \(V(0)=\frac{\partial}{\partial\theta}\) (\(\frac{\partial}{\partial\theta}\) is well defined at \((\sin\theta_0,0,\cos\theta_0)\) by continuity). Compute the angle by which \(V\) is rotated when it returns to the initial point. (**Remark:** The angle you have computed is exactly the angle by which the oscillation plane of the **Foucault pendulum** rotates during a day in a place at latitude \(\frac{\pi}{2}-\theta_0\), as it tries to remain fixed with respect to the stars on a rotating Earth).
- (4h) Use this result to prove that no open set \(U\subset S^2\) is isometric to an open set \(W\subset\mathbb R^2\) with the Euclidean metric.
- (4i) Given a geodesic \(c:\mathbb R\to\mathbb R^2\) of \(\mathbb R^2\) with the Euclidean metric and a point \(p\notin c(\mathbb R)\), there exists a unique geodesic \(\widetilde c:\mathbb R\to\mathbb R^2\) (up to reparameterization) such that \(p\in\widetilde c(\mathbb R)\) and \(c(\mathbb R)\cap\widetilde c(\mathbb R)=\emptyset\) (**parallel postulate**). Is this true in \(S^2\)?

(5) Recall that identifying each point in [rg-p117-d01] with the invertible affine map \(h:\mathbb R\to\mathbb R\) given by \(h(t)=yt+x\) induces a Lie group structure on \(H\) [cf. Exercise 7.17(3) in Chap. 1].

- (a) Show that the left-invariant metric induced by the Euclidean inner product \(dx\otimes dx+dy\otimes dy\) in \(\mathfrak h=T_{(0,1)}H\) is [rg-p117-d02] [cf. Exercise 1.10(4)]. (**Remark:** \(H\) endowed with this metric is called the **hyperbolic plane**).
- (b) Compute the Christoffel symbols of the Levi-Civita connection in the coordinates \((x,y)\).
- (c) Show that the curves \(\alpha,\beta:\mathbb R\to H\) given in these coordinates by [rg-p117-d03] are geodesics. What are the sets \(\alpha(\mathbb R)\) and \(\beta(\mathbb R)\)?
- (d) Determine all images of geodesics.
- (e) Show that, given two points \(p,q\in H\), there exists a unique geodesic through them (up to reparameterization).

## PDF 118 / printed 108

- (5f) Give examples of connected Riemannian manifolds containing two points through which there are (i) infinitely many geodesics (up to reparameterization); (ii) no geodesics.
- (5g) Show that no open set \(U\subset H\) is isometric to an open set \(V\subset\mathbb R^2\) with the Euclidean metric. (**Hint:** Show that in any neighborhood of any point \(p\in H\) there is always a geodesic quadrilateral whose internal angles add up to less than \(2\pi\)).
- (5h) Does the parallel postulate hold in the hyperbolic plane?

(6) Let \((M,\langle\cdot,\cdot\rangle)\) be a Riemannian manifold with Levi-Civita connection \(\widetilde\nabla\), and let \((N,\langle\langle\cdot,\cdot\rangle\rangle)\) be a submanifold with the induced metric and Levi-Civita connection \(\nabla\).

- (a) Show that [rg-p118-d01] for all \(X,Y\in\mathfrak X(N)\), where \(\widetilde X,\widetilde Y\) are any extensions of \(X,Y\) to \(\mathfrak X(M)\) and \({}^{\top}:TM|_N\to TN\) is the orthogonal projection.
- (b) Use this result to indicate curves that are, and curves that are not, geodesics of the following surfaces in \(\mathbb R^3\): (i) the sphere \(S^2\); (ii) the torus of revolution; (iii) the surface of a cone; (iv) a general surface of revolution.
- (c) Show that if two surfaces in \(\mathbb R^3\) are tangent along a curve, then the parallel transport of vectors along this curve in both surfaces coincides.
- (d) Use this result to compute the angle \(\Delta\theta\) by which a vector \(V\) is rotated when it is parallel transported along a circle on the sphere. (**Hint:** Consider the cone which is tangent to the sphere along the circle (cf. Fig. 3.1); notice that the cone minus a ray through the vertex is isometric to an open set of the Euclidean plane).

(7) Let \((M,g)\) be a Riemannian manifold with Levi-Civita connection \(\nabla\). Show that \(g\) is **parallel** along any curve, i.e. show that [rg-p118-d02] for all \(X\in\mathfrak X(M)\) [cf. Exercise 2.6(3)].

(8) Let \((M,g)\) be a Riemannian manifold with Levi-Civita connection \(\nabla\), and let \(\psi_t:M\to M\) be a 1-parameter group of isometries. The vector field \(X\in\mathfrak X(M)\) defined by [rg-p118-d03] is called the **Killing vector field** associated to \(\psi_t\). Show that:

- (a) \(L_Xg=0\) [cf. Exercise 2.8(3)];
- (b) \(X\) satisfies \(\langle\nabla_YX,Z\rangle+\langle\nabla_ZX,Y\rangle=0\) for all vector fields \(Y,Z\in\mathfrak X(M)\);

## PDF 119 / printed 109

**Fig. 3.1.** Parallel transport along a circle on the sphere. Source vector region: PDF points \((87,451,349,613)\) in bottom-left coordinates.

- (8c) if \(c:I\to M\) is a geodesic then \(\langle\dot c(t),X_{c(t)}\rangle\) is constant.

(9) Recall that if \(M\) is an oriented differential manifold with volume element \(\omega\in\Omega^n(M)\), the **divergence** of \(X\) is the function \(\operatorname{div}(X)\) such that [rg-p119-d01] [cf. Exercise 6.4(5) in Chap. 2]. Suppose that \(M\) has a Riemannian metric and that \(\omega\) is a Riemannian volume element. Show that at each point \(p\in M\), [rg-p119-d02] where \(\{Y_1,\ldots,Y_n\}\) is an orthonormal basis of \(T_pM\) and \(\nabla\) is the Levi-Civita connection.
