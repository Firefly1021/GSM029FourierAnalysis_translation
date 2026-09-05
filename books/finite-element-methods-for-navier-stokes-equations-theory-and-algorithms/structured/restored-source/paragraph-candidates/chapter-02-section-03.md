# Paragraph candidates: chapter-02-section-03

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-02-section-03-pc00001 | ordinary-paragraph | high | PDF 166

Stokes Problem satisfy: ue (H**(Q)N HQ), pe H*(Q) 1 L3(Q) for some integer ké [1,1]. Then the solution (u,, p,) of (1.39) with the spaces X,, and M, defined by (2.47) (2.48) satisfies the error bound: (2.51) Ju —uyli.o + IP — Palloe < Crh“(ule+s,0 + |Plk.a)- In addition, if the Stokes Problem (1.48) is regular, we have the L*-estimate (2.52) Ju — uyllo,g < C,A** (luless,a + |Plk.):

## chapter-02-section-03-pc00002 | remark | high | PDF 166

Remark 2.8. It is easy to show that the statement of Remark 2.6 concerning the

## chapter-02-section-03-pc00003 | ordinary-paragraph | high | PDF 166

convergence under weak regularity assumptions on (u,p) is still valid in the three-dimensional case.

## chapter-02-section-03-pc00004 | section | high | PDF 166

§ 3. Quadrilateral Finite Element Methods Using Discontinuous

## chapter-02-section-03-pc00005 | ordinary-paragraph | high | PDF 166

Pressures

## chapter-02-section-03-pc00006 | ordinary-paragraph | high | PDF 166

There are two reasons for treating separately quadrilateral finite elements. On the one hand, isoparametric finite element methods are less transparent than simplicial ones and must be handled with some more care. On the other hand, quadrilateral elements (more precisely, rectangular elements) provide excellent examples of schemes which do not satisfy the inf-sup condition and yet can be proved to converge with optimal accuracy. Some of these schemes, being particularly simple, are preferred by a number of users. For the sake of conciseness, we have only treated the two-dimensional case. The three-dimensional case is a straightforward adaptation of this material and that of Section 2.3.

## chapter-02-section-03-pc00007 | subsection | high | PDF 166

3.1. A Quadrilateral Finite Element of Order One

## chapter-02-section-03-pc00008 | ordinary-paragraph | high | PDF 166

The element discussed in this section is the analogue of the first-order element defined in Section 2.1. It has been introduced by Fortin [30]. Let Q be a bounded, plane polygon and let 7, be a “triangulation” of Qm ade of convex quadrilaterals with diameters bounded by h. Consider one of these quadrilaterals « with vertices a,, a3, a3, a4 (also numbered ay); we denote by f; the segment [a;_,4,; ] ( cf. Figure 10) and by n, its unit outward normal. To draw the parallel with Section 2.1 we replace the barycentric coordinates by the reference variables

## chapter-02-section-03-pc00009 | equation | low | PDF 166

[[FORMULA:f-p0166-02509]]

## chapter-02-section-03-pc00010 | ordinary-paragraph | low | PDF 167

n4 Q

## chapter-02-section-03-pc00011 | equation | low | PDF 167

[[FORMULA:f-p0167-02510]]

## chapter-02-section-03-pc00012 | ordinary-paragraph | medium | PDF 167

n1 f3 n3

## chapter-02-section-03-pc00013 | ordinary-paragraph | low | PDF 167

a n2 a2

## chapter-02-section-03-pc00014 | figure | medium | PDF 167

Figure 10

## chapter-02-section-03-pc00015 | ordinary-paragraph | medium | PDF 167

Now, we are looking for a velocity vector w that is compatible with a constant pressure in k. Keeping in mind the material of Section 2.1 it is likely that w will belong to a space larger than Q(k), but that its tangential components on each side of k will be affine. (The pair (Qi(k), Po) will in fact be the object of Section 3.3). As an example, the polynomial

## chapter-02-section-03-pc00016 | equation | low | PDF 167

[[FORMULA:f-p0167-02511]]

## chapter-02-section-03-pc00017 | ordinary-paragraph | medium | PDF 167

vanishes on the sides f2,f, and f4 of the reference square k. Therefore the function

## chapter-02-section-03-pc00018 | equation | low | PDF 167

[[FORMULA:f-p0167-02512]]

## chapter-02-section-03-pc00019 | ordinary-paragraph | medium | PDF 167

has zero tangential components on the sides of k. Generalizing this remark, we set

## chapter-02-section-03-pc00020 | equation | low | PDF 167

[[FORMULA:f-p0167-02513]]

## chapter-02-section-03-pc00021 | equation | low | PDF 167

[[FORMULA:f-p0167-02514]]

## chapter-02-section-03-pc00022 | equation | low | PDF 167

[[FORMULA:f-p0167-02515]]

## chapter-02-section-03-pc00023 | ordinary-paragraph | medium | PDF 167

and we take the velocities w in the space (of dimension 12):

## chapter-02-section-03-pc00024 | equation | low | PDF 167

[[FORMULA:f-p0167-02516]]

## chapter-02-section-03-pc00025 | equation | low | PDF 167

[[FORMULA:f-p0167-02517]]

## chapter-02-section-03-pc00026 | ordinary-paragraph | medium | PDF 167

As will be seen in the next lemma, the degrees of freedom naturally attached to this space are the values of w at the vertices a; and the flux of w through each side f of k.

## chapter-02-section-03-pc00027 | lemma | medium | PDF 167

Lemma 3.1. A polynomial p of 2,(k) is uniquely determined by the 12 quantities:

## chapter-02-section-03-pc00028 | equation | low | PDF 167

[[FORMULA:f-p0167-02518]]

## chapter-02-section-03-pc00029 | ordinary-paragraph | medium | PDF 167

p(a;)

## chapter-02-section-03-pc00030 | equation | low | PDF 167

[[FORMULA:f-p0167-02519]]

## chapter-02-section-03-pc00031 | ordinary-paragraph | medium | PDF 167

p·n;ds

## chapter-02-section-03-pc00032 | equation | low | PDF 167

[[FORMULA:f-p0167-02520]]

## chapter-02-section-03-pc00033 | ordinary-paragraph | medium | PDF 167,168

Furthermore the restriction of p to any side f; of k depends only upon the degrees 4 (3.4) p = Ip ae » a; Pj, aE R,

## chapter-02-section-03-pc00034 | equation | low | PDF 168

[[FORMULA:f-p0168-02522]]

## chapter-02-section-03-pc00035 | ordinary-paragraph | high | PDF 168

where J, denotes the standard interpolation operator on Q,(«)*. Furthermore, (3.5) (p — [,p)njl5 ,= a;(4,0 F.*)Iy,- From these two expressions we can easily derive that zero moments yield only the zero polynomial. fia Thus, we choose the following velocity and pressure spaces: w|.€2;(x) Vee F;},

## chapter-02-section-03-pc00036 | equation | low | PDF 168

[[FORMULA:f-p0168-02524]]

## chapter-02-section-03-pc00037 | equation | low | PDF 168

[[FORMULA:f-p0168-02525]]

## chapter-02-section-03-pc00038 | equation | low | PDF 168

[[FORMULA:f-p0168-02526]]

## chapter-02-section-03-pc00039 | ordinary-paragraph | high | PDF 168

J,},

## chapter-02-section-03-pc00040 | equation | low | PDF 168

[[FORMULA:f-p0168-02527]]

## chapter-02-section-03-pc00041 | equation | low | PDF 168

[[FORMULA:f-p0168-02528]]

## chapter-02-section-03-pc00042 | equation | low | PDF 168

[[FORMULA:f-p0168-02529]]

## chapter-02-section-03-pc00043 | lemma | high | PDF 168

Lemma 3.1 suggests the interpolation operator r, on 2,(x«) defined by:

## chapter-02-section-03-pc00044 | equation | low | PDF 168

[[FORMULA:f-p0168-02530]]

## chapter-02-section-03-pc00045 | ordinary-paragraph | high | PDF 168

ihe But once again, this operator does not satisfy Hypothesis H3 because it is not defined on H'(Q)*. Therefore, like in the simplicial case we replace the above values of v by those of the local regularization operator R,. similar to that of Section A.3: R,€ L(Ho(Q); ®,) with

## chapter-02-section-03-pc00046 | equation | low | PDF 168

[[FORMULA:f-p0168-02531]]

## chapter-02-section-03-pc00047 | ordinary-paragraph | high | PDF 168

Then we define the operator 7, ¢ Y(H}(Q)*; X,) by:

## chapter-02-section-03-pc00048 | equation | low | PDF 168

[[FORMULA:f-p0168-02532]]

## chapter-02-section-03-pc00049 | equation | low | PDF 168

[[FORMULA:f-p0168-02533]]

## chapter-02-section-03-pc00050 | equation | low | PDF 168

[[FORMULA:f-p0168-02534]]

## chapter-02-section-03-pc00051 | ordinary-paragraph | high | PDF 168

ij In order to establish the approximating properties of z, we must assume that the triangulation 7, is regular in the sense of Definition A.2 with the parameters: h, = diameter of x, p, = 2 Min {diameter of circle inscribed in S;}

## chapter-02-section-03-pc00052 | equation | low | PDF 168

[[FORMULA:f-p0168-02536]]

## chapter-02-section-03-pc00053 | ordinary-paragraph | high | PDF 168

where S; denotes the triangle with vertices a;_,, a;, a;4,.

## chapter-02-section-03-pc00054 | lemma | high | PDF 168

Lemma 3.2. The operator n, defined by (3.8) satisfies:

## chapter-02-section-03-pc00055 | equation | low | PDF 168

[[FORMULA:f-p0168-02538]]

## chapter-02-section-03-pc00056 | ordinary-paragraph | medium | PDF 168,169

Q Furthermore if the triangulation Jh, is regular, π, has the error bound:

## chapter-02-section-03-pc00057 | equation | low | PDF 169

[[FORMULA:f-p0169-02539]]

## chapter-02-section-03-pc00058 | equation | low | PDF 169

[[FORMULA:f-p0169-02540]]

## chapter-02-section-03-pc00059 | ordinary-paragraph | low | PDF 169

()HAA with m = 0 or 1 and k = 1 or 2.

## chapter-02-section-03-pc00060 | proof | medium | PDF 169

Proof. From (3.4) and (3.5) we derive:

## chapter-02-section-03-pc00061 | ordinary-paragraph | medium | PDF 169

4

## chapter-02-section-03-pc00062 | equation | low | PDF 169

[[FORMULA:f-p0169-02543]]

## chapter-02-section-03-pc00063 | ordinary-paragraph | medium | PDF 169

αPi

## chapter-02-section-03-pc00064 | equation | low | PDF 169

[[FORMULA:f-p0169-02544]]

## chapter-02-section-03-pc00065 | ordinary-paragraph | low | PDF 169

where (v- Rkv)·n;ds q;o F-1 ds. a： fi JSi On the one hand, the operator R, has the local interpolation error for ve H*(Q)2:

## chapter-02-section-03-pc00066 | equation | low | PDF 169

[[FORMULA:f-p0169-02545]]

## chapter-02-section-03-pc00067 | equation | low | PDF 169

[[FORMULA:f-p0169-02546]]

## chapter-02-section-03-pc00068 | equation | low | PDF 169

[[FORMULA:f-p0169-02547]]

## chapter-02-section-03-pc00069 | ordinary-paragraph | medium | PDF 169

where again A, denotes the union of quadrilaterals which share at least a vertex with K. On the other hand, Lemma A.9 implies:

## chapter-02-section-03-pc00070 | equation | low | PDF 169

[[FORMULA:f-p0169-02548]]

## chapter-02-section-03-pc00071 | ordinary-paragraph | medium | PDF 169

2m1,1-m

## chapter-02-section-03-pc00072 | equation | low | PDF 169

[[FORMULA:f-p0169-02549]]

## chapter-02-section-03-pc00073 | ordinary-paragraph | medium | PDF 169

Besides that 9;ds

## chapter-02-section-03-pc00074 | equation | low | PDF 169

[[FORMULA:f-p0169-02550]]

## chapter-02-section-03-pc00075 | ordinary-paragraph | low | PDF 169

Jfi and II -- R,vIl ds

## chapter-02-section-03-pc00076 | equation | low | PDF 169

[[FORMULA:f-p0169-02551]]

## chapter-02-section-03-pc00077 | ordinary-paragraph | low | PDF 169

Jsi Jsi because the restriction of F, to the sides of k is affine. Then using the trace

## chapter-02-section-03-pc00078 | theorem | medium | PDF 169

Theorem 1.1.5 and Lemma A.9 we obtain:

## chapter-02-section-03-pc00079 | equation | low | PDF 169

[[FORMULA:f-p0169-02552]]

## chapter-02-section-03-pc00080 | ordinary-paragraph | medium | PDF 169

Therefore (3.10) yields:

## chapter-02-section-03-pc00081 | equation | low | PDF 169

[[FORMULA:f-p0169-02554]]

## chapter-02-section-03-pc00082 | ordinary-paragraph | medium | PDF 169

Jfi Hence

## chapter-02-section-03-pc00083 | equation | low | PDF 169

[[FORMULA:f-p0169-02555]]

## chapter-02-section-03-pc00084 | ordinary-paragraph | medium | PDF 169,170

and have established that our scheme is of order one:

## chapter-02-section-03-pc00085 | theorem | medium | PDF 170

Theorem 3.1. Let Q be a bounded polygon and assume that the solution (u, p) of

## chapter-02-section-03-pc00086 | ordinary-paragraph | medium | PDF 170

the Stokes equations satisfies: ()TU(o)Hd [()iHU()H]n Then if the triangulation J, is regular, the solution (un, Pn) of (1.39) with the spaces X, and M, defined by (3.6) (3.7) satisfies the conclusion of Theorem 2.1.

## chapter-02-section-03-pc00087 | subsection | medium | PDF 170

3.2. Higher-Order Quadrilateral Elements

## chapter-02-section-03-pc00088 | ordinary-paragraph | medium | PDF 170

We propose to discuss and generalize the widely used “Q2-P," finite element scheme. In short, this method uses continuous velocities with components that are piecewise Q2(k) and discontinuous pressures that are piecewise P, on each element k. Its analysis is pretty straightforward and easily extended to arbitrary order I, so we can start directly with the general case. Again, let k be any quadrilateral of J, and let us choose:

## chapter-02-section-03-pc00089 | equation | low | PDF 170

[[FORMULA:f-p0170-02558]]

## chapter-02-section-03-pc00090 | equation | low | PDF 170

[[FORMULA:f-p0170-02559]]

## chapter-02-section-03-pc00091 | equation | low | PDF 170

[[FORMULA:f-p0170-02560]]

## chapter-02-section-03-pc00092 | equation | low | PDF 170

[[FORMULA:f-p0170-02561]]

## chapter-02-section-03-pc00093 | equation | low | PDF 170

[[FORMULA:f-p0170-02562]]

## chapter-02-section-03-pc00094 | equation | low | PDF 170

[[FORMULA:f-p0170-02563]]

## chapter-02-section-03-pc00095 | ordinary-paragraph | medium | PDF 170

with I ≥ 2. Right away, observe that X, c X, so that the inf-sup condition need only be checked locally. As a consequence, we can take the simplest degrees of freedom available such as: the values of each component of w on the principal lattice Z, of order l; the moments corresponding to Pi-, for q: qf dx Vf e Pi-1. K To begin with, let us establish the local inf-sup condition. Here again, we take the triangulation as our partition:

## chapter-02-section-03-pc00096 | equation | low | PDF 170

[[FORMULA:f-p0170-02567]]

## chapter-02-section-03-pc00097 | equation | low | PDF 170

[[FORMULA:f-p0170-02568]]

## chapter-02-section-03-pc00098 | equation | low | PDF 170

[[FORMULA:f-p0170-02569]]

## chapter-02-section-03-pc00099 | theorem | medium | PDF 170

Theorem 3.2. Let the triangulation J, be regular. Then the pair of spaces (X,(k),

## chapter-02-section-03-pc00100 | ordinary-paragraph | medium | PDF 170

M,(r) defined by (3.13) satisfies Hypothesis H4.

## chapter-02-section-03-pc00101 | proof | medium | PDF 171

Proof. The proof is much like that of Theorem 2.2 so we shall only dwell on the

## chapter-02-section-03-pc00102 | ordinary-paragraph | medium | PDF 171

details inherent to quadrilaterals. We have:

## chapter-02-section-03-pc00103 | equation | low | PDF 171

[[FORMULA:f-p0171-02571]]

## chapter-02-section-03-pc00104 | equation | low | PDF 171

[[FORMULA:f-p0171-02572]]

## chapter-02-section-03-pc00105 | equation | low | PDF 171

[[FORMULA:f-p0171-02573]]

## chapter-02-section-03-pc00106 | ordinary-paragraph | medium | PDF 171

Since qe Pi-1, we have grad qe P²-2 and therefore

## chapter-02-section-03-pc00107 | equation | low | PDF 171

[[FORMULA:f-p0171-02575]]

## chapter-02-section-03-pc00108 | ordinary-paragraph | low | PDF 171

on k. Let b(x)xxxx4 denote the “bubble" function on k and let us choose

## chapter-02-section-03-pc00109 | equation | low | PDF 171

[[FORMULA:f-p0171-02576]]

## chapter-02-section-03-pc00110 | ordinary-paragraph | medium | PDF 171

Then ve X,(k) and with this choice

## chapter-02-section-03-pc00111 | equation | low | PDF 171

[[FORMULA:f-p0171-02577]]

## chapter-02-section-03-pc00112 | equation | low | PDF 171

[[FORMULA:f-p0171-02578]]

## chapter-02-section-03-pc00113 | ordinary-paragraph | low | PDF 171

Of course the mapping b(x)/p|dx k is a norm on any finite-dimensional space; thus

## chapter-02-section-03-pc00114 | equation | low | PDF 171

[[FORMULA:f-p0171-02579]]

## chapter-02-section-03-pc00115 | equation | low | PDF 171

[[FORMULA:f-p0171-02580]]

## chapter-02-section-03-pc00116 | ordinary-paragraph | low | PDF 171

JK K

## chapter-02-section-03-pc00117 | equation | low | PDF 171

[[FORMULA:f-p0171-02581]]

## chapter-02-section-03-pc00118 | ordinary-paragraph | medium | PDF 171

Besides that

## chapter-02-section-03-pc00119 | equation | low | PDF 171

[[FORMULA:f-p0171-02582]]

## chapter-02-section-03-pc00120 | ordinary-paragraph | medium | PDF 171

and

## chapter-02-section-03-pc00121 | equation | low | PDF 171

[[FORMULA:f-p0171-02583]]

## chapter-02-section-03-pc00122 | ordinary-paragraph | medium | PDF 171

by applying to quadrilaterals the easy argument of Lemma A.6. Hence

## chapter-02-section-03-pc00123 | equation | low | PDF 171

[[FORMULA:f-p0171-02584]]

## chapter-02-section-03-pc00124 | ordinary-paragraph | high | PDF 172

independent of h and x, such that (3.14) Who < COM die Ve H*(K)N Lo(x). We skip the proof because it is entirely similar to that of Lemma 2.5. It remains to examine the approximation properties of W, and Q,. While the approximation error in W, is completely standard since it stems directly from (A.49):

## chapter-02-section-03-pc00125 | equation | low | PDF 172

[[FORMULA:f-p0172-02586]]

## chapter-02-section-03-pc00126 | equation | low | PDF 172

[[FORMULA:f-p0172-02587]]

## chapter-02-section-03-pc00127 | equation | low | PDF 172

[[FORMULA:f-p0172-02588]]

## chapter-02-section-03-pc00128 | ordinary-paragraph | high | PDF 172

the approximation error in Q, is not so immediate because we are dealing with polynomials of P,_, on quadrilaterals (instead of triangles). In particular,

## chapter-02-section-03-pc00129 | theorem | high | PDF 172

Theorem A.3 cannot be applied because {po F,;peP,_,} is a proper subspace

## chapter-02-section-03-pc00130 | ordinary-paragraph | high | PDF 172

of Q,_,. The following lemma is due to Bernardi (private communication).

## chapter-02-section-03-pc00131 | lemma | high | PDF 172

Lemma 3.4. If the triangulation 7, is regular, the operator p, of orthogonal

## chapter-02-section-03-pc00132 | ordinary-paragraph | high | PDF 172

L?-projection on Q,, satisfies the bound: (3.16) If — Prfllooa<Ch*lfl.g WeH(Q) ford<k<l.

## chapter-02-section-03-pc00133 | proof | high | PDF 172

Proof. Let « be a quadrilateral of %,. Notice that (3.16) would be trivial if the

## chapter-02-section-03-pc00134 | ordinary-paragraph | high | PDF 172

mapping F,, were affine instead of bilinear. So we propose to introduce another

## chapter-02-section-03-pc00135 | ordinary-paragraph | high | PDF 172

a3

## chapter-02-section-03-pc00136 | ordinary-paragraph | high | PDF 172

a

## chapter-02-section-03-pc00137 | ordinary-paragraph | high | PDF 172

(0,0) (1,0) a 1 a,

## chapter-02-section-03-pc00138 | figure | high | PDF 172

Figure 11

## chapter-02-section-03-pc00139 | ordinary-paragraph | medium | PDF 173

"reference" set k—not necessarily the unit square—that is related to k by an affine mapping F. More precisely, let us split k into the two subtriangles (cf.

## chapter-02-section-03-pc00140 | figure | medium | PDF 173

Figure 11):

## chapter-02-section-03-pc00141 | equation | low | PDF 173

[[FORMULA:f-p0173-02591]]

## chapter-02-section-03-pc00142 | ordinary-paragraph | medium | PDF 173

let S, be the reference unit triangle, F the affine mapping such that

## chapter-02-section-03-pc00143 | equation | low | PDF 173

[[FORMULA:f-p0173-02592]]

## chapter-02-section-03-pc00144 | equation | low | PDF 173

[[FORMULA:f-p0173-02593]]

## chapter-02-section-03-pc00145 | ordinary-paragraph | medium | PDF 173

and set

## chapter-02-section-03-pc00146 | equation | low | PDF 173

[[FORMULA:f-p0173-02594]]

## chapter-02-section-03-pc00147 | ordinary-paragraph | medium | PDF 173

In other words,

## chapter-02-section-03-pc00148 | equation | low | PDF 173

[[FORMULA:f-p0173-02595]]

## chapter-02-section-03-pc00149 | equation | low | PDF 173

[[FORMULA:f-p0173-02596]]

## chapter-02-section-03-pc00150 | ordinary-paragraph | medium | PDF 173

As F is affine and k is convex, the reference set k is also a convex quadrilateral. In addition, we readily derive that on the one hand

## chapter-02-section-03-pc00151 | equation | low | PDF 173

[[FORMULA:f-p0173-02597]]

## chapter-02-section-03-pc00152 | equation | low | PDF 173

[[FORMULA:f-p0173-02598]]

## chapter-02-section-03-pc00153 | ordinary-paragraph | medium | PDF 173

where S; (resp. S;) denotes any of the four subtriangles of k (resp. k). On the other hand any two vertices of k satisfy:

## chapter-02-section-03-pc00154 | equation | low | PDF 173

[[FORMULA:f-p0173-02599]]

## chapter-02-section-03-pc00155 | ordinary-paragraph | medium | PDF 173

Furthermore formulas (A.2) and (A.3) give here

## chapter-02-section-03-pc00156 | equation | low | PDF 173

[[FORMULA:f-p0173-02600]]

## chapter-02-section-03-pc00157 | ordinary-paragraph | medium | PDF 173

Now, let fe H*(k) with O ≤ k ≤ l. The L²-projection p, on Pi-1 is invariant under affine transformations. Thus

## chapter-02-section-03-pc00158 | equation | low | PDF 173

[[FORMULA:f-p0173-02602]]

## chapter-02-section-03-pc00159 | ordinary-paragraph | medium | PDF 173

But

## chapter-02-section-03-pc00160 | equation | low | PDF 173

[[FORMULA:f-p0173-02603]]

## chapter-02-section-03-pc00161 | equation | low | PDF 173

[[FORMULA:f-p0173-02604]]

## chapter-02-section-03-pc00162 | ordinary-paragraph | low | PDF 173

qEPj Since k is a variable quadrilateral, we must explicit the constant C(k) such that

## chapter-02-section-03-pc00163 | equation | low | PDF 173

[[FORMULA:f-p0173-02605]]

## chapter-02-section-03-pc00164 | ordinary-paragraph | low | PDF 173

This is done by induction on the degree j. When j = O, which is the only case where we can use Theorem A.3, we get Max,meas(S,) 71/2 Ifl1,es

## chapter-02-section-03-pc00165 | equation | low | PDF 173

[[FORMULA:f-p0173-02607]]

## chapter-02-section-03-pc00166 | ordinary-paragraph | medium | PDF 173

Min,meas(S,) with a constant C, independent of h, K and f. The above remarks concerning the geometry of k imply that:

## chapter-02-section-03-pc00167 | equation | low | PDF 174

[[FORMULA:f-p0174-02608]]

## chapter-02-section-03-pc00168 | equation | low | PDF 174

[[FORMULA:f-p0174-02609]]

## chapter-02-section-03-pc00169 | ordinary-paragraph | medium | PDF 174

Next assume that

## chapter-02-section-03-pc00170 | equation | low | PDF 174

[[FORMULA:f-p0174-02610]]

## chapter-02-section-03-pc00171 | ordinary-paragraph | low | PDF 174

We can write f + q + allo,x

## chapter-02-section-03-pc00172 | equation | low | PDF 174

[[FORMULA:f-p0174-02611]]

## chapter-02-section-03-pc00173 | ordinary-paragraph | low | PDF 174

(q,@)∈ Pj-1xP;

## chapter-02-section-03-pc00174 | equation | low | PDF 174

[[FORMULA:f-p0174-02612]]

## chapter-02-section-03-pc00175 | ordinary-paragraph | low | PDF 174

q∈P;q∈Pj-1

## chapter-02-section-03-pc00176 | equation | low | PDF 174

[[FORMULA:f-p0174-02613]]

## chapter-02-section-03-pc00177 | ordinary-paragraph | low | PDF 174

aePj by the induction hypothesis (3.18). Then (3.17) yields: 1/2

## chapter-02-section-03-pc00178 | equation | low | PDF 174

[[FORMULA:f-p0174-02615]]

## chapter-02-section-03-pc00179 | equation | low | PDF 174

[[FORMULA:f-p0174-02616]]

## chapter-02-section-03-pc00180 | equation | low | PDF 174

[[FORMULA:f-p0174-02617]]

## chapter-02-section-03-pc00181 | ordinary-paragraph | medium | PDF 174

Since the expression in brackets is I flj+1,*, this proves (3.18) for all j. As a consequence, we have:

## chapter-02-section-03-pc00182 | equation | low | PDF 174

[[FORMULA:f-p0174-02619]]

## chapter-02-section-03-pc00183 | ordinary-paragraph | medium | PDF 174

and (3.16) follows from (A.7) and the regularity of h. From Lemma 3.4, (3.15) and Theorem 3.2, we derive the expected estimate for this scheme.

## chapter-02-section-03-pc00184 | theorem | medium | PDF 174

Theorem 3.3. Let Q be a bounded plane polygon and suppose the solution (u, p) of

## chapter-02-section-03-pc00185 | ordinary-paragraph | low | PDF 174

the Stokes system satisfies: u∈ [H*+1(Ω) ∩ H(Ω)]²,  p∈ H*(Ω) N L(Q) for some integer ke [1, I]. If the triangulation J, is regular, the solution (un, pn) of (1.39) with the spaces X, and M, defined by (3.11) (3.12) has the estimate:

## chapter-02-section-03-pc00186 | equation | low | PDF 174

[[FORMULA:f-p0174-02623]]

## chapter-02-section-03-pc00187 | ordinary-paragraph | medium | PDF 174

In addition, if Q is convex we have the L²-estimate:

## chapter-02-section-03-pc00188 | equation | low | PDF 174

[[FORMULA:f-p0174-02624]]

## chapter-02-section-03-pc00189 | subsection | medium | PDF 174

3.3. An Example of Checkerboard Instability: the Q -Po Element

## chapter-02-section-03-pc00190 | ordinary-paragraph | medium | PDF 174,175

The most famous example of spaces failing to satisfy the inf-sup condition is that in which the velocity is made of piecewise polynomials of Q? and the pressure is piecewise constant on a rectangular grid. This combination is more familiarly called the “Q -P。" element. More precisely, let us assume that Ω is a bounded polygon with sides parallel to the axes and, to simplify suppose that T, is a square grid. We take:

## chapter-02-section-03-pc00191 | equation | low | PDF 175

[[FORMULA:f-p0175-02626]]

## chapter-02-section-03-pc00192 | equation | low | PDF 175

[[FORMULA:f-p0175-02627]]

## chapter-02-section-03-pc00193 | equation | low | PDF 175

[[FORMULA:f-p0175-02628]]

## chapter-02-section-03-pc00194 | ordinary-paragraph | medium | PDF 175

(i+1,j+1) (i.j+1)

## chapter-02-section-03-pc00195 | ordinary-paragraph | medium | PDF 175

(i+1/2.j+1/2) Ki.j

## chapter-02-section-03-pc00196 | ordinary-paragraph | medium | PDF 175

(i+1,j) (i.j)

## chapter-02-section-03-pc00197 | figure | medium | PDF 175

Figure 12

## chapter-02-section-03-pc00198 | ordinary-paragraph | medium | PDF 175

This pair of spaces was introduced a long time ago and because of its simplicity was used (and is still used) by many numerical analysts and engineers in connection with the Stokes Problem. But it was soon found out, through numerical instabilities in the approximate pressure, that there was something amiss with this choice of spaces. The most conspicuous anomaly of (3.19) is that Ker(B') is not reduced to {0}. Indeed, let (i,j) be a cartesian enumeration of the nodes of T, like in Figure 12, let ki.j denote the square with bottom left vertex (i,j) and let (i + 1/2,j + 1/2) be the index of the center of ki,§. To alleviate the notations, let v = (u,v) denote a function of X, and let ui,; or vi,; denote the vaiue of u or v at the node (i,j); similarly, we denote by qi+1/2.j+1/2 the value of q at the center of Ki.j. As qe Mh is constant on k;, ; we find immediately:

## chapter-02-section-03-pc00199 | equation | low | PDF 175

[[FORMULA:f-p0175-02631]]

## chapter-02-section-03-pc00200 | ordinary-paragraph | low | PDF 175

Jki.j

## chapter-02-section-03-pc00201 | equation | low | PDF 175

[[FORMULA:f-p0175-02632]]

## chapter-02-section-03-pc00202 | ordinary-paragraph | low | PDF 175

+ (Ui+1,j+1 + Vi,j+1 - Vi+1,j - Vi.j)}. Thus a summation by parts yields:

## chapter-02-section-03-pc00203 | equation | low | PDF 175

[[FORMULA:f-p0175-02633]]

## chapter-02-section-03-pc00204 | equation | low | PDF 175

[[FORMULA:f-p0175-02634]]

## chapter-02-section-03-pc00205 | equation | low | PDF 176

[[FORMULA:f-p0176-02635]]

## chapter-02-section-03-pc00206 | equation | low | PDF 176

[[FORMULA:f-p0176-02636]]

## chapter-02-section-03-pc00207 | ordinary-paragraph | medium | PDF 176

and the summation runs over all interior nodes (i,j) of J, (since v vanishes on F). Therefore, if q belongs to Ker(B'), i.e. if qe M, and

## chapter-02-section-03-pc00208 | equation | low | PDF 176

[[FORMULA:f-p0176-02638]]

## chapter-02-section-03-pc00209 | ordinary-paragraph | low | PDF 176

"XAA we must have

## chapter-02-section-03-pc00210 | equation | low | PDF 176

[[FORMULA:f-p0176-02639]]

## chapter-02-section-03-pc00211 | equation | low | PDF 176

[[FORMULA:f-p0176-02640]]

## chapter-02-section-03-pc00212 | ordinary-paragraph | low | PDF 176

6 b a 。 b b b a D D b b b b b a a a a a b b b b b a a a 9 b a b b b a a a a

## chapter-02-section-03-pc00213 | equation | low | PDF 176

[[FORMULA:f-p0176-02641]]

## chapter-02-section-03-pc00214 | ordinary-paragraph | low | PDF 176

b b b b b a a a a a b b b a a a a b b b b a a a b b b a a a a

## chapter-02-section-03-pc00215 | figure | medium | PDF 176

Figure 13

## chapter-02-section-03-pc00216 | ordinary-paragraph | medium | PDF 176

These equalities do not necessarily imply that q is a constant in Q. Rather, the values of q can alternate between two constants on adjacent elements like in

## chapter-02-section-03-pc00217 | figure | medium | PDF 176

Figure 13. That these constants should be opposite numbers follows from the

## chapter-02-section-03-pc00218 | ordinary-paragraph | medium | PDF 176

fact that fo q dx = 0. Let us characterize more precisely Ker(Bs). To simplify the discussion, it is convenient to suppose that Ω is the square (- 1, 1) x (- 1, 1) and that J, is the even square grid with mesh size

## chapter-02-section-03-pc00219 | equation | low | PDF 176

[[FORMULA:f-p0176-02644]]

## chapter-02-section-03-pc00220 | ordinary-paragraph | medium | PDF 176

and nodes

## chapter-02-section-03-pc00221 | equation | low | PDF 176

[[FORMULA:f-p0176-02645]]

## chapter-02-section-03-pc00222 | equation | low | PDF 176

[[FORMULA:f-p0176-02646]]

## chapter-02-section-03-pc00223 | ordinary-paragraph | medium | PDF 176

(cf. Figure 14). Let μe M, be defined by

## chapter-02-section-03-pc00224 | equation | low | PDF 176

[[FORMULA:f-p0176-02647]]

## chapter-02-section-03-pc00225 | equation | low | PDF 176

[[FORMULA:f-p0176-02648]]

## chapter-02-section-03-pc00226 | ordinary-paragraph | low | PDF 176

Vkii C Jh.

## chapter-02-section-03-pc00227 | figure | high | PDF 177

Figure 14

## chapter-02-section-03-pc00228 | ordinary-paragraph | medium | PDF 177,178

It stems from the above considerations that (3223) Ker(B,,) = span(y). Because of its alternate “plus and minus” pattern, the function p is called a checkerboard function. Its connection with Ker(B,,) was first reported by Fortin [28] and then by Sani et al. [70]. In view of (3.23), the pair of spaces (X,,, M,,) has no chance of satisfying the inf-sup condition. To save the situation, the first step we can take is to replace M,, by [Ker(B;,)]+. Let us characterize this space. Let J = 2i+ landJ = 2j + 1 for —n <i,j <n-—1 and let the macro-element @, , be the union of the four squares k with common vertex (I, J). Following Johnson & Pitkaranta [46], for each (I, J) we introduce the four functions (v,);,;1<k<4 which take the value +1 on the subsquares of Q, ,a ccording to the pattern of Figure 15. Note that (3.24) | (v,); 34x =0 whenk #1 1

## chapter-02-section-03-pc00229 | ordinary-paragraph | low | PDF 178

1 (vJ (v3)1.) (v2h.] (vh.)

## chapter-02-section-03-pc00230 | figure | medium | PDF 178

Figure 15

## chapter-02-section-03-pc00231 | ordinary-paragraph | medium | PDF 178

and

## chapter-02-section-03-pc00232 | equation | low | PDF 178

[[FORMULA:f-p0178-02657]]

## chapter-02-section-03-pc00233 | equation | low | PDF 178

[[FORMULA:f-p0178-02658]]

## chapter-02-section-03-pc00234 | ordinary-paragraph | low | PDF 178

JQ1.J Taking into account (3.24), it is easy to see that (3.19) defines M, as follows: 4

## chapter-02-section-03-pc00235 | equation | low | PDF 178

[[FORMULA:f-p0178-02660]]

## chapter-02-section-03-pc00236 | equation | low | PDF 178

[[FORMULA:f-p0178-02661]]

## chapter-02-section-03-pc00237 | ordinary-paragraph | medium | PDF 178

Furthermore since the spurious function μ can only arise from the "local alternating" function v4, we have in view of (3.25): 4

## chapter-02-section-03-pc00238 | equation | low | PDF 178

[[FORMULA:f-p0178-02663]]

## chapter-02-section-03-pc00239 | equation | low | PDF 178

[[FORMULA:f-p0178-02664]]

## chapter-02-section-03-pc00240 | equation | low | PDF 178

[[FORMULA:f-p0178-02665]]

## chapter-02-section-03-pc00241 | ordinary-paragraph | medium | PDF 178

To simplify we use the notation:

## chapter-02-section-03-pc00242 | equation | low | PDF 178

[[FORMULA:f-p0178-02666]]

## chapter-02-section-03-pc00243 | equation | low | PDF 178

[[FORMULA:f-p0178-02667]]

## chapter-02-section-03-pc00244 | ordinary-paragraph | medium | PDF 178

Since we are working with finite dimensional spaces the pair (X,, M ,) satisfies the inf-sup condition (1.12). Unfortunately this is not the end of trouble for, as we are going to see below, the condition is not uniformly satisfied with respect to h,

## chapter-02-section-03-pc00245 | lemma | medium | PDF 178

Lemma 3.5. Let Q be like above and let the spaces X, and M, be defined by (3.19)

## chapter-02-section-03-pc00246 | ordinary-paragraph | medium | PDF 178

and (3.26) respectively. There exists a constant C > 0, independent of h, such that:

## chapter-02-section-03-pc00247 | equation | low | PDF 178

[[FORMULA:f-p0178-02671]]

## chapter-02-section-03-pc00248 | ordinary-paragraph | medium | PDF 178

qdiv v dx

## chapter-02-section-03-pc00249 | equation | low | PDF 178

[[FORMULA:f-p0178-02672]]

## chapter-02-section-03-pc00250 | equation | low | PDF 178

[[FORMULA:f-p0178-02673]]

## chapter-02-section-03-pc00251 | ordinary-paragraph | low | PDF 178

Vqe Mh. vl1,Ω VEXn Ω

## chapter-02-section-03-pc00252 | proof | medium | PDF 178

Proof. Let q be an arbitrary function of .M,; we introduce the discrete seminorm:

## chapter-02-section-03-pc00253 | ordinary-paragraph | medium | PDF 178

1/2

## chapter-02-section-03-pc00254 | equation | low | PDF 178

[[FORMULA:f-p0178-02674]]

## chapter-02-section-03-pc00255 | equation | low | PDF 178

[[FORMULA:f-p0178-02675]]

## chapter-02-section-03-pc00256 | equation | low | PDF 178

[[FORMULA:f-p0178-02676]]

## chapter-02-section-03-pc00257 | ordinary-paragraph | medium | PDF 178

where the summation runs over all interior nodes (i,j) of T,. In view of (3.20), we define the function v = (u, v) of X, by:

## chapter-02-section-03-pc00258 | equation | low | PDF 178

[[FORMULA:f-p0178-02679]]

## chapter-02-section-03-pc00259 | equation | low | PDF 178

[[FORMULA:f-p0178-02680]]

## chapter-02-section-03-pc00260 | ordinary-paragraph | medium | PDF 179

on all interior nodes (i,j) of ,. With this choice we have:

## chapter-02-section-03-pc00261 | equation | low | PDF 179

[[FORMULA:f-p0179-02681]]

## chapter-02-section-03-pc00262 | ordinary-paragraph | medium | PDF 179

and by virtue of Lemma A.6, an easy calculation gives:

## chapter-02-section-03-pc00263 | equation | low | PDF 179

[[FORMULA:f-p0179-02682]]

## chapter-02-section-03-pc00264 | ordinary-paragraph | medium | PDF 179

Therefore

## chapter-02-section-03-pc00265 | equation | low | PDF 179

[[FORMULA:f-p0179-02683]]

## chapter-02-section-03-pc00266 | equation | low | PDF 179

[[FORMULA:f-p0179-02684]]

## chapter-02-section-03-pc00267 | ordinary-paragraph | low | PDF 179

Ω and (3.27) will be established if we show the following analogue of Theorem I.1.9: "mbA

## chapter-02-section-03-pc00268 | equation | low | PDF 179

[[FORMULA:f-p0179-02686]]

## chapter-02-section-03-pc00269 | equation | low | PDF 179

[[FORMULA:f-p0179-02687]]

## chapter-02-section-03-pc00270 | ordinary-paragraph | medium | PDF 179

Let us prove (3.29). First a straightforward, constructive argument shows that (3.29) holds for every function q of Q, that vanishes on two elements Ki, j: one with i + j even and one with i + j odd. And of course the constant C, is independent of h and q. Next, if q belongs to M, it is easy to find q e Ker(B') ① R such that q -- q is like above. Then the orthogonality of q and q implies that

## chapter-02-section-03-pc00271 | equation | low | PDF 179

[[FORMULA:f-p0179-02691]]

## chapter-02-section-03-pc00272 | ordinary-paragraph | low | PDF 179

For a long time it was conjectured that (3.27) could not be improved; but it is only recently that Boland & Nicolaides [12] established it with the following counter-example. Roughly speaking, the idea is to find a function q in .M , such that [vl1,2 q divvdx Ω is small while Il q ll o.o is large. More precisely let

## chapter-02-section-03-pc00273 | equation | low | PDF 179

[[FORMULA:f-p0179-02693]]

## chapter-02-section-03-pc00274 | equation | low | PDF 179

[[FORMULA:f-p0179-02694]]

## chapter-02-section-03-pc00275 | ordinary-paragraph | low | PDF 179

I.J On the one hand, q is indeed in .M, because I runs over integers of opposite signs. On the other hand, a simple calculation shows that:

## chapter-02-section-03-pc00276 | equation | low | PDF 179

[[FORMULA:f-p0179-02695]]

## chapter-02-section-03-pc00277 | ordinary-paragraph | medium | PDF 179

Thus

## chapter-02-section-03-pc00278 | equation | low | PDF 179

[[FORMULA:f-p0179-02696]]

## chapter-02-section-03-pc00279 | equation | low | PDF 179

[[FORMULA:f-p0179-02697]]

## chapter-02-section-03-pc00280 | ordinary-paragraph | medium | PDF 179

Next, let us evaluate fo q div v dx. According to (3.21) we have: if i is odd, 0

## chapter-02-section-03-pc00281 | equation | low | PDF 180

[[FORMULA:f-p0180-02699]]

## chapter-02-section-03-pc00282 | equation | low | PDF 180

[[FORMULA:f-p0180-02700]]

## chapter-02-section-03-pc00283 | equation | low | PDF 180

[[FORMULA:f-p0180-02701]]

## chapter-02-section-03-pc00284 | ordinary-paragraph | low | PDF 180

VQ f(2j+1)h 0v(2ih, x2)/0x2 dx2

## chapter-02-section-03-pc00285 | equation | low | PDF 180

[[FORMULA:f-p0180-02702]]

## chapter-02-section-03-pc00286 | equation | low | PDF 180

[[FORMULA:f-p0180-02703]]

## chapter-02-section-03-pc00287 | ordinary-paragraph | low | PDF 180

2jh Z 0v(2ih, x2)/0x2 dx2

## chapter-02-section-03-pc00288 | equation | low | PDF 180

[[FORMULA:f-p0180-02704]]

## chapter-02-section-03-pc00289 | ordinary-paragraph | medium | PDF 180

Hence

## chapter-02-section-03-pc00290 | equation | low | PDF 180

[[FORMULA:f-p0180-02705]]

## chapter-02-section-03-pc00291 | ordinary-paragraph | medium | PDF 180

[0v(2ih, x2)/0x21 dx2

## chapter-02-section-03-pc00292 | equation | low | PDF 180

[[FORMULA:f-p0180-02706]]

## chapter-02-section-03-pc00293 | ordinary-paragraph | low | PDF 180

Ω n-1

## chapter-02-section-03-pc00294 | equation | low | PDF 180

[[FORMULA:f-p0180-02707]]

## chapter-02-section-03-pc00295 | equation | low | PDF 180

[[FORMULA:f-p0180-02708]]

## chapter-02-section-03-pc00296 | equation | low | PDF 180

[[FORMULA:f-p0180-02709]]

## chapter-02-section-03-pc00297 | ordinary-paragraph | medium | PDF 180

Now observe that for every affine function f, the following quadrature formula holds:

## chapter-02-section-03-pc00298 | equation | low | PDF 180

[[FORMULA:f-p0180-02710]]

## chapter-02-section-03-pc00299 | equation | low | PDF 180

[[FORMULA:f-p0180-02711]]

## chapter-02-section-03-pc00300 | ordinary-paragraph | medium | PDF 180

in view of the inequality

## chapter-02-section-03-pc00301 | equation | low | PDF 180

[[FORMULA:f-p0180-02712]]

## chapter-02-section-03-pc00302 | equation | low | PDF 180

[[FORMULA:f-p0180-02713]]

## chapter-02-section-03-pc00303 | ordinary-paragraph | low | PDF 180

As a consequence 1 n-

## chapter-02-section-03-pc00304 | equation | low | PDF 180

[[FORMULA:f-p0180-02714]]

## chapter-02-section-03-pc00305 | ordinary-paragraph | medium | PDF 180

10v(x1, x2)/0x212 dx1. iz-(n-1) (Here we use the fact that Ou/ox, is a continuous and piecewise affine function of x1). Therefore,

## chapter-02-section-03-pc00306 | equation | low | PDF 180

[[FORMULA:f-p0180-02715]]

## chapter-02-section-03-pc00307 | ordinary-paragraph | medium | PDF 180

Combined with (3.31), this becomes:

## chapter-02-section-03-pc00308 | equation | low | PDF 180

[[FORMULA:f-p0180-02717]]

## chapter-02-section-03-pc00309 | equation | low | PDF 180

[[FORMULA:f-p0180-02718]]

## chapter-02-section-03-pc00310 | ordinary-paragraph | medium | PDF 180

Thus we have proved the following resuit:

## chapter-02-section-03-pc00311 | lemma | medium | PDF 180

Lemma 3.6. Under the hypotheses of Lemma 3.5, the function q defined by (3.30)

## chapter-02-section-03-pc00312 | ordinary-paragraph | low | PDF 180,181

belongs to M, and satisfies: [(

## chapter-02-section-03-pc00313 | equation | low | PDF 181

[[FORMULA:f-p0181-02720]]

## chapter-02-section-03-pc00314 | equation | low | PDF 181

[[FORMULA:f-p0181-02721]]

## chapter-02-section-03-pc00315 | equation | low | PDF 181

[[FORMULA:f-p0181-02722]]

## chapter-02-section-03-pc00316 | ordinary-paragraph | low | PDF 181

VeXh Together with Lemma 3.5, this means that the constant β* is really O(h). In fact, it can be proved that this undesirable factor h arises exclusively from the local alternating component v4 in the functions of M,. Again let us write qE M, in terms of the basis functions vk: 4

## chapter-02-section-03-pc00317 | equation | low | PDF 181

[[FORMULA:f-p0181-02723]]

## chapter-02-section-03-pc00318 | ordinary-paragraph | low | PDF 181

where (akvk)I,J, (α)1,J∈ R,

## chapter-02-section-03-pc00319 | equation | low | PDF 181

[[FORMULA:f-p0181-02724]]

## chapter-02-section-03-pc00320 | ordinary-paragraph | low | PDF 181

Z(a)1,J Following Boland & Nicolaides [12] we split .l, as follows:

## chapter-02-section-03-pc00321 | equation | low | PDF 181

[[FORMULA:f-p0181-02725]]

## chapter-02-section-03-pc00322 | ordinary-paragraph | medium | PDF 181

where

## chapter-02-section-03-pc00323 | equation | low | PDF 181

[[FORMULA:f-p0181-02726]]

## chapter-02-section-03-pc00324 | equation | low | PDF 181

[[FORMULA:f-p0181-02727]]

## chapter-02-section-03-pc00325 | equation | low | PDF 181

[[FORMULA:f-p0181-02728]]

## chapter-02-section-03-pc00326 | ordinary-paragraph | medium | PDF 181

and we associate with these spaces the following subspace of Xh:

## chapter-02-section-03-pc00327 | equation | low | PDF 181

[[FORMULA:f-p0181-02729]]

## chapter-02-section-03-pc00328 | equation | low | PDF 181

[[FORMULA:f-p0181-02730]]

## chapter-02-section-03-pc00329 | ordinary-paragraph | medium | PDF 181

We propose to establish that the pair ( V, M,) satisfies a uniform inf-sup condition. To this end, let us start with a local condition.

## chapter-02-section-03-pc00330 | lemma | medium | PDF 181

Lemma 3.7. With the above notations and hypotheses of Lemma 3.5, the pair

## chapter-02-section-03-pc00331 | ordinary-paragraph | low | PDF 181

(Vh, Mn) satisfies uniformly a local inf-sup condition with respect to the partition {21,1} of .

## chapter-02-section-03-pc00332 | proof | medium | PDF 181

Proof. Let

## chapter-02-section-03-pc00333 | equation | low | PDF 181

[[FORMULA:f-p0181-02733]]

## chapter-02-section-03-pc00334 | equation | low | PDF 181

[[FORMULA:f-p0181-02734]]

## chapter-02-section-03-pc00335 | ordinary-paragraph | medium | PDF 181

We must show that all qe M,(Qi.J) satisfy:

## chapter-02-section-03-pc00336 | equation | low | PDF 181

[[FORMULA:f-p0181-02735]]

## chapter-02-section-03-pc00337 | equation | low | PDF 181

[[FORMULA:f-p0181-02736]]

## chapter-02-section-03-pc00338 | equation | low | PDF 181

[[FORMULA:f-p0181-02737]]

## chapter-02-section-03-pc00339 | equation | low | PDF 181

[[FORMULA:f-p0181-02738]]

## chapter-02-section-03-pc00340 | ordinary-paragraph | low | PDF 181

veXno.) LJQ.) First, observe that

## chapter-02-section-03-pc00341 | equation | low | PDF 181

[[FORMULA:f-p0181-02739]]

## chapter-02-section-03-pc00342 | ordinary-paragraph | medium | PDF 181,182

where Φi.s denotes the basis function of X, that takes the value 1 at the node Then formula (3.20) yields for all ve X,(Q, J) and qe M,(Q1,J):

## chapter-02-section-03-pc00343 | equation | low | PDF 182

[[FORMULA:f-p0182-02741]]

## chapter-02-section-03-pc00344 | ordinary-paragraph | low | PDF 182

J21.J where

## chapter-02-section-03-pc00345 | equation | low | PDF 182

[[FORMULA:f-p0182-02742]]

## chapter-02-section-03-pc00346 | ordinary-paragraph | medium | PDF 182

By choosing

## chapter-02-section-03-pc00347 | equation | low | PDF 182

[[FORMULA:f-p0182-02743]]

## chapter-02-section-03-pc00348 | equation | low | PDF 182

[[FORMULA:f-p0182-02744]]

## chapter-02-section-03-pc00349 | ordinary-paragraph | medium | PDF 182

we immediately obtain (3.34) with C = (3/8)1/2. Thus setting,

## chapter-02-section-03-pc00350 | equation | low | PDF 182

[[FORMULA:f-p0182-02746]]

## chapter-02-section-03-pc00351 | ordinary-paragraph | medium | PDF 182

it follows from Theorem 1.12 that (V, M,) satisfies a uniform inf-sup condition provided the same is true for the pair (Vh, Mh). This last property is less obvious. In order to prove it, it is convenient to group the macro-elements Q.y four by four like in Figure 16; and of course we must assume that these super macroelements Oa,g form again a partition of Q. Then we proceed in two steps. First we introduce the subspace of M,:

## chapter-02-section-03-pc00352 | equation | low | PDF 182

[[FORMULA:f-p0182-02748]]

## chapter-02-section-03-pc00353 | ordinary-paragraph | medium | PDF 182

and we prove that the pair (V, Mzh) satisfies a uniform inf-sup condition. Next we show that the pair (V, Mh) satisfies a local inf sup-condition on each set Oa.8- This is achieved in the next two lemmas.

## chapter-02-section-03-pc00354 | ordinary-paragraph | medium | PDF 182

(α-1.β+1) (α+1,β3+1) 2h

## chapter-02-section-03-pc00355 | ordinary-paragraph | medium | PDF 182

(α.β) 2h (α-1,β-1) (α+1.β-1)

## chapter-02-section-03-pc00356 | ordinary-paragraph | medium | PDF 182

2h 2h

## chapter-02-section-03-pc00357 | lemma | medium | PDF 183

Lemma 3.8. Assume that Q can be partitioned into groups @a.p of four macro-

## chapter-02-section-03-pc00358 | ordinary-paragraph | medium | PDF 183

elements Q1.s like in Figure 16. Then the pair (Vh, Mzn) satisfies a global uniform inf-sup condition.

## chapter-02-section-03-pc00359 | proof | medium | PDF 183

Proof. First, observe that the functions of X2, belong necessarily to V, because

## chapter-02-section-03-pc00360 | ordinary-paragraph | medium | PDF 183

their divergence reduces to polynomials of P, in each macro-element Q, j and

## chapter-02-section-03-pc00361 | equation | low | PDF 183

[[FORMULA:f-p0183-02752]]

## chapter-02-section-03-pc00362 | ordinary-paragraph | low | PDF 183

JS1.3 Therefore let us prove the inf-sup condition for the pair (Xzh, M2h). For this, we exhibit an adequate operator 7, very similar to that of Lemma

## chapter-02-section-03-pc00363 | subsection | medium | PDF 183

2.2. Let R, be the local regularization operator of Section A.3 and let us fix one

## chapter-02-section-03-pc00364 | ordinary-paragraph | low | PDF 183

of the super macro-elements O.s. For v in H′(Oa.s) we define mveQ1 on each Ω1,J C Oa,p by:

## chapter-02-section-03-pc00365 | equation | low | PDF 183

[[FORMULA:f-p0183-02754]]

## chapter-02-section-03-pc00366 | equation | low | PDF 183

[[FORMULA:f-p0183-02755]]

## chapter-02-section-03-pc00367 | ordinary-paragraph | medium | PDF 183

T Then, we take Thv = tv on each Oa.b. By inspection, it easy to verify that π, E (H(Q)²; Xzh) and

## chapter-02-section-03-pc00368 | equation | low | PDF 183

[[FORMULA:f-p0183-02757]]

## chapter-02-section-03-pc00369 | ordinary-paragraph | low | PDF 183

JΩ Furthermore a simple argument shows that

## chapter-02-section-03-pc00370 | equation | low | PDF 183

[[FORMULA:f-p0183-02758]]

## chapter-02-section-03-pc00371 | ordinary-paragraph | medium | PDF 183

This yields the desired inf-sup condition,

## chapter-02-section-03-pc00372 | lemma | medium | PDF 183

Lemma 3.9. On each Ca.p, the pair of spaces (V,Mh) satisfies a local inf-sup

## chapter-02-section-03-pc00373 | ordinary-paragraph | medium | PDF 183

condition.

## chapter-02-section-03-pc00374 | proof | medium | PDF 183

Proof. Let q belong to the space:

## chapter-02-section-03-pc00375 | equation | low | PDF 183

[[FORMULA:f-p0183-02761]]

## chapter-02-section-03-pc00376 | ordinary-paragraph | medium | PDF 183

We must construct v in V, with vlao., = 0 such that

## chapter-02-section-03-pc00377 | equation | low | PDF 183

[[FORMULA:f-p0183-02763]]

## chapter-02-section-03-pc00378 | equation | low | PDF 183

[[FORMULA:f-p0183-02764]]

## chapter-02-section-03-pc00379 | equation | low | PDF 183

[[FORMULA:f-p0183-02765]]

## chapter-02-section-03-pc00380 | ordinary-paragraph | low | PDF 183

JOα.8 Let us fix v = 0 on the boundary and central nodes of Oa,s and also at the central node of each macro-element Ω1.j contained in Oa.s. Then, in view of the formula

## chapter-02-section-03-pc00381 | equation | low | PDF 184

[[FORMULA:f-p0184-02767]]

## chapter-02-section-03-pc00382 | ordinary-paragraph | high | PDF 184

on all remaining nodes (i,j) of O,,¢ (i.e. (a + 1, B),(% B + 1)). Wecan easily see that

## chapter-02-section-03-pc00383 | equation | low | PDF 184

[[FORMULA:f-p0184-02768]]

## chapter-02-section-03-pc00384 | ordinary-paragraph | high | PDF 184

Hence the resulting function v belongs to V,, and satisfies

## chapter-02-section-03-pc00385 | equation | low | PDF 184

[[FORMULA:f-p0184-02769]]

## chapter-02-section-03-pc00386 | ordinary-paragraph | high | PDF 184

oO, B i,j Then (3.35) follows from the inequality: 1/2 2

## chapter-02-section-03-pc00387 | equation | low | PDF 184

[[FORMULA:f-p0184-02771]]

## chapter-02-section-03-pc00388 | ordinary-paragraph | high | PDF 184

ij with a constant C, independent of h, « and f, and 2 lta ar |v; ;|7} Z 2) I4r.3l iF Tf considering that ),,; q;,; = 0 since ge Lo(,,g ). C] Lemmas 3.7, 3.8 and 3.9 yield immediately the next result.

## chapter-02-section-03-pc00389 | theorem | high | PDF 184

Theorem 3.4. Assume that Q can be partitioned into groups ©,, p Of four macro-

## chapter-02-section-03-pc00390 | ordinary-paragraph | high | PDF 184

elements like in Figure 16. Then the pair (V,,M,) defined by (3.33) and (3.32) satisfies a uniform inf-sup condition.

## chapter-02-section-03-pc00391 | remark | high | PDF 184

Remark 3.1. The argument of Lemma 3.8 can be used directly to show that the

## chapter-02-section-03-pc00392 | ordinary-paragraph | high | PDF 184

pair (X;,, M,,) satisfies a uniform inf-sup condition but this does not imply that (V,, M,,) satisfies it as well.

## chapter-02-section-03-pc00393 | remark | high | PDF 184

Remark 3.2. The above analysis does not apply directly to arbitrary quadrilat-

## chapter-02-section-03-pc00394 | ordinary-paragraph | high | PDF 184

erals. Usually, the “checkerboard” spurious pressure disappears from M, but the inf-sup condition is not satisfied (cf. Sani et al [70]). However, it is possible to derive similar results for special quadrilateral meshes (cf. Pitkaranta & Stenberg [65]).

## chapter-02-section-03-pc00395 | subsection | high | PDF 184

3.4. Error Estimates for the Q ,—P, Element

## chapter-02-section-03-pc00396 | ordinary-paragraph | high | PDF 184,185

The object of this section is to show that, although it does not satisfy the inf-sup condition, the pair of spaces (X;,, M,,) can still be used to compute successfully the velocity u and (with some precautions) the pressure p. For this purpose, the statement of Theorem 3.4 will play a crucial role. Let (u,, p,)€X, x M,, be a solution of: (3.26) aes Ups grad.y, )i—3(Dyy divv,) = <f,v, > aVy,exX

## chapter-02-section-03-pc00397 | equation | low | PDF 185

[[FORMULA:f-p0185-02779]]

## chapter-02-section-03-pc00398 | ordinary-paragraph | high | PDF 185

with X, and M,, defined by (3.19). We know that u, is unique but that each p, is of the form:

## chapter-02-section-03-pc00399 | equation | low | PDF 185

[[FORMULA:f-p0185-02781]]

## chapter-02-section-03-pc00400 | ordinary-paragraph | high | PDF 185

with ys defined by (3.22), p? and p,, uniquely determined in A, and M, respectively and C arbitrary. Furthermore, u,¢V, with V;, defined by (3.33) and the pair (u,,B,)€V, x M, is the unique solution of:

## chapter-02-section-03-pc00401 | equation | low | PDF 185

[[FORMULA:f-p0185-02784]]

## chapter-02-section-03-pc00402 | ordinary-paragraph | high | PDF 185

| Therefore, owing to Theorem 3.4, we can apply straight away Theorem 1.1 2°) with V, and M, instead of X,, and M, respectively: ju — Unl 1.2 + ||P — Prllo,e (3.38) : s

## chapter-02-section-03-pc00403 | equation | low | PDF 185

[[FORMULA:f-p0185-02786]]

## chapter-02-section-03-pc00404 | ordinary-paragraph | high | PDF 185

V,EVn qne My, with a constant C, > 0 independent of h. Hence it remains to investigate the approximation properties of the spaces V, and M,,. As far as V, is concerned, recall that (cf. Lemma 3.8): XG Vig Thus, formula (A.49) yields: (3.39) inf |u — ¥%4|,.9< |u—J,,U|;q9<Cyhlul,q Vue H?(Q)’. tnEeVn Likewise, since M, < M,, formula (A.51) gives: (3.40) inf |lp — G&llo.e< IP — PrrPllo.e < C3h|plig VpeH*(Q). Gn€ Mp These three inequalities are combined in the following theorem.

## chapter-02-section-03-pc00405 | theorem | high | PDF 185

Theorem 3.5. Assume that Q is like in Theorem 3.4 and suppose the solution (u, p)

## chapter-02-section-03-pc00406 | ordinary-paragraph | low | PDF 185,186

of the Stokes system satisfies: ue[H?7(Q)NHj(Q)]?, pe H'(Q)LGN( Q ). Then the solution (u,, p,) of the scheme (3.36) has the error estimate: (3.41) ju — uyl1,a+ lp — Prllo.e < Ch{lul+o IP,li.aa} ; where p,, is the component of p,, in M,. Here the component f, acts as a filter for the pressure p, since it discards p, the supplementary component of p, in A, is bounded. Indeed, it stems from (3.36) that "X"AA

## chapter-02-section-03-pc00407 | equation | low | PDF 186

[[FORMULA:f-p0186-02794]]

## chapter-02-section-03-pc00408 | ordinary-paragraph | medium | PDF 186

Therefore, (pt, divvh)

## chapter-02-section-03-pc00409 | equation | low | PDF 186

[[FORMULA:f-p0186-02795]]

## chapter-02-section-03-pc00410 | equation | low | PDF 186

[[FORMULA:f-p0186-02796]]

## chapter-02-section-03-pc00411 | ordinary-paragraph | low | PDF 186

[vnl1,Q Vh∈Xn It may happen, in the best of cases, that the left-hand side of this inequality is bounded below by Cs Il p llo.s with a constant Cs that does not depend upon h and thus I pllo.o is O(h). However, in the general case, all we can do is apply

## chapter-02-section-03-pc00412 | lemma | medium | PDF 186

Lemma 3.5; it yields the next result.

## chapter-02-section-03-pc00413 | corollary | medium | PDF 186

Corollary 3.1. Under the hypotheses of Theorem 3.5, the component p of p, in Ah

## chapter-02-section-03-pc00414 | ordinary-paragraph | medium | PDF 186

is bounded as follows:

## chapter-02-section-03-pc00415 | equation | low | PDF 186

[[FORMULA:f-p0186-02797]]

## chapter-02-section-03-pc00416 | equation | low | PDF 186

[[FORMULA:f-p0186-02798]]

## chapter-02-section-03-pc00417 | ordinary-paragraph | medium | PDF 186

Finally, we can also apply Theorem 1.2 with the pair of spaces (V, M,) and derive an optimal error estimate for Ilu - u, llo.Ω.

## chapter-02-section-03-pc00418 | corollary | medium | PDF 186

Corollary 3.2. Under the hypotheses of Theorem 3.5, we have:

## chapter-02-section-03-pc00419 | equation | low | PDF 186

[[FORMULA:f-p0186-02799]]

## chapter-02-section-03-pc00420 | equation | low | PDF 186

[[FORMULA:f-p0186-02800]]

## chapter-02-section-03-pc00421 | equation | low | PDF 186

[[FORMULA:f-p0186-02801]]

## chapter-02-section-03-pc00422 | equation | low | PDF 186

[[FORMULA:f-p0186-02802]]

## chapter-02-section-03-pc00423 | equation | low | PDF 186

[[FORMULA:f-p0186-02803]]

## chapter-02-section-03-pc00424 | equation | low | PDF 186

[[FORMULA:f-p0186-02804]]

## chapter-02-section-03-pc00425 | equation | low | PDF 186

[[FORMULA:f-p0186-02805]]

## chapter-02-section-03-pc00426 | ordinary-paragraph | medium | PDF 186

(1.-1)

## chapter-02-section-03-pc00427 | equation | low | PDF 186

[[FORMULA:f-p0186-02806]]

## chapter-02-section-03-pc00428 | equation | low | PDF 186

[[FORMULA:f-p0186-02807]]

## chapter-02-section-03-pc00429 | ordinary-paragraph | medium | PDF 186

K

## chapter-02-section-03-pc00430 | equation | low | PDF 186

[[FORMULA:f-p0186-02808]]

## chapter-02-section-03-pc00431 | equation | low | PDF 186

[[FORMULA:f-p0186-02809]]

## chapter-02-section-03-pc00432 | ordinary-paragraph | medium | PDF 186

(-1,1) (-1,-1)

## chapter-02-section-03-pc00433 | equation | low | PDF 186

[[FORMULA:f-p0186-02810]]

## chapter-02-section-03-pc00434 | ordinary-paragraph | medium | PDF 186

(0,0)

## chapter-02-section-03-pc00435 | equation | low | PDF 186

[[FORMULA:f-p0186-02811]]

## chapter-02-section-03-pc00436 | ordinary-paragraph | medium | PDF 186

(0,0)

## chapter-02-section-03-pc00437 | figure | medium | PDF 186

Figure 17
