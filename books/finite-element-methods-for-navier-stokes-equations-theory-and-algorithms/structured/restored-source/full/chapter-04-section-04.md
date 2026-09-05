# Restored-source review candidate: chapter-04-section-04



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 330 / printed 316



[p0330-b0004 | ordinary-paragraph | high] FuFa(A, Gn(A)) (On — Wh) — Fal, Un) + Fi(A, Wa)l x

[p0330-b0005 | equation | low] < CAL]i,( o6 | 4,(A) Ix) ln — Wall x

[p0330-b0006 | ordinary-paragraph | high] VAEA, Vv,, w,€ S(t, (A); 0) 9 V,.

[p0330-b0007 | ordinary-paragraph | high] Let

[p0330-b0008 | equation | low] K = sup sup ||@,(A)|lx-

[p0330-b0009 | equation | low] h<h, AeA

[p0330-b0010 | ordinary-paragraph | high] The monotonicity of L,, implies that

[p0330-b0011 | equation | low] Li(% || Gn(A) lx) < Li (@ K).

[p0330-b0012 | ordinary-paragraph | high] By assumption, the mapping py — L,(u;K) is monotonically increasing with

[p0330-b0013 | ordinary-paragraph | high] respect to h and pw and continuous at py = 0. In addition, by virtue of (3.65), it

[p0330-b0014 | ordinary-paragraph | high] satisfies the condition (3.57).

[p0330-b0015 | ordinary-paragraph | high] As a consequence, we can apply the conclusion of Theorem 3.7. It yields (3.66);

[p0330-b0016 | ordinary-paragraph | high] then (3.67) stems from (3.30’) with v, = a,(A), (3.68) and (3.59). ‘|

[p0330-b0017 | remark | high] Remark 3.9. The space V, which enters only in the assumption (3.61), plays a

[p0330-b0018 | ordinary-paragraph | high] minor part in this proof. It is useful when the restriction operator 2, requires

[p0330-b0019 | ordinary-paragraph | high] more regularity than the space X can provide.

[p0330-b0020 | section | high] §4. Numerical Analysis of Centered Finite Element Schemes

[p0330-b0021 | ordinary-paragraph | high] In this paragraph, we propose to apply to the homogeneous Navier-Stokes

[p0330-b0022 | ordinary-paragraph | high] equations most of the finite element methods developed in Chapters II and III

[p0330-b0023 | ordinary-paragraph | high] to solve the Stokes problem. The reader will find that in nearly every case, the

[p0330-b0024 | ordinary-paragraph | high] error analysis carries over successfully to Navier-Stokes equations. One of the

[p0330-b0025 | ordinary-paragraph | high] few exceptions is the three-dimensional mixed method elaborated in Paragraph

[p0330-b0026 | ordinary-paragraph | high] IfI.5. This method can be tried to solve the Navier-Stokes system but at the

[p0330-b0027 | ordinary-paragraph | high] present stage, its numerical analysis is still an open problem.

[p0330-b0028 | subsection | high] 4.1. Formulation in Primitive Variables: Methods Using Discontinuous

[p0330-b0029 | ordinary-paragraph | high] Pressures

[p0330-b0030 | ordinary-paragraph | high] The situation is that of Section II.1.3. For each value of the parameter h > 0, we

[p0330-b0031 | ordinary-paragraph | high] are given two finite-dimensional spaces:

[p0330-b0032 | equation | low] W,.< H*(Q)*, Q, < L?(Q)

[p0330-b0033 | ordinary-paragraph | high] and we assume that Q, contains the constant functions. Then we define:

## PDF 331 / printed 317



[p0331-b0003 | ordinary-paragraph | high] As usual, Q is a bounded, connected, open subset of R¥ witha Lipschitz-continuous

[p0331-b0004 | ordinary-paragraph | high] boundary I.

[p0331-b0005 | ordinary-paragraph | high] With the above spaces, the homogeneous Navier-Stokes Problem:

[p0331-b0006 | ordinary-paragraph | high] Given f in H~'(Q)%, find (u, p) in H{(Q)* x L2(Q) satisfying:

[p0331-b0007 | equation | low] a(u; u,v) — (p,divv) = <f,v) = VwHde (Q ),

[p0331-b0008 | equation | low] (4.1)

[p0331-b0009 | equation | low] divu=0 inQ

[p0331-b0010 | ordinary-paragraph | high] is discretized by the following Problem (Q,)

[p0331-b0011 | ordinary-paragraph | high] Find (u,, Py) € Wo, x M,, solution of

[p0331-b0012 | ordinary-paragraph | high] (4.2) A(U,; Up, V,) — (Py, divv,) = <f,v,> Vv,e Won,

[p0331-b0013 | equation | low] (q,,divu,)=90 Yq,eM,,.

[p0331-b0014 | ordinary-paragraph | high] Recall the three hypotheses introduced in Section II.1.3 and related to the

[p0331-b0015 | ordinary-paragraph | high] approximation of the Stokes system:

[p0331-b0016 | ordinary-paragraph | high] Hypothesis H1 (Approximation property of Wo,). There exist an operator r,€

[p0331-b0017 | ordinary-paragraph | high] L(LH?(Q) 9 H}5(Q)]*; Wo,) and an integer | such that:

[p0331-b0018 | ordinary-paragraph | high] (4.3) WV ito = Chi aaag VveH=(Q)", lamat

[p0331-b0019 | ordinary-paragraph | high] Hypothesis H2 (Approximation property of Q,). There exists an operator s),€

[p0331-b0020 | ordinary-paragraph | high] L(L?(Q); O,) such that:

[p0331-b0021 | ordinary-paragraph | high] (4.4) ld — Sn4lloa< Ch" ldIlma VaeH™Q), O<me<l.

[p0331-b0022 | ordinary-paragraph | high] Hypothesis H3 (Uniform inf-sup condition). For each q,¢M,, there exists a v,€

[p0331-b0023 | ordinary-paragraph | high] Wo, such that:

[p0331-b0024 | ordinary-paragraph | high] (4.5) (41, div v,) = Ild alld,a IVali,@ < Clldallo,a,

[p0331-b0025 | ordinary-paragraph | high] with a constant C > 0 independent of h, q,, and Vv).

[p0331-b0026 | ordinary-paragraph | high] In view of these assumptions, let us apply the material of Section 3.3.

[p0331-b0027 | theorem | high] Theorem 4.1. Suppose N < 3 and assume that the hypotheses H1, H2 and H3 hold.

[p0331-b0028 | ordinary-paragraph | high] Let {(A,(u(A), Ap(A)));4 = 1/veA } be a branch of nonsingular solutions of the

[p0331-b0029 | ordinary-paragraph | high] Navier-Stokes Problem (4.1). Then there exists a neighborhood © of the origin in

[p0331-b0030 | ordinary-paragraph | high] H3(Q)% x L2(Q) and for h < ho sufficiently small a unique 6 branch (A, (u,(A),

[p0331-b0031 | ordinary-paragraph | high] Ap,(A))2.)€; A } of nonsingular solutions of Problem (4.2) such that:

[p0331-b0032 | ordinary-paragraph | high] (u,(A), Apa(A)) €(u(A), Ap(A)) +O WAe A.

[p0331-b0033 | ordinary-paragraph | high] Moreover, we have the convergence property:

[p0331-b0034 | ordinary-paragraph | high] (4.6) lim sup {|u,(A) — u(A)|1,0 + IlPa(A) — PA)Ilo,a} = 9.

[p0331-b0035 | equation | low] h>0 AeA

## PDF 332 / printed 318



[p0332-b0004 | ordinary-paragraph | high] (4.7) Ju,(A) — uAli.o + IPa(A) — PA)ll o.@ < Kh”

[p0332-b0005 | proof | high] Proof. The idea is to apply Theorem 3.3 with the following choice:

[p0332-b0006 | equation | low] ees (OQ) oo (Q), k=

[p0332-b0007 | ordinary-paragraph | high] The operator Te Y(Y; X) is the Stokes operator:

[p0332-b0008 | ordinary-paragraph | high] for f given in Y, Tf = (v,q)€X is the solution of the Stokes problem:

[p0332-b0009 | equation | low] —Av+ gradg =f

[p0332-b0010 | ordinary-paragraph | high] in Q,

[p0332-b0011 | ordinary-paragraph | high] (4.8) divv = 0

[p0332-b0012 | equation | low] v=0 onl.

[p0332-b0013 | ordinary-paragraph | high] For a fixed f, the @°-mapping G: R, x X — Y is defined like in (3.8):

[p0332-b0014 | ordinary-paragraph | high] N

[p0332-b0015 | equation | low] G(A, v) = ify , v,0v/Ox; — ‘), v=(v,qgex

[p0332-b0016 | ordinary-paragraph | high] Sl

[p0332-b0017 | ordinary-paragraph | high] and

[p0332-b0018 | ordinary-paragraph | high] N

[p0332-b0019 | equation | low] D,G(A,v):w =A df v,0w/dx; + w,0v/dx;), w=(w rex.

[p0332-b0020 | ordinary-paragraph | high] Let us determine the space Z. In view of Theorem 1.1.3, we know that

[p0332-b0021 | ordinary-paragraph | high] HQ) ce £(Q) story 3

[p0332-b0022 | ordinary-paragraph | high] and the imbedding of H}(Q) into L?(Q) is compact for p < 6. Next, applying

[p0332-b0023 | corollary | high] Corollary I.1.1 observe that for v and w in Hj(Q)%, we have

[p0332-b0024 | ordinary-paragraph | high] N

[p0332-b0025 | ordinary-paragraph | high] » (vj0w/dx,; + w,0v/0x,)€ L*?(Q)*.

[p0332-b0026 | ordinary-paragraph | high] Finally, applying again Theorem I.1.3 we find that L7(Q) is compactly imbedded

[p0332-b0027 | ordinary-paragraph | high] in H-‘(Q) whenever q > 6/5. It stems from these remarks that we can choose

[p0332-b0028 | equation | low] Z = L°?(Q). SY with a compact imbedding

[p0332-b0029 | ordinary-paragraph | high] and (3.36) holds.

[p0332-b0030 | ordinary-paragraph | high] Now, let X, = Wo, x M, and let T,¢ 4(Y; X,,) be the approximate Stokes

[p0332-b0031 | ordinary-paragraph | high] operator defined by:

[p0332-b0032 | equation | low] T,£ = (V,59,)€X;, is the solution of

[p0332-b0033 | equation | low] (grad v,, grad w,,) — (q,,, div w,) = <f,w,> Vw,eWo,,

[p0332-b0034 | equation | low] | (r,,divv,)=0O Vr,eM,.

[p0332-b0035 | ordinary-paragraph | high] It follows from Theorem II.1.8 that, owing to the hypotheses H1, H2 and H3

## PDF 333 / printed 319



[p0333-b0003 | ordinary-paragraph | high] (4.9) Bb Ftyeh Il—d Glnlo, a} = 9,

[p0333-b0004 | ordinary-paragraph | high] ise,

[p0333-b0005 | equation | low] lim ||(J, — T)fly=0 VfeY.

[p0333-b0006 | equation | low] h->0

[p0333-b0007 | ordinary-paragraph | high] Furthermore, when (v,q) belongs to H™*1(Q)" x H™(Q) for some integer m in

[p0333-b0008 | ordinary-paragraph | high] [1,1], this same theorem asserts that:

[p0333-b0009 | ordinary-paragraph | high] (4.10) lv, — Vii.a + Ilda — Gllo.q < Ch™ (Vil ma1.a + 4 Ilma)

[p0333-b0010 | ordinary-paragraph | high] 1.€. I(T, — T)flly< Ch™| |T E |) msi (ayy x HQ):

[p0333-b0011 | ordinary-paragraph | high] As mentioned at the end of Remark 3.4, the compactness of the imbedding of Z

[p0333-b0012 | ordinary-paragraph | high] into Y together with (4.9) imply that

[p0333-b0013 | equation | low] lim ||7 , — T ||¢ z;x) = 9.

[p0333-b0014 | equation | low] h>0

[p0333-b0015 | ordinary-paragraph | high] Thus (3.37) and (3.38) hold.

[p0333-b0016 | ordinary-paragraph | high] Finally, since

[p0333-b0017 | ordinary-paragraph | high] 2

[p0333-b0018 | equation | low] a(u,;u,,V,) = v(grad u,, grad v,) + (5 yds /0%5.%),

[p0333-b0019 | ordinary-paragraph | high] we can express Problem (4.2) as follows:

[p0333-b0020 | ordinary-paragraph | high] N

[p0333-b0021 | equation | low] (grad u,, grad v,) — (1/v)(p,, div v,)= ayy (1 py iy0u/0%,%)

[p0333-b0022 | equation | low] (q,,divu,)=90 Vq,eM,.

[p0333-b0023 | ordinary-paragraph | high] In other words, u, = (u,,(1/v)p,) satisfies:

[p0333-b0024 | equation | low] u, = — T,,G(1/v, u;)

[p0333-b0025 | ordinary-paragraph | high] ie: F(A, u,) = u, + T,G(A,u,) =O with 2 = 1/\.

[p0333-b0026 | ordinary-paragraph | high] Consequently, we can apply the conclusion of Theorem 3.3: for h < ho

[p0333-b0027 | ordinary-paragraph | high] sufficiently small there exists a unique branch of nonsingular solutions of (4.2):

[p0333-b0028 | ordinary-paragraph | high] {(A, uy(A) = (uy(), Apy(A))); 4€ A},

[p0333-b0029 | ordinary-paragraph | high] i.e. u,(A) + T,G(A,u,(4)) =0 Wired,

[p0333-b0030 | ordinary-paragraph | high] and a real number a > 0, independent of h, such that:

[p0333-b0031 | equation | low] lu,(A)-—uA)llx<a WAed.

[p0333-b0032 | ordinary-paragraph | high] In addition, according to Remark 3.6, the mapping / > u,(A) is 6” because the

[p0333-b0033 | ordinary-paragraph | high] mapping G is also @” with bounded derivatives of all order on every bounded

[p0333-b0034 | ordinary-paragraph | high] subsets of A x X.

## PDF 334 / printed 320



[p0334-b0003 | equation | low] Ju,(2) — u(A)|1,.0 + IAL Ipla (A) — P(A) Ilo.e < KI — T)GU,u))Il x-

[p0334-b0004 | ordinary-paragraph | high] Hence (4.6) follows from (4.9). Furthermore, since

[p0334-b0005 | equation | low] u(A) = (u(A), Ap(A))e H™**(Q)” x H"(Q)

[p0334-b0006 | ordinary-paragraph | high] is the solution of the Stokes system:

[p0334-b0007 | equation | low] u(A) = —TG(A,u(A)),

[p0334-b0008 | ordinary-paragraph | high] the error estimate (II.1.46) gives:

[p0334-b0009 | equation | low] I(T, — T)GA, u(A))Ilx < Ch™{||u(A) |Im+1,0 + IPA) Ima}

[p0334-b0010 | ordinary-paragraph | high] Thus (4.7) stems from the continuity of the mapping 4— u(A) from A into

[p0334-b0011 | ordinary-paragraph | high] He (OV SH (Qy ies]

[p0334-b0012 | ordinary-paragraph | high] It is also possible to derive an L?-estimate for the velocity. Like in the linear

[p0334-b0013 | ordinary-paragraph | high] case we must assume that the associated Stokes problem is regular (cf. Definition

[p0334-b0014 | ordinary-paragraph | high] II.1.1):

[p0334-b0015 | ordinary-paragraph | high] (4.11) |t he mapping (, 1) > —v4 + grad p is an isomorphism from [H?(Q)"N

[p0334-b0016 | ordinary-paragraph | high] VLA (OC) Le (@)] onto L2(Qy.

[p0334-b0017 | theorem | high] Theorem 4.2. We retain the hypotheses of Theorem 4.1 and we assume that (4.11)

[p0334-b0018 | ordinary-paragraph | high] holds. If the mapping 4 > (u(A), p(A)) is continuous from A into H™*1(Q)% x H™(Q)

[p0334-b0019 | ordinary-paragraph | high] for some integer m in [1,1], then we have the following L?-estimate for all 4 in A:

[p0334-b0020 | ordinary-paragraph | high] (4.12) l|u,(4) — u(A) loa < KA™™.

[p0334-b0021 | proof | high] Proof. Let us apply Theorem 3.5. Since we are only interested in the velocity u,

[p0334-b0022 | ordinary-paragraph | high] we are going to drop entirely the pressure p. Thus we take

[p0334-b0023 | equation | low] oH. (O)y ee k= (Oy

[p0334-b0024 | ordinary-paragraph | high] and for f in Y we define v = Tf by:

[p0334-b0025 | equation | low] veV, (gradv,gradw)=<f,w> Ywel.

[p0334-b0026 | ordinary-paragraph | high] As the mapping G(A, v) depends only on the velocity v (and not on q) we can leave

[p0334-b0027 | ordinary-paragraph | high] it as such. Thus, u is a solution of the Navier-Stokes system (4.1) if and only if:

[p0334-b0028 | equation | low] F(A,u) =u + TG(,u) = 0.

[p0334-b0029 | ordinary-paragraph | high] Next, we choose

[p0334-b0030 | equation | low] Ae he(ovr W = (ASQ) OBA

[p0334-b0031 | ordinary-paragraph | high] From Theorem I.1.3, we know that X (resp. W) is compactly imbedded into

[p0334-b0032 | ordinary-paragraph | high] H (resp. X). Now, take u in W and let us check that D,G(A,u)e¢ Y(H; Y) =

[p0334-b0033 | ordinary-paragraph | high] L(L?(Q)*; H-*(Q)%). Indeed, if ve L?(Q)* and € P(Q)%, we can write:

## PDF 335 / printed 321



[p0335-b0003 | ordinary-paragraph | high] But <uj;0Vv/0x;,0> = —<v, 0(u;)/0x;>;

[p0335-b0004 | ordinary-paragraph | high] hence |<ujOv/0x;,0>| < Cy||Vllo,ellyllaalllli.a-

[p0335-b0005 | ordinary-paragraph | high] with a similar bound for <v,éu/dx;,@>. As a consequence, D,G(A,u) can be

[p0335-b0006 | ordinary-paragraph | high] extended to a continuous linear operator from L?(Q)* into H~'(Q)%, provided u

[p0335-b0007 | ordinary-paragraph | high] belongs to H*(Q)”. This settles (3.47).

[p0335-b0008 | ordinary-paragraph | high] As far as (3.48) is concerned, we make use of Remark 3.7 and the compactness

[p0335-b0009 | ordinary-paragraph | high] of X into H.

[p0335-b0010 | ordinary-paragraph | high] It remains to verify (3.50): D, F(A, u(4)) is an isomorphism of H. By assump-

[p0335-b0011 | ordinary-paragraph | high] tion, we already know that:

[p0335-b0012 | equation | low] D,F(A,u(A)) = I + TD,G(A,u(d))

[p0335-b0013 | ordinary-paragraph | high] is an isomorphism of X. In addition, we have just seen that TD,G(A,u(A))eé

[p0335-b0014 | ordinary-paragraph | high] L(L?(Q)’; V) whenever u(/) € H*(Q)". Therefore, the compactness of the imbed-

[p0335-b0015 | ordinary-paragraph | high] ding of H!(Q) into L?(Q) implies that TD, G(A, u(A)) is a compact operator from

[p0335-b0016 | ordinary-paragraph | high] L?(Q)* into itself. Hence we can apply to D,F(A,u(A)) Fredholm’s alternative,

[p0335-b0017 | ordinary-paragraph | high] namely D, F(A, u(A)) is an isomorphism of H iff the equation

[p0335-b0018 | ordinary-paragraph | high] (4.13) D,F(,u(A)):v=0 withy in H

[p0335-b0019 | ordinary-paragraph | high] has only the zero solution. But if v in H satisfies (4.13), then v belongs to V since

[p0335-b0020 | ordinary-paragraph | high] v = —TD,G(A,u(A)):v. Therefore v = 0 because D, F(A, u(A)) is an isomorphism

[p0335-b0021 | ordinary-paragraph | high] of X. This proves (3.50).

[p0335-b0022 | ordinary-paragraph | high] Consequently, we can apply the conclusion of Theorem 3.5: if the mapping

[p0335-b0023 | ordinary-paragraph | high] A= u(A) is continuous from A into [H}(Q)N H?(Q)}", then for all h sufficiently

[p0335-b0024 | ordinary-paragraph | high] small, we have:

[p0335-b0025 | ordinary-paragraph | high] llu,(A) — uA) llo,o < Co{ I(T— T,)G(A,u(4)) loa + lun(A) — u(A)It,o}-

[p0335-b0026 | ordinary-paragraph | high] Thus, when (u(A), p(A)) belongs to H"**(Q)*" x H™(Q), the bound (II.1.50) gives:

[p0335-b0027 | equation | low] I(T— T,)G(A,u())|lo,a < Ch" {U(A) IImsia + PA) Ilm,a}

[p0335-b0028 | ordinary-paragraph | high] and (4.12) stems from this estimate and (4.7). []

[p0335-b0029 | ordinary-paragraph | high] Roughly speaking, Theorems 4.1 and 4.2 can be summarized by saying that

[p0335-b0030 | ordinary-paragraph | high] all the function spaces introduced in Paragraphs II.2 and II.3 to solve the Stokes

[p0335-b0031 | ordinary-paragraph | high] equations can be also applied to approximate branches of nonsingular solutions

[p0335-b0032 | ordinary-paragraph | high] of the Navier-Stokes problem with a similar accuracy. For instance, assume that

[p0335-b0033 | ordinary-paragraph | high] the two-dimensional Navier-Stokes equations (4.1) have a branch of nonsingular

[p0335-b0034 | ordinary-paragraph | high] solutions with the regularity:

[p0335-b0035 | ordinary-paragraph | high] (4.14) A-—(u(A), p(4)) is continuous from A into H-7(O)- x A (Q),

[p0335-b0036 | ordinary-paragraph | high] Assume that Q is a bounded polygon triangulated by 7, and for each K€ 7, take

## PDF 336 / printed 322



[p0336-b0003 | equation | low] P,(k) = P? @ span{njjjA1<ij,k <3,i4j Fk}.

[p0336-b0004 | ordinary-paragraph | high] Then, if the triangulation 7, is regular the finite element scheme (4.2) with the

[p0336-b0005 | ordinary-paragraph | high] spaces:

[p0336-b0006 | equation | low] W, = {we (Q); wh EA(x) VkET;},

[p0336-b0007 | equation | low] Q, = {gE L*(Q); qe Po VKET;}

[p0336-b0008 | ordinary-paragraph | high] has a unique branch of solutions {(A, (u,(A), Ap,(4))); 4€ 4} that satisfies the error

[p0336-b0009 | ordinary-paragraph | high] bound:

[p0336-b0010 | ordinary-paragraph | high] ju,(A)— u(A)i1,0 + Ip a(A) — PA)Ilo.e < Ch(lu(A)l2.0 + IPAlio) VAed.

[p0336-b0011 | ordinary-paragraph | high] In addition, when Q is convex we have the L?-estimate:

[p0336-b0012 | equation | low] lu,(2) — u(A)Ilo,o < Ch*(\u(A)|2,0 + [PAI1.e) Wed.

[p0336-b0013 | ordinary-paragraph | high] Another interesting example is the scheme derived from the controversial

[p0336-b0014 | ordinary-paragraph | high] Q, — Py element discussed in Sections II.3.3 and II.3.4 in the case of the square

[p0336-b0015 | ordinary-paragraph | high] (—1,1) x (—1,1). Assume that 7, is a square grid with mesh-size h = 1/(4n) so

[p0336-b0016 | ordinary-paragraph | high] that the conclusion of Theorem IJ.3.4 be valid. Then take

[p0336-b0017 | equation | low] Won = V, and M, = M,

[p0336-b0018 | ordinary-paragraph | high] with V, and M, defined respectively by (II.3.33) and (I1.3.32). It is established in

[p0336-b0019 | ordinary-paragraph | high] Sections II.3.3 and II.3.4 that this choice of spaces satisfies the three hypotheses

[p0336-b0020 | ordinary-paragraph | high] H1, H2 and H3 (cf. (I1.3.39), (I1.3.40) and Theorem II.3.4). Therefore Theorems

[p0336-b0021 | ordinary-paragraph | high] 4.1 and II.3.5 imply that, under the condition (4.14), the finite element scheme

[p0336-b0022 | ordinary-paragraph | high] (4.2) has a unique branch of solutions

[p0336-b0023 | ordinary-paragraph | high] {(A, (u,(A), AB,(A))); Ae A}

[p0336-b0024 | ordinary-paragraph | high] and

[p0336-b0025 | ordinary-paragraph | high] Ju,(4) — uA) .o + ||P a(A) — PA)lo,2 S Ch{lu(A)l2,0 + IPAs. a}-

[p0336-b0026 | ordinary-paragraph | high] Likewise, we derive immediately from Theorem 4.2 and Corollary II.3.2 that:

[p0336-b0027 | equation | low] llu,(A) — u(A) Ilo, < Ch? {|uA)|2,0 + IPAs ,2}-

[p0336-b0028 | remark | high] Remark 4.1. To solve the scheme (4.2) with the Q, — P, element, it is convenient

[p0336-b0029 | ordinary-paragraph | high] (like in the linear case) to use the basis of V,, described at the end of Section II.3.4.

[p0336-b0030 | subsection | high] 4.2. Formulation in Primitive Variables: the Case of Continuous Pressures

[p0336-b0031 | ordinary-paragraph | high] Going back to Chapter II, we can plainly see that the previous analysis applies

[p0336-b0032 | ordinary-paragraph | high] readily to the “mini” element discussed in Section II.4.1 as well as the “Hood-

[p0336-b0033 | ordinary-paragraph | high] Taylor” elements of Section II.4.2. Indeed, all these elements satisfy the hypotheses

## PDF 337 / printed 323



[p0337-b0004 | ordinary-paragraph | high] Hence in the neighborhood of a branch of nonsingular solutions with the

[p0337-b0005 | ordinary-paragraph | high] regularity (4.14) and if the triangulation 7, is regular, the finite element scheme

[p0337-b0006 | ordinary-paragraph | high] (4.2) with the spaces

[p0337-b0007 | equation | low] W, = {weG(Q)?; wleA(k) Wee F;},

[p0337-b0008 | equation | low] P(k) = [P, © span(A, AzAs)1’,

[p0337-b0009 | equation | low] 0, = {qe@(Q); q|,EP, Vee T,}

[p0337-b0010 | ordinary-paragraph | high] has a unique branch of solutions: {(A,(u,(A), 4p,(4)));4¢4 } and there exists a

[p0337-b0011 | ordinary-paragraph | high] constant C independent of / such that:

[p0337-b0012 | equation | low] |u(A) — un(A)l1.0 + PA) — pilA)llo.o < ChtluAl2,0 + [PAli,9}-

[p0337-b0013 | ordinary-paragraph | high] When @ is convex we have the L?-estimate:

[p0337-b0014 | equation | low] |u(2) — u,(A)llo,@ < Ch? {uAl2,0 + [Pl a}-

[p0337-b0015 | ordinary-paragraph | high] Likewise the error estimates of Theorems II.4.3 and I.4.4 for the two “Hood-

[p0337-b0016 | ordinary-paragraph | high] Taylor” elements carry over to the scheme (4.2) when 7%, and the branch of

[p0337-b0017 | ordinary-paragraph | high] nonsingular solutions of the Navier-Stokes equations have the adequate regularity.

[p0337-b0018 | ordinary-paragraph | high] Unfortunately, the “Glowinski-Pironneau” scheme does not fit so neatly into

[p0337-b0019 | ordinary-paragraph | high] the preceding framework and has to be analyzed separately. Recall that the

[p0337-b0020 | ordinary-paragraph | high] velocity and pressure spaces are those of the “Hood-Taylor” scheme:

[p0337-b0021 | equation | low] X, = {ve $(Q); v|,eP? Wee J, vir =O},

[p0337-b0022 | equation | low] O, = {gE OQ); g\.EP: VKET;},

[p0337-b0023 | ordinary-paragraph | high] with the additional space

[p0337-b0024 | ordinary-paragraph | high] Ap ORs ELKO),

[p0337-b0025 | ordinary-paragraph | high] for the auxiliary potential. When adapted to the Navier-Stokes problem, the

[p0337-b0026 | ordinary-paragraph | high] “Glowinski-Pironneau” method, in the version given by Remark II.4.5, reads:

[p0337-b0027 | ordinary-paragraph | high] Find a triple (U,, Drs Mn) EX, X Qy X DP, Satisfying:

[p0337-b0028 | ordinary-paragraph | high] 2)

[p0337-b0029 | equation | low] v(grad u,,, grad v,) + (5 (u,,),Ou,/Ox;,¥, — grad i)

[p0337-b0030 | equation | low] j=1

[p0337-b0031 | equation | low] 4.15

[p0337-b0032 | ordinary-paragraph | high] ee +(grad p,,v, — gradq,) = (f,v, — gradq,) V(Vn,dn)EX n X D,

[p0337-b0033 | equation | low] (u, — grad y,,gradq,)=90 VWq,€ Qh.

[p0337-b0034 | ordinary-paragraph | high] Let us see under what conditions the exact Navier-Stokes problem admits a

[p0337-b0035 | ordinary-paragraph | high] formulation similar to (4.15). To solve the Stokes problem in Section II.4.3 we

[p0337-b0036 | ordinary-paragraph | high] took the right-hand side f in L?(Q)? and chose Hj(Q) for space of potentials.

[p0337-b0037 | ordinary-paragraph | high] Here this is not realistic because the nonlinear term

## PDF 338 / printed 324



[p0338-b0004 | equation | low] j=1

[p0338-b0005 | ordinary-paragraph | high] which is considered part of the right-hand side, belongs only to L?-*(Q)* for any

[p0338-b0006 | ordinary-paragraph | high] ¢ > 0 whenever u belongs to H!(Q)? (cf. Corollary I.1.1 with N = 2). This remark

[p0338-b0007 | ordinary-paragraph | high] suggests to fix a real r in the interval (1,2) and take W'*(Q) for space of

[p0338-b0008 | ordinary-paragraph | high] potentials with 1/s + 1/r = 1. Then consider the problem:

[p0338-b0009 | ordinary-paragraph | high] For fe L"(Q)* find a triple (u, p, u) € H3(Q)? x W'"(Q) x Wos(Q) such that

[p0338-b0010 | ordinary-paragraph | high] 2

[p0338-b0011 | ordinary-paragraph | high] v(grad u, grad v) + (3 u,0u/Ox;,v — grad ‘)+ (grad p, v — grad q)

[p0338-b0012 | equation | low] jH=1

[p0338-b0013 | equation | low] 4.16

[p0338-b0014 | ordinary-paragraph | high] na =(f.v—gradq) V(v,q)e Ho(Q)? x Wor(Q)

[p0338-b0015 | equation | low] (u — grady,gradg)=0 VqeWw'"(Q).

[p0338-b0016 | ordinary-paragraph | high] It is a matter of routine to check that this problem is equivalent to the Navier-

[p0338-b0017 | ordinary-paragraph | high] Stokes problem (4.1) in the following sense:

[p0338-b0018 | ordinary-paragraph | high] if (u, p) is a solution of (4.1) with p in W*"(Q) then the triple (u, p, uw= 0) is a

[p0338-b0019 | ordinary-paragraph | high] solution of (4.16). Conversely, each solution of (4.16) is of the form (u, p, u = 0)

[p0338-b0020 | ordinary-paragraph | high] where the pair (u, p) satisfies (4.1).

[p0338-b0021 | ordinary-paragraph | high] Obviously, the same conclusion applies to the Stokes problem with right-

[p0338-b0022 | ordinary-paragraph | high] hand side f in L’(Q)?:

[p0338-b0023 | ordinary-paragraph | high] if the pressure solution p of the Stokes problem belongs to W‘*’(Q) then this

[p0338-b0024 | ordinary-paragraph | high] problem is equivalent to:

[p0338-b0025 | ordinary-paragraph | high] Find (u, p, u)H€4 (2 )? x W'"(Q) x WIs(Q) such that

[p0338-b0026 | equation | low] (grad u, grad v) + (grad p, v — grad q) = (f, v — grad q)

[p0338-b0027 | ordinary-paragraph | high] (4.17) V(v, q)€ H4(Q)? x W}’5(Q),

[p0338-b0028 | equation | low] (u—gradg)=0 VqeW!:"(Q).

[p0338-b0029 | ordinary-paragraph | high] Therefore, in order to express the Stokes operator by (4.17) for every right-hand

[p0338-b0030 | ordinary-paragraph | high] side in L’(Q)? we must assume that the Stokes problem is regular in a more

[p0338-b0031 | ordinary-paragraph | high] general sense than (4.11):

[p0338-b0032 | ordinary-paragraph | high] (4.18) i mapping (@, 4) > — 4 + grad is an isomorphism from [W?""(Q)N

[p0338-b0033 | ordinary-paragraph | high] x [W2"(Q)/R] onto LQ) for all re(1, 2].

[p0338-b0034 | ordinary-paragraph | high] “WP

[p0338-b0035 | remark | high] Remark 4.2. Here the pressure is taken in the quotient space W':"(Q)/R instead

[p0338-b0036 | ordinary-paragraph | high] of W*"(Q)N Lo(Q) because in the practical computation of (4.15), P;, is fixed by

[p0338-b0037 | ordinary-paragraph | high] the condition |; p,ds = 0 (cf. Lemma IL4.3).

[p0338-b0038 | ordinary-paragraph | high] Now, we can put Problem (4.16) into the setting of Section 3.3. We take:

[p0338-b0039 | equation | low] Y = L'(Q)*.) +X HG (Q)? 9 [L2@) RIA).

## PDF 339 / printed 325



[p0339-b0004 | ordinary-paragraph | high] ReZi)). ft (wp, — 0) “solution of (4:17):

[p0339-b0005 | ordinary-paragraph | high] The nonlinearity is embodied by the usual mapping G:

[p0339-b0006 | ordinary-paragraph | high] 2

[p0339-b0007 | equation | low] ain) = 2 uavlex—1),

[p0339-b0008 | equation | low] j=l AeR,, v=(v,g,~)eX

[p0339-b0009 | ordinary-paragraph | high] which maps R, x X into L’(Q)*. With these notations, Problem (4.16) takes the

[p0339-b0010 | ordinary-paragraph | high] standard form:

[p0339-b0011 | equation | low] F(A,u) =0

[p0339-b0012 | ordinary-paragraph | high] with A = 1/v, u = (u, Ap, 0) and F(A, u) =u + TG(A,u).

[p0339-b0013 | remark | high] Remark 4.3. When the Stokes operator has the regularity (4.18), each solution u

[p0339-b0014 | ordinary-paragraph | high] of Problem (4.16) with right-hand side f in L’(Q)* has the regularity ue W7""(Q)’,

[p0339-b0015 | ordinary-paragraph | high] pe W?"(Q). This is valid for all real re(1, 2].

[p0339-b0016 | remark | high] Remark 4.4. It is important to note that if the Stokes operator has the regularity

[p0339-b0017 | ordinary-paragraph | high] (4.18) then every branch of nonsingular solutions of Problem (4.1) with right-

[p0339-b0018 | ordinary-paragraph | high] hand side f in L’(Q)? is also a branch of nonsingular solutions of Problem (4.16)

[p0339-b0019 | ordinary-paragraph | high] and conversely.

[p0339-b0020 | ordinary-paragraph | high] Next, we set

[p0339-b0021 | equation | low] W, =X, x [0,/R) x & eX

[p0339-b0022 | ordinary-paragraph | high] and let T,¢ #(Y; W,) be the discrete Stokes operator corresponding to (4.17):

[p0339-b0023 | equation | low] Tf = (u,, Pp, ;,) solution of:

[p0339-b0024 | equation | low] (grad u,, grad v,,) + (grad p,,v, — grad q,,) = (f, v, — grad q,)

[p0339-b0025 | ordinary-paragraph | high] (4.19) V(Vi59,)EX n X D,,

[p0339-b0026 | equation | low] (u, — grad w,,gradq,)=9 Vq,€Q,.

[p0339-b0027 | ordinary-paragraph | high] Therefore, Problem (4.15) has the equivalent formulation:

[p0339-b0028 | equation | low] F(A, u,(A)) = 0

[p0339-b0029 | ordinary-paragraph | high] with A = 1/v, u,(A) = (u,(A), App (A), Mn(A)) and F(A, u,) = Un + TGA, uy).

[p0339-b0030 | ordinary-paragraph | high] We are now in a position to apply Theorem 3.3. We take

[p0339-b0031 | equation | low] Z=Y

[p0339-b0032 | ordinary-paragraph | high] and (3.36) holds automatically. As far as the approximation properties of the

[p0339-b0033 | ordinary-paragraph | high] operator 7, are concerned, we can apply the material of Section 11.4.3. In

[p0339-b0034 | ordinary-paragraph | high] particular, it is established in Theorem II.4.6 that

## PDF 340 / printed 326



[p0340-b0003 | ordinary-paragraph | high] (4.20) |M alt, as< |lu— Urllo, Q>

[p0340-b0004 | ordinary-paragraph | high] (ple (1 + \/2/B%) inf IP — dallo.a + (1/6*)|u ~ Wsls,a.

[p0340-b0005 | ordinary-paragraph | high] Gn€ Qn

[p0340-b0006 | ordinary-paragraph | high] where P, denotes the H'-projection on Q,, L6(Q) defined by (A.25), p (resp. Pp)

[p0340-b0007 | ordinary-paragraph | high] denotes the representative of p (resp. p,,) in L$(Q) and f* is the constant of the

[p0340-b0008 | ordinary-paragraph | high] inf-sup condition. Note that (4.20) requires only the mild assumption (II.4.17)

[p0340-b0009 | ordinary-paragraph | high] and the regularity of the triangulation 7,. Thus (3.37) follows from (4.20) and a

[p0340-b0010 | ordinary-paragraph | high] standard density argument.

[p0340-b0011 | ordinary-paragraph | high] Finally, (3.38) is a consequence of (4.20) and the regularity assumption (4.18)

[p0340-b0012 | ordinary-paragraph | high] (which is valid when Q is convex). More precisely, if (4.18) holds then u and p

[p0340-b0013 | ordinary-paragraph | high] have the extra regularity:

[p0340-b0014 | ordinary-paragraph | high] ue w2""(Q)?, pew?"(Q).

[p0340-b0015 | ordinary-paragraph | high] Then just like in Section III.3.1 we derive:

[p0340-b0016 | ordinary-paragraph | high] (4.21) inf |u—V4l1,a< C,h** ul ,,0

[p0340-b0017 | ordinary-paragraph | high] Vn eXn

[p0340-b0018 | ordinary-paragraph | high] and if in addition 2 is convex and 7%, is uniformly regular, Lemma III.3.4

[p0340-b0019 | ordinary-paragraph | high] establishes that

[p0340-b0020 | ordinary-paragraph | high] (4.22) IP — PrPllo.g< C,h**|In hl ** |p|, a.

[p0340-b0021 | ordinary-paragraph | high] Collecting these inequalities we obtain:

[p0340-b0022 | ordinary-paragraph | high] (4.23) |u—uylie + |Hali.a + IP — Pallo.g <C 3h**|Ihnl? **||fllo,.0

[p0340-b0023 | ordinary-paragraph | high] which proves (3.38).

[p0340-b0024 | ordinary-paragraph | high] Observe also that when Q is convex and 7%, is uniformly regular, (4.19) and

[p0340-b0025 | theorem | high] Theorem A.2 imply that:

[p0340-b0026 | ordinary-paragraph | high] (4.24) Hnl1,2,.0 S C4(a) ||div(u —u,)llo,@ Vreal a > 2.

[p0340-b0027 | ordinary-paragraph | high] Indeed, we can consider that 1, is the H}-projection, B,u, of the solution p of

[p0340-b0028 | ordinary-paragraph | high] the Dirichlet problem:

[p0340-b0029 | equation | low] (grad uu, grad q) = —(div(u—u,),q) Vqe Ho(Q).

[p0340-b0030 | ordinary-paragraph | high] Consequently, the conclusion of Theorem 3.3 is valid; it is summarized in the

[p0340-b0031 | ordinary-paragraph | high] following theorem.

[p0340-b0032 | theorem | high] Theorem 4.3, Let Q be a bounded, convex polygon and assume that J, is a uniformly

[p0340-b0033 | ordinary-paragraph | high] regular triangulation of Q that satisfies (1.4.17). For fe LQ), re(1, 2], let {(A,

[p0340-b0034 | ordinary-paragraph | high] (u(A), Ap(A), 0); 2 = 1/v€ A}, with p(A) chosen in L2(Q), be a branch of nonsingular

[p0340-b0035 | ordinary-paragraph | high] solutions of the Navier-Stokes Problem (4.16). Then for h < hg sufficiently small,

[p0340-b0036 | ordinary-paragraph | high] there exists a unique 6” branch {(A,(u,(A), APp(A), Uy(A))); AE A}, with p,(A) chosen

[p0340-b0037 | ordinary-paragraph | high] in L2(Q), of solutions of Problem (4.15) such that:

## PDF 341 / printed 327



[p0341-b0004 | equation | low] sup [Ha(Ali.2.0 < C(ah|In hit?" Yar > 2,

[p0341-b0005 | ordinary-paragraph | high] AeA

[p0341-b0006 | ordinary-paragraph | high] 1/r + 1/s = 1, with constants independent of h and A.

[p0341-b0007 | ordinary-paragraph | high] Besides that, if the mapping 4 = (u(A), p(A)) is continuous from A into H™*'(Q)* x

[p0341-b0008 | ordinary-paragraph | high] H™(Q) for m = 1 or 2, we have the estimate:

[p0341-b0009 | ordinary-paragraph | high] (4.26) Jun(A) — u(A)li2 + IPA) — PA) Ilo. + Ha(Ali ae < KA™

[p0341-b0010 | ordinary-paragraph | high] for all AE A.

[p0341-b0011 | remark | high] Remark 4.5. It is not yet known whether or not a more accurate L?-estimate can

[p0341-b0012 | ordinary-paragraph | high] be obtained for u — u, + grad y,, as it is done in Theorem II.4.6 for the Stokes

[p0341-b0013 | ordinary-paragraph | high] problem. The delicate point is that the proof of Theorem II.4.6 uses explicitly the

[p0341-b0014 | ordinary-paragraph | high] equality:

[p0341-b0015 | equation | low] Ap = divf

[p0341-b0016 | ordinary-paragraph | high] which is valid for every Stokes system but is obviously not true for Navier-Stokes

[p0341-b0017 | ordinary-paragraph | high] equations.

[p0341-b0018 | subsection | high] 4.3. Mixed Incompressible Methods: the “Stream Function-Vorticity”

[p0341-b0019 | ordinary-paragraph | high] Formulation

[p0341-b0020 | ordinary-paragraph | high] In this section, we investigate exclusively the two-dimensional case. (As men-

[p0341-b0021 | ordinary-paragraph | high] tioned at the beginning of this paragraph, the corresponding analysis of mixed

[p0341-b0022 | ordinary-paragraph | high] incompressible schemes in three dimensions is still an open problem). We pro-

[p0341-b0023 | ordinary-paragraph | high] pose to extend to the Navier-Stokes equations the mixed formulation introduced

[p0341-b0024 | ordinary-paragraph | high] in Section III.2.1. To begin with, recall the stream function-vorticity formulation

[p0341-b0025 | ordinary-paragraph | high] of the Stokes operator.

[p0341-b0026 | ordinary-paragraph | high] Let us fix a real s > 4 and let r be its dual exponent:

[p0341-b0027 | equation | low] I/r + 1/s = 1.

[p0341-b0028 | ordinary-paragraph | high] Define the space of stream functions:

[p0341-b0029 | equation | low] ® = {ye H'(Q); ylr, = 9, xr, = a constant c;, 1 <i < p}

[p0341-b0030 | ordinary-paragraph | high] where as usual Jy, ..., , denote the connected components of the boundary I”

[p0341-b0031 | ordinary-paragraph | high] with exterior component [, (cf. Figure 2). We know that the operator curl is an

[p0341-b0032 | ordinary-paragraph | high] isomorphism from

[p0341-b0033 | equation | low] (4.27)

[p0341-b0034 | ordinary-paragraph | high] Pate Mel)

[p0341-b0035 | ordinary-paragraph | high] onto

[p0341-b0036 | equation | low] HO L(Q)? = {ve LQ); divv = 0,v

[p0341-b0037 | equation | low] -n|p = 0}.

## PDF 342 / printed 328



[p0342-b0004 | ordinary-paragraph | high] pe W1,"(Q) then the Stokes Problem (4.8) is equivalent to:

[p0342-b0005 | ordinary-paragraph | medium] Find y eΦ, and we Wi,(Q) such that:

[p0342-b0006 | ordinary-paragraph | low] "中A

[p0342-b0007 | equation | low] (curl w, curl Φ) = (f, curl Φ)

[p0342-b0008 | equation | low] (4.28a)

[p0342-b0009 | equation | low] (o)M>rA

[p0342-b0010 | equation | low] (curl y, curl μ) = (@,μ)

[p0342-b0011 | ordinary-paragraph | medium] Find pe W1,"(Q)N L?(Q) such that:

[p0342-b0012 | ordinary-paragraph | low] "()sM bA

[p0342-b0013 | equation | low] (grad p, grad q) = (f -- curl w, grad q)

[p0342-b0014 | equation | low] (4.28b)

[p0342-b0015 | ordinary-paragraph | high] with u = curl y and o = curlu.

[p0342-b0016 | ordinary-paragraph | high] Here again, it is necessary to write the Stokes problem in the form (4.28) for

[p0342-b0017 | ordinary-paragraph | high] every right-hand side fe L'(Q)?. Therefore we assume that (4.18) holds. Then

[p0342-b0018 | ordinary-paragraph | high] setting

[p0342-b0019 | equation | low] Y = L"(Ω)²,

[p0342-b0020 | equation | low] X = {curlΦ; Φ∈Φ,} × L²(Ω) x L(Ω),

[p0342-b0021 | ordinary-paragraph | high] the Stokes operator T is defined by:

[p0342-b0022 | ordinary-paragraph | medium] Te E(Y; X),

[p0342-b0023 | equation | low] Tf = (curl y,w, p)  solution of (4.28).

[p0342-b0024 | ordinary-paragraph | high] Next, in view of (2.27) the convection term satisfies the identities:

[p0342-b0025 | equation | low] ;du/0x; /curl Φdx =

[p0342-b0026 | equation | low] W grad y · curl Φ dx

[p0342-b0027 | ordinary-paragraph | medium] J

[p0342-b0028 | ordinary-paragraph | low] 12

[p0342-b0029 | equation | low] (4.29)

[p0342-b0030 | ordinary-paragraph | low] e帕

[p0342-b0031 | ordinary-paragraph | low] 叫

[p0342-b0032 | ordinary-paragraph | low] pe

[p0342-b0033 | ordinary-paragraph | high] dx,

[p0342-b0034 | ordinary-paragraph | medium] 0x1 0x2

[p0342-b0035 | ordinary-paragraph | medium] 0x2 0x1.

[p0342-b0036 | ordinary-paragraph | low] Ω

[p0342-b0037 | equation | low] u;ou/0x; gradq dx =

[p0342-b0038 | equation | low] w grad ↓ : grad q dx

[p0342-b0039 | ordinary-paragraph | low] Jo

[p0342-b0040 | equation | low] (4.30)

[p0342-b0041 | ordinary-paragraph | high] + (1/2)

[p0342-b0042 | equation | low] grad( llu ll²) : grad q dx,

[p0342-b0043 | ordinary-paragraph | high] where curly = u, w = curlu and Il. Il denotes the Euclidean norm. Hence we

[p0342-b0044 | ordinary-paragraph | high] introduce the nonlinearity by the mapping

[p0342-b0045 | equation | low] (4.31)

[p0342-b0046 | equation | low] G(,u) = A(wgrady -f)  AeR+,

[p0342-b0047 | equation | low] u = (curly,w, p)e X,

[p0342-b0048 | ordinary-paragraph | high] and we agree to include the term (1/2) Ilu |² in the pressure:

[p0342-b0049 | ordinary-paragraph | high] i.e. we work instead with the kinematic pressure p* = p + (1/2)llull². As

[p0342-b0050 | ordinary-paragraph | high] s ≥ 4, the terms w grad y and Iul² belong respectively to L4/3(Ω)² and L2(Q).

[p0342-b0051 | ordinary-paragraph | high] Now consider the following problem for f in L'(Q)2:

[p0342-b0052 | ordinary-paragraph | medium] Find y e Φ, and we W1,r(Q) such that

[p0342-b0053 | equation | low] v(curl w, curl Φ) + (w grad ↓, curl Φ) = (f, curl Φ)

[p0342-b0054 | ordinary-paragraph | low] VoeΦs,

[p0342-b0055 | equation | low] (4.32a)

[p0342-b0056 | ordinary-paragraph | low] (o)MrA

[p0342-b0057 | equation | low] (curl y,curl μ) = (w,μ)

## PDF 343 / printed 329



[p0343-b0004 | ordinary-paragraph | low] ()s1M =bA  (bpe18muna - pe8 m - J) = (bpe*d pe8) (9ze't)

[p0343-b0005 | ordinary-paragraph | high] With the above notations this problem reads:

[p0343-b0006 | equation | low] F(A,u) = u + TG(,u) = 0

[p0343-b0007 | ordinary-paragraph | high] with Λ = 1/v, u = (curly,w,Ap*)e X, G defined by (4.31) and T defined by

[p0343-b0008 | ordinary-paragraph | high] (4.28).

[p0343-b0009 | ordinary-paragraph | high] Again, a routine calculation shows that if (u, p) is a solution of Problem (4.1)

[p0343-b0010 | ordinary-paragraph | high] with curl u and p in W1.r(Ω), f in L'(Q)² then the triple (curl y,w, p*) with

[p0343-b0011 | equation | low] (4.33)

[p0343-b0012 | equation | low] curly =u, curlu = ∞, p*= p + (1/2)lul|²2

[p0343-b0013 | ordinary-paragraph | high] is a solution of Problem (4.32). Conversely, each solution (curl y, w, p*) of (4.32)

[p0343-b0014 | ordinary-paragraph | high] is such that w = - 4y and the pair (u, p) defined by (4.33) satisfies (4.1). In

[p0343-b0015 | ordinary-paragraph | high] addition, when the Stokes operator has the regularity (4.18), each solution

[p0343-b0016 | ordinary-paragraph | high] u = (curl y,w, p*) of Problem (4.32) with f in L'(Ω)² for some real ye [r,2] has

[p0343-b0017 | ordinary-paragraph | high] the regularity ↓e W3,*(Ω), we W1,(Ω), p* e W1,*(Ω). Furthermore, just like in

[p0343-b0018 | remark | high] Remark 4.4, every branch of nonsingular solutions of Problem (4.1) with right-

[p0343-b0019 | ordinary-paragraph | high] hand side f in L'(Ω)² is also a branch of nonsingular solutions of Problem (4.32)

[p0343-b0020 | ordinary-paragraph | high] and conversely.

[p0343-b0021 | ordinary-paragraph | high] As far as the approximation is concerned, we assume that Q is a polygonal

[p0343-b0022 | ordinary-paragraph | high] domain of R? in order to triangulate it entirely. Then let T, be a family of

[p0343-b0023 | ordinary-paragraph | high] triangulations of Q and I > 1 a fixed integer. We take:

[p0343-b0024 | equation | low] On = {0n∈6(); 0nlx∈P VK∈h} c W1,∞(Ω),

[p0343-b0025 | equation | low] Φn = 0n NΦ = {n∈ 0n; Φnlr。 = 0,

[p0343-b0026 | equation | low] (4.34)

[p0343-b0027 | equation | low] Φlr, = an arbitrary constantc;, 1 ≤ i ≤ p},

[p0343-b0028 | equation | low] Qh = {ah∈C°(Q)n L(Ω); anlx∈P VK∈h}, k = min(1,l - 1),

[p0343-b0029 | equation | low] Xh = {curl Φh; Φn∈Dh} x Oh x Qh c X.

[p0343-b0030 | ordinary-paragraph | high] With these spaces, the Stokes problem is approximated by:

[p0343-b0031 | ordinary-paragraph | medium] Find , in Φ, and w, in O, solution of

[p0343-b0032 | equation | low] (curl wn, curl Φh) = (f, curl Φh)  VΦh,∈ Φh,

[p0343-b0033 | equation | low] (4.35a)

[p0343-b0034 | equation | low] ((curlh,curl μn) = (@h μh) μn∈Oh;

[p0343-b0035 | ordinary-paragraph | high] Find pn in Qh such that

[p0343-b0036 | equation | low] (grad ph, grad qn) = (f -- curl wh, grad qh)Vqne Qh.

[p0343-b0037 | equation | low] (4.35b)

[p0343-b0038 | ordinary-paragraph | high] The corresponding operator T,e &(Y; X,) is defined by

[p0343-b0039 | equation | low] Tf = (curl yh,wn, Ph) solution of (4.35).

[p0343-b0040 | ordinary-paragraph | high] Likewise, the Navier-Stokes problem (4.32) is discretized by:

## PDF 344 / printed 330



[p0344-b0004 | ordinary-paragraph | low] VonEΦn,

[p0344-b0005 | equation | low] v(curl @h, curl Φn) + (w grad yh, curl Φn) = (f, curl Φh)

[p0344-b0006 | equation | low] (4.36a)

[p0344-b0007 | equation | low] :"0=unA

[p0344-b0008 | equation | low] (curl yh, curl μh) = (@h, μh)

[p0344-b0009 | ordinary-paragraph | high] Find p* e Qh such that:

[p0344-b0010 | ordinary-paragraph | medium] (grad p*, grad an) = (f - Wn grad yh - vcurl wh, grad qh)  Van E Qh.

[p0344-b0011 | equation | low] (4.36b)

[p0344-b0012 | ordinary-paragraph | high] In other words, this problem can also be written as:

[p0344-b0013 | equation | low] Fh(l,un) = un + ThG(,un) = 0,

[p0344-b0014 | ordinary-paragraph | high] with X = 1/v, u, = (curl yh, wn, Ap*)e X, G defined by (4.31) and T, by (4.35).

[p0344-b0015 | ordinary-paragraph | high] Now, let us apply Theorem 3.3 with Z = Y. Recall the approximation prop-

[p0344-b0016 | ordinary-paragraph | high] erties of the operator Th, derived in Section I11.3.1 (cf. Theorem HH1.3.2). When

[p0344-b0017 | ordinary-paragraph | high] Q is a convex polygon, the Stokes problem has the regularity (4.18); in other

[p0344-b0018 | ordinary-paragraph | high] words, if f belongs to L'(Q)² with r ≤ t ≤ 2 the solution of the Stokes problem

[p0344-b0019 | ordinary-paragraph | high] (curly,w, p) belongs to W2,(Ω) x W1,(Ω) x W1,(Ω) and

[p0344-b0020 | equation | low] ly ll3,t,2 + I|wll1,t,2 + Ipl1,o ≤ C, lfllo,,2.

[p0344-b0021 | ordinary-paragraph | high] Hence, if J, is a uniformly regular family of triangulations of Ω, we have the

[p0344-b0022 | ordinary-paragraph | high] following estimates for the solution (curl h, Wn, Ph) of Problem (4.35):

[p0344-b0023 | ordinary-paragraph | low] | -- Wnl1,s,2 + Ilw - Wnllo,2 + Ilp - Pnllo,2 ≤ C2h l/fllo,t,,

[p0344-b0024 | ordinary-paragraph | high] with r ≤ t < 2, 1/y + 1/t = 1, α = 1/y when l = 1 and α = 2/y when I > 2. This

[p0344-b0025 | ordinary-paragraph | high] settles (3.37) and (3.38). Therefore the conclusion of Theorem 3.3 holds and

[p0344-b0026 | ordinary-paragraph | high] combined with Theorem IH1.3.1, it gives the next result.

[p0344-b0027 | theorem | high] Theorem 4.4. 1°) Let Ω be a bounded, convex polygon and let J, be a uniformly

[p0344-b0028 | ordinary-paragraph | high] regular family of triangulations of Q. For fe L'(Q)², te [r,2), let {(A, (curl Φ(l),

[p0344-b0029 | ordinary-paragraph | high] w(l), Ap*(a)); X = 1/ve A} be a branch of nonsingular solutions of the Navier-

[p0344-b0030 | ordinary-paragraph | high] Stokes Problem (4.32). Then for h ≤ ho small enough there exists a unique C∞

[p0344-b0031 | ordinary-paragraph | medium] branch {(,(curl,(2), wn(a), Ap*(2);  = 1/ve A} of solutions of Problem (4.36)

[p0344-b0032 | ordinary-paragraph | high] that satisfies:

[p0344-b0033 | ordinary-paragraph | medium] sup {ln(2) - y(2)l1,s, + Ilwn(2) - w(2)llo,o + Il p*(l) - p*(2)lo.s}

[p0344-b0034 | ordinary-paragraph | low] neA

[p0344-b0035 | equation | low] [1/ ifl = 1

[p0344-b0036 | equation | low] ≤ Cha with α =

[p0344-b0037 | equation | low] (4.37)

[p0344-b0038 | equation | low] (2/y ifl≥ 2,

[p0344-b0039 | ordinary-paragraph | high] 1/t + 1/y = 1 and the constant C is independent of h or Λ. This bound is still valid

[p0344-b0040 | ordinary-paragraph | high] when t = 2 and either I ≥ 2 or ↓ belongs also to W2. ∞(Q). When I = 1 and t = 2,

[p0344-b0041 | ordinary-paragraph | high] the left-hand side of (4.37) is bounded by

[p0344-b0042 | equation | low] C(e)h1/2-e  for all ε > 0.

## PDF 345 / printed 331



[p0345-b0005 | ordinary-paragraph | high] have the

[p0345-b0006 | ordinary-paragraph | high] error estimate for all A in A:

[p0345-b0007 | ordinary-paragraph | high] (4.38) WA) — WAlis.o + llon(A) — ©A)|lo.0 + PEA) — P*(A)llo,@ < Kh”.

[p0345-b0008 | ordinary-paragraph | high] Like in the linear case, it is possible to sharpen the above estimate for Wy, — w

[p0345-b0009 | ordinary-paragraph | high] in the Hj norm. However, the argument of Theorem 3.5 does not seem to apply

[p0345-b0010 | ordinary-paragraph | high] here because it would have to bear on both w and w whereas the estimate on w

[p0345-b0011 | ordinary-paragraph | high] is unlikely to be improved. Let us introduce instead a more direct duality

[p0345-b0012 | ordinary-paragraph | high] argument. Since we are not concerned by the pressure, we take

[p0345-b0013 | equation | low] X = {curl ¢; de @,} x L7(Q), H = {curld; $e} x L?(Q)

[p0345-b0014 | ordinary-paragraph | high] and we suppose that

[p0345-b0015 | equation | low] 2 — u(A) = (curl (A), w(A))

[p0345-b0016 | ordinary-paragraph | high] is a branch of nonsingular solutions of Problem (4.32a) with fe L?(Q)?. Again

[p0345-b0017 | ordinary-paragraph | high] we assume that (4.18) holds so that u(A) belongs to H*(Q) x H1(Q). To simplify

[p0345-b0018 | ordinary-paragraph | high] we denote

[p0345-b0019 | equation | low] D = D,G(A, u(A)).

[p0345-b0020 | ordinary-paragraph | high] Recall that

[p0345-b0021 | equation | low] D-v = A(o(A) grad ¢@+ Ograd(A)) Vv = (curl d, 0)eX .

[p0345-b0022 | ordinary-paragraph | high] Then we introduce the operator D* « Y(H; X’) defined by:

[p0345-b0023 | ordinary-paragraph | high] (4.39) <D*z,v> =(curly,D-v) Vz = (curly, eH.

[p0345-b0024 | ordinary-paragraph | high] To relate D and D* recall that the space V associated with X is

[p0345-b0025 | equation | low] V = {v = (curl, 0)€X ; bv.) =0 VuewW(Q)},

[p0345-b0026 | ordinary-paragraph | high] where b(v, w) = (curl ¢, curl ) — (6, 1).

[p0345-b0027 | ordinary-paragraph | high] Recall also that V is a Hilbert space for the scalar product

[p0345-b0028 | equation | low] a(u,v) =(@,0) Vu=(eurly,@), v =(curld,0)EeV

[p0345-b0029 | ordinary-paragraph | high] and that the definition of the Stokes operator can be extended to

[p0345-b0030 | equation | low] TEL(XCGV) | aiv=<lo. Vvuoev:

[p0345-b0031 | ordinary-paragraph | high] Thus it follows readily from (4.39) that

[p0345-b0032 | equation | low] a(TD*z,v) = a(TDv,z) Vz, veV.

[p0345-b0033 | ordinary-paragraph | high] In other words, TD* is the adjoint of TD in V for the scalar product a(., .). As

[p0345-b0034 | ordinary-paragraph | high] a consequence, since by assumption J + TD is an isomorphism of V, then

[p0345-b0035 | ordinary-paragraph | high] I + TD* is also an isomorphism of V.

## PDF 346 / printed 332



[p0346-b0004 | equation | low] For g = ge L²(Q)² find z = (curl x, μ)e V such that:

[p0346-b0005 | equation | low] a((I + TD*)z,v) = (g,curl Φ)  Vu = (curlΦ,0)e V;

[p0346-b0006 | equation | low] (4.40)

[p0346-b0007 | equation | low] z = (I + TD*)-1 Tg.

[p0346-b0008 | ordinary-paragraph | high] i.e.

[p0346-b0009 | lemma | high] Lemma 4.1. Let Q be a bounded, Lipschitz-continuous domain of R² and suppose

[p0346-b0010 | ordinary-paragraph | high] the Stokes problem has the regularity (4.18). Then the solution z = (curl x,μ) of

[p0346-b0011 | ordinary-paragraph | high] Problem (4.40) belongs to H²(Q) x H'(Q2) with

[p0346-b0012 | equation | low] Ixll3,o + Il μlli,2 ≤ C{1 + A(lly(2)ll3,2 + I/∞(2)ll1,o)} Ilgllo,

[p0346-b0013 | equation | low] (4.41)

[p0346-b0014 | proof | high] Proof. First, it stems from (4.40) that

[p0346-b0015 | equation | low] II zllx ≤ C1 llgllo.s.

[p0346-b0016 | equation | low] (4.42)

[p0346-b0017 | ordinary-paragraph | high] Next we know from Lemma IIl.2.1 that all functions v = (curl Φ, 0)e V satisfy:

[p0346-b0018 | equation | low] curlΦ∈ H(Ω), 0 = -- 4Φ, ll0llo,o = |ul ≤ llullx.

[p0346-b0019 | ordinary-paragraph | high] Therefore

[p0346-b0020 | ordinary-paragraph | low] A3aA

[p0346-b0021 | equation | low] (D*z,v) = X(curl x, @()grad Φ - AΦ grad y())

[p0346-b0022 | equation | low] = (curl(curl x : grad y(2)) - w(2) grad x, curl Φ).

[p0346-b0023 | ordinary-paragraph | high] Thus D* z can be written in the form

[p0346-b0024 | equation | low] A =() = aA

[p0346-b0025 | equation | low] (D*z,v> = (l, curlΦ)

[p0346-b0026 | ordinary-paragraph | high] where, in view of the regularity of u(2) and Sobolev's Imbedding Theorem I.1.3,

[p0346-b0027 | ordinary-paragraph | medium] le L²(Ω)² with

[p0346-b0028 | equation | low] IIllo,2 ≤ C2A(llw(a)ll1.2 + I y(2)ll3.o) lxll 2.2,

[p0346-b0029 | equation | low] ≤ CA(ll∞(a) ll 1, + Il(2) ll3.2) Ilg llo.o,

[p0346-b0030 | ordinary-paragraph | high] since ze V and satisfies (4.42). Then (4.41) follows from this last inequality, the

[p0346-b0031 | ordinary-paragraph | high] regularity assumption (4.18) and the fact that z can also be expressed as z =

[p0346-b0032 | ordinary-paragraph | high] T(g - D* z).

[p0346-b0033 | ordinary-paragraph | high] 口

[p0346-b0034 | theorem | high] Theorem 4.5. Let Q and J, be like in Theorem 4.4 and suppose that the Navier-

[p0346-b0035 | ordinary-paragraph | high] Stokes Problem (4.42) has a branch of nonsingular solutions such that the mapping

[p0346-b0036 | ordinary-paragraph | medium]  → y(2) is continuous from A into Hi+1(Q) when l ≥ 2 or H?(Q) when l = 1. Then

[p0346-b0037 | ordinary-paragraph | high] we have the following estimate for all X in A:

[p0346-b0038 | equation | low] Ch' ifl≥2,

[p0346-b0039 | equation | low] [y(2) -h(2)l1,0 ≤<

[p0346-b0040 | equation | low] (4.43)

[p0346-b0041 | equation | low] (C2(e)h1- if l = 1 Ve > 0,

[p0346-b0042 | ordinary-paragraph | high] with constants independent of h and X.

## PDF 347 / printed 333



[p0347-b0004 | ordinary-paragraph | high] sponding solution of the linearized problem (4.40):

[p0347-b0005 | equation | low] (g, curl Φ) = a(z,u) + (curl x, D · v) + b(v, v) Vu = (curl Φ, 0)e X.

[p0347-b0006 | ordinary-paragraph | high] In particular (dropping for the moment the parameter A):

[p0347-b0007 | ordinary-paragraph | medium] (4.44) (g, curl(y - Vn)) = a(z,u - un) + (curl x, D·(u -- un)) + b(u - uh, v).

[p0347-b0008 | ordinary-paragraph | high] But we infer from (4.32a) and (4.36a) that u - u, satisfies:

[p0347-b0009 | equation | low] (4.45)

[p0347-b0010 | equation | low] a(u—un,zh) + b(zh,@) =-(G(1,u) - G(,un),curl xh)

[p0347-b0011 | ordinary-paragraph | medium] for every Zh = (curl Xh, vh)e Vh with

[p0347-b0012 | equation | low] Vh = {Un = (curl on, On); Φn∈Φn, On∈ On, b(Un μn) = 0 Vμn∈ On}.

[p0347-b0013 | ordinary-paragraph | high] Therefore, combining (4.44) and (4.45) and using the fact that u and z belong to

[p0347-b0014 | ordinary-paragraph | high] V and u, and z, belong to V, we obtain:

[p0347-b0015 | equation | low] (g,curl(y - n)) = a(z - Zhsu - un) + (curl(x - Xn),D·(u- uh))

[p0347-b0016 | ordinary-paragraph | low] +b(u—un,v-On)+b(z-—Zh(-μn)

[p0347-b0017 | equation | low] + (curl xh,D·(u - un) - (G(1,u) - G(l,un)))

[p0347-b0018 | ordinary-paragraph | low] VZh∈ Vh,  Vμn, On∈Oh.

[p0347-b0019 | ordinary-paragraph | high] Let us choose O, = P,v and μ, = Phw; formula (A.25) gives for all Φh, one Φh:

[p0347-b0020 | ordinary-paragraph | low] (a"d -a “μ - m) - (a"d - a)μuno( - p)μn) =(θ - a“n - n)q

[p0347-b0021 | ordinary-paragraph | low] ("d - m - a) - ((od - m)[μn(g - x)μn) = (μn - m4z - z)g

[p0347-b0022 | ordinary-paragraph | high] On the other hand, Taylor's formula (3.52) yields here:

[p0347-b0023 | ordinary-paragraph | low] ("n - n)·Da(/1)- = (n - n).(n)"a -(μn) - (n“)

[p0347-b0024 | equation | low] = -A(∞ - wn)grad(y - h).

[p0347-b0025 | ordinary-paragraph | medium] Hence for all z, e Vh, Φ, and S, e Φh, we have:

[p0347-b0026 | ordinary-paragraph | medium] (g,curl(y -h)) =a(z - Zh,u - un) + A(curl(x - Xh),wgrad(y - Wh))

[p0347-b0027 | equation | low] + X(curl(x - xh),(@ - wn)grad y)

[p0347-b0028 | equation | low] (4.46)

[p0347-b0029 | equation | low] + A(curl xh,(@ - Wn)grad(y - h))

[p0347-b0030 | ordinary-paragraph | low] (4'd - A"∞ - ∞) - ((ad - 4)n( - p)μn) +

[p0347-b0031 | ordinary-paragraph | low] (d - m" - 4) - ((o"d - m)μn("g - x)μn) +

[p0347-b0032 | ordinary-paragraph | high] from which we readily infer that

## PDF 348 / printed 334



[p0348-b0003 | ordinary-paragraph | high] + Alxnlia.al¥ — Walt,a.a + lly — Prvllo,a)

[p0348-b0004 | ordinary-paragraph | high] + Alul|W — Wilr,a.alx — Xnli,4,0

[p0348-b0005 | ordinary-paragraph | high] (4.47) + |v — Pyvlya— lbr¥lt ,o

[p0348-b0006 | ordinary-paragraph | high] + 1X — Oli, 010 — Peli. o

[p0348-b0007 | ordinary-paragraph | high] + |z — 2,|||0 — P,ollo,o

[p0348-b0008 | ordinary-paragraph | high] VznEV, Vn One D-

[p0348-b0009 | ordinary-paragraph | high] Finally, recall that (cf. Lemma III.3.3 and Remark III.3.2):

[p0348-b0010 | ordinary-paragraph | high] eee ie)

[p0348-b0011 | equation | low] inf ||z—z,|lx< C,Qh?*I[ylls,0 i: fl=1 Ve>0;

[p0348-b0012 | ordinary-paragraph | high] ZnhEVy,

[p0348-b0013 | ordinary-paragraph | high] on the other hand,

[p0348-b0014 | equation | low] inf |x — Opl1,e < C3h"|Wlati1,9 with « = mini, 2);

[p0348-b0015 | ordinary-paragraph | high] one Py,

[p0348-b0016 | ordinary-paragraph | high] and likewise:

[p0348-b0017 | equation | low] inf |W — Prli.a < Cyh'|Wlist.a;

[p0348-b0018 | ordinary-paragraph | high] ne Py,

[p0348-b0019 | equation | low] lo — P,@llo.g + hla — Proly.e < Csh*lol.o

[p0348-b0020 | ordinary-paragraph | high] with B = 1 when / = 1 and B =! — 1 when! > 2. By substituting these bounds

[p0348-b0021 | ordinary-paragraph | high] into (4.47) and applying Theorem 4.4 and Lemma 4.1 we easily derive (4.43). 1

[p0348-b0022 | subsection | high] 4.4. Remarks on the “Stream Function-Gradient of Velocity Tensor” Scheme

[p0348-b0023 | ordinary-paragraph | high] With minor modifications, the approach of Section 4.3 can be applied to the

[p0348-b0024 | ordinary-paragraph | high] “stream function-gradient of velocity tensor” method for the Navier-Stokes

[p0348-b0025 | ordinary-paragraph | high] equations, at least when Q2 is a plane, convex polygon. Going back to Paragraph

[p0348-b0026 | ordinary-paragraph | high] 4, Chapter III, recall the bilinear forms:

[p0348-b0027 | ordinary-paragraph | high] a,(o, T) — \0 ;;7;; dX,

[p0348-b0028 | ordinary-paragraph | high] Q

[p0348-b0029 | equation | low] b(.é)=- ¥. |1 ,,(02/0x,0x,) dx + | M,,(t)S(6@/6nd)s ,

[p0348-b0030 | ordinary-paragraph | high] KeTy

[p0348-b0031 | ordinary-paragraph | high] K qT,

[p0348-b0032 | ordinary-paragraph | high] and the spaces

[p0348-b0033 | equation | low] = {c= (0e L)7(Q) *) to = th cee Wk) eee

[p0348-b0034 | ordinary-paragraph | high] M,(t) is continuous on each segment of J;,},

## PDF 349 / printed 335



[p0349-b0005 | equation | low] Tf = u = (o,y)e ≤ x y,

[p0349-b0006 | equation | low] bn(o,Φ) = -(f,curlΦ)  VΦ∈ ,

[p0349-b0007 | equation | low] an(o,t) + bn(t,↓) = O  Vt∈.

[p0349-b0008 | ordinary-paragraph | medium] Setting

[p0349-b0009 | equation | low] Y = L'(Ω)²,

[p0349-b0010 | equation | low] X = {o = (0)∈ L²(Ω)4; 012 = 021} x Φs,

[p0349-b0011 | ordinary-paragraph | medium] we have

[p0349-b0012 | ordinary-paragraph | medium] Te E(Y; X)

[p0349-b0013 | ordinary-paragraph | medium] and since the Stokes problem is regular we also have

[p0349-b0014 | ordinary-paragraph | low] Te &(Y; W1,r(Q)4 x W3.r(Q).

[p0349-b0015 | ordinary-paragraph | medium] In view of (4.31) we introduce the nonlinear convection term by:

[p0349-b0016 | equation | low] G(l,u) = -A(tr(o)grady + f)

[p0349-b0017 | ordinary-paragraph | medium] which is a C∞-mapping from A x X into L'(Q)2. With these notations, the

[p0349-b0018 | ordinary-paragraph | medium] Navier-Stokes equations take the standard form:

[p0349-b0019 | equation | low] u(2)∈ X,  F(,u(2)) = u(2) + TG(,u(2) = 0

[p0349-b0020 | equation | low] (4.48)

[p0349-b0021 | ordinary-paragraph | low] O IeA.

[p0349-b0022 | ordinary-paragraph | medium] As far as the approximation is concerned, we take

[p0349-b0023 | equation | low] Xh = Eh x Φh C X,

[p0349-b0024 | ordinary-paragraph | medium] where

[p0349-b0025 | equation | low] Eh = {π∈; tlx∈Pi, VK∈h},

[p0349-b0026 | equation | low] Dh ={Φ∈Φ; Φlk∈P VK∈gh}

[p0349-b0027 | ordinary-paragraph | medium] for some integer I ≥ 1. The Stokes operator is discretized by

[p0349-b0028 | equation | low] Tf = uh = (oh,Vh)e Xh,

[p0349-b0029 | equation | low] bn(oh, Φn) = --(f, curl Φn)

[p0349-b0030 | equation | low] Vun = (th Φn)∈Xh;

[p0349-b0031 | equation | low] an(Ohth)+bn(tn,↓n)=0

[p0349-b0032 | ordinary-paragraph | medium] and the Navier-Stokes equations are approximated by:

[p0349-b0033 | equation | low] un(a)eXn,  Fn(l,un(a)) = un(2) + ThG(n,un(a)) = 0  A∈ A.

[p0349-b0034 | equation | low] (4.49)

[p0349-b0035 | ordinary-paragraph | medium] The results of Section IHl.4.3 give the following estimate for T -- T:

[p0349-b0036 | equation | low] I(T - T)fllx = Iα - onllo,2 + I - hl1,s,2
