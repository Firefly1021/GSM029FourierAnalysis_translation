# Restored-source review candidate: chapter-04-section-05



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 350 / printed 336



[p0350-b0004 | equation | low] |u (A) — u,(A)l x< Che

[p0350-b0005 | ordinary-paragraph | high] provided (A) H**?(Q) for some ke [1,1].

[p0350-b0006 | ordinary-paragraph | high] Finally if w(A)e H'*1(Q) when | > 2 or W(A)e H?(Q) when | = 1, a duality

[p0350-b0007 | ordinary-paragraph | high] argument similar to that of Theorem 4.5 yields the optimal estimate:

[p0350-b0008 | equation | low] WA) — WlAlio < Ch’.

[p0350-b0009 | ordinary-paragraph | high] By applying the material of Section 1.4.4, we can derive error bounds of the

[p0350-b0010 | ordinary-paragraph | high] same order for the pressure.

[p0350-b0011 | ordinary-paragraph | high] The proofs are left as exercises.

[p0350-b0012 | section | high] §5. Numerical Analysis of Upwind Schemes

[p0350-b0013 | ordinary-paragraph | high] When the viscosity v is small, or equivalently when the Reynolds number Re is

[p0350-b0014 | ordinary-paragraph | high] large compared to the other parameters of the fluid, there arises a boundary layer

[p0350-b0015 | ordinary-paragraph | high] in the neighborhood of I’ where the viscosity predominates while it is negligible

[p0350-b0016 | ordinary-paragraph | high] in the interior of 2. At the same time, the flow becomes turbulent. Thus the

[p0350-b0017 | ordinary-paragraph | high] solutions of the Navier-Stokes equations are seriously discontinuous at high

[p0350-b0018 | ordinary-paragraph | high] Reynolds number.

[p0350-b0019 | ordinary-paragraph | high] It is not our purpose here to modelize turbulent flows, but all the same, it is

[p0350-b0020 | ordinary-paragraph | high] worthwhile to examine one possible discretization of discontinuous solutions of

[p0350-b0021 | ordinary-paragraph | high] the Navier-Stokes equations. Instead of the centered schemes studied so far, we

[p0350-b0022 | ordinary-paragraph | high] propose upwind schemes which are better adapted to describe discontinuous

[p0350-b0023 | ordinary-paragraph | high] flows. The forthcoming analysis shows that these schemes are nearly optimal.

[p0350-b0024 | ordinary-paragraph | high] The reader can also refer to Johnson & Saranen [47] for an alternate method,

[p0350-b0025 | ordinary-paragraph | high] the streamline diffusion method, that applies to Euler and Navier-Stokes equa-

[p0350-b0026 | ordinary-paragraph | high] tions.

[p0350-b0027 | subsection | high] 5.1. Upwinding in the Stream Function-Vorticity Scheme

[p0350-b0028 | ordinary-paragraph | high] The upwind scheme discussed in this section was developed by Fortin [31],

[p0350-b0029 | ordinary-paragraph | high] inspired by a numerical method advocated in Lesaint & Raviart [51] to solve a

[p0350-b0030 | ordinary-paragraph | high] neutron transport equation. It stems from the following heuristic remarks. When

[p0350-b0031 | ordinary-paragraph | high] a smooth vector field u is divergence-free, the convection term satisfies (with the

[p0350-b0032 | ordinary-paragraph | high] usual summation convention that a repeated index represents a sum):

[p0350-b0033 | equation | low] uj(Ou;,/Ox;) = O(uju;)/Ox;.

[p0350-b0034 | ordinary-paragraph | high] Now, suppose {2 is the union of two bounded regions Q, and Q, separated by

[p0350-b0035 | ordinary-paragraph | high] an interface S like in Figure 21. Denote by I’ the boundary of Q and by n, the

## PDF 351 / printed 337



[p0351-b0002 | figure | high] Figure 21

[p0351-b0003 | ordinary-paragraph | high] unit exterior normal to Q; on S. Assume that the vector field u is no longer

[p0351-b0004 | ordinary-paragraph | high] globally smooth in Q but that instead,

[p0351-b0005 | ordinary-paragraph | high] ulo, €H'(Q,)", ulp=0, ueH(div;Q) and divu=0.

[p0351-b0006 | ordinary-paragraph | high] Then the product uj;u; is no longer differentiable in Q but its distributional

[p0351-b0007 | ordinary-paragraph | high] derivative has the form:

[p0351-b0008 | ordinary-paragraph | high] [o(uju;)/Ox;] = O(u;u;)/Ox;le, ua,

[p0351-b0009 | ordinary-paragraph | high] + a surface distribution corresponding to the jump of the field

[p0351-b0010 | ordinary-paragraph | high] u across the interface S, namely:

[p0351-b0011 | ordinary-paragraph | high] u-n(ur — uj") ds

[p0351-b0012 | ordinary-paragraph | high] where n and the notions of exterior and interior refer to the same region. The

[p0351-b0013 | ordinary-paragraph | high] upwinding relies on the following principle:

[p0351-b0014 | ordinary-paragraph | high] the flow in Q, depends exclusively upon the flux entering through S.

[p0351-b0015 | ordinary-paragraph | high] By virtue of this principle, we introduce the notation:

[p0351-b0016 | ordinary-paragraph | high] (3:8) 6_Q, = {x eS; u-n,(x) < 0}

[p0351-b0017 | ordinary-paragraph | high] for the portion of the interface S where the fluid enters 2, and we take as a

[p0351-b0018 | definition | high] definition the following expression for the convection term:

[p0351-b0019 | ordinary-paragraph | high] |u ;(Ou,/Ox,)v; dx

[p0351-b0020 | equation | low] =

[p0351-b0021 | ordinary-paragraph | high] (4)

[p0351-b0022 | ordinary-paragraph | high] 7) 2

[p0351-b0023 | ordinary-paragraph | high] ay u,(du;/0x;)v;dx + u-n,(ue” — uj")vi" ds

[p0351-b0024 | equation | low] k=1 )0, k=1 J0_Q,

[p0351-b0025 | ordinary-paragraph | high] for all u in H(div; Q) with divu = 0, ulg € H'(Q,)" and vio, € H'(Q,)”. Clearly,

[p0351-b0026 | ordinary-paragraph | high] when u and v belong to H'(Q), the surface term vanishes and we recover the

[p0351-b0027 | ordinary-paragraph | high] familiar expression for the convection. But when u and v are not globally in H'

[p0351-b0028 | ordinary-paragraph | high] we have to interpret (5.2) as a definition.

## PDF 352 / printed 338



[p0352-b0003 | ordinary-paragraph | high] gulated, each triangle being considered as a subregion of 2. But, beforehand, let

[p0352-b0004 | ordinary-paragraph | high] us recall the setting of the stream function-vorticity formulation and approxima-

[p0352-b0005 | ordinary-paragraph | high] tion of the Navier-Stokes system developed in Section 4.3.

[p0352-b0006 | ordinary-paragraph | high] Let Q be a bounded domain in R* with a polygonal boundary J, so that it

[p0352-b0007 | ordinary-paragraph | high] can be entirely triangulated and suppose Q is convex so the regularity condition

[p0352-b0008 | ordinary-paragraph | high] (4.18) holds. To simplify the discussion we agree to drop the pressure for the

[p0352-b0009 | ordinary-paragraph | high] moment and consider only the stream function and vorticity. Then we set

[p0352-b0010 | equation | low] Y=L(Q), XxX = {curl¢; de®.) <x L7(Q)

[p0352-b0011 | ordinary-paragraph | high] with s > 4.and 1/r + 1/s = 1. The Stokes operator Te L(Y;X ) is defined by

[p0352-b0012 | equation | low] Tf = (curly,@) where

[p0352-b0013 | ordinary-paragraph | high] ae te w, curl ¢) = (f,curld) Vde®,,

[p0352-b0014 | equation | low] (curl wy, curl yw) = (@,n) VueW?"(Q),

[p0352-b0015 | ordinary-paragraph | high] where w and w are related to the velocity u by

[p0352-b0016 | ordinary-paragraph | high] (5.4) u=curly and mw =curlu.

[p0352-b0017 | ordinary-paragraph | high] As usual, we introduce the subspace of X

[p0352-b0018 | ordinary-paragraph | high] (5.5) V = {(curl ¢, 0) eX; 6€ HG (Q), 0 = — Ad},

[p0352-b0019 | ordinary-paragraph | high] (has only one connected component since 92 is convex) and we know from

[p0352-b0020 | lemma | high] Lemma III.2.1 that Te Y(Y; V).

[p0352-b0021 | equation | low] The nonlinearity is expressed much like in (4.31):

[p0352-b0022 | ordinary-paragraph | high] (5.6) G(u) =q@gradW —f u=(curly,a@)eX.

[p0352-b0023 | ordinary-paragraph | high] Then the Navier-Stokes problem is stated like in (4.32):

[p0352-b0024 | equation | low] For f in L'(Q) find u = (curl, @)e X such that:

[p0352-b0025 | ordinary-paragraph | high] 65.7) ps co, curl ) + (@ grad w, curl ¢) = (f,curld) Vde®,,

[p0352-b0026 | equation | low] (curl y, curl w) = (@,u) Vue W'(Q),

[p0352-b0027 | ordinary-paragraph | high] where w and w are related to u by (5.4). With T and G defined above and 4 = 1/y,

[p0352-b0028 | ordinary-paragraph | high] this has the compact expression:

[p0352-b0029 | ordinary-paragraph | high] (5.8) F(A,u) =u + ATG(u) = 0.

[p0352-b0030 | ordinary-paragraph | high] For the purpose of the approximation, we introduce the first two finite-

[p0352-b0031 | ordinary-paragraph | high] dimensional spaces 9, and @, defined by (4.34):

[p0352-b0032 | equation | low] O, = {0,6 @°(Q); O,|,EP, VWKEF,}, &, = 0, H4(Q),

[p0352-b0033 | ordinary-paragraph | high] where 7, is a triangulation of Q and the integer | > 1. Naturally we take

[p0352-b0034 | equation | low] X, = {cur¢l, ; ¢,¢€D,} x O, < X

## PDF 353 / printed 339



[p0353-b0003 | ordinary-paragraph | high] (59) V, = {(curl ¢,, ,,)€X;,; (curl g,, curl ,) = (9, H,) Vay € O,}.

[p0353-b0004 | ordinary-paragraph | high] The discrete Stokes operator can be defined on a wider space than Y, namely:

[p0353-b0005 | equation | low] Y, = the dual space of {curl ¢,; 4, € ®,|

[p0353-b0006 | ordinary-paragraph | high] equipped with the norm

[p0353-b0007 | equation | low] Il, = sup Se

[p0353-b0008 | ordinary-paragraph | high] drne®, |Puli.s,@

[p0353-b0009 | ordinary-paragraph | high] By setting

[p0353-b0010 | equation | low] <l,u,> = <Leurlg,> Vv, = (curl ¢,, 4,)€ V,,,

[p0353-b0011 | ordinary-paragraph | high] the space Y, can also be identified with a subspace of V,, the dual space of V,;

[p0353-b0012 | ordinary-paragraph | high] thus we have the following continuous imbeddings:

[p0353-b0013 | ordinary-paragraph | high] VE eanF acerWi ne

[p0353-b0014 | ordinary-paragraph | high] It will be useful further on to provide Y, with the norm of V;, i.e. we put

[p0353-b0015 | ordinary-paragraph | high] Lv

[p0353-b0016 | equation | low] l/l,= sup TY, Vle Y,;

[p0353-b0017 | ordinary-paragraph | high] v,€ Vy, ll On llx

[p0353-b0018 | ordinary-paragraph | high] clearly we have:

[p0353-b0019 | equation | low] ln SWE, = Ve Y,.

[p0353-b0020 | ordinary-paragraph | high] Then we define the approximate Stokes operator T),¢ (Y,; X;,) by:

[p0353-b0021 | ordinary-paragraph | high] For le Y,, find T,! = (curl ,, @,)€ X ;, solution of

[p0353-b0022 | equation | low] (curl w,, curl d,) = <l,curl¢d,> Vo,E%,,

[p0353-b0023 | equation | low] (5.10)

[p0353-b0024 | equation | low] (curl y,, curl p1;,) = (©), Hn) Ven € Op.

[p0353-b0025 | ordinary-paragraph | high] Obviously the range of the operator T,, is the space V,,.

[p0353-b0026 | ordinary-paragraph | high] Now we turn to the upwind discretization of the convection term. Consider-

[p0353-b0027 | ordinary-paragraph | high] ing that Q is the union of all the triangles « of %,, formula (5.2) can be generalized

[p0353-b0028 | ordinary-paragraph | high] to yield the following definition:

[p0353-b0029 | ordinary-paragraph | high] u,(du;/0x;)v, dx

[p0353-b0030 | equation | low] (5.11)

[p0353-b0031 | ordinary-paragraph | high] » ‘|u j(du,/0x;)v;dx + ig ue n(uer — yint)pint ish

[p0353-b0032 | ordinary-paragraph | high] KET,

[p0353-b0033 | ordinary-paragraph | high] This induces us to split the convection term and replace the single trilinear form

[p0353-b0034 | ordinary-paragraph | high] by two forms: one for the volume integrals and one for the line integrals. Thus

[p0353-b0035 | ordinary-paragraph | high] for all u = (curly, @) and v = (curl ¢, 0) in X, and all w of the form w; = 0%/0x;

[p0353-b0036 | ordinary-paragraph | high] with x in ®, we set:

## PDF 354 / printed 340



[p0354-b0003 | ordinary-paragraph | high] KET, JK

[p0354-b0004 | ordinary-paragraph | high] where u = curly and v = curl ¢; likewise for z = (curl v, ) in X;, we take:

[p0354-b0005 | ordinary-paragraph | high] (5.13) atei.w) = >, | u-n(ve*t — vit')wit" ds,

[p0354-b0006 | ordinary-paragraph | high] KET), J 0_K(z)

[p0354-b0007 | ordinary-paragraph | high] where n denotes always the unit exterior normal to x, the superscript ext (resp.

[p0354-b0008 | ordinary-paragraph | high] int) denotes the external (resp. internal) trace of the function on the boundary of

[p0354-b0009 | ordinary-paragraph | high] kK and

[p0354-b0010 | ordinary-paragraph | high] (5.14) O_K(z) = {xe 0k; (z:n)(x) <0}, z=curly,

[p0354-b0011 | ordinary-paragraph | high] ie. 0_xk(z) is the portion of the boundary of x where the fluid with velocity z

[p0354-b0012 | ordinary-paragraph | high] enters x. Finally, we introduce the form

[p0354-b0013 | ordinary-paragraph | high] (5:85) a7 (u; v, W) = a,(u;v, w) + a5(u; v, W)

[p0354-b0014 | ordinary-paragraph | high] and we define the mapping G,: ve X, > G,(v)e Y, by

[p0354-b0015 | ordinary-paragraph | high] (5.16) <G,(v), curly > = a°(v; v, curl y) — (f,curly) VyeE®,.

[p0354-b0016 | ordinary-paragraph | high] The continuity of G, will be established subsequently, but right away we observe

[p0354-b0017 | ordinary-paragraph | high] that owing to the dependence of a3(v;v,w) on 0_x(v) the mapping G, is not

[p0354-b0018 | ordinary-paragraph | high] differentiable. Note that when we H'!(Q)? the form a satisfies the crucial property

[p0354-b0019 | ordinary-paragraph | high] justifying definition (5.11):

[p0354-b0020 | ordinary-paragraph | high] (5:17) a”(u; v, W) = -| u;(Ow;/0x;)v; dx,

[p0354-b0021 | ordinary-paragraph | high] whatever the function z, provided of course divu = 0 in Q andu-n=OonT.

[p0354-b0022 | ordinary-paragraph | high] Then the Navier-Stokes Problem (5.7) has the following upwind discretization:

[p0354-b0023 | ordinary-paragraph | high] Find ,€ ®, and w, € ©, solution of

[p0354-b0024 | ordinary-paragraph | high] Bai ee ,, curl @,) + G""(u,;u,, curl g,) = (f,curld,) Vd,e®,,

[p0354-b0025 | equation | low] (curl y,, curl ,) = (@,,4,) Viun,€9,,

[p0354-b0026 | ordinary-paragraph | high] with a defined by (5.12)-(5.15). Keeping in mind the above notations, this

[p0354-b0027 | ordinary-paragraph | high] problem takes the form of( 3.58):

[p0354-b0028 | ordinary-paragraph | high] (5.19) F(A, Uy) = Uy + AT, Ga(un) = 9,

[p0354-b0029 | ordinary-paragraph | high] where u, = (curl y,,,) and 2 = 1/v. Note that F, maps A x X, into J,.

[p0354-b0030 | subsection | high] 5.2. Error Analysis of the Upwind Scheme

[p0354-b0031 | ordinary-paragraph | high] Before applying the material of Section 3.4 to establish the convergence of (5.18),

[p0354-b0032 | ordinary-paragraph | high] let us prove some important properties of the form G(.; ., .). The reader will find

[p0354-b0033 | ordinary-paragraph | high] that this form is not as hard to manipulate as it would seem at first sight. First,

## PDF 355 / printed 341



[p0355-b0005 | ordinary-paragraph | high] the seminorm

[p0355-b0006 | ordinary-paragraph | high] 1/2

[p0355-b0007 | ordinary-paragraph | high] (5 68.

[p0355-b0008 | ordinary-paragraph | high] Ke ZT,

[p0355-b0009 | ordinary-paragraph | high] This is precisely the purpose of the space V,: it was shown in Chapter III that,

[p0355-b0010 | ordinary-paragraph | high] under adequate conditions, the functions of V, satisfy the uniform stability

[p0355-b0011 | ordinary-paragraph | high] properties:

[p0355-b0012 | ordinary-paragraph | high] (5.20) |@rlisa2<GMArllo.g (cf. (11L.2.41)) Vu,= (curl ¢,, 4,)€ V,,

[p0355-b0013 | ordinary-paragraph | high] (5.21) (= Bx) <C|l,llo,a (ef. (HI.2.65))

[p0355-b0014 | ordinary-paragraph | high] with constants independent of h. In other words:

[p0355-b0015 | ordinary-paragraph | high] the seminorm of X: |v;| = ||9 ,\lo,q is anorm on V, uniformly equivalent to both

[p0355-b0016 | ordinary-paragraph | high] IPrlr.a+ IlPrllo,@ and (» Prl3, a + ||@rllo,o for each t > 2.

[p0355-b0017 | ordinary-paragraph | high] This suggests to adopt the following mesh-dependent norms:

[p0355-b0018 | ordinary-paragraph | high] (5.22) [¢]. = (y l, Je ee ee.

[p0355-b0019 | ordinary-paragraph | high] Next, since the functions ofX have little regularity, it will sometimes be useful

[p0355-b0020 | ordinary-paragraph | high] to work with the following smoothing operator:

[p0355-b0021 | equation | low] Pe £(X; {curl¢ ; 6e H?(Q)N HG(Q)} x L?(Q))

[p0355-b0022 | ordinary-paragraph | high] defined by

[p0355-b0023 | ordinary-paragraph | high] for u = (curl y, m)e€ X, Pu = (curl ¢, «) is the solution of the Dirichlet problem

[p0355-b0024 | ordinary-paragraph | high] (5.23) —Ad=a@ inQ, ¢=0 onl.

[p0355-b0025 | ordinary-paragraph | high] When @ is convex, this function ¢ belongs indeed to H?(Q) and

[p0355-b0026 | ordinary-paragraph | high] (5.24) IP llo,0< Cllllo,a-

[p0355-b0027 | ordinary-paragraph | high] Clearly, the operator P reduces to the identity mapping on V. Moreover, when

[p0355-b0028 | ordinary-paragraph | high] u, = (curl y,, @,) belongs to V, the corresponding function ¢ coincides with the

[p0355-b0029 | ordinary-paragraph | high] function (h) introduced in the proof of Lemma III.2.5. In other words, u, =

[p0355-b0030 | ordinary-paragraph | high] (curl y,,,@,)€V, and Pu,= (curl ¢, @,) are related by

[p0355-b0031 | ordinary-paragraph | high] Wr re P,

[p0355-b0032 | ordinary-paragraph | high] the H-projection on ®, defined by (A.24):

[p0355-b0033 | ordinary-paragraph | high] (5.25) (curl(P,¢ — ¢),curlw,)=0 Wu, e® ,,.

[p0355-b0034 | ordinary-paragraph | high] The next lemma gives a useful estimate for [¢ — P,d|i-

## PDF 356 / printed 342



[p0356-b0005 | ordinary-paragraph | medium] k with 1 ≤ k ≤ l. Then we have the estimate:

[p0356-b0006 | equation | low] [Φ- Ph] ≤ C,hk-1 11llk+1,α

[p0356-b0007 | equation | low] Vt ≥ 2,

[p0356-b0008 | equation | low] (5.26)

[p0356-b0009 | ordinary-paragraph | medium] with constants C, independent of h.

[p0356-b0010 | ordinary-paragraph | medium] This lemma is an easy consequence of Theorem A.2 and

[p0356-b0011 | equation | low] [Φn]t ≤ C(t)h-1/Φnl1,s

[p0356-b0012 | ordinary-paragraph | low] ""中A

[p0356-b0013 | equation | low] (5.27)

[p0356-b0014 | ordinary-paragraph | medium] These preliminaries permit to derive some fundamental properties of a( .; ., . ).

[p0356-b0015 | ordinary-paragraph | medium] First a(.; ., .) is bounded.

[p0356-b0016 | lemma | medium] Lemma 5.2. Let us retain the assumptions of Lemma 5.1. The form a(.; ., .) is

[p0356-b0017 | ordinary-paragraph | medium] bounded as follows, for all vhe Vh and all zh, uh = (u, = curl yh, wn), wh = (wh =

[p0356-b0018 | ordinary-paragraph | medium] curl xh, &n)e Xh:

[p0356-b0019 | equation | low] 1a(un; Un, Wn) / + Ia²h(un; Uh, Wh)/ ≤ C l/un llo,4,2lUnl // wn1lo,4,2

[p0356-b0020 | equation | low] (5.28)

[p0356-b0021 | proof | medium] Proof. Let v, = (curl Φ,, O,) belong to V. By Holder's inequality, we have:

[p0356-b0022 | ordinary-paragraph | medium] 1/2

[p0356-b0023 | equation | low] [a(un; Uh, Wn)/ ≤ C1 14hl1,4,0/Xnl1,4,0

[p0356-b0024 | equation | low] ∑ 1hl2,x

[p0356-b0025 | ordinary-paragraph | low] KETn

[p0356-b0026 | ordinary-paragraph | medium] Thus (5.21) gives:

[p0356-b0027 | equation | low] [a1 (un; Un, Wh)| ≤ C2 ll u, llo,4,2lunl / wh llo,4,Q.

[p0356-b0028 | ordinary-paragraph | medium] Next, consider a2h(un; Pvh, wh) with Pv, = (curlΦ, On). As Φ belongs to H?(Ω),

[p0356-b0029 | ordinary-paragraph | medium] the surface integrals in a2(.; ., .) vanish over all interior segments k' of J, and

[p0356-b0030 | ordinary-paragraph | medium] since u, belongs to X, the factor curl y, · n vanishes on all boundary segments of

[p0356-b0031 | ordinary-paragraph | medium] J,. Hence

[p0356-b0032 | equation | low] (5.29)

[p0356-b0033 | equation | low] a²h(un; Pun, Wn) = 0,

[p0356-b0034 | ordinary-paragraph | medium] so that

[p0356-b0035 | equation | low] [a²n(un;Un,Wn)/ = |a²n(un;Un —Puh,Wh)l.

[p0356-b0036 | ordinary-paragraph | medium] Therefore

[p0356-b0037 | ordinary-paragraph | medium] 1/4

[p0356-b0038 | equation | low] ∑_ Ilcurl ynll6,4,0ox

[p0356-b0039 | equation | low] [a²n(un;Uh,Wn)/ ≤ C3

[p0356-b0040 | ordinary-paragraph | low] KETn

[p0356-b0041 | ordinary-paragraph | medium] 1/2

[p0356-b0042 | equation | low] Il curl xll0 4.0x

[p0356-b0043 | ordinary-paragraph | low] ∑ IIcurl(Φn -~ Φ)16,0x 

[p0356-b0044 | ordinary-paragraph | low] KETn

[p0356-b0045 | ordinary-paragraph | low] KE9h

[p0356-b0046 | ordinary-paragraph | medium] On the one hand a routine application of

[p0356-b0047 | equation | low] 110ll0,t,0x ≤ C4(h/px)(l10112,k + h21012.x)1/2

[p0356-b0048 | equation | low] (x),H=OA

[p0356-b0049 | ordinary-paragraph | medium] t≥ 1,

## PDF 357 / printed 343



[p0357-b0004 | ordinary-paragraph | medium] 1/2

[p0357-b0005 | ordinary-paragraph | low] ∑ lcurl(Φn - Φ)1.ox 

[p0357-b0006 | equation | low] ≤ Csh-1/2

[p0357-b0007 | ordinary-paragraph | low] [1Φn - Φl,2 + h

[p0357-b0008 | ordinary-paragraph | low] KEgn

[p0357-b0009 | ordinary-paragraph | low] KeJn

[p0357-b0010 | ordinary-paragraph | medium] On the other hand

[p0357-b0011 | equation | low] |l curl 0n ll0.4.0x ≤ Cgh-1/4|0nl1,4.,x 

[p0357-b0012 | ordinary-paragraph | low] Vke Jh

[p0357-b0013 | ordinary-paragraph | low] VOneOn.

[p0357-b0014 | ordinary-paragraph | medium] Combining these inequalities with (5.22) for t = 2 we obtain:

[p0357-b0015 | equation | low] (5.30)

[p0357-b0016 | equation | low] 1a²r(un; Un, Wh)/ ≤ C, 1lun lo,4,2 l/ Wh llo,4,Q[Φh - Φ]2.

[p0357-b0017 | ordinary-paragraph | medium] The next lemma shows that a?*( ; ., . ) is “almost Lipschitz-continuous" with

[p0357-b0018 | ordinary-paragraph | medium] respect to zh.

[p0357-b0019 | lemma | medium] Lemma 5.3. We keep the notations and assumptions of Lemma 5.2 but we suppose

[p0357-b0020 | ordinary-paragraph | medium] that both vn and w, belong to Vh. For all pairs Z, = (zh, Sh) and z* = (z, S*) in Xh,

[p0357-b0021 | ordinary-paragraph | medium] the difference a?r - az# satisfies:

[p0357-b0022 | ordinary-paragraph | low] [a²n(un;Uh,Wh) --a²(unUh, Wh)

[p0357-b0023 | ordinary-paragraph | low] [llu, llo,4,2 if z* ≠ un

[p0357-b0024 | equation | low] ≤Ch1/2|0nl|wnl 

[p0357-b0025 | equation | low] (5.31)

[p0357-b0026 | equation | low] [/Zh - z* llo,4,2 if z* = Un,

[p0357-b0027 | ordinary-paragraph | low] Vuh,Zh,2#∈Xh

[p0357-b0028 | ordinary-paragraph | low] Vuh, Whe Vh.

[p0357-b0029 | proof | medium] Proof. This proof is based on the identity:

[p0357-b0030 | ordinary-paragraph | low] a²n(un;Un,Wh)—a2(unUn,Wn)

[p0357-b0031 | equation | low] (5.32)

[p0357-b0032 | ordinary-paragraph | low] vinl)(wint

[p0357-b0033 | ordinary-paragraph | medium] —wex)ds

[p0357-b0034 | ordinary-paragraph | low] x∈JhJ0_x(zn,-zh)

[p0357-b0035 | ordinary-paragraph | medium] where

[p0357-b0036 | equation | low] 0_k(z, -z*) = {x∈Or; z·n(x) < 0 and z*·n(x) > 0}.

[p0357-b0037 | ordinary-paragraph | medium] Thus, in view of (5.29) we can replace not only v, by vh - Pu, but also w, by

[p0357-b0038 | ordinary-paragraph | medium] Wh -- Pwh. This gives:

[p0357-b0039 | ordinary-paragraph | medium] 1/4

[p0357-b0040 | equation | low] ∑I curl hnll0.4.0x 

[p0357-b0041 | ordinary-paragraph | low] [a²(un;Uh,Wn) —a²(un;Un,Wn)/ ≤ C

[p0357-b0042 | ordinary-paragraph | low] KEgn

[p0357-b0043 | ordinary-paragraph | medium] 1/4

[p0357-b0044 | equation | low] ∑ II curl(Φn - Φ)l,4,0x

[p0357-b0045 | ordinary-paragraph | low] KETn

[p0357-b0046 | ordinary-paragraph | medium] 1/2

[p0357-b0047 | ordinary-paragraph | low]  Ilcurl(xh - x)l1,ox 

[p0357-b0048 | ordinary-paragraph | low] KEgn

[p0357-b0049 | ordinary-paragraph | medium] Then the techniques of the preceding lemma easily yield:

## PDF 358 / printed 344



[p0358-b0004 | ordinary-paragraph | medium] Hence (5.31) follows from Lemma 5.1 and (5.24) in the general case.

[p0358-b0005 | ordinary-paragraph | medium] To handle the particular case where z* = un, we observe that:

[p0358-b0006 | equation | low] Vxeo_k(z, -u).

[p0358-b0007 | equation | low] I(x)u.z - (x)u.n| ≥ I(x)u.n|

[p0358-b0008 | ordinary-paragraph | medium] Therefore the factor u, : n in the right-hand side of (5.32) can be bounded by the

[p0358-b0009 | ordinary-paragraph | medium] difference I(u, - zh)· n| = I(z* - zh) · nl. It can be readily checked that the remain-

[p0358-b0010 | ordinary-paragraph | medium] der of the above argument is still valid with this modification.

[p0358-b0011 | ordinary-paragraph | medium] 口

[p0358-b0012 | ordinary-paragraph | medium] Finally, we can prove another interesting bound for a(.; ., .).

[p0358-b0013 | lemma | medium] Lemma 5.4. We retain the assumptions and notations of Lemma 5.3 except that we

[p0358-b0014 | ordinary-paragraph | medium] take vn in Xn. Then we have the following estimate for all z = (curla,β) with

[p0358-b0015 | ordinary-paragraph | medium] α ∈ H²(Ω) ∩ H(Ω) and β∈ L²(Ω):

[p0358-b0016 | equation | low] [a(un;Un — z, Wn)1 ≤ Ch1/21|un llo,4,Q[Φh ——α]41Wnl,

[p0358-b0017 | equation | low] (5.34)

[p0358-b0018 | ordinary-paragraph | low] VWhe Vh,

[p0358-b0019 | ordinary-paragraph | medium] Vuh, UhE Xh.

[p0358-b0020 | ordinary-paragraph | medium] where the line integrals in a2(.; ., .) are taken over any portion of 0k.

[p0358-b0021 | proof | medium] Proof. Take Pw, = (w = curl x,&,) and set z = curl α. The linearity ofa(.; ., . ) with

[p0358-b0022 | ordinary-paragraph | medium] respect to its last argument permits to write:

[p0358-b0023 | equation | low] a(unUh —- Z,Wn) =a(un;Un ——Z,Wh —W) + a(uh;Un ——2,W).

[p0358-b0024 | ordinary-paragraph | medium] Since w belongs to H1(Q) we can apply the identity (5.17):

[p0358-b0025 | equation | low] a(un;Un—Z,w) =—a(un;Pwh,Vh—z),

[p0358-b0026 | ordinary-paragraph | medium] so that Lemma 5.2 and (5.24) give:

[p0358-b0027 | equation | low] [a(un; Un - Z, w)/ ≤ C1 I/ un llo,4,2/ Pwnl // vh - Zllo,4,2

[p0358-b0028 | equation | low] ≤ C lun llo,4,2l wnl ll h -- Zllo,4,2.

[p0358-b0029 | ordinary-paragraph | medium] Likewise, we have

[p0358-b0030 | ordinary-paragraph | medium] 1/2

[p0358-b0031 | equation | low] [a(un; Un —— Z, Wh — w)/ ≤ C2 llunllo,4.2

[p0358-b0032 | ordinary-paragraph | low] II wh - wIllo,4,52

[p0358-b0033 | ordinary-paragraph | low] KETh

[p0358-b0034 | ordinary-paragraph | medium] 1/2

[p0358-b0035 | equation | low] ≤ C3h1/2 1/un ll0,4,0/ wnl

[p0358-b0036 | ordinary-paragraph | low] KETh

[p0358-b0037 | ordinary-paragraph | medium] in view of (5.22) and Lemma 5.1. Therefore

[p0358-b0038 | ordinary-paragraph | low] [a(un; Uh - Z, Wh —W)] + |a(un;Un - Z, w)] ≤ C4hi/2 1/unllo,4,q/wn1 [Φh — α]4.

[p0358-b0039 | ordinary-paragraph | medium] Finally, like in Lemma 5.2, we derive

## PDF 359 / printed 345



[p0359-b0003 | equation | low] < Ceh™? ||U g llo,a,01Wa[lb n— Wa.

[p0359-b0004 | ordinary-paragraph | high] By collecting these inequalities, we obtain (5.34). O

[p0359-b0005 | remark | high] Remark 5.1. It follows from Lemma 5.2 and the argument of Lemma 5.3 that the

[p0359-b0006 | ordinary-paragraph | high] mapping G, is Lipschitz-continuous on J,:

[p0359-b0007 | ordinary-paragraph | high] (9.35) Giln) — Gaur Ile < Clay] + [ut |)lu, — ut] Vayu,it eV,

[p0359-b0008 | ordinary-paragraph | high] with a constant C independent of h.

[p0359-b0009 | ordinary-paragraph | high] Now we are in a position to define the operator VG,(u,), i.e. to approach as

[p0359-b0010 | ordinary-paragraph | high] best as we can the “derivative” of the form 4(.; ., .). Clearly, the simplest guess

[p0359-b0011 | ordinary-paragraph | high] is to linearize the dependence of G7"(.; ., .) with respect to z,. Thus we set:

[p0359-b0012 | definition | high] Definition 5.1. For all u,€ V,, the operator VG,(u,)¢ L(V,; ¥,) is defined by

[p0359-b0013 | ordinary-paragraph | high] <VG,(UyUp), *Wa > = G""(UVpy_,5 W, ) + G""(Uq5 Uns Wy) Vw, = curl y,, %,€ ®,.

[p0359-b0014 | ordinary-paragraph | high] Obviously ’G,(u,) is a linear operator from V, into Y, and Lemma 5.2 implies that

[p0359-b0015 | equation | low] IV Gi(Uy) Valle < Cluallo,| Vur,, 0, UV,»

[p0359-b0016 | ordinary-paragraph | high] with a constant C independent of h.

[p0359-b0017 | remark | high] Remark 5.2. Note that VG,(u,) is “nearly Lipschitz-continuous” with respect to

[p0359-b0018 | ordinary-paragraph | high] u,. Indeed,

[p0359-b0019 | ordinary-paragraph | high] |G, (un) — VG, (uiPtn) Wn > |= [G"(Up5 Ons Wa) — GY (UFDEyS,W y)

[p0359-b0020 | ordinary-paragraph | high] Os" (0j,, Uy Wp) a'*(v,; ui, W;,)|

[p0359-b0021 | equation | low] < |G""(uj, — URS Vp, Wi)| + [G"™ (UF; Vp, Wa)

[p0359-b0022 | ordinary-paragraph | high] ox G** (ux; 0), W,)| + |G""(v,;U j,— Up, Wi)|

[p0359-b0023 | ordinary-paragraph | high] + |a"™(uvk,,3 W h)— G"*(vuky,; w, )|

[p0359-b0024 | equation | low] < C,|v,||waCllu , — us

[p0359-b0025 | ordinary-paragraph | high] + h*?(\\u, — uf llo,a.o + lug |),

[p0359-b0026 | ordinary-paragraph | high] by applying Lemmas 5.3 and 5.4. Hence

[p0359-b0027 | equation | low] VG, (u,) — VG,(UI eFay)sv_ ) S Coin — unl + h* \ui|).

[p0359-b0028 | ordinary-paragraph | high] Of course, we can derive a similar upper bound with the term h'?|u,| in the

[p0359-b0029 | ordinary-paragraph | high] right-hand side.

[p0359-b0030 | ordinary-paragraph | high] Finally in order to apply Theorem 3.8, it is necessary to relate the operator

[p0359-b0031 | ordinary-paragraph | high] G defined by (5.6) with the operator that corresponds to the trilinear form

## PDF 360 / printed 346



[p0360-b0004 | equation | low] (u;du;/0xj,vi) = (curl ugrad y,v) Vv = curl Φ,  Φe Φs.

[p0360-b0005 | ordinary-paragraph | high] Hence

[p0360-b0006 | equation | low] a(u; u, v) = (w grad y, v)

[p0360-b0007 | ordinary-paragraph | high] provided y has the regularity H2. Of course, when u belongs only to X this

[p0360-b0008 | ordinary-paragraph | high] Thus we define for all u in X:

[p0360-b0009 | equation | low] <G(u), v> = a(u; Pu, v) --<f,v)Vve L"(Ω)².

[p0360-b0010 | equation | low] (5.36)

[p0360-b0011 | ordinary-paragraph | high] Since Pu = u for all u in V, this definition coincides with (5.6) when ue V and

[p0360-b0012 | ordinary-paragraph | high] V = curl Φ, Φe Φ,. Furthermore, it can be readily checked that (5.36) defines a @∞_

[p0360-b0013 | ordinary-paragraph | high] mapping G: X → Y whose derivative DG(u)e &(X; Y) is given by the expression:

[p0360-b0014 | ordinary-paragraph | low] z(U)sTMA (

[p0360-b0015 | equation | low] (5.37)

[p0360-b0016 | equation | low] <DG(u)· v, w) = a(u; Pv, w) + a(v; Pu, w)

[p0360-b0017 | ordinary-paragraph | high] Finally, it can be proved that u is a nonsingular solution of (5.7) whenever u is

[p0360-b0018 | ordinary-paragraph | high] also a nonsingular solution of the Navier-Stokes problem with G defined by

[p0360-b0019 | ordinary-paragraph | high] (5.36), and conversely.

[p0360-b0020 | ordinary-paragraph | high] Let us check the assumptions of Theorem 3.8. It follows readily from (5.10)

[p0360-b0021 | ordinary-paragraph | high] that

[p0360-b0022 | equation | low] ITllx ≤(1 + C)'I/lh  Vle Yh,

[p0360-b0023 | equation | low] (5.38)

[p0360-b0024 | ordinary-paragraph | high] where C, denotes the constant of (5.20). Next, (3.60) has already been checked in

[p0360-b0025 | ordinary-paragraph | high] Section 4.3: owing to the regularity condition (4.18) T,f = (curl yh, w,) satisfies

[p0360-b0026 | ordinary-paragraph | high] the error estimate

[p0360-b0027 | equation | low] (5.39)

[p0360-b0028 | equation | low] y - yhl1,s,e + I0 -- Wnllo,o ≤ Cha l/fllo..2,

[p0360-b0029 | ordinary-paragraph | high] where r ≤t < 2, 1/y + 1/t = 1, α = 1/y when I = 1 and α = 2/v when l ≥ 2.

[p0360-b0030 | ordinary-paragraph | high] Likewise, the approximation properties of the operator π, have been derived in

[p0360-b0031 | ordinary-paragraph | high] Section IH1.3.1. Indeed, for v = (curl Φ, 0)e V we take

[p0360-b0032 | equation | low] (5.40)

[p0360-b0033 | equation | low] ThU = (curl(Phb), On)e Vh,

[p0360-b0034 | ordinary-paragraph | high] i.e. 0, is determined by

[p0360-b0035 | equation | low] (0n, μn) = (curl(PhΦ), curl μn)

[p0360-b0036 | equation | low] "θ>nA(

[p0360-b0037 | ordinary-paragraph | high] Then

[p0360-b0038 | equation | low] Ihu - vllx ≤ |PhΦ -—Φl1,s,2 + 2 inf IIμn -- 0llo,α

[p0360-b0039 | ordinary-paragraph | low] μh∈n

[p0360-b0040 | equation | low] (curl(PhΦ - Φ), curl μh)

[p0360-b0041 | equation | low] + sup

[p0360-b0042 | ordinary-paragraph | low] Il μnllo,α

[p0360-b0043 | ordinary-paragraph | low] u034n

[p0360-b0044 | ordinary-paragraph | high] Therefore Lemma H1.3.2, Theorem A.2 and a standard density argument yield

[p0360-b0045 | equation | low] lim Ilπ,u - ull x = O  Vu∈ V.

[p0360-b0046 | ordinary-paragraph | high] h→0

## PDF 361 / printed 347



[p0361-b0005 | equation | low] |nv - v/lx ≤ Chl-1/2(llΦll+3/2,2 + IlΦll+1. ∞,2).

[p0361-b0006 | ordinary-paragraph | medium] Now we turn to (3.62); we have

[p0361-b0007 | ordinary-paragraph | low] <Gn(πnu)—G(u),n>=an"(πnu;πnu,vn)-a(u;u,Vn)

[p0361-b0008 | ordinary-paragraph | medium] Hvh = curl Φh, Φh E Φh.

[p0361-b0009 | ordinary-paragraph | medium] Using a simple rearrangement of terms we obtain:

[p0361-b0010 | equation | low] <Gn(πhu) —G(u),Vh>=amn"(πnu;πnu—u,Vn) +a(πnu -u;u,Vn).

[p0361-b0011 | ordinary-paragraph | medium] Therefore Lemma 5.4 and Lemma 5.2 together with (5.22) yield:

[p0361-b0012 | ordinary-paragraph | low] [ -]( + ≥()  (n)" 

[p0361-b0013 | equation | low] (5.41)

[p0361-b0014 | ordinary-paragraph | medium] Hence (3.62) follows from Lemma 5.1. Furthermore we infer from this lemma

[p0361-b0015 | ordinary-paragraph | medium] and (5.41) that

[p0361-b0016 | equation | low] 1IGn(πhu) -- G(u)l/n ≤ Chk-1/2|y |2.oll/ llk+1,2

[p0361-b0017 | equation | low] (5.42)

[p0361-b0018 | ordinary-paragraph | medium] Vu = (curly,w)e V with y e Hk+1(Q), 1 ≤ k ≤ l.

[p0361-b0019 | ordinary-paragraph | medium] As far as (3.63) is concerned, we apply Definition 5.1 and (5.37):

[p0361-b0020 | ordinary-paragraph | low] <(DGh(πhu) —DG(u))·Un,Wn>=an"(πhu;Un,Wn) +amh"(Uh;πnu, Wn)

[p0361-b0021 | ordinary-paragraph | low] AsnA

[p0361-b0022 | ordinary-paragraph | low] —a(u; Pvh,Wh) —a(Un;u, Wh)

[p0361-b0023 | ordinary-paragraph | low] =aπn"(πhu;Un——PunWn)+an"(Unnu—u,Wh)

[p0361-b0024 | ordinary-paragraph | low] + a(πnu ——u; Pvh, Wh)

[p0361-b0025 | ordinary-paragraph | medium] taking into account the regularity of u and Pv,. Consequently, it stems from

[p0361-b0026 | lemma | medium] Lemma 5.3 and 5.4 that:

[p0361-b0027 | ordinary-paragraph | low] i1(DGn(πhu) -DG(u)·vnllh ≤ C{h1/²(1Phl1,4,o[Φh-Φ]4 + Iun1 [Pn -↓]4)

[p0361-b0028 | ordinary-paragraph | low] + |unl/Pny -Wl1,4.2},

[p0361-b0029 | ordinary-paragraph | medium] with Pun = (curl Φ, On), Vu = (curl y,w)e V, Vun = (curl Φh, On)e Vh.

[p0361-b0030 | ordinary-paragraph | medium] Thus Lemma 5.1 gives:

[p0361-b0031 | equation | low] 11(DGn(πhu) - DG(u)· vnlh ≤ Ch1/2(1yl.4. + I I/2.0)/unl,

[p0361-b0032 | ordinary-paragraph | medium] which implies (3.63).

[p0361-b0033 | ordinary-paragraph | medium] Finally, it remains to verify (3.64). Take uh, u* and u in V; by definition

[p0361-b0034 | ordinary-paragraph | medium] we have for all w, = curl Xh, Xh E Φh:

[p0361-b0035 | ordinary-paragraph | low] (Gn(un)—Gn(u)-DGn(uh)·(un-u),wn>

[p0361-b0036 | ordinary-paragraph | low] =a"n(unun,Wn)-aur(u;u,wn) -au%(u%;un——u,wn)-—a"%(un——u;u,Wn)

[p0361-b0037 | ordinary-paragraph | low] =a"%(un—u;un—u,wn)+aun(un—u;u—uh,wn)+{ar(un;un,Wh)

## PDF 362 / printed 348



[p0362-b0003 | ordinary-paragraph | high] {a3"(U, — Up; Uy, Wh) — ast(u, psUy, Wa) oe {as*(u uy, — Uj, Wp)

[p0362-b0004 | ordinary-paragraph | high] — ah(ui;u w,— uit,w ,)} + {a3(uUin,s W r)— a3" (US Uy, Wa) }-

[p0362-b0005 | ordinary-paragraph | high] Then using repeatedly Lemma 5.3 this expression can be bounded by:

[p0362-b0006 | ordinary-paragraph | high] Ch? {|u y| Wi, — Witlia.a + Wir — Wr li.4,alUn — url} |,

[p0362-b0007 | equation | low] < C,h'?|u, — uk |( lu, — unl + lug — up] + luplblwal =V n eV i:

[p0362-b0008 | ordinary-paragraph | high] Hence Lemma 5.2 gives the bound

[p0362-b0009 | ordinary-paragraph | high] | G,(Un) — Gut) — VG, (up) (Un — UDI

[p0362-b0010 | equation | low] < C3lu, — url {lun — up| + lug — up| + h*|?up| }.

[p0362-b0011 | ordinary-paragraph | high] This implies (3.64) with the function

[p0362-b0012 | equation | low] L, (uv) = Cy(u + h*? y).

[p0362-b0013 | ordinary-paragraph | high] Clearly L,, is continuous, monotonically increasing with respect to each variable

[p0362-b0014 | ordinary-paragraph | high] and

[p0362-b0015 | equation | low] lim L,(0;v) = lim(h'?v)=0 WveR,.

[p0362-b0016 | equation | low] h>0 h>0

[p0362-b0017 | ordinary-paragraph | high] Since all the assumptions of Theorem 3.8 are satisfied, we can apply its

[p0362-b0018 | ordinary-paragraph | high] conclusion to the upwind scheme (5.18), thus deriving the existence, uniqueness

[p0362-b0019 | ordinary-paragraph | high] and convergence of its branch of solutions. Furthermore, by comparing the two

[p0362-b0020 | ordinary-paragraph | high] error estimates (3.67) and (3.41) and taking into account (5.42) we readily deduce

[p0362-b0021 | ordinary-paragraph | high] that the error of the upwind scheme is bounded exactly like the error of the

[p0362-b0022 | ordinary-paragraph | high] centered scheme. In other words, in this case the upwinding does not alter the

[p0362-b0023 | ordinary-paragraph | high] scheme’s order. These results are summed up in the following theorem.

[p0362-b0024 | theorem | high] Theorem 5.1. Let Q be a bounded, convex polygon and JF, a uniformiy regular

[p0362-b0025 | ordinary-paragraph | high] family of triangulations of Q. For fe L'(Q)?, te[r, 2) let

[p0362-b0026 | equation | low] {(A, (curl y/(A), @(A))); 2 = 1/veA }

[p0362-b0027 | ordinary-paragraph | high] be a branch of nonsingular solutions of the Navier-Stokes Problem (5.7). Then for

[p0362-b0028 | ordinary-paragraph | high] h < hg small enough there exists a unique branch

[p0362-b0029 | equation | low] {(A, (curl y,(A), @,(A))); 2 = 1/veA }

[p0362-b0030 | ordinary-paragraph | high] of €°-solutions of the upwind scheme (5.18) satisfying the error estimate:

[p0362-b0031 | equation | low] a Wala) — WADI, s,2 + nA) — @(A)\lo,a} < Cyh*,

[p0362-b0032 | ordinary-paragraph | high] (5.43) l/yy ifl=1,

[p0362-b0033 | equation | low] L/t+ iy =1,

[p0362-b0034 | equation | low] ; ie if 1 > 2,

[p0362-b0035 | ordinary-paragraph | high] with a constant C independent of h or 2.

## PDF 363 / printed 349



[p0363-b0005 | equation | low] C2(e)h1/2-  for all ε > 0.

[p0363-b0006 | ordinary-paragraph | medium] In addition, when the mapping Λ → y(a) is continuous from A into Hm+2(Q)N

[p0363-b0007 | ordinary-paragraph | low] :aapy am [z/1 - 1'1]≥u ppau auos dof () z/e +uM

[p0363-b0008 | equation | low] (5.44)

[p0363-b0009 | equation | low] sup {Iyn() - y(2)l1.s,2 + I/w(2) - w()lo,o} ≤ Cshm.

[p0363-b0010 | ordinary-paragraph | low] AeA

[p0363-b0011 | ordinary-paragraph | medium] Finally, an argument closely resembling that of Section 4.3 permits to refine

[p0363-b0012 | ordinary-paragraph | medium] the error estimate for |y - yhli.o and obtain the same order of convergence as

[p0363-b0013 | theorem | medium] Theorem 4.5.

[p0363-b0014 | theorem | medium] Theorem 5.2. Let Q and J, be like in Theorem 5.1 and assume that the branch of

[p0363-b0015 | ordinary-paragraph | medium] nonsingular solutions of the Navier-Stokes Problem (5.7) has the regularity:

[p0363-b0016 | equation | low]  →y(2)∈°(A; Hl+1(Ω)) for l ≥ 2 or H²(Ω) for I = 1.

[p0363-b0017 | ordinary-paragraph | medium] Then the approximate solution Wn of the upwind scheme (5.18) satisfies the error

[p0363-b0018 | ordinary-paragraph | medium] bound:

[p0363-b0019 | equation | low] [Ch' when l ≥ 2,

[p0363-b0020 | equation | low] (5.45)

[p0363-b0021 | equation | low] y(2) -h(2)l ≤

[p0363-b0022 | equation | low] (C2()hi-e when l = 1 Ve >0,

[p0363-b0023 | ordinary-paragraph | medium] with constants independent of h and X.

[p0363-b0024 | proof | medium] Proof. Let g be any function of L?(Ω)² and let us introduce the following dual

[p0363-b0025 | ordinary-paragraph | medium] linearized Navier-Stokes problem, analogous to (4.40):

[p0363-b0026 | equation | low] z = (z = curl x, v)e V such that:

[p0363-b0027 | equation | low] (5.46)

[p0363-b0028 | equation | low] (v, 0) + Aa(v; u(2),z) - Aa,(u(a); z,v) = (g, curl Φ)

[p0363-b0029 | ordinary-paragraph | medium] Vv = (v = curl Φ, 0)e V.

[p0363-b0030 | ordinary-paragraph | medium] We know that on the one hand:

[p0363-b0031 | equation | low] a(u, z, v) = -a (u; u,z)

[p0363-b0032 | ordinary-paragraph | medium] and on the other hand:

[p0363-b0033 | equation | low] a(u; v,z) + a(v;u,z) = (DG(u)· v, z)

[p0363-b0034 | ordinary-paragraph | medium] for all u, v and z in V. Therefore Problem (5.46) is the same as Problem (4.40) and

[p0363-b0035 | ordinary-paragraph | medium] hence its solution enjoys the regularity properties stated in Lemma 4.1.

[p0363-b0036 | ordinary-paragraph | medium] Now, by reasoning like in Theorem 4.5 we readily obtain:

[p0363-b0037 | ordinary-paragraph | low] (g,curl(b -— yn)) =(v- Vn,C -—@n) + b(u --uh,v -— 0n) + b(z - Zh,@ - μn)

[p0363-b0038 | ordinary-paragraph | low] +Aa(u —un;u,z) -Aa(u,z,u -un) —Aa(u;u,Zh)

[p0363-b0039 | ordinary-paragraph | low] +Aa(un;un,Zn) +Aan(un;uh,Zh)

## PDF 364 / printed 350



[p0364-b0004 | ordinary-paragraph | low] (g,curl(y -Vn)) = (v-Vh,@ -Wn) + b(u -—un,v- On) + b(z —Zh( -μn)

[p0364-b0005 | ordinary-paragraph | low] +A{a(u-unu,z-—Zn) + a“n(unu—unz-Zh)

[p0364-b0006 | equation | low] (5.47)

[p0364-b0007 | ordinary-paragraph | low] -- a(u -un;z,u- un)}.

[p0364-b0008 | ordinary-paragraph | medium] But, the delicate step in this proof is an adequate estimate of the a(.; ., .) term

[p0364-b0009 | ordinary-paragraph | medium] in the factor multiplying . Indeed, if we apply Lemma 5.2, we get:

[p0364-b0010 | equation | low] [x]²-]y≥(-znnn)un|

[p0364-b0011 | ordinary-paragraph | medium] And when I = 1, this upper bound is useless because infx, [x - xh]2 = O(1).

[p0364-b0012 | ordinary-paragraph | medium] Instead, it is better to take advantage of the fact that xe H?(Q) and replace the

[p0364-b0013 | ordinary-paragraph | medium] previous bound by:

[p0364-b0014 | equation | low] [aun(un;u-uh,Z -Zn)/ ≤C11ynl1.4,o[y -h]2

[p0364-b0015 | equation | low] ∑ 1x - xnl,4,x

[p0364-b0016 | ordinary-paragraph | low] 1x-xnl1,4, + h(

[p0364-b0017 | ordinary-paragraph | low] KETh

[p0364-b0018 | ordinary-paragraph | medium] Hence, if we choose zh = Thz e Vh defined by (5.40), the fact that Xn = Phx implies

[p0364-b0019 | ordinary-paragraph | medium] that

[p0364-b0020 | equation | low] [a"n(un;u - uh, Z — Zh)/ ≤ C2h/nl1,4,o[y - Wn]2 l/xl/2.4.Q.

[p0364-b0021 | ordinary-paragraph | medium] Finally, observe that

[p0364-b0022 | equation | low] [-n]2≤[-Ph]2+[Pn-n]2

[p0364-b0023 | equation | low] (5.48)

[p0364-b0024 | equation | low] ≤ C3hl-1 l lli+1.2 + C4/πhu - unl

[p0364-b0025 | ordinary-paragraph | medium] by virtue of (5.26), (5.21) and (5.40). This gives an upper bound of the form:

[p0364-b0026 | ordinary-paragraph | low] [aun(un;u - uh, Z - Zh)/ ≤ Cs(lly l/2.s) /x ll 2.4.o(h' l/yll1+1,o + h|πnu - u,l).

[p0364-b0027 | ordinary-paragraph | medium] The other terms in (5.47) are easily estimated and the proof ends exactly like

[p0364-b0028 | ordinary-paragraph | medium] that of Theorem 4.5.

[p0364-b0029 | ordinary-paragraph | medium] 口

[p0364-b0030 | subsection | medium] 5.3. Approximating the Pressure with the Upwind Scheme

[p0364-b0031 | ordinary-paragraph | medium] We have seen in Section 4.3 that the pressure term p underlying the Navier-Stokes

[p0364-b0032 | ordinary-paragraph | medium] system (5.7) is the solution of the problem:

[p0364-b0033 | ordinary-paragraph | medium] Find pe Wi,r(Q)N L?(Q) such that:

[p0364-b0034 | equation | low] ∑ u;du/0x,, grad q

[p0364-b0035 | ordinary-paragraph | low] ()s,M bA

[p0364-b0036 | ordinary-paragraph | medium] (5.49)  (grad p,grad q)

[p0364-b0037 | ordinary-paragraph | medium] f - vcurlo -

[p0364-b0038 | equation | low] =1

[p0364-b0039 | ordinary-paragraph | medium] Likewise, to recover the pressure ph associated with the upwind scheme (5.18),

[p0364-b0040 | ordinary-paragraph | medium] we introduce the space Q, defined by (4.34):

## PDF 365 / printed 351



[p0365-b0004 | ordinary-paragraph | medium] and we discretize (5.49) by:

[p0365-b0005 | ordinary-paragraph | medium] Find ph e Qn satisfying:

[p0365-b0006 | equation | low] (grad ph, grad qh) = (f - vcurl wh,grad qh) - a"r(un; un, grad qh)

[p0365-b0007 | equation | low] (5.51)

[p0365-b0008 | ordinary-paragraph | low] "0="bA

[p0365-b0009 | ordinary-paragraph | medium] Obviously, this problem has a unique solution.

[p0365-b0010 | ordinary-paragraph | medium] To estimate the error p - ph we use the same duality argument as in Theorem

[p0365-b0011 | ordinary-paragraph | medium] 111.2.7. We introduce the function ve H1 (Q) defined by

[p0365-b0012 | equation | low] divv = p -- Ph, Ivla,o ≤ C, llp - Phllo.

[p0365-b0013 | ordinary-paragraph | medium] which we can split into

[p0365-b0014 | equation | low] V = grad q + curl Φ.

[p0365-b0015 | ordinary-paragraph | medium] Since Q is assumed to be a convex polygon, both q and Φ belong to H?(Ω) with

[p0365-b0016 | equation | low] Ilq ll2,o + Il Φ ll 2,o ≤ C2Ivl1,o  (cf. Lemma I11.2.6).

[p0365-b0017 | ordinary-paragraph | medium] In addition, if the triangulation , is uniformly regular Lemma Il1.2.6 shows that

[p0365-b0018 | equation | low] (5.52)

[p0365-b0019 | equation | low] lq - Phql1,s,2 + 1 - InΦl1.s.2 ≤ C3h2/s|vl±.o.

[p0365-b0020 | ordinary-paragraph | medium] Now, like in Theorem I11.2.7 we can write:

[p0365-b0021 | ordinary-paragraph | medium] II p -- Phll2,α = (grad(qh - p), grad(q - Phq) + (grad(ph -- p), grad(Phq))

[p0365-b0022 | ordinary-paragraph | medium] VaneQn.

[p0365-b0023 | ordinary-paragraph | medium] Thus, to estimate p - ph, we must derive a sharp bound for thc second term. By

[p0365-b0024 | ordinary-paragraph | medium] subtracting (5.49) from (5.51) we obtain:

[p0365-b0025 | ordinary-paragraph | medium] (grad(Ph - p), grad(P:q)) = - v(curl(wn - (), grad(Phq)) + a,(u; u, grad(Phq))

[p0365-b0026 | equation | low] -aun(un; uh, grad(Phq))

[p0365-b0027 | equation | low] = v(curl(o - wn),vh - v) + v(∞ - Wh, curl v)

[p0365-b0028 | ordinary-paragraph | low] + a"n(unu -uhVh-v) + a(u-uhu,Vh -v)

[p0365-b0029 | ordinary-paragraph | medium] + a(uh - u;v,un) + a(u;v,un - u)

[p0365-b0030 | ordinary-paragraph | medium] where

[p0365-b0031 | equation | low] Vh = grad(Ph9) + curl(IhΦ).

[p0365-b0032 | ordinary-paragraph | medium] Therefore (5.52) together with familiar estimates for the forms a"(.; ., .) and

[p0365-b0033 | ordinary-paragraph | medium] a1(.; ., .) give a result analogous to (I11.2.38).

[p0365-b0034 | lemma | medium] Lemma 5.5. Let Q be a bounded, convex polygon and J, a uniformly regular

[p0365-b0035 | ordinary-paragraph | medium] triangulation of Ω. If p and w belong to W1,(Ω) for some real t e [r,2] then the

[p0365-b0036 | ordinary-paragraph | medium] error on p is:
