# Paragraph candidates: chapter-02-section-04

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-02-section-04-pc00001 | ordinary-paragraph | high | PDF 187

Numerical results confirm this theoretical analysis but it appears most often that it is the entire pressure p, that converges towards p—not the component Pp, alone—. This renders the filtering of the pressure component p} seldom necessary. There are cases, though, where p} does diverge; the reader can refer to Boland & Nicolaides [12] for a specific example. Besides that, the reader will find in Malkus & Olsen [55] other examples of currently used finite element spaces which do not satisfy a uniform inf-sup condition. From a practical point of view, Problem (3.36) can be solved by the penalty method of Section 1.3 (cf. (1.52)). Numerical results can be found for example in Carey & Krishnan [16]. But it is also possible to decouple directly the velocity from the pressure by using a basis of “divergence-free” velocities, i.e. a basis of V,. Following Stephens et al [76] we introduce the vector field v,¢ X,, that takes the values (1, — 1), (1, 1), (— 1, 1), (— 1, —1) at the four vertices of x like in

## chapter-02-section-04-pc00002 | figure | high | PDF 187

Figure 17 and (0,0) at all other nodes of 7,; then we define the set

## chapter-02-section-04-pc00003 | equation | low | PDF 187

[[FORMULA:f-p0187-02815]]

## chapter-02-section-04-pc00004 | ordinary-paragraph | high | PDF 187

By inspection, we can easily ascertain that each v,¢S belongs to V, and that all these functions are linearly independent. In addition, a simple dimension argument yields:

## chapter-02-section-04-pc00005 | equation | low | PDF 187

[[FORMULA:f-p0187-02816]]

## chapter-02-section-04-pc00006 | ordinary-paragraph | high | PDF 187

Hence S is a convenient basis of V,. The reader will find numerical results with this basis in the above reference.

## chapter-02-section-04-pc00007 | section | high | PDF 187

§4. Continuous Approximation of the Pressure

## chapter-02-section-04-pc00008 | ordinary-paragraph | high | PDF 187

So far, we have used approximate pressures that were (generally) discontinuous across interelement boundaries. But from the engineering point of view, continuous pressures are more natural because the pressures encountered in practice are usually continuous functions. The fact is that numerical analysts found Stokes solvers with ¢° pressures more difficult to analyze than those with L” pressures. This difficulty accounts for the relatively meager literature on the theory of important schemes of the “Hood-Taylor” type. The first rigorous error analysis of the very popular Hood & Taylor [44] scheme is due to Bercovier & Pironneau [7]. Later on this analysis was cleverly simplified by Verfiirth [83]; but now the approach of Section 1.4 permits to insert directly the Hood-Taylor method into the framework of § 1. Apart from the Hood-Taylor and closely related schemes, this paragraph studies an interesting variant introduced by Glowinski & Pironneau [38] which approximates the Stokes problem by a sequence of discrete Dirichlet problems for —Z.

## chapter-02-section-04-pc00009 | ordinary-paragraph | high | PDF 188

With minor modifications, the setting of the problem is that of Section 1.3. We take for Q a bounded, plane polygon and we assume that the Stokes system

## chapter-02-section-04-pc00010 | equation | low | PDF 188

[[FORMULA:f-p0188-02817]]

## chapter-02-section-04-pc00011 | ordinary-paragraph | high | PDF 188

in Q, (4.1) divu = 0

## chapter-02-section-04-pc00012 | equation | low | PDF 188

[[FORMULA:f-p0188-02819]]

## chapter-02-section-04-pc00013 | ordinary-paragraph | high | PDF 188

is such that: p belongs to H'(Q). Following Arnold et al [2], we construct a triangulation 7, of Q and we approximate the velocity on each element x by a polynomial of (4.2) P (xk) = [P, @ span{A,A,A3}]? and the pressure by a polynomial of P,. Thus we choose the following finite element spaces: (4.3) X, = {ve @°(Q)’; v|,EA,(k) Vee FJ, v/p = 0}, (4.4) Q, = {ge @°(Q); q|.EP, VKET,}, M, = Q,1L3(Q). The degrees of freedom are the simplest ones, namely the values of the velocity at the vertices and center of k and the values of the pressure at the vertices of k. As usual, the space V, is defined by:

## chapter-02-section-04-pc00014 | equation | low | PDF 188

[[FORMULA:f-p0188-02823]]

## chapter-02-section-04-pc00015 | ordinary-paragraph | high | PDF 188

and the approximate problem, called Problem (Q,) reads: Find a pair (u,, p;,) in X, x M,, satisfying:

## chapter-02-section-04-pc00016 | equation | low | PDF 188

[[FORMULA:f-p0188-02824]]

## chapter-02-section-04-pc00017 | equation | low | PDF 188

[[FORMULA:f-p0188-02825]]

## chapter-02-section-04-pc00018 | equation | low | PDF 188

[[FORMULA:f-p0188-02826]]

## chapter-02-section-04-pc00019 | ordinary-paragraph | high | PDF 188

where the bilinear form a(., .) is unchanged:

## chapter-02-section-04-pc00020 | equation | low | PDF 188

[[FORMULA:f-p0188-02827]]

## chapter-02-section-04-pc00021 | ordinary-paragraph | high | PDF 188

ij or

## chapter-02-section-04-pc00022 | equation | low | PDF 188

[[FORMULA:f-p0188-02828]]

## chapter-02-section-04-pc00023 | ordinary-paragraph | high | PDF 188

Note that because the space Q, is contained in H1(Q), the bilinear form b(., .) can be written equivalently as:

## chapter-02-section-04-pc00024 | equation | low | PDF 188

[[FORMULA:f-p0188-02829]]

## chapter-02-section-04-pc00025 | ordinary-paragraph | high | PDF 189

The approximation properties of X,, and Q, are well known. For instance, if the triangulation 7, is regular, the interpolation operator r, defined by:

## chapter-02-section-04-pc00026 | equation | low | PDF 189

[[FORMULA:f-p0189-02830]]

## chapter-02-section-04-pc00027 | ordinary-paragraph | high | PDF 189

(4.6) r,V(a,.) = v(a,) onthe center a, ofk, VKeZ,, r,VEP,(K) oneach k, satisfies r,€ £(LH?(QHo) (@N)] *; Xi) and (4.7) IV —ThVllm.@ <Ch?-"|vlp9 VWreH?(QY, m=Oorl. Indeed, r, is preserved by affine transformations on each x and leaves invariant the polynomials of P?. Likewise, the local regularization operator R, on P, defined by (A.53), (A.54) satisfies R, €Y (L?(Q); Q,,) and (4.8) la —Ridllma<Ch "gle VqeH'(Q) m=Oorl, provided of course that 7, is regular. Therefore the Hypotheses H1 and H2 are fulfilled and it remains to verify H3, namely the inf-sup condition:

## chapter-02-section-04-pc00028 | equation | low | PDF 189

[[FORMULA:f-p0189-02835]]

## chapter-02-section-04-pc00029 | ordinary-paragraph | high | PDF 189

(4.9) sup —"——* > B* lidullo.g Vane My. Yne Xn IVali,2 This is achieved by the next lemma.

## chapter-02-section-04-pc00030 | lemma | high | PDF 189

Lemma 4.1. If the triangulation 7, is regular, the pair of spaces (X;,,M,) defined

## chapter-02-section-04-pc00031 | ordinary-paragraph | high | PDF 189

by (4.3) (4.4) satisfies (4.9) with a constant B* > 0 independent of h.

## chapter-02-section-04-pc00032 | proof | high | PDF 189

Proof. Let us exhibit the operator 2, of Lemma 1.1. Take an arbitrary q, in M,.

## chapter-02-section-04-pc00033 | ordinary-paragraph | high | PDF 189

Since q,, € L2(Q) there exists v in Hj(Q)* such that (4.10) divv=q_, |V l1,2 < Ci lld alloa- Therefore, since M, < H'(Q) we want to construct a function 7,v in X,, that satisfies

## chapter-02-section-04-pc00034 | equation | low | PDF 189

[[FORMULA:f-p0189-02840]]

## chapter-02-section-04-pc00035 | ordinary-paragraph | high | PDF 189,190

KeTZ,, KeT;, As grad p,€P ? on each x, this equality induces us to define z,v in X,, such that: (4.11) 1,Vv(a) =(R,v)(a) Wnode a of 7, and where R, denotes the now familiar local regularization operator on Pee Clearly, (4.11) and (4.12) determine uniquely z,v in X, and 7,€ L(H}(Q); X,,). Moreover

## chapter-02-section-04-pc00036 | equation | low | PDF 190

[[FORMULA:f-p0190-02844]]

## chapter-02-section-04-pc00037 | ordinary-paragraph | high | PDF 190

Q Finally an argument similar to that of Lemma 2.2 shows that

## chapter-02-section-04-pc00038 | equation | low | PDF 190

[[FORMULA:f-p0190-02845]]

## chapter-02-section-04-pc00039 | ordinary-paragraph | high | PDF 190

provided 7, is regular. This proves the lemma. O These results are summarized in the following theorem.

## chapter-02-section-04-pc00040 | theorem | high | PDF 190

Theorem 4.1. Let Q be a bounded plane polygon and let the solution (u, p) of the

## chapter-02-section-04-pc00041 | ordinary-paragraph | high | PDF 190

Stokes system (4.1) satisfy: nelH7Q)OAHA(Oy. pel OL. @). If the triangulation 7, is regular, the solution (u,, p;,) of Problem (4.5) with the spaces X,, and M,, defined by (4.3) and (4.4) respectively satisfies the error bound: (4.13) Ju — uglie + IP — Pallooe < Crh{lulz.e + |Plia}- In addition, when Q is convex, we have the L?-estimate: (4.14) lu —uylloe < Ch? {lulz.0 + IP|1,a}- This “mini” finite element method can easily be generalized to schemes of arbitrary order. The details can be found in Arnold et al [2].

## chapter-02-section-04-pc00042 | subsection | high | PDF 190

4.2. The “‘Hood-Taylor’”’ Finite Element Method

## chapter-02-section-04-pc00043 | ordinary-paragraph | high | PDF 190

The results of the preceding section can be improved by taking a more accurate approximation oft he velocity. Following Hood & Taylor [44], we keep the same space Q, and we replace X,, by: (4.15) X, = {ve S(Q)?; v|,.€P? Vee J, vjp = 0}, with the function values at the principal lattice of order 2 (cf. (A.19)) as degrees of freedom. Therefore the standard interpolation operator I, satisfies: I,€ 2(LH*(Q)N Ho(2)]’; X,), (4.16) |lv—J,VIImo< Chi "|vi,g YWeH*(Q), k=20r3, m=Oorl.

## chapter-02-section-04-pc00044 | ordinary-paragraph | medium | PDF 191

The remainder of this section is devoted to the proof of the inf-sup condition. We propose to establish it first locally and then extend it by Theorem 1.12. The reader can also refer to Verfirth [83] for a direct global proof. Here, the difficulty in a local argument lies in the choice of an adequate partition of Ω. We propose to group together all the elements which share a common vertex like in Figure 18. More precisely, we make the following assumption on the triangulation h: J, has a set of interior nodes {a,}=1 such that {Ω,}-1 with Uk

## chapter-02-section-04-pc00045 | equation | low | PDF 191

[[FORMULA:f-p0191-02855]]

## chapter-02-section-04-pc00046 | equation | low | PDF 191

[[FORMULA:f-p0191-02856]]

## chapter-02-section-04-pc00047 | ordinary-paragraph | medium | PDF 191

k has vertex ar is a partition of Ω.

## chapter-02-section-04-pc00048 | ordinary-paragraph | low | PDF 191

K X R,

## chapter-02-section-04-pc00049 | equation | low | PDF 191

[[FORMULA:f-p0191-02857]]

## chapter-02-section-04-pc00050 | ordinary-paragraph | low | PDF 191

α2 α α3 α α6K α5 K K6 K6 a,

## chapter-02-section-04-pc00051 | equation | low | PDF 191

[[FORMULA:f-p0191-02858]]

## chapter-02-section-04-pc00052 | figure | medium | PDF 191

Figure 18

## chapter-02-section-04-pc00053 | ordinary-paragraph | medium | PDF 191

If this assumption holds, each element k of , belongs to exactly one macroelement Q,. In addition, the fact that all the nodes a, are inside Q implies that each element k has exactly one side on the boundary of its macro-element Q, and at most one side on the boundary I of Q. In practice, it is not difficult to construct a triangulation that satisfies (4.17). The usual procedure is to start with a coarse grid and then progressively refine it by adding interior nodes.

## chapter-02-section-04-pc00054 | ordinary-paragraph | high | PDF 192

(4.18) Qn(2,) = {dlo,3 4 Qn},

## chapter-02-section-04-pc00055 | equation | low | PDF 192

[[FORMULA:f-p0192-02861]]

## chapter-02-section-04-pc00056 | ordinary-paragraph | high | PDF 192

Let us prove that the pair (X,(Q,), M,(Q,)) satisfies a local inf-sup condition.

## chapter-02-section-04-pc00057 | theorem | high | PDF 192

Theorem 4.2. Suppose that 7, is a regular triangulation of Q and that J, satisfies

## chapter-02-section-04-pc00058 | ordinary-paragraph | high | PDF 192

(4.17). Then there exists a constant A* > 0, independent of h and r, such that: (4.19) sup (| acivyds) Ivo, > A*\d\lo.a, VaeM,(2,). ve X,(Q,) Q

## chapter-02-section-04-pc00059 | proof | high | PDF 192

Proof. Let J be the number of elements x in Q, and let us number them with an

## chapter-02-section-04-pc00060 | ordinary-paragraph | high | PDF 192

index i ranging from 0 to J such that x; is adjacent to x;_, and k,,, and Ky = Ky (like in Figure 18): 0 a

## chapter-02-section-04-pc00061 | ordinary-paragraph | high | PDF 192

We denote by x; the side shared by x; and x;,,, by a; the midpoint of x; and by a, the vertex common to all the x; in Q,. Like in Section A.3, we associate with Q, the reference set: J)

## chapter-02-section-04-pc00062 | equation | low | PDF 192

[[FORMULA:f-p0192-02866]]

## chapter-02-section-04-pc00063 | ordinary-paragraph | high | PDF 192

through the continuous, piecewise affine function F. defined by:

## chapter-02-section-04-pc00064 | equation | low | PDF 192

[[FORMULA:f-p0192-02867]]

## chapter-02-section-04-pc00065 | ordinary-paragraph | high | PDF 192

Since the triangulation is regular, the number J is bounded above by a fixed constant I independent of r and as a consequence there are at most J different reference sets 2. This means that all geometrical constants related to Q and K; can be bounded independently of h and r. Now let q,, be an arbitrary element of Q,(Q,) and let v,, be a function in X,(Q,) that satisfies v,(a,) = 0. Since y, vanishes on 0Q, and q, belongs to H!(Q,) we have: J

## chapter-02-section-04-pc00066 | equation | low | PDF 192

[[FORMULA:f-p0192-02869]]

## chapter-02-section-04-pc00067 | ordinary-paragraph | high | PDF 192

Q, RAP, Observe that each component v of v, is a polynomial of P, on x; that vanishes at the vertices of «;. Hence the following quadrature formula holds:

## chapter-02-section-04-pc00068 | equation | low | PDF 192

[[FORMULA:f-p0192-02870]]

## chapter-02-section-04-pc00069 | ordinary-paragraph | high | PDF 192

i As grad q,, is constant on each x; (say grad Gnlx, = &i), this formula yields: J (4.20) [ div v,q,4x = —(1/3) Zem eas(x;) {¥(o;) +

## chapter-02-section-04-pc00070 | equation | low | PDF 192

[[FORMULA:f-p0192-02873]]

## chapter-02-section-04-pc00071 | ordinary-paragraph | high | PDF 193

Next, remark that 0q,,/0t is continuous at interelements boundaries. This suggests to choose

## chapter-02-section-04-pc00072 | equation | low | PDF 193

[[FORMULA:f-p0193-02874]]

## chapter-02-section-04-pc00073 | ordinary-paragraph | high | PDF 193

where t; is the tangent vector to x; with length ||«;|| and (say) pointing outside Q,. With this choice we obtain

## chapter-02-section-04-pc00074 | equation | low | PDF 193

[[FORMULA:f-p0193-02875]]

## chapter-02-section-04-pc00075 | ordinary-paragraph | high | PDF 193

But according to (A.9), g-t is preserved by affine transformations. Thus, with obvious notations we can write:

## chapter-02-section-04-pc00076 | equation | low | PDF 193

[[FORMULA:f-p0193-02876]]

## chapter-02-section-04-pc00077 | ordinary-paragraph | high | PDF 193

r Clearly, each set of vectors te, ; t;} is a basis on the reference space. Therefore the mapping g > {(g-t,;_,)* + (g:t,)7}1” is equivalent to the Euclidean norm on the reference space. Hence, in view of

## chapter-02-section-04-pc00078 | equation | low | PDF 193

[[FORMULA:f-p0193-02878]]

## chapter-02-section-04-pc00079 | ordinary-paragraph | high | PDF 193

there exists a constant C, > 0 such that: df (4.21) | divv,q,dx > C, ¥, meas(x;,)|417,«, Oy. ial Next, on the one hand the definition of v, yields:

## chapter-02-section-04-pc00080 | equation | low | PDF 193

[[FORMULA:f-p0193-02881]]

## chapter-02-section-04-pc00081 | equation | low | PDF 193

[[FORMULA:f-p0193-02882]]

## chapter-02-section-04-pc00082 | equation | low | PDF 193

[[FORMULA:f-p0193-02883]]

## chapter-02-section-04-pc00083 | ordinary-paragraph | high | PDF 193

And on the other hand, the argument of Lemma A.6 gives:

## chapter-02-section-04-pc00084 | equation | low | PDF 193

[[FORMULA:f-p0193-02884]]

## chapter-02-section-04-pc00085 | equation | low | PDF 193

[[FORMULA:f-p0193-02885]]

## chapter-02-section-04-pc00086 | equation | low | PDF 193

[[FORMULA:f-p0193-02886]]

## chapter-02-section-04-pc00087 | ordinary-paragraph | high | PDF 193

by virtue of (A.2) and (4.22). Hence it stems from (4.21), (4.23) and the regularity of 7, that J 1/2 (4.24) | div v,q,dx 2 Coll/ova.a.4 3 meas(e) dif :

## chapter-02-section-04-pc00088 | equation | low | PDF 193

[[FORMULA:f-p0193-02889]]

## chapter-02-section-04-pc00089 | ordinary-paragraph | high | PDF 193

It remains to show that, on a regular triangulation, Ap 1/2 VaeH*(2,)N Lo).

## chapter-02-section-04-pc00090 | equation | low | PDF 193

[[FORMULA:f-p0193-02890]]

## chapter-02-section-04-pc00091 | equation | low | PDF 193

[[FORMULA:f-p0193-02891]]

## chapter-02-section-04-pc00092 | ordinary-paragraph | high | PDF 193

The corresponding proof is a simple variant of that of Lemma 2.5. To begin with,

## chapter-02-section-04-pc00093 | equation | low | PDF 194

[[FORMULA:f-p0194-02892]]

## chapter-02-section-04-pc00094 | ordinary-paragraph | low | PDF 194

q dx. 02 Then q and q differ by a constant and we have:

## chapter-02-section-04-pc00095 | equation | low | PDF 194

[[FORMULA:f-p0194-02893]]

## chapter-02-section-04-pc00096 | ordinary-paragraph | medium | PDF 194

ceR But

## chapter-02-section-04-pc00097 | equation | low | PDF 194

[[FORMULA:f-p0194-02894]]

## chapter-02-section-04-pc00098 | ordinary-paragraph | low | PDF 194

14 l16,2, 

## chapter-02-section-04-pc00099 | equation | low | PDF 194

[[FORMULA:f-p0194-02895]]

## chapter-02-section-04-pc00100 | equation | low | PDF 194

[[FORMULA:f-p0194-02896]]

## chapter-02-section-04-pc00101 | equation | low | PDF 194

[[FORMULA:f-p0194-02897]]

## chapter-02-section-04-pc00102 | ordinary-paragraph | low | PDF 194

meas(k:)lali,x*

## chapter-02-section-04-pc00103 | equation | low | PDF 194

[[FORMULA:f-p0194-02898]]

## chapter-02-section-04-pc00104 | equation | low | PDF 194

[[FORMULA:f-p0194-02899]]

## chapter-02-section-04-pc00105 | equation | low | PDF 194

[[FORMULA:f-p0194-02900]]

## chapter-02-section-04-pc00106 | equation | low | PDF 194

[[FORMULA:f-p0194-02901]]

## chapter-02-section-04-pc00107 | ordinary-paragraph | low | PDF 194

Hence 1/2 meas(k;)al,x;(

## chapter-02-section-04-pc00108 | equation | low | PDF 194

[[FORMULA:f-p0194-02902]]

## chapter-02-section-04-pc00109 | equation | low | PDF 194

[[FORMULA:f-p0194-02903]]

## chapter-02-section-04-pc00110 | ordinary-paragraph | medium | PDF 194

where

## chapter-02-section-04-pc00111 | equation | low | PDF 194

[[FORMULA:f-p0194-02904]]

## chapter-02-section-04-pc00112 | equation | low | PDF 194

[[FORMULA:f-p0194-02905]]

## chapter-02-section-04-pc00113 | equation | low | PDF 194

[[FORMULA:f-p0194-02906]]

## chapter-02-section-04-pc00114 | equation | low | PDF 194

[[FORMULA:f-p0194-02907]]

## chapter-02-section-04-pc00115 | ordinary-paragraph | medium | PDF 194

This finishes the proof because the regularity of , implies that (cf. Bernardi [9]):

## chapter-02-section-04-pc00116 | equation | low | PDF 194

[[FORMULA:f-p0194-02908]]

## chapter-02-section-04-pc00117 | equation | low | PDF 194

[[FORMULA:f-p0194-02909]]

## chapter-02-section-04-pc00118 | ordinary-paragraph | low | PDF 194

口 Owing to Theorem 1.12, the local inf-sup condition (4.19) yields readily the required global condition.

## chapter-02-section-04-pc00119 | corollary | medium | PDF 194

Corollary 4.1. Under the assumptions of Theorem 4.2 the pair of spaces (Xn, Mh)

## chapter-02-section-04-pc00120 | ordinary-paragraph | medium | PDF 194

defined by (4.15) (4.4) satisfies the inf-sup condition (4.9) with a constant β* > 0 independent of h.

## chapter-02-section-04-pc00121 | proof | medium | PDF 194

Proof. Let X, be the finite element space defined by (2.3) and let

## chapter-02-section-04-pc00122 | equation | low | PDF 194

[[FORMULA:f-p0194-02913]]

## chapter-02-section-04-pc00123 | ordinary-paragraph | low | PDF 194

Then on the one hand, X, c X, because the functions of X, are piecewise incomplete polynomials of P2. On the other hand, it follows from Lemma 2.2 that the pair (X,, M,) satisfies a uniform inf-sup condition since the functions of M, are a particular case of piecewise constants. Hence the result follows from Theorems 1.12 and 4.2. 口

## chapter-02-section-04-pc00124 | remark | high | PDF 195

Remark 4.1. Most technical details in the proof of Theorem 4.2 have already been

## chapter-02-section-04-pc00125 | ordinary-paragraph | high | PDF 195

used by Bercovier & Pironneau [7] in establishing a weak form of the inf-sup condition (4.9). Albeit simple, the above proof is long because it deals with a reference region composed of several reference triangles instead of a single one. The crucial point in the proof is the particular choice of v at the midpoint of the interior segments. Apart from that, the major steps are essentially the same as those used in proving Theorem 2.2.

## chapter-02-section-04-pc00126 | ordinary-paragraph | high | PDF 195

With Theorem 4.2 and its corollary we readily derive the major result of this section.

## chapter-02-section-04-pc00127 | theorem | high | PDF 195

Theorem 4.3. Let Q be a bounded, plane polygon and let the solution (u, p) of the

## chapter-02-section-04-pc00128 | ordinary-paragraph | high | PDF 195

Stokes system (4.1) satisfy

## chapter-02-section-04-pc00129 | equation | low | PDF 195

[[FORMULA:f-p0195-02918]]

## chapter-02-section-04-pc00130 | ordinary-paragraph | high | PDF 195

If the triangulation Z,, is regular and like in (4.17), the solution (u,, p,) of Problem (4.5) with spaces X,, and M,, defined by (4.15) (4.4) satisfies the estimate: (4.27) |u—uyIlP i— Poal+le <Cih*{luh+s [1P.h0ot k= Lord.

## chapter-02-section-04-pc00131 | ordinary-paragraph | high | PDF 195

When Q is convex, this can be refined: (4.28) ju —u,lloa<O h ule O ar IP|x, a}:

## chapter-02-section-04-pc00132 | ordinary-paragraph | high | PDF 195

Furthermore, if 7, is uniformly regular (but Q not necessarily convex) we also have: (4.29) p= Pleo = Gh laleeco + 'IPleo)

## chapter-02-section-04-pc00133 | remark | high | PDF 195

Remark 4.2. In order to establish (4.29) we can apply Corollary 4.1 and switch

## chapter-02-section-04-pc00134 | ordinary-paragraph | high | PDF 195

from ||p_ — allo.e to [Pr — Gal1,q by Corollary A.3 (this is where the uniformity of 7, steps in).

## chapter-02-section-04-pc00135 | remark | high | PDF 195

Remark 4.3. Obviously, Remark 2.6 is also valid here.

## chapter-02-section-04-pc00136 | ordinary-paragraph | high | PDF 195

We finish this section with a quick study of a popular variant of the Hood- Taylor method. Again, let 7, be a regular triangulation of Q that satisfies (4.17)

## chapter-02-section-04-pc00137 | ordinary-paragraph | high | PDF 195

divide each of its triangles « into four equal triangles & by joining the and let us midpoints of the sides (cf. Figure 19). For the pressure, we retain the spaces Q, and M, defined by (4.4) and we replace the velocity space X,, by:

## chapter-02-section-04-pc00138 | equation | low | PDF 195

[[FORMULA:f-p0195-02928]]

## chapter-02-section-04-pc00139 | equation | low | PDF 195

[[FORMULA:f-p0195-02929]]

## chapter-02-section-04-pc00140 | equation | low | PDF 195

[[FORMULA:f-p0195-02930]]

## chapter-02-section-04-pc00141 | ordinary-paragraph | high | PDF 195

The approximation properties of Q, and M, are unchanged while the approximation properties of X,, correspond to polynomials of P,, i.e. we have:

## chapter-02-section-04-pc00142 | figure | high | PDF 196

Figure 19. Triangle K divided into four subtriangles

## chapter-02-section-04-pc00143 | ordinary-paragraph | high | PDF 196

where I, €f ((H?(Q)N H3(Q)]’; X,,) is the standard interpolator at the vertices of each subtriangle kK of 7,. The proof of the inf-sup condition is almost exactly like above. We take the same partition (4.17) and observe that the space X,(Q,) with X,, defined by (4.30) involves exactly the same degrees of freedom as if the space X, were defined by (4.15). Just the degree of the polynomials varies and this affects only the factor 1/3 in the quadrature formula (4.20) and the reference constants C in subsequent formulas. Hence the statement of Theorem 4.2 carries over here without modification. To switch from the local inf-sup condition to the global inf-sup condition, we choose the same space M, but we take xe — Ge It is easy to prove that the pair of spaces (X,,M,) satisfies a uniform inf-sup condition. This is in fact part of a more general result.

## chapter-02-section-04-pc00144 | lemma | high | PDF 196

Lemma 4.2. If the triangulation 7, is regular, the spaces X,, and

## chapter-02-section-04-pc00145 | ordinary-paragraph | high | PDF 196

{qe L(Q); q is constant onk VKeZ,} satisfy a uniform inf-sup condition. We skip the proof since it is included in the argument of Lemma 3.8: it suffices to adapt the definition of the restriction operator z to the present case. Summarizing, we have the analogue of Theorem 4.3.

## chapter-02-section-04-pc00146 | theorem | high | PDF 196

Theorem 4.4. Let Q and 7, satisfy the hypotheses of Theorem 4.3 and suppose the

## chapter-02-section-04-pc00147 | ordinary-paragraph | high | PDF 196

solution (u, p) of (4.1) belongs to H*(Q)? x [H*(Q)N L2(Q)]. Then the solution (u,, Pr) of Problem (4.5) with X,, and M, defined by (4.30) (4.4) has the error bound: (4.32) lu — uylia + IP — Palloa < Cyh{lul, 9 + IPli,a}- Moreover, when Q is convex we have the L?-estimate: (4.33) lu — uy llo.g< Cah? {luo + IPli,a}-

## chapter-02-section-04-pc00148 | remark | high | PDF 197

Remark 4.4. Although it is less accurate than the preceding scheme while involv-

## chapter-02-section-04-pc00149 | ordinary-paragraph | high | PDF 197

ing the same number of unknowns, this last method is often preferred because it leads to better conditioned linear systems.

## chapter-02-section-04-pc00150 | subsection | high | PDF 197

4.3. The “Glowinski-Pironneau” Finite Element Method

## chapter-02-section-04-pc00151 | ordinary-paragraph | high | PDF 197

To begin with, let the dimension N be two or three. The numerical scheme discussed in this section, introduced by Glowinski & Pironneau [38], is based on a Poisson equation for the pressure. By taking the divergence of both sides of the equation:

## chapter-02-section-04-pc00152 | equation | low | PDF 197

[[FORMULA:f-p0197-02942]]

## chapter-02-section-04-pc00153 | ordinary-paragraph | high | PDF 197

and taking into account the condition divu = 0, we obtain:

## chapter-02-section-04-pc00154 | equation | low | PDF 197

[[FORMULA:f-p0197-02944]]

## chapter-02-section-04-pc00155 | ordinary-paragraph | high | PDF 197

Hence, if we know the trace p = p|, of p on J, the Stokes equations reduce to N + 1 Dirichlet problems for the Laplace operator: (4.34) Ap= i v 1. in:2 .5 ap =p» sone, (4.35) vAu=gradp—f inQ, u=0 onl. In fact, p is the major unknown of the problem. We shall show that p can be in turn determined by the constraint divu = 0. More precisely, observe that u and p can be split into two components: (4.36) u=u°+u(p), p=p° + p(p), where p° and wu® are the solutions of the Dirichlet problems: (4.37a) Ap =dvi-m®Q. p-=0 ‘on, (4.37b) vAu° = gradp?—f inQ, u°=0 on/J, and, for each boundary value g, p(g) and u(g) are the solutions of: (4.38a) APG) =—Onsto. Op (G)i =a on, (4.38b) vAu(g) = gradp(g) inQ, u(g)=0 onl. The space G of the boundary functions g is chosen so that the mapping g > p(g) defined by (4.38a) is an isomorphism from G onto the space

## chapter-02-section-04-pc00156 | equation | low | PDF 197

[[FORMULA:f-p0197-02955]]

## chapter-02-section-04-pc00157 | ordinary-paragraph | high | PDF 197

Then, since the solution u of (4.34) (4.35) must satisfy

## chapter-02-section-04-pc00158 | equation | low | PDF 197

[[FORMULA:f-p0197-02957]]

## chapter-02-section-04-pc00159 | ordinary-paragraph | high | PDF 198

or equivalently by (4.39) (div u(p), p(g)) = —(divu’,p(g)) VgeG. We are going to see below that, for a proper choice of the space G, the equation (4.39) defines a unique boundary function p. In order to choose G, let us put Problem (4.38a) in variational form. Assuming for the moment that the function p(g) is smooth enough, Green’s formula yields: (4.40) |p (g)Apdx = |g on/énds = Wue H*(Q)N HG (2). Q Vk When the boundary I is @'*', we know from Theorem I.1.6 that the mapping > Ou/én is continuous from H?(Q)N H3(Q) onto H'7(’). When I is a plane polygon, made of segments J; for 1 <j < J, Remark I.1.1 asserts that the mapping uw > (6u/0n,; 1 <j < J) is continuous from H?(Q)N Ho(@) onto [| H*? (75). These considerations suggest the following choice for G:

## chapter-02-section-04-pc00160 | equation | low | PDF 198

[[FORMULA:f-p0198-02964]]

## chapter-02-section-04-pc00161 | ordinary-paragraph | high | PDF 198

(441) G= |I T wUr)| if [is a two-dimensional polygon

## chapter-02-section-04-pc00162 | equation | low | PDF 198

[[FORMULA:f-p0198-02966]]

## chapter-02-section-04-pc00163 | ordinary-paragraph | high | PDF 198

equipped with the usual dual norm which, for the sake of simplicity, we denote in both cases by ||. ||_-1)2,r. Then, in either case, when g and p(g) are related by (4.40) we have: 1

## chapter-02-section-04-pc00164 | equation | low | PDF 198

[[FORMULA:f-p0198-02968]]

## chapter-02-section-04-pc00165 | ordinary-paragraph | high | PDF 198

we HQ) NHK@) \IHll2,e Jr ;

## chapter-02-section-04-pc00166 | equation | low | PDF 198

[[FORMULA:f-p0198-02969]]

## chapter-02-section-04-pc00167 | ordinary-paragraph | high | PDF 198

Conversely, if either [is @'*' or if Q is a convex polygon, it stems from

## chapter-02-section-04-pc00168 | remark | high | PDF 198

Remark I.1.2 that for all q in L?(Q), the problem:

## chapter-02-section-04-pc00169 | equation | low | PDF 198

[[FORMULA:f-p0198-02970]]

## chapter-02-section-04-pc00170 | ordinary-paragraph | high | PDF 198

has a unique solution uw in H?(Q)N H3(Q) and |\L\|,.o< Cy\|q|lo.o. Hence Problem (4.40) has a unique solution p(g) and 1

## chapter-02-section-04-pc00171 | equation | low | PDF 198

[[FORMULA:f-p0198-02973]]

## chapter-02-section-04-pc00172 | ordinary-paragraph | high | PDF 198

we H2(Q) 1 HA(Q) lH Il2,0 Q

## chapter-02-section-04-pc00173 | equation | low | PDF 198

[[FORMULA:f-p0198-02974]]

## chapter-02-section-04-pc00174 | ordinary-paragraph | high | PDF 198

Moreover, using the fact that Y(Q) is dense in the space

## chapter-02-section-04-pc00175 | equation | low | PDF 198

[[FORMULA:f-p0198-02975]]

## chapter-02-section-04-pc00176 | ordinary-paragraph | high | PDF 198,199

we can readily define the trace mappping y: L(4; 2) > H~"/?(L) and establish the following Green's formula for all pe L(4; Q):

## chapter-02-section-04-pc00177 | ordinary-paragraph | medium | PDF 199

()H U ()HA

## chapter-02-section-04-pc00178 | equation | low | PDF 199

[[FORMULA:f-p0199-02977]]

## chapter-02-section-04-pc00179 | ordinary-paragraph | low | PDF 199

(yp)du/onds Jr Collecting these results, we find that Problems (4.38a) and (4.40) are equivalent, have a unique solution p(g) for each g in G and

## chapter-02-section-04-pc00180 | equation | low | PDF 199

[[FORMULA:f-p0199-02979]]

## chapter-02-section-04-pc00181 | equation | low | PDF 199

[[FORMULA:f-p0199-02980]]

## chapter-02-section-04-pc00182 | ordinary-paragraph | low | PDF 199

'bA Next, we write Problem (4.38b) in variational form:

## chapter-02-section-04-pc00183 | equation | low | PDF 199

[[FORMULA:f-p0199-02981]]

## chapter-02-section-04-pc00184 | equation | low | PDF 199

[[FORMULA:f-p0199-02982]]

## chapter-02-section-04-pc00185 | ordinary-paragraph | high | PDF 199

From this and Corollary 1.2.4 we derive immediately that

## chapter-02-section-04-pc00186 | equation | low | PDF 199

[[FORMULA:f-p0199-02983]]

## chapter-02-section-04-pc00187 | equation | low | PDF 199

[[FORMULA:f-p0199-02984]]

## chapter-02-section-04-pc00188 | ordinary-paragraph | high | PDF 199

Thus, combining (4.42) and (4.44) and using the fact that

## chapter-02-section-04-pc00189 | equation | low | PDF 199

[[FORMULA:f-p0199-02986]]

## chapter-02-section-04-pc00190 | ordinary-paragraph | high | PDF 199

we obtain

## chapter-02-section-04-pc00191 | ordinary-paragraph | medium | PDF 199

C4 inf Ilg + cll-1/2,r ≤ lu(g)l,α ≤(//N/v)C, inf Ilg + cll -1/2,r

## chapter-02-section-04-pc00192 | equation | low | PDF 199

[[FORMULA:f-p0199-02988]]

## chapter-02-section-04-pc00193 | ordinary-paragraph | low | PDF 199

vNC, ceR ceR Finally, by substituting (4.43) into (4.39) we derive:

## chapter-02-section-04-pc00194 | equation | low | PDF 199

[[FORMULA:f-p0199-02990]]

## chapter-02-section-04-pc00195 | ordinary-paragraph | high | PDF 199

VleG. In other words, with the notation

## chapter-02-section-04-pc00196 | equation | low | PDF 199

[[FORMULA:f-p0199-02991]]

## chapter-02-section-04-pc00197 | equation | low | PDF 199

[[FORMULA:f-p0199-02992]]

## chapter-02-section-04-pc00198 | ordinary-paragraph | high | PDF 199

Problem (4.39) reads:

## chapter-02-section-04-pc00199 | ordinary-paragraph | high | PDF 199

Find p in G/R such that:

## chapter-02-section-04-pc00200 | equation | low | PDF 199

[[FORMULA:f-p0199-02994]]

## chapter-02-section-04-pc00201 | equation | low | PDF 199

[[FORMULA:f-p0199-02995]]

## chapter-02-section-04-pc00202 | ordinary-paragraph | low | PDF 199

Hle G/r. Clearly, in view of (4.44) and (4.45) this problem has a unique solution. Note also that the bilinear form a(., .) is symmetric.

## chapter-02-section-04-pc00203 | ordinary-paragraph | high | PDF 199

The above results are summarized in the following theorem.

## chapter-02-section-04-pc00204 | theorem | high | PDF 199

Theorem 4.5. Let N = 2 or 3. Assume that Q is bounded with either a %1.1

## chapter-02-section-04-pc00205 | ordinary-paragraph | high | PDF 199

boundary or a polygonal boundary with no reentrant corners. For f given in L?(Q)N, the solution (u, p) of the Stokes system (4.1) can be split into:

## chapter-02-section-04-pc00206 | equation | low | PDF 199

[[FORMULA:f-p0199-02999]]

## chapter-02-section-04-pc00207 | ordinary-paragraph | high | PDF 199,200

where p is the unique solution of Problem (4.47) and the pairs (u°, p°), (u(p), p(p)) The Glowinski-Pironneau scheme is a very straightforward approximation of Problems (4.37) and (4.38), on a polygonal domain 2, with the Hood-Taylor finite element spaces for the velocity and pressure:

## chapter-02-section-04-pc00208 | equation | low | PDF 200

[[FORMULA:f-p0200-03002]]

## chapter-02-section-04-pc00209 | ordinary-paragraph | high | PDF 200

The space G/R is represented by: (4.48) (Cr = Jane0 s g,(a)=90 Vnodeaof FN Q, |G .dsi— of ia Observe that, on the one hand the support of the functions of G, is a neighborhood of I’. On the other hand, the additive constant of these functions is fixed by the condition |;-q,ds = 0. In addition, we introduce the space (4.49) &, = 0, HA(Q). Note that we have the decomposition:

## chapter-02-section-04-pc00210 | equation | low | PDF 200

[[FORMULA:f-p0200-03006]]

## chapter-02-section-04-pc00211 | ordinary-paragraph | high | PDF 200

Ig With these spaces, Problems (4.37) and (4.38) are discretized as follows: Find p? € ®, such that: (4.50) (grad p;, grad q,) = (f,gradq,) Vq,€®,; Find u} € X,, such that:

## chapter-02-section-04-pc00212 | equation | low | PDF 200

[[FORMULA:f-p0200-03009]]

## chapter-02-section-04-pc00213 | ordinary-paragraph | high | PDF 200

For g,, given in G,, find p,(g),)€Q,, such that:

## chapter-02-section-04-pc00214 | equation | low | PDF 200

[[FORMULA:f-p0200-03010]]

## chapter-02-section-04-pc00215 | ordinary-paragraph | high | PDF 200

(4.51) Pi(Gn) — G, = 9 onl; Find u,(g;,€) X; , such that:

## chapter-02-section-04-pc00216 | equation | low | PDF 200

[[FORMULA:f-p0200-03012]]

## chapter-02-section-04-pc00217 | ordinary-paragraph | high | PDF 200

Finally, the boundary function p is discretized by the analogue of (4.47): Find p,,€ G,, satisfying: (4.52) v(grad u,(p,,), grad u,(/,)) = (up, grad p,(I,)) Vl,€ G,.- Then the approximate velocity and pressure calculated by the Glowinski- Pironneau scheme are: (4.53) u, =U, + U,(P,), Py = pe + Pil Pa)» where (uj, p;,) is the solution of (4.50), p, is the solution of (4.52) and (u,(p,), Pp(P;,)) 1s the solution of (4.51) for this p,,.

## chapter-02-section-04-pc00218 | ordinary-paragraph | high | PDF 201

To stress the parallel with the continuous case, we set

## chapter-02-section-04-pc00219 | equation | low | PDF 201

[[FORMULA:f-p0201-03018]]

## chapter-02-section-04-pc00220 | ordinary-paragraph | high | PDF 201

Clearly, Problem (4.50) has a unique solution, and so does Problem (4.51) for a given g,. Moreover, it is easy to check that Problem (4.52) has also a unique solution p,. Indeed, if u,(p,) = 0 then

## chapter-02-section-04-pc00221 | equation | low | PDF 201

[[FORMULA:f-p0201-03022]]

## chapter-02-section-04-pc00222 | ordinary-paragraph | high | PDF 201

But the inf-sup condition established by Corollary 4.1 implies that

## chapter-02-section-04-pc00223 | equation | low | PDF 201

[[FORMULA:f-p0201-03024]]

## chapter-02-section-04-pc00224 | ordinary-paragraph | high | PDF 201

i.e. p, is constant in Q. As p,(p,) also satisfies |p ,(p,)ds = 0 we conclude that P,(P;,) = 0 and in particular, p, = 0. Therefore we have the following result:

## chapter-02-section-04-pc00225 | lemma | high | PDF 201

Lemma 4.3. Let the right-hand side f belong to L?(Q)? where Q is a plane, bounded

## chapter-02-section-04-pc00226 | ordinary-paragraph | high | PDF 201

polygon and assume that the triangulation 7, is like in (4.17). Then the Glowinski- Pironneau scheme (4.50) ... (4.53) determines a unique pair (u,, p,) with u, in X,, and Pn in Qh, IrPn ds = 0. Moreover, the pair (u,, p;,,) satisfies: (4,54) v(grad u,, grad v,) + (grad p,,v, — grad q,)

## chapter-02-section-04-pc00227 | equation | low | PDF 201

[[FORMULA:f-p0201-03031]]

## chapter-02-section-04-pc00228 | ordinary-paragraph | high | PDF 201

Note that (4.54) amounts to two independent equations: one for u, and one for P,- Vhey are obtained by combining the last equations (resp. the first equations) of (4.50) and (4.51). It is important to point out that, although the finite element spaces coincide with those of the Hood-Taylor method and (4.54) with q,, = 0 is satisfied in both cases, the above pair (u,, p;,) is not, in general, the solution of the Hood-Taylor algorithm because it does not satisfy the discrete divergence-free constraint:

## chapter-02-section-04-pc00229 | equation | low | PDF 201

[[FORMULA:f-p0201-03035]]

## chapter-02-section-04-pc00230 | ordinary-paragraph | high | PDF 201

Indeed, it follows from (4.51) that we have:

## chapter-02-section-04-pc00231 | equation | low | PDF 201

[[FORMULA:f-p0201-03037]]

## chapter-02-section-04-pc00232 | equation | low | PDF 201

[[FORMULA:f-p0201-03038]]

## chapter-02-section-04-pc00233 | equation | low | PDF 201

[[FORMULA:f-p0201-03039]]

## chapter-02-section-04-pc00234 | ordinary-paragraph | high | PDF 201

by virtue of (4.52). Hence, another application of (4.51) shows that we have:

## chapter-02-section-04-pc00235 | equation | low | PDF 201

[[FORMULA:f-p0201-03041]]

## chapter-02-section-04-pc00236 | ordinary-paragraph | high | PDF 201,202

Unlike the continuous case, this equality does not necessarily carry over to all (4.55) (grad 4, grad q,) = (u,,gradq,) Vq,E®, then the sum u, — grad /, does satisfy:

## chapter-02-section-04-pc00237 | equation | low | PDF 202

[[FORMULA:f-p0202-03044]]

## chapter-02-section-04-pc00238 | ordinary-paragraph | high | PDF 202

Indeed, let gq, € Q,, with [-q,ds = O and let g, € G, denote the boundary value of q;:

## chapter-02-section-04-pc00239 | equation | low | PDF 202

[[FORMULA:f-p0202-03046]]

## chapter-02-section-04-pc00240 | ordinary-paragraph | high | PDF 202

Then gq, has the orthogonal decomposition (with respect to |.|;,9):

## chapter-02-section-04-pc00241 | equation | low | PDF 202

[[FORMULA:f-p0202-03047]]

## chapter-02-section-04-pc00242 | ordinary-paragraph | high | PDF 202

where q,,(g,) is the solution of (4.51) and q? e ®,. We have:

## chapter-02-section-04-pc00243 | equation | low | PDF 202

[[FORMULA:f-p0202-03049]]

## chapter-02-section-04-pc00244 | equation | low | PDF 202

[[FORMULA:f-p0202-03050]]

## chapter-02-section-04-pc00245 | equation | low | PDF 202

[[FORMULA:f-p0202-03051]]

## chapter-02-section-04-pc00246 | ordinary-paragraph | high | PDF 202

We shall see below that 4, is indeed small, so that u, is nearly “divergence-free”. In addition, although 4, has only been introduced here for a theoretical purpose, it will prove to be useful in practice for solving efficiently (4.52).

## chapter-02-section-04-pc00247 | remark | high | PDF 202

Remark 4.5. The triple (u,,, p,,4,) can also be introduced directly as the unique

## chapter-02-section-04-pc00248 | ordinary-paragraph | high | PDF 202

solution in X, x (Q,/R) x @, of:

## chapter-02-section-04-pc00249 | equation | low | PDF 202

[[FORMULA:f-p0202-03053]]

## chapter-02-section-04-pc00250 | ordinary-paragraph | high | PDF 202

V(VWan >EX , X D,,

## chapter-02-section-04-pc00251 | equation | low | PDF 202

[[FORMULA:f-p0202-03055]]

## chapter-02-section-04-pc00252 | ordinary-paragraph | high | PDF 202

But the advantage of the formulations (4.50)...(4.53) is that it appears as the solution of a sequence of decoupled Dirichlet problems for the Laplace operator. The error analysis closely resembles that of the corresponding Problem (4.5). In particular, its inf-sup condition is precisely (4.9) and therefore, Theorem 4.2 and its corollary are valid.

## chapter-02-section-04-pc00253 | theorem | high | PDF 202

Theorem 4.6. Let Q be a bounded, convex, plane polygon and suppose the right-

## chapter-02-section-04-pc00254 | ordinary-paragraph | high | PDF 202

hand side f of the Stokes Problem (4.1) belongs to L?(Q)?. If the solution (u, p) of (4.1) has the regularity:

## chapter-02-section-04-pc00255 | equation | low | PDF 202

[[FORMULA:f-p0202-03061]]

## chapter-02-section-04-pc00256 | ordinary-paragraph | high | PDF 202

and if the triangulation J, is uniformly regular and like in (4.17), we have the error estimates:

## chapter-02-section-04-pc00257 | equation | low | PDF 202

[[FORMULA:f-p0202-03063]]

## chapter-02-section-04-pc00258 | ordinary-paragraph | high | PDF 202

u — u,lia + IAnli.e eine = Puilo,a < One Olh een ae IP\k.a}

## chapter-02-section-04-pc00259 | equation | low | PDF 203

[[FORMULA:f-p0203-03065]]

## chapter-02-section-04-pc00260 | equation | low | PDF 203

[[FORMULA:f-p0203-03066]]

## chapter-02-section-04-pc00261 | equation | low | PDF 203

[[FORMULA:f-p0203-03067]]

## chapter-02-section-04-pc00262 | equation | low | PDF 203

[[FORMULA:f-p0203-03068]]

## chapter-02-section-04-pc00263 | ordinary-paragraph | high | PDF 203

where (un, Pn) is the solution of (4.50)...(4.53), An is given by (4.55) and pn is the representative of p, in L?(Q).

## chapter-02-section-04-pc00264 | proof | high | PDF 203

Proof. We have:

## chapter-02-section-04-pc00265 | equation | low | PDF 203

[[FORMULA:f-p0203-03070]]

## chapter-02-section-04-pc00266 | equation | low | PDF 203

[[FORMULA:f-p0203-03071]]

## chapter-02-section-04-pc00267 | ordinary-paragraph | low | PDF 203

(vh,gn)∈ Xh x Dn, "O"bA

## chapter-02-section-04-pc00268 | equation | low | PDF 203

[[FORMULA:f-p0203-03072]]

## chapter-02-section-04-pc00269 | ordinary-paragraph | high | PDF 203

Let us restrict the pair (vh 9h) to the space:

## chapter-02-section-04-pc00270 | equation | low | PDF 203

[[FORMULA:f-p0203-03073]]

## chapter-02-section-04-pc00271 | ordinary-paragraph | high | PDF 203

Note that (u,, A,)e B,. Then (4.59) reads:

## chapter-02-section-04-pc00272 | equation | low | PDF 203

[[FORMULA:f-p0203-03075]]

## chapter-02-section-04-pc00273 | ordinary-paragraph | low | PDF 203

(vh,qh)∈ Bh, ."0uA To get rid of grad qh, we choose μ, = Php, the H'-projection of p on M, defined by (A.25). Hence (Vh,Ih)e Bh.

## chapter-02-section-04-pc00274 | equation | low | PDF 203

[[FORMULA:f-p0203-03077]]

## chapter-02-section-04-pc00275 | ordinary-paragraph | high | PDF 203

As (u, ,)e B, this equation readily implies:

## chapter-02-section-04-pc00276 | equation | low | PDF 203

[[FORMULA:f-p0203-03078]]

## chapter-02-section-04-pc00277 | ordinary-paragraph | low | PDF 203

V(wh, Ih)e Bh. Clearly, we may choose here the pair (w, 0) with w, in V, and since the spaces (Xh, M,) satisfy the inf-sup condition (4.9) we can apply (1.16):

## chapter-02-section-04-pc00278 | equation | low | PDF 203

[[FORMULA:f-p0203-03080]]

## chapter-02-section-04-pc00279 | ordinary-paragraph | low | PDF 203

WneVn VhEXn As a consequence,

## chapter-02-section-04-pc00280 | ordinary-paragraph | low | PDF 203

[u - ul1.o ≤ 2(1 + √/2/β*) inf ↓u -vnl1,α + (2/v) llp -- Phpllo,2, VnE Xh and the velocity bound in (4.56) follows from (4.16) and (A.26). Notice that it is (A.26) alone which requires the convexity of Q and the uniform regularity of h.

## chapter-02-section-04-pc00281 | ordinary-paragraph | high | PDF 203

The bound for A, is obtained from the above inequality and the fact that div u = 0:

## chapter-02-section-04-pc00282 | equation | low | PDF 203

[[FORMULA:f-p0203-03084]]

## chapter-02-section-04-pc00283 | equation | low | PDF 203

[[FORMULA:f-p0203-03085]]

## chapter-02-section-04-pc00284 | equation | low | PDF 203

[[FORMULA:f-p0203-03086]]

## chapter-02-section-04-pc00285 | ordinary-paragraph | high | PDF 203

Therefore

## chapter-02-section-04-pc00286 | equation | low | PDF 203

[[FORMULA:f-p0203-03087]]

## chapter-02-section-04-pc00287 | ordinary-paragraph | high | PDF 204

Glam):

## chapter-02-section-04-pc00288 | equation | low | PDF 204

[[FORMULA:f-p0204-03088]]

## chapter-02-section-04-pc00289 | ordinary-paragraph | high | PDF 204

qne My, This yields (4.56); in turn a familiar argument gives (4.57). Finally we establish an L?-estimate for the velocity. The proof is an easy variant of that of Theorem 1.2. As Q is convex, there exists a unique pair (4, 1) in [VN H?7(Q)?] x [H1(Q)N LZ(Q)] such that

## chapter-02-section-04-pc00290 | equation | low | PDF 204

[[FORMULA:f-p0204-03090]]

## chapter-02-section-04-pc00291 | equation | low | PDF 204

[[FORMULA:f-p0204-03091]]

## chapter-02-section-04-pc00292 | equation | low | PDF 204

[[FORMULA:f-p0204-03092]]

## chapter-02-section-04-pc00293 | ordinary-paragraph | high | PDF 204

Combining this equality with (4.59) we readily derive:

## chapter-02-section-04-pc00294 | equation | low | PDF 204

[[FORMULA:f-p0204-03094]]

## chapter-02-section-04-pc00295 | equation | low | PDF 204

[[FORMULA:f-p0204-03095]]

## chapter-02-section-04-pc00296 | ordinary-paragraph | high | PDF 204

—(g,gradi,) YVo,EX,, Vq,EQh.- (Here we use the fact that 4u = divg in Q). Therefore choosing q, = P, we obtain: (g,u —u, + grad /,,) = v(grad( — @,), grad(u — u,)) + (p — p,, div(, — ))

## chapter-02-section-04-pc00297 | equation | low | PDF 204

[[FORMULA:f-p0204-03098]]

## chapter-02-section-04-pc00298 | ordinary-paragraph | high | PDF 204

In view of (4.56) and (4.61) this yields (4.58). O

## chapter-02-section-04-pc00299 | remark | high | PDF 204

Remark 4.6. It does not appear possible to find an L? bound like (4.58) for u — u,

## chapter-02-section-04-pc00300 | ordinary-paragraph | high | PDF 204

alone. On the contrary, (4.60) implies that

## chapter-02-section-04-pc00301 | equation | low | PDF 204

[[FORMULA:f-p0204-03102]]

## chapter-02-section-04-pc00302 | ordinary-paragraph | high | PDF 204

so that neither u — u, nor A, can be isolated from (4.58). But this is not surprising since 4, acts as a correction on the velocity u,. The same analysis can be applied when X,, is defined by (4.30) (and M,, is unchanged). Because of (4.31), the statement of Theorem 4.6 holds only with eve

## chapter-02-section-04-pc00303 | subsection | high | PDF 204

4.4. Implementation of the Glowinski-Pironneau Scheme

## chapter-02-section-04-pc00304 | ordinary-paragraph | high | PDF 204

It is not absolutely straightforward to compute the solution of (4.50) (4.51) (4.52) because the test function |, does not appear explicitly in the left-hand side of (4.52). It is easier to split the computation by calculating the auxiliary function A, defined by (4.55), that compensates for the fact that u, does not satisfy the discrete divergence-free constraint.

## chapter-02-section-04-pc00305 | ordinary-paragraph | low | PDF 205

To be specific, following the pattern of the equations (4.50) and (4.51), let us define An(gn) and x by: ∈ Pn, VahE Φh,

## chapter-02-section-04-pc00306 | equation | low | PDF 205

[[FORMULA:f-p0205-03110]]

## chapter-02-section-04-pc00307 | equation | low | PDF 205

[[FORMULA:f-p0205-03111]]

## chapter-02-section-04-pc00308 | ordinary-paragraph | low | PDF 205

VaheΦn.

## chapter-02-section-04-pc00309 | equation | low | PDF 205

[[FORMULA:f-p0205-03112]]

## chapter-02-section-04-pc00310 | ordinary-paragraph | medium | PDF 205

Then

## chapter-02-section-04-pc00311 | equation | low | PDF 205

[[FORMULA:f-p0205-03113]]

## chapter-02-section-04-pc00312 | ordinary-paragraph | medium | PDF 205

and we have an alternate expression for the bilinear form a,( ., .).

## chapter-02-section-04-pc00313 | lemma | medium | PDF 205

Lemma 4.4. We have:

## chapter-02-section-04-pc00314 | ordinary-paragraph | medium | PDF 205

Agh, Ihe Gn.

## chapter-02-section-04-pc00315 | equation | low | PDF 205

[[FORMULA:f-p0205-03114]]

## chapter-02-section-04-pc00316 | equation | low | PDF 205

[[FORMULA:f-p0205-03115]]

## chapter-02-section-04-pc00317 | ordinary-paragraph | medium | PDF 205

Likewise, the right-hand side of (4.52) reads:

## chapter-02-section-04-pc00318 | equation | low | PDF 205

[[FORMULA:f-p0205-03117]]

## chapter-02-section-04-pc00319 | ordinary-paragraph | low | PDF 205

Hlhe Gh.

## chapter-02-section-04-pc00320 | equation | low | PDF 205

[[FORMULA:f-p0205-03118]]

## chapter-02-section-04-pc00321 | proof | medium | PDF 205

Proof. By definition and (4.51) we have:

## chapter-02-section-04-pc00322 | equation | low | PDF 205

[[FORMULA:f-p0205-03120]]

## chapter-02-section-04-pc00323 | equation | low | PDF 205

[[FORMULA:f-p0205-03121]]

## chapter-02-section-04-pc00324 | equation | low | PDF 205

[[FORMULA:f-p0205-03122]]

## chapter-02-section-04-pc00325 | ordinary-paragraph | medium | PDF 205

by (4.62). Then (4.51) implies that

## chapter-02-section-04-pc00326 | equation | low | PDF 205

[[FORMULA:f-p0205-03124]]

## chapter-02-section-04-pc00327 | ordinary-paragraph | low | PDF 205

thus proving (4.63). The proof of (4.64) is similar. Hence the Problem (4.52) takes the more manageable form: Find p, in G, such that: (4.65) (gradA,(Pn) - un(Pn), grad Ih) = (grad A --u%,grad In) Vlhe Gh. From the preceding lemma and the definition of the bilinear form a,(., .) we know that the left-hand side of (4.65) is a bilinear, symmetric and positive definite form on G, x G,. Let us show briefly how (4.65) is solved in practice; the reader will find more details in Glowinski et al., Chapter 13 [37]. Assume that the nodes of , N I are numbered from 1 to N, and let {μ}1<i≤Nn be the set of basis functions of Q, defined by:

## chapter-02-section-04-pc00328 | equation | low | PDF 205

[[FORMULA:f-p0205-03131]]

## chapter-02-section-04-pc00329 | equation | low | PDF 205

[[FORMULA:f-p0205-03132]]

## chapter-02-section-04-pc00330 | equation | low | PDF 206

[[FORMULA:f-p0206-03133]]

## chapter-02-section-04-pc00331 | equation | low | PDF 206

[[FORMULA:f-p0206-03134]]

## chapter-02-section-04-pc00332 | ordinary-paragraph | high | PDF 206

With this notation, (4.65) is equivalent to: Nn

## chapter-02-section-04-pc00333 | equation | low | PDF 206

[[FORMULA:f-p0206-03136]]

## chapter-02-section-04-pc00334 | equation | low | PDF 206

[[FORMULA:f-p0206-03137]]

## chapter-02-section-04-pc00335 | ordinary-paragraph | high | PDF 206

In other words we have to solve the system of linear equations: (4.66) A,p =b where

## chapter-02-section-04-pc00336 | equation | low | PDF 206

[[FORMULA:f-p0206-03139]]

## chapter-02-section-04-pc00337 | equation | low | PDF 206

[[FORMULA:f-p0206-03140]]

## chapter-02-section-04-pc00338 | ordinary-paragraph | high | PDF 206

To compute b, we have to solve the three Dirichlet problems (4.50) to find up plus the first Dirichlet problem (4.62) to obtain 4?—a total of four Dirichlet problems. To compute the j‘" column of the matrix A, we must solve the three Dirichlet problems (4.51) with g, = yu; to find u,(u;) plus the second problem (4.62) to get ,(4;)—again a total of four Dirichlet problems. From the above considerations, it follows that the matrix A, is symmetric and semi-positive definite with zero as a simple eigenvalue. Furthermore, when the nodes of Y, are properly numbered, it can be shown that Ker(A,) is the constant vector and that the principal block A, = (a,(Hj , Hi))1 <i,j<w,,-1 18 positive definite. Therefore, setting py, = 0, we can solve (4.66) by the Cholesky factorisation for the first N, — 1 components of a representative p of p. Then the solution pn Of (4.65) that satisfies | p,ds = 0 is given by: P, — (1/meas(I’)) a ds. Once p,, is known, the pressure p,(,,) and velocity u,(p,) are computed by solving the three Dirichlet problems (4.51). The problem (4.65) can also be solved by the conjugate-gradient algorithm (cf. Glowinski et al. loc. cit.).
