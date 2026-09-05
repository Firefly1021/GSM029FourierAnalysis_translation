# Restored-source review candidate: chapter-04-section-02



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 298 / printed 284



[p0298-b0003 | ordinary-paragraph | high] As we have seen in Paragraph I.5, the stationary Navier-Stokes equations may

[p0298-b0004 | ordinary-paragraph | high] be written in the form

[p0298-b0005 | ordinary-paragraph | high] N

[p0298-b0006 | equation | low] —vAu+ ) udu/dx, + gradp = f,

[p0298-b0007 | ordinary-paragraph | high] (2.1) d owen inQ

[p0298-b0008 | equation | low] divu = 0,

[p0298-b0009 | ordinary-paragraph | high] f given in H-1(Q)",

[p0298-b0010 | ordinary-paragraph | high] where again Q is a bounded domain of R* (N = 2, 3) with a Lipschitz-continuous

[p0298-b0011 | ordinary-paragraph | high] boundary J. In this paragraph, we want to derive from the abstract material of

[p0298-b0012 | section | high] §1 existence and uniqueness results for various formulations of the Navier-Stokes

[p0298-b0013 | ordinary-paragraph | high] equations.

[p0298-b0014 | subsection | high] 2.1. The Dirichlet Problem in the Velocity-Pressure Formulation

[p0298-b0015 | ordinary-paragraph | high] We first consider the case of the homogeneous Dirichlet boundary condition

[p0298-b0016 | ordinary-paragraph | high] (2.2) u=0 onl.

[p0298-b0017 | ordinary-paragraph | high] In order to write Problem (2.1), (2.2) in a variational form, we introduce the

[p0298-b0018 | ordinary-paragraph | high] trilinear form

[p0298-b0019 | ordinary-paragraph | high] (2.3) a,(W; u,v) = s dela Crane nh oe

[p0298-b0020 | ordinary-paragraph | high] The next two lemmas state useful properties of the trilinear form a,(.; ., .).

[p0298-b0021 | lemma | high] Lemma 2.1. For N < 4, the trilinear form a,(.; ., .) is continuous on (H}(Q)%)?,

[p0298-b0022 | proof | high] Proof. According to the Sobolev Imbedding Theorem I.1.3, the space H'(Q) is

[p0298-b0023 | ordinary-paragraph | high] continuously imbedded in L*(Q) for N < 4. Then by Hdlder’s inequality, we have

[p0298-b0024 | ordinary-paragraph | high] if u, v, we H'(Q)*:

[p0298-b0025 | equation | low] w;(du,/Ox;)v,EL1(Q), 1<i,j <Q,

[p0298-b0026 | ordinary-paragraph | high] with

[p0298-b0027 | equation | low] | w,(0u;/Ox;)v; dx| < ||W yllo,4,a ll0 u;/0X;llo,a ll¥ illo,4,0

[p0298-b0028 | equation | low] <C, || w; I 1,214il1,allllia-

[p0298-b0029 | ordinary-paragraph | high] Thus, the form a,(.;., .) is well defined and continuous on (H!(Q)%)? and

[p0298-b0030 | ordinary-paragraph | high] |a,(wsu,v)| < CylolluV ilila llyW ili .a- O

## PDF 299 / printed 285



[p0299-b0004 | ordinary-paragraph | medium] Then, we have:

[p0299-b0005 | equation | low] (2.4)

[p0299-b0006 | equation | low] a(w;u, v) + a(w; v,u) = 0,

[p0299-b0007 | equation | low] (2.5)

[p0299-b0008 | equation | low] a1(w; v, v) = 0.

[p0299-b0009 | proof | medium] Proof. Clearly, the properties (2.4) and (2.5) are equivalent and it suffices to check

[p0299-b0010 | ordinary-paragraph | medium] (2.5). Let ve D(Q) and we H'(Ω); we may write:

[p0299-b0011 | equation | low] a,(w;v,v) =(1/2) ∑

[p0299-b0012 | ordinary-paragraph | medium] w;0(v2)/0x;dx

[p0299-b0013 | equation | low] i,j=1 JΩ

[p0299-b0014 | ordinary-paragraph | medium] and by Green's formula (1.2.17):

[p0299-b0015 | ordinary-paragraph | medium] N

[p0299-b0016 | equation | low] div wv; dx +

[p0299-b0017 | equation | low] a(w;v,v) = --(1/2) ∑

[p0299-b0018 | ordinary-paragraph | medium] w·nv; ds

[p0299-b0019 | equation | low] i,j=1

[p0299-b0020 | ordinary-paragraph | low] Vr

[p0299-b0021 | ordinary-paragraph | medium] When w satisfies div w = O and w· nl r = O, this implies

[p0299-b0022 | equation | low] a,(w; v, v) = 0.

[p0299-b0023 | ordinary-paragraph | medium] Then the lemma follows by using the density of D(Ω) into H1(Q) (cf. Theorem

[p0299-b0024 | ordinary-paragraph | medium] 1.1.2).

[p0299-b0025 | ordinary-paragraph | medium] 口

[p0299-b0026 | ordinary-paragraph | medium] Now, recall the following spaces:

[p0299-b0027 | equation | low]  = {v∈ D(Ω); divv = 0},

[p0299-b0028 | equation | low] V = {ve H(Ω)'; divv = 0}.

[p0299-b0029 | ordinary-paragraph | medium] We set

[p0299-b0030 | equation | low] ao(u, v) = v(grad u, grad v)

[p0299-b0031 | equation | low] (2.6)

[p0299-b0032 | ordinary-paragraph | medium] N

[p0299-b0033 | equation | low] = 2v ∑ (D;(u), D;(v))

[p0299-b0034 | ordinary-paragraph | medium] if either u or ve V,

[p0299-b0035 | equation | low] i,=1

[p0299-b0036 | ordinary-paragraph | medium] and

[p0299-b0037 | equation | low] (2.7)

[p0299-b0038 | equation | low] a(w; u, v) = ao(u, v) + a(w; u, v).

[p0299-b0039 | ordinary-paragraph | medium] Then Problem (2.1) (2.2) has the equivalent form:

[p0299-b0040 | ordinary-paragraph | medium] Find a pair (u, p)e V x L?(Ω) such that:

[p0299-b0041 | ordinary-paragraph | low] Wve Hl(2)y.

[p0299-b0042 | equation | low] a(u;u, v) - (p, div v) = <f, v)

[p0299-b0043 | equation | low] (2.8)

[p0299-b0044 | theorem | medium] Theorem 2.1. Let N ≤ 4 and let Q be a bounded domain of R? with a Lipschitz-

[p0299-b0045 | ordinary-paragraph | medium] continuous boundary I. Given fe H-'(Q), there exists at least one pair (u, p)e

[p0299-b0046 | ordinary-paragraph | medium] V x L2(Q) which satisfies (2.8) or equivalently (2.1) (2.2).

## PDF 300 / printed 286



[p0300-b0003 | equation | low] X = H4(Q)" normed by|.|;,.0, M = L3(Q),

[p0300-b0004 | equation | low] b(v, q) = SAGE div v), a v> = aE v>.

[p0300-b0005 | ordinary-paragraph | high] Hence (2.8) is a particular case of Problem (Q). Thus, it remains to check the

[p0300-b0006 | ordinary-paragraph | high] hypotheses of Theorems 1.2 and 1.4. First, using (2.5), we get for all v, we V

[p0300-b0007 | equation | low] a(W; ¥, ¥) = do(¥, v) = v|VIt,0.-

[p0300-b0008 | ordinary-paragraph | high] Therefore, the form a(.;., .) satisfies the property (1.13) (and thus (1.9)).

[p0300-b0009 | ordinary-paragraph | high] Next, let u be a function of V and (u,,) be a sequence in V such that

[p0300-b0010 | equation | low] u,—2u_ weakly in V asm— oo.

[p0300-b0011 | ordinary-paragraph | high] Then, the compactness of the imbedding of Hj(Q) into L?(Q) (cf. Theorem I.1.3)

[p0300-b0012 | ordinary-paragraph | high] implies that:

[p0300-b0013 | equation | low] u,, 2 u_ strongly in L?(Q)" as m > oo.

[p0300-b0014 | ordinary-paragraph | high] Now, let v be in Y and let us take the limit of a(u,,; u,,,, v). According to (2.4),

[p0300-b0015 | ordinary-paragraph | high] we have

[p0300-b0016 | equation | low] A, (Un; Up v= =a (U, V, U,,)

[p0300-b0017 | equation | low] = — si mitlmj(Ov;/OX;)a x

[p0300-b0018 | equation | low] i,j=1

[p0300-b0019 | ordinary-paragraph | high] As 0v;/0x;€ L®(Q) and lim mim; = Uju; in L*(Q), it follows that

[p0300-b0020 | ordinary-paragraph | high] mo U

[p0300-b0021 | equation | low] lim a,(U,.3U,>V) = — : u,(Ov;/0x;)d x

[p0300-b0022 | equation | low] m>~ co i,j=1 Ba

[p0300-b0023 | equation | low] = —d,(u;V,u) = a,(u;4u, Vv).

[p0300-b0024 | ordinary-paragraph | high] Since it is clear that

[p0300-b0025 | equation | low] lim dao(u,,,V) = ao(u, v),

[p0300-b0026 | ordinary-paragraph | high] we get

[p0300-b0027 | equation | low] lim a(u,,;U,,,V) = a(u; U, Vv)

[p0300-b0028 | ordinary-paragraph | high] for all ve ¥ and therefore for all ve V by virtue of the density of YW in V (ef.

[p0300-b0029 | corollary | high] Corollary 1.2.5) and the continuity of the mapping v > a(u;u, y).

[p0300-b0030 | ordinary-paragraph | high] Finally, we have already seen that the bilinear form b(., .) satisfies the inf-sup

[p0300-b0031 | ordinary-paragraph | high] condition of Theorem 1.4 (see inequality (I.5.14)).

[p0300-b0032 | ordinary-paragraph | high] Thus, the hypotheses of Theorems 1.2 and 1.4 are fulfilled. Hence, there exists

[p0300-b0033 | ordinary-paragraph | high] at least one function ue V such that

[p0300-b0034 | ordinary-paragraph | high] (2.9) a(u;u,v) = <f,v> VveV.

## PDF 301 / printed 287



[p0301-b0003 | ordinary-paragraph | high] (u, p) is a solution of Problem (2.8). zt

[p0301-b0004 | ordinary-paragraph | high] Now, we turn to the uniqueness of the solution (u, p) of Problem (2.8). For

[p0301-b0005 | ordinary-paragraph | high] this, we introduce the norm of the trilinear form a,(.;.,.) in V?:

[p0301-b0006 | ordinary-paragraph | high] (2.10) oe eee

[p0301-b0007 | ordinary-paragraph | high] uvewev [Uy olV|1,0/Wli,0

[p0301-b0008 | ordinary-paragraph | high] We also set:

[p0301-b0009 | ordinary-paragraph | high] f,v

[p0301-b0010 | ordinary-paragraph | high] (2.11) llpaesup= es

[p0301-b0011 | ordinary-paragraph | high] veV |V|1.0

[p0301-b0012 | theorem | high] Theorem 2.2. Under the hypotheses of Theorem 2.1 and if in addition

[p0301-b0013 | ordinary-paragraph | high] (2.12) (V/v) ||f lly. < 1,

[p0301-b0014 | ordinary-paragraph | high] then Problem (2.8) has a unique solution (u, p) in V x L3(Q).

[p0301-b0015 | proof | high] Proof. Here, we make use of Theorem 1.3. We have already proved the property

[p0301-b0016 | ordinary-paragraph | high] (1.13) with « = v and it suffices to establish (1.14). Let u, v, w, and w, be in V; we

[p0301-b0017 | ordinary-paragraph | high] have:

[p0301-b0018 | equation | low] la(w,:u,v) — a(wa3u,¥)| = |a(w, — wo30,9)

[p0301-b0019 | equation | low] < MN uly alVii,olW1 — Woli.a-

[p0301-b0020 | ordinary-paragraph | high] Therefore, the form a(.; ., .) satisfies the hypothesis (1.14) with L(u) = for all

[p0301-b0021 | ordinary-paragraph | high] u. Then, the condition (2.12) coincides precisely with (1.15). Hence, the conclusion

[p0301-b0022 | ordinary-paragraph | high] of Theorem 1.3 is valid. el

[p0301-b0023 | ordinary-paragraph | high] Let us next consider the general case of a nonhomogeneous Dirichlet boundary

[p0301-b0024 | ordinary-paragraph | high] condition

[p0301-b0025 | ordinary-paragraph | high] (2.13) 12007.

[p0301-b0026 | ordinary-paragraph | high] Denote again by /;,0 <i < p, the connected components oft he boundary Jl ike

[p0301-b0027 | ordinary-paragraph | high] in Figure 2. We shall assume in all the sequel that

[p0301-b0028 | ordinary-paragraph | high] (2.14) | g-nds=0, O<i<p.

[p0301-b0029 | ordinary-paragraph | high] rT;

[p0301-b0030 | ordinary-paragraph | high] Now, we need the following important technical result due to Hopf [45].

[p0301-b0031 | lemma | high] Lemma 2.3. Suppose N < 3 and Q is like in Theorem 2.1. Then, given a function

[p0301-b0032 | ordinary-paragraph | high] geH'?(L)" satisfying the conditions (2.14), there exists for any e > Oa function

[p0301-b0033 | ordinary-paragraph | high] Uy = Uo(é)€ H'(Q)* such that

## PDF 302 / printed 288



[p0302-b0005 | equation | low] a(v;uo, v)l ≤ slvli.o

[p0302-b0006 | equation | low] (2.16)

[p0302-b0007 | ordinary-paragraph | low] AA

[p0302-b0008 | ordinary-paragraph | medium] Before proving Lemma 2.3, we check two preliminary lemmas. For any point

[p0302-b0009 | ordinary-paragraph | medium] x e Ω, we denote by d(x; I) the distance of x to the boundary F. Then, we have:

[p0302-b0010 | lemma | medium] Lemma 2.4. Let Q be like in Theorem 2.1. For all ε > 0, there exists a function

[p0302-b0011 | ordinary-paragraph | low] iny1 yons (o)8=0

[p0302-b0012 | equation | low] 0. = 1 in a neighborhood of I,

[p0302-b0013 | equation | low] ， 8(e) = exp(- 1/e),

[p0302-b0014 | equation | low] (2.17)

[p0302-b0015 | equation | low] 0(x) = 0 if d(x; F) ≥ 28(e),

[p0302-b0016 | equation | low] 'n>!>I 

[p0302-b0017 | equation | low] [00(x)/0x;l ≤ e/d(x; I) if d(x; F) ≤ 28(8),

[p0302-b0018 | proof | medium] Proof. Let us consider the function μ → Φ(μ) defined for μ ≥ O by

[p0302-b0019 | equation | low] if0≤μ≤o(e)²,

[p0302-b0020 | equation | low] if o(e)² ≤μ ≤ 8(8),

[p0302-b0021 | equation | low] Φ(μ) = 3 ε Log(8(e)/μ)

[p0302-b0022 | equation | low] if μ ≥ 8(8).

[p0302-b0023 | ordinary-paragraph | medium] 0

[p0302-b0024 | ordinary-paragraph | medium] Clearly, Φe W1,∞(R+ ). We set:

[p0302-b0025 | ordinary-paragraph | medium] xeΩ.

[p0302-b0026 | equation | low] x(x) = Φ(d(x; I),

[p0302-b0027 | ordinary-paragraph | medium] Since I is Lipschitz-continuous, the function d belongs to W1. ∞(Q) and we have

[p0302-b0028 | equation | low] [ad(x; F)/ax,;I ≤ 1.

[p0302-b0029 | ordinary-paragraph | medium] Hence the function x. belongs to W1, ∞(Q) and satisfies

[p0302-b0030 | equation | low] [0x(x)/0x;I ≤ e/d(x; I)  if d(x; I) ≤ 8(e).

[p0302-b0031 | ordinary-paragraph | medium] By regularizing X, we obtain a function 0. e 62(@) with the properties (2.17).

[p0302-b0032 | lemma | medium] Lemma 2.5. Let Q be like in Theorem 2.1. There exists a constant C = C(Ω) > 0

[p0302-b0033 | ordinary-paragraph | medium] such that

[p0302-b0034 | equation | low] (2.18)

[p0302-b0035 | ordinary-paragraph | low] ()H中A

[p0302-b0036 | equation | low] IlΦ/d(.; F)llo,o ≤ ClΦl1,s

[p0302-b0037 | proof | medium] Proof. By introducing a partition of unity subordinate to a covering of I and

[p0302-b0038 | ordinary-paragraph | medium] systems of local coordinates near I, we need only to investigate the case where

[p0302-b0039 | ordinary-paragraph | medium] Q is the half-space

[p0302-b0040 | equation | low] R = {x =(x',xn) xn> 0}

[p0302-b0041 | ordinary-paragraph | medium] and d(x; F) = x. Hence, for proving (2.18), it is sufficient to check that

[p0302-b0042 | ordinary-paragraph | low] 10b(x)/axv12 dx  VΦ∈ @(R).

[p0302-b0043 | equation | low] [p(x)/xn]² dx ≤ C

[p0302-b0044 | ordinary-paragraph | low] JR

[p0302-b0045 | ordinary-paragraph | medium] JR

## PDF 303 / printed 289



[p0303-b0004 | ordinary-paragraph | medium] 8

[p0303-b0005 | ordinary-paragraph | medium] 8

[p0303-b0006 | equation | low] 1Φ(t)/t/|2 dt ≤ 4

[p0303-b0007 | equation | low] (2.19)

[p0303-b0008 | equation | low] (0 0)6 =ΦA

[p0303-b0009 | ordinary-paragraph | low] P z1(0),p1

[p0303-b0010 | ordinary-paragraph | low] Vo

[p0303-b0011 | ordinary-paragraph | medium] 0

[p0303-b0012 | ordinary-paragraph | medium] which can be established as follows. By writing

[p0303-b0013 | ordinary-paragraph | medium] p'(s)ds

[p0303-b0014 | equation | low] Φ(t) =

[p0303-b0015 | ordinary-paragraph | medium] and setting t = e', s = e°, we have

[p0303-b0016 | ordinary-paragraph | low] 12

[p0303-b0017 | ordinary-paragraph | medium] 8

[p0303-b0018 | ordinary-paragraph | medium] 8

[p0303-b0019 | equation | low] 1Φ(t)/t)2 dt =

[p0303-b0020 | ordinary-paragraph | medium] p'(s)ds

[p0303-b0021 | ordinary-paragraph | medium] (1/t)

[p0303-b0022 | ordinary-paragraph | medium] (dt/t)

[p0303-b0023 | ordinary-paragraph | low] 0

[p0303-b0024 | ordinary-paragraph | medium] 0

[p0303-b0025 | ordinary-paragraph | medium] 2

[p0303-b0026 | ordinary-paragraph | low] dt

[p0303-b0027 | ordinary-paragraph | medium] Φ'(e)e do

[p0303-b0028 | ordinary-paragraph | low] 2

[p0303-b0029 | ordinary-paragraph | low] DP z/(),Pz/(o-2)-0(0 - 2)H

[p0303-b0030 | ordinary-paragraph | medium] dt,

[p0303-b0031 | ordinary-paragraph | medium] where H is the classical Heaviside function. Now, using the standard convolution

[p0303-b0032 | ordinary-paragraph | medium] inequality:

[p0303-b0033 | equation | low] Ilf *g ll 2 ≤ Ilf ll  lgll 2,

[p0303-b0034 | ordinary-paragraph | medium] we get

[p0303-b0035 | ordinary-paragraph | medium] +8

[p0303-b0036 | ordinary-paragraph | medium] 8

[p0303-b0037 | ordinary-paragraph | medium] H(t)e-t/2 dt

[p0303-b0038 | ordinary-paragraph | medium] $'(e)²e do

[p0303-b0039 | equation | low] 1Φ(t)/t|2 dt ≤

[p0303-b0040 | ordinary-paragraph | medium] 8

[p0303-b0041 | ordinary-paragraph | medium] 0

[p0303-b0042 | ordinary-paragraph | medium] 8

[p0303-b0043 | ordinary-paragraph | medium] $'(s)² ds

[p0303-b0044 | ordinary-paragraph | medium] which is the desired inequality.

[p0303-b0045 | proof | medium] Proof of Lemma 2.3. Let the function ge H1/2(F) satisfy the conditions (2.14).

[p0303-b0046 | ordinary-paragraph | medium] We already know from Lemma 1.2.2 that there exists a function wo e H'(Q) such

[p0303-b0047 | ordinary-paragraph | medium] that

[p0303-b0048 | equation | low] div w。 = 0,

[p0303-b0049 | equation | low] Wolr = g.

[p0303-b0050 | ordinary-paragraph | medium] Moreover, it follows from (2.14), Theorem I.3.1 or I.3.4 and Corollary 1.3.3, that

[p0303-b0051 | ordinary-paragraph | medium] we can find a stream function yoe H?(Q) if the dimension N = 2 or a vector

[p0303-b0052 | ordinary-paragraph | medium] potential wo e H²(Q)3 if the dimension N = 3, such that

[p0303-b0053 | equation | low] curl yo,

[p0303-b0054 | equation | low] N = 2,

[p0303-b0055 | ordinary-paragraph | medium] wo

[p0303-b0056 | equation | low] curl yo,

[p0303-b0057 | equation | low] N = 3.

[p0303-b0058 | ordinary-paragraph | medium] Consider the case N = 3, the case N = 2 being exactly similar. For all μ > 0,

[p0303-b0059 | ordinary-paragraph | medium] we introduce the function

## PDF 304 / printed 290



[p0304-b0004 | ordinary-paragraph | medium] where 0, is defined as in Lemma 2.4. Clearly uo, e H'(Q)3 and

[p0304-b0005 | equation | low] div uoμ = 0,

[p0304-b0006 | equation | low] Uou!r = g.

[p0304-b0007 | ordinary-paragraph | medium] Now, using Lemma 2.4, we have if d(x; F) ≤ 28(μ)

[p0304-b0008 | ordinary-paragraph | low] oloi (

[p0304-b0009 | ordinary-paragraph | low] 0(0μloi)

[p0304-b0010 | ordinary-paragraph | low] μ

[p0304-b0011 | ordinary-paragraph | medium] (x)

[p0304-b0012 | ordinary-paragraph | low] |Woi(x)l +

[p0304-b0013 | ordinary-paragraph | medium] (x)

[p0304-b0014 | ordinary-paragraph | low] 0xj

[p0304-b0015 | ordinary-paragraph | low] 0xj

[p0304-b0016 | ordinary-paragraph | medium] d(x; F)

[p0304-b0017 | ordinary-paragraph | medium] so that

[p0304-b0018 | equation | low] uoμ(x) Il ≤ C [(μ/d(x; F)) Ilwo(x)l + I| Dwo(x)Il]

[p0304-b0019 | ordinary-paragraph | medium] where Il. Il denotes as usual the Euclidean norm of R? and

[p0304-b0020 | ordinary-paragraph | medium] 1/2

[p0304-b0021 | ordinary-paragraph | medium] N

[p0304-b0022 | equation | low] ∑l0lo(x)/ax,)2

[p0304-b0023 | equation | low] |Dwo(x)ll =

[p0304-b0024 | ordinary-paragraph | medium] Let v belong to V. Since H?(Ω) c C°(Ω), we obtain

[p0304-b0025 | ordinary-paragraph | low] [v;lI Dwo(x)|l]² dx

[p0304-b0026 | ordinary-paragraph | low] Ilv;uoujllo.o ≤ C2 μllv;/d( .; F)llo.2 +

[p0304-b0027 | equation | low] Jd(x; F)≤28(μ)

[p0304-b0028 | ordinary-paragraph | medium] Applying Lemma 2.5 gives

[p0304-b0029 | equation | low] Ilv;/d(.; F) llo.o ≤ Cslvil1.2.

[p0304-b0030 | ordinary-paragraph | medium] Moreover, since H'(Q)  L6(Q), we have by Holder's inequality

[p0304-b0031 | ordinary-paragraph | medium] 1/2

[p0304-b0032 | ordinary-paragraph | medium] 1/3

[p0304-b0033 | ordinary-paragraph | low] |I Dyo(x)!l 3 dx

[p0304-b0034 | ordinary-paragraph | low] [v;ll Dwoll]² dx

[p0304-b0035 | equation | low] ≤ C4lvil1,o x

[p0304-b0036 | ordinary-paragraph | medium] Jd(x;F)≤28(μ)

[p0304-b0037 | equation | low] Jd(x;F)≤20(μ)

[p0304-b0038 | ordinary-paragraph | medium] Setting

[p0304-b0039 | ordinary-paragraph | medium] 1/3

[p0304-b0040 | ordinary-paragraph | low] Φ(μ) :

[p0304-b0041 | ordinary-paragraph | low] |IDwo(x)ll13 dx

[p0304-b0042 | equation | low] Jd(x;F)≤28(μ)

[p0304-b0043 | ordinary-paragraph | medium] we get

[p0304-b0044 | equation | low] llV;uouillo,o ≤ Cs(μ + Φ(μ)|vil1.2

[p0304-b0045 | ordinary-paragraph | medium] Therefore, using Lemma 2.2, we have

[p0304-b0046 | ordinary-paragraph | medium] N

[p0304-b0047 | equation | low] [a(v; uou, v)l = |a,(v; v, uou)|

[p0304-b0048 | ordinary-paragraph | medium] v;uou;0v;/0x;dx

[p0304-b0049 | equation | low] i,j=1JQ

[p0304-b0050 | equation | low] ≤ C6(μ + Φ(μ)Ivii.o.

[p0304-b0051 | ordinary-paragraph | medium] Thus, given ε > 0 and since limμ +o Φ(μ) = 0, we may choose μ = μ(e) small

[p0304-b0052 | ordinary-paragraph | medium] enough so that

[p0304-b0053 | equation | low] Ce(μ + Φ(μ) ≤8.

## PDF 305 / printed 291



[p0305-b0004 | ordinary-paragraph | medium] (2.16).

[p0305-b0005 | ordinary-paragraph | medium] 口

[p0305-b0006 | ordinary-paragraph | medium] Now, a variational form of Problem (2.1), (2.13) consists in finding a pair

[p0305-b0007 | ordinary-paragraph | medium] (u, p)e H'(Q) x L2(Ω) solution of the equations

[p0305-b0008 | equation | low] a(u;u, v) - (p, divv) = <f,v) Vv∈ H(Ω),

[p0305-b0009 | equation | low] (2.20)

[p0305-b0010 | equation | low] divu = 0 in Ω,

[p0305-b0011 | equation | low] u=g on I.

[p0305-b0012 | theorem | medium] Theorem 2.3. Let N ≤ 3 and let Q be a bounded domain of R? with a Lipschitz-

[p0305-b0013 | ordinary-paragraph | medium] continuous boundary F. Given fe H-′(Q) and ge H'/2(F) satisfying the condi-

[p0305-b0014 | ordinary-paragraph | medium] tions (2.14), there exists at least one pair (u, p)e H'(Q) × L2(Q) solution of (2.20)

[p0305-b0015 | ordinary-paragraph | medium] or equivalently solution of Problem (2.1) (2.13).

[p0305-b0016 | proof | medium] Proof. Let u. be a function of H'(Q) such that

[p0305-b0017 | equation | low] divuo = O, uolr = g.

[p0305-b0018 | ordinary-paragraph | medium] We set u = uo + w. Since

[p0305-b0019 | ordinary-paragraph | medium] a(uo + w; uo + w, v) = a(w; w, v) + a,(uo; w, v) + a(w; uo, v) + a(uo;uo, v),

[p0305-b0020 | ordinary-paragraph | medium] Problem (2.20) may be equivalently stated as follows:

[p0305-b0021 | ordinary-paragraph | medium] Find a pair (w, p)e V x L?(Ω) such that

[p0305-b0022 | ordinary-paragraph | low] N(O)HAA

[p0305-b0023 | equation | low] a(w; w,v) - (p, div v) = <f,v) -- a(uo; uo, v)

[p0305-b0024 | equation | low] (2.21)

[p0305-b0025 | ordinary-paragraph | medium] where

[p0305-b0026 | equation | low] a(w; u, v) = a(w; u, v) + a (uo; u, v) + a,(u; uo, v).

[p0305-b0027 | ordinary-paragraph | medium] Observe that Problem (2.21) fits into the framework of Paragraph 1 if we take

[p0305-b0028 | equation | low] X = H(Ω),  M = L(Ω),

[p0305-b0029 | equation | low] a(.; ., .) replaced by a(.; ., .), b(v,q) = --(q, divv),

[p0305-b0030 | equation | low] <l,v> = <f,v> - a(uo;uo, V).

[p0305-b0031 | ordinary-paragraph | medium] Again, we have to check the hypotheses of Theorems 1.2 and 1.4. First, using

[p0305-b0032 | ordinary-paragraph | medium] (2.5), we have for all v, w e V

[p0305-b0033 | equation | low] a(w; v, v) = v/vl²,2 + a, (v; uo, V).

[p0305-b0034 | ordinary-paragraph | medium] It follows from Lemma 2.3 that we may choose the function uo so that

[p0305-b0035 | equation | low] [a(v;uo, v)l ≤ 8lvli,2

[p0305-b0036 | equation | low] >3 AA 

[p0305-b0037 | ordinary-paragraph | medium] and therefore

[p0305-b0038 | ordinary-paragraph | low] 3MAA

[p0305-b0039 | equation | low] a(w;v,v) ≥(v - 8)/vli.o

## PDF 306 / printed 292



[p0306-b0004 | ordinary-paragraph | high] the inf-sup condition (1.18) holds, we obtain that Problem (2.21) has at least one

[p0306-b0005 | ordinary-paragraph | high] solution (w, p)¢ V x L2(Q), which proves the theorem. ie)

[p0306-b0006 | ordinary-paragraph | high] Next, we derive a uniqueness result. For any function uy € H'(Q)", we set

[p0306-b0007 | ordinary-paragraph | high] (2.22) pli) std,(Vp;Up,V

[p0306-b0008 | ordinary-paragraph | high] vey |YI7,0

[p0306-b0009 | equation | low] <1,v >

[p0306-b0010 | ordinary-paragraph | high] (2.23) || (6 uo) lly = sup lee <I,v> = <f,v > — a(UUo;, Y ).

[p0306-b0011 | ordinary-paragraph | high] veV 1

[p0306-b0012 | ordinary-paragraph | high] Then, we define vo = vo(Q; f, g) by

[p0306-b0013 | ordinary-paragraph | high] (2.24) vo = inf{p(uo) + (W|I (fu) |lp-)”7; Up € H' (Q)” satisfies (2.15)}.

[p0306-b0014 | ordinary-paragraph | high] Given any number v > 0, it follows from Lemma 2.3 and the continuity of the

[p0306-b0015 | ordinary-paragraph | high] mapping g > Uo (cf. (1.2.12)) that we have vy < v for |/f\|,, and ||g|| 12,7 small

[p0306-b0016 | ordinary-paragraph | high] enough.

[p0306-b0017 | theorem | high] Theorem 2.4. Assume the hypotheses of Theorem 2.3. Then, for v > vo(Q;f, g),

[p0306-b0018 | ordinary-paragraph | high] Problem (2.20) has a unique solution (u, p)€ H'(Q)* x L2(Q).

[p0306-b0019 | proof | high] Proof. Let us choose a function uy € H'(Q)* which satisfies (2.15) and p(ug) < v.

[p0306-b0020 | ordinary-paragraph | high] We want to apply Theorem 1.3 to Problem (2.21). We have for all v, we V

[p0306-b0021 | equation | low] a(w; v,v ) > (v — p(u))|VI7,0,

[p0306-b0022 | ordinary-paragraph | high] so that the property (1.13) holds with « = v — p(u,). Hence, it remains only to

[p0306-b0023 | ordinary-paragraph | high] check (1.14). Let u, v, w,, w, be in V; using (2.10), we get

[p0306-b0024 | equation | low] |a(w,;u,V v)— a(w,;u,v)| = |a,(w, — w>;u,v) |

[p0306-b0025 | equation | low] < Nu], alVi1.elWi — Walia:

[p0306-b0026 | ordinary-paragraph | high] Hence, the form a(.;., .) satisfies the property (1.14) with L(u) = “”. Now, the

[p0306-b0027 | ordinary-paragraph | high] condition (1.15) becomes in our case

[p0306-b0028 | ordinary-paragraph | high] AN ||I (f; uo) lly

[p0306-b0029 | ordinary-paragraph | high] (v — p(Uo))?

[p0306-b0030 | ordinary-paragraph | high] or equivalently

[p0306-b0031 | equation | low] V > p(Uo) + (WI 1(6 uo) lp)".

[p0306-b0032 | ordinary-paragraph | high] By taking the infimum over all the admissible functions uy, we obtain that, for

[p0306-b0033 | ordinary-paragraph | high] v > Vo, Problem (2.21) has a unique solution (w, p)€ H3(Q)" x L2(Q) and there-

[p0306-b0034 | ordinary-paragraph | high] fore Problem (2.20) has a unique solution (ug + w, p)¢ H1(Q)% x L2(Q). oO

## PDF 307 / printed 293



[p0307-b0003 | equation | low] divup =0, Ulr=2, Vv > p(uo).

[p0307-b0004 | ordinary-paragraph | high] Then, we have for all solution (u = uy + w, p) of Problem (2.20)

[p0307-b0005 | ordinary-paragraph | high] ||1 06 uo) lly

[p0307-b0006 | equation | low] IWl,a< ,

[p0307-b0007 | ordinary-paragraph | high] : v — p(Uo)

[p0307-b0008 | remark | high] Remark 2.2. Assuming the hypotheses of Theorem 2.4, we may apply the results

[p0307-b0009 | ordinary-paragraph | high] of Remark 1.3 to Problem (2.21). Starting from an arbitrary w° € V, the iterative

[p0307-b0010 | ordinary-paragraph | high] scheme

[p0307-b0011 | equation | low] G(w™; w"*!, vy)— (p™*1, divv) = <f,v> — a(ug;Up,v) VvHeo (Q )%

[p0307-b0012 | ordinary-paragraph | high] uniquely defines a sequence (w”, p”) in V x L$(Q) which converges towards the

[p0307-b0013 | ordinary-paragraph | high] solution (w, p) of Problem (2.21).

[p0307-b0014 | ordinary-paragraph | high] Equivalently, starting from an arbitrary function u° ¢ H*(Q)" such that divu° =

[p0307-b0015 | ordinary-paragraph | high] 0 and u°|; = g, the iterative scheme

[p0307-b0016 | ordinary-paragraph | high] N

[p0307-b0017 | equation | low] —vAu™*! + x u™(du™*!/dx;) + gradp”™** =f in Q,

[p0307-b0018 | ordinary-paragraph | high] a

[p0307-b0019 | ordinary-paragraph | high] (2.25) Pea ay

[p0307-b0020 | ordinary-paragraph | high] u”*! Siri s

[p0307-b0021 | ordinary-paragraph | high] uniquely defines a sequence (u™, p”) in H'(Q)" x L6(Q) such that

[p0307-b0022 | equation | low] lim {||u" — ull; + llp” — Pllo,a} = 9.

[p0307-b0023 | ordinary-paragraph | high] m~ oo

[p0307-b0024 | subsection | high] 2.2. The Stream Function Formulation of the Homogeneous Problem

[p0307-b0025 | ordinary-paragraph | high] For the sake of simplicity, we restrict the discussion exclusively to the homoge-

[p0307-b0026 | ordinary-paragraph | high] neous boundary condition:

[p0307-b0027 | ordinary-paragraph | high] (2.2) a= 07 on.

[p0307-b0028 | ordinary-paragraph | high] Let us first consider the two-dimensional case: N = 2. Since ue Hg(Q)? is

[p0307-b0029 | ordinary-paragraph | high] divergence-free, we know from Section 1.3.1 that

[p0307-b0030 | equation | low] u = curly

[p0307-b0031 | ordinary-paragraph | high] for a unique stream function w in the space

[p0307-b0032 | equation | low] = 0}.

[p0307-b0033 | equation | low] constant for 1 <i < p, 0x/dn|

[p0307-b0034 | ordinary-paragraph | high] W = {ye H?(Q); x1, = 0, xIr, is

[p0307-b0035 | ordinary-paragraph | high] To express the nonlinear term a,(u;u, v) in terms of stream functions, observe

[p0307-b0036 | ordinary-paragraph | high] that

## PDF 308 / printed 294



[p0308-b0003 | ordinary-paragraph | high] (2.26) Q

[p0308-b0004 | ordinary-paragraph | high] Vu = (uy, U2) € Hg (Q)’, VS (v,,02)€ V.

[p0308-b0005 | ordinary-paragraph | high] This result stems from the identities:

[p0308-b0006 | equation | low] Ps +u eas == (1/2e) e + u3) — u,curlu,

[p0308-b0007 | ordinary-paragraph | high] Ox, 2 One

[p0308-b0008 | ordinary-paragraph | high] 227)

[p0308-b0009 | ordinary-paragraph | high] Ou, Ou,

[p0308-b0010 | equation | low] u,—— + 4u = (1/2)a s + u3) + u,curlu,

[p0308-b0011 | ordinary-paragraph | high] Ox, 2 ax,

[p0308-b0012 | ordinary-paragraph | high] followed by an integration by parts to eliminate grad(|\u||*). Therefore the

[p0308-b0013 | ordinary-paragraph | high] nonlinear term reads:

[p0308-b0014 | equation | low] auny)= |a u ( a — ae ax

[p0308-b0015 | ordinary-paragraph | high] (2.28) Q Oxs OXGe VOXTOx,

[p0308-b0016 | ordinary-paragraph | high] YVu=curly, v=curl¢d withy,¢d in¥.

[p0308-b0017 | ordinary-paragraph | high] In addition, we have proved in Theorem I.5.5 that

[p0308-b0018 | equation | low] (grad u, grad v) = (Aw, 4¢) with the notations of (2.28).

[p0308-b0019 | ordinary-paragraph | high] Thus, the Navier-Stokes Problem (2.1) (2.2) has the equivalent formulation:

[p0308-b0020 | ordinary-paragraph | high] Find a function in ¥ such that

[p0308-b0021 | ordinary-paragraph | high] op op ow aM

[p0308-b0022 | ordinary-paragraph | high] (2.29) v(4Awd,) + |a u Jax = <feurld) Woe

[p0308-b0023 | ordinary-paragraph | high] OX, OX p OX, OX,

[p0308-b0024 | ordinary-paragraph | high] Q

[p0308-b0025 | ordinary-paragraph | high] Owing to this equivalence, all the existence and uniqueness results of the

[p0308-b0026 | ordinary-paragraph | high] preceding section carry over to Problem (2.29).

[p0308-b0027 | ordinary-paragraph | high] It remains to interpret Problem (2.29). We easily derive that w satisfies the

[p0308-b0028 | ordinary-paragraph | high] following nonlinear biharmonic equations:

[p0308-b0029 | ordinary-paragraph | high] vA ae( at )+2 -(445o t) — cunt in Q,

[p0308-b0030 | ordinary-paragraph | high] X 4

[p0308-b0031 | equation | low] wip= 0, wip =aconstantc, 1 <li<p,

[p0308-b0032 | equation | low] oy/on|r = 0

[p0308-b0033 | equation | low] | (vo(4p)/On —f-t)ds=0, 1<i<p.

[p0308-b0034 | ordinary-paragraph | high] r,

[p0308-b0035 | ordinary-paragraph | high] Now, we turn to the three-dimensional case: N = 3. Here, we consider only

[p0308-b0036 | ordinary-paragraph | high] simply-connected domains 92. In order to express Problem (2.1) (2.2) in terms of

[p0308-b0037 | ordinary-paragraph | high] vector potentials, we use extensively the material of Section I.5.3. Let us take the

[p0308-b0038 | ordinary-paragraph | high] space of vector potentials:

## PDF 309 / printed 295



[p0309-b0005 | equation | low] d≥!≥00= spu.Φ

[p0309-b0006 | ordinary-paragraph | low] JF

[p0309-b0007 | ordinary-paragraph | high] with the norm

[p0309-b0008 | equation | low] IΦll = {lΦll6,o + I|divΦll,o + Ilcurl Φlli.2}1/2.

[p0309-b0009 | ordinary-paragraph | high] Recall that this norm is equivalent to I 4Φllo.o (cf. Lemma I.5.2) and for the sake

[p0309-b0010 | ordinary-paragraph | medium] of brevity we denote: IΦl = I/ 4Φ llo.s.

[p0309-b0011 | ordinary-paragraph | high] Since div u = 0 and Ω is simply-connected, u has a unique vector potential

[p0309-b0012 | ordinary-paragraph | high] y in Y that satisfies

[p0309-b0013 | equation | low] u = curl y,

[p0309-b0014 | equation | low] div w = 0.

[p0309-b0015 | ordinary-paragraph | high] Then, taking into account the identity:

[p0309-b0016 | equation | low] (2.30)

[p0309-b0017 | equation | low] u;(@u;/0x;)v; = (curlu x u) · v + (1/2)grad(llull²)· v,

[p0309-b0018 | ordinary-paragraph | low]   s     s  r      

[p0309-b0019 | ordinary-paragraph | high] nonlinear biharmonic problem:

[p0309-b0020 | ordinary-paragraph | high] Find y in Y such that

[p0309-b0021 | equation | low] (4y × curl y)· curl Φ dx = <f, curl Φ>

[p0309-b0022 | ordinary-paragraph | medium] Voe Y.

[p0309-b0023 | ordinary-paragraph | high] (2.31)v(4w, 4Φ) -

[p0309-b0024 | ordinary-paragraph | low] JΩ

[p0309-b0025 | ordinary-paragraph | high] Therefore, it follows from Theorem 2.1 that, for each f in H-1(Ω), Problem (2.31)

[p0309-b0026 | ordinary-paragraph | high] has at least one divergence-free solution w in Y.

[p0309-b0027 | ordinary-paragraph | high] But conversely, we cannot establish in general that every solution w of (2.31)

[p0309-b0028 | ordinary-paragraph | high] is a vector potential of a solution u of the Navier-Stokes Problem (2.1) (2.3).

[p0309-b0029 | ordinary-paragraph | high] Indeed, setting

[p0309-b0030 | equation | low] w = curl y,

[p0309-b0031 | ordinary-paragraph | high] we infer from (2.31) that w satisfies: w e V,

[p0309-b0032 | equation | low] grad(div y) x w·v dx

[p0309-b0033 | ordinary-paragraph | high] v(grad w, grad v) +

[p0309-b0034 | equation | low] + <AJ> = xpA.M x MJn

[p0309-b0035 | ordinary-paragraph | low] JQ

[p0309-b0036 | ordinary-paragraph | low] AA

[p0309-b0037 | ordinary-paragraph | high] Unless fo grad(div w) x w· v dx = 0(and this property does not stem from (2.31),

[p0309-b0038 | ordinary-paragraph | high] we see that w does not satisfy the Navier-Stokes equations.

[p0309-b0039 | ordinary-paragraph | high] The trilinear form naturally attached to Problem (2.31) is

[p0309-b0040 | equation | low] (2.32)

[p0309-b0041 | equation | low] (4Φ x curl y)· curl x dx.

[p0309-b0042 | equation | low] a1(Φ; Y,x) =

[p0309-b0043 | ordinary-paragraph | high] Clearly, this form satisfies (2.4) and (2.5). In addition, like in Lemma 2.1, a,(. ; -, . )

## PDF 310 / printed 296



[p0310-b0004 | equation | low] 1a, (O5 Y,X%)| < 49 ]lo,qlleurl wllo,4,ql/eurl X |lo,4 ,0:

[p0310-b0005 | equation | low] < C;||4]/o,yq| |l, qllleeurul rx| l|1, 0.

[p0310-b0006 | ordinary-paragraph | high] Hence

[p0310-b0007 | ordinary-paragraph | high] (2.33) lady.xyl<Clollivilzil Vow, xe?

[p0310-b0008 | ordinary-paragraph | high] As far as the uniqueness of the solution is concerned, the equivalence of

[p0310-b0009 | ordinary-paragraph | high] norms:

[p0310-b0010 | equation | low] ld = l4bloo=l6| Voe?

[p0310-b0011 | ordinary-paragraph | high] guarantees the ellipticity of the form

[p0310-b0012 | equation | low] ap; y, x) = v(Ay, 4x) + a1 (6; y, x).

[p0310-b0013 | ordinary-paragraph | high] On the other hand, setting

[p0310-b0014 | ordinary-paragraph | high] ~ a,(o; y, x)

[p0310-b0015 | ordinary-paragraph | high] gDe34s4 A= bvBri ey —[ Ollyllx

[p0310-b0016 | ordinary-paragraph | high] we get

[p0310-b0017 | equation | low] 1a,(01;Y W,% ) — 41 (b2;Y W,x )| = 1a1(0, — O25, x)

[p0310-b0018 | equation | low] < Vo, — oailvilxl.

[p0310-b0019 | ordinary-paragraph | high] Therefore the trilinear form a,(.; ., .) satisfies (1.14) with L(y) = 1, independent

[p0310-b0020 | ordinary-paragraph | high] of u (the space Y being equipped with the norm |.|). Thus when vy is large enough

[p0310-b0021 | ordinary-paragraph | high] or ||f\|,. is sufficiently small the solution wy of Problem (2.31) is unique. As the

[p0310-b0022 | ordinary-paragraph | high] vector potential of every solution u of Problem (2.1) (2.2) is a solution of (2.31),

[p0310-b0023 | ordinary-paragraph | high] this means that Problem (2.1) (2.2) has also a unique solution u and

[p0310-b0024 | equation | low] u = curly

[p0310-b0025 | ordinary-paragraph | high] with y solution of (2.31). As a consequence y satisfies necessarily

[p0310-b0026 | equation | low] divy = 0.

[p0310-b0027 | ordinary-paragraph | high] These results are summed up in the following theorem.

[p0310-b0028 | theorem | high] Theorem 2.5. Let Q be a bounded, simply-connected domain of R? with a Lipschitz-

[p0310-b0029 | ordinary-paragraph | high] continuous boundary I’. Then Problem (2.31) has at least one solution w in ¥. In

[p0310-b0030 | ordinary-paragraph | high] addition, if

[p0310-b0031 | ordinary-paragraph | high] (2.35) W(1/v?) sup eae <4

[p0310-b0032 | ordinary-paragraph | high] be |p|

[p0310-b0033 | ordinary-paragraph | high] then the solution w is unique, there exists p in L3(Q) such that (u = curly, p) is

[p0310-b0034 | ordinary-paragraph | high] the unique solution of Problem (2.1) (2.2) and

[p0310-b0035 | equation | low] divy=0 inQ.
