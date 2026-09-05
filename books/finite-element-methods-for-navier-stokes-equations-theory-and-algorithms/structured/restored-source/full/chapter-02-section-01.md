# Restored-source review candidate: chapter-02-section-01



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 126 / printed 112



[p0126-b0002 | ordinary-paragraph | high] Problem in the Primitive Variables

[p0126-b0003 | section | high] § 1. General Approximation

[p0126-b0004 | ordinary-paragraph | high] The abstract problem discussed in Chapter I, § 4 lends itself readily to a straight-

[p0126-b0005 | ordinary-paragraph | high] forward approximation that converges under reasonable assumptions with an

[p0126-b0006 | ordinary-paragraph | high] error proportional to the approximation error of the spaces involved. When

[p0126-b0007 | ordinary-paragraph | high] applied to the Stokes problem, this approach yields a conforming approximation

[p0126-b0008 | ordinary-paragraph | high] of the velocity and pressure, although the approximate velocity field is (in general)

[p0126-b0009 | ordinary-paragraph | high] not exactly divergence-free. The wide range of finite element methods developped

[p0126-b0010 | ordinary-paragraph | high] in the remainder of the chapter are all founded on the material of this paragraph.

[p0126-b0011 | ordinary-paragraph | high] Non-conforming methods can also be put into this framework (cf. Zine [85]) but

[p0126-b0012 | ordinary-paragraph | high] for the sake of conciseness we have skipped them entirely.

[p0126-b0013 | subsection | high] 1.1. An Abstract Approximation Result

[p0126-b0014 | ordinary-paragraph | high] This section is devoted to the approximation of the abstract variational problem

[p0126-b0015 | ordinary-paragraph | high] analyzed in §4 of Chapter I. We keep here the same notation and we put the

[p0126-b0016 | ordinary-paragraph | high] problem in exactly the same situation. Recall that our Problem (Q) reads:

[p0126-b0017 | ordinary-paragraph | high] Given | in X’ and x in M’, find a pair (u, A) in X x M such that

[p0126-b0018 | ordinary-paragraph | high] (1.1) a(u,v) + b(v,A)=<lLv> Vuoex,

[p0126-b0019 | ordinary-paragraph | high] (1.2) buuw=<xyu> VueMm.

[p0126-b0020 | ordinary-paragraph | high] Here, X and M are two real Hilbert spaces and a(.,.) and b(.,.) are two

[p0126-b0021 | ordinary-paragraph | high] continuous bilinear forms defined respectively on X x X and X x M. With the

[p0126-b0022 | ordinary-paragraph | high] form b(., .) we associate the linear operators B and B’ defined by:

[p0126-b0023 | equation | low] (Bu,u > = <v, B’u> = b(v,n) VueX , VueM

[p0126-b0024 | ordinary-paragraph | high] and we set

[p0126-b0025 | equation | low] V(x) = {veX ; Bu = x},

[p0126-b0026 | equation | low] V = V(0) = Ker(B).

## PDF 127 / printed 113



[p0127-b0004 | ordinary-paragraph | medium] Given I in X' and x in M', find u in V(x) such that:

[p0127-b0005 | ordinary-paragraph | low] 'AaA

[p0127-b0006 | equation | low] (1.3)

[p0127-b0007 | equation | low] a(u,u) =<l,v)

[p0127-b0008 | ordinary-paragraph | medium] We retain the two hypotheses which guarantee that Problems (Q) and (P) are

[p0127-b0009 | ordinary-paragraph | medium] equivalent and have a unique solution (cf. Theorem I.4.1 and its Corollary):

[p0127-b0010 | ordinary-paragraph | medium] there exists a constant α > O such that

[p0127-b0011 | ordinary-paragraph | low] :AaA

[p0127-b0012 | equation | low] a(v,u) ≥αlv11x

[p0127-b0013 | equation | low] (1.4)

[p0127-b0014 | ordinary-paragraph | medium] there exists a constant β > 0 such that

[p0127-b0015 | ordinary-paragraph | medium] b(v, μ)

[p0127-b0016 | equation | low] -≥β.

[p0127-b0017 | equation | low] inf sup

[p0127-b0018 | equation | low] (1.5)

[p0127-b0019 | ordinary-paragraph | low] peM vex Iullxlμll m

[p0127-b0020 | ordinary-paragraph | medium] Let h denote a discretization parameter tending to zero and, for each h, let

[p0127-b0021 | ordinary-paragraph | medium] X, and M, be two finite-dimensional spaces such that:

[p0127-b0022 | ordinary-paragraph | medium] M, c M.

[p0127-b0023 | ordinary-paragraph | medium] Xh c X,

[p0127-b0024 | ordinary-paragraph | medium] Let X', and M' denote their dual spaces with the dual norms:

[p0127-b0025 | equation | low] <Xhs μh>

[p0127-b0026 | equation | low] <lnUn>

[p0127-b0027 | equation | low] llxal m = sup

[p0127-b0028 | equation | low] I/llx = sup

[p0127-b0029 | ordinary-paragraph | low] μheMnIμn M

[p0127-b0030 | ordinary-paragraph | low] vnexnlunllx

[p0127-b0031 | ordinary-paragraph | medium] Clearly,

[p0127-b0032 | ordinary-paragraph | medium] Wxe m'.

[p0127-b0033 | equation | low] II/lxn ≤ I /lx,  Ilxll m ≤Ilxll m'

[p0127-b0034 | equation | low] ‘X≥1A

[p0127-b0035 | ordinary-paragraph | medium] Like in the continuous case, we associate with a(., . ) and b(., .) the operators

[p0127-b0036 | ordinary-paragraph | medium] A,e (X; Xh), Bh∈ (X; M) and B,e (M; X) defined by:

[p0127-b0037 | ordinary-paragraph | low] 'XnA

[p0127-b0038 | ordinary-paragraph | low] VUhE Xh,

[p0127-b0039 | equation | low] <Ahu,Un> =a(u,Un)

[p0127-b0040 | ordinary-paragraph | low] 'XaA

[p0127-b0041 | equation | low] (Bhu,μh>=b(u,μn)

[p0127-b0042 | ordinary-paragraph | low] VunE Mh.

[p0127-b0043 | ordinary-paragraph | medium] Aue M.

[p0127-b0044 | ordinary-paragraph | low] Vun∈ Xh.

[p0127-b0045 | equation | low] <vn,Bhμ>=b(unμ)

[p0127-b0046 | ordinary-paragraph | medium] Strictly speaking, B', is not the dual operator of B, but if B, is restricted to X,

[p0127-b0047 | ordinary-paragraph | medium] and B' to M, then B, and B' are indeed dual operators. In addition, we

[p0127-b0048 | ordinary-paragraph | medium] obviously have:

[p0127-b0049 | ordinary-paragraph | low] XaA

[p0127-b0050 | equation | low] II Bnull m, ≤ II Bull m'

[p0127-b0051 | ordinary-paragraph | medium] with similar inequalities for Il A,ullx, and | B'μllxk.

[p0127-b0052 | ordinary-paragraph | medium] For each xe M', we define the finite-dimensional analogue of V(x):

[p0127-b0053 | equation | low] Vh(x) ={Un∈Xn; b(Unμn) =<xμn>Vμn∈ Mn}

[p0127-b0054 | ordinary-paragraph | medium] and we set

[p0127-b0055 | equation | low] Vh = V(0) = Ker(Bh)N Xh;

[p0127-b0056 | ordinary-paragraph | medium] i.e.

## PDF 128 / printed 114



[p0128-b0005 | ordinary-paragraph | low]    so ()  ()  4    e  m 3 

[p0128-b0006 | ordinary-paragraph | medium] proper subspace of M.

[p0128-b0007 | ordinary-paragraph | medium] Now we approximate Problem (Q) by Problem (Qh):

[p0128-b0008 | ordinary-paragraph | medium] Find a pair (un, 2n) in X, x M, satisfying:

[p0128-b0009 | ordinary-paragraph | low] x#aA

[p0128-b0010 | equation | low] a(un,Un) +b(unn)=<l,un>

[p0128-b0011 | equation | low] (1.7)

[p0128-b0012 | equation | low] b(unμn)=<x,μn>μn∈Mn

[p0128-b0013 | equation | low] (1.8)

[p0128-b0014 | ordinary-paragraph | medium] and we associate with (Qh) the following Problem (Ph):

[p0128-b0015 | ordinary-paragraph | medium] Find u,e Vh(x) such that:

[p0128-b0016 | ordinary-paragraph | low] ""aA

[p0128-b0017 | equation | low] (1.9)

[p0128-b0018 | equation | low] a(unUn)=<l0n>

[p0128-b0019 | ordinary-paragraph | medium] As V,  V, Problem (P,) may be viewed as an external approximation of Problem

[p0128-b0020 | ordinary-paragraph | medium] (P). Here again, the first component u, of any solution (u,, A,) of Problem (Qh) is

[p0128-b0021 | ordinary-paragraph | medium] also a solution of Problem (Ph). The converse is proved as part of the next

[p0128-b0022 | theorem | medium] theorem.

[p0128-b0023 | theorem | medium] Theorem 1.1. 1°) Assume that the following conditions hold:

[p0128-b0024 | ordinary-paragraph | medium] (i) Vh(x) is not empty;

[p0128-b0025 | equation | low] (ii) there exists a constant α* > O such that:

[p0128-b0026 | equation | low] (1.10)

[p0128-b0027 | equation | low] a(Un,Un)≥α*/0n11x

[p0128-b0028 | ordinary-paragraph | low] ""aA

[p0128-b0029 | ordinary-paragraph | medium] Then Problem (Pn) has a unique solution u, E Vh(x) and there exists a constant C,

[p0128-b0030 | ordinary-paragraph | medium] depending only upon α*, Ila! and I/bll such that the "error bound" holds:

[p0128-b0031 | equation | low] inf Ilu-vnllx+ inf |A— μhllm

[p0128-b0032 | equation | low] (1.11)

[p0128-b0033 | equation | low] Ilu - u,llx ≤ C1

[p0128-b0034 | ordinary-paragraph | low] (Un∈ Vn(x)

[p0128-b0035 | ordinary-paragraph | low] μhEMn

[p0128-b0036 | ordinary-paragraph | medium] 2°) Assume that hypothesis (ii) holds and, in addition, that:

[p0128-b0037 | equation | low] (ii) there exists a constant β* > O such that

[p0128-b0038 | ordinary-paragraph | medium] b(Un μh)

[p0128-b0039 | equation | low] (1.12)

[p0128-b0040 | equation | low] ≥β*11μn Il M

[p0128-b0041 | equation | low] sup

[p0128-b0042 | ordinary-paragraph | low] Vuhe Mh.

[p0128-b0043 | ordinary-paragraph | low] lun ll x

[p0128-b0044 | ordinary-paragraph | low] UhEXn

[p0128-b0045 | ordinary-paragraph | medium] Then Vh(x) ≠ Φ and there exists a unique Λ, in M, such that (un, Λn) is the only

[p0128-b0046 | ordinary-paragraph | medium] solution of Problem (Qn). Furthermore, there exists a constant C2 depending only

[p0128-b0047 | ordinary-paragraph | medium] upon α*, β*, Ilall and llbll such that:

[p0128-b0048 | ordinary-paragraph | low] inf Ilu-vnllx+ inf I-μnlm

[p0128-b0049 | ordinary-paragraph | low] (1.13) u -unlx + I/ -Anlim ≤ C2

[p0128-b0050 | ordinary-paragraph | low] UnEXh

[p0128-b0051 | ordinary-paragraph | low] μhEMn

[p0128-b0052 | ordinary-paragraph | low] od s os sm u ()' ui n e ssooo am da sou si ()' sa (1 oo

[p0128-b0053 | ordinary-paragraph | medium] Find z, in Vh such that

[p0128-b0054 | equation | low] a(ZhUn)=<l,un>—a(un,Un)Vun∈Vn.

## PDF 129 / printed 115



[p0129-b0004 | equation | low] un =Zh+ un

[p0129-b0005 | ordinary-paragraph | medium] is the only solution of Problem (P,).

[p0129-b0006 | ordinary-paragraph | medium] Now let w, be an arbitrary element of V(x); then v, = u, - w, e V, and

[p0129-b0007 | equation | low] (1.14)

[p0129-b0008 | equation | low] a(Uh,un) =<l,un>—a(wn,Un).

[p0129-b0009 | ordinary-paragraph | medium] Since v,e X,, we can take v = v, in (1.1) and substitute in (1.14). This yields:

[p0129-b0010 | equation | low] a(Un Un) =a(u —Wh,Un) + b(un, ).

[p0129-b0011 | ordinary-paragraph | medium] Moreover, since v, e Vh, we have b(vn, μn) = O u, E M,. Hence

[p0129-b0012 | equation | low] a(unUn)=a(u—Wn,Un) +b(un,—μn)

[p0129-b0013 | ordinary-paragraph | low] )AunEMh.

[p0129-b0014 | equation | low] (1.15)

[p0129-b0015 | ordinary-paragraph | medium] The V,-ellipticity of a and the continuity of a and b yield:

[p0129-b0016 | equation | low] Ilunllx ≤ (llall lu - W llx + Ilbil/A - μn ll m)/α*.

[p0129-b0017 | ordinary-paragraph | medium] Therefore

[p0129-b0018 | ordinary-paragraph | low] 1—μnllM

[p0129-b0019 | ordinary-paragraph | low] Ilu - Wn llx + 

[p0129-b0020 | equation | low] Ilu - uhllx ≤

[p0129-b0021 | ordinary-paragraph | medium] *

[p0129-b0022 | equation | low] (x) ="MA

[p0129-b0023 | ordinary-paragraph | low] Vuh e Mh.

[p0129-b0024 | ordinary-paragraph | low] llallbl

[p0129-b0025 | ordinary-paragraph | medium] This yields (1.11) with C, = max

[p0129-b0026 | ordinary-paragraph | low] *

[p0129-b0027 | ordinary-paragraph | medium] 2°) Let us apply Lemma I.4.1 to the particular case of X, and M,. Hypothesis

[p0129-b0028 | ordinary-paragraph | medium] (ii) implies that B, is an isomorphism from V, (taken in X,) onto M'. Therefore

[p0129-b0029 | ordinary-paragraph | medium] V(x) is not empty and according to n? 1 Problem (Ph) has a unique solution un.

[p0129-b0030 | ordinary-paragraph | medium] Furthermore, it follows from Corollary I.4.1 that there exists a unique , in M,

[p0129-b0031 | ordinary-paragraph | medium] such that the pair (u,, h) is the only solution of Problem (Qh).

[p0129-b0032 | ordinary-paragraph | medium] To derive the error bound (1.13) we shall first prove that

[p0129-b0033 | ordinary-paragraph | low] |/bll

[p0129-b0034 | equation | low] inf Ilu - Un llx.

[p0129-b0035 | equation | low] inf Ilu - wnllx ≤

[p0129-b0036 | equation | low] (1.16)

[p0129-b0037 | ordinary-paragraph | low] β*

[p0129-b0038 | ordinary-paragraph | low] Un∈Xh

[p0129-b0039 | ordinary-paragraph | medium] Wh∈ Vn(x)

[p0129-b0040 | ordinary-paragraph | medium] Let v, be an arbitrary element of X,; like above, there exists a unique z, in V

[p0129-b0041 | ordinary-paragraph | medium] such that

[p0129-b0042 | equation | low] Bh2h=Bh(u—Unh)

[p0129-b0043 | ordinary-paragraph | medium] and

[p0129-b0044 | equation | low] I/zhllx≤

[p0129-b0045 | ordinary-paragraph | medium] B*

[p0129-b0046 | ordinary-paragraph | medium] Thus, if we set wh, = Zh + vn, then

## PDF 130 / printed 116



[p0130-b0004 | ordinary-paragraph | low] Iu - Un llx.

[p0130-b0005 | equation | low] u —— Wnllx≤ 1|u ——Unllx+ I|zhllx

[p0130-b0006 | ordinary-paragraph | medium] R*

[p0130-b0007 | ordinary-paragraph | medium] As v, is arbitrary, this implies (1.16).

[p0130-b0008 | ordinary-paragraph | medium] It remains to evaluate IlX - A,llm. From (1.1) and (1.7) we derive that:

[p0130-b0009 | ordinary-paragraph | low] Vuh E Mh.

[p0130-b0010 | ordinary-paragraph | low] Vuhe Xh.

[p0130-b0011 | equation | low] b(un, -μn) =a(u——un,Un) +b(un——μn)

[p0130-b0012 | ordinary-paragraph | medium] Therefore hypothesis (1.12) yields:

[p0130-b0013 | ordinary-paragraph | medium] 1

[p0130-b0014 | ordinary-paragraph | medium] 1

[p0130-b0015 | ordinary-paragraph | low] {a(u——unUn)+b(un,—μn)}

[p0130-b0016 | equation | low] IIAh - μn llM ≤

[p0130-b0017 | equation | low]  sup

[p0130-b0018 | ordinary-paragraph | low] β*

[p0130-b0019 | ordinary-paragraph | low] vnexn llun1lx

[p0130-b0020 | ordinary-paragraph | medium] 1

[p0130-b0021 | ordinary-paragraph | low] Illall lu - unllx + IIbl/ lI - μhll m}.

[p0130-b0022 | ordinary-paragraph | medium] B*

[p0130-b0023 | ordinary-paragraph | medium] Hence

[p0130-b0024 | equation | low] Ilall lu -- u,llx+(β*+ libl)  inf I -μnlli

[p0130-b0025 | ordinary-paragraph | medium] (1.17)  -lm ≤

[p0130-b0026 | ordinary-paragraph | medium] β*

[p0130-b0027 | ordinary-paragraph | low] μnE Mn

[p0130-b0028 | ordinary-paragraph | medium] Then the bound (1.13) follows immediately from (1.11), (1.16) and (1.17).

[p0130-b0029 | remark | medium] Remark 1.1. The bound (1.11) can be slightly improved without making use of

[p0130-b0030 | ordinary-paragraph | medium] the inf-sup condition (1.12). Indeed, by applying (1.10) to (1.15) we obtain:

[p0130-b0031 | ordinary-paragraph | low] b(un,A——μh)

[p0130-b0032 | equation | low] Ilunllx ≤

[p0130-b0033 | equation | low] llall llu - wllx + sup

[p0130-b0034 | ordinary-paragraph | low] II un ll x

[p0130-b0035 | ordinary-paragraph | low] UnEVn

[p0130-b0036 | ordinary-paragraph | medium] Therefore

[p0130-b0037 | ordinary-paragraph | low] b(vh, -μh)

[p0130-b0038 | ordinary-paragraph | low] |a|l

[p0130-b0039 | ordinary-paragraph | medium] 1

[p0130-b0040 | equation | low] inf |iu- wnllx+

[p0130-b0041 | equation | low] inf   sup

[p0130-b0042 | equation | low] lu-unllx ≤

[p0130-b0043 | ordinary-paragraph | medium] x*

[p0130-b0044 | ordinary-paragraph | low] llunllx

[p0130-b0045 | ordinary-paragraph | medium] Wn∈ Vn(x)

[p0130-b0046 | ordinary-paragraph | low] un∈Mh Un∈Vn

[p0130-b0047 | equation | low] (1.18)

[p0130-b0048 | ordinary-paragraph | medium] Note that the expression

[p0130-b0049 | ordinary-paragraph | medium] b(vn-μn)

[p0130-b0050 | equation | low] inf  sup

[p0130-b0051 | ordinary-paragraph | low] lun ll x

[p0130-b0052 | ordinary-paragraph | low] UnEMh the Vh

[p0130-b0053 | ordinary-paragraph | medium] takes into account the fact that Vh  V: it vanishes when V, c V.

[p0130-b0054 | remark | medium] Remark 1.2. If besides Hypotheses (1.10) and (1.12) we assume that the bilinear

[p0130-b0055 | ordinary-paragraph | medium] form a(., .) is symmetric and semi-positive definite on X,, then we can relate

[p0130-b0056 | ordinary-paragraph | medium] Problems (Ph) and (Qh) to optimization problems. As in the continuous case,

[p0130-b0057 | ordinary-paragraph | medium] and with the same notations, it can be shown that the solution u, of (Ph) is

[p0130-b0058 | ordinary-paragraph | medium] characterized by:

[p0130-b0059 | equation | low] J(uh) = inf J(vn),

[p0130-b0060 | equation | low] (x)A=a

## PDF 131 / printed 117



[p0131-b0003 | equation | low] Lu, P,) = Min sup 2(v,,¢,) = Max inf S(v,, q,).

[p0131-b0004 | ordinary-paragraph | high] vnE Xp Ine Mp an€ Mp vn€ Xn

[p0131-b0005 | remark | high] Remark 1.3. From the argument of Theorem 1.1, we readily derive that if Hy-

[p0131-b0006 | ordinary-paragraph | high] potheses (1.10) and (1.12) hold then the solution (u,, 4,,) is bounded as follows:

[p0131-b0007 | ordinary-paragraph | high] 1 1

[p0131-b0008 | equation | low] I|Unlly S = {lll a peo an lal) tac

[p0131-b0009 | ordinary-paragraph | high] on

[p0131-b0010 | ordinary-paragraph | high] An lla Se UME: + Wall lea ll}.

[p0131-b0011 | ordinary-paragraph | high] Br

[p0131-b0012 | ordinary-paragraph | high] Observe that the bilinear form a(., .) is V,-elliptic as soon as a(v,, v,) > 0 for

[p0131-b0013 | ordinary-paragraph | high] all v, # 0. Similarly, the bilinear form b(., .) satisfies the discrete inf-sup condition

[p0131-b0014 | ordinary-paragraph | high] (1.12) provided Ker(B;,) M, = {0}. But of course in either case the constants

[p0131-b0015 | ordinary-paragraph | high] a* and f* will generally depend upon h. Now, in order to derive optimal error

[p0131-b0016 | ordinary-paragraph | high] bounds in Theorem 1.1, it is clear that both constants «* and f* must be

[p0131-b0017 | ordinary-paragraph | high] independent of h. And since usually V, ¢ V, the V-ellipticity of a(., .) does not

[p0131-b0018 | ordinary-paragraph | high] necessarily carry over to V,,. As a consequence, hypothesis (1.10) must be checked

[p0131-b0019 | ordinary-paragraph | high] in each particular case; but for the applications we have in mind, this is not a

[p0131-b0020 | ordinary-paragraph | high] major obstacle. On the other hand, the discrete inf-sup condition (1.12) which

[p0131-b0021 | ordinary-paragraph | high] acts as a uniform compatibility condition between X, and M, is much more

[p0131-b0022 | ordinary-paragraph | high] delicate to check. The following lemma due to Fortin [28] establishes a useful

[p0131-b0023 | ordinary-paragraph | high] criterion for (1.12).

[p0131-b0024 | lemma | high] Lemma 1.1. The inf-sup condition (1.12) holds with a constant f* > 0 independent

[p0131-b0025 | ordinary-paragraph | high] of hif and only if there exists an operator I,€ L(X; X,,) satisfying:

[p0131-b0026 | ordinary-paragraph | high] (1.19) b(v — 11,0; 4,)=90 Vey,eM, Voex

[p0131-b0027 | ordinary-paragraph | high] and

[p0131-b0028 | ordinary-paragraph | high] (1.20) |Z vlly <Cllvlly Voex

[p0131-b0029 | ordinary-paragraph | high] with a constant C > 0 independent of h.

[p0131-b0030 | proof | high] Proof. Assume that such an operator II, exists; then we have for all 4,€ M,:

[p0131-b0031 | ordinary-paragraph | high] b(Up, Un) eS bUT,v, Ln) a. b(v, Ln)

[p0131-b0032 | ordinary-paragraph | high] pee WO ee Whol oes Tv ll

[p0131-b0033 | ordinary-paragraph | high] owing to (1.19). Thus (1.20) and (1.5) imply that

[p0131-b0034 | equation | low] b(U;5 Un) > I bv,

[p0131-b0035 | equation | low] Hn) = L IlH all ae

[p0131-b0036 | ordinary-paragraph | high] v,pE Xn I Vp llx Cex |v llx C

[p0131-b0037 | ordinary-paragraph | high] and (1.12) follows with B* = B/C.

## PDF 132 / printed 118



[p0132-b0004 | equation | low] bUT,v, Un) = D(v, Hy) =V n€ My,

[p0132-b0005 | ordinary-paragraph | high] and

[p0132-b0006 | ordinary-paragraph | high] Peer alll

[p0132-b0007 | equation | low] Tv lly < Be | Biv lms, S pe IlU llx-

[p0132-b0008 | ordinary-paragraph | high] Clearly [7,¢ £(X; X,) and satisfies (1.20) with C = ||b||/B*. O

[p0132-b0009 | ordinary-paragraph | high] In practice, the construction of JJ, is by no means easy. The reader will find

[p0132-b0010 | ordinary-paragraph | high] in Section 1.4 how to establish the inf-sup condition in a number of cases without

[p0132-b0011 | ordinary-paragraph | high] constructing /7, explicitly.

[p0132-b0012 | remark | high] Remark 1.4. Another useful way of writing the inf-sup condition (1.12) is:

[p0132-b0013 | ordinary-paragraph | high] for each py, € M, there exists a v, in X,, (unique in V,") such that:

[p0132-b0014 | ordinary-paragraph | high] 1

[p0132-b0015 | equation | low] D(V;;Mn ) = Il Hall de> lUrllx < Be IlM al la e

[p0132-b0016 | ordinary-paragraph | high] This result, which is also valid in the continuous case, uses explicitly the fact that

[p0132-b0017 | ordinary-paragraph | high] \|. lly is a Hilbert norm.

[p0132-b0018 | remark | high] Remark 1.5. In the particular case where the bilinear form a(., .) coincides with

[p0132-b0019 | ordinary-paragraph | high] the scalar product ((., .)), associated with the Hilbert norm ||. || ,, formula (1.17)

[p0132-b0020 | ordinary-paragraph | high] simplifies to:

[p0132-b0021 | ordinary-paragraph | high] ; i ,

[p0132-b0022 | ordinary-paragraph | high] (1.17') IA = dale <5} inf ||u — wally + (B* + |[b||) inf |4— salle

[p0132-b0023 | ordinary-paragraph | high] Wn € Vn), Hye My,

[p0132-b0024 | ordinary-paragraph | high] Indeed, we have:

[p0132-b0025 | equation | low] D(Vp_,A n — My) = ((U — Wy, 0,))x + B(0,,2 — Ln)

[p0132-b0026 | ordinary-paragraph | high] Wo,€ Vis VwnE Vi), Vine Mi,

[p0132-b0027 | ordinary-paragraph | high] and the v, (in V,;+) of Remark 1.4 gives (1.17).

[p0132-b0028 | theorem | high] Theorem 1.1 readily yields the following general convergence results.

[p0132-b0029 | corollary | high] Corollary 1.1. Assume that the following hypotheses hold:

[p0132-b0030 | ordinary-paragraph | high] 1°) the form a(., .) satisfies (1.10) with a constant «* > 0 independent

[p0132-b0031 | ordinary-paragraph | high] of h;

[p0132-b0032 | ordinary-paragraph | high] 2°) there exist a dense subvariety V(x) of V(x), a dense subspace M of M

[p0132-b0033 | ordinary-paragraph | high] and

[p0132-b0034 | ordinary-paragraph | high] two mappings r,: V (x) > V,(x) and p,: M@ > M,, with:

[p0132-b0035 | equation | low] lim ||7,0 — v|ly = 0 YeV (yx),

[p0132-b0036 | equation | low] h>0

[p0132-b0037 | equation | low] im Pn! — Him =O Vue”.

## PDF 133 / printed 119



[p0133-b0004 | equation | low] lim Il u - u,llx = 0.

[p0133-b0005 | ordinary-paragraph | medium] h→0

[p0133-b0006 | corollary | medium] Corollary 1.2. We retain the above hypotheses on a( ., . ) and M and we assume that

[p0133-b0007 | ordinary-paragraph | medium] b(., . ) satisfies a uniform inf-sup condition (1.12). If there exists a dense subspace

[p0133-b0008 | ordinary-paragraph | medium] X of X and a mapping rn: X → X, satisfying:

[p0133-b0009 | equation | low] lim Ilrnu - vlx = 0

[p0133-b0010 | ordinary-paragraph | low] aA

[p0133-b0011 | ordinary-paragraph | medium] h→0

[p0133-b0012 | ordinary-paragraph | medium] then

[p0133-b0013 | equation | low] lim{lu - unllx + llA - Anllm} = 0.

[p0133-b0014 | ordinary-paragraph | medium] h→0

[p0133-b0015 | ordinary-paragraph | medium] Now, let us extend the classical duality argument of Aubin [3] and Nitsche

[p0133-b0016 | ordinary-paragraph | medium] [61] to the case of Problems (P) and (Ph). For this, we introduce a Hilbert space

[p0133-b0017 | ordinary-paragraph | medium] H with scalar product (., .) and associated norm I.I such that

[p0133-b0018 | ordinary-paragraph | medium] X c H with continuous imbedding and X is dense in H.

[p0133-b0019 | ordinary-paragraph | medium] We identify H with its dual space H' for the scalar product (., -). Therefore, H

[p0133-b0020 | ordinary-paragraph | medium] can be identified with a subspace of X':

[p0133-b0021 | ordinary-paragraph | medium] H e X' with continuous and dense imbedding.

[p0133-b0022 | ordinary-paragraph | medium] In order to evaluate |u -- u,l, we introduce for each g in H the unique solution

[p0133-b0023 | ordinary-paragraph | medium] pair (Φg, ,) of the dual problem:

[p0133-b0024 | equation | low] a(v,Φg) + b(v,) =(g,u)  Vv∈ X

[p0133-b0025 | equation | low] (1.21)

[p0133-b0026 | equation | low] b(Pg, μ) = O Vμe M.

[p0133-b0027 | theorem | medium] Theorem 1.2. Assume that Problem (P,) has a unique solution u,. Then there exists

[p0133-b0028 | ordinary-paragraph | medium] a constant C, depending only upon Ilal and /bll, such that:

[p0133-b0029 | equation | low] |u—un| ≤C|lu-unllx+ inf 1—μnlm

[p0133-b0030 | ordinary-paragraph | low] μne Mn

[p0133-b0031 | equation | low] (1.22)

[p0133-b0032 | ordinary-paragraph | low] inf IPg -- Pnllx + inf Ilg -- hlm

[p0133-b0033 | equation | low] x sup

[p0133-b0034 | ordinary-paragraph | low] geH gl

[p0133-b0035 | ordinary-paragraph | low] ShEMn

[p0133-b0036 | ordinary-paragraph | low] (n∈ Vn

[p0133-b0037 | proof | medium] Proof. On the one hand, we have:

[p0133-b0038 | ordinary-paragraph | medium] (g,u -— un)

[p0133-b0039 | equation | low] [u - u,| = sup

[p0133-b0040 | ordinary-paragraph | low] [gl

[p0133-b0041 | ordinary-paragraph | medium] gEH

[p0133-b0042 | ordinary-paragraph | medium] On the other hand by choosing v = u - u, in (1.21), we get

[p0133-b0043 | equation | low] (g,u - un) = a(u -— uhs Pg) + b(u -— uh,g).

[p0133-b0044 | equation | low] (1.23)

[p0133-b0045 | ordinary-paragraph | medium] Then taking into account (1.1) and (1.6) we find:

## PDF 134 / printed 120



[p0134-b0004 | ordinary-paragraph | low] Wuhe Mh

[p0134-b0005 | equation | low] b(Pg, - μn) = 0 

[p0134-b0006 | ordinary-paragraph | medium] and as ue V(x) and u, e V(x), we also have:

[p0134-b0007 | ordinary-paragraph | low] Ashe Mh.

[p0134-b0008 | equation | low] b(u -- un,Sn) = 0

[p0134-b0009 | ordinary-paragraph | medium] When substituted into (1.23), these three equalities yield:

[p0134-b0010 | ordinary-paragraph | low] ("un-—n)q + (un -u )q + (-- un-n) =(n-nb)

[p0134-b0011 | ordinary-paragraph | low] Vone Vh, Auh, She Mh.

[p0134-b0012 | ordinary-paragraph | medium] Hence

[p0134-b0013 | ordinary-paragraph | low] I(g,u - un)l ≤C{llu --unllx + I/A - μnllm}{llΦg - Φnllx + Ilg - Shllm}

[p0134-b0014 | ordinary-paragraph | low] "A

[p0134-b0015 | ordinary-paragraph | low] uh, Sh∈ Mh,

[p0134-b0016 | ordinary-paragraph | medium] where C = max( lla ll, Il blIl).

[p0134-b0017 | ordinary-paragraph | medium] 口

[p0134-b0018 | remark | medium] Remark 1.6. When Problem (Qh) has a solution (u,, A,) a straightforward modi-

[p0134-b0019 | ordinary-paragraph | medium] fication of the above argument shows that:

[p0134-b0020 | equation | low] [u-unl ≤ C{llu -unllx + I/ -Anlim}

[p0134-b0021 | ordinary-paragraph | medium] 1

[p0134-b0022 | equation | low] inf Ilg- Pnllx + inf Ig -Shllm{

[p0134-b0023 | equation | low] x sup

[p0134-b0024 | ordinary-paragraph | low] geH|gl

[p0134-b0025 | ordinary-paragraph | low] ShEMn

[p0134-b0026 | ordinary-paragraph | low] (on∈Xn

[p0134-b0027 | ordinary-paragraph | medium] with the constant C of (1.22).

[p0134-b0028 | subsection | medium] 1.2. Decoupling the Computation of u, and ,

[p0134-b0029 | ordinary-paragraph | medium] In this short section, we propose to apply the technique of Sections I.4.3 and 1.4.4

[p0134-b0030 | ordinary-paragraph | medium] to dissociate the computation of , from that of u,. These methods are often used

[p0134-b0031 | ordinary-paragraph | medium] in practice.

[p0134-b0032 | ordinary-paragraph | medium] Let us consider first the regularization procedure of Section I.4.3. Recall that

[p0134-b0033 | ordinary-paragraph | medium] we require a continuous, bilinear form c( ., .) on M, x M, which is supposed to

[p0134-b0034 | ordinary-paragraph | medium] be M,-elliptic, i.e. there exists a constant y* > O such that:

[p0134-b0035 | equation | low] (1.24)

[p0134-b0036 | equation | low] C(μn, uh) ≥ y* l/ uh llVunE Mh.

[p0134-b0037 | ordinary-paragraph | medium] With the form c( ., .) we associate as usual the operator C,e &(M,; M') by:

[p0134-b0038 | equation | low] <Chμh, Vh>= c(μn, Vn)

[p0134-b0039 | ordinary-paragraph | low] Wuh, VhE Mh.

[p0134-b0040 | ordinary-paragraph | medium] Like in the continuous case, for each & > 0 we introduce the Problem (Qh):

[p0134-b0041 | ordinary-paragraph | medium] Find a pair (u, Ai)e X, x M, such that

[p0134-b0042 | equation | low] "x≥"aA

[p0134-b0043 | equation | low] a(un,un) +b(vn,h)=<l,un>

[p0134-b0044 | equation | low] (1.25)

[p0134-b0045 | equation | low] EC(hμn)+b(u,μn)=<x,μn>

[p0134-b0046 | ordinary-paragraph | low] Wune Mh.

## PDF 135 / printed 121



[p0135-b0004 | ordinary-paragraph | medium] eliminated from the above equations. Thus Problem (Q) is equivalent to the

[p0135-b0005 | ordinary-paragraph | medium] following Problem (Ph):

[p0135-b0006 | ordinary-paragraph | medium] Find ue X, satisfying:

[p0135-b0007 | ordinary-paragraph | medium] 1

[p0135-b0008 | ordinary-paragraph | low] "x="aA

[p0135-b0009 | ordinary-paragraph | medium] (1.26)a(u,un) +<Ch 1Bnu,Bnun>=<l,un>+<Chx,Bnun>

[p0135-b0010 | ordinary-paragraph | low] 8

[p0135-b0011 | ordinary-paragraph | medium] where C-1 e S(M': M,) denotes the inverse of C,

[p0135-b0012 | ordinary-paragraph | medium] Clearly, the situation here is exactly that of Section I.4.3, wiih the operators

[p0135-b0013 | ordinary-paragraph | medium] B and C replaced by B, and C,. Hence the statement of Theorem 1.4.3 is valid

[p0135-b0014 | ordinary-paragraph | medium] for Problems (Pi) and (Q):

[p0135-b0015 | theorem | medium] Theorem 1.3. In addition to (1.12) and (1.24), assume that there exists a constant

[p0135-b0016 | ordinary-paragraph | medium] α* > O such that:

[p0135-b0017 | ordinary-paragraph | low] "x"aA

[p0135-b0018 | equation | low] a(UnUn)+<CBhUn,Bhun>≥α*|/un1x

[p0135-b0019 | equation | low] (1.27)

[p0135-b0020 | ordinary-paragraph | medium] Then Problems (Qh) and (Qh) for & ≤ 1 have both a unique solution (u,, Λn) and

[p0135-b0021 | ordinary-paragraph | medium] (u, X) in X, x M,. Moreover, for all ε ≤ &o small enough we have the following

[p0135-b0022 | ordinary-paragraph | medium] error bound:

[p0135-b0023 | equation | low] Iluh - unllx + I/A - Anllm ≤ K*&(ll llx + Ilxllm),

[p0135-b0024 | equation | low] (1.28)

[p0135-b0025 | ordinary-paragraph | medium] where the constant K* depends only upon α*, β*, Ilall, IIbll and I/cll.

[p0135-b0026 | ordinary-paragraph | medium] Likewise, we can refine (1.28) and obtain an asymptotic expansion for (u;, X;)

[p0135-b0027 | ordinary-paragraph | medium] of the problems:

[p0135-b0028 | ordinary-paragraph | low] "x"aA

[p0135-b0029 | equation | low] a(un,un) + b(un,An) = 0

[p0135-b0030 | equation | low] (1.29)

[p0135-b0031 | equation | low] b(un,μn)=c(an-,μn)

[p0135-b0032 | ordinary-paragraph | low] Vu,E Mh,

[p0135-b0033 | ordinary-paragraph | medium] starting with 2 = Λ,. We have the analogue of Theorem I.4.4:

[p0135-b0034 | theorem | medium] Theorem 1.4. Under the hypotheses of Theorem 1.3, we have for all integers N ≥ 1

[p0135-b0035 | ordinary-paragraph | medium] and for & ≤ &o small enough:

[p0135-b0036 | ordinary-paragraph | medium] N

[p0135-b0037 | ordinary-paragraph | medium] N

[p0135-b0038 | ordinary-paragraph | low] —nen

[p0135-b0039 | equation | low] ∑e"un 

[p0135-b0040 | ordinary-paragraph | low] uh —— uh -—

[p0135-b0041 | equation | low] n=1

[p0135-b0042 | equation | low] n=1

[p0135-b0043 | ordinary-paragraph | medium] M

[p0135-b0044 | ordinary-paragraph | medium] x

[p0135-b0045 | equation | low] (1.30)

[p0135-b0046 | equation | low] ≤K*e+1(I/llx + Ixllm),

[p0135-b0047 | ordinary-paragraph | medium] where the constant K* depends only upon N, α*, β*, Ilall, Ilbll and Ilcll.

[p0135-b0048 | ordinary-paragraph | medium] Now, we turn to the gradient algorithms of Section I.4.4. With the above

[p0135-b0049 | ordinary-paragraph | medium] notations, we set for each real parameter r ≥ 0:

## PDF 136 / printed 122



[p0136-b0003 | ordinary-paragraph | high] there exists a constant «* > 0 such that

[p0136-b0004 | ordinary-paragraph | high] (1.32) al (UpV,p ,) > &* |g VOne Xn.

[p0136-b0005 | ordinary-paragraph | high] Then the simple gradient algorithm with optimal parameter has the following

[p0136-b0006 | ordinary-paragraph | high] discrete version:

[p0136-b0007 | ordinary-paragraph | high] 1°) Given an initial guess 2?¢M,, compute the solution uleX , of the

[p0136-b0008 | ordinary-paragraph | high] problem

[p0136-b0009 | equation | low] ay (up, Un) = <1,0,> + NO MAG Te I)) NEL

[p0136-b0010 | ordinary-paragraph | high] 2°) For m > 0, knowing (uj", Aj")e X, x M,, determine (z;”,g;")X€; , < Mh,

[p0136-b0011 | ordinary-paragraph | high] py'e R and the pair (u7"*!, Ay"*")eX , x M,, by:

[p0136-b0012 | equation | low] (a) jh i = (¥, Un» — blur’. Hn) Ven, eM,

[p0136-b0013 | ordinary-paragraph | high] a

[p0136-b0014 | equation | low] ap (ZK, Up) = b(v, Sr) Vu, E Xp,

[p0136-b0015 | equation | low] C(Gn'> In’)

[p0136-b0016 | ordinary-paragraph | high] ;

[p0136-b0017 | ordinary-paragraph | high] 1.33 b fh a eA

[p0136-b0018 | equation | low] An? =A — Pr’ Gh's

[p0136-b0019 | ordinary-paragraph | high] (c) {

[p0136-b0020 | equation | low] Uhm +1 —= URSm se (Oym —_>m<

[p0136-b0021 | ordinary-paragraph | high] Needless to say, the above scheme is a gradient algorithm only when the

[p0136-b0022 | ordinary-paragraph | high] bilinear forms a(.,.) and c(.,.) are symmetric. Then the following result is a

[p0136-b0023 | ordinary-paragraph | high] direct consequence of Corollary 1.4.4.

[p0136-b0024 | theorem | high] Theorem 1.5. Suppose the bilinear forms al(., .), b(., .) and c(., .) satisfy respec-

[p0136-b0025 | ordinary-paragraph | high] tively (1.32), (1.12) and (1.24) and assume that a(., .) and c(., .) are symmetric. Then

[p0136-b0026 | ordinary-paragraph | high] the simple gradient algorithm (1.33) is convergent for every choice of the starting

[p0136-b0027 | ordinary-paragraph | high] value A? € M;,;:

[p0136-b0028 | equation | low] lim { || up" Up ta Ape Anlluc} =

[p0136-b0029 | ordinary-paragraph | high] m~ oo

[p0136-b0030 | ordinary-paragraph | high] Like in Section 1.4.4, observe that the simple gradient algorithm can converge

[p0136-b0031 | ordinary-paragraph | high] without optimal parameters. In that case, the bilinear form a(.,.) need not be

[p0136-b0032 | ordinary-paragraph | high] symmetric and we have the analogue of Theorem I.4.7:

[p0136-b0033 | theorem | high] Theorem 1.6. We retain all hypotheses of Theorem 1.5 except the symmetry as-

[p0136-b0034 | ordinary-paragraph | high] sumption on a(., .). Then the algorithm (1.33a) (1.33c) is convergenfto r every choice

[p0136-b0035 | ordinary-paragraph | high] of the initial guess Ap € M,, and every sequence of numbers (p,") in the range:

[p0136-b0036 | equation | low] O= mfp, < sup p,. = 28s

[p0136-b0037 | ordinary-paragraph | high] where

[p0136-b0038 | ordinary-paragraph | high] Chg aa (4; (Up,

[p0136-b0039 | ordinary-paragraph | high] 0,)/ || Ban lis,

## PDF 137 / printed 123



[p0137-b0004 | ordinary-paragraph | medium] is entirely similar to the scheme (1.4.70). Let us describe it for the sake of

[p0137-b0005 | ordinary-paragraph | medium] completeness:

[p0137-b0006 | ordinary-paragraph | medium] 1°) Starting from an initial guess A e M,, compute the solution u e X, of

[p0137-b0007 | ordinary-paragraph | medium] the problem:

[p0137-b0008 | ordinary-paragraph | low] "x"aA

[p0137-b0009 | equation | low] a(u,vn)=<l,vn>+b(uh,rC²x-)

[p0137-b0010 | ordinary-paragraph | medium] 2°) For m ≥ 0, knowing (um,Am)e Xh × M, compute gn, wm∈ Mh, zm∈Xh,

[p0137-b0011 | ordinary-paragraph | medium] p", onm e R and the pair (um+1, am+1)e X, × Mn, by:

[p0137-b0012 | equation | low] c(gn,μn)=<xn,μh>-b(un,μn)

[p0137-b0013 | ordinary-paragraph | low] Vune Mh,

[p0137-b0014 | ordinary-paragraph | low] c(gm, 9m)

[p0137-b0015 | ordinary-paragraph | medium] c(gm-1 , 9m-1)

[p0137-b0016 | equation | low] only if m ≥ 1

[p0137-b0017 | equation | low] @ = gh otherwise,

[p0137-b0018 | equation | low] (1.34)

[p0137-b0019 | equation | low] a(zn,vn)=b(un,@m),

[p0137-b0020 | ordinary-paragraph | low] c(gn", gm)

[p0137-b0021 | ordinary-paragraph | low] Pn

[p0137-b0022 | ordinary-paragraph | low] b(zm,9m")'

[p0137-b0023 | ordinary-paragraph | low] m-prom,

[p0137-b0024 | equation | low] =

[p0137-b0025 | equation | low] =um + pmzm.

[p0137-b0026 | theorem | medium] Theorem 1.7. The conjugate-gradient algorithm converges with the hypotheses of

[p0137-b0027 | theorem | medium] Theorem 1.5.

[p0137-b0028 | subsection | medium] 1.3. Application to the Homogeneous Stokes Problem

[p0137-b0029 | ordinary-paragraph | medium] For the sake of simplicity, we focus our attention on homogeneous boundary

[p0137-b0030 | ordinary-paragraph | medium] conditions. Let Ω be a bounded, connected, open subset of R with a Lipschitz-

[p0137-b0031 | ordinary-paragraph | medium] continuous boundary F and let f be a given function of H-1(Q). Recall that the

[p0137-b0032 | ordinary-paragraph | medium] homogeneous Stokes equations:

[p0137-b0033 | ordinary-paragraph | medium] Find (u, p) in H(Q) x L2(Q) such that

[p0137-b0034 | equation | low] -- v4u + grad p = f

[p0137-b0035 | equation | low] (1.35)

[p0137-b0036 | ordinary-paragraph | medium] in Ω,

[p0137-b0037 | equation | low] divu = 0

[p0137-b0038 | ordinary-paragraph | medium] has a unique solution. Moreover, setting either

[p0137-b0039 | ordinary-paragraph | medium] N

[p0137-b0040 | equation | low] a(u, v) = 2v ∑ (D;(u), D;(v))

[p0137-b0041 | ordinary-paragraph | medium] (a)

[p0137-b0042 | ordinary-paragraph | medium] i,1

[p0137-b0043 | equation | low] (1.36)

[p0137-b0044 | ordinary-paragraph | medium] ）or

[p0137-b0045 | equation | low] a(u, v) = v(grad u, grad v),

[p0137-b0046 | ordinary-paragraph | medium] (b)

[p0137-b0047 | ordinary-paragraph | medium] we know that (1.35) is equivalent to the variational formulation:

## PDF 138 / printed 124



[p0138-b0004 | ordinary-paragraph | low] N()HAA

[p0138-b0005 | equation | low] a(u, v) -- (p, div v) = (f, v)

[p0138-b0006 | equation | low] (1.37)

[p0138-b0007 | equation | low] (q, divu) = 0  Vqe L(Ω).

[p0138-b0008 | ordinary-paragraph | medium] With the following substitutions:

[p0138-b0009 | equation | low] Il- Ilm = Il. llo,2,

[p0138-b0010 | equation | low] Il.Ilx = I.l1,2s

[p0138-b0011 | equation | low] X = H(Ω),  M = L(Ω),

[p0138-b0012 | equation | low] b(v,q) = -(q, div v),

[p0138-b0013 | equation | low] x=0,  I=f

[p0138-b0014 | ordinary-paragraph | medium] this is exactly the problem studied in Section I.5.1.

[p0138-b0015 | ordinary-paragraph | medium] Now, for each h let W, and Q, be two finite-dimensional spaces such that

[p0138-b0016 | ordinary-paragraph | low] Wh c H'(Ω),  Qh c L²(Ω)

[p0138-b0017 | ordinary-paragraph | medium] and throughout this section we assume that Qh, contains the constant functions.

[p0138-b0018 | ordinary-paragraph | medium] We set:

[p0138-b0019 | equation | low] Xh = Wn∩ H(Q) = {vh∈ Wh; Vnr = 0},

[p0138-b0020 | equation | low] (1.38)

[p0138-b0021 | equation | low] = xp"b

[p0138-b0022 | equation | low] M, = Qh ∩ L2(Ω) =

[p0138-b0023 | ordinary-paragraph | low] {ah∈ Qh;

[p0138-b0024 | ordinary-paragraph | medium] With these spaces, Problem (1.37) is approximated by:

[p0138-b0025 | ordinary-paragraph | medium] Find a pair (un, Ph)e X, x Mh such that:

[p0138-b0026 | ordinary-paragraph | low] Wwhe Xh,

[p0138-b0027 | equation | low] a(un,Vn)—(Phdivvh) =<f,vn)

[p0138-b0028 | equation | low] (1.39)

[p0138-b0029 | equation | low] (qh, divun) = O Vah∈ Mn.

[p0138-b0030 | ordinary-paragraph | medium] As div u, e L?(Q), observe that the second equation in (1.39) is cquivalent to

[p0138-b0031 | equation | low] (an, divun) = 0  Van∈Qh.

[p0138-b0032 | ordinary-paragraph | medium] In view of this remark, the corresponding space V, is given by:

[p0138-b0033 | equation | low] Vh = {vh∈Xh;(ah, divvh) = O Van∈Qn}.

[p0138-b0034 | ordinary-paragraph | medium] Hence the Problem (P,) associated with (1.39) is:

[p0138-b0035 | ordinary-paragraph | medium] Find u, e V, satisfying

[p0138-b0036 | equation | low] (1.40)

[p0138-b0037 | equation | low] "="AA

[p0138-b0038 | equation | low] a(un,Vh) =<f,vn)

[p0138-b0039 | remark | medium] Remark 1.7. As mentioned in the preceding section, V, is generally not included

[p0138-b0040 | ordinary-paragraph | medium] in V: {ve H(Ω); div v = O}; this will be the case in all the examples of this

[p0138-b0041 | ordinary-paragraph | medium] chapter. Thus the functions of V, are not divergence-free but satisfy only

[p0138-b0042 | equation | low] Pn(divvh) = 0,

[p0138-b0043 | ordinary-paragraph | medium] where p, is the orthogonal projection of L2(Ω) onto Qh. As a consequence, the

## PDF 139 / printed 125



[p0139-b0003 | ordinary-paragraph | high] equivalent formulations.

[p0139-b0004 | ordinary-paragraph | high] In order to study Problem (1.40) we relate the continuous and discrete spaces

[p0139-b0005 | ordinary-paragraph | high] by the following hypotheses:

[p0139-b0006 | ordinary-paragraph | high] Hypothesis H1 (Approximation property of X,,). There exist an operator r,€

[p0139-b0007 | ordinary-paragraph | high] L(A? (Q)§; W,) ON L((H7(Q) N H4(Q))%; X,,) and an integer | such that:

[p0139-b0008 | ordinary-paragraph | high] G4 ev Avro Cn7lView > VYeH™ (OQ), lama.

[p0139-b0009 | ordinary-paragraph | high] Hypothesis H2 (Approximation property of Q,). There exist an operator S,€

[p0139-b0010 | ordinary-paragraph | high] L(L?(Q); Q,) such that:

[p0139-b0011 | ordinary-paragraph | high] (1.42) la —Sidlloe<Ch™\Id Ima VaeH™(Q), O<me<l.

[p0139-b0012 | ordinary-paragraph | high] Hypothesis H3 (Uniform inf-sup condition). For each q,,€ M,, there exists av,€ X,,

[p0139-b0013 | ordinary-paragraph | high] such that

[p0139-b0014 | ordinary-paragraph | high] (1.43) (dn, div V,) = |ldnllo,0

[p0139-b0015 | ordinary-paragraph | high] (1.44) IWalt,@ < Cll dallo.e

[p0139-b0016 | ordinary-paragraph | high] with a constant C > 0 independent of h, q;, and Vy.

[p0139-b0017 | ordinary-paragraph | high] Recall that according to Remark 1.4 the statement of Hypothesis H3 is equivalent

[p0139-b0018 | ordinary-paragraph | high] to the inf-sup condition (1.12) with B* = 1/C.

[p0139-b0019 | theorem | high] Theorem 1.8. Under Hypotheses H1, H2 and H3, Problem (1.39) has a unique

[p0139-b0020 | ordinary-paragraph | high] solution (u,,p,)€V, x M, and u, is also the only solution of Problem (1.40). In

[p0139-b0021 | ordinary-paragraph | high] addition, (u,, p,,) tends to the solution (u, p) of Problem (1.35):

[p0139-b0022 | ordinary-paragraph | high] (1.45) lim {{u, — Wly,o+ Px — Pllo,a=} 9 .

[p0139-b0023 | equation | low] h>0

[p0139-b0024 | ordinary-paragraph | high] Furthermore, when (u,p ) belongs to H™*1(Q)% x (H™(Q)N Lo(Q)) for some

[p0139-b0025 | ordinary-paragraph | high] integer m with 1 < m <l, we have the error bound:

[p0139-b0026 | ordinary-paragraph | high] (1.46) ju — uglia + IP — Pallo.g < Ch {4 llms1.0 + IP limos:

[p0139-b0027 | proof | high] Proof. Let us apply Theorem 1.1. Owing to Hypothesis H3, the pair of spaces

[p0139-b0028 | ordinary-paragraph | high] (X,,M,,) satisfies a uniform inf-sup condition; therefore it suffices to check the

[p0139-b0029 | ordinary-paragraph | high] ellipticity of a(., .) in order to obtain that Problem (1.39) has a unique solution.

[p0139-b0030 | ordinary-paragraph | high] When a(., .) is defined by (1.36b), we have:

[p0139-b0031 | equation | low] a(v,v) =v\vi2q WeH'(Q)*

[p0139-b0032 | ordinary-paragraph | high] inequality (cf. (1.5.31))

[p0139-b0033 | ordinary-paragraph | high] and when a(., .) is defined by (1.36a) we use Korn’s

[p0139-b0034 | equation | low] av.) >vivii.g Wwe H§(2)*.

## PDF 140 / printed 126



[p0140-b0003 | ordinary-paragraph | high] that Problem (1.39) has a unique solution (u,,p,)¢X), x M,, where u, is the

[p0140-b0004 | ordinary-paragraph | high] unique solution of Problem (1.40), and we have:

[p0140-b0005 | ordinary-paragraph | high] (1.47) ja ayh.a+ bP Pao. C14 inf |u—v,|;,q+ inf I2 ~ aulo.o}

[p0140-b0006 | ordinary-paragraph | high] VnE Xn qn€ My

[p0140-b0007 | ordinary-paragraph | high] with a constant C, independent of h.

[p0140-b0008 | ordinary-paragraph | high] Now, observe that if s, does not map Lg(Q) onto M, we can replace it by:

[p0140-b0009 | ordinary-paragraph | high] - 1

[p0140-b0010 | equation | low] Snd = Sand — le Spq ax;

[p0140-b0011 | ordinary-paragraph | high] then 5,¢ L(L7(Q);M,) and 5.4 — dllo.e< snd — Glog VaeLo(Q). Thus if

[p0140-b0012 | ordinary-paragraph | high] pe H™(Q) L3(Q), Hypothesis H2 gives:

[p0140-b0013 | equation | low] inf ||P — dallo,e< |P — SpPllo,e < Cyh™ ||P \lm,a-

[p0140-b0014 | ordinary-paragraph | high] qne My,

[p0140-b0015 | ordinary-paragraph | high] Likewise, if ue H”*'(Q)*" NV, Hypothesis H1 yields:

[p0140-b0016 | equation | low] inf |u — v,|,,.0< |u—7%<U C3lh™|,Ul,| 0nit ,a-

[p0140-b0017 | ordinary-paragraph | high] VnAE Xp,

[p0140-b0018 | ordinary-paragraph | high] These inequalities and (1.47) imply (1.46).

[p0140-b0019 | ordinary-paragraph | high] It remains to establish the limit (1.45). For this we make use of Corollary 1.2

[p0140-b0020 | ordinary-paragraph | high] and the above considerations. We know that H?(Q)M H}(Q) is dense in H}({Q)

[p0140-b0021 | ordinary-paragraph | high] and that H'(Q)M L$(Q) is dense in L3(Q). Hence it suffices to work with the

[p0140-b0022 | ordinary-paragraph | high] above operators r, and s, to obtain (1.45). i

[p0140-b0023 | ordinary-paragraph | high] Of course, (1.46) implies that ||u — u, ||oo = O(h™), but it is possible to refine

[p0140-b0024 | ordinary-paragraph | high] this estimate by making use of Theorem 1.2. Here we take

[p0140-b0025 | ordinary-paragraph | high] He LQ

[p0140-b0026 | ordinary-paragraph | high] Then Problem (1.21) is the homogeneous Stokes Problem:

[p0140-b0027 | ordinary-paragraph | high] Find a pair (9, €) in Hj(Q)*% x L3(Q) such that:

[p0140-b0028 | ordinary-paragraph | high] (1.48) —vAg + gradé = g

[p0140-b0029 | ordinary-paragraph | high] in Q, where ge L?(Q)*.

[p0140-b0030 | equation | low] div@ =0

[p0140-b0031 | ordinary-paragraph | high] We shall require below the following concept of regularity for this problem.

[p0140-b0032 | definition | high] Definition 1.1. We say that Problem (1.48) is regular if the mapping

[p0140-b0033 | equation | low] (p, Cc) —vA@ + grad€

[p0140-b0034 | ordinary-paragraph | high] is an isomorphism from [H?(Q)*NV] x [H1(Q)N L2(Q)] onto L7(Q)".

[p0140-b0035 | ordinary-paragraph | high] This definition means that @ belongs to H?(Q)" and & to H'!(Q) whenever the

[p0140-b0036 | ordinary-paragraph | high] right-hand side g belongs to L?(Q)" and

## PDF 141 / printed 127



[p0141-b0003 | ordinary-paragraph | medium] Observe that in view of Theorem 1.5.4, Problem (1.48) is regular as soon as the

[p0141-b0004 | ordinary-paragraph | medium] boundary I of Ω is of class &2. When F is only Lipschitz-continuous -and

[p0141-b0005 | ordinary-paragraph | medium] subsequently I will be a polygonal line—Remark 1.5.6 asserts that Problem

[p0141-b0006 | ordinary-paragraph | medium] (1.48) is regular provided Q is a plane, bounded and convex polygon.

[p0141-b0007 | ordinary-paragraph | medium] 'Theorem 1.9. Assume that Hypotheses H1, H2 and H3 are satisfied and that

[p0141-b0008 | ordinary-paragraph | medium] Problem (1.48) is regular. Then, if the solution (u, p) of the Stokes Problem (1.35)

[p0141-b0009 | ordinary-paragraph | medium] belongs to Hm+1(Q) x Hm(Ω)N L2(Q) for some integer m with 1 ≤ m ≤l, we

[p0141-b0010 | ordinary-paragraph | medium] have the following error bound:

[p0141-b0011 | equation | low] 1l u - unllo,2 ≤ Chm+1(llu llm+1,2 + l pllm,2).

[p0141-b0012 | equation | low] (1.50)

[p0141-b0013 | proof | medium] Proof. According to Theorem 1.2 and Remark 1.6, we have:

[p0141-b0014 | equation | low] llu- un llo,2 ≤ C {lu - unl1,2 + llp - phllo.2}

[p0141-b0015 | equation | low] (1.51)

[p0141-b0016 | ordinary-paragraph | medium] 1

[p0141-b0017 | equation | low] inf Ip - Pnl1,s + inf  - Shllo,2{

[p0141-b0018 | equation | low] x sup

[p0141-b0019 | ordinary-paragraph | low] geL2(2) 1gll0,Q (neXn

[p0141-b0020 | ordinary-paragraph | low] Sh∈Mh

[p0141-b0021 | ordinary-paragraph | low]   ()a  () >  A  o)H    (t 1) o 

[p0141-b0022 | ordinary-paragraph | medium] extra power of h in (1.50) follows from Hypotheses H1 and H2 with m = 1 and

[p0141-b0023 | ordinary-paragraph | medium] (1.46) substituted into (1.51).

[p0141-b0024 | ordinary-paragraph | medium] Thus Hypothesis H1 with m = 1 and Hypothesis H2 with m = 1 yield:

[p0141-b0025 | equation | low] inf Ilg - E,llo,o ≤ C4hl§li,Q.

[p0141-b0026 | equation | low] inf Ip - Φhl1,o ≤ Chlpl2,2,

[p0141-b0027 | ordinary-paragraph | low] SheMn

[p0141-b0028 | ordinary-paragraph | low] Φn∈Vn

[p0141-b0029 | ordinary-paragraph | medium] Therefore combining (1.49) and (1.51) we obtain:

[p0141-b0030 | equation | low] |u - unl1,s + inf Ilp - anllo,.2{

[p0141-b0031 | equation | low] Ilu -unllo,2 ≤ Csh

[p0141-b0032 | ordinary-paragraph | low] qhE Mh

[p0141-b0033 | ordinary-paragraph | medium] and (1.50) follows from (1.46) and (1.42).

[p0141-b0034 | ordinary-paragraph | low] 口

[p0141-b0035 | ordinary-paragraph | medium] As mentioned in the previous section, the verification of Hypothesis H3 is

[p0141-b0036 | ordinary-paragraph | medium] bound to be often quite intricate. In fact, the choice of the spaces X, and M, is

[p0141-b0037 | ordinary-paragraph | medium] The reader will find in the next section how to construct such pairs of spaces.

[p0141-b0038 | ordinary-paragraph | medium] We finish this section with a brief survey of the iterative methods proposed

[p0141-b0039 | ordinary-paragraph | medium] in Section 1.2 to decouple the computation of u, from that of ph. We choose the

[p0141-b0040 | ordinary-paragraph | medium] scalar product of L2(Q) for the bilinear form c( ., .):

[p0141-b0041 | ordinary-paragraph | medium] p(x)q(x)dx.

[p0141-b0042 | equation | low] c(p,q) =

[p0141-b0043 | ordinary-paragraph | low] Q

[p0141-b0044 | ordinary-paragraph | medium] Then, the penalized version of Problem (1.40) becomes:

[p0141-b0045 | ordinary-paragraph | medium] Find a function ui, e X, such that

## PDF 142 / printed 128



[p0142-b0003 | ordinary-paragraph | high] Problem (1.52) dissociates the computation of uj, from that of p;, since here p;,

[p0142-b0004 | ordinary-paragraph | high] is given explicitly by

[p0142-b0005 | equation | low] pi = ——p a(diuvi )

[p0142-b0006 | ordinary-paragraph | high] But, of course, this problem offers a practical interest only if the calculation of

[p0142-b0007 | ordinary-paragraph | high] p, (div v,) is simple. This will be precisely the case of nearly all methods discussed

[p0142-b0008 | ordinary-paragraph | high] in this chapter because the functions of M,, will be piecewise discontinuous and

[p0142-b0009 | ordinary-paragraph | high] p, Will be a local operator.

[p0142-b0010 | ordinary-paragraph | high] As far as the convergence of uj, is concerned, a straightforward application

[p0142-b0011 | ordinary-paragraph | high] of Theorem 1.3 gives the following result.

[p0142-b0012 | theorem | high] Theorem 1.10. Problem (1.52) has a unique solution uj, for all ¢ > 0. Moreover,

[p0142-b0013 | ordinary-paragraph | high] under Hypothesis H3, we have for all € < & sufficiently small:

[p0142-b0014 | ordinary-paragraph | high] 1 :

[p0142-b0015 | equation | low] lu, — Uslie + |Pa + Paldiv ur) < Cellfll-1,0

[p0142-b0016 | ordinary-paragraph | high] 0,2

[p0142-b0017 | ordinary-paragraph | high] with a constant C > 0 independent of h and «.

[p0142-b0018 | ordinary-paragraph | high] Similarly, uj; and p; can be expanded in powers of «. Starting with p? = p,,

[p0142-b0019 | ordinary-paragraph | high] we define the sequence (uj, pj) € X), x M,, solution of

[p0142-b0020 | equation | low] a(u;,Vv,) — (divv,,pi)=90 Vv,EX;,,

[p0142-b0021 | equation | low] (1.53)

[p0142-b0022 | equation | low] (div uy, dn) = —(Ph °.4n) Van€ Qn.

[p0142-b0023 | ordinary-paragraph | high] Then Theorem 1.4 yields the following asymptotic expansion:

[p0142-b0024 | theorem | high] Theorem 1.11. Under Hypothesis H3, we have for all integers M > 1 and alle < &

[p0142-b0025 | ordinary-paragraph | high] sufficiently small:

[p0142-b0026 | ordinary-paragraph | high] M Liee M

[p0142-b0027 | equation | low] u, —u,— > "ur ae — p,(div uj) + p, + > e"pR

[p0142-b0028 | equation | low] n=1 1,92 é n=1 0,Q

[p0142-b0029 | equation | low] ~ rey oe [fll_1,0,

[p0142-b0030 | ordinary-paragraph | high] with a constant Ky independent of h and «.

[p0142-b0031 | ordinary-paragraph | high] Now, let us discuss the gradient algorithms. With the above choice of c(., .),

[p0142-b0032 | ordinary-paragraph | high] the bilinear form a’"(., .) reads:

[p0142-b0033 | equation | low] a;( u,v) = a(u, v) + r(p,(div u), p,(div v)).

[p0142-b0034 | ordinary-paragraph | high] It is H}(Q)*-elliptic and obviously symmetric. Therefore, the algorithms de-

[p0142-b0035 | ordinary-paragraph | high] scribed by (1.33) and (1.34) are genuine gradient algorithms. The formulas for the

[p0142-b0036 | ordinary-paragraph | high] simple gradient algorithm with optimal parameter are:

[p0142-b0037 | ordinary-paragraph | high] 1°) Predict the initial value p? ¢ M, and compute the solution uy € X, of:

## PDF 143 / printed 129



[p0143-b0005 | ordinary-paragraph | medium] 2°) For m ≥O, knowing (u,p) determine z"e X, μeR and the pair

[p0143-b0006 | ordinary-paragraph | low] (um+1,pm+1)∈ Xn x Mn by:

[p0143-b0007 | equation | low] a(zn, vn) =--(pn(divum), Pn(divvh))

[p0143-b0008 | ordinary-paragraph | low] Vvhe Xh;

[p0143-b0009 | equation | low] Il Ph(div um)12,2

[p0143-b0010 | equation | low] (pn(div u), pn(div z))

[p0143-b0011 | equation | low] = pm —μpn(div u),

[p0143-b0012 | ordinary-paragraph | low] um + ur zn.

[p0143-b0013 | ordinary-paragraph | medium] The conjugate-gradient algorithm initializes u like above and replaces step n° 2

[p0143-b0014 | ordinary-paragraph | medium] by:

[p0143-b0015 | ordinary-paragraph | medium] 2°) For m ≥0, knowing (um,pm)eX, x M, compute (zm,om)eX, × Mh

[p0143-b0016 | ordinary-paragraph | medium] (μn, om)e R × R and the pair (um+1, pm+1)e X, × M, by:

[p0143-b0017 | equation | low] Il Ph(div u")12.2

[p0143-b0018 | ordinary-paragraph | medium] m

[p0143-b0019 | ordinary-paragraph | low] Oh

[p0143-b0020 | equation | low] Il k(div ug-1)112,2

[p0143-b0021 | equation | low] only if m ≥ 1,

[p0143-b0022 | equation | low] w = p(div u),

[p0143-b0023 | ordinary-paragraph | low] Wvhe Xh,

[p0143-b0024 | equation | low] a(zn,vn) =-(@n,divvn)

[p0143-b0025 | equation | low] Il Pn(div ur)ll?.2

[p0143-b0026 | ordinary-paragraph | medium] μm

[p0143-b0027 | equation | low] (pn(div u), ph(div zm))

[p0143-b0028 | equation | low] = p-μ@,

[p0143-b0029 | equation | low] =um + μrzn.

[p0143-b0030 | ordinary-paragraph | medium] It follows from Theorems 1.5 and 1.7 that both gradient algorithms are convergent

[p0143-b0031 | ordinary-paragraph | medium] provided the Hypothesis H3 holds. Furthermore, the simple-gradient algorithm

[p0143-b0032 | ordinary-paragraph | medium] converges for any choice of the parameters μm such that:

[p0143-b0033 | equation | low] 0 < inf μm ≤ sup μn <

[p0143-b0034 | ordinary-paragraph | medium] m

[p0143-b0035 | ordinary-paragraph | medium] m

[p0143-b0036 | subsection | medium] 1.4. Checking the inf-sup Condition

[p0143-b0037 | ordinary-paragraph | medium] This short section is dedicated to the construction of pairs of spaces (X, M,) that

[p0143-b0038 | ordinary-paragraph | medium] satisfy uniformly the inf-sup condition (1.12). The underlying idea due to Boland

[p0143-b0039 | ordinary-paragraph | medium] & Nicolaides [11], is that if (1.12) holds uniformly for a pair of spaces (X, M,)

[p0143-b0040 | ordinary-paragraph | medium] then one can generate a whole family of pairs of spaces that also satisfy (1.12)

[p0143-b0041 | ordinary-paragraph | medium] uniformly provided they satisfy a local inf-sup condition. In other words, the

[p0143-b0042 | ordinary-paragraph | medium] global condition (1.12) can be reduced to a local condition, which is of course

## PDF 144 / printed 130



[p0144-b0004 | ordinary-paragraph | medium] open subsets Q, with boundary I,:

[p0144-b0005 | ordinary-paragraph | medium] R

[p0144-b0006 | equation | low] Ω =UΩ,.

[p0144-b0007 | equation | low] r=1

[p0144-b0008 | ordinary-paragraph | medium] Let X, and M, be defined by (1.38) with R c Qh. For 1 ≤ r ≤ R we set:

[p0144-b0009 | equation | low] X(Ω,) = {veXh; v = 0 in Ω - Ω,},

[p0144-b0010 | equation | low] Qh(Ω) = {qo,; q∈Qn},

[p0144-b0011 | equation | low] (1.54)

[p0144-b0012 | equation | low] M,(Q,) = Qh(Q,)N L(Q,),

[p0144-b0013 | equation | low] Mh, = {qe L?(Ω); qjo, is constant, 1 ≤ r ≤ R}.

[p0144-b0014 | equation | low] (1.55)

[p0144-b0015 | ordinary-paragraph | medium] Note that the functions of X,(Ω,) belong to H(Q,). We introduce as an

[p0144-b0016 | ordinary-paragraph | medium] assumption the following concept of uniform, local inf-sup condition with respect

[p0144-b0017 | ordinary-paragraph | medium] to this partition:

[p0144-b0018 | ordinary-paragraph | medium] Hypothesis H4. There exists a constant X* > 0, independent of h and r, such that:

[p0144-b0019 | equation | low] Jo, qh div vn dx 

[p0144-b0020 | equation | low] ≥ A* 1l4hll0,2,

[p0144-b0021 | equation | low] (1.56)

[p0144-b0022 | ordinary-paragraph | low] VaneM(Ω),  1 ≤r ≤ R.

[p0144-b0023 | equation | low] sup

[p0144-b0024 | ordinary-paragraph | low] [Vhli,2,

[p0144-b0025 | ordinary-paragraph | low] h∈Xn(S) 

[p0144-b0026 | ordinary-paragraph | medium] Let us establish the salient result of this section.

[p0144-b0027 | theorem | medium] Theorem 1.12. Let the pair of spaces (X, M,) defined by (1.38) satisfy Hypothesis

[p0144-b0028 | ordinary-paragraph | medium] H4. If there exists a subspace X, of X, such that the pair (X,, Mh) satisfies the

[p0144-b0029 | ordinary-paragraph | medium] inf-sup condition (1.12) with a constant β independent of h, then (X,, Mh) also

[p0144-b0030 | ordinary-paragraph | medium] satisfies (1.12) with a constant β* independent of h.

[p0144-b0031 | proof | medium] Proof. From the definition (1.54) we derive immediately the orthogonal decom-

[p0144-b0032 | ordinary-paragraph | medium] position of Q,(Ω,):

[p0144-b0033 | equation | low] Qh(Ω,) = M,(Ω,) ① R

[p0144-b0034 | ordinary-paragraph | medium] Thus each function qn e M, can be split as follows:

[p0144-b0035 | equation | low] “+=b

[p0144-b0036 | ordinary-paragraph | medium] where

[p0144-b0037 | ordinary-paragraph | medium] 1

[p0144-b0038 | equation | low] gh2, =

[p0144-b0039 | ordinary-paragraph | low] qh dx

[p0144-b0040 | ordinary-paragraph | medium] meas(Ω,) J

[p0144-b0041 | ordinary-paragraph | medium] and á, = ahl2, E M,(Q,). Observe that qnE M, and that the orthogonality of the

[p0144-b0042 | ordinary-paragraph | medium] decomposition implies:

[p0144-b0043 | equation | low] I ah ll6,2 = Ilanll6,α + Il ah ll0.2.

[p0144-b0044 | equation | low] (1.57)

[p0144-b0045 | ordinary-paragraph | medium] Now, owing to Hypothesis H4 and Remark 1.4 there exists a function

## PDF 145 / printed 131



[p0145-b0003 | equation | low] q, divv, dx = Ila ll,2,,

[p0145-b0004 | ordinary-paragraph | low] Jsr

[p0145-b0005 | equation | low] (1.58)

[p0145-b0006 | equation | low] rl1,2, ≤ llarllo,2,.

[p0145-b0007 | ordinary-paragraph | low] 1*

[p0145-b0008 | ordinary-paragraph | medium] Similarly, since the pair (X , M,) satisfies (1.12) there exists a function v, e X , such

[p0145-b0009 | ordinary-paragraph | medium] that

[p0145-b0010 | equation | low] Gn divvndx = 1/anll,,

[p0145-b0011 | equation | low] (1.59)

[p0145-b0012 | equation | low] Ivhli.o ≤ llah llo.2.

[p0145-b0013 | ordinary-paragraph | medium] β

[p0145-b0014 | ordinary-paragraph | medium] Let , be the function of X, defined by:

[p0145-b0015 | equation | low] Vhlo, = Vr.

[p0145-b0016 | ordinary-paragraph | medium] We propose to associate with q, the function v,e X,:

[p0145-b0017 | equation | low] Vh =h+ aVn,

[p0145-b0018 | ordinary-paragraph | medium] for some x > O and we hope to adjust the parameter α so that the pair (vh,qh)

[p0145-b0019 | ordinary-paragraph | medium] verifies the inf-sup condition.

[p0145-b0020 | ordinary-paragraph | medium] Let us evaluate (qh, div vh). We have:

[p0145-b0021 | equation | low] (Gh, divvn) = (an, div n) + (an, div h) + α(an, div vn) + α(qh, div vn).

[p0145-b0022 | ordinary-paragraph | medium] Now,

[p0145-b0023 | equation | low] (h, div v,) = O  since v, vanishes on I,

[p0145-b0024 | equation | low] (ah, divvh) = Ilanll,2,

[p0145-b0025 | equation | low] (ah, div vn) = 1/anl16,2,

[p0145-b0026 | ordinary-paragraph | medium] by virtue of (1.58) and (1.59) respectively and

[p0145-b0027 | ordinary-paragraph | medium] /N

[p0145-b0028 | equation | low] Il ah llo.a ll an llo,s in view of (1.59).

[p0145-b0029 | equation | low] (qh, divvh) ≤

[p0145-b0030 | ordinary-paragraph | medium] β

[p0145-b0031 | ordinary-paragraph | medium] Hence, collecting these results we obtain:

[p0145-b0032 | ordinary-paragraph | low] lI an llo,ollah llo,2.

[p0145-b0033 | equation | low] (qn, divvn) ≥ 1lan ll,2 + αllanll2,2

[p0145-b0034 | ordinary-paragraph | low] R

[p0145-b0035 | ordinary-paragraph | medium] Then, the inequality:

[p0145-b0036 | ordinary-paragraph | low] 1

[p0145-b0037 | equation | low] llaullo,2llanllo, ≤ ellanll,α + ÷ Ilanl6,.2

[p0145-b0038 | ordinary-paragraph | medium] 48

[p0145-b0039 | ordinary-paragraph | medium] yields
