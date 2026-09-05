# Restored-source review candidate: chapter-02-section-03



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 166 / printed 152



[p0166-b0003 | ordinary-paragraph | high] Stokes Problem satisfy:

[p0166-b0004 | ordinary-paragraph | high] ue (H**(Q)N HQ), pe H*(Q) 1 L3(Q)

[p0166-b0005 | ordinary-paragraph | high] for some integer ké [1,1]. Then the solution (u,, p,) of (1.39) with the spaces X,, and

[p0166-b0006 | ordinary-paragraph | high] M, defined by (2.47) (2.48) satisfies the error bound:

[p0166-b0007 | ordinary-paragraph | high] (2.51) Ju —uyli.o + IP — Palloe < Crh“(ule+s,0 + |Plk.a)-

[p0166-b0008 | ordinary-paragraph | high] In addition, if the Stokes Problem (1.48) is regular, we have the L*-estimate

[p0166-b0009 | ordinary-paragraph | high] (2.52) Ju — uyllo,g < C,A** (luless,a + |Plk.):

[p0166-b0010 | remark | high] Remark 2.8. It is easy to show that the statement of Remark 2.6 concerning the

[p0166-b0011 | ordinary-paragraph | high] convergence under weak regularity assumptions on (u,p) is still valid in the

[p0166-b0012 | ordinary-paragraph | high] three-dimensional case.

[p0166-b0013 | section | high] § 3. Quadrilateral Finite Element Methods Using Discontinuous

[p0166-b0014 | ordinary-paragraph | high] Pressures

[p0166-b0015 | ordinary-paragraph | high] There are two reasons for treating separately quadrilateral finite elements. On

[p0166-b0016 | ordinary-paragraph | high] the one hand, isoparametric finite element methods are less transparent than

[p0166-b0017 | ordinary-paragraph | high] simplicial ones and must be handled with some more care. On the other hand,

[p0166-b0018 | ordinary-paragraph | high] quadrilateral elements (more precisely, rectangular elements) provide excellent

[p0166-b0019 | ordinary-paragraph | high] examples of schemes which do not satisfy the inf-sup condition and yet can

[p0166-b0020 | ordinary-paragraph | high] be proved to converge with optimal accuracy. Some of these schemes, being

[p0166-b0021 | ordinary-paragraph | high] particularly simple, are preferred by a number of users.

[p0166-b0022 | ordinary-paragraph | high] For the sake of conciseness, we have only treated the two-dimensional case.

[p0166-b0023 | ordinary-paragraph | high] The three-dimensional case is a straightforward adaptation of this material and

[p0166-b0024 | ordinary-paragraph | high] that of Section 2.3.

[p0166-b0025 | subsection | high] 3.1. A Quadrilateral Finite Element of Order One

[p0166-b0026 | ordinary-paragraph | high] The element discussed in this section is the analogue of the first-order element

[p0166-b0027 | ordinary-paragraph | high] defined in Section 2.1. It has been introduced by Fortin [30].

[p0166-b0028 | ordinary-paragraph | high] Let Q be a bounded, plane polygon and let 7, be a “triangulation” of Qm ade

[p0166-b0029 | ordinary-paragraph | high] of convex quadrilaterals with diameters bounded by h. Consider one of these

[p0166-b0030 | ordinary-paragraph | high] quadrilaterals « with vertices a,, a3, a3, a4 (also numbered ay); we denote by f;

[p0166-b0031 | ordinary-paragraph | high] the segment [a;_,4,; ] ( cf. Figure 10) and by n, its unit outward normal. To draw

[p0166-b0032 | ordinary-paragraph | high] the parallel with Section 2.1 we replace the barycentric coordinates by the

[p0166-b0033 | ordinary-paragraph | high] reference variables

[p0166-b0034 | equation | low] Ki, %2,%3 =1—X, and Sa 1h

## PDF 167 / printed 153



[p0167-b0003 | ordinary-paragraph | low] n4

[p0167-b0004 | ordinary-paragraph | low] Q

[p0167-b0005 | equation | low] (=ao)

[p0167-b0006 | ordinary-paragraph | medium] n1

[p0167-b0007 | ordinary-paragraph | medium] f3

[p0167-b0008 | ordinary-paragraph | medium] n3

[p0167-b0009 | ordinary-paragraph | low] a

[p0167-b0010 | ordinary-paragraph | low] n2

[p0167-b0011 | ordinary-paragraph | low] a2

[p0167-b0012 | figure | medium] Figure 10

[p0167-b0013 | ordinary-paragraph | medium] Now, we are looking for a velocity vector w that is compatible with a constant

[p0167-b0014 | ordinary-paragraph | medium] pressure in k. Keeping in mind the material of Section 2.1 it is likely that w will

[p0167-b0015 | ordinary-paragraph | medium] belong to a space larger than Q(k), but that its tangential components on each

[p0167-b0016 | ordinary-paragraph | medium] side of k will be affine. (The pair (Qi(k), Po) will in fact be the object of Section

[p0167-b0017 | ordinary-paragraph | medium] 3.3). As an example, the polynomial

[p0167-b0018 | equation | low] q1=xxx4

[p0167-b0019 | ordinary-paragraph | medium] vanishes on the sides f2,f, and f4 of the reference square k. Therefore the function

[p0167-b0020 | equation | low] P1 = n1(q o F-1)

[p0167-b0021 | ordinary-paragraph | medium] has zero tangential components on the sides of k. Generalizing this remark, we set

[p0167-b0022 | equation | low] a2=xx4x1，43=x4xx2，q4=xxx3

[p0167-b0023 | equation | low] (3.1)

[p0167-b0024 | equation | low] P; = n(a;o F-1)

[p0167-b0025 | ordinary-paragraph | medium] and we take the velocities w in the space (of dimension 12):

[p0167-b0026 | equation | low] 2,(k) = Q1(k)² ① span {P1, P2, P3, P4} c Q2(k)2.

[p0167-b0027 | equation | low] (3.2)

[p0167-b0028 | ordinary-paragraph | medium] As will be seen in the next lemma, the degrees of freedom naturally attached to

[p0167-b0029 | ordinary-paragraph | medium] this space are the values of w at the vertices a; and the flux of w through each

[p0167-b0030 | ordinary-paragraph | medium] side f of k.

[p0167-b0031 | lemma | medium] Lemma 3.1. A polynomial p of 2,(k) is uniquely determined by the 12 quantities:

[p0167-b0032 | equation | low] 1≤i≤4,

[p0167-b0033 | ordinary-paragraph | medium] p(a;)

[p0167-b0034 | equation | low] (3.3)

[p0167-b0035 | ordinary-paragraph | medium] p·n;ds

[p0167-b0036 | equation | low] 1≤i≤ 4.

[p0167-b0037 | ordinary-paragraph | medium] Furthermore the restriction of p to any side f; of k depends only upon the degrees

## PDF 168 / printed 154



[p0168-b0003 | ordinary-paragraph | high] 4

[p0168-b0004 | ordinary-paragraph | high] (3.4) p = Ip ae » a; Pj, aE R,

[p0168-b0005 | equation | low] = I

[p0168-b0006 | ordinary-paragraph | high] where J, denotes the standard interpolation operator on Q,(«)*. Furthermore,

[p0168-b0007 | ordinary-paragraph | high] (3.5) (p — [,p)njl5 ,= a;(4,0 F.*)Iy,-

[p0168-b0008 | ordinary-paragraph | high] From these two expressions we can easily derive that zero moments yield only

[p0168-b0009 | ordinary-paragraph | high] the zero polynomial. fia

[p0168-b0010 | ordinary-paragraph | high] Thus, we choose the following velocity and pressure spaces:

[p0168-b0011 | ordinary-paragraph | high] w|.€2;(x) Vee F;},

[p0168-b0012 | equation | low] te= {we $(Q);

[p0168-b0013 | equation | low] (3.6)

[p0168-b0014 | equation | low] X, = Wi, H(Q)’,

[p0168-b0015 | ordinary-paragraph | high] J,},

[p0168-b0016 | equation | low] ‘ = ches: q.€Pyo Wee

[p0168-b0017 | equation | low] (3.7)

[p0168-b0018 | equation | low] My, = Qn LG(Q).

[p0168-b0019 | lemma | high] Lemma 3.1 suggests the interpolation operator r, on 2,(x«) defined by:

[p0168-b0020 | equation | low] r,,V(a;) = v(a;), | (,,v—v)nds=0, 1l<i<j<4.

[p0168-b0021 | ordinary-paragraph | high] ihe

[p0168-b0022 | ordinary-paragraph | high] But once again, this operator does not satisfy Hypothesis H3 because it is not

[p0168-b0023 | ordinary-paragraph | high] defined on H'(Q)*. Therefore, like in the simplicial case we replace the above

[p0168-b0024 | ordinary-paragraph | high] values of v by those of the local regularization operator R,. similar to that of

[p0168-b0025 | ordinary-paragraph | high] Section A.3:

[p0168-b0026 | ordinary-paragraph | high] R,€ L(Ho(Q); ®,)

[p0168-b0027 | ordinary-paragraph | high] with

[p0168-b0028 | equation | low] D, = ($6 OQ); o|,€ Qik) Vee F,} HG (Q).

[p0168-b0029 | ordinary-paragraph | high] Then we define the operator 7, ¢ Y(H}(Q)*; X,) by:

[p0168-b0030 | equation | low] ™,V(a) = R,v(a) Wnodea of J,

[p0168-b0031 | equation | low] (3.8)

[p0168-b0032 | equation | low] |( z,V —v)'nds=0 Ysifd ofe J ,.

[p0168-b0033 | ordinary-paragraph | high] ij

[p0168-b0034 | ordinary-paragraph | high] In order to establish the approximating properties of z, we must assume that

[p0168-b0035 | ordinary-paragraph | high] the triangulation 7, is regular in the sense of Definition A.2 with the parameters:

[p0168-b0036 | ordinary-paragraph | high] h, = diameter of x, p, = 2 Min {diameter of circle inscribed in S;}

[p0168-b0037 | equation | low] 1<i<4

[p0168-b0038 | ordinary-paragraph | high] where S; denotes the triangle with vertices a;_,, a;, a;4,.

[p0168-b0039 | lemma | high] Lemma 3.2. The operator n, defined by (3.8) satisfies:

[p0168-b0040 | equation | low] \d iv(v—1,v)qgdx =0 VYqeQ,.

[p0168-b0041 | ordinary-paragraph | high] Q

## PDF 169 / printed 155



[p0169-b0003 | ordinary-paragraph | medium] Furthermore if the triangulation Jh, is regular, π, has the error bound:

[p0169-b0004 | equation | low] Iv-nnV/m, ≤ Chk-m1vlk.

[p0169-b0005 | equation | low] (3.9)

[p0169-b0006 | ordinary-paragraph | low] ()HAA

[p0169-b0007 | ordinary-paragraph | medium] with m = 0 or 1 and k = 1 or 2.

[p0169-b0008 | proof | medium] Proof. From (3.4) and (3.5) we derive:

[p0169-b0009 | ordinary-paragraph | medium] 4

[p0169-b0010 | equation | low] ThV = Rhv +

[p0169-b0011 | ordinary-paragraph | medium] αPi

[p0169-b0012 | equation | low] =

[p0169-b0013 | ordinary-paragraph | medium] where

[p0169-b0014 | ordinary-paragraph | medium] (v- Rkv)·n;ds

[p0169-b0015 | ordinary-paragraph | medium] q;o F-1 ds.

[p0169-b0016 | ordinary-paragraph | low] a：

[p0169-b0017 | ordinary-paragraph | low] fi

[p0169-b0018 | ordinary-paragraph | low] JSi

[p0169-b0019 | ordinary-paragraph | medium] On the one hand, the operator R, has the local interpolation error for ve H*(Q)2:

[p0169-b0020 | equation | low]  k = 1 or 2

[p0169-b0021 | equation | low] llv-Rnvllo,x+h1v-Rhv1,x≤ Chkvk,x

[p0169-b0022 | equation | low] (3.10)

[p0169-b0023 | ordinary-paragraph | medium] where again A, denotes the union of quadrilaterals which share at least a vertex

[p0169-b0024 | ordinary-paragraph | medium] with K.

[p0169-b0025 | ordinary-paragraph | medium] On the other hand, Lemma A.9 implies:

[p0169-b0026 | equation | low] IPinm,x≤C2a2mh-mlailm,≤C302m

[p0169-b0027 | ordinary-paragraph | medium] 2m1,1-m

[p0169-b0028 | equation | low] m = 0 or 1.

[p0169-b0029 | ordinary-paragraph | medium] Besides that

[p0169-b0030 | ordinary-paragraph | medium] 9;ds

[p0169-b0031 | equation | low] q;o F-1 ds = meas(f)

[p0169-b0032 | ordinary-paragraph | medium] Jfi

[p0169-b0033 | ordinary-paragraph | medium] and

[p0169-b0034 | ordinary-paragraph | low] II -- R,vIl ds

[p0169-b0035 | equation | low] (v - R,v)·n; ds  ≤ meas(fi)

[p0169-b0036 | ordinary-paragraph | low] Jsi

[p0169-b0037 | ordinary-paragraph | low] Jsi

[p0169-b0038 | ordinary-paragraph | medium] because the restriction of F, to the sides of k is affine. Then using the trace

[p0169-b0039 | theorem | medium] Theorem 1.1.5 and Lemma A.9 we obtain:

[p0169-b0040 | equation | low] I-— Rnv1 ds ≤(C4/px){11v- Rnv1,x +h²1v - Rnvl,x}1/2

[p0169-b0041 | ordinary-paragraph | medium] Therefore (3.10) yields:

[p0169-b0042 | equation | low] (v - Rnv)·n;ds  ≤ Csoxmeas(fi)hk-11vlk,4k

[p0169-b0043 | ordinary-paragraph | medium] Jfi

[p0169-b0044 | ordinary-paragraph | medium] Hence

[p0169-b0045 | equation | low] [a:1 ≤ C60xhk-11vlk,4x

[p0169-b0046 | ordinary-paragraph | medium] and

## PDF 170 / printed 156



[p0170-b0004 | ordinary-paragraph | medium] have established that our scheme is of order one:

[p0170-b0005 | theorem | medium] Theorem 3.1. Let Q be a bounded polygon and assume that the solution (u, p) of

[p0170-b0006 | ordinary-paragraph | medium] the Stokes equations satisfies:

[p0170-b0007 | ordinary-paragraph | medium] ()TU(o)Hd [()iHU()H]n

[p0170-b0008 | ordinary-paragraph | medium] Then if the triangulation J, is regular, the solution (un, Pn) of (1.39) with the spaces

[p0170-b0009 | ordinary-paragraph | medium] X, and M, defined by (3.6) (3.7) satisfies the conclusion of Theorem 2.1.

[p0170-b0010 | subsection | medium] 3.2. Higher-Order Quadrilateral Elements

[p0170-b0011 | ordinary-paragraph | medium] We propose to discuss and generalize the widely used “Q2-P," finite element

[p0170-b0012 | ordinary-paragraph | medium] scheme. In short, this method uses continuous velocities with components that

[p0170-b0013 | ordinary-paragraph | medium] are piecewise Q2(k) and discontinuous pressures that are piecewise P, on each

[p0170-b0014 | ordinary-paragraph | medium] element k. Its analysis is pretty straightforward and easily extended to arbitrary

[p0170-b0015 | ordinary-paragraph | medium] order I, so we can start directly with the general case.

[p0170-b0016 | ordinary-paragraph | medium] Again, let k be any quadrilateral of J, and let us choose:

[p0170-b0017 | equation | low] [Wh = {w∈Go()²; wlk∈Q(K)2 VK∈gh},

[p0170-b0018 | equation | low] (3.11)

[p0170-b0019 | equation | low] Xh = W, n H(Ω),

[p0170-b0020 | equation | low] Qh ={q∈L²(Q) qlx∈Pi-1 VKegh},

[p0170-b0021 | equation | low] (3.12)

[p0170-b0022 | equation | low] Mh = Qn N L2(Ω),

[p0170-b0023 | ordinary-paragraph | medium] with I ≥ 2.

[p0170-b0024 | ordinary-paragraph | medium] Right away, observe that X, c X, so that the inf-sup condition need only be

[p0170-b0025 | ordinary-paragraph | medium] checked locally. As a consequence, we can take the simplest degrees of freedom

[p0170-b0026 | ordinary-paragraph | medium] available such as:

[p0170-b0027 | ordinary-paragraph | medium] the values of each component of w on the principal lattice Z, of order l;

[p0170-b0028 | ordinary-paragraph | medium] the moments corresponding to Pi-, for q:

[p0170-b0029 | ordinary-paragraph | medium] qf dx

[p0170-b0030 | ordinary-paragraph | medium] Vf e Pi-1.

[p0170-b0031 | ordinary-paragraph | medium] K

[p0170-b0032 | ordinary-paragraph | medium] To begin with, let us establish the local inf-sup condition. Here again, we take

[p0170-b0033 | ordinary-paragraph | medium] the triangulation as our partition:

[p0170-b0034 | equation | low] Xh(k) = {v∈Qi(k)²;vlox = 0},

[p0170-b0035 | equation | low] (3.13)

[p0170-b0036 | equation | low] Mh(k) =P- NL2(K).

[p0170-b0037 | theorem | medium] Theorem 3.2. Let the triangulation J, be regular. Then the pair of spaces (X,(k),

[p0170-b0038 | ordinary-paragraph | medium] M,(r) defined by (3.13) satisfies Hypothesis H4.

## PDF 171 / printed 157



[p0171-b0003 | proof | medium] Proof. The proof is much like that of Theorem 2.2 so we shall only dwell on the

[p0171-b0004 | ordinary-paragraph | medium] details inherent to quadrilaterals. We have:

[p0171-b0005 | equation | low] qdiv v dx =

[p0171-b0006 | equation | low] v· grad q dx

[p0171-b0007 | equation | low] JFv  [(grad g)o F] dx.

[p0171-b0008 | ordinary-paragraph | medium] Since qe Pi-1, we have grad qe P²-2 and therefore

[p0171-b0009 | equation | low] (grad q)o F ∈ Qi-2

[p0171-b0010 | ordinary-paragraph | medium]  on k.

[p0171-b0011 | ordinary-paragraph | medium] Let

[p0171-b0012 | ordinary-paragraph | low] b(x)xxxx4

[p0171-b0013 | ordinary-paragraph | medium] denote the “bubble" function on k and let us choose

[p0171-b0014 | equation | low]  = - b(x)[(grad q) o F<].

[p0171-b0015 | ordinary-paragraph | medium] Then ve X,(k) and with this choice

[p0171-b0016 | equation | low] qdiv v dx =

[p0171-b0017 | equation | low] Jrb(x) Il(grad q) o F ll² dx.

[p0171-b0018 | ordinary-paragraph | medium] Of course the mapping

[p0171-b0019 | ordinary-paragraph | medium] b(x)/p|dx

[p0171-b0020 | ordinary-paragraph | low] k

[p0171-b0021 | ordinary-paragraph | medium] is a norm on any finite-dimensional space; thus

[p0171-b0022 | equation | low] JF ll(grad q) o F ll² dx

[p0171-b0023 | equation | low] qdivvdx ≥ C

[p0171-b0024 | ordinary-paragraph | low] JK

[p0171-b0025 | ordinary-paragraph | medium] K

[p0171-b0026 | equation | low] ≥ C1qli.x.

[p0171-b0027 | ordinary-paragraph | medium] Besides that

[p0171-b0028 | equation | low] II vllo.x ≤ lal1,k

[p0171-b0029 | ordinary-paragraph | medium] and

[p0171-b0030 | equation | low] [vl1.x ≤ C2(o2 /px) Ilvllo,x

[p0171-b0031 | ordinary-paragraph | medium] by applying to quadrilaterals the easy argument of Lemma A.6. Hence

[p0171-b0032 | equation | low] qdiv vdx ≥ C3(pr/o)lql1,x

## PDF 172 / printed 158



[p0172-b0003 | ordinary-paragraph | high] independent of h and x, such that

[p0172-b0004 | ordinary-paragraph | high] (3.14) Who < COM die Ve H*(K)N Lo(x).

[p0172-b0005 | ordinary-paragraph | high] We skip the proof because it is entirely similar to that of Lemma 2.5.

[p0172-b0006 | ordinary-paragraph | high] It remains to examine the approximation properties of W, and Q,. While the

[p0172-b0007 | ordinary-paragraph | high] approximation error in W, is completely standard since it stems directly from

[p0172-b0008 | ordinary-paragraph | high] (A.49):

[p0172-b0009 | equation | low] |W —1,WIna < Ch" |Whare Wwe (Q), 1<k<l

[p0172-b0010 | equation | low] (3.15)

[p0172-b0011 | equation | low] i) = OOF iL.

[p0172-b0012 | ordinary-paragraph | high] the approximation error in Q, is not so immediate because we are dealing

[p0172-b0013 | ordinary-paragraph | high] with polynomials of P,_, on quadrilaterals (instead of triangles). In particular,

[p0172-b0014 | theorem | high] Theorem A.3 cannot be applied because {po F,;peP,_,} is a proper subspace

[p0172-b0015 | ordinary-paragraph | high] of Q,_,. The following lemma is due to Bernardi (private communication).

[p0172-b0016 | lemma | high] Lemma 3.4. If the triangulation 7, is regular, the operator p, of orthogonal

[p0172-b0017 | ordinary-paragraph | high] L?-projection on Q,, satisfies the bound:

[p0172-b0018 | ordinary-paragraph | high] (3.16) If — Prfllooa<Ch*lfl.g WeH(Q) ford<k<l.

[p0172-b0019 | proof | high] Proof. Let « be a quadrilateral of %,. Notice that (3.16) would be trivial if the

[p0172-b0020 | ordinary-paragraph | high] mapping F,, were affine instead of bilinear. So we propose to introduce another

[p0172-b0021 | ordinary-paragraph | high] a3

[p0172-b0022 | ordinary-paragraph | high] a

[p0172-b0023 | ordinary-paragraph | high] (0,0) (1,0)

[p0172-b0024 | ordinary-paragraph | high] a 1 a,

[p0172-b0025 | figure | high] Figure 11

## PDF 173 / printed 159



[p0173-b0003 | ordinary-paragraph | medium] "reference" set k—not necessarily the unit square—that is related to k by an

[p0173-b0004 | ordinary-paragraph | medium] affine mapping F. More precisely, let us split k into the two subtriangles (cf.

[p0173-b0005 | figure | medium] Figure 11):

[p0173-b0006 | equation | low] K = S, USs,

[p0173-b0007 | ordinary-paragraph | medium] let S, be the reference unit triangle, F the affine mapping such that

[p0173-b0008 | equation | low] S = F(S),

[p0173-b0009 | equation | low] F(x) = Bx + b

[p0173-b0010 | ordinary-paragraph | medium] and set

[p0173-b0011 | equation | low] S3 = F-1(Ss).

[p0173-b0012 | ordinary-paragraph | medium] In other words,

[p0173-b0013 | equation | low] = Suss,

[p0173-b0014 | equation | low] K = F().

[p0173-b0015 | ordinary-paragraph | medium] As F is affine and k is convex, the reference set k is also a convex quadrilateral.

[p0173-b0016 | ordinary-paragraph | medium] In addition, we readily derive that on the one hand

[p0173-b0017 | equation | low] 1≤i≤4

[p0173-b0018 | equation | low] )s/)s]() = ()s)

[p0173-b0019 | ordinary-paragraph | medium] where S; (resp. S;) denotes any of the four subtriangles of k (resp. k). On the other

[p0173-b0020 | ordinary-paragraph | medium] hand any two vertices of k satisfy:

[p0173-b0021 | equation | low] a-a; = B-(a;-aj)

[p0173-b0022 | ordinary-paragraph | medium] Furthermore formulas (A.2) and (A.3) give here

[p0173-b0023 | equation | low] IIBIll ≤ (3/2)hs,, IB-1 1l ≤ 2/ps,  |det(B)I = 2 meas(S).

[p0173-b0024 | ordinary-paragraph | medium] Now, let fe H*(k) with O ≤ k ≤ l. The L²-projection p, on Pi-1 is invariant

[p0173-b0025 | ordinary-paragraph | medium] under affine transformations. Thus

[p0173-b0026 | equation | low] I1 f - pnf /lo,x = |det(B)1/ I1 f -- pf llo,k-

[p0173-b0027 | ordinary-paragraph | medium] But

[p0173-b0028 | equation | low] 1 f - pfllo,x ≤ inf If + allo,x =1IIfllL2(c)P; 

[p0173-b0029 | equation | low] 'I-1>!>0

[p0173-b0030 | ordinary-paragraph | low] qEPj

[p0173-b0031 | ordinary-paragraph | medium] Since k is a variable quadrilateral, we must explicit the constant C(k) such that

[p0173-b0032 | equation | low] IIfllL2(t)p, ≤ C(k)Ifli+1,R.

[p0173-b0033 | ordinary-paragraph | medium] This is done by induction on the degree j. When j = O, which is the only case

[p0173-b0034 | ordinary-paragraph | medium] where we can use Theorem A.3, we get

[p0173-b0035 | ordinary-paragraph | medium] Max,meas(S,) 71/2

[p0173-b0036 | ordinary-paragraph | low] Ifl1,es

[p0173-b0037 | equation | low] f1L2()Po ≤ Ch

[p0173-b0038 | ordinary-paragraph | medium] Min,meas(S,)

[p0173-b0039 | ordinary-paragraph | medium] with a constant C, independent of h, K and f. The above remarks concerning the

[p0173-b0040 | ordinary-paragraph | medium] geometry of k imply that:

## PDF 174 / printed 160



[p0174-b0004 | equation | low] 1f/I2(R)P。 ≤ C4o21f11,x

[p0174-b0005 | equation | low] (3.17)

[p0174-b0006 | ordinary-paragraph | medium] Next assume that

[p0174-b0007 | equation | low] (3.18)

[p0174-b0008 | ordinary-paragraph | medium] We can write

[p0174-b0009 | ordinary-paragraph | low] f + q + allo,x

[p0174-b0010 | equation | low] inf

[p0174-b0011 | ordinary-paragraph | low] (q,@)∈ Pj-1xP;

[p0174-b0012 | equation | low] = inf inf Il(f + @) + qllo,x

[p0174-b0013 | ordinary-paragraph | low] q∈P;q∈Pj-1

[p0174-b0014 | equation | low] ≤(C4o2)j inf If + alj,k

[p0174-b0015 | ordinary-paragraph | low] aePj

[p0174-b0016 | ordinary-paragraph | medium] by the induction hypothesis (3.18). Then (3.17) yields:

[p0174-b0017 | ordinary-paragraph | medium] 1/2

[p0174-b0018 | equation | low] ∑10xf,

[p0174-b0019 | equation | low] I /L2()p; ≤ (C40)i+1

[p0174-b0020 | equation | low] a|=j

[p0174-b0021 | ordinary-paragraph | medium] Since the expression in brackets is I flj+1,*, this proves (3.18) for all j.

[p0174-b0022 | ordinary-paragraph | medium] As a consequence, we have:

[p0174-b0023 | equation | low] 11f — Pnf llo.K ≤(C4o)|det(B)1/2 1fk,k

[p0174-b0024 | ordinary-paragraph | medium] and (3.16) follows from (A.7) and the regularity of h.

[p0174-b0025 | ordinary-paragraph | medium] From Lemma 3.4, (3.15) and Theorem 3.2, we derive the expected estimate

[p0174-b0026 | ordinary-paragraph | medium] for this scheme.

[p0174-b0027 | theorem | medium] Theorem 3.3. Let Q be a bounded plane polygon and suppose the solution (u, p) of

[p0174-b0028 | ordinary-paragraph | medium] the Stokes system satisfies:

[p0174-b0029 | ordinary-paragraph | low] u∈ [H*+1(Ω) ∩ H(Ω)]²,  p∈ H*(Ω) N L(Q)

[p0174-b0030 | ordinary-paragraph | medium] for some integer ke [1, I]. If the triangulation J, is regular, the solution (un, pn) of

[p0174-b0031 | ordinary-paragraph | medium] (1.39) with the spaces X, and M, defined by (3.11) (3.12) has the estimate:

[p0174-b0032 | equation | low] [u - unl1,2 + II p - Phllo,a ≤ C,h*{/ulk+1,o + Iplk,s}.

[p0174-b0033 | ordinary-paragraph | medium] In addition, if Q is convex we have the L²-estimate:

[p0174-b0034 | equation | low] Ilu - un llo.s ≤ C2hk+1(ulk+1.2 + I plk.o).

[p0174-b0035 | subsection | medium] 3.3. An Example of Checkerboard Instability: the Q -Po Element

[p0174-b0036 | ordinary-paragraph | medium] The most famous example of spaces failing to satisfy the inf-sup condition is that

[p0174-b0037 | ordinary-paragraph | medium] in which the velocity is made of piecewise polynomials of Q? and the pressure

[p0174-b0038 | ordinary-paragraph | medium] is piecewise constant on a rectangular grid. This combination is more familiarly

## PDF 175 / printed 161



[p0175-b0003 | ordinary-paragraph | medium] called the “Q -P。" element. More precisely, let us assume that Ω is a bounded

[p0175-b0004 | ordinary-paragraph | medium] polygon with sides parallel to the axes and, to simplify suppose that T, is a square

[p0175-b0005 | ordinary-paragraph | medium] grid. We take:

[p0175-b0006 | equation | low] [Xh = {vh∈6()²; vhlk∈Q² VK∈ h, vhlr = 0}.

[p0175-b0007 | equation | low] (3.19)

[p0175-b0008 | equation | low] Mn = {an∈ L(Q); anik∈ Po KeTh}.

[p0175-b0009 | ordinary-paragraph | medium] (i+1,j+1)

[p0175-b0010 | ordinary-paragraph | medium] (i.j+1)

[p0175-b0011 | ordinary-paragraph | medium] (i+1/2.j+1/2)

[p0175-b0012 | ordinary-paragraph | medium] Ki.j

[p0175-b0013 | ordinary-paragraph | medium] (i+1,j)

[p0175-b0014 | ordinary-paragraph | medium] (i.j)

[p0175-b0015 | figure | medium] Figure 12

[p0175-b0016 | ordinary-paragraph | medium] This pair of spaces was introduced a long time ago and because of its simplicity

[p0175-b0017 | ordinary-paragraph | medium] was used (and is still used) by many numerical analysts and engineers in connec-

[p0175-b0018 | ordinary-paragraph | medium] tion with the Stokes Problem. But it was soon found out, through numerical

[p0175-b0019 | ordinary-paragraph | medium] instabilities in the approximate pressure, that there was something amiss with

[p0175-b0020 | ordinary-paragraph | medium] this choice of spaces.

[p0175-b0021 | ordinary-paragraph | medium] The most conspicuous anomaly of (3.19) is that Ker(B') is not reduced to {0}.

[p0175-b0022 | ordinary-paragraph | medium] Indeed, let (i,j) be a cartesian enumeration of the nodes of T, like in Figure 12,

[p0175-b0023 | ordinary-paragraph | medium] let ki.j denote the square with bottom left vertex (i,j) and let (i + 1/2,j + 1/2) be

[p0175-b0024 | ordinary-paragraph | medium] the index of the center of ki,§. To alleviate the notations, let v = (u,v) denote a

[p0175-b0025 | ordinary-paragraph | medium] function of X, and let ui,; or vi,; denote the vaiue of u or v at the node (i,j);

[p0175-b0026 | ordinary-paragraph | medium] similarly, we denote by qi+1/2.j+1/2 the value of q at the center of Ki.j. As qe Mh

[p0175-b0027 | ordinary-paragraph | medium] is constant on k;, ; we find immediately:

[p0175-b0028 | equation | low] q div v dx = h² qi+1/2,j+1/2(div v)i+1/2,j+1/2

[p0175-b0029 | ordinary-paragraph | low] Jki.j

[p0175-b0030 | equation | low] = h²qi+1/2,j+1/2[1/(2h)] {(ui+1,j+1 + ui+1,j — ui,j+1 —— ui,j)

[p0175-b0031 | ordinary-paragraph | low] + (Ui+1,j+1 + Vi,j+1 - Vi+1,j - Vi.j)}.

[p0175-b0032 | ordinary-paragraph | medium] Thus a summation by parts yields:

[p0175-b0033 | equation | low] qdivvdx =-h²∑{ui,;(Vi@i,j +vi,;(V2qi,j}

[p0175-b0034 | equation | low] (3.20)

## PDF 176 / printed 162



[p0176-b0004 | equation | low] (3.21)

[p0176-b0005 | equation | low] (V29)i,j = [1/(2h)](qi+1/2,j+1/2 + qi-1/2,j+1/2 — qi-1/2,j+1/2 - qi-1/2,j-1/2)

[p0176-b0006 | ordinary-paragraph | medium] and the summation runs over all interior nodes (i,j) of J, (since v vanishes on

[p0176-b0007 | ordinary-paragraph | medium] F). Therefore, if q belongs to Ker(B'), i.e. if qe M, and

[p0176-b0008 | equation | low] qdivvdx = 0

[p0176-b0009 | ordinary-paragraph | low] "XAA

[p0176-b0010 | ordinary-paragraph | medium] we must have

[p0176-b0011 | equation | low] qi-1/2,j+1/2 = Qi+1/2,j-1/2-

[p0176-b0012 | equation | low] qi+1/2,j+1/2 = qi-1/2,j-1/2>

[p0176-b0013 | ordinary-paragraph | low] 6

[p0176-b0014 | ordinary-paragraph | medium] b

[p0176-b0015 | ordinary-paragraph | low] a

[p0176-b0016 | ordinary-paragraph | medium] 。

[p0176-b0017 | ordinary-paragraph | medium] b

[p0176-b0018 | ordinary-paragraph | medium] b

[p0176-b0019 | ordinary-paragraph | medium] b

[p0176-b0020 | ordinary-paragraph | medium] a

[p0176-b0021 | ordinary-paragraph | low] D

[p0176-b0022 | ordinary-paragraph | low] D

[p0176-b0023 | ordinary-paragraph | medium] b

[p0176-b0024 | ordinary-paragraph | medium] b

[p0176-b0025 | ordinary-paragraph | medium] b

[p0176-b0026 | ordinary-paragraph | medium] b

[p0176-b0027 | ordinary-paragraph | medium] b

[p0176-b0028 | ordinary-paragraph | medium] a

[p0176-b0029 | ordinary-paragraph | medium] a

[p0176-b0030 | ordinary-paragraph | medium] a

[p0176-b0031 | ordinary-paragraph | medium] a

[p0176-b0032 | ordinary-paragraph | medium] a

[p0176-b0033 | ordinary-paragraph | medium] b

[p0176-b0034 | ordinary-paragraph | medium] b

[p0176-b0035 | ordinary-paragraph | medium] b

[p0176-b0036 | ordinary-paragraph | medium] b

[p0176-b0037 | ordinary-paragraph | low] b

[p0176-b0038 | ordinary-paragraph | medium] a

[p0176-b0039 | ordinary-paragraph | medium] a

[p0176-b0040 | ordinary-paragraph | medium] a

[p0176-b0041 | ordinary-paragraph | medium] 9

[p0176-b0042 | ordinary-paragraph | medium] b

[p0176-b0043 | ordinary-paragraph | medium] a

[p0176-b0044 | ordinary-paragraph | medium] b

[p0176-b0045 | ordinary-paragraph | medium] b

[p0176-b0046 | ordinary-paragraph | medium] b

[p0176-b0047 | ordinary-paragraph | medium] a

[p0176-b0048 | ordinary-paragraph | medium] a

[p0176-b0049 | ordinary-paragraph | medium] a

[p0176-b0050 | ordinary-paragraph | medium] a

[p0176-b0051 | equation | low] b=-a

[p0176-b0052 | ordinary-paragraph | medium] b

[p0176-b0053 | ordinary-paragraph | medium] b

[p0176-b0054 | ordinary-paragraph | medium] b

[p0176-b0055 | ordinary-paragraph | medium] b

[p0176-b0056 | ordinary-paragraph | medium] b

[p0176-b0057 | ordinary-paragraph | medium] a

[p0176-b0058 | ordinary-paragraph | medium] a

[p0176-b0059 | ordinary-paragraph | medium] a

[p0176-b0060 | ordinary-paragraph | medium] a

[p0176-b0061 | ordinary-paragraph | medium] a

[p0176-b0062 | ordinary-paragraph | medium] b

[p0176-b0063 | ordinary-paragraph | medium] b

[p0176-b0064 | ordinary-paragraph | medium] b

[p0176-b0065 | ordinary-paragraph | medium] a

[p0176-b0066 | ordinary-paragraph | medium] a

[p0176-b0067 | ordinary-paragraph | low] a

[p0176-b0068 | ordinary-paragraph | medium] a

[p0176-b0069 | ordinary-paragraph | medium] b

[p0176-b0070 | ordinary-paragraph | medium] b

[p0176-b0071 | ordinary-paragraph | medium] b

[p0176-b0072 | ordinary-paragraph | medium] b

[p0176-b0073 | ordinary-paragraph | medium] a

[p0176-b0074 | ordinary-paragraph | medium] a

[p0176-b0075 | ordinary-paragraph | medium] a

[p0176-b0076 | ordinary-paragraph | medium] b

[p0176-b0077 | ordinary-paragraph | medium] b

[p0176-b0078 | ordinary-paragraph | medium] b

[p0176-b0079 | ordinary-paragraph | medium] a

[p0176-b0080 | ordinary-paragraph | medium] a

[p0176-b0081 | ordinary-paragraph | medium] a

[p0176-b0082 | ordinary-paragraph | medium] a

[p0176-b0083 | figure | medium] Figure 13

[p0176-b0084 | ordinary-paragraph | medium] These equalities do not necessarily imply that q is a constant in Q. Rather, the

[p0176-b0085 | ordinary-paragraph | medium] values of q can alternate between two constants on adjacent elements like in

[p0176-b0086 | figure | medium] Figure 13. That these constants should be opposite numbers follows from the

[p0176-b0087 | ordinary-paragraph | medium] fact that fo q dx = 0.

[p0176-b0088 | ordinary-paragraph | medium] Let us characterize more precisely Ker(Bs). To simplify the discussion, it is

[p0176-b0089 | ordinary-paragraph | medium] convenient to suppose that Ω is the square (- 1, 1) x (- 1, 1) and that J, is the

[p0176-b0090 | ordinary-paragraph | medium] even square grid with mesh size

[p0176-b0091 | equation | low] h = 1/(2n)

[p0176-b0092 | ordinary-paragraph | medium] and nodes

[p0176-b0093 | equation | low] Xi,j = (ih,jh)

[p0176-b0094 | equation | low] with - 2n ≤ i,j ≤ 2n

[p0176-b0095 | ordinary-paragraph | medium] (cf. Figure 14). Let μe M, be defined by

[p0176-b0096 | equation | low] μlks =(-1)i+j

[p0176-b0097 | equation | low] (3.22)

[p0176-b0098 | ordinary-paragraph | low] Vkii C Jh.

## PDF 177 / printed 163



[p0177-b0002 | figure | high] Figure 14

[p0177-b0003 | ordinary-paragraph | high] It stems from the above considerations that

[p0177-b0004 | ordinary-paragraph | high] (3223) Ker(B,,) = span(y).

[p0177-b0005 | ordinary-paragraph | high] Because of its alternate “plus and minus” pattern, the function p is called a

[p0177-b0006 | ordinary-paragraph | high] checkerboard function. Its connection with Ker(B,,) was first reported by Fortin

[p0177-b0007 | ordinary-paragraph | high] [28] and then by Sani et al. [70].

[p0177-b0008 | ordinary-paragraph | high] In view of (3.23), the pair of spaces (X,,, M,,) has no chance of satisfying the

[p0177-b0009 | ordinary-paragraph | high] inf-sup condition. To save the situation, the first step we can take is to replace

[p0177-b0010 | ordinary-paragraph | high] M,, by [Ker(B;,)]+. Let us characterize this space. Let J = 2i+ landJ = 2j + 1

[p0177-b0011 | ordinary-paragraph | high] for —n <i,j <n-—1 and let the macro-element @, , be the union of the four

[p0177-b0012 | ordinary-paragraph | high] squares k with common vertex (I, J). Following Johnson & Pitkaranta [46], for

[p0177-b0013 | ordinary-paragraph | high] each (I, J) we introduce the four functions (v,);,;1<k<4 which take the value

[p0177-b0014 | ordinary-paragraph | high] +1 on the subsquares of Q, ,a ccording to the pattern of Figure 15.

[p0177-b0015 | ordinary-paragraph | high] Note that

[p0177-b0016 | ordinary-paragraph | high] (3.24) | (v,); 34x =0 whenk #1

## PDF 178 / printed 164



[p0178-b0003 | ordinary-paragraph | medium] 1

[p0178-b0004 | ordinary-paragraph | medium] 1

[p0178-b0005 | ordinary-paragraph | low] (vJ

[p0178-b0006 | ordinary-paragraph | low] (v3)1.)

[p0178-b0007 | ordinary-paragraph | low] (v2h.]

[p0178-b0008 | ordinary-paragraph | low] (vh.)

[p0178-b0009 | figure | medium] Figure 15

[p0178-b0010 | ordinary-paragraph | medium] and

[p0178-b0011 | equation | low] (vk)1,s(vi)1,dx = 0 if k ≠ l.

[p0178-b0012 | equation | low] (3.25)

[p0178-b0013 | ordinary-paragraph | low] JQ1.J

[p0178-b0014 | ordinary-paragraph | medium] Taking into account (3.24), it is easy to see that (3.19) defines M, as follows:

[p0178-b0015 | ordinary-paragraph | medium] 4

[p0178-b0016 | equation | low] ∑∑ (a)i,J(Vb)I,J;

[p0178-b0017 | equation | low] ∑(α)

[p0178-b0018 | ordinary-paragraph | medium] Furthermore since the spurious function μ can only arise from the "local alternat-

[p0178-b0019 | ordinary-paragraph | medium] ing" function v4, we have in view of (3.25):

[p0178-b0020 | ordinary-paragraph | medium] 4

[p0178-b0021 | equation | low] ∑(x1).s =(x4).s = 0{

[p0178-b0022 | equation | low] ∑ ∑ (ak).s(vk)1.s;

[p0178-b0023 | equation | low] [Ker(B)]

[p0178-b0024 | ordinary-paragraph | medium] To simplify we use the notation:

[p0178-b0025 | equation | low] M =[Ker(B)]

[p0178-b0026 | equation | low] (3.26)

[p0178-b0027 | ordinary-paragraph | medium] Since we are working with finite dimensional spaces the pair (X,, M ,) satisfies

[p0178-b0028 | ordinary-paragraph | medium] the inf-sup condition (1.12). Unfortunately this is not the end of trouble for, as

[p0178-b0029 | ordinary-paragraph | medium] we are going to see below, the condition is not uniformly satisfied with respect

[p0178-b0030 | ordinary-paragraph | medium] to h,

[p0178-b0031 | lemma | medium] Lemma 3.5. Let Q be like above and let the spaces X, and M, be defined by (3.19)

[p0178-b0032 | ordinary-paragraph | medium] and (3.26) respectively. There exists a constant C > 0, independent of h, such that:

[p0178-b0033 | equation | low] (3.27)

[p0178-b0034 | ordinary-paragraph | medium] qdiv v dx

[p0178-b0035 | equation | low] ≥ Chllgllo.s

[p0178-b0036 | equation | low] sup

[p0178-b0037 | ordinary-paragraph | low] Vqe Mh.

[p0178-b0038 | ordinary-paragraph | low] vl1,Ω

[p0178-b0039 | ordinary-paragraph | low] VEXn

[p0178-b0040 | ordinary-paragraph | low] Ω

[p0178-b0041 | proof | medium] Proof. Let q be an arbitrary function of .M,; we introduce the discrete seminorm:

[p0178-b0042 | ordinary-paragraph | medium] 1/2

[p0178-b0043 | equation | low] lql1,h =

[p0178-b0044 | equation | low] ∑h²{(Pq）+(V2j}

[p0178-b0045 | equation | low] (3.28)

[p0178-b0046 | ordinary-paragraph | medium] where the summation runs over all interior nodes (i,j) of T,. In view of (3.20), we

[p0178-b0047 | ordinary-paragraph | medium] define the function v = (u, v) of X, by:

[p0178-b0048 | equation | low] ui.j = --(V1q)i.j

[p0178-b0049 | equation | low] Vi.j=-(V2q)i.j

## PDF 179 / printed 165



[p0179-b0003 | ordinary-paragraph | medium] on all interior nodes (i,j) of ,. With this choice we have:

[p0179-b0004 | equation | low] qdivvdx =lqli,h

[p0179-b0005 | ordinary-paragraph | medium] and by virtue of Lemma A.6, an easy calculation gives:

[p0179-b0006 | equation | low] [vl1,2 ≤ (C /h) lvllo,α ≤ (C2 /h)lql1,h

[p0179-b0007 | ordinary-paragraph | medium] Therefore

[p0179-b0008 | equation | low] q div vdx

[p0179-b0009 | equation | low] [vl1,o ≥(h/C2)1ql1,h

[p0179-b0010 | ordinary-paragraph | low] Ω

[p0179-b0011 | ordinary-paragraph | medium] and (3.27) will be established if we show the following analogue of Theorem I.1.9:

[p0179-b0012 | ordinary-paragraph | low] "mbA

[p0179-b0013 | equation | low] (3.29)

[p0179-b0014 | equation | low] llallo,a ≤ Cslal1,h

[p0179-b0015 | ordinary-paragraph | medium] Let us prove (3.29). First a straightforward, constructive argument shows

[p0179-b0016 | ordinary-paragraph | medium] that (3.29) holds for every function q of Q, that vanishes on two elements Ki, j:

[p0179-b0017 | ordinary-paragraph | medium] one with i + j even and one with i + j odd. And of course the constant C, is

[p0179-b0018 | ordinary-paragraph | medium] independent of h and q. Next, if q belongs to M, it is easy to find q e Ker(B') ① R

[p0179-b0019 | ordinary-paragraph | medium] such that q -- q is like above. Then the orthogonality of q and q implies that

[p0179-b0020 | equation | low] llall6,α = llq - g ll,2 - I1al16,2 ≤ C3!q -- gli,n = C31ali,h-

[p0179-b0021 | ordinary-paragraph | medium] For a long time it was conjectured that (3.27) could not be improved; but it

[p0179-b0022 | ordinary-paragraph | medium] is only recently that Boland & Nicolaides [12] established it with the following

[p0179-b0023 | ordinary-paragraph | medium] counter-example. Roughly speaking, the idea is to find a function q in .M , such

[p0179-b0024 | ordinary-paragraph | medium] that

[p0179-b0025 | ordinary-paragraph | low] [vl1,2

[p0179-b0026 | ordinary-paragraph | medium] q divvdx

[p0179-b0027 | ordinary-paragraph | low] Ω

[p0179-b0028 | ordinary-paragraph | medium] is small while Il q ll o.o is large.

[p0179-b0029 | ordinary-paragraph | medium] More precisely let

[p0179-b0030 | equation | low] q =∑{1(v4)1.3}.

[p0179-b0031 | equation | low] (3.30)

[p0179-b0032 | ordinary-paragraph | low] I.J

[p0179-b0033 | ordinary-paragraph | medium] On the one hand, q is indeed in .M, because I runs over integers of opposite signs.

[p0179-b0034 | ordinary-paragraph | medium] On the other hand, a simple calculation shows that:

[p0179-b0035 | equation | low] llal16,α = 4h²(2n) ∑ 12 = 4h(2n/3)(4n² -- 1).

[p0179-b0036 | ordinary-paragraph | medium] Thus

[p0179-b0037 | equation | low] Il llo.2 = [2/(/3h)](1 - h2)1/2

[p0179-b0038 | equation | low] (3.31)

[p0179-b0039 | ordinary-paragraph | medium] Next, let us evaluate fo q div v dx. According to (3.21) we have:

[p0179-b0040 | ordinary-paragraph | medium] if i is odd,

[p0179-b0041 | ordinary-paragraph | medium] 0

## PDF 180 / printed 166



[p0180-b0004 | equation | low] ∑ {u(2ih,(2j + 1)h) - v(2ih,2jh)}

[p0180-b0005 | equation | low] qdivvdx = 2h

[p0180-b0006 | equation | low] i=-（n-1）j=-n

[p0180-b0007 | ordinary-paragraph | low] VQ

[p0180-b0008 | ordinary-paragraph | medium] f(2j+1)h

[p0180-b0009 | ordinary-paragraph | medium] 0v(2ih, x2)/0x2 dx2

[p0180-b0010 | equation | low] (j=-nJ2jh

[p0180-b0011 | equation | low] =-（n-1）

[p0180-b0012 | ordinary-paragraph | medium] 2jh

[p0180-b0013 | ordinary-paragraph | low] Z

[p0180-b0014 | ordinary-paragraph | medium] 0v(2ih, x2)/0x2 dx2

[p0180-b0015 | equation | low] j=-n+1 J(2j-1)h

[p0180-b0016 | ordinary-paragraph | medium] Hence

[p0180-b0017 | equation | low] qdivvdx|≤h ∑

[p0180-b0018 | ordinary-paragraph | medium] [0v(2ih, x2)/0x21 dx2

[p0180-b0019 | equation | low] i=-(n-1)J-1

[p0180-b0020 | ordinary-paragraph | low] Ω

[p0180-b0021 | ordinary-paragraph | medium] n-1

[p0180-b0022 | equation | low] ≤√2h(2n - 1)1/2

[p0180-b0023 | equation | low] ∑(0v(2ih, x2)/0x2|² dx

[p0180-b0024 | equation | low] i=-(n-1)

[p0180-b0025 | ordinary-paragraph | medium] Now observe that for every affine function f, the following quadrature formula

[p0180-b0026 | ordinary-paragraph | medium] holds:

[p0180-b0027 | equation | low] f²(x)dx = (1/3) ( f²(0) + f(0)f(1) + f2(1)}.

[p0180-b0028 | equation | low] ≥ (1/4) Max(f2(0), f2(1)),

[p0180-b0029 | ordinary-paragraph | medium] in view of the inequality

[p0180-b0030 | equation | low] ab ≤ (1/4)a² + b2 

[p0180-b0031 | equation | low] Va, b ≥ 0.

[p0180-b0032 | ordinary-paragraph | medium] As a consequence

[p0180-b0033 | ordinary-paragraph | medium] 1

[p0180-b0034 | ordinary-paragraph | low] n-

[p0180-b0035 | equation | low]  10u(2ih,x2)/0x212 ≤(2/h)

[p0180-b0036 | ordinary-paragraph | medium] 10v(x1, x2)/0x212 dx1.

[p0180-b0037 | ordinary-paragraph | medium] iz-(n-1)

[p0180-b0038 | ordinary-paragraph | medium] (Here we use the fact that Ou/ox, is a continuous and piecewise affine function

[p0180-b0039 | ordinary-paragraph | medium] of x1). Therefore,

[p0180-b0040 | equation | low] q divvdx| ≤ 2(1 -- h)/2|vl1,o.

[p0180-b0041 | ordinary-paragraph | medium] Combined with (3.31), this becomes:

[p0180-b0042 | equation | low] Ivli.s ≤√3hllallo..

[p0180-b0043 | equation | low] q div v dx

[p0180-b0044 | ordinary-paragraph | medium] Thus we have proved the following resuit:

[p0180-b0045 | lemma | medium] Lemma 3.6. Under the hypotheses of Lemma 3.5, the function q defined by (3.30)

[p0180-b0046 | ordinary-paragraph | medium] belongs to M, and satisfies:

## PDF 181 / printed 167



[p0181-b0003 | ordinary-paragraph | low] [(

[p0181-b0004 | equation | low] v,o≤√3hllallo,

[p0181-b0005 | equation | low] q div v dx

[p0181-b0006 | equation | low] sup

[p0181-b0007 | ordinary-paragraph | low] VeXh

[p0181-b0008 | ordinary-paragraph | medium] Together with Lemma 3.5, this means that the constant β* is really O(h).

[p0181-b0009 | ordinary-paragraph | medium] In fact, it can be proved that this undesirable factor h arises exclusively from

[p0181-b0010 | ordinary-paragraph | medium] the local alternating component v4 in the functions of M,. Again let us write

[p0181-b0011 | ordinary-paragraph | medium] qE M, in terms of the basis functions vk:

[p0181-b0012 | ordinary-paragraph | medium] 4

[p0181-b0013 | equation | low] k=1

[p0181-b0014 | ordinary-paragraph | medium] where

[p0181-b0015 | ordinary-paragraph | low] (akvk)I,J, (α)1,J∈ R,

[p0181-b0016 | equation | low] =∑ (α4)1,J = 0.

[p0181-b0017 | ordinary-paragraph | low] Z(a)1,J

[p0181-b0018 | ordinary-paragraph | medium] Following Boland & Nicolaides [12] we split .l, as follows:

[p0181-b0019 | equation | low] M = Ah + Mn,

[p0181-b0020 | ordinary-paragraph | medium] where

[p0181-b0021 | equation | low] An = {q∈Mn; qlo,, = (a4v4)1,J},

[p0181-b0022 | equation | low] (3.32)

[p0181-b0023 | equation | low] Mn =A={q∈Mh;qla.s =(α1v1 + α2V2 + αv3),J}

[p0181-b0024 | ordinary-paragraph | medium] and we associate with these spaces the following subspace of Xh:

[p0181-b0025 | equation | low] Vh = {vh∈Xh;(qh, divvn) = O Van∈An}.

[p0181-b0026 | equation | low] (3.33)

[p0181-b0027 | ordinary-paragraph | medium] We propose to establish that the pair ( V, M,) satisfies a uniform inf-sup condition.

[p0181-b0028 | ordinary-paragraph | medium] To this end, let us start with a local condition.

[p0181-b0029 | lemma | medium] Lemma 3.7. With the above notations and hypotheses of Lemma 3.5, the pair

[p0181-b0030 | ordinary-paragraph | medium] (Vh, Mn) satisfies uniformly a local inf-sup condition with respect to the partition

[p0181-b0031 | ordinary-paragraph | low] {21,1} of .

[p0181-b0032 | proof | medium] Proof. Let

[p0181-b0033 | equation | low] Xh(Q,小) = {v∈ Vh; vlo2., = 0}),

[p0181-b0034 | equation | low] M(Q1,J) = {qle,s; qe Mn} n L2(Q1.J).

[p0181-b0035 | ordinary-paragraph | medium] We must show that all qe M,(Qi.J) satisfy:

[p0181-b0036 | equation | low] Ivli.o., ≥ Cll llo.2,.

[p0181-b0037 | equation | low] q div v dx

[p0181-b0038 | equation | low] (3.34)

[p0181-b0039 | equation | low] sup

[p0181-b0040 | ordinary-paragraph | low] veXno.) LJQ.)

[p0181-b0041 | ordinary-paragraph | medium] First, observe that

[p0181-b0042 | equation | low] Xh(Q1.1) = {v = V1,JΦ1,J; Vv1,J = (u1,J,U1,J)∈ R²},

[p0181-b0043 | ordinary-paragraph | medium] where Φi.s denotes the basis function of X, that takes the value 1 at the node

## PDF 182 / printed 168



[p0182-b0004 | ordinary-paragraph | medium] Then formula (3.20) yields for all ve X,(Q, J) and qe M,(Q1,J):

[p0182-b0005 | equation | low] q div vdx = -2h(α2u1,J + α3V1,J),

[p0182-b0006 | ordinary-paragraph | low] J21.J

[p0182-b0007 | ordinary-paragraph | medium] where

[p0182-b0008 | equation | low] Ilallo,2,.s = 2h(x2 + α3)1/2.

[p0182-b0009 | ordinary-paragraph | medium] By choosing

[p0182-b0010 | equation | low] u1,J = - 2hα2,

[p0182-b0011 | equation | low] V1.J = - 2ha3

[p0182-b0012 | ordinary-paragraph | medium] we immediately obtain (3.34) with C = (3/8)1/2.

[p0182-b0013 | ordinary-paragraph | medium] Thus setting,

[p0182-b0014 | equation | low] M, = {qe L(Q); qla.,eR VI, J} = {q∈ Mn; ala., = (av1)1,J}

[p0182-b0015 | ordinary-paragraph | medium] it follows from Theorem 1.12 that (V, M,) satisfies a uniform inf-sup condition

[p0182-b0016 | ordinary-paragraph | medium] provided the same is true for the pair (Vh, Mh). This last property is less obvious.

[p0182-b0017 | ordinary-paragraph | medium] In order to prove it, it is convenient to group the macro-elements Q.y four by

[p0182-b0018 | ordinary-paragraph | medium] four like in Figure 16; and of course we must assume that these super macro-

[p0182-b0019 | ordinary-paragraph | medium] elements Oa,g form again a partition of Q. Then we proceed in two steps. First

[p0182-b0020 | ordinary-paragraph | medium] we introduce the subspace of M,:

[p0182-b0021 | equation | low] M2n = {qe L(Ω); qlo.s∈ R Vα, β}

[p0182-b0022 | ordinary-paragraph | medium] and we prove that the pair (V, Mzh) satisfies a uniform inf-sup condition. Next

[p0182-b0023 | ordinary-paragraph | medium] we show that the pair (V, Mh) satisfies a local inf sup-condition on each set Oa.8-

[p0182-b0024 | ordinary-paragraph | medium] This is achieved in the next two lemmas.

[p0182-b0025 | ordinary-paragraph | medium] (α-1.β+1)

[p0182-b0026 | ordinary-paragraph | medium] (α+1,β3+1)

[p0182-b0027 | ordinary-paragraph | medium] 2h

[p0182-b0028 | ordinary-paragraph | medium] (α.β)

[p0182-b0029 | ordinary-paragraph | medium] 2h

[p0182-b0030 | ordinary-paragraph | medium] (α-1,β-1)

[p0182-b0031 | ordinary-paragraph | medium] (α+1.β-1)

[p0182-b0032 | ordinary-paragraph | medium] 2h

[p0182-b0033 | ordinary-paragraph | medium] 2h

## PDF 183 / printed 169



[p0183-b0003 | lemma | medium] Lemma 3.8. Assume that Q can be partitioned into groups @a.p of four macro-

[p0183-b0004 | ordinary-paragraph | medium] elements Q1.s like in Figure 16. Then the pair (Vh, Mzn) satisfies a global uniform

[p0183-b0005 | ordinary-paragraph | medium] inf-sup condition.

[p0183-b0006 | proof | medium] Proof. First, observe that the functions of X2, belong necessarily to V, because

[p0183-b0007 | ordinary-paragraph | medium] their divergence reduces to polynomials of P, in each macro-element Q, j and

[p0183-b0008 | equation | low] (v4)i.spdx = O  Vpe P.

[p0183-b0009 | ordinary-paragraph | low] JS1.3

[p0183-b0010 | ordinary-paragraph | medium] Therefore let us prove the inf-sup condition for the pair (Xzh, M2h).

[p0183-b0011 | ordinary-paragraph | medium] For this, we exhibit an adequate operator 7, very similar to that of Lemma

[p0183-b0012 | subsection | medium] 2.2. Let R, be the local regularization operator of Section A.3 and let us fix one

[p0183-b0013 | ordinary-paragraph | medium] of the super macro-elements O.s. For v in H′(Oa.s) we define mveQ1 on each

[p0183-b0014 | ordinary-paragraph | low] Ω1,J C Oa,p by:

[p0183-b0015 | equation | low] πU(xi,.) = Ru(xi,j)  at the four corners and center of x,B

[p0183-b0016 | equation | low] (πv -- v)ds = 0 on each side T of o,β.

[p0183-b0017 | ordinary-paragraph | medium] T

[p0183-b0018 | ordinary-paragraph | medium] Then, we take Thv = tv on each Oa.b.

[p0183-b0019 | ordinary-paragraph | medium] By inspection, it easy to verify that π, E (H(Q)²; Xzh) and

[p0183-b0020 | equation | low] div(πnv - v)qdx = 0 Vq∈M2h.

[p0183-b0021 | ordinary-paragraph | low] JΩ

[p0183-b0022 | ordinary-paragraph | medium] Furthermore a simple argument shows that

[p0183-b0023 | equation | low] [,vl1.o ≤ Clvli,o with a constant C > 0 independent of h.

[p0183-b0024 | ordinary-paragraph | medium] This yields the desired inf-sup condition,

[p0183-b0025 | lemma | medium] Lemma 3.9. On each Ca.p, the pair of spaces (V,Mh) satisfies a local inf-sup

[p0183-b0026 | ordinary-paragraph | medium] condition.

[p0183-b0027 | proof | medium] Proof. Let q belong to the space:

[p0183-b0028 | equation | low] Mh(Oa,β) = {q I0c,} N L2(Ox,β).

[p0183-b0029 | ordinary-paragraph | medium] We must construct v in V, with vlao., = 0 such that

[p0183-b0030 | equation | low] Ivl1,0., ≥ C ll llo,0c.s-

[p0183-b0031 | equation | low] q div v dx

[p0183-b0032 | equation | low] (3.35)

[p0183-b0033 | ordinary-paragraph | low] JOα.8

[p0183-b0034 | ordinary-paragraph | medium] Let us fix v = 0 on the boundary and central nodes of Oa,s and also at the

[p0183-b0035 | ordinary-paragraph | medium] central node of each macro-element Ω1.j contained in Oa.s. Then, in view of the

[p0183-b0036 | ordinary-paragraph | medium] formula

## PDF 184 / printed 170



[p0184-b0003 | equation | low] Ci = SW Ua —h(V2q)i,j

[p0184-b0004 | ordinary-paragraph | high] on all remaining nodes (i,j) of O,,¢ (i.e. (a + 1, B),(% B + 1)). Wecan easily see that

[p0184-b0005 | equation | low] (V4); (Vd :,; =9 fork = 1, 2, on all such nodes (i, j).

[p0184-b0006 | ordinary-paragraph | high] Hence the resulting function v belongs to V,, and satisfies

[p0184-b0007 | equation | low] | qdivvdx =hY {\u,| ? + |v,,4\7}-

[p0184-b0008 | ordinary-paragraph | high] oO, B i,j

[p0184-b0009 | ordinary-paragraph | high] Then (3.35) follows from the inequality:

[p0184-b0010 | ordinary-paragraph | high] 1/2

[p0184-b0011 | ordinary-paragraph | high] 2

[p0184-b0012 | equation | low] IVinli.0,,, <C, (5( tu? as |v;, || } >

[p0184-b0013 | ordinary-paragraph | high] ij

[p0184-b0014 | ordinary-paragraph | high] with a constant C, independent of h, « and f, and

[p0184-b0015 | ordinary-paragraph | high] 2

[p0184-b0016 | ordinary-paragraph | high] lta ar |v; ;|7} Z 2) I4r.3l

[p0184-b0017 | ordinary-paragraph | high] iF Tf

[p0184-b0018 | ordinary-paragraph | high] considering that ),,; q;,; = 0 since ge Lo(,,g ). C]

[p0184-b0019 | ordinary-paragraph | high] Lemmas 3.7, 3.8 and 3.9 yield immediately the next result.

[p0184-b0020 | theorem | high] Theorem 3.4. Assume that Q can be partitioned into groups ©,, p Of four macro-

[p0184-b0021 | ordinary-paragraph | high] elements like in Figure 16. Then the pair (V,,M,) defined by (3.33) and (3.32)

[p0184-b0022 | ordinary-paragraph | high] satisfies a uniform inf-sup condition.

[p0184-b0023 | remark | high] Remark 3.1. The argument of Lemma 3.8 can be used directly to show that the

[p0184-b0024 | ordinary-paragraph | high] pair (X;,, M,,) satisfies a uniform inf-sup condition but this does not imply that

[p0184-b0025 | ordinary-paragraph | high] (V,, M,,) satisfies it as well.

[p0184-b0026 | remark | high] Remark 3.2. The above analysis does not apply directly to arbitrary quadrilat-

[p0184-b0027 | ordinary-paragraph | high] erals. Usually, the “checkerboard” spurious pressure disappears from M, but the

[p0184-b0028 | ordinary-paragraph | high] inf-sup condition is not satisfied (cf. Sani et al [70]). However, it is possible to

[p0184-b0029 | ordinary-paragraph | high] derive similar results for special quadrilateral meshes (cf. Pitkaranta & Stenberg

[p0184-b0030 | ordinary-paragraph | high] [65]).

[p0184-b0031 | subsection | high] 3.4. Error Estimates for the Q ,—P, Element

[p0184-b0032 | ordinary-paragraph | high] The object of this section is to show that, although it does not satisfy the inf-sup

[p0184-b0033 | ordinary-paragraph | high] condition, the pair of spaces (X;,, M,,) can still be used to compute successfully

[p0184-b0034 | ordinary-paragraph | high] the velocity u and (with some precautions) the pressure p. For this purpose, the

[p0184-b0035 | ordinary-paragraph | high] statement of Theorem 3.4 will play a crucial role.

[p0184-b0036 | ordinary-paragraph | high] Let (u,, p,)€X, x M,, be a solution of:

## PDF 185 / printed 171



[p0185-b0002 | ordinary-paragraph | high] (3.26) aes Ups grad.y, )i—3(Dyy divv,) = <f,v, > aVy,exX

[p0185-b0003 | equation | low] (q,, div u,) = 0 Van€ M,,

[p0185-b0004 | ordinary-paragraph | high] with X, and M,, defined by (3.19). We know that u, is unique but that each p, is

[p0185-b0005 | ordinary-paragraph | high] of the form:

[p0185-b0006 | equation | low] Pi = By + Dy + Cy

[p0185-b0007 | ordinary-paragraph | high] with ys defined by (3.22), p? and p,, uniquely determined in A, and M, respectively

[p0185-b0008 | ordinary-paragraph | high] and C arbitrary. Furthermore, u,¢V, with V;, defined by (3.33) and the pair

[p0185-b0009 | ordinary-paragraph | high] (u,,B,)€V, x M, is the unique solution of:

[p0185-b0010 | equation | low] (G,,divu,)=0 VgG,eM,,.

[p0185-b0011 | ordinary-paragraph | high] |

[p0185-b0012 | ordinary-paragraph | high] Therefore, owing to Theorem 3.4, we can apply straight away Theorem 1.1 2°)

[p0185-b0013 | ordinary-paragraph | high] with V, and M, instead of X,, and M, respectively:

[p0185-b0014 | ordinary-paragraph | high] ju — Unl 1.2 + ||P — Prllo,e

[p0185-b0015 | ordinary-paragraph | high] (3.38) : s

[p0185-b0016 | equation | low] <C, in ju — Vili.e ate _inf |p — inlowah

[p0185-b0017 | ordinary-paragraph | high] V,EVn qne My,

[p0185-b0018 | ordinary-paragraph | high] with a constant C, > 0 independent of h.

[p0185-b0019 | ordinary-paragraph | high] Hence it remains to investigate the approximation properties of the spaces

[p0185-b0020 | ordinary-paragraph | high] V, and M,,. As far as V, is concerned, recall that (cf. Lemma 3.8):

[p0185-b0021 | ordinary-paragraph | high] XG Vig

[p0185-b0022 | ordinary-paragraph | high] Thus, formula (A.49) yields:

[p0185-b0023 | ordinary-paragraph | high] (3.39) inf |u — ¥%4|,.9< |u—J,,U|;q9<Cyhlul,q Vue H?(Q)’.

[p0185-b0024 | ordinary-paragraph | high] tnEeVn

[p0185-b0025 | ordinary-paragraph | high] Likewise, since M, < M,, formula (A.51) gives:

[p0185-b0026 | ordinary-paragraph | high] (3.40) inf |lp — G&llo.e< IP — PrrPllo.e < C3h|plig VpeH*(Q).

[p0185-b0027 | ordinary-paragraph | high] Gn€ Mp

[p0185-b0028 | ordinary-paragraph | high] These three inequalities are combined in the following theorem.

[p0185-b0029 | theorem | high] Theorem 3.5. Assume that Q is like in Theorem 3.4 and suppose the solution (u, p)

[p0185-b0030 | ordinary-paragraph | high] of the Stokes system satisfies:

[p0185-b0031 | ordinary-paragraph | high] ue[H?7(Q)NHj(Q)]?, pe H'(Q)LGN( Q ).

[p0185-b0032 | ordinary-paragraph | high] Then the solution (u,, p,) of the scheme (3.36) has the error estimate:

[p0185-b0033 | ordinary-paragraph | high] (3.41) ju — uyl1,a+ lp — Prllo.e < Ch{lul+o IP,li.aa} ;

[p0185-b0034 | ordinary-paragraph | high] where p,, is the component of p,, in M,.

[p0185-b0035 | ordinary-paragraph | high] Here the component f, acts as a filter for the pressure p, since it discards

## PDF 186 / printed 172



[p0186-b0004 | ordinary-paragraph | medium] p, the supplementary component of p, in A, is bounded. Indeed, it stems from

[p0186-b0005 | ordinary-paragraph | medium] (3.36) that

[p0186-b0006 | ordinary-paragraph | low] "X"AA

[p0186-b0007 | equation | low] (ph, divvn) = v(grad(un - u), grad vn) + (p - Ph, div vh)

[p0186-b0008 | ordinary-paragraph | medium] Therefore,

[p0186-b0009 | ordinary-paragraph | medium] (pt, divvh)

[p0186-b0010 | equation | low] ≤ C4h{|ul2,2 + Ipli,a}.

[p0186-b0011 | equation | low] sup

[p0186-b0012 | ordinary-paragraph | low] [vnl1,Q

[p0186-b0013 | ordinary-paragraph | low] Vh∈Xn

[p0186-b0014 | ordinary-paragraph | medium] It may happen, in the best of cases, that the left-hand side of this inequality is

[p0186-b0015 | ordinary-paragraph | medium] bounded below by Cs Il p llo.s with a constant Cs that does not depend upon h

[p0186-b0016 | ordinary-paragraph | medium] and thus I pllo.o is O(h). However, in the general case, all we can do is apply

[p0186-b0017 | lemma | medium] Lemma 3.5; it yields the next result.

[p0186-b0018 | corollary | medium] Corollary 3.1. Under the hypotheses of Theorem 3.5, the component p of p, in Ah

[p0186-b0019 | ordinary-paragraph | medium] is bounded as follows:

[p0186-b0020 | equation | low] (3.42)

[p0186-b0021 | equation | low] Il ph lo.s ≤ C{lul2,2 + Ipl1,2}.

[p0186-b0022 | ordinary-paragraph | medium] Finally, we can also apply Theorem 1.2 with the pair of spaces (V, M,) and

[p0186-b0023 | ordinary-paragraph | medium] derive an optimal error estimate for Ilu - u, llo.Ω.

[p0186-b0024 | corollary | medium] Corollary 3.2. Under the hypotheses of Theorem 3.5, we have:

[p0186-b0025 | equation | low] (3.43)

[p0186-b0026 | equation | low] Ilu - un llo,o ≤ Ch²{Iul2.o + Ipl1,2}.

[p0186-b0027 | equation | low] (0.0)

[p0186-b0028 | equation | low] (0.0)

[p0186-b0029 | equation | low] (0.0)

[p0186-b0030 | equation | low] (0.0)

[p0186-b0031 | equation | low] (1.1)

[p0186-b0032 | ordinary-paragraph | medium] (1.-1)

[p0186-b0033 | equation | low] (0.0)

[p0186-b0034 | equation | low] (0.0)

[p0186-b0035 | ordinary-paragraph | medium] K

[p0186-b0036 | equation | low] (0.0)

[p0186-b0037 | equation | low] (0.0)

[p0186-b0038 | ordinary-paragraph | medium] (-1,1)

[p0186-b0039 | ordinary-paragraph | medium] (-1,-1)

[p0186-b0040 | equation | low] (0.0)

[p0186-b0041 | ordinary-paragraph | medium] (0,0)

[p0186-b0042 | equation | low] (0.0)

[p0186-b0043 | ordinary-paragraph | medium] (0,0)

[p0186-b0044 | figure | medium] Figure 17
