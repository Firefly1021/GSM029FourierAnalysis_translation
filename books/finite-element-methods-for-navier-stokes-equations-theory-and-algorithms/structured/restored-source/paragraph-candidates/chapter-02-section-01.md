# Paragraph candidates: chapter-02-section-01

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-02-section-01-pc00001 | ordinary-paragraph | high | PDF 126

Problem in the Primitive Variables

## chapter-02-section-01-pc00002 | section | high | PDF 126

§ 1. General Approximation

## chapter-02-section-01-pc00003 | ordinary-paragraph | high | PDF 126

The abstract problem discussed in Chapter I, § 4 lends itself readily to a straightforward approximation that converges under reasonable assumptions with an error proportional to the approximation error of the spaces involved. When applied to the Stokes problem, this approach yields a conforming approximation of the velocity and pressure, although the approximate velocity field is (in general) not exactly divergence-free. The wide range of finite element methods developped in the remainder of the chapter are all founded on the material of this paragraph. Non-conforming methods can also be put into this framework (cf. Zine [85]) but for the sake of conciseness we have skipped them entirely.

## chapter-02-section-01-pc00004 | subsection | high | PDF 126

1.1. An Abstract Approximation Result

## chapter-02-section-01-pc00005 | ordinary-paragraph | high | PDF 126

This section is devoted to the approximation of the abstract variational problem analyzed in §4 of Chapter I. We keep here the same notation and we put the problem in exactly the same situation. Recall that our Problem (Q) reads: Given | in X’ and x in M’, find a pair (u, A) in X x M such that (1.1) a(u,v) + b(v,A)=<lLv> Vuoex, (1.2) buuw=<xyu> VueMm. Here, X and M are two real Hilbert spaces and a(.,.) and b(.,.) are two continuous bilinear forms defined respectively on X x X and X x M. With the form b(., .) we associate the linear operators B and B’ defined by:

## chapter-02-section-01-pc00006 | equation | low | PDF 126

[[FORMULA:f-p0126-01861]]

## chapter-02-section-01-pc00007 | ordinary-paragraph | high | PDF 126

and we set

## chapter-02-section-01-pc00008 | equation | low | PDF 126

[[FORMULA:f-p0126-01862]]

## chapter-02-section-01-pc00009 | equation | low | PDF 126

[[FORMULA:f-p0126-01863]]

## chapter-02-section-01-pc00010 | ordinary-paragraph | low | PDF 127

Given I in X' and x in M', find u in V(x) such that: 'AaA

## chapter-02-section-01-pc00011 | equation | low | PDF 127

[[FORMULA:f-p0127-01864]]

## chapter-02-section-01-pc00012 | equation | low | PDF 127

[[FORMULA:f-p0127-01865]]

## chapter-02-section-01-pc00013 | ordinary-paragraph | low | PDF 127

We retain the two hypotheses which guarantee that Problems (Q) and (P) are equivalent and have a unique solution (cf. Theorem I.4.1 and its Corollary): there exists a constant α > O such that :AaA

## chapter-02-section-01-pc00014 | equation | low | PDF 127

[[FORMULA:f-p0127-01867]]

## chapter-02-section-01-pc00015 | equation | low | PDF 127

[[FORMULA:f-p0127-01868]]

## chapter-02-section-01-pc00016 | ordinary-paragraph | medium | PDF 127

there exists a constant β > 0 such that b(v, μ)

## chapter-02-section-01-pc00017 | equation | low | PDF 127

[[FORMULA:f-p0127-01870]]

## chapter-02-section-01-pc00018 | equation | low | PDF 127

[[FORMULA:f-p0127-01871]]

## chapter-02-section-01-pc00019 | equation | low | PDF 127

[[FORMULA:f-p0127-01872]]

## chapter-02-section-01-pc00020 | ordinary-paragraph | low | PDF 127

peM vex Iullxlμll m Let h denote a discretization parameter tending to zero and, for each h, let X, and M, be two finite-dimensional spaces such that: M, c M. Xh c X, Let X', and M' denote their dual spaces with the dual norms:

## chapter-02-section-01-pc00021 | equation | low | PDF 127

[[FORMULA:f-p0127-01873]]

## chapter-02-section-01-pc00022 | equation | low | PDF 127

[[FORMULA:f-p0127-01874]]

## chapter-02-section-01-pc00023 | equation | low | PDF 127

[[FORMULA:f-p0127-01875]]

## chapter-02-section-01-pc00024 | equation | low | PDF 127

[[FORMULA:f-p0127-01876]]

## chapter-02-section-01-pc00025 | ordinary-paragraph | low | PDF 127

μheMnIμn M vnexnlunllx Clearly, Wxe m'.

## chapter-02-section-01-pc00026 | equation | low | PDF 127

[[FORMULA:f-p0127-01877]]

## chapter-02-section-01-pc00027 | equation | low | PDF 127

[[FORMULA:f-p0127-01878]]

## chapter-02-section-01-pc00028 | ordinary-paragraph | low | PDF 127

Like in the continuous case, we associate with a(., . ) and b(., .) the operators A,e (X; Xh), Bh∈ (X; M) and B,e (M; X) defined by: 'XnA VUhE Xh,

## chapter-02-section-01-pc00029 | equation | low | PDF 127

[[FORMULA:f-p0127-01879]]

## chapter-02-section-01-pc00030 | ordinary-paragraph | low | PDF 127

'XaA

## chapter-02-section-01-pc00031 | equation | low | PDF 127

[[FORMULA:f-p0127-01880]]

## chapter-02-section-01-pc00032 | ordinary-paragraph | low | PDF 127

VunE Mh. Aue M. Vun∈ Xh.

## chapter-02-section-01-pc00033 | equation | low | PDF 127

[[FORMULA:f-p0127-01881]]

## chapter-02-section-01-pc00034 | ordinary-paragraph | low | PDF 127

Strictly speaking, B', is not the dual operator of B, but if B, is restricted to X, and B' to M, then B, and B' are indeed dual operators. In addition, we obviously have: XaA

## chapter-02-section-01-pc00035 | equation | low | PDF 127

[[FORMULA:f-p0127-01882]]

## chapter-02-section-01-pc00036 | ordinary-paragraph | medium | PDF 127

with similar inequalities for Il A,ullx, and | B'μllxk. For each xe M', we define the finite-dimensional analogue of V(x):

## chapter-02-section-01-pc00037 | equation | low | PDF 127

[[FORMULA:f-p0127-01883]]

## chapter-02-section-01-pc00038 | ordinary-paragraph | medium | PDF 127

and we set

## chapter-02-section-01-pc00039 | equation | low | PDF 127

[[FORMULA:f-p0127-01884]]

## chapter-02-section-01-pc00040 | ordinary-paragraph | medium | PDF 127

i.e.

## chapter-02-section-01-pc00041 | ordinary-paragraph | low | PDF 128

so ()  ()  4    e  m 3 proper subspace of M. Now we approximate Problem (Q) by Problem (Qh): Find a pair (un, 2n) in X, x M, satisfying: x#aA

## chapter-02-section-01-pc00042 | equation | low | PDF 128

[[FORMULA:f-p0128-01885]]

## chapter-02-section-01-pc00043 | equation | low | PDF 128

[[FORMULA:f-p0128-01886]]

## chapter-02-section-01-pc00044 | equation | low | PDF 128

[[FORMULA:f-p0128-01887]]

## chapter-02-section-01-pc00045 | equation | low | PDF 128

[[FORMULA:f-p0128-01888]]

## chapter-02-section-01-pc00046 | ordinary-paragraph | low | PDF 128

and we associate with (Qh) the following Problem (Ph): Find u,e Vh(x) such that: ""aA

## chapter-02-section-01-pc00047 | equation | low | PDF 128

[[FORMULA:f-p0128-01889]]

## chapter-02-section-01-pc00048 | equation | low | PDF 128

[[FORMULA:f-p0128-01890]]

## chapter-02-section-01-pc00049 | ordinary-paragraph | medium | PDF 128

As V,  V, Problem (P,) may be viewed as an external approximation of Problem (P). Here again, the first component u, of any solution (u,, A,) of Problem (Qh) is also a solution of Problem (Ph). The converse is proved as part of the next

## chapter-02-section-01-pc00050 | theorem | medium | PDF 128

theorem.

## chapter-02-section-01-pc00051 | theorem | medium | PDF 128

Theorem 1.1. 1°) Assume that the following conditions hold:

## chapter-02-section-01-pc00052 | ordinary-paragraph | medium | PDF 128

(i) Vh(x) is not empty;

## chapter-02-section-01-pc00053 | equation | low | PDF 128

[[FORMULA:f-p0128-01891]]

## chapter-02-section-01-pc00054 | equation | low | PDF 128

[[FORMULA:f-p0128-01892]]

## chapter-02-section-01-pc00055 | equation | low | PDF 128

[[FORMULA:f-p0128-01893]]

## chapter-02-section-01-pc00056 | ordinary-paragraph | low | PDF 128

""aA Then Problem (Pn) has a unique solution u, E Vh(x) and there exists a constant C, depending only upon α*, Ila! and I/bll such that the "error bound" holds:

## chapter-02-section-01-pc00057 | equation | low | PDF 128

[[FORMULA:f-p0128-01894]]

## chapter-02-section-01-pc00058 | equation | low | PDF 128

[[FORMULA:f-p0128-01895]]

## chapter-02-section-01-pc00059 | equation | low | PDF 128

[[FORMULA:f-p0128-01896]]

## chapter-02-section-01-pc00060 | ordinary-paragraph | low | PDF 128

(Un∈ Vn(x) μhEMn 2°) Assume that hypothesis (ii) holds and, in addition, that:

## chapter-02-section-01-pc00061 | equation | low | PDF 128

[[FORMULA:f-p0128-01897]]

## chapter-02-section-01-pc00062 | ordinary-paragraph | medium | PDF 128

b(Un μh)

## chapter-02-section-01-pc00063 | equation | low | PDF 128

[[FORMULA:f-p0128-01898]]

## chapter-02-section-01-pc00064 | equation | low | PDF 128

[[FORMULA:f-p0128-01899]]

## chapter-02-section-01-pc00065 | equation | low | PDF 128

[[FORMULA:f-p0128-01900]]

## chapter-02-section-01-pc00066 | ordinary-paragraph | low | PDF 128

Vuhe Mh. lun ll x UhEXn Then Vh(x) ≠ Φ and there exists a unique Λ, in M, such that (un, Λn) is the only solution of Problem (Qn). Furthermore, there exists a constant C2 depending only upon α*, β*, Ilall and llbll such that: inf Ilu-vnllx+ inf I-μnlm (1.13) u -unlx + I/ -Anlim ≤ C2 UnEXh μhEMn od s os sm u ()' ui n e ssooo am da sou si ()' sa (1 oo Find z, in Vh such that

## chapter-02-section-01-pc00067 | equation | low | PDF 128

[[FORMULA:f-p0128-01903]]

## chapter-02-section-01-pc00068 | equation | low | PDF 129

[[FORMULA:f-p0129-01904]]

## chapter-02-section-01-pc00069 | ordinary-paragraph | medium | PDF 129

is the only solution of Problem (P,). Now let w, be an arbitrary element of V(x); then v, = u, - w, e V, and

## chapter-02-section-01-pc00070 | equation | low | PDF 129

[[FORMULA:f-p0129-01906]]

## chapter-02-section-01-pc00071 | equation | low | PDF 129

[[FORMULA:f-p0129-01907]]

## chapter-02-section-01-pc00072 | ordinary-paragraph | medium | PDF 129

Since v,e X,, we can take v = v, in (1.1) and substitute in (1.14). This yields:

## chapter-02-section-01-pc00073 | equation | low | PDF 129

[[FORMULA:f-p0129-01909]]

## chapter-02-section-01-pc00074 | ordinary-paragraph | medium | PDF 129

Moreover, since v, e Vh, we have b(vn, μn) = O u, E M,. Hence

## chapter-02-section-01-pc00075 | equation | low | PDF 129

[[FORMULA:f-p0129-01911]]

## chapter-02-section-01-pc00076 | ordinary-paragraph | low | PDF 129

)AunEMh.

## chapter-02-section-01-pc00077 | equation | low | PDF 129

[[FORMULA:f-p0129-01912]]

## chapter-02-section-01-pc00078 | ordinary-paragraph | medium | PDF 129

The V,-ellipticity of a and the continuity of a and b yield:

## chapter-02-section-01-pc00079 | equation | low | PDF 129

[[FORMULA:f-p0129-01913]]

## chapter-02-section-01-pc00080 | ordinary-paragraph | low | PDF 129

Therefore 1—μnllM Ilu - Wn llx + 

## chapter-02-section-01-pc00081 | equation | low | PDF 129

[[FORMULA:f-p0129-01914]]

## chapter-02-section-01-pc00082 | ordinary-paragraph | medium | PDF 129

*

## chapter-02-section-01-pc00083 | equation | low | PDF 129

[[FORMULA:f-p0129-01915]]

## chapter-02-section-01-pc00084 | ordinary-paragraph | low | PDF 129

Vuh e Mh. llallbl This yields (1.11) with C, = max * 2°) Let us apply Lemma I.4.1 to the particular case of X, and M,. Hypothesis (ii) implies that B, is an isomorphism from V, (taken in X,) onto M'. Therefore V(x) is not empty and according to n? 1 Problem (Ph) has a unique solution un. Furthermore, it follows from Corollary I.4.1 that there exists a unique , in M, such that the pair (u,, h) is the only solution of Problem (Qh). To derive the error bound (1.13) we shall first prove that |/bll

## chapter-02-section-01-pc00085 | equation | low | PDF 129

[[FORMULA:f-p0129-01918]]

## chapter-02-section-01-pc00086 | equation | low | PDF 129

[[FORMULA:f-p0129-01919]]

## chapter-02-section-01-pc00087 | equation | low | PDF 129

[[FORMULA:f-p0129-01920]]

## chapter-02-section-01-pc00088 | ordinary-paragraph | low | PDF 129

β* Un∈Xh Wh∈ Vn(x) Let v, be an arbitrary element of X,; like above, there exists a unique z, in V such that

## chapter-02-section-01-pc00089 | equation | low | PDF 129

[[FORMULA:f-p0129-01921]]

## chapter-02-section-01-pc00090 | ordinary-paragraph | medium | PDF 129

and

## chapter-02-section-01-pc00091 | equation | low | PDF 129

[[FORMULA:f-p0129-01922]]

## chapter-02-section-01-pc00092 | ordinary-paragraph | low | PDF 129,130

B* Thus, if we set wh, = Zh + vn, then Iu - Un llx.

## chapter-02-section-01-pc00093 | equation | low | PDF 130

[[FORMULA:f-p0130-01924]]

## chapter-02-section-01-pc00094 | ordinary-paragraph | low | PDF 130

R* As v, is arbitrary, this implies (1.16). It remains to evaluate IlX - A,llm. From (1.1) and (1.7) we derive that: Vuh E Mh. Vuhe Xh.

## chapter-02-section-01-pc00095 | equation | low | PDF 130

[[FORMULA:f-p0130-01927]]

## chapter-02-section-01-pc00096 | ordinary-paragraph | low | PDF 130

Therefore hypothesis (1.12) yields: 1 1 {a(u——unUn)+b(un,—μn)}

## chapter-02-section-01-pc00097 | equation | low | PDF 130

[[FORMULA:f-p0130-01929]]

## chapter-02-section-01-pc00098 | equation | low | PDF 130

[[FORMULA:f-p0130-01930]]

## chapter-02-section-01-pc00099 | ordinary-paragraph | low | PDF 130

β* vnexn llun1lx 1 Illall lu - unllx + IIbl/ lI - μhll m}. B* Hence

## chapter-02-section-01-pc00100 | equation | low | PDF 130

[[FORMULA:f-p0130-01931]]

## chapter-02-section-01-pc00101 | ordinary-paragraph | low | PDF 130

(1.17)  -lm ≤ β* μnE Mn Then the bound (1.13) follows immediately from (1.11), (1.16) and (1.17).

## chapter-02-section-01-pc00102 | remark | medium | PDF 130

Remark 1.1. The bound (1.11) can be slightly improved without making use of

## chapter-02-section-01-pc00103 | ordinary-paragraph | low | PDF 130

the inf-sup condition (1.12). Indeed, by applying (1.10) to (1.15) we obtain: b(un,A——μh)

## chapter-02-section-01-pc00104 | equation | low | PDF 130

[[FORMULA:f-p0130-01936]]

## chapter-02-section-01-pc00105 | equation | low | PDF 130

[[FORMULA:f-p0130-01937]]

## chapter-02-section-01-pc00106 | ordinary-paragraph | low | PDF 130

II un ll x UnEVn Therefore b(vh, -μh) |a|l 1

## chapter-02-section-01-pc00107 | equation | low | PDF 130

[[FORMULA:f-p0130-01938]]

## chapter-02-section-01-pc00108 | equation | low | PDF 130

[[FORMULA:f-p0130-01939]]

## chapter-02-section-01-pc00109 | equation | low | PDF 130

[[FORMULA:f-p0130-01940]]

## chapter-02-section-01-pc00110 | ordinary-paragraph | low | PDF 130

x* llunllx Wn∈ Vn(x) un∈Mh Un∈Vn

## chapter-02-section-01-pc00111 | equation | low | PDF 130

[[FORMULA:f-p0130-01941]]

## chapter-02-section-01-pc00112 | ordinary-paragraph | medium | PDF 130

Note that the expression b(vn-μn)

## chapter-02-section-01-pc00113 | equation | low | PDF 130

[[FORMULA:f-p0130-01942]]

## chapter-02-section-01-pc00114 | ordinary-paragraph | low | PDF 130

lun ll x UnEMh the Vh takes into account the fact that Vh  V: it vanishes when V, c V.

## chapter-02-section-01-pc00115 | remark | medium | PDF 130

Remark 1.2. If besides Hypotheses (1.10) and (1.12) we assume that the bilinear

## chapter-02-section-01-pc00116 | ordinary-paragraph | medium | PDF 130

form a(., .) is symmetric and semi-positive definite on X,, then we can relate Problems (Ph) and (Qh) to optimization problems. As in the continuous case, and with the same notations, it can be shown that the solution u, of (Ph) is characterized by:

## chapter-02-section-01-pc00117 | equation | low | PDF 130

[[FORMULA:f-p0130-01944]]

## chapter-02-section-01-pc00118 | equation | low | PDF 130

[[FORMULA:f-p0130-01945]]

## chapter-02-section-01-pc00119 | equation | low | PDF 131

[[FORMULA:f-p0131-01946]]

## chapter-02-section-01-pc00120 | ordinary-paragraph | high | PDF 131

vnE Xp Ine Mp an€ Mp vn€ Xn

## chapter-02-section-01-pc00121 | remark | high | PDF 131

Remark 1.3. From the argument of Theorem 1.1, we readily derive that if Hy-

## chapter-02-section-01-pc00122 | ordinary-paragraph | high | PDF 131

potheses (1.10) and (1.12) hold then the solution (u,, 4,,) is bounded as follows:

## chapter-02-section-01-pc00123 | ordinary-paragraph | high | PDF 131

1 1

## chapter-02-section-01-pc00124 | equation | low | PDF 131

[[FORMULA:f-p0131-01948]]

## chapter-02-section-01-pc00125 | ordinary-paragraph | high | PDF 131

on An lla Se UME: + Wall lea ll}. Br Observe that the bilinear form a(., .) is V,-elliptic as soon as a(v,, v,) > 0 for all v, # 0. Similarly, the bilinear form b(., .) satisfies the discrete inf-sup condition (1.12) provided Ker(B;,) M, = {0}. But of course in either case the constants a* and f* will generally depend upon h. Now, in order to derive optimal error bounds in Theorem 1.1, it is clear that both constants «* and f* must be independent of h. And since usually V, ¢ V, the V-ellipticity of a(., .) does not necessarily carry over to V,,. As a consequence, hypothesis (1.10) must be checked in each particular case; but for the applications we have in mind, this is not a major obstacle. On the other hand, the discrete inf-sup condition (1.12) which acts as a uniform compatibility condition between X, and M, is much more delicate to check. The following lemma due to Fortin [28] establishes a useful criterion for (1.12).

## chapter-02-section-01-pc00126 | lemma | high | PDF 131

Lemma 1.1. The inf-sup condition (1.12) holds with a constant f* > 0 independent

## chapter-02-section-01-pc00127 | ordinary-paragraph | high | PDF 131

of hif and only if there exists an operator I,€ L(X; X,,) satisfying: (1.19) b(v — 11,0; 4,)=90 Vey,eM, Voex and (1.20) |Z vlly <Cllvlly Voex with a constant C > 0 independent of h.

## chapter-02-section-01-pc00128 | proof | high | PDF 131

Proof. Assume that such an operator II, exists; then we have for all 4,€ M,:

## chapter-02-section-01-pc00129 | ordinary-paragraph | high | PDF 131

b(Up, Un) eS bUT,v, Ln) a. b(v, Ln) pee WO ee Whol oes Tv ll owing to (1.19). Thus (1.20) and (1.5) imply that

## chapter-02-section-01-pc00130 | equation | low | PDF 131

[[FORMULA:f-p0131-01960]]

## chapter-02-section-01-pc00131 | equation | low | PDF 131

[[FORMULA:f-p0131-01961]]

## chapter-02-section-01-pc00132 | ordinary-paragraph | high | PDF 131

v,pE Xn I Vp llx Cex |v llx C and (1.12) follows with B* = B/C.

## chapter-02-section-01-pc00133 | equation | low | PDF 132

[[FORMULA:f-p0132-01963]]

## chapter-02-section-01-pc00134 | ordinary-paragraph | high | PDF 132

and Peer alll

## chapter-02-section-01-pc00135 | equation | low | PDF 132

[[FORMULA:f-p0132-01964]]

## chapter-02-section-01-pc00136 | ordinary-paragraph | high | PDF 132

Clearly [7,¢ £(X; X,) and satisfies (1.20) with C = ||b||/B*. O In practice, the construction of JJ, is by no means easy. The reader will find in Section 1.4 how to establish the inf-sup condition in a number of cases without constructing /7, explicitly.

## chapter-02-section-01-pc00137 | remark | high | PDF 132

Remark 1.4. Another useful way of writing the inf-sup condition (1.12) is:

## chapter-02-section-01-pc00138 | ordinary-paragraph | high | PDF 132

for each py, € M, there exists a v, in X,, (unique in V,") such that: 1

## chapter-02-section-01-pc00139 | equation | low | PDF 132

[[FORMULA:f-p0132-01968]]

## chapter-02-section-01-pc00140 | ordinary-paragraph | high | PDF 132

This result, which is also valid in the continuous case, uses explicitly the fact that \|. lly is a Hilbert norm.

## chapter-02-section-01-pc00141 | remark | high | PDF 132

Remark 1.5. In the particular case where the bilinear form a(., .) coincides with

## chapter-02-section-01-pc00142 | ordinary-paragraph | high | PDF 132

the scalar product ((., .)), associated with the Hilbert norm ||. || ,, formula (1.17) simplifies to: ; i , (1.17') IA = dale <5} inf ||u — wally + (B* + |[b||) inf |4— salle Wn € Vn), Hye My, Indeed, we have:

## chapter-02-section-01-pc00143 | equation | low | PDF 132

[[FORMULA:f-p0132-01971]]

## chapter-02-section-01-pc00144 | ordinary-paragraph | high | PDF 132

Wo,€ Vis VwnE Vi), Vine Mi, and the v, (in V,;+) of Remark 1.4 gives (1.17).

## chapter-02-section-01-pc00145 | theorem | high | PDF 132

Theorem 1.1 readily yields the following general convergence results.

## chapter-02-section-01-pc00146 | corollary | high | PDF 132

Corollary 1.1. Assume that the following hypotheses hold:

## chapter-02-section-01-pc00147 | ordinary-paragraph | high | PDF 132

1°) the form a(., .) satisfies (1.10) with a constant «* > 0 independent of h; 2°) there exist a dense subvariety V(x) of V(x), a dense subspace M of M and two mappings r,: V (x) > V,(x) and p,: M@ > M,, with:

## chapter-02-section-01-pc00148 | equation | low | PDF 132

[[FORMULA:f-p0132-01975]]

## chapter-02-section-01-pc00149 | equation | low | PDF 132

[[FORMULA:f-p0132-01976]]

## chapter-02-section-01-pc00150 | equation | low | PDF 132

[[FORMULA:f-p0132-01977]]

## chapter-02-section-01-pc00151 | equation | low | PDF 133

[[FORMULA:f-p0133-01978]]

## chapter-02-section-01-pc00152 | ordinary-paragraph | medium | PDF 133

h→0

## chapter-02-section-01-pc00153 | corollary | medium | PDF 133

Corollary 1.2. We retain the above hypotheses on a( ., . ) and M and we assume that

## chapter-02-section-01-pc00154 | ordinary-paragraph | medium | PDF 133

b(., . ) satisfies a uniform inf-sup condition (1.12). If there exists a dense subspace X of X and a mapping rn: X → X, satisfying:

## chapter-02-section-01-pc00155 | equation | low | PDF 133

[[FORMULA:f-p0133-01980]]

## chapter-02-section-01-pc00156 | ordinary-paragraph | low | PDF 133

aA h→0 then

## chapter-02-section-01-pc00157 | equation | low | PDF 133

[[FORMULA:f-p0133-01981]]

## chapter-02-section-01-pc00158 | ordinary-paragraph | medium | PDF 133

h→0 Now, let us extend the classical duality argument of Aubin [3] and Nitsche [61] to the case of Problems (P) and (Ph). For this, we introduce a Hilbert space H with scalar product (., .) and associated norm I.I such that X c H with continuous imbedding and X is dense in H. We identify H with its dual space H' for the scalar product (., -). Therefore, H can be identified with a subspace of X': H e X' with continuous and dense imbedding. In order to evaluate |u -- u,l, we introduce for each g in H the unique solution pair (Φg, ,) of the dual problem:

## chapter-02-section-01-pc00159 | equation | low | PDF 133

[[FORMULA:f-p0133-01982]]

## chapter-02-section-01-pc00160 | equation | low | PDF 133

[[FORMULA:f-p0133-01983]]

## chapter-02-section-01-pc00161 | equation | low | PDF 133

[[FORMULA:f-p0133-01984]]

## chapter-02-section-01-pc00162 | theorem | medium | PDF 133

Theorem 1.2. Assume that Problem (P,) has a unique solution u,. Then there exists

## chapter-02-section-01-pc00163 | ordinary-paragraph | medium | PDF 133

a constant C, depending only upon Ilal and /bll, such that:

## chapter-02-section-01-pc00164 | equation | low | PDF 133

[[FORMULA:f-p0133-01985]]

## chapter-02-section-01-pc00165 | ordinary-paragraph | low | PDF 133

μne Mn

## chapter-02-section-01-pc00166 | equation | low | PDF 133

[[FORMULA:f-p0133-01986]]

## chapter-02-section-01-pc00167 | ordinary-paragraph | low | PDF 133

inf IPg -- Pnllx + inf Ilg -- hlm

## chapter-02-section-01-pc00168 | equation | low | PDF 133

[[FORMULA:f-p0133-01988]]

## chapter-02-section-01-pc00169 | ordinary-paragraph | low | PDF 133

geH gl ShEMn (n∈ Vn

## chapter-02-section-01-pc00170 | proof | medium | PDF 133

Proof. On the one hand, we have:

## chapter-02-section-01-pc00171 | ordinary-paragraph | medium | PDF 133

(g,u -— un)

## chapter-02-section-01-pc00172 | equation | low | PDF 133

[[FORMULA:f-p0133-01989]]

## chapter-02-section-01-pc00173 | ordinary-paragraph | low | PDF 133

[gl gEH On the other hand by choosing v = u - u, in (1.21), we get

## chapter-02-section-01-pc00174 | equation | low | PDF 133

[[FORMULA:f-p0133-01991]]

## chapter-02-section-01-pc00175 | equation | low | PDF 133

[[FORMULA:f-p0133-01992]]

## chapter-02-section-01-pc00176 | ordinary-paragraph | low | PDF 133,134

Then taking into account (1.1) and (1.6) we find: Wuhe Mh

## chapter-02-section-01-pc00177 | equation | low | PDF 134

[[FORMULA:f-p0134-01994]]

## chapter-02-section-01-pc00178 | ordinary-paragraph | low | PDF 134

and as ue V(x) and u, e V(x), we also have: Ashe Mh.

## chapter-02-section-01-pc00179 | equation | low | PDF 134

[[FORMULA:f-p0134-01995]]

## chapter-02-section-01-pc00180 | ordinary-paragraph | low | PDF 134

When substituted into (1.23), these three equalities yield: ("un-—n)q + (un -u )q + (-- un-n) =(n-nb) Vone Vh, Auh, She Mh. Hence I(g,u - un)l ≤C{llu --unllx + I/A - μnllm}{llΦg - Φnllx + Ilg - Shllm} "A uh, Sh∈ Mh, where C = max( lla ll, Il blIl). 口

## chapter-02-section-01-pc00181 | remark | medium | PDF 134

Remark 1.6. When Problem (Qh) has a solution (u,, A,) a straightforward modi-

## chapter-02-section-01-pc00182 | ordinary-paragraph | medium | PDF 134

fication of the above argument shows that:

## chapter-02-section-01-pc00183 | equation | low | PDF 134

[[FORMULA:f-p0134-02000]]

## chapter-02-section-01-pc00184 | ordinary-paragraph | medium | PDF 134

1

## chapter-02-section-01-pc00185 | equation | low | PDF 134

[[FORMULA:f-p0134-02001]]

## chapter-02-section-01-pc00186 | equation | low | PDF 134

[[FORMULA:f-p0134-02002]]

## chapter-02-section-01-pc00187 | ordinary-paragraph | low | PDF 134

geH|gl ShEMn (on∈Xn with the constant C of (1.22).

## chapter-02-section-01-pc00188 | subsection | medium | PDF 134

1.2. Decoupling the Computation of u, and ,

## chapter-02-section-01-pc00189 | ordinary-paragraph | medium | PDF 134

In this short section, we propose to apply the technique of Sections I.4.3 and 1.4.4 to dissociate the computation of , from that of u,. These methods are often used in practice. Let us consider first the regularization procedure of Section I.4.3. Recall that we require a continuous, bilinear form c( ., .) on M, x M, which is supposed to be M,-elliptic, i.e. there exists a constant y* > O such that:

## chapter-02-section-01-pc00190 | equation | low | PDF 134

[[FORMULA:f-p0134-02005]]

## chapter-02-section-01-pc00191 | equation | low | PDF 134

[[FORMULA:f-p0134-02006]]

## chapter-02-section-01-pc00192 | ordinary-paragraph | medium | PDF 134

With the form c( ., .) we associate as usual the operator C,e &(M,; M') by:

## chapter-02-section-01-pc00193 | equation | low | PDF 134

[[FORMULA:f-p0134-02007]]

## chapter-02-section-01-pc00194 | ordinary-paragraph | low | PDF 134

Wuh, VhE Mh. Like in the continuous case, for each & > 0 we introduce the Problem (Qh): Find a pair (u, Ai)e X, x M, such that

## chapter-02-section-01-pc00195 | equation | low | PDF 134

[[FORMULA:f-p0134-02009]]

## chapter-02-section-01-pc00196 | equation | low | PDF 134

[[FORMULA:f-p0134-02010]]

## chapter-02-section-01-pc00197 | equation | low | PDF 134

[[FORMULA:f-p0134-02011]]

## chapter-02-section-01-pc00198 | equation | low | PDF 134

[[FORMULA:f-p0134-02012]]

## chapter-02-section-01-pc00199 | ordinary-paragraph | low | PDF 134,135

Wune Mh. eliminated from the above equations. Thus Problem (Q) is equivalent to the following Problem (Ph): Find ue X, satisfying: 1 "x="aA (1.26)a(u,un) +<Ch 1Bnu,Bnun>=<l,un>+<Chx,Bnun> 8 where C-1 e S(M': M,) denotes the inverse of C, Clearly, the situation here is exactly that of Section I.4.3, wiih the operators B and C replaced by B, and C,. Hence the statement of Theorem 1.4.3 is valid for Problems (Pi) and (Q):

## chapter-02-section-01-pc00200 | theorem | medium | PDF 135

Theorem 1.3. In addition to (1.12) and (1.24), assume that there exists a constant

## chapter-02-section-01-pc00201 | ordinary-paragraph | low | PDF 135

α* > O such that: "x"aA

## chapter-02-section-01-pc00202 | equation | low | PDF 135

[[FORMULA:f-p0135-02017]]

## chapter-02-section-01-pc00203 | equation | low | PDF 135

[[FORMULA:f-p0135-02018]]

## chapter-02-section-01-pc00204 | ordinary-paragraph | medium | PDF 135

Then Problems (Qh) and (Qh) for & ≤ 1 have both a unique solution (u,, Λn) and (u, X) in X, x M,. Moreover, for all ε ≤ &o small enough we have the following error bound:

## chapter-02-section-01-pc00205 | equation | low | PDF 135

[[FORMULA:f-p0135-02021]]

## chapter-02-section-01-pc00206 | equation | low | PDF 135

[[FORMULA:f-p0135-02022]]

## chapter-02-section-01-pc00207 | ordinary-paragraph | low | PDF 135

where the constant K* depends only upon α*, β*, Ilall, IIbll and I/cll. Likewise, we can refine (1.28) and obtain an asymptotic expansion for (u;, X;) of the problems: "x"aA

## chapter-02-section-01-pc00208 | equation | low | PDF 135

[[FORMULA:f-p0135-02024]]

## chapter-02-section-01-pc00209 | equation | low | PDF 135

[[FORMULA:f-p0135-02025]]

## chapter-02-section-01-pc00210 | equation | low | PDF 135

[[FORMULA:f-p0135-02026]]

## chapter-02-section-01-pc00211 | ordinary-paragraph | low | PDF 135

Vu,E Mh, starting with 2 = Λ,. We have the analogue of Theorem I.4.4:

## chapter-02-section-01-pc00212 | theorem | medium | PDF 135

Theorem 1.4. Under the hypotheses of Theorem 1.3, we have for all integers N ≥ 1

## chapter-02-section-01-pc00213 | ordinary-paragraph | low | PDF 135

and for & ≤ &o small enough: N N —nen

## chapter-02-section-01-pc00214 | equation | low | PDF 135

[[FORMULA:f-p0135-02030]]

## chapter-02-section-01-pc00215 | ordinary-paragraph | low | PDF 135

uh —— uh -—

## chapter-02-section-01-pc00216 | equation | low | PDF 135

[[FORMULA:f-p0135-02031]]

## chapter-02-section-01-pc00217 | equation | low | PDF 135

[[FORMULA:f-p0135-02032]]

## chapter-02-section-01-pc00218 | ordinary-paragraph | medium | PDF 135

M x

## chapter-02-section-01-pc00219 | equation | low | PDF 135

[[FORMULA:f-p0135-02033]]

## chapter-02-section-01-pc00220 | equation | low | PDF 135

[[FORMULA:f-p0135-02034]]

## chapter-02-section-01-pc00221 | ordinary-paragraph | medium | PDF 135,136

where the constant K* depends only upon N, α*, β*, Ilall, Ilbll and Ilcll. Now, we turn to the gradient algorithms of Section I.4.4. With the above notations, we set for each real parameter r ≥ 0: there exists a constant «* > 0 such that (1.32) al (UpV,p ,) > &* |g VOne Xn. Then the simple gradient algorithm with optimal parameter has the following discrete version: 1°) Given an initial guess 2?¢M,, compute the solution uleX , of the problem

## chapter-02-section-01-pc00222 | equation | low | PDF 136

[[FORMULA:f-p0136-02038]]

## chapter-02-section-01-pc00223 | ordinary-paragraph | high | PDF 136

2°) For m > 0, knowing (uj", Aj")e X, x M,, determine (z;”,g;")X€; , < Mh, py'e R and the pair (u7"*!, Ay"*")eX , x M,, by:

## chapter-02-section-01-pc00224 | equation | low | PDF 136

[[FORMULA:f-p0136-02040]]

## chapter-02-section-01-pc00225 | ordinary-paragraph | high | PDF 136

a

## chapter-02-section-01-pc00226 | equation | low | PDF 136

[[FORMULA:f-p0136-02041]]

## chapter-02-section-01-pc00227 | equation | low | PDF 136

[[FORMULA:f-p0136-02042]]

## chapter-02-section-01-pc00228 | ordinary-paragraph | high | PDF 136

; 1.33 b fh a eA

## chapter-02-section-01-pc00229 | equation | low | PDF 136

[[FORMULA:f-p0136-02043]]

## chapter-02-section-01-pc00230 | ordinary-paragraph | high | PDF 136

(c) {

## chapter-02-section-01-pc00231 | equation | low | PDF 136

[[FORMULA:f-p0136-02044]]

## chapter-02-section-01-pc00232 | ordinary-paragraph | high | PDF 136

Needless to say, the above scheme is a gradient algorithm only when the bilinear forms a(.,.) and c(.,.) are symmetric. Then the following result is a direct consequence of Corollary 1.4.4.

## chapter-02-section-01-pc00233 | theorem | high | PDF 136

Theorem 1.5. Suppose the bilinear forms al(., .), b(., .) and c(., .) satisfy respec-

## chapter-02-section-01-pc00234 | ordinary-paragraph | high | PDF 136

tively (1.32), (1.12) and (1.24) and assume that a(., .) and c(., .) are symmetric. Then the simple gradient algorithm (1.33) is convergent for every choice of the starting value A? € M;,;:

## chapter-02-section-01-pc00235 | equation | low | PDF 136

[[FORMULA:f-p0136-02047]]

## chapter-02-section-01-pc00236 | ordinary-paragraph | high | PDF 136

m~ oo Like in Section 1.4.4, observe that the simple gradient algorithm can converge without optimal parameters. In that case, the bilinear form a(.,.) need not be symmetric and we have the analogue of Theorem I.4.7:

## chapter-02-section-01-pc00237 | theorem | high | PDF 136

Theorem 1.6. We retain all hypotheses of Theorem 1.5 except the symmetry as-

## chapter-02-section-01-pc00238 | ordinary-paragraph | high | PDF 136

sumption on a(., .). Then the algorithm (1.33a) (1.33c) is convergenfto r every choice of the initial guess Ap € M,, and every sequence of numbers (p,") in the range:

## chapter-02-section-01-pc00239 | equation | low | PDF 136

[[FORMULA:f-p0136-02048]]

## chapter-02-section-01-pc00240 | ordinary-paragraph | low | PDF 136,137

where Chg aa (4; (Up, 0,)/ || Ban lis, is entirely similar to the scheme (1.4.70). Let us describe it for the sake of completeness: 1°) Starting from an initial guess A e M,, compute the solution u e X, of the problem: "x"aA

## chapter-02-section-01-pc00241 | equation | low | PDF 137

[[FORMULA:f-p0137-02049]]

## chapter-02-section-01-pc00242 | ordinary-paragraph | medium | PDF 137

2°) For m ≥ 0, knowing (um,Am)e Xh × M, compute gn, wm∈ Mh, zm∈Xh, p", onm e R and the pair (um+1, am+1)e X, × Mn, by:

## chapter-02-section-01-pc00243 | equation | low | PDF 137

[[FORMULA:f-p0137-02051]]

## chapter-02-section-01-pc00244 | ordinary-paragraph | low | PDF 137

Vune Mh, c(gm, 9m) c(gm-1 , 9m-1)

## chapter-02-section-01-pc00245 | equation | low | PDF 137

[[FORMULA:f-p0137-02052]]

## chapter-02-section-01-pc00246 | equation | low | PDF 137

[[FORMULA:f-p0137-02053]]

## chapter-02-section-01-pc00247 | equation | low | PDF 137

[[FORMULA:f-p0137-02054]]

## chapter-02-section-01-pc00248 | equation | low | PDF 137

[[FORMULA:f-p0137-02055]]

## chapter-02-section-01-pc00249 | ordinary-paragraph | low | PDF 137

c(gn", gm) Pn b(zm,9m")' m-prom,

## chapter-02-section-01-pc00250 | equation | low | PDF 137

[[FORMULA:f-p0137-02056]]

## chapter-02-section-01-pc00251 | equation | low | PDF 137

[[FORMULA:f-p0137-02057]]

## chapter-02-section-01-pc00252 | theorem | medium | PDF 137

Theorem 1.7. The conjugate-gradient algorithm converges with the hypotheses of

## chapter-02-section-01-pc00253 | theorem | medium | PDF 137

Theorem 1.5.

## chapter-02-section-01-pc00254 | subsection | medium | PDF 137

1.3. Application to the Homogeneous Stokes Problem

## chapter-02-section-01-pc00255 | ordinary-paragraph | medium | PDF 137

For the sake of simplicity, we focus our attention on homogeneous boundary conditions. Let Ω be a bounded, connected, open subset of R with a Lipschitzcontinuous boundary F and let f be a given function of H-1(Q). Recall that the homogeneous Stokes equations: Find (u, p) in H(Q) x L2(Q) such that

## chapter-02-section-01-pc00256 | equation | low | PDF 137

[[FORMULA:f-p0137-02058]]

## chapter-02-section-01-pc00257 | equation | low | PDF 137

[[FORMULA:f-p0137-02059]]

## chapter-02-section-01-pc00258 | ordinary-paragraph | medium | PDF 137

in Ω,

## chapter-02-section-01-pc00259 | equation | low | PDF 137

[[FORMULA:f-p0137-02060]]

## chapter-02-section-01-pc00260 | ordinary-paragraph | medium | PDF 137

has a unique solution. Moreover, setting either N

## chapter-02-section-01-pc00261 | equation | low | PDF 137

[[FORMULA:f-p0137-02061]]

## chapter-02-section-01-pc00262 | ordinary-paragraph | medium | PDF 137

(a) i,1

## chapter-02-section-01-pc00263 | equation | low | PDF 137

[[FORMULA:f-p0137-02062]]

## chapter-02-section-01-pc00264 | ordinary-paragraph | medium | PDF 137

）or

## chapter-02-section-01-pc00265 | equation | low | PDF 137

[[FORMULA:f-p0137-02063]]

## chapter-02-section-01-pc00266 | ordinary-paragraph | low | PDF 137,138

(b) we know that (1.35) is equivalent to the variational formulation: N()HAA

## chapter-02-section-01-pc00267 | equation | low | PDF 138

[[FORMULA:f-p0138-02065]]

## chapter-02-section-01-pc00268 | equation | low | PDF 138

[[FORMULA:f-p0138-02066]]

## chapter-02-section-01-pc00269 | equation | low | PDF 138

[[FORMULA:f-p0138-02067]]

## chapter-02-section-01-pc00270 | ordinary-paragraph | medium | PDF 138

With the following substitutions:

## chapter-02-section-01-pc00271 | equation | low | PDF 138

[[FORMULA:f-p0138-02068]]

## chapter-02-section-01-pc00272 | equation | low | PDF 138

[[FORMULA:f-p0138-02069]]

## chapter-02-section-01-pc00273 | equation | low | PDF 138

[[FORMULA:f-p0138-02070]]

## chapter-02-section-01-pc00274 | equation | low | PDF 138

[[FORMULA:f-p0138-02071]]

## chapter-02-section-01-pc00275 | equation | low | PDF 138

[[FORMULA:f-p0138-02072]]

## chapter-02-section-01-pc00276 | ordinary-paragraph | low | PDF 138

this is exactly the problem studied in Section I.5.1. Now, for each h let W, and Q, be two finite-dimensional spaces such that Wh c H'(Ω),  Qh c L²(Ω) and throughout this section we assume that Qh, contains the constant functions. We set:

## chapter-02-section-01-pc00277 | equation | low | PDF 138

[[FORMULA:f-p0138-02073]]

## chapter-02-section-01-pc00278 | equation | low | PDF 138

[[FORMULA:f-p0138-02074]]

## chapter-02-section-01-pc00279 | equation | low | PDF 138

[[FORMULA:f-p0138-02075]]

## chapter-02-section-01-pc00280 | equation | low | PDF 138

[[FORMULA:f-p0138-02076]]

## chapter-02-section-01-pc00281 | ordinary-paragraph | low | PDF 138

{ah∈ Qh; With these spaces, Problem (1.37) is approximated by: Find a pair (un, Ph)e X, x Mh such that: Wwhe Xh,

## chapter-02-section-01-pc00282 | equation | low | PDF 138

[[FORMULA:f-p0138-02078]]

## chapter-02-section-01-pc00283 | equation | low | PDF 138

[[FORMULA:f-p0138-02079]]

## chapter-02-section-01-pc00284 | equation | low | PDF 138

[[FORMULA:f-p0138-02080]]

## chapter-02-section-01-pc00285 | ordinary-paragraph | medium | PDF 138

As div u, e L?(Q), observe that the second equation in (1.39) is cquivalent to

## chapter-02-section-01-pc00286 | equation | low | PDF 138

[[FORMULA:f-p0138-02082]]

## chapter-02-section-01-pc00287 | ordinary-paragraph | medium | PDF 138

In view of this remark, the corresponding space V, is given by:

## chapter-02-section-01-pc00288 | equation | low | PDF 138

[[FORMULA:f-p0138-02083]]

## chapter-02-section-01-pc00289 | ordinary-paragraph | medium | PDF 138

Hence the Problem (P,) associated with (1.39) is: Find u, e V, satisfying

## chapter-02-section-01-pc00290 | equation | low | PDF 138

[[FORMULA:f-p0138-02085]]

## chapter-02-section-01-pc00291 | equation | low | PDF 138

[[FORMULA:f-p0138-02086]]

## chapter-02-section-01-pc00292 | equation | low | PDF 138

[[FORMULA:f-p0138-02087]]

## chapter-02-section-01-pc00293 | remark | medium | PDF 138

Remark 1.7. As mentioned in the preceding section, V, is generally not included

## chapter-02-section-01-pc00294 | ordinary-paragraph | medium | PDF 138

in V: {ve H(Ω); div v = O}; this will be the case in all the examples of this chapter. Thus the functions of V, are not divergence-free but satisfy only

## chapter-02-section-01-pc00295 | equation | low | PDF 138

[[FORMULA:f-p0138-02089]]

## chapter-02-section-01-pc00296 | ordinary-paragraph | medium | PDF 138,139

where p, is the orthogonal projection of L2(Ω) onto Qh. As a consequence, the equivalent formulations. In order to study Problem (1.40) we relate the continuous and discrete spaces by the following hypotheses: Hypothesis H1 (Approximation property of X,,). There exist an operator r,€ L(A? (Q)§; W,) ON L((H7(Q) N H4(Q))%; X,,) and an integer | such that: G4 ev Avro Cn7lView > VYeH™ (OQ), lama. Hypothesis H2 (Approximation property of Q,). There exist an operator S,€ L(L?(Q); Q,) such that: (1.42) la —Sidlloe<Ch™\Id Ima VaeH™(Q), O<me<l. Hypothesis H3 (Uniform inf-sup condition). For each q,,€ M,, there exists av,€ X,, such that (1.43) (dn, div V,) = |ldnllo,0 (1.44) IWalt,@ < Cll dallo.e with a constant C > 0 independent of h, q;, and Vy. Recall that according to Remark 1.4 the statement of Hypothesis H3 is equivalent to the inf-sup condition (1.12) with B* = 1/C.

## chapter-02-section-01-pc00297 | theorem | high | PDF 139

Theorem 1.8. Under Hypotheses H1, H2 and H3, Problem (1.39) has a unique

## chapter-02-section-01-pc00298 | ordinary-paragraph | high | PDF 139

solution (u,,p,)€V, x M, and u, is also the only solution of Problem (1.40). In addition, (u,, p,,) tends to the solution (u, p) of Problem (1.35): (1.45) lim {{u, — Wly,o+ Px — Pllo,a=} 9 .

## chapter-02-section-01-pc00299 | equation | low | PDF 139

[[FORMULA:f-p0139-02102]]

## chapter-02-section-01-pc00300 | ordinary-paragraph | high | PDF 139

Furthermore, when (u,p ) belongs to H™*1(Q)% x (H™(Q)N Lo(Q)) for some integer m with 1 < m <l, we have the error bound: (1.46) ju — uglia + IP — Pallo.g < Ch {4 llms1.0 + IP limos:

## chapter-02-section-01-pc00301 | proof | high | PDF 139

Proof. Let us apply Theorem 1.1. Owing to Hypothesis H3, the pair of spaces

## chapter-02-section-01-pc00302 | ordinary-paragraph | high | PDF 139

(X,,M,,) satisfies a uniform inf-sup condition; therefore it suffices to check the ellipticity of a(., .) in order to obtain that Problem (1.39) has a unique solution. When a(., .) is defined by (1.36b), we have:

## chapter-02-section-01-pc00303 | equation | low | PDF 139

[[FORMULA:f-p0139-02107]]

## chapter-02-section-01-pc00304 | ordinary-paragraph | high | PDF 139

inequality (cf. (1.5.31)) and when a(., .) is defined by (1.36a) we use Korn’s

## chapter-02-section-01-pc00305 | equation | low | PDF 139

[[FORMULA:f-p0139-02108]]

## chapter-02-section-01-pc00306 | ordinary-paragraph | high | PDF 140

that Problem (1.39) has a unique solution (u,,p,)¢X), x M,, where u, is the unique solution of Problem (1.40), and we have: (1.47) ja ayh.a+ bP Pao. C14 inf |u—v,|;,q+ inf I2 ~ aulo.o} VnE Xn qn€ My with a constant C, independent of h. Now, observe that if s, does not map Lg(Q) onto M, we can replace it by: - 1

## chapter-02-section-01-pc00307 | equation | low | PDF 140

[[FORMULA:f-p0140-02112]]

## chapter-02-section-01-pc00308 | ordinary-paragraph | high | PDF 140

then 5,¢ L(L7(Q);M,) and 5.4 — dllo.e< snd — Glog VaeLo(Q). Thus if pe H™(Q) L3(Q), Hypothesis H2 gives:

## chapter-02-section-01-pc00309 | equation | low | PDF 140

[[FORMULA:f-p0140-02114]]

## chapter-02-section-01-pc00310 | ordinary-paragraph | high | PDF 140

qne My, Likewise, if ue H”*'(Q)*" NV, Hypothesis H1 yields:

## chapter-02-section-01-pc00311 | equation | low | PDF 140

[[FORMULA:f-p0140-02115]]

## chapter-02-section-01-pc00312 | ordinary-paragraph | high | PDF 140

VnAE Xp, These inequalities and (1.47) imply (1.46). It remains to establish the limit (1.45). For this we make use of Corollary 1.2 and the above considerations. We know that H?(Q)M H}(Q) is dense in H}({Q) and that H'(Q)M L$(Q) is dense in L3(Q). Hence it suffices to work with the above operators r, and s, to obtain (1.45). i Of course, (1.46) implies that ||u — u, ||oo = O(h™), but it is possible to refine this estimate by making use of Theorem 1.2. Here we take He LQ Then Problem (1.21) is the homogeneous Stokes Problem: Find a pair (9, €) in Hj(Q)*% x L3(Q) such that: (1.48) —vAg + gradé = g in Q, where ge L?(Q)*.

## chapter-02-section-01-pc00313 | equation | low | PDF 140

[[FORMULA:f-p0140-02122]]

## chapter-02-section-01-pc00314 | ordinary-paragraph | high | PDF 140

We shall require below the following concept of regularity for this problem.

## chapter-02-section-01-pc00315 | definition | high | PDF 140

Definition 1.1. We say that Problem (1.48) is regular if the mapping

## chapter-02-section-01-pc00316 | equation | low | PDF 140

[[FORMULA:f-p0140-02124]]

## chapter-02-section-01-pc00317 | ordinary-paragraph | medium | PDF 140,141

is an isomorphism from [H?(Q)*NV] x [H1(Q)N L2(Q)] onto L7(Q)". This definition means that @ belongs to H?(Q)" and & to H'!(Q) whenever the right-hand side g belongs to L?(Q)" and Observe that in view of Theorem 1.5.4, Problem (1.48) is regular as soon as the boundary I of Ω is of class &2. When F is only Lipschitz-continuous -and subsequently I will be a polygonal line—Remark 1.5.6 asserts that Problem (1.48) is regular provided Q is a plane, bounded and convex polygon. 'Theorem 1.9. Assume that Hypotheses H1, H2 and H3 are satisfied and that Problem (1.48) is regular. Then, if the solution (u, p) of the Stokes Problem (1.35) belongs to Hm+1(Q) x Hm(Ω)N L2(Q) for some integer m with 1 ≤ m ≤l, we have the following error bound:

## chapter-02-section-01-pc00318 | equation | low | PDF 141

[[FORMULA:f-p0141-02129]]

## chapter-02-section-01-pc00319 | equation | low | PDF 141

[[FORMULA:f-p0141-02130]]

## chapter-02-section-01-pc00320 | proof | medium | PDF 141

Proof. According to Theorem 1.2 and Remark 1.6, we have:

## chapter-02-section-01-pc00321 | equation | low | PDF 141

[[FORMULA:f-p0141-02131]]

## chapter-02-section-01-pc00322 | equation | low | PDF 141

[[FORMULA:f-p0141-02132]]

## chapter-02-section-01-pc00323 | ordinary-paragraph | medium | PDF 141

1

## chapter-02-section-01-pc00324 | equation | low | PDF 141

[[FORMULA:f-p0141-02133]]

## chapter-02-section-01-pc00325 | equation | low | PDF 141

[[FORMULA:f-p0141-02134]]

## chapter-02-section-01-pc00326 | ordinary-paragraph | low | PDF 141

geL2(2) 1gll0,Q (neXn Sh∈Mh ()a  () >  A  o)H    (t 1) o extra power of h in (1.50) follows from Hypotheses H1 and H2 with m = 1 and (1.46) substituted into (1.51). Thus Hypothesis H1 with m = 1 and Hypothesis H2 with m = 1 yield:

## chapter-02-section-01-pc00327 | equation | low | PDF 141

[[FORMULA:f-p0141-02139]]

## chapter-02-section-01-pc00328 | equation | low | PDF 141

[[FORMULA:f-p0141-02140]]

## chapter-02-section-01-pc00329 | ordinary-paragraph | low | PDF 141

SheMn Φn∈Vn Therefore combining (1.49) and (1.51) we obtain:

## chapter-02-section-01-pc00330 | equation | low | PDF 141

[[FORMULA:f-p0141-02142]]

## chapter-02-section-01-pc00331 | equation | low | PDF 141

[[FORMULA:f-p0141-02143]]

## chapter-02-section-01-pc00332 | ordinary-paragraph | low | PDF 141

qhE Mh and (1.50) follows from (1.46) and (1.42). 口 As mentioned in the previous section, the verification of Hypothesis H3 is bound to be often quite intricate. In fact, the choice of the spaces X, and M, is The reader will find in the next section how to construct such pairs of spaces. We finish this section with a brief survey of the iterative methods proposed in Section 1.2 to decouple the computation of u, from that of ph. We choose the scalar product of L2(Q) for the bilinear form c( ., .): p(x)q(x)dx.

## chapter-02-section-01-pc00333 | equation | low | PDF 141

[[FORMULA:f-p0141-02145]]

## chapter-02-section-01-pc00334 | ordinary-paragraph | low | PDF 141,142

Q Then, the penalized version of Problem (1.40) becomes: Find a function ui, e X, such that Problem (1.52) dissociates the computation of uj, from that of p;, since here p;, is given explicitly by

## chapter-02-section-01-pc00335 | equation | low | PDF 142

[[FORMULA:f-p0142-02148]]

## chapter-02-section-01-pc00336 | ordinary-paragraph | high | PDF 142

But, of course, this problem offers a practical interest only if the calculation of p, (div v,) is simple. This will be precisely the case of nearly all methods discussed in this chapter because the functions of M,, will be piecewise discontinuous and p, Will be a local operator. As far as the convergence of uj, is concerned, a straightforward application of Theorem 1.3 gives the following result.

## chapter-02-section-01-pc00337 | theorem | high | PDF 142

Theorem 1.10. Problem (1.52) has a unique solution uj, for all ¢ > 0. Moreover,

## chapter-02-section-01-pc00338 | ordinary-paragraph | high | PDF 142

under Hypothesis H3, we have for all € < & sufficiently small: 1 :

## chapter-02-section-01-pc00339 | equation | low | PDF 142

[[FORMULA:f-p0142-02152]]

## chapter-02-section-01-pc00340 | ordinary-paragraph | high | PDF 142

0,2 with a constant C > 0 independent of h and «. Similarly, uj; and p; can be expanded in powers of «. Starting with p? = p,, we define the sequence (uj, pj) € X), x M,, solution of

## chapter-02-section-01-pc00341 | equation | low | PDF 142

[[FORMULA:f-p0142-02155]]

## chapter-02-section-01-pc00342 | equation | low | PDF 142

[[FORMULA:f-p0142-02156]]

## chapter-02-section-01-pc00343 | equation | low | PDF 142

[[FORMULA:f-p0142-02157]]

## chapter-02-section-01-pc00344 | ordinary-paragraph | high | PDF 142

Then Theorem 1.4 yields the following asymptotic expansion:

## chapter-02-section-01-pc00345 | theorem | high | PDF 142

Theorem 1.11. Under Hypothesis H3, we have for all integers M > 1 and alle < &

## chapter-02-section-01-pc00346 | ordinary-paragraph | high | PDF 142

sufficiently small: M Liee M

## chapter-02-section-01-pc00347 | equation | low | PDF 142

[[FORMULA:f-p0142-02159]]

## chapter-02-section-01-pc00348 | equation | low | PDF 142

[[FORMULA:f-p0142-02160]]

## chapter-02-section-01-pc00349 | equation | low | PDF 142

[[FORMULA:f-p0142-02161]]

## chapter-02-section-01-pc00350 | ordinary-paragraph | high | PDF 142

with a constant Ky independent of h and «. Now, let us discuss the gradient algorithms. With the above choice of c(., .), the bilinear form a’"(., .) reads:

## chapter-02-section-01-pc00351 | equation | low | PDF 142

[[FORMULA:f-p0142-02162]]

## chapter-02-section-01-pc00352 | ordinary-paragraph | low | PDF 142,143

It is H}(Q)*-elliptic and obviously symmetric. Therefore, the algorithms described by (1.33) and (1.34) are genuine gradient algorithms. The formulas for the simple gradient algorithm with optimal parameter are: 1°) Predict the initial value p? ¢ M, and compute the solution uy € X, of: 2°) For m ≥O, knowing (u,p) determine z"e X, μeR and the pair (um+1,pm+1)∈ Xn x Mn by:

## chapter-02-section-01-pc00353 | equation | low | PDF 143

[[FORMULA:f-p0143-02165]]

## chapter-02-section-01-pc00354 | ordinary-paragraph | low | PDF 143

Vvhe Xh;

## chapter-02-section-01-pc00355 | equation | low | PDF 143

[[FORMULA:f-p0143-02166]]

## chapter-02-section-01-pc00356 | equation | low | PDF 143

[[FORMULA:f-p0143-02167]]

## chapter-02-section-01-pc00357 | equation | low | PDF 143

[[FORMULA:f-p0143-02168]]

## chapter-02-section-01-pc00358 | ordinary-paragraph | low | PDF 143

um + ur zn. The conjugate-gradient algorithm initializes u like above and replaces step n° 2 by: 2°) For m ≥0, knowing (um,pm)eX, x M, compute (zm,om)eX, × Mh (μn, om)e R × R and the pair (um+1, pm+1)e X, × M, by:

## chapter-02-section-01-pc00359 | equation | low | PDF 143

[[FORMULA:f-p0143-02170]]

## chapter-02-section-01-pc00360 | ordinary-paragraph | low | PDF 143

m Oh

## chapter-02-section-01-pc00361 | equation | low | PDF 143

[[FORMULA:f-p0143-02171]]

## chapter-02-section-01-pc00362 | equation | low | PDF 143

[[FORMULA:f-p0143-02172]]

## chapter-02-section-01-pc00363 | equation | low | PDF 143

[[FORMULA:f-p0143-02173]]

## chapter-02-section-01-pc00364 | ordinary-paragraph | low | PDF 143

Wvhe Xh,

## chapter-02-section-01-pc00365 | equation | low | PDF 143

[[FORMULA:f-p0143-02174]]

## chapter-02-section-01-pc00366 | equation | low | PDF 143

[[FORMULA:f-p0143-02175]]

## chapter-02-section-01-pc00367 | ordinary-paragraph | medium | PDF 143

μm

## chapter-02-section-01-pc00368 | equation | low | PDF 143

[[FORMULA:f-p0143-02176]]

## chapter-02-section-01-pc00369 | equation | low | PDF 143

[[FORMULA:f-p0143-02177]]

## chapter-02-section-01-pc00370 | equation | low | PDF 143

[[FORMULA:f-p0143-02178]]

## chapter-02-section-01-pc00371 | ordinary-paragraph | medium | PDF 143

It follows from Theorems 1.5 and 1.7 that both gradient algorithms are convergent provided the Hypothesis H3 holds. Furthermore, the simple-gradient algorithm converges for any choice of the parameters μm such that:

## chapter-02-section-01-pc00372 | equation | low | PDF 143

[[FORMULA:f-p0143-02179]]

## chapter-02-section-01-pc00373 | ordinary-paragraph | medium | PDF 143

m m

## chapter-02-section-01-pc00374 | subsection | medium | PDF 143

1.4. Checking the inf-sup Condition

## chapter-02-section-01-pc00375 | ordinary-paragraph | medium | PDF 143,144

This short section is dedicated to the construction of pairs of spaces (X, M,) that satisfy uniformly the inf-sup condition (1.12). The underlying idea due to Boland & Nicolaides [11], is that if (1.12) holds uniformly for a pair of spaces (X, M,) then one can generate a whole family of pairs of spaces that also satisfy (1.12) uniformly provided they satisfy a local inf-sup condition. In other words, the global condition (1.12) can be reduced to a local condition, which is of course open subsets Q, with boundary I,: R

## chapter-02-section-01-pc00376 | equation | low | PDF 144

[[FORMULA:f-p0144-02186]]

## chapter-02-section-01-pc00377 | equation | low | PDF 144

[[FORMULA:f-p0144-02187]]

## chapter-02-section-01-pc00378 | ordinary-paragraph | medium | PDF 144

Let X, and M, be defined by (1.38) with R c Qh. For 1 ≤ r ≤ R we set:

## chapter-02-section-01-pc00379 | equation | low | PDF 144

[[FORMULA:f-p0144-02189]]

## chapter-02-section-01-pc00380 | equation | low | PDF 144

[[FORMULA:f-p0144-02190]]

## chapter-02-section-01-pc00381 | equation | low | PDF 144

[[FORMULA:f-p0144-02191]]

## chapter-02-section-01-pc00382 | equation | low | PDF 144

[[FORMULA:f-p0144-02192]]

## chapter-02-section-01-pc00383 | equation | low | PDF 144

[[FORMULA:f-p0144-02193]]

## chapter-02-section-01-pc00384 | equation | low | PDF 144

[[FORMULA:f-p0144-02194]]

## chapter-02-section-01-pc00385 | ordinary-paragraph | medium | PDF 144

Note that the functions of X,(Ω,) belong to H(Q,). We introduce as an assumption the following concept of uniform, local inf-sup condition with respect to this partition: Hypothesis H4. There exists a constant X* > 0, independent of h and r, such that:

## chapter-02-section-01-pc00386 | equation | low | PDF 144

[[FORMULA:f-p0144-02197]]

## chapter-02-section-01-pc00387 | equation | low | PDF 144

[[FORMULA:f-p0144-02198]]

## chapter-02-section-01-pc00388 | equation | low | PDF 144

[[FORMULA:f-p0144-02199]]

## chapter-02-section-01-pc00389 | ordinary-paragraph | low | PDF 144

VaneM(Ω),  1 ≤r ≤ R.

## chapter-02-section-01-pc00390 | equation | low | PDF 144

[[FORMULA:f-p0144-02201]]

## chapter-02-section-01-pc00391 | ordinary-paragraph | low | PDF 144

[Vhli,2, h∈Xn(S) Let us establish the salient result of this section.

## chapter-02-section-01-pc00392 | theorem | medium | PDF 144

Theorem 1.12. Let the pair of spaces (X, M,) defined by (1.38) satisfy Hypothesis

## chapter-02-section-01-pc00393 | ordinary-paragraph | medium | PDF 144

H4. If there exists a subspace X, of X, such that the pair (X,, Mh) satisfies the inf-sup condition (1.12) with a constant β independent of h, then (X,, Mh) also satisfies (1.12) with a constant β* independent of h.

## chapter-02-section-01-pc00394 | proof | medium | PDF 144

Proof. From the definition (1.54) we derive immediately the orthogonal decom-

## chapter-02-section-01-pc00395 | ordinary-paragraph | medium | PDF 144

position of Q,(Ω,):

## chapter-02-section-01-pc00396 | equation | low | PDF 144

[[FORMULA:f-p0144-02206]]

## chapter-02-section-01-pc00397 | ordinary-paragraph | medium | PDF 144

Thus each function qn e M, can be split as follows:

## chapter-02-section-01-pc00398 | equation | low | PDF 144

[[FORMULA:f-p0144-02207]]

## chapter-02-section-01-pc00399 | ordinary-paragraph | medium | PDF 144

where 1

## chapter-02-section-01-pc00400 | equation | low | PDF 144

[[FORMULA:f-p0144-02208]]

## chapter-02-section-01-pc00401 | ordinary-paragraph | low | PDF 144

qh dx meas(Ω,) J and á, = ahl2, E M,(Q,). Observe that qnE M, and that the orthogonality of the decomposition implies:

## chapter-02-section-01-pc00402 | equation | low | PDF 144

[[FORMULA:f-p0144-02210]]

## chapter-02-section-01-pc00403 | equation | low | PDF 144

[[FORMULA:f-p0144-02211]]

## chapter-02-section-01-pc00404 | ordinary-paragraph | medium | PDF 144

Now, owing to Hypothesis H4 and Remark 1.4 there exists a function

## chapter-02-section-01-pc00405 | equation | low | PDF 145

[[FORMULA:f-p0145-02212]]

## chapter-02-section-01-pc00406 | ordinary-paragraph | low | PDF 145

Jsr

## chapter-02-section-01-pc00407 | equation | low | PDF 145

[[FORMULA:f-p0145-02213]]

## chapter-02-section-01-pc00408 | equation | low | PDF 145

[[FORMULA:f-p0145-02214]]

## chapter-02-section-01-pc00409 | ordinary-paragraph | low | PDF 145

1* Similarly, since the pair (X , M,) satisfies (1.12) there exists a function v, e X , such that

## chapter-02-section-01-pc00410 | equation | low | PDF 145

[[FORMULA:f-p0145-02216]]

## chapter-02-section-01-pc00411 | equation | low | PDF 145

[[FORMULA:f-p0145-02217]]

## chapter-02-section-01-pc00412 | equation | low | PDF 145

[[FORMULA:f-p0145-02218]]

## chapter-02-section-01-pc00413 | ordinary-paragraph | medium | PDF 145

β Let , be the function of X, defined by:

## chapter-02-section-01-pc00414 | equation | low | PDF 145

[[FORMULA:f-p0145-02219]]

## chapter-02-section-01-pc00415 | ordinary-paragraph | medium | PDF 145

We propose to associate with q, the function v,e X,:

## chapter-02-section-01-pc00416 | equation | low | PDF 145

[[FORMULA:f-p0145-02220]]

## chapter-02-section-01-pc00417 | ordinary-paragraph | medium | PDF 145

for some x > O and we hope to adjust the parameter α so that the pair (vh,qh) verifies the inf-sup condition. Let us evaluate (qh, div vh). We have:

## chapter-02-section-01-pc00418 | equation | low | PDF 145

[[FORMULA:f-p0145-02224]]

## chapter-02-section-01-pc00419 | ordinary-paragraph | medium | PDF 145

Now,

## chapter-02-section-01-pc00420 | equation | low | PDF 145

[[FORMULA:f-p0145-02225]]

## chapter-02-section-01-pc00421 | equation | low | PDF 145

[[FORMULA:f-p0145-02226]]

## chapter-02-section-01-pc00422 | equation | low | PDF 145

[[FORMULA:f-p0145-02227]]

## chapter-02-section-01-pc00423 | ordinary-paragraph | medium | PDF 145

by virtue of (1.58) and (1.59) respectively and /N

## chapter-02-section-01-pc00424 | equation | low | PDF 145

[[FORMULA:f-p0145-02229]]

## chapter-02-section-01-pc00425 | equation | low | PDF 145

[[FORMULA:f-p0145-02230]]

## chapter-02-section-01-pc00426 | ordinary-paragraph | low | PDF 145

β Hence, collecting these results we obtain: lI an llo,ollah llo,2.

## chapter-02-section-01-pc00427 | equation | low | PDF 145

[[FORMULA:f-p0145-02231]]

## chapter-02-section-01-pc00428 | ordinary-paragraph | low | PDF 145

R Then, the inequality: 1

## chapter-02-section-01-pc00429 | equation | low | PDF 145

[[FORMULA:f-p0145-02232]]

## chapter-02-section-01-pc00430 | ordinary-paragraph | medium | PDF 145

48 yields
