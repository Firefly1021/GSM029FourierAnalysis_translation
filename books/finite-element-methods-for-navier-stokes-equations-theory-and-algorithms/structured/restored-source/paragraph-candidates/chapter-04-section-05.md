# Paragraph candidates: chapter-04-section-05

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-04-section-05-pc00001 | equation | low | PDF 350

[[FORMULA:f-p0350-05806]]

## chapter-04-section-05-pc00002 | ordinary-paragraph | high | PDF 350

provided (A) H**?(Q) for some ke [1,1]. Finally if w(A)e H'*1(Q) when | > 2 or W(A)e H?(Q) when | = 1, a duality argument similar to that of Theorem 4.5 yields the optimal estimate:

## chapter-04-section-05-pc00003 | equation | low | PDF 350

[[FORMULA:f-p0350-05808]]

## chapter-04-section-05-pc00004 | ordinary-paragraph | high | PDF 350

By applying the material of Section 1.4.4, we can derive error bounds of the same order for the pressure. The proofs are left as exercises.

## chapter-04-section-05-pc00005 | section | high | PDF 350

§5. Numerical Analysis of Upwind Schemes

## chapter-04-section-05-pc00006 | ordinary-paragraph | high | PDF 350

When the viscosity v is small, or equivalently when the Reynolds number Re is large compared to the other parameters of the fluid, there arises a boundary layer in the neighborhood of I’ where the viscosity predominates while it is negligible in the interior of 2. At the same time, the flow becomes turbulent. Thus the solutions of the Navier-Stokes equations are seriously discontinuous at high Reynolds number. It is not our purpose here to modelize turbulent flows, but all the same, it is worthwhile to examine one possible discretization of discontinuous solutions of the Navier-Stokes equations. Instead of the centered schemes studied so far, we propose upwind schemes which are better adapted to describe discontinuous flows. The forthcoming analysis shows that these schemes are nearly optimal. The reader can also refer to Johnson & Saranen [47] for an alternate method, the streamline diffusion method, that applies to Euler and Navier-Stokes equations.

## chapter-04-section-05-pc00007 | subsection | high | PDF 350

5.1. Upwinding in the Stream Function-Vorticity Scheme

## chapter-04-section-05-pc00008 | ordinary-paragraph | high | PDF 350

The upwind scheme discussed in this section was developed by Fortin [31], inspired by a numerical method advocated in Lesaint & Raviart [51] to solve a neutron transport equation. It stems from the following heuristic remarks. When a smooth vector field u is divergence-free, the convection term satisfies (with the usual summation convention that a repeated index represents a sum):

## chapter-04-section-05-pc00009 | equation | low | PDF 350

[[FORMULA:f-p0350-05809]]

## chapter-04-section-05-pc00010 | ordinary-paragraph | high | PDF 350

Now, suppose {2 is the union of two bounded regions Q, and Q, separated by an interface S like in Figure 21. Denote by I’ the boundary of Q and by n, the

## chapter-04-section-05-pc00011 | figure | high | PDF 351

Figure 21

## chapter-04-section-05-pc00012 | ordinary-paragraph | high | PDF 351

unit exterior normal to Q; on S. Assume that the vector field u is no longer globally smooth in Q but that instead, ulo, €H'(Q,)", ulp=0, ueH(div;Q) and divu=0. Then the product uj;u; is no longer differentiable in Q but its distributional derivative has the form: [o(uju;)/Ox;] = O(u;u;)/Ox;le, ua, + a surface distribution corresponding to the jump of the field u across the interface S, namely: u-n(ur — uj") ds where n and the notions of exterior and interior refer to the same region. The upwinding relies on the following principle:

## chapter-04-section-05-pc00013 | ordinary-paragraph | high | PDF 351

the flow in Q, depends exclusively upon the flux entering through S. By virtue of this principle, we introduce the notation: (3:8) 6_Q, = {x eS; u-n,(x) < 0} for the portion of the interface S where the fluid enters 2, and we take as a

## chapter-04-section-05-pc00014 | definition | high | PDF 351

definition the following expression for the convection term:

## chapter-04-section-05-pc00015 | ordinary-paragraph | high | PDF 351

|u ;(Ou,/Ox,)v; dx

## chapter-04-section-05-pc00016 | equation | low | PDF 351

[[FORMULA:f-p0351-05813]]

## chapter-04-section-05-pc00017 | ordinary-paragraph | high | PDF 351

(4)

## chapter-04-section-05-pc00018 | ordinary-paragraph | high | PDF 351

7) 2 ay u,(du;/0x;)v;dx + u-n,(ue” — uj")vi" ds

## chapter-04-section-05-pc00019 | equation | low | PDF 351

[[FORMULA:f-p0351-05814]]

## chapter-04-section-05-pc00020 | ordinary-paragraph | high | PDF 351

for all u in H(div; Q) with divu = 0, ulg € H'(Q,)" and vio, € H'(Q,)”. Clearly, when u and v belong to H'(Q), the surface term vanishes and we recover the familiar expression for the convection. But when u and v are not globally in H' we have to interpret (5.2) as a definition.

## chapter-04-section-05-pc00021 | ordinary-paragraph | high | PDF 352

gulated, each triangle being considered as a subregion of 2. But, beforehand, let us recall the setting of the stream function-vorticity formulation and approximation of the Navier-Stokes system developed in Section 4.3. Let Q be a bounded domain in R* with a polygonal boundary J, so that it can be entirely triangulated and suppose Q is convex so the regularity condition (4.18) holds. To simplify the discussion we agree to drop the pressure for the moment and consider only the stream function and vorticity. Then we set

## chapter-04-section-05-pc00022 | equation | low | PDF 352

[[FORMULA:f-p0352-05818]]

## chapter-04-section-05-pc00023 | ordinary-paragraph | high | PDF 352

with s > 4.and 1/r + 1/s = 1. The Stokes operator Te L(Y;X ) is defined by

## chapter-04-section-05-pc00024 | equation | low | PDF 352

[[FORMULA:f-p0352-05820]]

## chapter-04-section-05-pc00025 | ordinary-paragraph | high | PDF 352

ae te w, curl ¢) = (f,curld) Vde®,,

## chapter-04-section-05-pc00026 | equation | low | PDF 352

[[FORMULA:f-p0352-05822]]

## chapter-04-section-05-pc00027 | ordinary-paragraph | high | PDF 352

where w and w are related to the velocity u by (5.4) u=curly and mw =curlu. As usual, we introduce the subspace of X (5.5) V = {(curl ¢, 0) eX; 6€ HG (Q), 0 = — Ad}, (has only one connected component since 92 is convex) and we know from

## chapter-04-section-05-pc00028 | lemma | high | PDF 352

Lemma III.2.1 that Te Y(Y; V).

## chapter-04-section-05-pc00029 | equation | low | PDF 352

[[FORMULA:f-p0352-05825]]

## chapter-04-section-05-pc00030 | ordinary-paragraph | high | PDF 352

(5.6) G(u) =q@gradW —f u=(curly,a@)eX. Then the Navier-Stokes problem is stated like in (4.32):

## chapter-04-section-05-pc00031 | equation | low | PDF 352

[[FORMULA:f-p0352-05828]]

## chapter-04-section-05-pc00032 | ordinary-paragraph | high | PDF 352

65.7) ps co, curl ) + (@ grad w, curl ¢) = (f,curld) Vde®,,

## chapter-04-section-05-pc00033 | equation | low | PDF 352

[[FORMULA:f-p0352-05830]]

## chapter-04-section-05-pc00034 | ordinary-paragraph | high | PDF 352

where w and w are related to u by (5.4). With T and G defined above and 4 = 1/y, this has the compact expression: (5.8) F(A,u) =u + ATG(u) = 0. For the purpose of the approximation, we introduce the first two finitedimensional spaces 9, and @, defined by (4.34):

## chapter-04-section-05-pc00035 | equation | low | PDF 352

[[FORMULA:f-p0352-05834]]

## chapter-04-section-05-pc00036 | ordinary-paragraph | high | PDF 352

where 7, is a triangulation of Q and the integer | > 1. Naturally we take

## chapter-04-section-05-pc00037 | equation | low | PDF 352

[[FORMULA:f-p0352-05836]]

## chapter-04-section-05-pc00038 | ordinary-paragraph | high | PDF 353

(59) V, = {(curl ¢,, ,,)€X;,; (curl g,, curl ,) = (9, H,) Vay € O,}. The discrete Stokes operator can be defined on a wider space than Y, namely:

## chapter-04-section-05-pc00039 | equation | low | PDF 353

[[FORMULA:f-p0353-05838]]

## chapter-04-section-05-pc00040 | ordinary-paragraph | high | PDF 353

equipped with the norm

## chapter-04-section-05-pc00041 | equation | low | PDF 353

[[FORMULA:f-p0353-05839]]

## chapter-04-section-05-pc00042 | ordinary-paragraph | high | PDF 353

drne®, |Puli.s,@ By setting

## chapter-04-section-05-pc00043 | equation | low | PDF 353

[[FORMULA:f-p0353-05840]]

## chapter-04-section-05-pc00044 | ordinary-paragraph | high | PDF 353

the space Y, can also be identified with a subspace of V,, the dual space of V,; thus we have the following continuous imbeddings:

## chapter-04-section-05-pc00045 | ordinary-paragraph | high | PDF 353

VE eanF acerWi ne It will be useful further on to provide Y, with the norm of V;, i.e. we put

## chapter-04-section-05-pc00046 | ordinary-paragraph | high | PDF 353

Lv

## chapter-04-section-05-pc00047 | equation | low | PDF 353

[[FORMULA:f-p0353-05841]]

## chapter-04-section-05-pc00048 | ordinary-paragraph | high | PDF 353

v,€ Vy, ll On llx clearly we have:

## chapter-04-section-05-pc00049 | equation | low | PDF 353

[[FORMULA:f-p0353-05842]]

## chapter-04-section-05-pc00050 | ordinary-paragraph | high | PDF 353

Then we define the approximate Stokes operator T),¢ (Y,; X;,) by: For le Y,, find T,! = (curl ,, @,)€ X ;, solution of

## chapter-04-section-05-pc00051 | equation | low | PDF 353

[[FORMULA:f-p0353-05844]]

## chapter-04-section-05-pc00052 | equation | low | PDF 353

[[FORMULA:f-p0353-05845]]

## chapter-04-section-05-pc00053 | equation | low | PDF 353

[[FORMULA:f-p0353-05846]]

## chapter-04-section-05-pc00054 | ordinary-paragraph | high | PDF 353

Obviously the range of the operator T,, is the space V,,.

## chapter-04-section-05-pc00055 | ordinary-paragraph | high | PDF 353

Now we turn to the upwind discretization of the convection term. Considering that Q is the union of all the triangles « of %,, formula (5.2) can be generalized to yield the following definition:

## chapter-04-section-05-pc00056 | ordinary-paragraph | high | PDF 353

u,(du;/0x;)v, dx

## chapter-04-section-05-pc00057 | equation | low | PDF 353

[[FORMULA:f-p0353-05848]]

## chapter-04-section-05-pc00058 | ordinary-paragraph | high | PDF 353,354

» ‘|u j(du,/0x;)v;dx + ig ue n(uer — yint)pint ish KET, This induces us to split the convection term and replace the single trilinear form by two forms: one for the volume integrals and one for the line integrals. Thus for all u = (curly, @) and v = (curl ¢, 0) in X, and all w of the form w; = 0%/0x; with x in ®, we set: KET, JK where u = curly and v = curl ¢; likewise for z = (curl v, ) in X;, we take: (5.13) atei.w) = >, | u-n(ve*t — vit')wit" ds, KET), J 0_K(z) where n denotes always the unit exterior normal to x, the superscript ext (resp. int) denotes the external (resp. internal) trace of the function on the boundary of kK and (5.14) O_K(z) = {xe 0k; (z:n)(x) <0}, z=curly, ie. 0_xk(z) is the portion of the boundary of x where the fluid with velocity z enters x. Finally, we introduce the form (5:85) a7 (u; v, W) = a,(u;v, w) + a5(u; v, W) and we define the mapping G,: ve X, > G,(v)e Y, by (5.16) <G,(v), curly > = a°(v; v, curl y) — (f,curly) VyeE®,. The continuity of G, will be established subsequently, but right away we observe that owing to the dependence of a3(v;v,w) on 0_x(v) the mapping G, is not differentiable. Note that when we H'!(Q)? the form a satisfies the crucial property justifying definition (5.11): (5:17) a”(u; v, W) = -| u;(Ow;/0x;)v; dx, whatever the function z, provided of course divu = 0 in Q andu-n=OonT. Then the Navier-Stokes Problem (5.7) has the following upwind discretization: Find ,€ ®, and w, € ©, solution of Bai ee ,, curl @,) + G""(u,;u,, curl g,) = (f,curld,) Vd,e®,,

## chapter-04-section-05-pc00059 | equation | low | PDF 354

[[FORMULA:f-p0354-05861]]

## chapter-04-section-05-pc00060 | ordinary-paragraph | high | PDF 354

with a defined by (5.12)-(5.15). Keeping in mind the above notations, this problem takes the form of( 3.58): (5.19) F(A, Uy) = Uy + AT, Ga(un) = 9, where u, = (curl y,,,) and 2 = 1/v. Note that F, maps A x X, into J,.

## chapter-04-section-05-pc00061 | subsection | high | PDF 354

5.2. Error Analysis of the Upwind Scheme

## chapter-04-section-05-pc00062 | ordinary-paragraph | high | PDF 354,355

Before applying the material of Section 3.4 to establish the convergence of (5.18), let us prove some important properties of the form G(.; ., .). The reader will find that this form is not as hard to manipulate as it would seem at first sight. First, the seminorm

## chapter-04-section-05-pc00063 | ordinary-paragraph | high | PDF 355

1/2 (5 68. Ke ZT, This is precisely the purpose of the space V,: it was shown in Chapter III that, under adequate conditions, the functions of V, satisfy the uniform stability properties: (5.20) |@rlisa2<GMArllo.g (cf. (11L.2.41)) Vu,= (curl ¢,, 4,)€ V,, (5.21) (= Bx) <C|l,llo,a (ef. (HI.2.65)) with constants independent of h. In other words:

## chapter-04-section-05-pc00064 | ordinary-paragraph | high | PDF 355

the seminorm of X: |v;| = ||9 ,\lo,q is anorm on V, uniformly equivalent to both IPrlr.a+ IlPrllo,@ and (» Prl3, a + ||@rllo,o for each t > 2. This suggests to adopt the following mesh-dependent norms: (5.22) [¢]. = (y l, Je ee ee.

## chapter-04-section-05-pc00065 | ordinary-paragraph | high | PDF 355

Next, since the functions ofX have little regularity, it will sometimes be useful to work with the following smoothing operator:

## chapter-04-section-05-pc00066 | equation | low | PDF 355

[[FORMULA:f-p0355-05871]]

## chapter-04-section-05-pc00067 | ordinary-paragraph | high | PDF 355

defined by

## chapter-04-section-05-pc00068 | ordinary-paragraph | high | PDF 355

for u = (curl y, m)e€ X, Pu = (curl ¢, «) is the solution of the Dirichlet problem (5.23) —Ad=a@ inQ, ¢=0 onl. When @ is convex, this function ¢ belongs indeed to H?(Q) and (5.24) IP llo,0< Cllllo,a- Clearly, the operator P reduces to the identity mapping on V. Moreover, when u, = (curl y,, @,) belongs to V, the corresponding function ¢ coincides with the function (h) introduced in the proof of Lemma III.2.5. In other words, u, = (curl y,,,@,)€V, and Pu,= (curl ¢, @,) are related by

## chapter-04-section-05-pc00069 | ordinary-paragraph | medium | PDF 355,356

Wr re P, the H-projection on ®, defined by (A.24): (5.25) (curl(P,¢ — ¢),curlw,)=0 Wu, e® ,,. The next lemma gives a useful estimate for [¢ — P,d|ik with 1 ≤ k ≤ l. Then we have the estimate:

## chapter-04-section-05-pc00070 | equation | low | PDF 356

[[FORMULA:f-p0356-05880]]

## chapter-04-section-05-pc00071 | equation | low | PDF 356

[[FORMULA:f-p0356-05881]]

## chapter-04-section-05-pc00072 | equation | low | PDF 356

[[FORMULA:f-p0356-05882]]

## chapter-04-section-05-pc00073 | ordinary-paragraph | medium | PDF 356

with constants C, independent of h. This lemma is an easy consequence of Theorem A.2 and

## chapter-04-section-05-pc00074 | equation | low | PDF 356

[[FORMULA:f-p0356-05883]]

## chapter-04-section-05-pc00075 | ordinary-paragraph | low | PDF 356

""中A

## chapter-04-section-05-pc00076 | equation | low | PDF 356

[[FORMULA:f-p0356-05884]]

## chapter-04-section-05-pc00077 | ordinary-paragraph | medium | PDF 356

These preliminaries permit to derive some fundamental properties of a( .; ., . ). First a(.; ., .) is bounded.

## chapter-04-section-05-pc00078 | lemma | medium | PDF 356

Lemma 5.2. Let us retain the assumptions of Lemma 5.1. The form a(.; ., .) is

## chapter-04-section-05-pc00079 | ordinary-paragraph | medium | PDF 356

bounded as follows, for all vhe Vh and all zh, uh = (u, = curl yh, wn), wh = (wh = curl xh, &n)e Xh:

## chapter-04-section-05-pc00080 | equation | low | PDF 356

[[FORMULA:f-p0356-05887]]

## chapter-04-section-05-pc00081 | equation | low | PDF 356

[[FORMULA:f-p0356-05888]]

## chapter-04-section-05-pc00082 | proof | medium | PDF 356

Proof. Let v, = (curl Φ,, O,) belong to V. By Holder's inequality, we have:

## chapter-04-section-05-pc00083 | ordinary-paragraph | medium | PDF 356

1/2

## chapter-04-section-05-pc00084 | equation | low | PDF 356

[[FORMULA:f-p0356-05890]]

## chapter-04-section-05-pc00085 | equation | low | PDF 356

[[FORMULA:f-p0356-05891]]

## chapter-04-section-05-pc00086 | ordinary-paragraph | low | PDF 356

KETn Thus (5.21) gives:

## chapter-04-section-05-pc00087 | equation | low | PDF 356

[[FORMULA:f-p0356-05893]]

## chapter-04-section-05-pc00088 | ordinary-paragraph | medium | PDF 356

Next, consider a2h(un; Pvh, wh) with Pv, = (curlΦ, On). As Φ belongs to H?(Ω), the surface integrals in a2(.; ., .) vanish over all interior segments k' of J, and since u, belongs to X, the factor curl y, · n vanishes on all boundary segments of J,. Hence

## chapter-04-section-05-pc00089 | equation | low | PDF 356

[[FORMULA:f-p0356-05896]]

## chapter-04-section-05-pc00090 | equation | low | PDF 356

[[FORMULA:f-p0356-05897]]

## chapter-04-section-05-pc00091 | ordinary-paragraph | medium | PDF 356

so that

## chapter-04-section-05-pc00092 | equation | low | PDF 356

[[FORMULA:f-p0356-05898]]

## chapter-04-section-05-pc00093 | ordinary-paragraph | medium | PDF 356

Therefore 1/4

## chapter-04-section-05-pc00094 | equation | low | PDF 356

[[FORMULA:f-p0356-05899]]

## chapter-04-section-05-pc00095 | equation | low | PDF 356

[[FORMULA:f-p0356-05900]]

## chapter-04-section-05-pc00096 | ordinary-paragraph | low | PDF 356

KETn 1/2

## chapter-04-section-05-pc00097 | equation | low | PDF 356

[[FORMULA:f-p0356-05901]]

## chapter-04-section-05-pc00098 | ordinary-paragraph | low | PDF 356

∑ IIcurl(Φn -~ Φ)16,0x KETn KE9h On the one hand a routine application of

## chapter-04-section-05-pc00099 | equation | low | PDF 356

[[FORMULA:f-p0356-05903]]

## chapter-04-section-05-pc00100 | equation | low | PDF 356

[[FORMULA:f-p0356-05904]]

## chapter-04-section-05-pc00101 | ordinary-paragraph | low | PDF 356,357

t≥ 1, 1/2 ∑ lcurl(Φn - Φ)1.ox 

## chapter-04-section-05-pc00102 | equation | low | PDF 357

[[FORMULA:f-p0357-05907]]

## chapter-04-section-05-pc00103 | ordinary-paragraph | low | PDF 357

[1Φn - Φl,2 + h KEgn KeJn On the other hand

## chapter-04-section-05-pc00104 | equation | low | PDF 357

[[FORMULA:f-p0357-05908]]

## chapter-04-section-05-pc00105 | ordinary-paragraph | low | PDF 357

Vke Jh VOneOn. Combining these inequalities with (5.22) for t = 2 we obtain:

## chapter-04-section-05-pc00106 | equation | low | PDF 357

[[FORMULA:f-p0357-05910]]

## chapter-04-section-05-pc00107 | equation | low | PDF 357

[[FORMULA:f-p0357-05911]]

## chapter-04-section-05-pc00108 | ordinary-paragraph | medium | PDF 357

The next lemma shows that a?*( ; ., . ) is “almost Lipschitz-continuous" with respect to zh.

## chapter-04-section-05-pc00109 | lemma | medium | PDF 357

Lemma 5.3. We keep the notations and assumptions of Lemma 5.2 but we suppose

## chapter-04-section-05-pc00110 | ordinary-paragraph | medium | PDF 357

that both vn and w, belong to Vh. For all pairs Z, = (zh, Sh) and z* = (z, S*) in Xh, the difference a?r - az# satisfies:

## chapter-04-section-05-pc00111 | ordinary-paragraph | low | PDF 357

[a²n(un;Uh,Wh) --a²(unUh, Wh) [llu, llo,4,2 if z* ≠ un

## chapter-04-section-05-pc00112 | equation | low | PDF 357

[[FORMULA:f-p0357-05913]]

## chapter-04-section-05-pc00113 | equation | low | PDF 357

[[FORMULA:f-p0357-05914]]

## chapter-04-section-05-pc00114 | equation | low | PDF 357

[[FORMULA:f-p0357-05915]]

## chapter-04-section-05-pc00115 | ordinary-paragraph | low | PDF 357

Vuh,Zh,2#∈Xh Vuh, Whe Vh.

## chapter-04-section-05-pc00116 | proof | medium | PDF 357

Proof. This proof is based on the identity:

## chapter-04-section-05-pc00117 | ordinary-paragraph | low | PDF 357

a²n(un;Un,Wh)—a2(unUn,Wn)

## chapter-04-section-05-pc00118 | equation | low | PDF 357

[[FORMULA:f-p0357-05916]]

## chapter-04-section-05-pc00119 | ordinary-paragraph | low | PDF 357

vinl)(wint —wex)ds x∈JhJ0_x(zn,-zh) where

## chapter-04-section-05-pc00120 | equation | low | PDF 357

[[FORMULA:f-p0357-05917]]

## chapter-04-section-05-pc00121 | ordinary-paragraph | medium | PDF 357

Thus, in view of (5.29) we can replace not only v, by vh - Pu, but also w, by Wh -- Pwh. This gives:

## chapter-04-section-05-pc00122 | ordinary-paragraph | medium | PDF 357

1/4

## chapter-04-section-05-pc00123 | equation | low | PDF 357

[[FORMULA:f-p0357-05919]]

## chapter-04-section-05-pc00124 | ordinary-paragraph | low | PDF 357

[a²(un;Uh,Wn) —a²(un;Un,Wn)/ ≤ C KEgn 1/4

## chapter-04-section-05-pc00125 | equation | low | PDF 357

[[FORMULA:f-p0357-05921]]

## chapter-04-section-05-pc00126 | ordinary-paragraph | low | PDF 357,358

KETn 1/2 Ilcurl(xh - x)l1,ox KEgn Then the techniques of the preceding lemma easily yield: Hence (5.31) follows from Lemma 5.1 and (5.24) in the general case. To handle the particular case where z* = un, we observe that:

## chapter-04-section-05-pc00127 | equation | low | PDF 358

[[FORMULA:f-p0358-05924]]

## chapter-04-section-05-pc00128 | equation | low | PDF 358

[[FORMULA:f-p0358-05925]]

## chapter-04-section-05-pc00129 | ordinary-paragraph | medium | PDF 358

Therefore the factor u, : n in the right-hand side of (5.32) can be bounded by the difference I(u, - zh)· n| = I(z* - zh) · nl. It can be readily checked that the remainder of the above argument is still valid with this modification. 口

## chapter-04-section-05-pc00130 | ordinary-paragraph | medium | PDF 358

Finally, we can prove another interesting bound for a(.; ., .).

## chapter-04-section-05-pc00131 | lemma | medium | PDF 358

Lemma 5.4. We retain the assumptions and notations of Lemma 5.3 except that we

## chapter-04-section-05-pc00132 | ordinary-paragraph | medium | PDF 358

take vn in Xn. Then we have the following estimate for all z = (curla,β) with α ∈ H²(Ω) ∩ H(Ω) and β∈ L²(Ω):

## chapter-04-section-05-pc00133 | equation | low | PDF 358

[[FORMULA:f-p0358-05929]]

## chapter-04-section-05-pc00134 | equation | low | PDF 358

[[FORMULA:f-p0358-05930]]

## chapter-04-section-05-pc00135 | ordinary-paragraph | low | PDF 358

VWhe Vh, Vuh, UhE Xh. where the line integrals in a2(.; ., .) are taken over any portion of 0k.

## chapter-04-section-05-pc00136 | proof | medium | PDF 358

Proof. Take Pw, = (w = curl x,&,) and set z = curl α. The linearity ofa(.; ., . ) with

## chapter-04-section-05-pc00137 | ordinary-paragraph | medium | PDF 358

respect to its last argument permits to write:

## chapter-04-section-05-pc00138 | equation | low | PDF 358

[[FORMULA:f-p0358-05932]]

## chapter-04-section-05-pc00139 | ordinary-paragraph | medium | PDF 358

Since w belongs to H1(Q) we can apply the identity (5.17):

## chapter-04-section-05-pc00140 | equation | low | PDF 358

[[FORMULA:f-p0358-05934]]

## chapter-04-section-05-pc00141 | ordinary-paragraph | medium | PDF 358

so that Lemma 5.2 and (5.24) give:

## chapter-04-section-05-pc00142 | equation | low | PDF 358

[[FORMULA:f-p0358-05936]]

## chapter-04-section-05-pc00143 | equation | low | PDF 358

[[FORMULA:f-p0358-05937]]

## chapter-04-section-05-pc00144 | ordinary-paragraph | medium | PDF 358

Likewise, we have 1/2

## chapter-04-section-05-pc00145 | equation | low | PDF 358

[[FORMULA:f-p0358-05938]]

## chapter-04-section-05-pc00146 | ordinary-paragraph | low | PDF 358

II wh - wIllo,4,52 KETh 1/2

## chapter-04-section-05-pc00147 | equation | low | PDF 358

[[FORMULA:f-p0358-05939]]

## chapter-04-section-05-pc00148 | ordinary-paragraph | low | PDF 358

KETh in view of (5.22) and Lemma 5.1. Therefore [a(un; Uh - Z, Wh —W)] + |a(un;Un - Z, w)] ≤ C4hi/2 1/unllo,4,q/wn1 [Φh — α]4. Finally, like in Lemma 5.2, we derive

## chapter-04-section-05-pc00149 | equation | low | PDF 359

[[FORMULA:f-p0359-05942]]

## chapter-04-section-05-pc00150 | ordinary-paragraph | high | PDF 359

By collecting these inequalities, we obtain (5.34). O

## chapter-04-section-05-pc00151 | remark | high | PDF 359

Remark 5.1. It follows from Lemma 5.2 and the argument of Lemma 5.3 that the

## chapter-04-section-05-pc00152 | ordinary-paragraph | high | PDF 359

mapping G, is Lipschitz-continuous on J,: (9.35) Giln) — Gaur Ile < Clay] + [ut |)lu, — ut] Vayu,it eV, with a constant C independent of h.

## chapter-04-section-05-pc00153 | ordinary-paragraph | high | PDF 359

Now we are in a position to define the operator VG,(u,), i.e. to approach as best as we can the “derivative” of the form 4(.; ., .). Clearly, the simplest guess is to linearize the dependence of G7"(.; ., .) with respect to z,. Thus we set:

## chapter-04-section-05-pc00154 | definition | high | PDF 359

Definition 5.1. For all u,€ V,, the operator VG,(u,)¢ L(V,; ¥,) is defined by

## chapter-04-section-05-pc00155 | ordinary-paragraph | high | PDF 359

<VG,(UyUp), *Wa > = G""(UVpy_,5 W, ) + G""(Uq5 Uns Wy) Vw, = curl y,, %,€ ®,. Obviously ’G,(u,) is a linear operator from V, into Y, and Lemma 5.2 implies that

## chapter-04-section-05-pc00156 | equation | low | PDF 359

[[FORMULA:f-p0359-05946]]

## chapter-04-section-05-pc00157 | ordinary-paragraph | high | PDF 359

with a constant C independent of h.

## chapter-04-section-05-pc00158 | remark | high | PDF 359

Remark 5.2. Note that VG,(u,) is “nearly Lipschitz-continuous” with respect to

## chapter-04-section-05-pc00159 | ordinary-paragraph | high | PDF 359

u,. Indeed,

## chapter-04-section-05-pc00160 | ordinary-paragraph | high | PDF 359

|G, (un) — VG, (uiPtn) Wn > |= [G"(Up5 Ons Wa) — GY (UFDEyS,W y) Os" (0j,, Uy Wp) a'*(v,; ui, W;,)|

## chapter-04-section-05-pc00161 | equation | low | PDF 359

[[FORMULA:f-p0359-05948]]

## chapter-04-section-05-pc00162 | ordinary-paragraph | high | PDF 359

ox G** (ux; 0), W,)| + |G""(v,;U j,— Up, Wi)| + |a"™(uvk,,3 W h)— G"*(vuky,; w, )|

## chapter-04-section-05-pc00163 | equation | low | PDF 359

[[FORMULA:f-p0359-05949]]

## chapter-04-section-05-pc00164 | ordinary-paragraph | high | PDF 359

+ h*?(\\u, — uf llo,a.o + lug |), by applying Lemmas 5.3 and 5.4. Hence

## chapter-04-section-05-pc00165 | equation | low | PDF 359

[[FORMULA:f-p0359-05950]]

## chapter-04-section-05-pc00166 | ordinary-paragraph | high | PDF 359

Of course, we can derive a similar upper bound with the term h'?|u,| in the right-hand side.

## chapter-04-section-05-pc00167 | ordinary-paragraph | high | PDF 359

Finally in order to apply Theorem 3.8, it is necessary to relate the operator G defined by (5.6) with the operator that corresponds to the trilinear form

## chapter-04-section-05-pc00168 | equation | low | PDF 360

[[FORMULA:f-p0360-05952]]

## chapter-04-section-05-pc00169 | ordinary-paragraph | high | PDF 360

Hence

## chapter-04-section-05-pc00170 | equation | low | PDF 360

[[FORMULA:f-p0360-05953]]

## chapter-04-section-05-pc00171 | ordinary-paragraph | high | PDF 360

provided y has the regularity H2. Of course, when u belongs only to X this Thus we define for all u in X:

## chapter-04-section-05-pc00172 | equation | low | PDF 360

[[FORMULA:f-p0360-05954]]

## chapter-04-section-05-pc00173 | equation | low | PDF 360

[[FORMULA:f-p0360-05955]]

## chapter-04-section-05-pc00174 | ordinary-paragraph | low | PDF 360

Since Pu = u for all u in V, this definition coincides with (5.6) when ue V and V = curl Φ, Φe Φ,. Furthermore, it can be readily checked that (5.36) defines a @∞_ mapping G: X → Y whose derivative DG(u)e &(X; Y) is given by the expression: z(U)sTMA (

## chapter-04-section-05-pc00175 | equation | low | PDF 360

[[FORMULA:f-p0360-05958]]

## chapter-04-section-05-pc00176 | equation | low | PDF 360

[[FORMULA:f-p0360-05959]]

## chapter-04-section-05-pc00177 | ordinary-paragraph | high | PDF 360

Finally, it can be proved that u is a nonsingular solution of (5.7) whenever u is also a nonsingular solution of the Navier-Stokes problem with G defined by (5.36), and conversely. Let us check the assumptions of Theorem 3.8. It follows readily from (5.10) that

## chapter-04-section-05-pc00178 | equation | low | PDF 360

[[FORMULA:f-p0360-05963]]

## chapter-04-section-05-pc00179 | equation | low | PDF 360

[[FORMULA:f-p0360-05964]]

## chapter-04-section-05-pc00180 | ordinary-paragraph | high | PDF 360

where C, denotes the constant of (5.20). Next, (3.60) has already been checked in Section 4.3: owing to the regularity condition (4.18) T,f = (curl yh, w,) satisfies the error estimate

## chapter-04-section-05-pc00181 | equation | low | PDF 360

[[FORMULA:f-p0360-05967]]

## chapter-04-section-05-pc00182 | equation | low | PDF 360

[[FORMULA:f-p0360-05968]]

## chapter-04-section-05-pc00183 | ordinary-paragraph | high | PDF 360

where r ≤t < 2, 1/y + 1/t = 1, α = 1/y when I = 1 and α = 2/v when l ≥ 2. Likewise, the approximation properties of the operator π, have been derived in Section IH1.3.1. Indeed, for v = (curl Φ, 0)e V we take

## chapter-04-section-05-pc00184 | equation | low | PDF 360

[[FORMULA:f-p0360-05971]]

## chapter-04-section-05-pc00185 | equation | low | PDF 360

[[FORMULA:f-p0360-05972]]

## chapter-04-section-05-pc00186 | ordinary-paragraph | high | PDF 360

i.e. 0, is determined by

## chapter-04-section-05-pc00187 | equation | low | PDF 360

[[FORMULA:f-p0360-05973]]

## chapter-04-section-05-pc00188 | equation | low | PDF 360

[[FORMULA:f-p0360-05974]]

## chapter-04-section-05-pc00189 | ordinary-paragraph | high | PDF 360

Then

## chapter-04-section-05-pc00190 | equation | low | PDF 360

[[FORMULA:f-p0360-05975]]

## chapter-04-section-05-pc00191 | ordinary-paragraph | low | PDF 360

μh∈n

## chapter-04-section-05-pc00192 | equation | low | PDF 360

[[FORMULA:f-p0360-05976]]

## chapter-04-section-05-pc00193 | equation | low | PDF 360

[[FORMULA:f-p0360-05977]]

## chapter-04-section-05-pc00194 | ordinary-paragraph | low | PDF 360

Il μnllo,α u034n Therefore Lemma H1.3.2, Theorem A.2 and a standard density argument yield

## chapter-04-section-05-pc00195 | equation | low | PDF 360

[[FORMULA:f-p0360-05978]]

## chapter-04-section-05-pc00196 | ordinary-paragraph | high | PDF 360

h→0

## chapter-04-section-05-pc00197 | equation | low | PDF 361

[[FORMULA:f-p0361-05979]]

## chapter-04-section-05-pc00198 | ordinary-paragraph | low | PDF 361

Now we turn to (3.62); we have <Gn(πnu)—G(u),n>=an"(πnu;πnu,vn)-a(u;u,Vn) Hvh = curl Φh, Φh E Φh. Using a simple rearrangement of terms we obtain:

## chapter-04-section-05-pc00199 | equation | low | PDF 361

[[FORMULA:f-p0361-05983]]

## chapter-04-section-05-pc00200 | ordinary-paragraph | medium | PDF 361

Therefore Lemma 5.4 and Lemma 5.2 together with (5.22) yield:

## chapter-04-section-05-pc00201 | ordinary-paragraph | low | PDF 361

[ -]( + ≥()  (n)" 

## chapter-04-section-05-pc00202 | equation | low | PDF 361

[[FORMULA:f-p0361-05986]]

## chapter-04-section-05-pc00203 | ordinary-paragraph | medium | PDF 361

Hence (3.62) follows from Lemma 5.1. Furthermore we infer from this lemma and (5.41) that

## chapter-04-section-05-pc00204 | equation | low | PDF 361

[[FORMULA:f-p0361-05989]]

## chapter-04-section-05-pc00205 | equation | low | PDF 361

[[FORMULA:f-p0361-05990]]

## chapter-04-section-05-pc00206 | ordinary-paragraph | low | PDF 361

Vu = (curly,w)e V with y e Hk+1(Q), 1 ≤ k ≤ l. As far as (3.63) is concerned, we apply Definition 5.1 and (5.37): <(DGh(πhu) —DG(u))·Un,Wn>=an"(πhu;Un,Wn) +amh"(Uh;πnu, Wn) AsnA —a(u; Pvh,Wh) —a(Un;u, Wh) =aπn"(πhu;Un——PunWn)+an"(Unnu—u,Wh) + a(πnu ——u; Pvh, Wh) taking into account the regularity of u and Pv,. Consequently, it stems from

## chapter-04-section-05-pc00207 | lemma | medium | PDF 361

Lemma 5.3 and 5.4 that:

## chapter-04-section-05-pc00208 | ordinary-paragraph | low | PDF 361

i1(DGn(πhu) -DG(u)·vnllh ≤ C{h1/²(1Phl1,4,o[Φh-Φ]4 + Iun1 [Pn -↓]4) + |unl/Pny -Wl1,4.2}, with Pun = (curl Φ, On), Vu = (curl y,w)e V, Vun = (curl Φh, On)e Vh. Thus Lemma 5.1 gives:

## chapter-04-section-05-pc00209 | equation | low | PDF 361

[[FORMULA:f-p0361-05997]]

## chapter-04-section-05-pc00210 | ordinary-paragraph | medium | PDF 361

which implies (3.63).

## chapter-04-section-05-pc00211 | ordinary-paragraph | low | PDF 361

Finally, it remains to verify (3.64). Take uh, u* and u in V; by definition we have for all w, = curl Xh, Xh E Φh: (Gn(un)—Gn(u)-DGn(uh)·(un-u),wn>

## chapter-04-section-05-pc00212 | ordinary-paragraph | low | PDF 361,362

=a"n(unun,Wn)-aur(u;u,wn) -au%(u%;un——u,wn)-—a"%(un——u;u,Wn) =a"%(un—u;un—u,wn)+aun(un—u;u—uh,wn)+{ar(un;un,Wh) {a3"(U, — Up; Uy, Wh) — ast(u, psUy, Wa) oe {as*(u uy, — Uj, Wp) — ah(ui;u w,— uit,w ,)} + {a3(uUin,s W r)— a3" (US Uy, Wa) }- Then using repeatedly Lemma 5.3 this expression can be bounded by: Ch? {|u y| Wi, — Witlia.a + Wir — Wr li.4,alUn — url} |,

## chapter-04-section-05-pc00213 | equation | low | PDF 362

[[FORMULA:f-p0362-06004]]

## chapter-04-section-05-pc00214 | ordinary-paragraph | high | PDF 362

Hence Lemma 5.2 gives the bound | G,(Un) — Gut) — VG, (up) (Un — UDI

## chapter-04-section-05-pc00215 | equation | low | PDF 362

[[FORMULA:f-p0362-06005]]

## chapter-04-section-05-pc00216 | ordinary-paragraph | high | PDF 362

This implies (3.64) with the function

## chapter-04-section-05-pc00217 | equation | low | PDF 362

[[FORMULA:f-p0362-06007]]

## chapter-04-section-05-pc00218 | ordinary-paragraph | high | PDF 362

Clearly L,, is continuous, monotonically increasing with respect to each variable and

## chapter-04-section-05-pc00219 | equation | low | PDF 362

[[FORMULA:f-p0362-06008]]

## chapter-04-section-05-pc00220 | equation | low | PDF 362

[[FORMULA:f-p0362-06009]]

## chapter-04-section-05-pc00221 | ordinary-paragraph | high | PDF 362

Since all the assumptions of Theorem 3.8 are satisfied, we can apply its conclusion to the upwind scheme (5.18), thus deriving the existence, uniqueness and convergence of its branch of solutions. Furthermore, by comparing the two error estimates (3.67) and (3.41) and taking into account (5.42) we readily deduce that the error of the upwind scheme is bounded exactly like the error of the centered scheme. In other words, in this case the upwinding does not alter the scheme’s order. These results are summed up in the following theorem.

## chapter-04-section-05-pc00222 | theorem | high | PDF 362

Theorem 5.1. Let Q be a bounded, convex polygon and JF, a uniformiy regular

## chapter-04-section-05-pc00223 | ordinary-paragraph | high | PDF 362

family of triangulations of Q. For fe L'(Q)?, te[r, 2) let

## chapter-04-section-05-pc00224 | equation | low | PDF 362

[[FORMULA:f-p0362-06012]]

## chapter-04-section-05-pc00225 | ordinary-paragraph | high | PDF 362

be a branch of nonsingular solutions of the Navier-Stokes Problem (5.7). Then for h < hg small enough there exists a unique branch

## chapter-04-section-05-pc00226 | equation | low | PDF 362

[[FORMULA:f-p0362-06015]]

## chapter-04-section-05-pc00227 | ordinary-paragraph | high | PDF 362

of €°-solutions of the upwind scheme (5.18) satisfying the error estimate:

## chapter-04-section-05-pc00228 | equation | low | PDF 362

[[FORMULA:f-p0362-06017]]

## chapter-04-section-05-pc00229 | ordinary-paragraph | high | PDF 362

(5.43) l/yy ifl=1,

## chapter-04-section-05-pc00230 | equation | low | PDF 362

[[FORMULA:f-p0362-06019]]

## chapter-04-section-05-pc00231 | equation | low | PDF 362

[[FORMULA:f-p0362-06020]]

## chapter-04-section-05-pc00232 | ordinary-paragraph | high | PDF 362

with a constant C independent of h or 2.

## chapter-04-section-05-pc00233 | equation | low | PDF 363

[[FORMULA:f-p0363-06021]]

## chapter-04-section-05-pc00234 | ordinary-paragraph | low | PDF 363

In addition, when the mapping Λ → y(a) is continuous from A into Hm+2(Q)N :aapy am [z/1 - 1'1]≥u ppau auos dof () z/e +uM

## chapter-04-section-05-pc00235 | equation | low | PDF 363

[[FORMULA:f-p0363-06023]]

## chapter-04-section-05-pc00236 | equation | low | PDF 363

[[FORMULA:f-p0363-06024]]

## chapter-04-section-05-pc00237 | ordinary-paragraph | low | PDF 363

AeA Finally, an argument closely resembling that of Section 4.3 permits to refine the error estimate for |y - yhli.o and obtain the same order of convergence as

## chapter-04-section-05-pc00238 | theorem | medium | PDF 363

Theorem 4.5.

## chapter-04-section-05-pc00239 | theorem | medium | PDF 363

Theorem 5.2. Let Q and J, be like in Theorem 5.1 and assume that the branch of

## chapter-04-section-05-pc00240 | ordinary-paragraph | medium | PDF 363

nonsingular solutions of the Navier-Stokes Problem (5.7) has the regularity:

## chapter-04-section-05-pc00241 | equation | low | PDF 363

[[FORMULA:f-p0363-06026]]

## chapter-04-section-05-pc00242 | ordinary-paragraph | medium | PDF 363

Then the approximate solution Wn of the upwind scheme (5.18) satisfies the error bound:

## chapter-04-section-05-pc00243 | equation | low | PDF 363

[[FORMULA:f-p0363-06028]]

## chapter-04-section-05-pc00244 | equation | low | PDF 363

[[FORMULA:f-p0363-06029]]

## chapter-04-section-05-pc00245 | equation | low | PDF 363

[[FORMULA:f-p0363-06030]]

## chapter-04-section-05-pc00246 | equation | low | PDF 363

[[FORMULA:f-p0363-06031]]

## chapter-04-section-05-pc00247 | ordinary-paragraph | medium | PDF 363

with constants independent of h and X.

## chapter-04-section-05-pc00248 | proof | medium | PDF 363

Proof. Let g be any function of L?(Ω)² and let us introduce the following dual

## chapter-04-section-05-pc00249 | ordinary-paragraph | medium | PDF 363

linearized Navier-Stokes problem, analogous to (4.40):

## chapter-04-section-05-pc00250 | equation | low | PDF 363

[[FORMULA:f-p0363-06033]]

## chapter-04-section-05-pc00251 | equation | low | PDF 363

[[FORMULA:f-p0363-06034]]

## chapter-04-section-05-pc00252 | equation | low | PDF 363

[[FORMULA:f-p0363-06035]]

## chapter-04-section-05-pc00253 | ordinary-paragraph | medium | PDF 363

Vv = (v = curl Φ, 0)e V. We know that on the one hand:

## chapter-04-section-05-pc00254 | equation | low | PDF 363

[[FORMULA:f-p0363-06037]]

## chapter-04-section-05-pc00255 | ordinary-paragraph | medium | PDF 363

and on the other hand:

## chapter-04-section-05-pc00256 | equation | low | PDF 363

[[FORMULA:f-p0363-06038]]

## chapter-04-section-05-pc00257 | ordinary-paragraph | medium | PDF 363

for all u, v and z in V. Therefore Problem (5.46) is the same as Problem (4.40) and hence its solution enjoys the regularity properties stated in Lemma 4.1.

## chapter-04-section-05-pc00258 | ordinary-paragraph | low | PDF 363

Now, by reasoning like in Theorem 4.5 we readily obtain: (g,curl(b -— yn)) =(v- Vn,C -—@n) + b(u --uh,v -— 0n) + b(z - Zh,@ - μn)

## chapter-04-section-05-pc00259 | ordinary-paragraph | low | PDF 363,364

+Aa(u —un;u,z) -Aa(u,z,u -un) —Aa(u;u,Zh) +Aa(un;un,Zn) +Aan(un;uh,Zh) (g,curl(y -Vn)) = (v-Vh,@ -Wn) + b(u -—un,v- On) + b(z —Zh( -μn) +A{a(u-unu,z-—Zn) + a“n(unu—unz-Zh)

## chapter-04-section-05-pc00260 | equation | low | PDF 364

[[FORMULA:f-p0364-06042]]

## chapter-04-section-05-pc00261 | ordinary-paragraph | low | PDF 364

-- a(u -un;z,u- un)}. But, the delicate step in this proof is an adequate estimate of the a(.; ., .) term in the factor multiplying . Indeed, if we apply Lemma 5.2, we get:

## chapter-04-section-05-pc00262 | equation | low | PDF 364

[[FORMULA:f-p0364-06043]]

## chapter-04-section-05-pc00263 | ordinary-paragraph | medium | PDF 364

And when I = 1, this upper bound is useless because infx, [x - xh]2 = O(1). Instead, it is better to take advantage of the fact that xe H?(Q) and replace the previous bound by:

## chapter-04-section-05-pc00264 | equation | low | PDF 364

[[FORMULA:f-p0364-06045]]

## chapter-04-section-05-pc00265 | equation | low | PDF 364

[[FORMULA:f-p0364-06046]]

## chapter-04-section-05-pc00266 | ordinary-paragraph | low | PDF 364

1x-xnl1,4, + h( KETh Hence, if we choose zh = Thz e Vh defined by (5.40), the fact that Xn = Phx implies that

## chapter-04-section-05-pc00267 | equation | low | PDF 364

[[FORMULA:f-p0364-06048]]

## chapter-04-section-05-pc00268 | ordinary-paragraph | medium | PDF 364

Finally, observe that

## chapter-04-section-05-pc00269 | equation | low | PDF 364

[[FORMULA:f-p0364-06049]]

## chapter-04-section-05-pc00270 | equation | low | PDF 364

[[FORMULA:f-p0364-06050]]

## chapter-04-section-05-pc00271 | equation | low | PDF 364

[[FORMULA:f-p0364-06051]]

## chapter-04-section-05-pc00272 | ordinary-paragraph | low | PDF 364

by virtue of (5.26), (5.21) and (5.40). This gives an upper bound of the form: [aun(un;u - uh, Z - Zh)/ ≤ Cs(lly l/2.s) /x ll 2.4.o(h' l/yll1+1,o + h|πnu - u,l). The other terms in (5.47) are easily estimated and the proof ends exactly like that of Theorem 4.5. 口

## chapter-04-section-05-pc00273 | subsection | medium | PDF 364

5.3. Approximating the Pressure with the Upwind Scheme

## chapter-04-section-05-pc00274 | ordinary-paragraph | medium | PDF 364

We have seen in Section 4.3 that the pressure term p underlying the Navier-Stokes system (5.7) is the solution of the problem: Find pe Wi,r(Q)N L?(Q) such that:

## chapter-04-section-05-pc00275 | equation | low | PDF 364

[[FORMULA:f-p0364-06056]]

## chapter-04-section-05-pc00276 | ordinary-paragraph | low | PDF 364

()s,M bA (5.49)  (grad p,grad q) f - vcurlo -

## chapter-04-section-05-pc00277 | equation | low | PDF 364

[[FORMULA:f-p0364-06058]]

## chapter-04-section-05-pc00278 | ordinary-paragraph | medium | PDF 364,365

Likewise, to recover the pressure ph associated with the upwind scheme (5.18), we introduce the space Q, defined by (4.34): and we discretize (5.49) by:

## chapter-04-section-05-pc00279 | ordinary-paragraph | medium | PDF 365

Find ph e Qn satisfying:

## chapter-04-section-05-pc00280 | equation | low | PDF 365

[[FORMULA:f-p0365-06062]]

## chapter-04-section-05-pc00281 | equation | low | PDF 365

[[FORMULA:f-p0365-06063]]

## chapter-04-section-05-pc00282 | ordinary-paragraph | low | PDF 365

"0="bA Obviously, this problem has a unique solution.

## chapter-04-section-05-pc00283 | ordinary-paragraph | medium | PDF 365

To estimate the error p - ph we use the same duality argument as in Theorem 111.2.7. We introduce the function ve H1 (Q) defined by

## chapter-04-section-05-pc00284 | equation | low | PDF 365

[[FORMULA:f-p0365-06065]]

## chapter-04-section-05-pc00285 | ordinary-paragraph | medium | PDF 365

which we can split into

## chapter-04-section-05-pc00286 | equation | low | PDF 365

[[FORMULA:f-p0365-06066]]

## chapter-04-section-05-pc00287 | ordinary-paragraph | medium | PDF 365

Since Q is assumed to be a convex polygon, both q and Φ belong to H?(Ω) with

## chapter-04-section-05-pc00288 | equation | low | PDF 365

[[FORMULA:f-p0365-06067]]

## chapter-04-section-05-pc00289 | ordinary-paragraph | medium | PDF 365

In addition, if the triangulation , is uniformly regular Lemma Il1.2.6 shows that

## chapter-04-section-05-pc00290 | equation | low | PDF 365

[[FORMULA:f-p0365-06068]]

## chapter-04-section-05-pc00291 | equation | low | PDF 365

[[FORMULA:f-p0365-06069]]

## chapter-04-section-05-pc00292 | ordinary-paragraph | medium | PDF 365

Now, like in Theorem I11.2.7 we can write: II p -- Phll2,α = (grad(qh - p), grad(q - Phq) + (grad(ph -- p), grad(Phq)) VaneQn. Thus, to estimate p - ph, we must derive a sharp bound for thc second term. By subtracting (5.49) from (5.51) we obtain:

## chapter-04-section-05-pc00293 | ordinary-paragraph | medium | PDF 365

(grad(Ph - p), grad(P:q)) = - v(curl(wn - (), grad(Phq)) + a,(u; u, grad(Phq))

## chapter-04-section-05-pc00294 | equation | low | PDF 365

[[FORMULA:f-p0365-06073]]

## chapter-04-section-05-pc00295 | equation | low | PDF 365

[[FORMULA:f-p0365-06074]]

## chapter-04-section-05-pc00296 | ordinary-paragraph | low | PDF 365

+ a"n(unu -uhVh-v) + a(u-uhu,Vh -v) + a(uh - u;v,un) + a(u;v,un - u) where

## chapter-04-section-05-pc00297 | equation | low | PDF 365

[[FORMULA:f-p0365-06075]]

## chapter-04-section-05-pc00298 | ordinary-paragraph | medium | PDF 365

Therefore (5.52) together with familiar estimates for the forms a"(.; ., .) and a1(.; ., .) give a result analogous to (I11.2.38).

## chapter-04-section-05-pc00299 | lemma | medium | PDF 365

Lemma 5.5. Let Q be a bounded, convex polygon and J, a uniformly regular

## chapter-04-section-05-pc00300 | ordinary-paragraph | medium | PDF 365

triangulation of Ω. If p and w belong to W1,(Ω) for some real t e [r,2] then the error on p is:
