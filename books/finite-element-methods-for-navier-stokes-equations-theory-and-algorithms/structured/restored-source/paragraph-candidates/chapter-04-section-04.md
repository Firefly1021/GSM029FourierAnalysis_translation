# Paragraph candidates: chapter-04-section-04

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-04-section-04-pc00001 | ordinary-paragraph | high | PDF 330

FuFa(A, Gn(A)) (On — Wh) — Fal, Un) + Fi(A, Wa)l x

## chapter-04-section-04-pc00002 | equation | low | PDF 330

[[FORMULA:f-p0330-05428]]

## chapter-04-section-04-pc00003 | ordinary-paragraph | high | PDF 330

VAEA, Vv,, w,€ S(t, (A); 0) 9 V,. Let

## chapter-04-section-04-pc00004 | equation | low | PDF 330

[[FORMULA:f-p0330-05429]]

## chapter-04-section-04-pc00005 | equation | low | PDF 330

[[FORMULA:f-p0330-05430]]

## chapter-04-section-04-pc00006 | ordinary-paragraph | high | PDF 330

The monotonicity of L,, implies that

## chapter-04-section-04-pc00007 | equation | low | PDF 330

[[FORMULA:f-p0330-05431]]

## chapter-04-section-04-pc00008 | ordinary-paragraph | high | PDF 330

By assumption, the mapping py — L,(u;K) is monotonically increasing with respect to h and pw and continuous at py = 0. In addition, by virtue of (3.65), it satisfies the condition (3.57). As a consequence, we can apply the conclusion of Theorem 3.7. It yields (3.66); then (3.67) stems from (3.30’) with v, = a,(A), (3.68) and (3.59). ‘|

## chapter-04-section-04-pc00009 | remark | high | PDF 330

Remark 3.9. The space V, which enters only in the assumption (3.61), plays a

## chapter-04-section-04-pc00010 | ordinary-paragraph | high | PDF 330

minor part in this proof. It is useful when the restriction operator 2, requires more regularity than the space X can provide.

## chapter-04-section-04-pc00011 | section | high | PDF 330

§4. Numerical Analysis of Centered Finite Element Schemes

## chapter-04-section-04-pc00012 | ordinary-paragraph | high | PDF 330

In this paragraph, we propose to apply to the homogeneous Navier-Stokes equations most of the finite element methods developed in Chapters II and III to solve the Stokes problem. The reader will find that in nearly every case, the error analysis carries over successfully to Navier-Stokes equations. One of the few exceptions is the three-dimensional mixed method elaborated in Paragraph IfI.5. This method can be tried to solve the Navier-Stokes system but at the present stage, its numerical analysis is still an open problem.

## chapter-04-section-04-pc00013 | subsection | high | PDF 330

4.1. Formulation in Primitive Variables: Methods Using Discontinuous

## chapter-04-section-04-pc00014 | ordinary-paragraph | high | PDF 330

Pressures The situation is that of Section II.1.3. For each value of the parameter h > 0, we are given two finite-dimensional spaces:

## chapter-04-section-04-pc00015 | equation | low | PDF 330

[[FORMULA:f-p0330-05438]]

## chapter-04-section-04-pc00016 | ordinary-paragraph | high | PDF 330,331

and we assume that Q, contains the constant functions. Then we define: As usual, Q is a bounded, connected, open subset of R¥ witha Lipschitz-continuous boundary I.

## chapter-04-section-04-pc00017 | ordinary-paragraph | high | PDF 331

With the above spaces, the homogeneous Navier-Stokes Problem: Given f in H~'(Q)%, find (u, p) in H{(Q)* x L2(Q) satisfying:

## chapter-04-section-04-pc00018 | equation | low | PDF 331

[[FORMULA:f-p0331-05439]]

## chapter-04-section-04-pc00019 | equation | low | PDF 331

[[FORMULA:f-p0331-05440]]

## chapter-04-section-04-pc00020 | equation | low | PDF 331

[[FORMULA:f-p0331-05441]]

## chapter-04-section-04-pc00021 | ordinary-paragraph | high | PDF 331

is discretized by the following Problem (Q,)

## chapter-04-section-04-pc00022 | ordinary-paragraph | high | PDF 331

Find (u,, Py) € Wo, x M,, solution of (4.2) A(U,; Up, V,) — (Py, divv,) = <f,v,> Vv,e Won,

## chapter-04-section-04-pc00023 | equation | low | PDF 331

[[FORMULA:f-p0331-05443]]

## chapter-04-section-04-pc00024 | ordinary-paragraph | high | PDF 331

Recall the three hypotheses introduced in Section II.1.3 and related to the approximation of the Stokes system: Hypothesis H1 (Approximation property of Wo,). There exist an operator r,€ L(LH?(Q) 9 H}5(Q)]*; Wo,) and an integer | such that: (4.3) WV ito = Chi aaag VveH=(Q)", lamat Hypothesis H2 (Approximation property of Q,). There exists an operator s),€ L(L?(Q); O,) such that: (4.4) ld — Sn4lloa< Ch" ldIlma VaeH™Q), O<me<l. Hypothesis H3 (Uniform inf-sup condition). For each q,¢M,, there exists a v,€ Wo, such that: (4.5) (41, div v,) = Ild alld,a IVali,@ < Clldallo,a, with a constant C > 0 independent of h, q,, and Vv).

## chapter-04-section-04-pc00025 | ordinary-paragraph | high | PDF 331

In view of these assumptions, let us apply the material of Section 3.3.

## chapter-04-section-04-pc00026 | theorem | high | PDF 331

Theorem 4.1. Suppose N < 3 and assume that the hypotheses H1, H2 and H3 hold.

## chapter-04-section-04-pc00027 | ordinary-paragraph | high | PDF 331

Let {(A,(u(A), Ap(A)));4 = 1/veA } be a branch of nonsingular solutions of the Navier-Stokes Problem (4.1). Then there exists a neighborhood © of the origin in H3(Q)% x L2(Q) and for h < ho sufficiently small a unique 6 branch (A, (u,(A), Ap,(A))2.)€; A } of nonsingular solutions of Problem (4.2) such that:

## chapter-04-section-04-pc00028 | ordinary-paragraph | high | PDF 331

(u,(A), Apa(A)) €(u(A), Ap(A)) +O WAe A. Moreover, we have the convergence property: (4.6) lim sup {|u,(A) — u(A)|1,0 + IlPa(A) — PA)Ilo,a} = 9.

## chapter-04-section-04-pc00029 | equation | low | PDF 331

[[FORMULA:f-p0331-05455]]

## chapter-04-section-04-pc00030 | ordinary-paragraph | high | PDF 332

(4.7) Ju,(A) — uAli.o + IPa(A) — PA)ll o.@ < Kh”

## chapter-04-section-04-pc00031 | proof | high | PDF 332

Proof. The idea is to apply Theorem 3.3 with the following choice:

## chapter-04-section-04-pc00032 | equation | low | PDF 332

[[FORMULA:f-p0332-05457]]

## chapter-04-section-04-pc00033 | ordinary-paragraph | high | PDF 332

The operator Te Y(Y; X) is the Stokes operator: for f given in Y, Tf = (v,q)€X is the solution of the Stokes problem:

## chapter-04-section-04-pc00034 | equation | low | PDF 332

[[FORMULA:f-p0332-05459]]

## chapter-04-section-04-pc00035 | ordinary-paragraph | high | PDF 332

in Q, (4.8) divv = 0

## chapter-04-section-04-pc00036 | equation | low | PDF 332

[[FORMULA:f-p0332-05461]]

## chapter-04-section-04-pc00037 | ordinary-paragraph | high | PDF 332

For a fixed f, the @°-mapping G: R, x X — Y is defined like in (3.8): N

## chapter-04-section-04-pc00038 | equation | low | PDF 332

[[FORMULA:f-p0332-05463]]

## chapter-04-section-04-pc00039 | ordinary-paragraph | high | PDF 332

Sl and N

## chapter-04-section-04-pc00040 | equation | low | PDF 332

[[FORMULA:f-p0332-05464]]

## chapter-04-section-04-pc00041 | ordinary-paragraph | high | PDF 332

Let us determine the space Z. In view of Theorem 1.1.3, we know that HQ) ce £(Q) story 3 and the imbedding of H}(Q) into L?(Q) is compact for p < 6. Next, applying

## chapter-04-section-04-pc00042 | corollary | high | PDF 332

Corollary I.1.1 observe that for v and w in Hj(Q)%, we have

## chapter-04-section-04-pc00043 | ordinary-paragraph | high | PDF 332

N » (vj0w/dx,; + w,0v/0x,)€ L*?(Q)*. Finally, applying again Theorem I.1.3 we find that L7(Q) is compactly imbedded in H-‘(Q) whenever q > 6/5. It stems from these remarks that we can choose

## chapter-04-section-04-pc00044 | equation | low | PDF 332

[[FORMULA:f-p0332-05467]]

## chapter-04-section-04-pc00045 | ordinary-paragraph | high | PDF 332

and (3.36) holds. Now, let X, = Wo, x M, and let T,¢ 4(Y; X,,) be the approximate Stokes operator defined by:

## chapter-04-section-04-pc00046 | equation | low | PDF 332

[[FORMULA:f-p0332-05470]]

## chapter-04-section-04-pc00047 | equation | low | PDF 332

[[FORMULA:f-p0332-05471]]

## chapter-04-section-04-pc00048 | equation | low | PDF 332

[[FORMULA:f-p0332-05472]]

## chapter-04-section-04-pc00049 | ordinary-paragraph | high | PDF 332,333

It follows from Theorem II.1.8 that, owing to the hypotheses H1, H2 and H3 (4.9) Bb Ftyeh Il—d Glnlo, a} = 9, ise,

## chapter-04-section-04-pc00050 | equation | low | PDF 333

[[FORMULA:f-p0333-05474]]

## chapter-04-section-04-pc00051 | equation | low | PDF 333

[[FORMULA:f-p0333-05475]]

## chapter-04-section-04-pc00052 | ordinary-paragraph | high | PDF 333

Furthermore, when (v,q) belongs to H™*1(Q)" x H™(Q) for some integer m in [1,1], this same theorem asserts that: (4.10) lv, — Vii.a + Ilda — Gllo.q < Ch™ (Vil ma1.a + 4 Ilma) 1.€. I(T, — T)flly< Ch™| |T E |) msi (ayy x HQ): As mentioned at the end of Remark 3.4, the compactness of the imbedding of Z into Y together with (4.9) imply that

## chapter-04-section-04-pc00053 | equation | low | PDF 333

[[FORMULA:f-p0333-05479]]

## chapter-04-section-04-pc00054 | equation | low | PDF 333

[[FORMULA:f-p0333-05480]]

## chapter-04-section-04-pc00055 | ordinary-paragraph | high | PDF 333

Thus (3.37) and (3.38) hold.

## chapter-04-section-04-pc00056 | ordinary-paragraph | high | PDF 333

Finally, since 2

## chapter-04-section-04-pc00057 | equation | low | PDF 333

[[FORMULA:f-p0333-05482]]

## chapter-04-section-04-pc00058 | ordinary-paragraph | high | PDF 333

we can express Problem (4.2) as follows:

## chapter-04-section-04-pc00059 | ordinary-paragraph | high | PDF 333

N

## chapter-04-section-04-pc00060 | equation | low | PDF 333

[[FORMULA:f-p0333-05484]]

## chapter-04-section-04-pc00061 | equation | low | PDF 333

[[FORMULA:f-p0333-05485]]

## chapter-04-section-04-pc00062 | ordinary-paragraph | high | PDF 333

In other words, u, = (u,,(1/v)p,) satisfies:

## chapter-04-section-04-pc00063 | equation | low | PDF 333

[[FORMULA:f-p0333-05487]]

## chapter-04-section-04-pc00064 | ordinary-paragraph | high | PDF 333

ie: F(A, u,) = u, + T,G(A,u,) =O with 2 = 1/\.

## chapter-04-section-04-pc00065 | ordinary-paragraph | high | PDF 333

Consequently, we can apply the conclusion of Theorem 3.3: for h < ho sufficiently small there exists a unique branch of nonsingular solutions of (4.2): {(A, uy(A) = (uy(), Apy(A))); 4€ A}, i.e. u,(A) + T,G(A,u,(4)) =0 Wired, and a real number a > 0, independent of h, such that:

## chapter-04-section-04-pc00066 | equation | low | PDF 333

[[FORMULA:f-p0333-05494]]

## chapter-04-section-04-pc00067 | ordinary-paragraph | high | PDF 333

In addition, according to Remark 3.6, the mapping / > u,(A) is 6” because the mapping G is also @” with bounded derivatives of all order on every bounded subsets of A x X.

## chapter-04-section-04-pc00068 | equation | low | PDF 334

[[FORMULA:f-p0334-05496]]

## chapter-04-section-04-pc00069 | ordinary-paragraph | high | PDF 334

Hence (4.6) follows from (4.9). Furthermore, since

## chapter-04-section-04-pc00070 | equation | low | PDF 334

[[FORMULA:f-p0334-05498]]

## chapter-04-section-04-pc00071 | ordinary-paragraph | high | PDF 334

is the solution of the Stokes system:

## chapter-04-section-04-pc00072 | equation | low | PDF 334

[[FORMULA:f-p0334-05499]]

## chapter-04-section-04-pc00073 | ordinary-paragraph | high | PDF 334

the error estimate (II.1.46) gives:

## chapter-04-section-04-pc00074 | equation | low | PDF 334

[[FORMULA:f-p0334-05500]]

## chapter-04-section-04-pc00075 | ordinary-paragraph | high | PDF 334

Thus (4.7) stems from the continuity of the mapping 4— u(A) from A into He (OV SH (Qy ies] It is also possible to derive an L?-estimate for the velocity. Like in the linear case we must assume that the associated Stokes problem is regular (cf. Definition II.1.1): (4.11) |t he mapping (, 1) > —v4 + grad p is an isomorphism from [H?(Q)"N VLA (OC) Le (@)] onto L2(Qy.

## chapter-04-section-04-pc00076 | theorem | high | PDF 334

Theorem 4.2. We retain the hypotheses of Theorem 4.1 and we assume that (4.11)

## chapter-04-section-04-pc00077 | ordinary-paragraph | high | PDF 334

holds. If the mapping 4 > (u(A), p(A)) is continuous from A into H™*1(Q)% x H™(Q) for some integer m in [1,1], then we have the following L?-estimate for all 4 in A: (4.12) l|u,(4) — u(A) loa < KA™™.

## chapter-04-section-04-pc00078 | proof | high | PDF 334

Proof. Let us apply Theorem 3.5. Since we are only interested in the velocity u,

## chapter-04-section-04-pc00079 | ordinary-paragraph | high | PDF 334

we are going to drop entirely the pressure p. Thus we take

## chapter-04-section-04-pc00080 | equation | low | PDF 334

[[FORMULA:f-p0334-05506]]

## chapter-04-section-04-pc00081 | ordinary-paragraph | high | PDF 334

and for f in Y we define v = Tf by:

## chapter-04-section-04-pc00082 | equation | low | PDF 334

[[FORMULA:f-p0334-05508]]

## chapter-04-section-04-pc00083 | ordinary-paragraph | high | PDF 334

As the mapping G(A, v) depends only on the velocity v (and not on q) we can leave it as such. Thus, u is a solution of the Navier-Stokes system (4.1) if and only if:

## chapter-04-section-04-pc00084 | equation | low | PDF 334

[[FORMULA:f-p0334-05510]]

## chapter-04-section-04-pc00085 | ordinary-paragraph | high | PDF 334

Next, we choose

## chapter-04-section-04-pc00086 | equation | low | PDF 334

[[FORMULA:f-p0334-05511]]

## chapter-04-section-04-pc00087 | ordinary-paragraph | high | PDF 334,335

From Theorem I.1.3, we know that X (resp. W) is compactly imbedded into H (resp. X). Now, take u in W and let us check that D,G(A,u)e¢ Y(H; Y) = L(L?(Q)*; H-*(Q)%). Indeed, if ve L?(Q)* and € P(Q)%, we can write: But <uj;0Vv/0x;,0> = —<v, 0(u;)/0x;>; hence |<ujOv/0x;,0>| < Cy||Vllo,ellyllaalllli.awith a similar bound for <v,éu/dx;,@>. As a consequence, D,G(A,u) can be extended to a continuous linear operator from L?(Q)* into H~'(Q)%, provided u belongs to H*(Q)”. This settles (3.47).

## chapter-04-section-04-pc00088 | ordinary-paragraph | high | PDF 335

As far as (3.48) is concerned, we make use of Remark 3.7 and the compactness of X into H.

## chapter-04-section-04-pc00089 | ordinary-paragraph | high | PDF 335

It remains to verify (3.50): D, F(A, u(4)) is an isomorphism of H. By assumption, we already know that:

## chapter-04-section-04-pc00090 | equation | low | PDF 335

[[FORMULA:f-p0335-05519]]

## chapter-04-section-04-pc00091 | ordinary-paragraph | high | PDF 335

is an isomorphism of X. In addition, we have just seen that TD,G(A,u(A))eé L(L?(Q)’; V) whenever u(/) € H*(Q)". Therefore, the compactness of the imbedding of H!(Q) into L?(Q) implies that TD, G(A, u(A)) is a compact operator from L?(Q)* into itself. Hence we can apply to D,F(A,u(A)) Fredholm’s alternative, namely D, F(A, u(A)) is an isomorphism of H iff the equation (4.13) D,F(,u(A)):v=0 withy in H has only the zero solution. But if v in H satisfies (4.13), then v belongs to V since v = —TD,G(A,u(A)):v. Therefore v = 0 because D, F(A, u(A)) is an isomorphism of X. This proves (3.50).

## chapter-04-section-04-pc00092 | ordinary-paragraph | high | PDF 335

Consequently, we can apply the conclusion of Theorem 3.5: if the mapping A= u(A) is continuous from A into [H}(Q)N H?(Q)}", then for all h sufficiently small, we have:

## chapter-04-section-04-pc00093 | ordinary-paragraph | high | PDF 335

llu,(A) — uA) llo,o < Co{ I(T— T,)G(A,u(4)) loa + lun(A) — u(A)It,o}- Thus, when (u(A), p(A)) belongs to H"**(Q)*" x H™(Q), the bound (II.1.50) gives:

## chapter-04-section-04-pc00094 | equation | low | PDF 335

[[FORMULA:f-p0335-05526]]

## chapter-04-section-04-pc00095 | ordinary-paragraph | high | PDF 335

and (4.12) stems from this estimate and (4.7). []

## chapter-04-section-04-pc00096 | ordinary-paragraph | high | PDF 335

Roughly speaking, Theorems 4.1 and 4.2 can be summarized by saying that all the function spaces introduced in Paragraphs II.2 and II.3 to solve the Stokes equations can be also applied to approximate branches of nonsingular solutions of the Navier-Stokes problem with a similar accuracy. For instance, assume that the two-dimensional Navier-Stokes equations (4.1) have a branch of nonsingular solutions with the regularity: (4.14) A-—(u(A), p(4)) is continuous from A into H-7(O)- x A (Q), Assume that Q is a bounded polygon triangulated by 7, and for each K€ 7, take

## chapter-04-section-04-pc00097 | equation | low | PDF 336

[[FORMULA:f-p0336-05530]]

## chapter-04-section-04-pc00098 | ordinary-paragraph | high | PDF 336

Then, if the triangulation 7, is regular the finite element scheme (4.2) with the spaces:

## chapter-04-section-04-pc00099 | equation | low | PDF 336

[[FORMULA:f-p0336-05532]]

## chapter-04-section-04-pc00100 | equation | low | PDF 336

[[FORMULA:f-p0336-05533]]

## chapter-04-section-04-pc00101 | ordinary-paragraph | high | PDF 336

has a unique branch of solutions {(A, (u,(A), Ap,(4))); 4€ 4} that satisfies the error bound: ju,(A)— u(A)i1,0 + Ip a(A) — PA)Ilo.e < Ch(lu(A)l2.0 + IPAlio) VAed. In addition, when Q is convex we have the L?-estimate:

## chapter-04-section-04-pc00102 | equation | low | PDF 336

[[FORMULA:f-p0336-05535]]

## chapter-04-section-04-pc00103 | ordinary-paragraph | high | PDF 336

Another interesting example is the scheme derived from the controversial Q, — Py element discussed in Sections II.3.3 and II.3.4 in the case of the square (—1,1) x (—1,1). Assume that 7, is a square grid with mesh-size h = 1/(4n) so that the conclusion of Theorem IJ.3.4 be valid. Then take

## chapter-04-section-04-pc00104 | equation | low | PDF 336

[[FORMULA:f-p0336-05537]]

## chapter-04-section-04-pc00105 | ordinary-paragraph | high | PDF 336

with V, and M, defined respectively by (II.3.33) and (I1.3.32). It is established in Sections II.3.3 and II.3.4 that this choice of spaces satisfies the three hypotheses H1, H2 and H3 (cf. (I1.3.39), (I1.3.40) and Theorem II.3.4). Therefore Theorems 4.1 and II.3.5 imply that, under the condition (4.14), the finite element scheme (4.2) has a unique branch of solutions {(A, (u,(A), AB,(A))); Ae A} and Ju,(4) — uA) .o + ||P a(A) — PA)lo,2 S Ch{lu(A)l2,0 + IPAs. a}- Likewise, we derive immediately from Theorem 4.2 and Corollary II.3.2 that:

## chapter-04-section-04-pc00106 | equation | low | PDF 336

[[FORMULA:f-p0336-05540]]

## chapter-04-section-04-pc00107 | remark | high | PDF 336

Remark 4.1. To solve the scheme (4.2) with the Q, — P, element, it is convenient

## chapter-04-section-04-pc00108 | ordinary-paragraph | high | PDF 336

(like in the linear case) to use the basis of V,, described at the end of Section II.3.4.

## chapter-04-section-04-pc00109 | subsection | high | PDF 336

4.2. Formulation in Primitive Variables: the Case of Continuous Pressures

## chapter-04-section-04-pc00110 | ordinary-paragraph | high | PDF 336,337

Going back to Chapter II, we can plainly see that the previous analysis applies readily to the “mini” element discussed in Section II.4.1 as well as the “Hood- Taylor” elements of Section II.4.2. Indeed, all these elements satisfy the hypotheses Hence in the neighborhood of a branch of nonsingular solutions with the regularity (4.14) and if the triangulation 7, is regular, the finite element scheme (4.2) with the spaces

## chapter-04-section-04-pc00111 | equation | low | PDF 337

[[FORMULA:f-p0337-05544]]

## chapter-04-section-04-pc00112 | equation | low | PDF 337

[[FORMULA:f-p0337-05545]]

## chapter-04-section-04-pc00113 | equation | low | PDF 337

[[FORMULA:f-p0337-05546]]

## chapter-04-section-04-pc00114 | ordinary-paragraph | high | PDF 337

has a unique branch of solutions: {(A,(u,(A), 4p,(4)));4¢4 } and there exists a constant C independent of / such that:

## chapter-04-section-04-pc00115 | equation | low | PDF 337

[[FORMULA:f-p0337-05547]]

## chapter-04-section-04-pc00116 | ordinary-paragraph | high | PDF 337

When @ is convex we have the L?-estimate:

## chapter-04-section-04-pc00117 | equation | low | PDF 337

[[FORMULA:f-p0337-05548]]

## chapter-04-section-04-pc00118 | ordinary-paragraph | high | PDF 337

Likewise the error estimates of Theorems II.4.3 and I.4.4 for the two “Hood- Taylor” elements carry over to the scheme (4.2) when 7%, and the branch of nonsingular solutions of the Navier-Stokes equations have the adequate regularity. Unfortunately, the “Glowinski-Pironneau” scheme does not fit so neatly into the preceding framework and has to be analyzed separately. Recall that the velocity and pressure spaces are those of the “Hood-Taylor” scheme:

## chapter-04-section-04-pc00119 | equation | low | PDF 337

[[FORMULA:f-p0337-05550]]

## chapter-04-section-04-pc00120 | equation | low | PDF 337

[[FORMULA:f-p0337-05551]]

## chapter-04-section-04-pc00121 | ordinary-paragraph | high | PDF 337

with the additional space Ap ORs ELKO), for the auxiliary potential. When adapted to the Navier-Stokes problem, the “Glowinski-Pironneau” method, in the version given by Remark II.4.5, reads: Find a triple (U,, Drs Mn) EX, X Qy X DP, Satisfying: 2)

## chapter-04-section-04-pc00122 | equation | low | PDF 337

[[FORMULA:f-p0337-05552]]

## chapter-04-section-04-pc00123 | equation | low | PDF 337

[[FORMULA:f-p0337-05553]]

## chapter-04-section-04-pc00124 | equation | low | PDF 337

[[FORMULA:f-p0337-05554]]

## chapter-04-section-04-pc00125 | ordinary-paragraph | high | PDF 337

ee +(grad p,,v, — gradq,) = (f,v, — gradq,) V(Vn,dn)EX n X D,

## chapter-04-section-04-pc00126 | equation | low | PDF 337

[[FORMULA:f-p0337-05556]]

## chapter-04-section-04-pc00127 | ordinary-paragraph | high | PDF 337

Let us see under what conditions the exact Navier-Stokes problem admits a formulation similar to (4.15). To solve the Stokes problem in Section II.4.3 we took the right-hand side f in L?(Q)? and chose Hj(Q) for space of potentials. Here this is not realistic because the nonlinear term

## chapter-04-section-04-pc00128 | equation | low | PDF 338

[[FORMULA:f-p0338-05558]]

## chapter-04-section-04-pc00129 | ordinary-paragraph | high | PDF 338

which is considered part of the right-hand side, belongs only to L?-*(Q)* for any ¢ > 0 whenever u belongs to H!(Q)? (cf. Corollary I.1.1 with N = 2). This remark suggests to fix a real r in the interval (1,2) and take W'*(Q) for space of potentials with 1/s + 1/r = 1. Then consider the problem: For fe L"(Q)* find a triple (u, p, u) € H3(Q)? x W'"(Q) x Wos(Q) such that 2 v(grad u, grad v) + (3 u,0u/Ox;,v — grad ‘)+ (grad p, v — grad q)

## chapter-04-section-04-pc00130 | equation | low | PDF 338

[[FORMULA:f-p0338-05562]]

## chapter-04-section-04-pc00131 | equation | low | PDF 338

[[FORMULA:f-p0338-05563]]

## chapter-04-section-04-pc00132 | ordinary-paragraph | high | PDF 338

na =(f.v—gradq) V(v,q)e Ho(Q)? x Wor(Q)

## chapter-04-section-04-pc00133 | equation | low | PDF 338

[[FORMULA:f-p0338-05565]]

## chapter-04-section-04-pc00134 | ordinary-paragraph | high | PDF 338

It is a matter of routine to check that this problem is equivalent to the Navier- Stokes problem (4.1) in the following sense: if (u, p) is a solution of (4.1) with p in W*"(Q) then the triple (u, p, uw= 0) is a solution of (4.16). Conversely, each solution of (4.16) is of the form (u, p, u = 0) where the pair (u, p) satisfies (4.1). Obviously, the same conclusion applies to the Stokes problem with righthand side f in L’(Q)?: if the pressure solution p of the Stokes problem belongs to W‘*’(Q) then this problem is equivalent to: Find (u, p, u)H€4 (2 )? x W'"(Q) x WIs(Q) such that

## chapter-04-section-04-pc00135 | equation | low | PDF 338

[[FORMULA:f-p0338-05570]]

## chapter-04-section-04-pc00136 | ordinary-paragraph | high | PDF 338

(4.17) V(v, q)€ H4(Q)? x W}’5(Q),

## chapter-04-section-04-pc00137 | equation | low | PDF 338

[[FORMULA:f-p0338-05572]]

## chapter-04-section-04-pc00138 | ordinary-paragraph | high | PDF 338

Therefore, in order to express the Stokes operator by (4.17) for every right-hand side in L’(Q)? we must assume that the Stokes problem is regular in a more general sense than (4.11): (4.18) i mapping (@, 4) > — 4 + grad is an isomorphism from [W?""(Q)N x [W2"(Q)/R] onto LQ) for all re(1, 2]. “WP

## chapter-04-section-04-pc00139 | remark | high | PDF 338

Remark 4.2. Here the pressure is taken in the quotient space W':"(Q)/R instead

## chapter-04-section-04-pc00140 | ordinary-paragraph | high | PDF 338

of W*"(Q)N Lo(Q) because in the practical computation of (4.15), P;, is fixed by the condition |; p,ds = 0 (cf. Lemma IL4.3). Now, we can put Problem (4.16) into the setting of Section 3.3. We take:

## chapter-04-section-04-pc00141 | equation | low | PDF 338

[[FORMULA:f-p0338-05579]]

## chapter-04-section-04-pc00142 | ordinary-paragraph | high | PDF 339

ReZi)). ft (wp, — 0) “solution of (4:17): The nonlinearity is embodied by the usual mapping G:

## chapter-04-section-04-pc00143 | ordinary-paragraph | high | PDF 339

2

## chapter-04-section-04-pc00144 | equation | low | PDF 339

[[FORMULA:f-p0339-05580]]

## chapter-04-section-04-pc00145 | equation | low | PDF 339

[[FORMULA:f-p0339-05581]]

## chapter-04-section-04-pc00146 | ordinary-paragraph | high | PDF 339

which maps R, x X into L’(Q)*. With these notations, Problem (4.16) takes the standard form:

## chapter-04-section-04-pc00147 | equation | low | PDF 339

[[FORMULA:f-p0339-05583]]

## chapter-04-section-04-pc00148 | ordinary-paragraph | high | PDF 339

with A = 1/v, u = (u, Ap, 0) and F(A, u) =u + TG(A,u).

## chapter-04-section-04-pc00149 | remark | high | PDF 339

Remark 4.3. When the Stokes operator has the regularity (4.18), each solution u

## chapter-04-section-04-pc00150 | ordinary-paragraph | high | PDF 339

of Problem (4.16) with right-hand side f in L’(Q)* has the regularity ue W7""(Q)’, pe W?"(Q). This is valid for all real re(1, 2].

## chapter-04-section-04-pc00151 | remark | high | PDF 339

Remark 4.4. It is important to note that if the Stokes operator has the regularity

## chapter-04-section-04-pc00152 | ordinary-paragraph | high | PDF 339

(4.18) then every branch of nonsingular solutions of Problem (4.1) with righthand side f in L’(Q)? is also a branch of nonsingular solutions of Problem (4.16) and conversely.

## chapter-04-section-04-pc00153 | ordinary-paragraph | high | PDF 339

Next, we set

## chapter-04-section-04-pc00154 | equation | low | PDF 339

[[FORMULA:f-p0339-05589]]

## chapter-04-section-04-pc00155 | ordinary-paragraph | high | PDF 339

and let T,¢ #(Y; W,) be the discrete Stokes operator corresponding to (4.17):

## chapter-04-section-04-pc00156 | equation | low | PDF 339

[[FORMULA:f-p0339-05591]]

## chapter-04-section-04-pc00157 | equation | low | PDF 339

[[FORMULA:f-p0339-05592]]

## chapter-04-section-04-pc00158 | ordinary-paragraph | high | PDF 339

(4.19) V(Vi59,)EX n X D,,

## chapter-04-section-04-pc00159 | equation | low | PDF 339

[[FORMULA:f-p0339-05594]]

## chapter-04-section-04-pc00160 | ordinary-paragraph | high | PDF 339

Therefore, Problem (4.15) has the equivalent formulation:

## chapter-04-section-04-pc00161 | equation | low | PDF 339

[[FORMULA:f-p0339-05596]]

## chapter-04-section-04-pc00162 | ordinary-paragraph | high | PDF 339

with A = 1/v, u,(A) = (u,(A), App (A), Mn(A)) and F(A, u,) = Un + TGA, uy).

## chapter-04-section-04-pc00163 | ordinary-paragraph | high | PDF 339

We are now in a position to apply Theorem 3.3. We take

## chapter-04-section-04-pc00164 | equation | low | PDF 339

[[FORMULA:f-p0339-05598]]

## chapter-04-section-04-pc00165 | ordinary-paragraph | high | PDF 339,340

and (3.36) holds automatically. As far as the approximation properties of the operator 7, are concerned, we can apply the material of Section 11.4.3. In particular, it is established in Theorem II.4.6 that (4.20) |M alt, as< |lu— Urllo, Q> (ple (1 + \/2/B%) inf IP — dallo.a + (1/6*)|u ~ Wsls,a. Gn€ Qn where P, denotes the H'-projection on Q,, L6(Q) defined by (A.25), p (resp. Pp) denotes the representative of p (resp. p,,) in L$(Q) and f* is the constant of the inf-sup condition. Note that (4.20) requires only the mild assumption (II.4.17) and the regularity of the triangulation 7,. Thus (3.37) follows from (4.20) and a standard density argument. Finally, (3.38) is a consequence of (4.20) and the regularity assumption (4.18) (which is valid when Q is convex). More precisely, if (4.18) holds then u and p have the extra regularity: ue w2""(Q)?, pew?"(Q). Then just like in Section III.3.1 we derive: (4.21) inf |u—V4l1,a< C,h** ul ,,0 Vn eXn and if in addition 2 is convex and 7%, is uniformly regular, Lemma III.3.4 establishes that (4.22) IP — PrPllo.g< C,h**|In hl ** |p|, a. Collecting these inequalities we obtain: (4.23) |u—uylie + |Hali.a + IP — Pallo.g <C 3h**|Ihnl? **||fllo,.0 which proves (3.38). Observe also that when Q is convex and 7%, is uniformly regular, (4.19) and

## chapter-04-section-04-pc00166 | theorem | high | PDF 340

Theorem A.2 imply that:

## chapter-04-section-04-pc00167 | ordinary-paragraph | high | PDF 340

(4.24) Hnl1,2,.0 S C4(a) ||div(u —u,)llo,@ Vreal a > 2. Indeed, we can consider that 1, is the H}-projection, B,u, of the solution p of the Dirichlet problem:

## chapter-04-section-04-pc00168 | equation | low | PDF 340

[[FORMULA:f-p0340-05612]]

## chapter-04-section-04-pc00169 | ordinary-paragraph | high | PDF 340

Consequently, the conclusion of Theorem 3.3 is valid; it is summarized in the following theorem.

## chapter-04-section-04-pc00170 | theorem | high | PDF 340

Theorem 4.3, Let Q be a bounded, convex polygon and assume that J, is a uniformly

## chapter-04-section-04-pc00171 | ordinary-paragraph | high | PDF 340

regular triangulation of Q that satisfies (1.4.17). For fe LQ), re(1, 2], let {(A, (u(A), Ap(A), 0); 2 = 1/v€ A}, with p(A) chosen in L2(Q), be a branch of nonsingular solutions of the Navier-Stokes Problem (4.16). Then for h < hg sufficiently small, there exists a unique 6” branch {(A,(u,(A), APp(A), Uy(A))); AE A}, with p,(A) chosen in L2(Q), of solutions of Problem (4.15) such that:

## chapter-04-section-04-pc00172 | equation | low | PDF 341

[[FORMULA:f-p0341-05616]]

## chapter-04-section-04-pc00173 | ordinary-paragraph | high | PDF 341

AeA 1/r + 1/s = 1, with constants independent of h and A. Besides that, if the mapping 4 = (u(A), p(A)) is continuous from A into H™*'(Q)* x H™(Q) for m = 1 or 2, we have the estimate: (4.26) Jun(A) — u(A)li2 + IPA) — PA) Ilo. + Ha(Ali ae < KA™ for all AE A.

## chapter-04-section-04-pc00174 | remark | high | PDF 341

Remark 4.5. It is not yet known whether or not a more accurate L?-estimate can

## chapter-04-section-04-pc00175 | ordinary-paragraph | high | PDF 341

be obtained for u — u, + grad y,, as it is done in Theorem II.4.6 for the Stokes problem. The delicate point is that the proof of Theorem II.4.6 uses explicitly the equality:

## chapter-04-section-04-pc00176 | equation | low | PDF 341

[[FORMULA:f-p0341-05622]]

## chapter-04-section-04-pc00177 | ordinary-paragraph | high | PDF 341

which is valid for every Stokes system but is obviously not true for Navier-Stokes equations.

## chapter-04-section-04-pc00178 | subsection | high | PDF 341

4.3. Mixed Incompressible Methods: the “Stream Function-Vorticity”

## chapter-04-section-04-pc00179 | ordinary-paragraph | high | PDF 341

Formulation In this section, we investigate exclusively the two-dimensional case. (As mentioned at the beginning of this paragraph, the corresponding analysis of mixed incompressible schemes in three dimensions is still an open problem). We propose to extend to the Navier-Stokes equations the mixed formulation introduced in Section III.2.1. To begin with, recall the stream function-vorticity formulation of the Stokes operator. Let us fix a real s > 4 and let r be its dual exponent:

## chapter-04-section-04-pc00180 | equation | low | PDF 341

[[FORMULA:f-p0341-05624]]

## chapter-04-section-04-pc00181 | ordinary-paragraph | high | PDF 341

Define the space of stream functions:

## chapter-04-section-04-pc00182 | equation | low | PDF 341

[[FORMULA:f-p0341-05625]]

## chapter-04-section-04-pc00183 | ordinary-paragraph | high | PDF 341

where as usual Jy, ..., , denote the connected components of the boundary I” with exterior component [, (cf. Figure 2). We know that the operator curl is an isomorphism from

## chapter-04-section-04-pc00184 | equation | low | PDF 341

[[FORMULA:f-p0341-05627]]

## chapter-04-section-04-pc00185 | ordinary-paragraph | high | PDF 341

Pate Mel) onto

## chapter-04-section-04-pc00186 | equation | low | PDF 341

[[FORMULA:f-p0341-05628]]

## chapter-04-section-04-pc00187 | equation | low | PDF 341

[[FORMULA:f-p0341-05629]]

## chapter-04-section-04-pc00188 | ordinary-paragraph | low | PDF 342

pe W1,"(Q) then the Stokes Problem (4.8) is equivalent to: Find y eΦ, and we Wi,(Q) such that: "中A

## chapter-04-section-04-pc00189 | equation | low | PDF 342

[[FORMULA:f-p0342-05631]]

## chapter-04-section-04-pc00190 | equation | low | PDF 342

[[FORMULA:f-p0342-05632]]

## chapter-04-section-04-pc00191 | equation | low | PDF 342

[[FORMULA:f-p0342-05633]]

## chapter-04-section-04-pc00192 | equation | low | PDF 342

[[FORMULA:f-p0342-05634]]

## chapter-04-section-04-pc00193 | ordinary-paragraph | low | PDF 342

Find pe W1,"(Q)N L?(Q) such that: "()sM bA

## chapter-04-section-04-pc00194 | equation | low | PDF 342

[[FORMULA:f-p0342-05635]]

## chapter-04-section-04-pc00195 | equation | low | PDF 342

[[FORMULA:f-p0342-05636]]

## chapter-04-section-04-pc00196 | ordinary-paragraph | high | PDF 342

with u = curl y and o = curlu. Here again, it is necessary to write the Stokes problem in the form (4.28) for every right-hand side fe L'(Q)?. Therefore we assume that (4.18) holds. Then setting

## chapter-04-section-04-pc00197 | equation | low | PDF 342

[[FORMULA:f-p0342-05640]]

## chapter-04-section-04-pc00198 | equation | low | PDF 342

[[FORMULA:f-p0342-05641]]

## chapter-04-section-04-pc00199 | ordinary-paragraph | medium | PDF 342

the Stokes operator T is defined by: Te E(Y; X),

## chapter-04-section-04-pc00200 | equation | low | PDF 342

[[FORMULA:f-p0342-05642]]

## chapter-04-section-04-pc00201 | ordinary-paragraph | high | PDF 342

Next, in view of (2.27) the convection term satisfies the identities:

## chapter-04-section-04-pc00202 | equation | low | PDF 342

[[FORMULA:f-p0342-05644]]

## chapter-04-section-04-pc00203 | equation | low | PDF 342

[[FORMULA:f-p0342-05645]]

## chapter-04-section-04-pc00204 | ordinary-paragraph | low | PDF 342

J 12

## chapter-04-section-04-pc00205 | equation | low | PDF 342

[[FORMULA:f-p0342-05646]]

## chapter-04-section-04-pc00206 | ordinary-paragraph | low | PDF 342

e帕 叫 pe dx, 0x1 0x2 0x2 0x1. Ω

## chapter-04-section-04-pc00207 | equation | low | PDF 342

[[FORMULA:f-p0342-05647]]

## chapter-04-section-04-pc00208 | equation | low | PDF 342

[[FORMULA:f-p0342-05648]]

## chapter-04-section-04-pc00209 | ordinary-paragraph | low | PDF 342

Jo

## chapter-04-section-04-pc00210 | equation | low | PDF 342

[[FORMULA:f-p0342-05649]]

## chapter-04-section-04-pc00211 | ordinary-paragraph | high | PDF 342

+ (1/2)

## chapter-04-section-04-pc00212 | equation | low | PDF 342

[[FORMULA:f-p0342-05650]]

## chapter-04-section-04-pc00213 | ordinary-paragraph | high | PDF 342

where curly = u, w = curlu and Il. Il denotes the Euclidean norm. Hence we introduce the nonlinearity by the mapping

## chapter-04-section-04-pc00214 | equation | low | PDF 342

[[FORMULA:f-p0342-05652]]

## chapter-04-section-04-pc00215 | equation | low | PDF 342

[[FORMULA:f-p0342-05653]]

## chapter-04-section-04-pc00216 | equation | low | PDF 342

[[FORMULA:f-p0342-05654]]

## chapter-04-section-04-pc00217 | ordinary-paragraph | medium | PDF 342

and we agree to include the term (1/2) Ilu |² in the pressure: i.e. we work instead with the kinematic pressure p* = p + (1/2)llull². As s ≥ 4, the terms w grad y and Iul² belong respectively to L4/3(Ω)² and L2(Q). Now consider the following problem for f in L'(Q)2: Find y e Φ, and we W1,r(Q) such that

## chapter-04-section-04-pc00218 | equation | low | PDF 342

[[FORMULA:f-p0342-05657]]

## chapter-04-section-04-pc00219 | ordinary-paragraph | low | PDF 342

VoeΦs,

## chapter-04-section-04-pc00220 | equation | low | PDF 342

[[FORMULA:f-p0342-05658]]

## chapter-04-section-04-pc00221 | ordinary-paragraph | low | PDF 342

(o)MrA

## chapter-04-section-04-pc00222 | equation | low | PDF 342

[[FORMULA:f-p0342-05659]]

## chapter-04-section-04-pc00223 | ordinary-paragraph | low | PDF 343

()s1M =bA  (bpe18muna - pe8 m - J) = (bpe*d pe8) (9ze't) With the above notations this problem reads:

## chapter-04-section-04-pc00224 | equation | low | PDF 343

[[FORMULA:f-p0343-05661]]

## chapter-04-section-04-pc00225 | ordinary-paragraph | high | PDF 343

with Λ = 1/v, u = (curly,w,Ap*)e X, G defined by (4.31) and T defined by (4.28). Again, a routine calculation shows that if (u, p) is a solution of Problem (4.1) with curl u and p in W1.r(Ω), f in L'(Q)² then the triple (curl y,w, p*) with

## chapter-04-section-04-pc00226 | equation | low | PDF 343

[[FORMULA:f-p0343-05666]]

## chapter-04-section-04-pc00227 | equation | low | PDF 343

[[FORMULA:f-p0343-05667]]

## chapter-04-section-04-pc00228 | ordinary-paragraph | high | PDF 343

is a solution of Problem (4.32). Conversely, each solution (curl y, w, p*) of (4.32) is such that w = - 4y and the pair (u, p) defined by (4.33) satisfies (4.1). In addition, when the Stokes operator has the regularity (4.18), each solution u = (curl y,w, p*) of Problem (4.32) with f in L'(Ω)² for some real ye [r,2] has the regularity ↓e W3,*(Ω), we W1,(Ω), p* e W1,*(Ω). Furthermore, just like in

## chapter-04-section-04-pc00229 | remark | high | PDF 343

Remark 4.4, every branch of nonsingular solutions of Problem (4.1) with right-

## chapter-04-section-04-pc00230 | ordinary-paragraph | high | PDF 343

hand side f in L'(Ω)² is also a branch of nonsingular solutions of Problem (4.32) and conversely.

## chapter-04-section-04-pc00231 | ordinary-paragraph | high | PDF 343

As far as the approximation is concerned, we assume that Q is a polygonal domain of R? in order to triangulate it entirely. Then let T, be a family of triangulations of Q and I > 1 a fixed integer. We take:

## chapter-04-section-04-pc00232 | equation | low | PDF 343

[[FORMULA:f-p0343-05675]]

## chapter-04-section-04-pc00233 | equation | low | PDF 343

[[FORMULA:f-p0343-05676]]

## chapter-04-section-04-pc00234 | equation | low | PDF 343

[[FORMULA:f-p0343-05677]]

## chapter-04-section-04-pc00235 | equation | low | PDF 343

[[FORMULA:f-p0343-05678]]

## chapter-04-section-04-pc00236 | equation | low | PDF 343

[[FORMULA:f-p0343-05679]]

## chapter-04-section-04-pc00237 | equation | low | PDF 343

[[FORMULA:f-p0343-05680]]

## chapter-04-section-04-pc00238 | ordinary-paragraph | medium | PDF 343

With these spaces, the Stokes problem is approximated by: Find , in Φ, and w, in O, solution of

## chapter-04-section-04-pc00239 | equation | low | PDF 343

[[FORMULA:f-p0343-05681]]

## chapter-04-section-04-pc00240 | equation | low | PDF 343

[[FORMULA:f-p0343-05682]]

## chapter-04-section-04-pc00241 | equation | low | PDF 343

[[FORMULA:f-p0343-05683]]

## chapter-04-section-04-pc00242 | ordinary-paragraph | high | PDF 343

Find pn in Qh such that

## chapter-04-section-04-pc00243 | equation | low | PDF 343

[[FORMULA:f-p0343-05684]]

## chapter-04-section-04-pc00244 | equation | low | PDF 343

[[FORMULA:f-p0343-05685]]

## chapter-04-section-04-pc00245 | ordinary-paragraph | high | PDF 343

The corresponding operator T,e &(Y; X,) is defined by

## chapter-04-section-04-pc00246 | equation | low | PDF 343

[[FORMULA:f-p0343-05686]]

## chapter-04-section-04-pc00247 | ordinary-paragraph | low | PDF 343,344

Likewise, the Navier-Stokes problem (4.32) is discretized by: VonEΦn,

## chapter-04-section-04-pc00248 | equation | low | PDF 344

[[FORMULA:f-p0344-05688]]

## chapter-04-section-04-pc00249 | equation | low | PDF 344

[[FORMULA:f-p0344-05689]]

## chapter-04-section-04-pc00250 | equation | low | PDF 344

[[FORMULA:f-p0344-05690]]

## chapter-04-section-04-pc00251 | equation | low | PDF 344

[[FORMULA:f-p0344-05691]]

## chapter-04-section-04-pc00252 | ordinary-paragraph | medium | PDF 344

Find p* e Qh such that: (grad p*, grad an) = (f - Wn grad yh - vcurl wh, grad qh)  Van E Qh.

## chapter-04-section-04-pc00253 | equation | low | PDF 344

[[FORMULA:f-p0344-05693]]

## chapter-04-section-04-pc00254 | ordinary-paragraph | high | PDF 344

In other words, this problem can also be written as:

## chapter-04-section-04-pc00255 | equation | low | PDF 344

[[FORMULA:f-p0344-05694]]

## chapter-04-section-04-pc00256 | ordinary-paragraph | high | PDF 344

with X = 1/v, u, = (curl yh, wn, Ap*)e X, G defined by (4.31) and T, by (4.35). Now, let us apply Theorem 3.3 with Z = Y. Recall the approximation properties of the operator Th, derived in Section I11.3.1 (cf. Theorem HH1.3.2). When Q is a convex polygon, the Stokes problem has the regularity (4.18); in other words, if f belongs to L'(Q)² with r ≤ t ≤ 2 the solution of the Stokes problem (curly,w, p) belongs to W2,(Ω) x W1,(Ω) x W1,(Ω) and

## chapter-04-section-04-pc00257 | equation | low | PDF 344

[[FORMULA:f-p0344-05699]]

## chapter-04-section-04-pc00258 | ordinary-paragraph | low | PDF 344

Hence, if J, is a uniformly regular family of triangulations of Ω, we have the following estimates for the solution (curl h, Wn, Ph) of Problem (4.35): | -- Wnl1,s,2 + Ilw - Wnllo,2 + Ilp - Pnllo,2 ≤ C2h l/fllo,t,, with r ≤ t < 2, 1/y + 1/t = 1, α = 1/y when l = 1 and α = 2/y when I > 2. This settles (3.37) and (3.38). Therefore the conclusion of Theorem 3.3 holds and combined with Theorem IH1.3.1, it gives the next result.

## chapter-04-section-04-pc00259 | theorem | high | PDF 344

Theorem 4.4. 1°) Let Ω be a bounded, convex polygon and let J, be a uniformly

## chapter-04-section-04-pc00260 | ordinary-paragraph | low | PDF 344

regular family of triangulations of Q. For fe L'(Q)², te [r,2), let {(A, (curl Φ(l), w(l), Ap*(a)); X = 1/ve A} be a branch of nonsingular solutions of the Navier- Stokes Problem (4.32). Then for h ≤ ho small enough there exists a unique C∞ branch {(,(curl,(2), wn(a), Ap*(2);  = 1/ve A} of solutions of Problem (4.36) that satisfies: sup {ln(2) - y(2)l1,s, + Ilwn(2) - w(2)llo,o + Il p*(l) - p*(2)lo.s} neA

## chapter-04-section-04-pc00261 | equation | low | PDF 344

[[FORMULA:f-p0344-05709]]

## chapter-04-section-04-pc00262 | equation | low | PDF 344

[[FORMULA:f-p0344-05710]]

## chapter-04-section-04-pc00263 | equation | low | PDF 344

[[FORMULA:f-p0344-05711]]

## chapter-04-section-04-pc00264 | equation | low | PDF 344

[[FORMULA:f-p0344-05712]]

## chapter-04-section-04-pc00265 | ordinary-paragraph | high | PDF 344

1/t + 1/y = 1 and the constant C is independent of h or Λ. This bound is still valid when t = 2 and either I ≥ 2 or ↓ belongs also to W2. ∞(Q). When I = 1 and t = 2, the left-hand side of (4.37) is bounded by

## chapter-04-section-04-pc00266 | equation | low | PDF 344

[[FORMULA:f-p0344-05716]]

## chapter-04-section-04-pc00267 | ordinary-paragraph | high | PDF 345

have the error estimate for all A in A: (4.38) WA) — WAlis.o + llon(A) — ©A)|lo.0 + PEA) — P*(A)llo,@ < Kh”. Like in the linear case, it is possible to sharpen the above estimate for Wy, — w in the Hj norm. However, the argument of Theorem 3.5 does not seem to apply here because it would have to bear on both w and w whereas the estimate on w is unlikely to be improved. Let us introduce instead a more direct duality argument. Since we are not concerned by the pressure, we take

## chapter-04-section-04-pc00268 | equation | low | PDF 345

[[FORMULA:f-p0345-05718]]

## chapter-04-section-04-pc00269 | ordinary-paragraph | high | PDF 345

and we suppose that

## chapter-04-section-04-pc00270 | equation | low | PDF 345

[[FORMULA:f-p0345-05719]]

## chapter-04-section-04-pc00271 | ordinary-paragraph | high | PDF 345

is a branch of nonsingular solutions of Problem (4.32a) with fe L?(Q)?. Again we assume that (4.18) holds so that u(A) belongs to H*(Q) x H1(Q). To simplify we denote

## chapter-04-section-04-pc00272 | equation | low | PDF 345

[[FORMULA:f-p0345-05721]]

## chapter-04-section-04-pc00273 | ordinary-paragraph | high | PDF 345

Recall that

## chapter-04-section-04-pc00274 | equation | low | PDF 345

[[FORMULA:f-p0345-05722]]

## chapter-04-section-04-pc00275 | ordinary-paragraph | high | PDF 345

Then we introduce the operator D* « Y(H; X’) defined by: (4.39) <D*z,v> =(curly,D-v) Vz = (curly, eH. To relate D and D* recall that the space V associated with X is

## chapter-04-section-04-pc00276 | equation | low | PDF 345

[[FORMULA:f-p0345-05724]]

## chapter-04-section-04-pc00277 | ordinary-paragraph | high | PDF 345

where b(v, w) = (curl ¢, curl ) — (6, 1). Recall also that V is a Hilbert space for the scalar product

## chapter-04-section-04-pc00278 | equation | low | PDF 345

[[FORMULA:f-p0345-05726]]

## chapter-04-section-04-pc00279 | ordinary-paragraph | high | PDF 345

and that the definition of the Stokes operator can be extended to

## chapter-04-section-04-pc00280 | equation | low | PDF 345

[[FORMULA:f-p0345-05727]]

## chapter-04-section-04-pc00281 | ordinary-paragraph | high | PDF 345

Thus it follows readily from (4.39) that

## chapter-04-section-04-pc00282 | equation | low | PDF 345

[[FORMULA:f-p0345-05729]]

## chapter-04-section-04-pc00283 | ordinary-paragraph | high | PDF 345

In other words, TD* is the adjoint of TD in V for the scalar product a(., .). As a consequence, since by assumption J + TD is an isomorphism of V, then I + TD* is also an isomorphism of V.

## chapter-04-section-04-pc00284 | equation | low | PDF 346

[[FORMULA:f-p0346-05730]]

## chapter-04-section-04-pc00285 | equation | low | PDF 346

[[FORMULA:f-p0346-05731]]

## chapter-04-section-04-pc00286 | equation | low | PDF 346

[[FORMULA:f-p0346-05732]]

## chapter-04-section-04-pc00287 | equation | low | PDF 346

[[FORMULA:f-p0346-05733]]

## chapter-04-section-04-pc00288 | ordinary-paragraph | high | PDF 346

i.e.

## chapter-04-section-04-pc00289 | lemma | high | PDF 346

Lemma 4.1. Let Q be a bounded, Lipschitz-continuous domain of R² and suppose

## chapter-04-section-04-pc00290 | ordinary-paragraph | high | PDF 346

the Stokes problem has the regularity (4.18). Then the solution z = (curl x,μ) of Problem (4.40) belongs to H²(Q) x H'(Q2) with

## chapter-04-section-04-pc00291 | equation | low | PDF 346

[[FORMULA:f-p0346-05736]]

## chapter-04-section-04-pc00292 | equation | low | PDF 346

[[FORMULA:f-p0346-05737]]

## chapter-04-section-04-pc00293 | proof | high | PDF 346

Proof. First, it stems from (4.40) that

## chapter-04-section-04-pc00294 | equation | low | PDF 346

[[FORMULA:f-p0346-05739]]

## chapter-04-section-04-pc00295 | equation | low | PDF 346

[[FORMULA:f-p0346-05740]]

## chapter-04-section-04-pc00296 | ordinary-paragraph | high | PDF 346

Next we know from Lemma IIl.2.1 that all functions v = (curl Φ, 0)e V satisfy:

## chapter-04-section-04-pc00297 | equation | low | PDF 346

[[FORMULA:f-p0346-05742]]

## chapter-04-section-04-pc00298 | ordinary-paragraph | low | PDF 346

Therefore A3aA

## chapter-04-section-04-pc00299 | equation | low | PDF 346

[[FORMULA:f-p0346-05743]]

## chapter-04-section-04-pc00300 | equation | low | PDF 346

[[FORMULA:f-p0346-05744]]

## chapter-04-section-04-pc00301 | ordinary-paragraph | high | PDF 346

Thus D* z can be written in the form

## chapter-04-section-04-pc00302 | equation | low | PDF 346

[[FORMULA:f-p0346-05745]]

## chapter-04-section-04-pc00303 | equation | low | PDF 346

[[FORMULA:f-p0346-05746]]

## chapter-04-section-04-pc00304 | ordinary-paragraph | medium | PDF 346

where, in view of the regularity of u(2) and Sobolev's Imbedding Theorem I.1.3, le L²(Ω)² with

## chapter-04-section-04-pc00305 | equation | low | PDF 346

[[FORMULA:f-p0346-05747]]

## chapter-04-section-04-pc00306 | equation | low | PDF 346

[[FORMULA:f-p0346-05748]]

## chapter-04-section-04-pc00307 | ordinary-paragraph | high | PDF 346

since ze V and satisfies (4.42). Then (4.41) follows from this last inequality, the regularity assumption (4.18) and the fact that z can also be expressed as z = T(g - D* z). 口

## chapter-04-section-04-pc00308 | theorem | high | PDF 346

Theorem 4.5. Let Q and J, be like in Theorem 4.4 and suppose that the Navier-

## chapter-04-section-04-pc00309 | ordinary-paragraph | medium | PDF 346

Stokes Problem (4.42) has a branch of nonsingular solutions such that the mapping → y(2) is continuous from A into Hi+1(Q) when l ≥ 2 or H?(Q) when l = 1. Then we have the following estimate for all X in A:

## chapter-04-section-04-pc00310 | equation | low | PDF 346

[[FORMULA:f-p0346-05753]]

## chapter-04-section-04-pc00311 | equation | low | PDF 346

[[FORMULA:f-p0346-05754]]

## chapter-04-section-04-pc00312 | equation | low | PDF 346

[[FORMULA:f-p0346-05755]]

## chapter-04-section-04-pc00313 | equation | low | PDF 346

[[FORMULA:f-p0346-05756]]

## chapter-04-section-04-pc00314 | ordinary-paragraph | high | PDF 346,347

with constants independent of h and X. sponding solution of the linearized problem (4.40):

## chapter-04-section-04-pc00315 | equation | low | PDF 347

[[FORMULA:f-p0347-05758]]

## chapter-04-section-04-pc00316 | ordinary-paragraph | medium | PDF 347

In particular (dropping for the moment the parameter A): (4.44) (g, curl(y - Vn)) = a(z,u - un) + (curl x, D·(u -- un)) + b(u - uh, v). But we infer from (4.32a) and (4.36a) that u - u, satisfies:

## chapter-04-section-04-pc00317 | equation | low | PDF 347

[[FORMULA:f-p0347-05760]]

## chapter-04-section-04-pc00318 | equation | low | PDF 347

[[FORMULA:f-p0347-05761]]

## chapter-04-section-04-pc00319 | ordinary-paragraph | medium | PDF 347

for every Zh = (curl Xh, vh)e Vh with

## chapter-04-section-04-pc00320 | equation | low | PDF 347

[[FORMULA:f-p0347-05763]]

## chapter-04-section-04-pc00321 | ordinary-paragraph | high | PDF 347

Therefore, combining (4.44) and (4.45) and using the fact that u and z belong to V and u, and z, belong to V, we obtain:

## chapter-04-section-04-pc00322 | equation | low | PDF 347

[[FORMULA:f-p0347-05765]]

## chapter-04-section-04-pc00323 | ordinary-paragraph | low | PDF 347

+b(u—un,v-On)+b(z-—Zh(-μn)

## chapter-04-section-04-pc00324 | equation | low | PDF 347

[[FORMULA:f-p0347-05766]]

## chapter-04-section-04-pc00325 | ordinary-paragraph | low | PDF 347

VZh∈ Vh,  Vμn, On∈Oh. Let us choose O, = P,v and μ, = Phw; formula (A.25) gives for all Φh, one Φh: (a"d -a “μ - m) - (a"d - a)μuno( - p)μn) =(θ - a“n - n)q ("d - m - a) - ((od - m)[μn(g - x)μn) = (μn - m4z - z)g On the other hand, Taylor's formula (3.52) yields here:

## chapter-04-section-04-pc00326 | ordinary-paragraph | low | PDF 347

("n - n)·Da(/1)- = (n - n).(n)"a -(μn) - (n“)

## chapter-04-section-04-pc00327 | equation | low | PDF 347

[[FORMULA:f-p0347-05772]]

## chapter-04-section-04-pc00328 | ordinary-paragraph | medium | PDF 347

Hence for all z, e Vh, Φ, and S, e Φh, we have:

## chapter-04-section-04-pc00329 | ordinary-paragraph | medium | PDF 347

(g,curl(y -h)) =a(z - Zh,u - un) + A(curl(x - Xh),wgrad(y - Wh))

## chapter-04-section-04-pc00330 | equation | low | PDF 347

[[FORMULA:f-p0347-05774]]

## chapter-04-section-04-pc00331 | equation | low | PDF 347

[[FORMULA:f-p0347-05775]]

## chapter-04-section-04-pc00332 | equation | low | PDF 347

[[FORMULA:f-p0347-05776]]

## chapter-04-section-04-pc00333 | ordinary-paragraph | low | PDF 347,348

(4'd - A"∞ - ∞) - ((ad - 4)n( - p)μn) + (d - m" - 4) - ((o"d - m)μn("g - x)μn) + from which we readily infer that + Alxnlia.al¥ — Walt,a.a + lly — Prvllo,a) + Alul|W — Wilr,a.alx — Xnli,4,0 (4.47) + |v — Pyvlya— lbr¥lt ,o + 1X — Oli, 010 — Peli. o + |z — 2,|||0 — P,ollo,o VznEV, Vn One D- Finally, recall that (cf. Lemma III.3.3 and Remark III.3.2): eee ie)

## chapter-04-section-04-pc00334 | equation | low | PDF 348

[[FORMULA:f-p0348-05778]]

## chapter-04-section-04-pc00335 | ordinary-paragraph | high | PDF 348

ZnhEVy, on the other hand,

## chapter-04-section-04-pc00336 | equation | low | PDF 348

[[FORMULA:f-p0348-05779]]

## chapter-04-section-04-pc00337 | ordinary-paragraph | high | PDF 348

one Py, and likewise:

## chapter-04-section-04-pc00338 | equation | low | PDF 348

[[FORMULA:f-p0348-05780]]

## chapter-04-section-04-pc00339 | ordinary-paragraph | high | PDF 348

ne Py,

## chapter-04-section-04-pc00340 | equation | low | PDF 348

[[FORMULA:f-p0348-05781]]

## chapter-04-section-04-pc00341 | ordinary-paragraph | high | PDF 348

with B = 1 when / = 1 and B =! — 1 when! > 2. By substituting these bounds into (4.47) and applying Theorem 4.4 and Lemma 4.1 we easily derive (4.43). 1

## chapter-04-section-04-pc00342 | subsection | high | PDF 348

4.4. Remarks on the “Stream Function-Gradient of Velocity Tensor” Scheme

## chapter-04-section-04-pc00343 | ordinary-paragraph | high | PDF 348

With minor modifications, the approach of Section 4.3 can be applied to the “stream function-gradient of velocity tensor” method for the Navier-Stokes equations, at least when Q2 is a plane, convex polygon. Going back to Paragraph 4, Chapter III, recall the bilinear forms:

## chapter-04-section-04-pc00344 | ordinary-paragraph | high | PDF 348

a,(o, T) — \0 ;;7;; dX, Q

## chapter-04-section-04-pc00345 | equation | low | PDF 348

[[FORMULA:f-p0348-05784]]

## chapter-04-section-04-pc00346 | ordinary-paragraph | high | PDF 348

KeTy K qT, and the spaces

## chapter-04-section-04-pc00347 | equation | low | PDF 348

[[FORMULA:f-p0348-05785]]

## chapter-04-section-04-pc00348 | ordinary-paragraph | high | PDF 348

M,(t) is continuous on each segment of J;,},

## chapter-04-section-04-pc00349 | equation | low | PDF 349

[[FORMULA:f-p0349-05786]]

## chapter-04-section-04-pc00350 | equation | low | PDF 349

[[FORMULA:f-p0349-05787]]

## chapter-04-section-04-pc00351 | equation | low | PDF 349

[[FORMULA:f-p0349-05788]]

## chapter-04-section-04-pc00352 | ordinary-paragraph | medium | PDF 349

Setting

## chapter-04-section-04-pc00353 | equation | low | PDF 349

[[FORMULA:f-p0349-05789]]

## chapter-04-section-04-pc00354 | equation | low | PDF 349

[[FORMULA:f-p0349-05790]]

## chapter-04-section-04-pc00355 | ordinary-paragraph | medium | PDF 349

we have

## chapter-04-section-04-pc00356 | ordinary-paragraph | medium | PDF 349

Te E(Y; X) and since the Stokes problem is regular we also have

## chapter-04-section-04-pc00357 | ordinary-paragraph | low | PDF 349

Te &(Y; W1,r(Q)4 x W3.r(Q). In view of (4.31) we introduce the nonlinear convection term by:

## chapter-04-section-04-pc00358 | equation | low | PDF 349

[[FORMULA:f-p0349-05792]]

## chapter-04-section-04-pc00359 | ordinary-paragraph | medium | PDF 349

which is a C∞-mapping from A x X into L'(Q)2. With these notations, the Navier-Stokes equations take the standard form:

## chapter-04-section-04-pc00360 | equation | low | PDF 349

[[FORMULA:f-p0349-05793]]

## chapter-04-section-04-pc00361 | equation | low | PDF 349

[[FORMULA:f-p0349-05794]]

## chapter-04-section-04-pc00362 | ordinary-paragraph | low | PDF 349

O IeA. As far as the approximation is concerned, we take

## chapter-04-section-04-pc00363 | equation | low | PDF 349

[[FORMULA:f-p0349-05795]]

## chapter-04-section-04-pc00364 | ordinary-paragraph | medium | PDF 349

where

## chapter-04-section-04-pc00365 | equation | low | PDF 349

[[FORMULA:f-p0349-05796]]

## chapter-04-section-04-pc00366 | equation | low | PDF 349

[[FORMULA:f-p0349-05797]]

## chapter-04-section-04-pc00367 | ordinary-paragraph | medium | PDF 349

for some integer I ≥ 1. The Stokes operator is discretized by

## chapter-04-section-04-pc00368 | equation | low | PDF 349

[[FORMULA:f-p0349-05799]]

## chapter-04-section-04-pc00369 | equation | low | PDF 349

[[FORMULA:f-p0349-05800]]

## chapter-04-section-04-pc00370 | equation | low | PDF 349

[[FORMULA:f-p0349-05801]]

## chapter-04-section-04-pc00371 | equation | low | PDF 349

[[FORMULA:f-p0349-05802]]

## chapter-04-section-04-pc00372 | ordinary-paragraph | medium | PDF 349

and the Navier-Stokes equations are approximated by:

## chapter-04-section-04-pc00373 | equation | low | PDF 349

[[FORMULA:f-p0349-05803]]

## chapter-04-section-04-pc00374 | equation | low | PDF 349

[[FORMULA:f-p0349-05804]]

## chapter-04-section-04-pc00375 | ordinary-paragraph | medium | PDF 349

The results of Section IHl.4.3 give the following estimate for T -- T:

## chapter-04-section-04-pc00376 | equation | low | PDF 349

[[FORMULA:f-p0349-05805]]
