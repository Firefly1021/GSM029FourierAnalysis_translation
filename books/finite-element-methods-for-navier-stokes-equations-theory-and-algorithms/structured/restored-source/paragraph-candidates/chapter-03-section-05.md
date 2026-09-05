# Paragraph candidates: chapter-03-section-05

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-03-section-05-pc00001 | remark | high | PDF 271

Remark 4.7. Of course, we can use here a continuous approximation of the

## chapter-03-section-05-pc00002 | ordinary-paragraph | high | PDF 271

pressure analogous to (2.36), but the error analysis of the corresponding scheme is more delicate.

## chapter-03-section-05-pc00003 | section | high | PDF 271

§5. A “Vector Potential-Vorticity” Scheme in Three

## chapter-03-section-05-pc00004 | ordinary-paragraph | high | PDF 271

Dimensions It is not easy to adapt the schemes developed in the previous paragraphs to the three-dimensional Stokes problem. The obvious reason is that the conditions determining the vector potential are more intricate than those defining the two-dimensional stream function. Therefore we shall only attempt to extend to the homogeneous Stokes problem in a very simple region of R° the “stream function-vorticity” scheme of § 2.

## chapter-03-section-05-pc00005 | ordinary-paragraph | high | PDF 271

Throughout this paragraph, we shall assume that Q is a bounded, simplyconnected open subset of R? with a polyhedral connected bounded I. Leaving the approximation of the pressure to the last section, our first object is to relax the regularity of the function spaces related to the biharmonic problems of Section 1.5.3. The reader will discover that it suffices to work with functions in H(curl; Q). This approach will lead to the construction of finite-dimensional subspaces of conforming finite elements in H(curl; Q), which are not subspaces of H'(Q)’. Finally, since discontinuous elements are used it is reasonable to use a discontinuous approximation of the pressure, very similar to that of Section 4.4.

## chapter-03-section-05-pc00006 | subsection | high | PDF 271

5.1. A Mixed Formulation of the Three-Dimensional Stokes Problem

## chapter-03-section-05-pc00007 | ordinary-paragraph | high | PDF 271

Let f be a given vector of L?(Q)? and consider the homogeneous Stokes Problem: Find (u, p) in H*(Q)> x L6(Q) satisfying:

## chapter-03-section-05-pc00008 | equation | low | PDF 271

[[FORMULA:f-p0271-04341]]

## chapter-03-section-05-pc00009 | ordinary-paragraph | low | PDF 271,272

in Q, (5.1) divu=0 u— 0 Tonl. biharmonic We have seen in Section I.5.3 that this problem can be interpreted as a problem for the vector potential y of u (recall that u = curl y) where w belongs to the space: (5.2) YW = {pe L7(Q); divde H'(Q), cuper Hyl(@)° *, @ x np = OF. order to derive a mixed formulation of Problem (5.1), let us multiply both In with curl and determine exactly what properties we require of @. sides of (5.1) ()HA(

## chapter-03-section-05-pc00010 | equation | low | PDF 272

[[FORMULA:f-p0272-04348]]

## chapter-03-section-05-pc00011 | ordinary-paragraph | high | PDF 272

where < ., . > denotes the duality between Ho(curl; Ω) and its dual space. Now, let us set

## chapter-03-section-05-pc00012 | equation | low | PDF 272

[[FORMULA:f-p0272-04350]]

## chapter-03-section-05-pc00013 | equation | low | PDF 272

[[FORMULA:f-p0272-04351]]

## chapter-03-section-05-pc00014 | ordinary-paragraph | low | PDF 272

and assume that o e H(curl; Ω); then we have ()HA

## chapter-03-section-05-pc00015 | equation | low | PDF 272

[[FORMULA:f-p0272-04353]]

## chapter-03-section-05-pc00016 | ordinary-paragraph | high | PDF 272

Finally, since

## chapter-03-section-05-pc00017 | equation | low | PDF 272

[[FORMULA:f-p0272-04354]]

## chapter-03-section-05-pc00018 | ordinary-paragraph | low | PDF 272

equation (5.3) can be written equivalently as: E()TA

## chapter-03-section-05-pc00019 | equation | low | PDF 272

[[FORMULA:f-p0272-04356]]

## chapter-03-section-05-pc00020 | ordinary-paragraph | medium | PDF 272

And by restricting μ to H(curl; Ω) this becomes: ()HA

## chapter-03-section-05-pc00021 | equation | low | PDF 272

[[FORMULA:f-p0272-04358]]

## chapter-03-section-05-pc00022 | ordinary-paragraph | high | PDF 272

Hence, summing up we see that the following Problem (Q): Find a pair (y,?)e Ho(curl; Q) x H(curl; Q) such that:

## chapter-03-section-05-pc00023 | equation | low | PDF 272

[[FORMULA:f-p0272-04360]]

## chapter-03-section-05-pc00024 | equation | low | PDF 272

[[FORMULA:f-p0272-04361]]

## chapter-03-section-05-pc00025 | equation | low | PDF 272

[[FORMULA:f-p0272-04362]]

## chapter-03-section-05-pc00026 | equation | low | PDF 272

[[FORMULA:f-p0272-04363]]

## chapter-03-section-05-pc00027 | ordinary-paragraph | low | PDF 272

()HA (

## chapter-03-section-05-pc00028 | equation | low | PDF 272

[[FORMULA:f-p0272-04364]]

## chapter-03-section-05-pc00029 | equation | low | PDF 272

[[FORMULA:f-p0272-04365]]

## chapter-03-section-05-pc00030 | ordinary-paragraph | high | PDF 272

has at least one solution (w, w = -- 4w) where u = curl y and y e Y. Conversely, it is easy to check that this problem has at most one solution. Indeed, if

## chapter-03-section-05-pc00031 | equation | low | PDF 272

[[FORMULA:f-p0272-04367]]

## chapter-03-section-05-pc00032 | ordinary-paragraph | low | PDF 272

0 = o Aeaissons io m ('s) ui m = n pue  =  susoouo u curl y = 0. Since div y = O and F has only one connected component this implies that y = 0 (cf. Remark 1.3.9). Therefore, we have proved the following result:

## chapter-03-section-05-pc00033 | theorem | high | PDF 272

Theorem 5.1. Assume that the solution u of Problem (5.1) satisfies

## chapter-03-section-05-pc00034 | equation | low | PDF 272

[[FORMULA:f-p0272-04372]]

## chapter-03-section-05-pc00035 | ordinary-paragraph | high | PDF 272

Then Problem (5.4) (5.5) (5.6) has the unique solution:

## chapter-03-section-05-pc00036 | equation | low | PDF 272

[[FORMULA:f-p0272-04374]]

## chapter-03-section-05-pc00037 | ordinary-paragraph | high | PDF 272

Now we want to insert Problem (Q) into the framework of Section 1.1. We set

## chapter-03-section-05-pc00038 | equation | low | PDF 272

[[FORMULA:f-p0272-04375]]

## chapter-03-section-05-pc00039 | ordinary-paragraph | medium | PDF 272,273

Clearly, Problem (Q) is equivalent to: VpeΦo,

## chapter-03-section-05-pc00040 | equation | low | PDF 273

[[FORMULA:f-p0273-04376]]

## chapter-03-section-05-pc00041 | equation | low | PDF 273

[[FORMULA:f-p0273-04377]]

## chapter-03-section-05-pc00042 | equation | low | PDF 273

[[FORMULA:f-p0273-04378]]

## chapter-03-section-05-pc00043 | ordinary-paragraph | low | PDF 273

( )Ha Next, we introduce:

## chapter-03-section-05-pc00044 | equation | low | PDF 273

[[FORMULA:f-p0273-04379]]

## chapter-03-section-05-pc00045 | equation | low | PDF 273

[[FORMULA:f-p0273-04380]]

## chapter-03-section-05-pc00046 | equation | low | PDF 273

[[FORMULA:f-p0273-04381]]

## chapter-03-section-05-pc00047 | equation | low | PDF 273

[[FORMULA:f-p0273-04382]]

## chapter-03-section-05-pc00048 | equation | low | PDF 273

[[FORMULA:f-p0273-04383]]

## chapter-03-section-05-pc00049 | equation | low | PDF 273

[[FORMULA:f-p0273-04384]]

## chapter-03-section-05-pc00050 | equation | low | PDF 273

[[FORMULA:f-p0273-04385]]

## chapter-03-section-05-pc00051 | equation | low | PDF 273

[[FORMULA:f-p0273-04386]]

## chapter-03-section-05-pc00052 | equation | low | PDF 273

[[FORMULA:f-p0273-04387]]

## chapter-03-section-05-pc00053 | ordinary-paragraph | medium | PDF 273

With this notation, Problem (Q) takes the more familiar form: Find a pair (u, X) in X × M such that: VueX,

## chapter-03-section-05-pc00054 | equation | low | PDF 273

[[FORMULA:f-p0273-04388]]

## chapter-03-section-05-pc00055 | equation | low | PDF 273

[[FORMULA:f-p0273-04389]]

## chapter-03-section-05-pc00056 | ordinary-paragraph | medium | PDF 273

Wue M.

## chapter-03-section-05-pc00057 | equation | low | PDF 273

[[FORMULA:f-p0273-04390]]

## chapter-03-section-05-pc00058 | ordinary-paragraph | medium | PDF 273

As usual, the space V is defined by:

## chapter-03-section-05-pc00059 | equation | low | PDF 273

[[FORMULA:f-p0273-04391]]

## chapter-03-section-05-pc00060 | ordinary-paragraph | medium | PDF 273

i.e.

## chapter-03-section-05-pc00061 | equation | low | PDF 273

[[FORMULA:f-p0273-04392]]

## chapter-03-section-05-pc00062 | ordinary-paragraph | low | PDF 273

{( )H A Since the mapping Φ -→ llcurl Φ lio,o is a norm on Φ。 equivalent to the norm of H(curl; Ω) (cf. Lemma I.3.4): V$e Po,

## chapter-03-section-05-pc00063 | equation | low | PDF 273

[[FORMULA:f-p0273-04394]]

## chapter-03-section-05-pc00064 | equation | low | PDF 273

[[FORMULA:f-p0273-04395]]

## chapter-03-section-05-pc00065 | ordinary-paragraph | medium | PDF 273

it follows that on the one hand we can choose the following norm on X:

## chapter-03-section-05-pc00066 | equation | low | PDF 273

[[FORMULA:f-p0273-04396]]

## chapter-03-section-05-pc00067 | equation | low | PDF 273

[[FORMULA:f-p0273-04397]]

## chapter-03-section-05-pc00068 | ordinary-paragraph | medium | PDF 273

and on the other hand we have:

## chapter-03-section-05-pc00069 | equation | low | PDF 273

[[FORMULA:f-p0273-04398]]

## chapter-03-section-05-pc00070 | equation | low | PDF 273

[[FORMULA:f-p0273-04399]]

## chapter-03-section-05-pc00071 | equation | low | PDF 273

[[FORMULA:f-p0273-04400]]

## chapter-03-section-05-pc00072 | ordinary-paragraph | low | PDF 273

Hence the mapping v = (curl Φ,0) → I/0llo.s is a norm on V equivalent to the norm of x:

## chapter-03-section-05-pc00073 | equation | low | PDF 273

[[FORMULA:f-p0273-04402]]

## chapter-03-section-05-pc00074 | ordinary-paragraph | medium | PDF 273

and we set:

## chapter-03-section-05-pc00075 | equation | low | PDF 273

[[FORMULA:f-p0273-04403]]

## chapter-03-section-05-pc00076 | ordinary-paragraph | medium | PDF 273

As a consequence, the form a( ., .) is V-elliptic:

## chapter-03-section-05-pc00077 | ordinary-paragraph | medium | PDF 273

Vue V,

## chapter-03-section-05-pc00078 | equation | low | PDF 273

[[FORMULA:f-p0273-04404]]

## chapter-03-section-05-pc00079 | ordinary-paragraph | medium | PDF 273

with & = v/(C² + 1).

## chapter-03-section-05-pc00080 | ordinary-paragraph | high | PDF 274

condition:

## chapter-03-section-05-pc00081 | equation | low | PDF 274

[[FORMULA:f-p0274-04406]]

## chapter-03-section-05-pc00082 | ordinary-paragraph | high | PDF 274

veX Finally, we readily derive that here the Lagrange multiplier 4 satisfies 4 = vo.

## chapter-03-section-05-pc00083 | remark | high | PDF 274

Remark 5.1. Observe the analogy between Problem (5.7) and Problem (2.20) in

## chapter-03-section-05-pc00084 | ordinary-paragraph | high | PDF 274

two dimensions.

## chapter-03-section-05-pc00085 | remark | high | PDF 274

Remark 5.2. Note that the first equation of (5.8) holds on a larger space than xe

## chapter-03-section-05-pc00086 | equation | low | PDF 274

[[FORMULA:f-p0274-04410]]

## chapter-03-section-05-pc00087 | equation | low | PDF 274

[[FORMULA:f-p0274-04411]]

## chapter-03-section-05-pc00088 | subsection | high | PDF 274

5.2. Mixed Approximation in H (curl; Q2)

## chapter-03-section-05-pc00089 | ordinary-paragraph | high | PDF 274

The statement of Problem (Q) induces us to define its approximation in finitedimensional subspaces of H(curl; 2). Thus, we introduce three finite-dimensional spaces: (Geil) ®, < H,(curl;2), M, < H(curl;Q), 0, < H3(Q) and we assume that

## chapter-03-section-05-pc00090 | equation | low | PDF 274

[[FORMULA:f-p0274-04415]]

## chapter-03-section-05-pc00091 | ordinary-paragraph | high | PDF 274

Since &, is not necessarily contained in H(div; Q), the divergence-free condition is expressed by: (5.12) (,,gradq,)=90 YVq,€O,. In other words, the space ®, is approximated by: (S213) Pio = (0, € ®,; o,, satisfies (5.12)}, which, in general, is not contained in ©). Nevertheless, it is reasonable to ask that the functions of ®, 9s atisfy the same equivalence of norms as ®,, namely: there exists a positive constant C* > 0 such that: (5.14) IPillo.e < C*lleurl Oy |lo.o VO, Dyo- With these spaces, we propose the following approximation of Problem (5.7) called Problem (Q,):

## chapter-03-section-05-pc00092 | equation | low | PDF 274

[[FORMULA:f-p0274-04422]]

## chapter-03-section-05-pc00093 | equation | low | PDF 274

[[FORMULA:f-p0274-04423]]

## chapter-03-section-05-pc00094 | ordinary-paragraph | high | PDF 274

(5:15)

## chapter-03-section-05-pc00095 | equation | low | PDF 274

[[FORMULA:f-p0274-04424]]

## chapter-03-section-05-pc00096 | ordinary-paragraph | high | PDF 275

following approximation of Problem (Q) which works with the entire space ©, Find a pair (W,,, @),)€ Pyo < My, satisfying:

## chapter-03-section-05-pc00097 | equation | low | PDF 275

[[FORMULA:f-p0275-04426]]

## chapter-03-section-05-pc00098 | equation | low | PDF 275

[[FORMULA:f-p0275-04427]]

## chapter-03-section-05-pc00099 | equation | low | PDF 275

[[FORMULA:f-p0275-04428]]

## chapter-03-section-05-pc00100 | ordinary-paragraph | high | PDF 275

Obviously, it is desirable that these two problems be equivalent; but this requires an additional hypothesis: for each function ,, of &, there exists a function Ojo Of Pyo with (5.17) curl o, = curl d, 0. Clearly, (5.17) implies the equivalence between Problems (5.15) and (5.16). As far as the solution of these problems is concerned, uniqueness implies existence, for (5.15) is a square system of linear equations. Like in the continuous case, we readily infer this existence from (5.14) and the inclusion ®, < M,. Hence we have the following result.

## chapter-03-section-05-pc00101 | lemma | high | PDF 275

Lemma 5.1. Let the spaces ®,, M,, and @,, satisfy (5.11) with ®, < M,, and let ®,o

## chapter-03-section-05-pc00102 | ordinary-paragraph | high | PDF 275

be defined by (5.13). Under the hypothesis (5.14), Problem (Q,) has a unique solution (w,,@,)in ®,. x M,,. If, in addition the hypothesis (5.17) holds, then Problem (5.16) is equivalent to Problem (Q,). It is possible to derive directly an error bound for the solution of (Q,), but it is easier and more satisfactory to place this problem into the setting of Section 1.2 and use Theorem 1.2. Here, there is a slight difficulty because the natural discretization of X: (curl ®,,) x M,, is not contained in X. However we can make use of Remark 5.2 and observe that the crucial spaces of Problem (5.8) are in fact H,( curl; Q) x L?(Q)° and V. Thus, we take (5.18) X, = feurldy; b,€ Dio} x M, < {curl; o € Ho(curlQ;) } x L?(Q)?, (5.19) V, = {(curl o,, ,) € X;,; (curl p,, curl w,) = (0, Mi) Vine My}. Ofc ourse, V, is generally not included in V but if ®, < M, and if (5.14) holds then we have the analogue of( 5.10): (5.20) curl, |lo,0 < C*|9pllo,0 Wn = (curl, 0,)€ Vi, which means that the mapping v,= (curl o,,9,) > || 9\;/ o,0 = Um 1s. an equivalent norm on J,. With this notation, Problem (Q,,) becomes: Find a pair (uj, 4,)€X }, X M,, such that

## chapter-03-section-05-pc00103 | equation | low | PDF 275

[[FORMULA:f-p0275-04444]]

## chapter-03-section-05-pc00104 | equation | low | PDF 275

[[FORMULA:f-p0275-04445]]

## chapter-03-section-05-pc00105 | ordinary-paragraph | high | PDF 276

solution u, = (curl y,, @,) of Problem (Q,,) satisfies the error estimate: (5.21) ||@ — @llo,o <2 inf |u—v,|+ (1+ C**)? inf |l}o — pyllaceurt2 ) vaeVy, Phe My,

## chapter-03-section-05-pc00106 | equation | low | PDF 276

[[FORMULA:f-p0276-04448]]

## chapter-03-section-05-pc00107 | ordinary-paragraph | high | PDF 276

(5.22) e .

## chapter-03-section-05-pc00108 | equation | low | PDF 276

[[FORMULA:f-p0276-04450]]

## chapter-03-section-05-pc00109 | ordinary-paragraph | high | PDF 276

vneVy, Hnpe My, where C* is the constant of (5.14). Like in the two-dimensional case, we are now faced with the evaluation of the approximation error of V,: inf, -y, ||u — U,||z- It is easy to see that the statement of Lemma 3.1 is still valid here.

## chapter-03-section-05-pc00110 | lemma | high | PDF 276

Lemma 5.2. With the notations of Lemma 5.1 we have the upper bound for all

## chapter-03-section-05-pc00111 | ordinary-paragraph | high | PDF 276

v = (curl d, 0) V:

## chapter-03-section-05-pc00112 | equation | low | PDF 276

[[FORMULA:f-p0276-04454]]

## chapter-03-section-05-pc00113 | ordinary-paragraph | high | PDF 276

inf |v — w,| < inf {2k— v,| + sup Guid mt wneVn vp=(curl b;,,9;,)eXy, ,e My, IlP a llo.e

## chapter-03-section-05-pc00114 | equation | low | PDF 276

[[FORMULA:f-p0276-04457]]

## chapter-03-section-05-pc00115 | ordinary-paragraph | high | PDF 276

and a similar upper bound for ||v — w, || with the norm |.| replaced by ||. ||z i n the right-hand side side of (5.23).

## chapter-03-section-05-pc00116 | subsection | high | PDF 276

5.3. A Family of Conforming Finite Elements in H (curl; Q)

## chapter-03-section-05-pc00117 | ordinary-paragraph | high | PDF 276

In this section, we present a space of finite elements developed by Nédélec [59, 60]. Its construction is by no means straightforward, inasmuch as it requires exactly the continuity of the tangential components at element interfaces. This implies that we must work with incomplete spaces of polynomials of (say) degree l, for some integer / > 1. Let P, denote the space of homogeneous polynomials of degree | in R? and consider the following subspaces of P;:

## chapter-03-section-05-pc00118 | equation | low | PDF 276

[[FORMULA:f-p0276-04461]]

## chapter-03-section-05-pc00119 | equation | low | PDF 276

[[FORMULA:f-p0276-04462]]

## chapter-03-section-05-pc00120 | ordinary-paragraph | high | PDF 276

R, ae PS CD) Si. Examples. Let us exhibit S, and S,. Clearly, all homogeneous polynomial vectors of degree one that satisfy p(x): x = 0 must necessarily be of the form:

## chapter-03-section-05-pc00121 | equation | low | PDF 276

[[FORMULA:f-p0276-04464]]

## chapter-03-section-05-pc00122 | ordinary-paragraph | high | PDF 276

where @ is an arbitrary vector of R*. Thus, S, has the basis:

## chapter-03-section-05-pc00123 | equation | low | PDF 276

[[FORMULA:f-p0276-04465]]

## chapter-03-section-05-pc00124 | equation | low | PDF 276

[[FORMULA:f-p0276-04466]]

## chapter-03-section-05-pc00125 | ordinary-paragraph | high | PDF 277

form: 3

## chapter-03-section-05-pc00126 | equation | low | PDF 277

[[FORMULA:f-p0277-04467]]

## chapter-03-section-05-pc00127 | equation | low | PDF 277

[[FORMULA:f-p0277-04468]]

## chapter-03-section-05-pc00128 | ordinary-paragraph | high | PDF 277

But the nine polynomials x;p,(x) are not all linearly independent, for they are linked by one relation:

## chapter-03-section-05-pc00129 | equation | low | PDF 277

[[FORMULA:f-p0277-04469]]

## chapter-03-section-05-pc00130 | ordinary-paragraph | high | PDF 277

ee

## chapter-03-section-05-pc00131 | equation | low | PDF 277

[[FORMULA:f-p0277-04470]]

## chapter-03-section-05-pc00132 | ordinary-paragraph | high | PDF 277

Thus we can suppress one of these polynomials and it can be readily checked that the remaining eight are linearly independent. For example, we can take for S, the following eight basis functions: X;Pi, X2Pi, X3Pi, %1P2, %2P2, X3P2, %1P3, %X2Ps- The space R, has the following attractive property.

## chapter-03-section-05-pc00133 | lemma | high | PDF 277

Lemma 5.3. If the vector field ue R, satisfies curlu = 0 then

## chapter-03-section-05-pc00134 | equation | low | PDF 277

[[FORMULA:f-p0277-04472]]

## chapter-03-section-05-pc00135 | proof | high | PDF 277

Proof. First observe that each fe P, satisfies

## chapter-03-section-05-pc00136 | equation | low | PDF 277

[[FORMULA:f-p0277-04473]]

## chapter-03-section-05-pc00137 | ordinary-paragraph | high | PDF 277

Now, we know that u = gradp with pe P,,,. Therefore, the term in gradp that belongs to S, vanishes according to the definition (5.24). Hence p has no term of degree / + 1. o

## chapter-03-section-05-pc00138 | remark | high | PDF 277

Remark 5.3. The definition of R, can obviously be extended to an arbitrary

## chapter-03-section-05-pc00139 | ordinary-paragraph | high | PDF 277

dimension N. Then the statement of Lemma 5.3 is also valid for all dimensions.

## chapter-03-section-05-pc00140 | ordinary-paragraph | high | PDF 277

CO

## chapter-03-section-05-pc00141 | definition | high | PDF 277

Definition 5.1. Let « be a tetrahedron in R* with edges denoted by e and faces

## chapter-03-section-05-pc00142 | ordinary-paragraph | high | PDF 277

by f and let u be a function in W''‘(x)* for some s > 2. We define the three sets of moments of u on k:

## chapter-03-section-05-pc00143 | equation | low | PDF 277

[[FORMULA:f-p0277-04477]]

## chapter-03-section-05-pc00144 | ordinary-paragraph | high | PDF 277

where t denotes the unit vector of e;

## chapter-03-section-05-pc00145 | ordinary-paragraph | high | PDF 277

M,(u) = 1|( uxn)-qds VqeP2,(f) for all aces fof x} i

## chapter-03-section-05-pc00146 | equation | low | PDF 277

[[FORMULA:f-p0277-04479]]

## chapter-03-section-05-pc00147 | ordinary-paragraph | high | PDF 278

more regularity than H'(x)> because M,(u) makes no sense when u is only in H(i). These definitions will enable us to construct conforming finite elements in H (curl; Q) provided that on the one hand, the above set of moments is unisolvent on R, and on the other hand, the moments M, and M, determine entirely the tangential components of polynomials of R,. This is achieved in the next lemmas.

## chapter-03-section-05-pc00148 | lemma | high | PDF 278

Lemma 5.4. The total number of moments in Definition 5.1 is equal to N,, the

## chapter-03-section-05-pc00149 | ordinary-paragraph | high | PDF 278

dimension of R;:

## chapter-03-section-05-pc00150 | equation | low | PDF 278

[[FORMULA:f-p0278-04482]]

## chapter-03-section-05-pc00151 | proof | high | PDF 278

Proof. In view of Definition 5.1, we have:

## chapter-03-section-05-pc00152 | equation | low | PDF 278

[[FORMULA:f-p0278-04483]]

## chapter-03-section-05-pc00153 | equation | low | PDF 278

[[FORMULA:f-p0278-04484]]

## chapter-03-section-05-pc00154 | equation | low | PDF 278

[[FORMULA:f-p0278-04485]]

## chapter-03-section-05-pc00155 | ordinary-paragraph | high | PDF 278

On summing these three quantities we obtain (1/2)/(/ + 2)(/ + 3) moments. On the other hand, observe that the product of an arbitrary polynomial of P? by x: p(x): x yields an arbitrary polynomial of P,,,. Hence the identity p(x)-x = 0 amounts to dim(P,,,) independent conditions. Therefore

## chapter-03-section-05-pc00156 | equation | low | PDF 278

[[FORMULA:f-p0278-04487]]

## chapter-03-section-05-pc00157 | equation | low | PDF 278

[[FORMULA:f-p0278-04488]]

## chapter-03-section-05-pc00158 | ordinary-paragraph | high | PDF 278

= (1 2\ee 3) eek Oo The equality in Lemma 5.4 means that the polynomials of R, are uniquely determined by their three sets of moments if and only if the zero moments define only the zero polynomial. But this unisolvence is not easily established on an arbitrary tetrahedron x. Therefore, we shall first prove that the zero moments are preserved by an affine transformation and subsequently work on the reference tetrahedron kK whenever it is convenient. As usual, we denote by F,. the affine invertible transformation from & onto x:

## chapter-03-section-05-pc00159 | equation | low | PDF 278

[[FORMULA:f-p0278-04490]]

## chapter-03-section-05-pc00160 | ordinary-paragraph | high | PDF 278,279

Scalar functions defined on « are transformed by a composition with F,: (5.25) d6=¢0F, \¢ defined on x, while vector functions defined on « are transformed like gradients: (5.26) a= Bi(uoF.) Vudefined on kx. Recall that the unit normal and unit tangent vectors are transformed respectively by (5.28) toF, = (By t)/IlB. tl. The main reason for adopting the transformation (5.26) is that it preserves the curl in a certain sense. Indeed, let us introduce the matrices (5.29) ‘ = (Ci)i, j = (0u,/0x; as u;/OX;);, js

## chapter-03-section-05-pc00161 | equation | low | PDF 279

[[FORMULA:f-p0279-04497]]

## chapter-03-section-05-pc00162 | ordinary-paragraph | high | PDF 279

Then by expanding the formula (5.26) we easily derive that the matrices C and C are related by: (5.30) COre=(B,*).C(B.*). As a consequence, curlu and curl @ vanish always simultaneously. Besides that, the transformation (5.26) preserves the space R).

## chapter-03-section-05-pc00163 | lemma | high | PDF 279

Lemma 5.5. The space R, is invariant under the transformation (5.26).

## chapter-03-section-05-pc00164 | proof | high | PDF 279

Proof. Clearly (5.26) preserves the space P; for arbitrary k; hence we need only

## chapter-03-section-05-pc00165 | ordinary-paragraph | high | PDF 279

consider u in S,. Formula (5.26) reads:

## chapter-03-section-05-pc00166 | equation | low | PDF 279

[[FORMULA:f-p0279-04505]]

## chapter-03-section-05-pc00167 | equation | low | PDF 279

[[FORMULA:f-p0279-04506]]

## chapter-03-section-05-pc00168 | ordinary-paragraph | high | PDF 279

where the degree of p is strictly less than / and B7 u(B,.x)e P>. Now,

## chapter-03-section-05-pc00169 | equation | low | PDF 279

[[FORMULA:f-p0279-04508]]

## chapter-03-section-05-pc00170 | ordinary-paragraph | high | PDF 279

since ue S,. Hence fie R, on Kk. Conversely, the same argument shows that if fe R, on K then ue R, on k. Cc

## chapter-03-section-05-pc00171 | lemma | high | PDF 279

Lemma 5.6. The three sets of moments of a function u given by Definition 5.1 vanish

## chapter-03-section-05-pc00172 | ordinary-paragraph | high | PDF 279

on k iff the moments of & vanish on R.

## chapter-03-section-05-pc00173 | proof | high | PDF 279

Proof. In view of (5.26) we have:

## chapter-03-section-05-pc00174 | equation | low | PDF 279

[[FORMULA:f-p0279-04510]]

## chapter-03-section-05-pc00175 | ordinary-paragraph | high | PDF 279

Hence ;

## chapter-03-section-05-pc00176 | equation | low | PDF 279

[[FORMULA:f-p0279-04511]]

## chapter-03-section-05-pc00177 | ordinary-paragraph | high | PDF 279

Next, observe that every vector q of R?® satisfies

## chapter-03-section-05-pc00178 | equation | low | PDF 279

[[FORMULA:f-p0279-04512]]

## chapter-03-section-05-pc00179 | ordinary-paragraph | high | PDF 279

Furthermore, all tangent vectors q to the affine variety f with normal n (ie. q is characterized by q-n = 0) are of the form q = p x n for arbitrary p of R’. Hence

## chapter-03-section-05-pc00180 | equation | low | PDF 280

[[FORMULA:f-p0280-04514]]

## chapter-03-section-05-pc00181 | ordinary-paragraph | high | PDF 280

di Therefore, applying (5.26) and (5.27) we have:

## chapter-03-section-05-pc00182 | equation | low | PDF 280

[[FORMULA:f-p0280-04516]]

## chapter-03-section-05-pc00183 | ordinary-paragraph | high | PDF 280

such that (Ba }(qio f)-n.— 0

## chapter-03-section-05-pc00184 | equation | low | PDF 280

[[FORMULA:f-p0280-04517]]

## chapter-03-section-05-pc00185 | equation | low | PDF 280

[[FORMULA:f-p0280-04518]]

## chapter-03-section-05-pc00186 | ordinary-paragraph | high | PDF 280

M.,(u) = {0>} M,( @) = {0}. fs Now we turn to the unisolvence. Let us start with a boundary result.

## chapter-03-section-05-pc00187 | lemma | high | PDF 280

Lemma 5.7. A vector u of R, has all its moments zero on a given face f of k iff the

## chapter-03-section-05-pc00188 | ordinary-paragraph | high | PDF 280

tangential components of u vanish on f.

## chapter-03-section-05-pc00189 | proof | high | PDF 280

Proof. As all conditions involved are preserved by an affine transformation, we

## chapter-03-section-05-pc00190 | ordinary-paragraph | high | PDF 280

can assume that the face f lies on the plane x, = 0. Then the tangential components u, of u on f reduce to its first two components:

## chapter-03-section-05-pc00191 | equation | low | PDF 280

[[FORMULA:f-p0280-04521]]

## chapter-03-section-05-pc00192 | ordinary-paragraph | high | PDF 280

Moreover, the conditions M,(u)= {0} and M,(u) = {0} are respectively equivalent to: (5.31) |u r'qdx,;dx,=0 VqeP-,(f), i (5:32) |u ;;tqde=0 VqeP_,(e). Hence Green’s formula (1.2.22) in two dimensions gives:

## chapter-03-section-05-pc00193 | equation | low | PDF 280

[[FORMULA:f-p0280-04525]]

## chapter-03-section-05-pc00194 | ordinary-paragraph | high | PDF 280

af Le: curlu; =0 onf. Now, it is easy to verify that u; belongs to the two-dimensional analogue of R,. Therefore it follows from Lemma 5.3 and its Remark that

## chapter-03-section-05-pc00195 | equation | low | PDF 280

[[FORMULA:f-p0280-04527]]

## chapter-03-section-05-pc00196 | ordinary-paragraph | high | PDF 280

As a consequence, (5.32) implies that p is constant on the boundary Of of f; thus we can take

## chapter-03-section-05-pc00197 | equation | low | PDF 280

[[FORMULA:f-p0280-04529]]

## chapter-03-section-05-pc00198 | ordinary-paragraph | low | PDF 280,281

es p=A,A,A3r_ withreP,_3(f), yields that r = 0. 口

## chapter-03-section-05-pc00199 | lemma | medium | PDF 281

Lemma 5.8. If the moments of the vector u of R are all zero on k then u is

## chapter-03-section-05-pc00200 | ordinary-paragraph | medium | PDF 281

identically zero.

## chapter-03-section-05-pc00201 | proof | medium | PDF 281

Proof. On the one hand, Lemma 5.7 shows that

## chapter-03-section-05-pc00202 | equation | low | PDF 281

[[FORMULA:f-p0281-04532]]

## chapter-03-section-05-pc00203 | equation | low | PDF 281

[[FORMULA:f-p0281-04533]]

## chapter-03-section-05-pc00204 | ordinary-paragraph | medium | PDF 281

on the other hand, we have

## chapter-03-section-05-pc00205 | equation | low | PDF 281

[[FORMULA:f-p0281-04534]]

## chapter-03-section-05-pc00206 | ordinary-paragraph | medium | PDF 281

Vqe Pi-3(k).

## chapter-03-section-05-pc00207 | equation | low | PDF 281

[[FORMULA:f-p0281-04535]]

## chapter-03-section-05-pc00208 | ordinary-paragraph | medium | PDF 281

Again, since these conditions are preserved by an affine transformation, we can switch to the reference element. Then Green's formula gives:

## chapter-03-section-05-pc00209 | equation | low | PDF 281

[[FORMULA:f-p0281-04536]]

## chapter-03-section-05-pc00210 | ordinary-paragraph | low | PDF 281

JK and it stems from (5.33) that

## chapter-03-section-05-pc00211 | equation | low | PDF 281

[[FORMULA:f-p0281-04538]]

## chapter-03-section-05-pc00212 | ordinary-paragraph | medium | PDF 281

Now, taking advantage of the geometry of k, it is easy to prove that these conditions (together with the fact that curl áe P?- (k)) imply

## chapter-03-section-05-pc00213 | equation | low | PDF 281

[[FORMULA:f-p0281-04540]]

## chapter-03-section-05-pc00214 | ordinary-paragraph | medium | PDF 281

Hence it follows from (5.30) that

## chapter-03-section-05-pc00215 | equation | low | PDF 281

[[FORMULA:f-p0281-04542]]

## chapter-03-section-05-pc00216 | ordinary-paragraph | medium | PDF 281

Therefore, owing to Lemma 5.3,

## chapter-03-section-05-pc00217 | equation | low | PDF 281

[[FORMULA:f-p0281-04543]]

## chapter-03-section-05-pc00218 | ordinary-paragraph | medium | PDF 281

with pe P; and plak = 0 because u x n = 0 on Ok. As a consequence, p = Λ,^2^4r with re P-4(k) and (5.34) implies that r = 0.

## chapter-03-section-05-pc00219 | ordinary-paragraph | medium | PDF 281

口

## chapter-03-section-05-pc00220 | remark | medium | PDF 281

Remark 5.5. By applying the arguments of Lemmas 5.7 and 5.8 it can also be

## chapter-03-section-05-pc00221 | ordinary-paragraph | medium | PDF 281

proved that every vector u of P3 with zero moments in k satisfies

## chapter-03-section-05-pc00222 | equation | low | PDF 281

[[FORMULA:f-p0281-04546]]

## chapter-03-section-05-pc00223 | ordinary-paragraph | medium | PDF 281

First, observe that Lemma 5.7 shows that

## chapter-03-section-05-pc00224 | equation | low | PDF 281

[[FORMULA:f-p0281-04547]]

## chapter-03-section-05-pc00225 | ordinary-paragraph | medium | PDF 281

But since this property is preserved by an affine transformation, it holds on each face of k. Then the argument of Lemma 5.8 yields

## chapter-03-section-05-pc00226 | equation | low | PDF 281

[[FORMULA:f-p0281-04548]]

## chapter-03-section-05-pc00227 | ordinary-paragraph | medium | PDF 282

beginning of this section.

## chapter-03-section-05-pc00228 | theorem | medium | PDF 282

Theorem 5.3. A vector field u of R, is entirely determined in a tetrahedron k by its

## chapter-03-section-05-pc00229 | ordinary-paragraph | medium | PDF 282

three sets of moments: Me(u), Ms(u), Mx(u). Moreover the tangential components of u on a given face f of r depend only upon the moments M,(u) and Me(u) defined on that face. This theorem induces a natural interpolation operator in K.

## chapter-03-section-05-pc00230 | ordinary-paragraph | low | PDF 282

sy r ' go pd u a si   sh 7 < ss moments as u on k. In other words, rxu is determined by:

## chapter-03-section-05-pc00231 | equation | low | PDF 282

[[FORMULA:f-p0282-04550]]

## chapter-03-section-05-pc00232 | ordinary-paragraph | medium | PDF 282

Clearly, it follows from the invariance Lemmas 5.5 and 5.6 that

## chapter-03-section-05-pc00233 | equation | low | PDF 282

[[FORMULA:f-p0282-04551]]

## chapter-03-section-05-pc00234 | equation | low | PDF 282

[[FORMULA:f-p0282-04552]]

## chapter-03-section-05-pc00235 | ordinary-paragraph | medium | PDF 282

i.e.

## chapter-03-section-05-pc00236 | equation | low | PDF 282

[[FORMULA:f-p0282-04553]]

## chapter-03-section-05-pc00237 | remark | medium | PDF 282

Remark 5.6. When ue W1,s(x)3 satisfies curl u = 0, the argument of Lemma 5.8

## chapter-03-section-05-pc00238 | ordinary-paragraph | medium | PDF 282

shows that curl(r,u) = O in K. Likewise, when ue P? , Remark 5.5 establishes that

## chapter-03-section-05-pc00239 | equation | low | PDF 282

[[FORMULA:f-p0282-04556]]

## chapter-03-section-05-pc00240 | ordinary-paragraph | medium | PDF 282

Now we are in a position to define the finite element spaces M, and Φ,. As a matter of convenience, we assume that Q is a bounded polyhcuiron. Let T, be a triangulation of Ω consisting of polyhedra k with diameters bounded by h. For each integer I ≥ 1, we set:

## chapter-03-section-05-pc00241 | equation | low | PDF 282

[[FORMULA:f-p0282-04558]]

## chapter-03-section-05-pc00242 | equation | low | PDF 282

[[FORMULA:f-p0282-04559]]

## chapter-03-section-05-pc00243 | equation | low | PDF 282

[[FORMULA:f-p0282-04560]]

## chapter-03-section-05-pc00244 | equation | low | PDF 282

[[FORMULA:f-p0282-04561]]

## chapter-03-section-05-pc00245 | ordinary-paragraph | medium | PDF 282

and we define the interpolation operator r, on M, by:

## chapter-03-section-05-pc00246 | equation | low | PDF 282

[[FORMULA:f-p0282-04562]]

## chapter-03-section-05-pc00247 | equation | low | PDF 282

[[FORMULA:f-p0282-04563]]

## chapter-03-section-05-pc00248 | ordinary-paragraph | low | PDF 282

( ds) ' r ss 1n ax u 7 < s as  )siM n a conforming approximation of H(curl; Q) (resp. Ho(curl; Ω)).

## chapter-03-section-05-pc00249 | lemma | medium | PDF 282

Lemma 5.9. If ue W1.s(Q)3, then r,ue M,. Similarly, when ue W1,s(Q) with

## chapter-03-section-05-pc00250 | ordinary-paragraph | medium | PDF 282,283

u x nlr = O then rhue Φh. We skip the proof as it is a straightforward consequence of Lemma 5.7. the triangulation 7, is regular as h tends to zero (cf. Definition A.2):

## chapter-03-section-05-pc00251 | equation | low | PDF 283

[[FORMULA:f-p0283-04567]]

## chapter-03-section-05-pc00252 | theorem | high | PDF 283

Theorem 5.4. Let 7, be a regular family of triangulations of Q and let M,, and r,

## chapter-03-section-05-pc00253 | ordinary-paragraph | high | PDF 283

be defined by (5.36) and (5.37) for some integer | > 1. We have the upper bound for all ue H'*1(Q)?: (5.38) ju — T,U ||( curl) < Cyh' {Jule ae |Wlh41,Q}- Moreover, the operator r, satisfies the following stability estimate: (5.39) ju — 7,0 lo, + Alleurl(u — 7,0) \|o,9 < Cyhlul,0 for allue W**(Q)? with s > 2, where the positive constants C, and C, are independent of h and u.

## chapter-03-section-05-pc00254 | proof | high | PDF 283

Proof. Let us first prove (5.38). By virtue of (5.26) we have:

## chapter-03-section-05-pc00255 | equation | low | PDF 283

[[FORMULA:f-p0283-04573]]

## chapter-03-section-05-pc00256 | ordinary-paragraph | high | PDF 283

But since the operator rz preserves the polynomials of P?,, Corollary A.1 implies that:

## chapter-03-section-05-pc00257 | ordinary-paragraph | high | PDF 283

: [tle wail2 ,

## chapter-03-section-05-pc00258 | equation | low | PDF 283

[[FORMULA:f-p0283-04574]]

## chapter-03-section-05-pc00259 | equation | low | PDF 283

[[FORMULA:f-p0283-04575]]

## chapter-03-section-05-pc00260 | ordinary-paragraph | high | PDF 283

Next, combining formulas (A.7) and (5.26) we derive: (5.40) [lk < Cp ||B y ||| det(B,7) Ju|le. .. Therefore, these three inequalities yield:

## chapter-03-section-05-pc00261 | equation | low | PDF 283

[[FORMULA:f-p0283-04578]]

## chapter-03-section-05-pc00262 | ordinary-paragraph | high | PDF 283

(5.41) 5

## chapter-03-section-05-pc00263 | ordinary-paragraph | high | PDF 283

lu —rUllone < C3 Bei WN Bell? (uli + Bell lule,.) when! = 1. Next, let us examine curl(u — r,,u). According to (5.30), we have:

## chapter-03-section-05-pc00264 | equation | low | PDF 283

[[FORMULA:f-p0283-04582]]

## chapter-03-section-05-pc00265 | ordinary-paragraph | high | PDF 283

As mentioned in Remark 5.6, the linear mapping 4 > curl(@ — r,fi) vanishes on the space P,. Therefore, a simple application of Theorem A.1 yields:

## chapter-03-section-05-pc00266 | equation | low | PDF 283

[[FORMULA:f-p0283-04584]]

## chapter-03-section-05-pc00267 | ordinary-paragraph | high | PDF 283

Hence (5.42) l|curl(u — 7,0) lo < Coll Be 7 Bell 7 alistx :

## chapter-03-section-05-pc00268 | ordinary-paragraph | high | PDF 283

Finally (5.38) stems from (5.41) and (5.42) together with (A.2) and the regularity Or7,.

## chapter-03-section-05-pc00269 | ordinary-paragraph | high | PDF 283

The proof of the stability estimate (5.39) is a trifle more intricate. Taking into account the facts that r; preserves the constant polynomials and belongs to

## chapter-03-section-05-pc00270 | equation | low | PDF 284

[[FORMULA:f-p0284-04588]]

## chapter-03-section-05-pc00271 | ordinary-paragraph | high | PDF 284

Hence

## chapter-03-section-05-pc00272 | equation | low | PDF 284

[[FORMULA:f-p0284-04589]]

## chapter-03-section-05-pc00273 | ordinary-paragraph | high | PDF 284

Then HO6lder’s inequality and the regularity of 7, imply that

## chapter-03-section-05-pc00274 | equation | low | PDF 284

[[FORMULA:f-p0284-04590]]

## chapter-03-section-05-pc00275 | ordinary-paragraph | high | PDF 284

Likewise, we have

## chapter-03-section-05-pc00276 | equation | low | PDF 284

[[FORMULA:f-p0284-04591]]

## chapter-03-section-05-pc00277 | ordinary-paragraph | high | PDF 284

Therefore, we infer from the above inequalities that: ||curl(u — 7,0) |lo,9 < C,1(meas(Q"|)u)|," ?0 . O

## chapter-03-section-05-pc00278 | subsection | high | PDF 284

5.4. Error Analysis for Finite Elements of Degree /

## chapter-03-section-05-pc00279 | ordinary-paragraph | high | PDF 284

The spaces M, and ®, have already been defined in (5.36) and it remains to define the space 9,. Here, we simply take the standard finite element space: (5.43) 0, = {q,€ 6° (Q); dnleEP, VRE; Galr= O}- Recall that the functions of ®,, satisfy (5.12) (,,gradq,)=0 Vq,eO,. The next three results check the hypotheses (5.14) and (5.17). They will lead in particular to an interesting decomposition of our discrete finite element spaces. Before proving that the space @,, satisfies (5.14), let us show the following preliminary result.

## chapter-03-section-05-pc00280 | lemma | high | PDF 284

Lemma 5.10. Let u be a function of the form:

## chapter-03-section-05-pc00281 | equation | low | PDF 284

[[FORMULA:f-p0284-04598]]

## chapter-03-section-05-pc00282 | ordinary-paragraph | high | PDF 284

and assume that wis such that r,u is well defined. Then there exists p,,in ©, such that

## chapter-03-section-05-pc00283 | equation | low | PDF 284

[[FORMULA:f-p0284-04599]]

## chapter-03-section-05-pc00284 | proof | high | PDF 284

Proof. As curlu = 0, Remark 5.6 implies that

## chapter-03-section-05-pc00285 | equation | low | PDF 284

[[FORMULA:f-p0284-04601]]

## chapter-03-section-05-pc00286 | ordinary-paragraph | high | PDF 284

But since p is constant on J’, we also have u x n= 0 on J” Therefore, it follows from Lemma 5.9 that r,u€ Ho(curl; Q); this means that

## chapter-03-section-05-pc00287 | equation | low | PDF 284

[[FORMULA:f-p0284-04604]]

## chapter-03-section-05-pc00288 | ordinary-paragraph | high | PDF 284,285

Hence On the other hand, Lemma 5.3 implies that q|.€P, for each kx. Therefore qe @,,. |

## chapter-03-section-05-pc00289 | remark | high | PDF 285

Remark 5.7. Lemma 5.10 shows that for each function @, in ®, that satisfies

## chapter-03-section-05-pc00290 | ordinary-paragraph | high | PDF 285

curl , = 0 in Q there exists a (unique) element p, of O, such that

## chapter-03-section-05-pc00291 | equation | low | PDF 285

[[FORMULA:f-p0285-04606]]

## chapter-03-section-05-pc00292 | ordinary-paragraph | high | PDF 285

Thus {grad p,; p,€9,} = {o,€®,; curl, = 0}. It follows from this last remark that @,, satisfies (5.14). But if we want to check that (5.14) holds uniformly, we shall require below a uniformly regular triangulation, i.e. a regular triangulation 7%, that also satisfies for some t > 0 independent of h:

## chapter-03-section-05-pc00293 | equation | low | PDF 285

[[FORMULA:f-p0285-04611]]

## chapter-03-section-05-pc00294 | proposition | high | PDF 285

Proposition 5.1. Let Q be an open, bounded and convex region of R? with a

## chapter-03-section-05-pc00295 | ordinary-paragraph | high | PDF 285

polyhedral boundary I. If %,,is a uniformly regular triangulation of Q, there exists a constant C*, independent of h, such that: (5.14) Ir Hoo < C*lleurld,llo,0 VO, Pro-

## chapter-03-section-05-pc00296 | proof | high | PDF 285

Proof. The idea is to write , as the sum of a gradient and a divergence-free

## chapter-03-section-05-pc00297 | ordinary-paragraph | high | PDF 285

function w, smooth enough to satisfy an inequality similar to (5.14). First, let p€ H4(Q) be the unique solution of the problem:

## chapter-03-section-05-pc00298 | equation | low | PDF 285

[[FORMULA:f-p0285-04614]]

## chapter-03-section-05-pc00299 | ordinary-paragraph | high | PDF 285

Clearly the difference

## chapter-03-section-05-pc00300 | equation | low | PDF 285

[[FORMULA:f-p0285-04615]]

## chapter-03-section-05-pc00301 | ordinary-paragraph | high | PDF 285

satisfies curlw = curld,, divw=0, wxnjp=0. In addition, curl, belongs to L?(Q)° for all y. Therefore, since 2 is convex, it follows from Remark I.3.14 that there exists a real s > 2 such that:

## chapter-03-section-05-pc00302 | ordinary-paragraph | high | PDF 285

we W!5(Q)3 and (5.44) IWllia.e <C,(@)|leurlwilo.,0 foralla with2<a<s.

## chapter-03-section-05-pc00303 | ordinary-paragraph | high | PDF 285

Hence, the interpolate r,w is well defined. As @, belongs to ®,, this in turn implies that r,(grad p) is also well defined and owing to Lemma 5.10, there exists Pp, in O, such that

## chapter-03-section-05-pc00304 | equation | low | PDF 285

[[FORMULA:f-p0285-04621]]

## chapter-03-section-05-pc00305 | equation | low | PDF 286

[[FORMULA:f-p0286-04622]]

## chapter-03-section-05-pc00306 | ordinary-paragraph | high | PDF 286

Then, applying (5.12) with q, = p, we easily derive

## chapter-03-section-05-pc00307 | equation | low | PDF 286

[[FORMULA:f-p0286-04624]]

## chapter-03-section-05-pc00308 | ordinary-paragraph | high | PDF 286

Thus, (5.14) will be established if we show that (5.45) TrW llo,a < C* |leurl >, \Io,0-

## chapter-03-section-05-pc00309 | equation | low | PDF 286

[[FORMULA:f-p0286-04627]]

## chapter-03-section-05-pc00310 | equation | low | PDF 286

[[FORMULA:f-p0286-04628]]

## chapter-03-section-05-pc00311 | ordinary-paragraph | high | PDF 286

But since 7, is uniformly regular and @, is a polynomial on each k, we easily obtain from (5.30) and (A.34):

## chapter-03-section-05-pc00312 | equation | low | PDF 286

[[FORMULA:f-p0286-04630]]

## chapter-03-section-05-pc00313 | ordinary-paragraph | high | PDF 286

Therefore

## chapter-03-section-05-pc00314 | equation | low | PDF 286

[[FORMULA:f-p0286-04631]]

## chapter-03-section-05-pc00315 | ordinary-paragraph | high | PDF 286

with a non negative exponent « as long as 2 < s < 6. This proves (5.45). O

## chapter-03-section-05-pc00316 | corollary | high | PDF 286

Corollary 5.1. Let Q be an open, bounded polyhedron of R*. For each function w,,

## chapter-03-section-05-pc00317 | ordinary-paragraph | high | PDF 286

of ®, there exists a unique function v, in ®,,. and p,, in O, such that:

## chapter-03-section-05-pc00318 | equation | low | PDF 286

[[FORMULA:f-p0286-04633]]

## chapter-03-section-05-pc00319 | equation | low | PDF 286

[[FORMULA:f-p0286-04634]]

## chapter-03-section-05-pc00320 | ordinary-paragraph | high | PDF 286

IPali,a@S ||W allo.a- Moreover, under the assumptions of Proposition 5.1, v, is bounded as follows: (5.47) [Vllin ve urt;;2)< ( 1 + C*?)*||c”u r l w|yl o, 0.

## chapter-03-section-05-pc00321 | proof | high | PDF 286

Proof. Let us take for p, the unique solution in @, of

## chapter-03-section-05-pc00322 | equation | low | PDF 286

[[FORMULA:f-p0286-04636]]

## chapter-03-section-05-pc00323 | ordinary-paragraph | high | PDF 286

Then the difference

## chapter-03-section-05-pc00324 | equation | low | PDF 286

[[FORMULA:f-p0286-04637]]

## chapter-03-section-05-pc00325 | ordinary-paragraph | high | PDF 286

belongs to ®,9 and (5.47) follows immediately from Proposition 5.1. fia Observe that the first part of this corollary establishes (5.17). From Lemmas 5.1 and 5.2, Theorems 5.1, 5.2 and 5.4, Proposition 5.1 and

## chapter-03-section-05-pc00326 | corollary | high | PDF 286

Corollary 5.1, we derive the major result of this section.

## chapter-03-section-05-pc00327 | theorem | high | PDF 286

Theorem 5.5. Let Q be a bounded polyhedron in R*. Then Problems (5.15) and

## chapter-03-section-05-pc00328 | ordinary-paragraph | high | PDF 286

(5.16) associated with the choice of finite element spaces (5.36) and (5.43) are equivalent and have a unique solution u, = (curl y,,, ,).

## chapter-03-section-05-pc00329 | equation | low | PDF 287

[[FORMULA:f-p0287-04643]]

## chapter-03-section-05-pc00330 | ordinary-paragraph | high | PDF 287

for some integer | > 1. Then, if Y, is a uniformly regular family of triangulations of Q, u,, satisfies the error estimates:

## chapter-03-section-05-pc00331 | equation | low | PDF 287

[[FORMULA:f-p0287-04645]]

## chapter-03-section-05-pc00332 | equation | low | PDF 287

[[FORMULA:f-p0287-04646]]

## chapter-03-section-05-pc00333 | equation | low | PDF 287

[[FORMULA:f-p0287-04647]]

## chapter-03-section-05-pc00334 | ordinary-paragraph | high | PDF 287

with positive constants C, and C, independent of h, o and w.

## chapter-03-section-05-pc00335 | remark | high | PDF 287

Remark 5.8. Like in the two-dimensional case, we observe a loss of one power of

## chapter-03-section-05-pc00336 | ordinary-paragraph | high | PDF 287

h arising from the term (cf. Lemma 5.2):

## chapter-03-section-05-pc00337 | equation | low | PDF 287

[[FORMULA:f-p0287-04648]]

## chapter-03-section-05-pc00338 | equation | low | PDF 287

[[FORMULA:f-p0287-04649]]

## chapter-03-section-05-pc00339 | ordinary-paragraph | high | PDF 287

On€ Pro Mhe Mp, | Hallo. If it were known that the projection B,w (for y in ,):

## chapter-03-section-05-pc00340 | equation | low | PDF 287

[[FORMULA:f-p0287-04650]]

## chapter-03-section-05-pc00341 | ordinary-paragraph | high | PDF 287

satisfied the L?-estimate: (5.50) ||Bw — Wllo.p.@ + Alleurl(B,y — W)llo,p,.0 < Ch'** | wlls+1,p,0 for all pe[2, ©] and se[1,/], then the argument of Section 3.1 could be applied to derive a sharper estimate than (5.48) and regain part of the missing power of h. In particular this would enable us to obtain an acceptable rate of convergence when using first degree elements, which Theorem 5.5 fails to show.

## chapter-03-section-05-pc00342 | ordinary-paragraph | high | PDF 287

Although (5.50) is still a conjecture, it does not sound unreasonable and it is hoped that this problem will be solved in a near future.

## chapter-03-section-05-pc00343 | subsection | high | PDF 287

5.5. Discontinuous Approximation of the Pressure

## chapter-03-section-05-pc00344 | ordinary-paragraph | high | PDF 287

This section briefly describes and analyzes a finite element method that solves for the pressure term underlying Problems (5.15) and (5.16). Since the situation is fairly similar to that in Section 4.4 we shall state nearly all results without

## chapter-03-section-05-pc00345 | proof | high | PDF 287

proof. The reader will easily fill in the blanks.

## chapter-03-section-05-pc00346 | ordinary-paragraph | high | PDF 287

It is clear that here we must construct subspaces D, of H(div; 2) such that, on the one hand, curl p, belongs to D, for p,, in M, and on the other hand, div v, belongs to the discrete pressure space for v, in D,. The following definition generalizes the polynomial space D defined by (4.61a).

## chapter-03-section-05-pc00347 | definition | high | PDF 287

Definition 5.3. 1°) For each integer / > 1, let

## chapter-03-section-05-pc00348 | equation | low | PDF 287

[[FORMULA:f-p0287-04658]]

## chapter-03-section-05-pc00349 | equation | low | PDF 288

[[FORMULA:f-p0288-04659]]

## chapter-03-section-05-pc00350 | ordinary-paragraph | high | PDF 288

if

## chapter-03-section-05-pc00351 | equation | low | PDF 288

[[FORMULA:f-p0288-04660]]

## chapter-03-section-05-pc00352 | ordinary-paragraph | high | PDF 288

We can immediately check that for uin D,, u-n belongs to P,_, on each face f of k. In addition, it easy to see that when u is a divergence-free vector field of D, then u belongs to P?.,. As usual, let K denote the unit reference tetrahedron. Instead of (5.26), let us transform vector functions defined on x by the contravariant transformation: (551) a= B.'(uoF,) Vudefined on kx. It coincides with the contravariant transformation (4.63), up to the multiplicative factor J, which is constant here:

## chapter-03-section-05-pc00353 | equation | low | PDF 288

[[FORMULA:f-p0288-04664]]

## chapter-03-section-05-pc00354 | ordinary-paragraph | high | PDF 288

As a consequence (5.51) preserves entirely the divergence: (5:52) (divu)o F, = diva. In addition, we have the analogue of Lemmas 5.5, 5.6 and Theorem 5.3.

## chapter-03-section-05-pc00355 | proposition | high | PDF 288

Proposition 5.2. 1°) The space D, is invariant under the transformation (5.51) and

## chapter-03-section-05-pc00356 | ordinary-paragraph | high | PDF 288

the moments of u given by Definition 5.3 vanish on k iff the same moments of 0 vanish on kK. 2°) A vector field u of D, is entirely determined in a tetrahedron x by its two sets of moments: N,(u), N,.(u). Moreover, the normal component of uon a given face f of « depends only upon the moments N,(u) defined on that face.

## chapter-03-section-05-pc00357 | definition | high | PDF 288

Definition 5.4. Let ue H'(«)°, where x is an arbitrary tetrahedron. Its interpolant

## chapter-03-section-05-pc00358 | ordinary-paragraph | high | PDF 288

@,U is the unique polynomial of D, that has the same moments as u on x. Thus @,.u is determined by the conditions:

## chapter-03-section-05-pc00359 | equation | low | PDF 288

[[FORMULA:f-p0288-04668]]

## chapter-03-section-05-pc00360 | ordinary-paragraph | high | PDF 288

Again, the invariance in Proposition 5.2 implies that

## chapter-03-section-05-pc00361 | equation | low | PDF 288

[[FORMULA:f-p0288-04669]]

## chapter-03-section-05-pc00362 | ordinary-paragraph | high | PDF 288

Moreover, we observe that

## chapter-03-section-05-pc00363 | equation | low | PDF 288

[[FORMULA:f-p0288-04670]]

## chapter-03-section-05-pc00364 | ordinary-paragraph | high | PDF 288

and that divu = 0 on xk implies that div(@,u) = 0.

## chapter-03-section-05-pc00365 | equation | low | PDF 289

[[FORMULA:f-p0289-04672]]

## chapter-03-section-05-pc00366 | ordinary-paragraph | high | PDF 289

(553) Do, = D,N Ho (div; 2),

## chapter-03-section-05-pc00367 | equation | low | PDF 289

[[FORMULA:f-p0289-04674]]

## chapter-03-section-05-pc00368 | ordinary-paragraph | high | PDF 289

together with the interpolation operator @,:

## chapter-03-section-05-pc00369 | equation | low | PDF 289

[[FORMULA:f-p0289-04675]]

## chapter-03-section-05-pc00370 | ordinary-paragraph | high | PDF 289

and for all ue H'(Q)°. Clearly, div u, belongs to Q, for all u, in Do, and curl p, belongs to Do, for all p, in ®,. Furthermore, we have the analogue of Lemma 5.9:

## chapter-03-section-05-pc00371 | ordinary-paragraph | high | PDF 289

uc H'(Q)? implies w,ueD,,

## chapter-03-section-05-pc00372 | equation | low | PDF 289

[[FORMULA:f-p0289-04677]]

## chapter-03-section-05-pc00373 | ordinary-paragraph | high | PDF 289

The following proposition states the approximation properties of D,.

## chapter-03-section-05-pc00374 | proposition | high | PDF 289

Proposition 5.3. Let 7, be a regular family of triangulations of Q and let D, be

## chapter-03-section-05-pc00375 | ordinary-paragraph | high | PDF 289

defined by (5.53) for an integer | > 1. We have the estimates:

## chapter-03-section-05-pc00376 | equation | low | PDF 289

[[FORMULA:f-p0289-04679]]

## chapter-03-section-05-pc00377 | ordinary-paragraph | high | PDF 289

(5.54) '

## chapter-03-section-05-pc00378 | equation | low | PDF 289

[[FORMULA:f-p0289-04681]]

## chapter-03-section-05-pc00379 | ordinary-paragraph | high | PDF 289

The next lemma establishes the desired relationship between the spaces D, and M,,.

## chapter-03-section-05-pc00380 | lemma | high | PDF 289

Lemma 5.11. Let Q be an open, bounded polyhedron in R? and let T;,0 <i< p,

## chapter-03-section-05-pc00381 | ordinary-paragraph | high | PDF 289

denote the connected components of its boundary. A function u, of D, (resp. Don) satisfies:

## chapter-03-section-05-pc00382 | equation | low | PDF 289

[[FORMULA:f-p0289-04683]]

## chapter-03-section-05-pc00383 | ordinary-paragraph | high | PDF 289

I, iff there exists a function , in M, (resp. ®,) such that:

## chapter-03-section-05-pc00384 | equation | low | PDF 289

[[FORMULA:f-p0289-04684]]

## chapter-03-section-05-pc00385 | proof | high | PDF 289

Proof. We already know that curl #, belongs to D, (resp. Do,,) whenever o,, belongs

## chapter-03-section-05-pc00386 | ordinary-paragraph | high | PDF 289

to M, (resp. ®,).

## chapter-03-section-05-pc00387 | ordinary-paragraph | high | PDF 289

Conversely, Theorem I.3.4 asserts that there exists @ € H'(2)° such that

## chapter-03-section-05-pc00388 | equation | low | PDF 289

[[FORMULA:f-p0289-04686]]

## chapter-03-section-05-pc00389 | ordinary-paragraph | high | PDF 289,290

Furthermore, the fact that u,, belongs to H*(Q)°* for alla with0 < a < 1/2 implies that @ belongs to H!*7(Q)? (cf. Remark 1.3.12). Thus, the interpolate of 6, 7, is well defined. Let us prove that: Le; curl(d — 7,60) =90 inQ. On the one hand, observe that curl(@ — r,)€| P?.,,(« ). On the other hand, we have

## chapter-03-section-05-pc00390 | equation | low | PDF 290

[[FORMULA:f-p0290-04690]]

## chapter-03-section-05-pc00391 | equation | low | PDF 290

[[FORMULA:f-p0290-04691]]

## chapter-03-section-05-pc00392 | ordinary-paragraph | high | PDF 290

Hence like in Lemma 5.8, we deduce:

## chapter-03-section-05-pc00393 | equation | low | PDF 290

[[FORMULA:f-p0290-04692]]

## chapter-03-section-05-pc00394 | ordinary-paragraph | high | PDF 290

and since @ — r,¢ belongs to H(curl; Q), its curl vanishes on the whole of Q. It remains to establish that when u,,-n vanishes on J’ then @, may be chosen such that @, x n = 0 on J. The proof follows the lines of Theorem I.3.6. We take an open ball ( containing Q; then, it is easy to construct a function q in H?(@) such that

## chapter-03-section-05-pc00395 | equation | low | PDF 290

[[FORMULA:f-p0290-04695]]

## chapter-03-section-05-pc00396 | ordinary-paragraph | high | PDF 290

Note that this requires no regularity on Q since grad q need not be divergencefree. As q belongs to H*(Q), r, grad q is well defined and therefore r,(@ — grad q) is the desired potential vector of u, in &,. O

## chapter-03-section-05-pc00397 | remark | high | PDF 290

Remark 5.9. According to Corollary 5.1, for each divergence-free vector field u,

## chapter-03-section-05-pc00398 | ordinary-paragraph | high | PDF 290

in Do, there exists a unique vector potential , in ®,, such that:

## chapter-03-section-05-pc00399 | equation | low | PDF 290

[[FORMULA:f-p0290-04698]]

## chapter-03-section-05-pc00400 | ordinary-paragraph | high | PDF 290

In addition, under the hypotheses of Proposition 5.1, we have:

## chapter-03-section-05-pc00401 | equation | low | PDF 290

[[FORMULA:f-p0290-04699]]

## chapter-03-section-05-pc00402 | ordinary-paragraph | high | PDF 290

With this lemma and the statement of Problem (5.16), we can formulate the corresponding problem in u,, @,, Dp: Find a pair (u,,),) in Do, x M,, and a function p, in Q,, such that:

## chapter-03-section-05-pc00403 | equation | low | PDF 290

[[FORMULA:f-p0290-04701]]

## chapter-03-section-05-pc00404 | ordinary-paragraph | high | PDF 290

(5.55) (u,, curl p,) = (@,,6,) Ve,eM,,

## chapter-03-section-05-pc00405 | equation | low | PDF 290

[[FORMULA:f-p0290-04703]]

## chapter-03-section-05-pc00406 | ordinary-paragraph | high | PDF 290

The existence and uniqueness of p, is a consequence of the following lemma which establishes the inf-sup condition relative to the space Do, x M, and Q,. Then

## chapter-03-section-05-pc00407 | lemma | high | PDF 290

Lemma 5.11 implies the equivalence between this problem and (5.15) or (5.16).

## chapter-03-section-05-pc00408 | ordinary-paragraph | high | PDF 290

Therefore when Q is a bounded polyhedron, Problem (5.55) has a unique solution (U,,, ,, Dn)-

## chapter-03-section-05-pc00409 | equation | low | PDF 291

[[FORMULA:f-p0291-04707]]

## chapter-03-section-05-pc00410 | equation | low | PDF 291

[[FORMULA:f-p0291-04708]]

## chapter-03-section-05-pc00411 | ordinary-paragraph | medium | PDF 291

In addition, when J, is a regular family of triangulations of Q, we have:

## chapter-03-section-05-pc00412 | equation | low | PDF 291

[[FORMULA:f-p0291-04709]]

## chapter-03-section-05-pc00413 | equation | low | PDF 291

[[FORMULA:f-p0291-04710]]

## chapter-03-section-05-pc00414 | ordinary-paragraph | medium | PDF 291

where the positive constant C is independent of h and pn.

## chapter-03-section-05-pc00415 | ordinary-paragraph | medium | PDF 291

The above lemmas lead to the expected estimate for the error p - Ph.

## chapter-03-section-05-pc00416 | theorem | medium | PDF 291

Theorem 5.6. Let Q be a bounded polyhedron in R3. Then Problem (5.55) has a

## chapter-03-section-05-pc00417 | ordinary-paragraph | medium | PDF 291

unique solution (un,wn) in Doh × M, and ph in Qh where (u, = curlwh,wn) is the solution of Problem (5.15).

## chapter-03-section-05-pc00418 | ordinary-paragraph | medium | PDF 291

Moreover, under the hypotheses of Theorem 5.5 and if the exact pressure p belongs to H'(Q) for I ≥ 1, the following error estimate holds:

## chapter-03-section-05-pc00419 | equation | low | PDF 291

[[FORMULA:f-p0291-04715]]

## chapter-03-section-05-pc00420 | equation | low | PDF 291

[[FORMULA:f-p0291-04716]]

## chapter-03-section-05-pc00421 | ordinary-paragraph | medium | PDF 291

with a positive constant C independent of h, p, o and y.
