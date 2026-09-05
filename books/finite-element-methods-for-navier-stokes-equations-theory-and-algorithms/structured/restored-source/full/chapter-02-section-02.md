# Restored-source review candidate: chapter-02-section-02



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 146 / printed 132



[p0146-b0004 | ordinary-paragraph | medium] β

[p0146-b0005 | ordinary-paragraph | medium] 1

[p0146-b0006 | ordinary-paragraph | medium] 2

[p0146-b0007 | ordinary-paragraph | medium] this becomes:

[p0146-b0008 | ordinary-paragraph | medium] aN

[p0146-b0009 | equation | low] (qh,divvn) ≥= Hanl1, + α( 1

[p0146-b0010 | ordinary-paragraph | medium] 2β2

[p0146-b0011 | ordinary-paragraph | medium] Let us choose for example

[p0146-b0012 | ordinary-paragraph | medium] β2

[p0146-b0013 | ordinary-paragraph | medium] N

[p0146-b0014 | ordinary-paragraph | medium] Then (1.57) implies:

[p0146-b0015 | ordinary-paragraph | low] Il ah l10,2

[p0146-b0016 | equation | low] (1.60)

[p0146-b0017 | equation | low] (qh, div vn) ≥ min

[p0146-b0018 | ordinary-paragraph | low] 2'2

[p0146-b0019 | ordinary-paragraph | medium] Finally, we have:

[p0146-b0020 | equation | low] [Vhl1,o ≤ Ihl1, + α/Vnl1,2

[p0146-b0021 | ordinary-paragraph | medium] 1

[p0146-b0022 | ordinary-paragraph | low] α

[p0146-b0023 | equation | low] ≤la llo, +1ahllo.2

[p0146-b0024 | ordinary-paragraph | low] B

[p0146-b0025 | ordinary-paragraph | low] [时+每]

[p0146-b0026 | ordinary-paragraph | low] llahllo,2

[p0146-b0027 | ordinary-paragraph | medium] by virtue of (1.57), (1.58) and (1.59). Combined with (1.60), this last inequality

[p0146-b0028 | ordinary-paragraph | medium] gives the expected inf-sup condition:

[p0146-b0029 | equation | low] (Gh, div vh)

[p0146-b0030 | equation | low] ≥ β* I|ahllo,

[p0146-b0031 | ordinary-paragraph | low] Ivhl1.2

[p0146-b0032 | ordinary-paragraph | medium] with a constant β* that depends solely upon N, β and 2*.

[p0146-b0033 | ordinary-paragraph | medium] The reader can also refer to Stenberg [75] for a related approach.

[p0146-b0034 | ordinary-paragraph | medium] $ 2. Simplicial Finite Element Methods Using Discontinuous

[p0146-b0035 | ordinary-paragraph | medium] Pressures

[p0146-b0036 | ordinary-paragraph | medium] The methods discussed in this paragraph are essentially the oldest finite element

[p0146-b0037 | ordinary-paragraph | medium] methods developed to solve the Stokes and Navier-Stokes problem. Since their

[p0146-b0038 | ordinary-paragraph | medium] first publication by Fortin [29] and by Crouzeix & Raviart [23], they have

[p0146-b0039 | ordinary-paragraph | medium] been substantially simplified and generalized by a number of authors. We shall

## PDF 147 / printed 133



[p0147-b0002 | ordinary-paragraph | high] study here contributions by Bernardi & Raugel [10], Fortin [30], Johnson &

[p0147-b0003 | ordinary-paragraph | high] Pitkaranta [46], Mansfield [56] and Boland & Nicolaides [12].

[p0147-b0004 | ordinary-paragraph | high] The situation and notations are those of Section 1.3.

[p0147-b0005 | subsection | high] 2.1. A First Order Approximation on Triangular Elements

[p0147-b0006 | ordinary-paragraph | high] Throughout this section, we assume that Q is a bounded polygon in R? so that it

[p0147-b0007 | ordinary-paragraph | high] can be entirely triangulated. For each h > 0, J, is a triangulation of Q made of

[p0147-b0008 | ordinary-paragraph | high] triangles k with diameters bound by h:

[p0147-b0009 | ordinary-paragraph | high] Ora \erc

[p0147-b0010 | ordinary-paragraph | high] KeZ,

[p0147-b0011 | ordinary-paragraph | high] By now, the reader is well aware that the choice of compatible spaces X,, and

[p0147-b0012 | ordinary-paragraph | high] M,, whatever their accuracy, is crucial for the success of the approximation. For

[p0147-b0013 | ordinary-paragraph | high] example, the most straightforward choice of first-order spaces is:

[p0147-b0014 | equation | low] W, = {we S(O)wl;,E P? VKeT,},

[p0147-b0015 | equation | low] X, = W,NH3(Q),

[p0147-b0016 | equation | low] 0, = {qEL2(Q);qleePo VET},

[p0147-b0017 | equation | low] M, = 0, L2(Q).

[p0147-b0018 | ordinary-paragraph | high] But, more often than not, this choice leads to V, = {0} as can be checked in the

[p0147-b0019 | ordinary-paragraph | high] simple example of Figure 7. Here, X,, has only two degrees of freedom, while the

[p0147-b0020 | definition | high] definition of V, requires five independent conditions. Hence, V,, = {0}.

[p0147-b0021 | figure | high] Figure 7. Example of incompatible pair of spaces (X,,, M,)

[p0147-b0022 | ordinary-paragraph | high] degrees of

[p0147-b0023 | ordinary-paragraph | high] This example illustrates the fact that the space W, needs more

[p0147-b0024 | ordinary-paragraph | high] freedom in order to generate a sufficiently large space V,. Fortin [29] suggested

## PDF 148 / printed 134



[p0148-b0003 | ordinary-paragraph | high] above pressure space Q,. However, following a further idea of Fortin [30],

[p0148-b0004 | ordinary-paragraph | high] Bernardi & Raugel [10] recently analyzed an intermediate velocity space which

[p0148-b0005 | ordinary-paragraph | high] involves less degrees of freedom and lends itself more readily to higher order

[p0148-b0006 | ordinary-paragraph | high] extensions. We shall study this element in detail.

[p0148-b0007 | ordinary-paragraph | high] Let « be an arbitrary triangle of 7, with vertices a,, a2, a3 like in Figure 8.

[p0148-b0008 | ordinary-paragraph | high] We denote by f; the side opposite a; and by n, and t; the unit outward normal

[p0148-b0009 | ordinary-paragraph | high] and unit tangent to f;. Our aim is a function w with quadratic components in K

[p0148-b0010 | ordinary-paragraph | high] and affine tangential components on each side f; of x:

[p0148-b0011 | ordinary-paragraph | high] wi,EPz, wet,,;e P y.

[p0148-b0012 | ordinary-paragraph | high] This can be achieved by splitting w:

[p0148-b0013 | equation | low] w= Ww, SP Wo

[p0148-b0014 | figure | high] Figure 8

[p0148-b0015 | ordinary-paragraph | high] As an example, observe that the function

[p0148-b0016 | equation | low] Pi =N,/,A3

[p0148-b0017 | ordinary-paragraph | high] vanishes on the sides f, and f; and satisfies p,-t,|,, = 0. Generalizing this

[p0148-b0018 | ordinary-paragraph | high] remark, we set:

[p0148-b0019 | ordinary-paragraph | high] (2.1) Pi =Nj4543, Po = Bored, Ps — Neri

[p0148-b0020 | ordinary-paragraph | high] and we take the velocities w in the polynomial subspace of P?:

[p0148-b0021 | ordinary-paragraph | high] (2.2) P,(k) = P? ® sp{pa,, pno,

[p0148-b0022 | ordinary-paragraph | high] p s}.

[p0148-b0023 | ordinary-paragraph | high] Hence, we propose the following pair of spaces:

[p0148-b0024 | equation | low] ie= {(we@(Q)?; wi.EA(k), VKEI,},

[p0148-b0025 | ordinary-paragraph | high] (2.3) 3

[p0148-b0026 | equation | low] X, = W,0 HG(Q)’,

## PDF 149 / printed 135



[p0149-b0002 | equation | low] a = {qe L*(Q); q|,E Po, Vee F,},

[p0149-b0003 | equation | low] (2.4)

[p0149-b0004 | equation | low] M, = 0,19) L3(Q).

[p0149-b0005 | ordinary-paragraph | high] (The bars on top of X;,, and M, are put to match the notation of Section 1.4.)

[p0149-b0006 | remark | high] Remark 2.1. Let pe Y, (x) and let

[p0149-b0007 | ordinary-paragraph | high] 3

[p0149-b0008 | ordinary-paragraph | high] op 2,p (a,)A;

[p0149-b0009 | ordinary-paragraph | high] denote its standard interpolant on P{. Then since p(a;) = 0 for 1 <i, j <3, p

[p0149-b0010 | ordinary-paragraph | high] has the form:

[p0149-b0011 | ordinary-paragraph | high] 3

[p0149-b0012 | equation | low] p=1,.p+ > ap; witha eR.

[p0149-b0013 | equation | low] i=1

[p0149-b0014 | ordinary-paragraph | high] In addition, since p;|, ,= 0 for i 4 j, we immediately derive that

[p0149-b0015 | equation | low] OL;D il yp,= (p — I,P)| ,-

[p0149-b0016 | ordinary-paragraph | high] This remark suggests to choose the following degrees of freedom for the

[p0149-b0017 | ordinary-paragraph | high] functions of F, (x): the values of p at the vertices a; of « and the flux of p through

[p0149-b0018 | ordinary-paragraph | high] each side f, of x. The next lemma checks the Y; (x)-unisolvence of these degrees

[p0149-b0019 | ordinary-paragraph | high] of freedom.

[p0149-b0020 | lemma | high] Lemma 2.1. A polynomial p of Y,(«) is uniquely determined by:

[p0149-b0021 | equation | low] pia), 1<i<3

[p0149-b0022 | ordinary-paragraph | high] (2.5) :

[p0149-b0023 | equation | low] pnjds, 1<is3.

[p0149-b0024 | ordinary-paragraph | high] Si

[p0149-b0025 | ordinary-paragraph | high] Moreover, on any sidef ,= [a,, a, ] of «, p depends only upon the degrees of freedom

[p0149-b0026 | ordinary-paragraph | high] defined on that side, namely: p(a,), p(a,) and Sr, p:n; ds.

[p0149-b0027 | proof | high] Proof. First, observe that (2.5) involves nine linear conditions and that p has nine

[p0149-b0028 | ordinary-paragraph | high] coefficients. Thus it suffices to prove that if all the degrees of freedom in (2.5)

[p0149-b0029 | ordinary-paragraph | high] vanish then p = 0.

[p0149-b0030 | ordinary-paragraph | high] In view of Remark 2.1, we have I,p= 0. Likewise, |;,a;p;-n;ds = 0; Le.

[p0149-b0031 | ordinary-paragraph | high] [,,%4;4,d=s 0 .H encea ; = 0 for 1 < i <3and therefore p = 0.

[p0149-b0032 | ordinary-paragraph | high] Similarly, if p(a,)= p(a,)= 0 and {;,p°n;ds= 0 we readily find that p| ;, = 0.

[p0149-b0033 | ordinary-paragraph | high] O

[p0149-b0034 | lemma | high] Lemma 2.1 leads to the following interpolation operator:

[p0149-b0035 | ordinary-paragraph | high] for ve $°(Q)’, let r,v be the unique polynomial of Y, (x) defined by:

[p0149-b0036 | equation | low] r,V(a;)=v(a)) 1<is<3,

[p0149-b0037 | equation | low] (2.6)

## PDF 150 / printed 136



[p0150-b0003 | ordinary-paragraph | high] It follows from Lemma 2.1 that

[p0150-b0004 | ordinary-paragraph | high] rhe L(6(Q)?; Wi) L((6°(Q) NN HG (Q))?; X;)-

[p0150-b0005 | ordinary-paragraph | high] However, if we want to check the inf-sup condition—i.e. Hypothesis H3—it is

[p0150-b0006 | ordinary-paragraph | high] convenient, in vew of Lemma 1.1, to work right away with the appropriate

[p0150-b0007 | ordinary-paragraph | high] operator 7,. At first sight, it appears that the above operator r, would do the

[p0150-b0008 | ordinary-paragraph | high] trick since

[p0150-b0009 | ordinary-paragraph | high] 3

[p0150-b0010 | equation | low] |d iv(v —r,v)dx =) | (v —r.v)-n;ds = 0.

[p0150-b0011 | ordinary-paragraph | high] K wl Jf;

[p0150-b0012 | ordinary-paragraph | high] But strictly speaking, r, does not satisfy H3 because it is defined on H*(Q)?

[p0150-b0013 | ordinary-paragraph | high] instead of H!(Q)?. Thus we must replace r, by another operator which does not

[p0150-b0014 | ordinary-paragraph | high] involve the values of v at the vertices of x. The easiest way of turning the difficulty

[p0150-b0015 | ordinary-paragraph | high] consists in replacing the values of v by those of the projection P,v on X,. From

[p0150-b0016 | ordinary-paragraph | high] a practical point of view, this global regularization is not satisfactory because

[p0150-b0017 | ordinary-paragraph | high] the corresponding proof requires the uniform regularity of the triangulation (cf.

[p0150-b0018 | theorem | high] Theorem A.2 and Girault & Raviart [32]). This additional requirement, which

[p0150-b0019 | ordinary-paragraph | high] stems from the global regularization and not from the above approximation, can

[p0150-b0020 | ordinary-paragraph | high] be released by using instead the local regularization operator in Section A.3.

[p0150-b0021 | ordinary-paragraph | high] Thus, following Bernardi & Raugel [10], with each ve Hj(Q)? we associate

[p0150-b0022 | ordinary-paragraph | high] the function w, = R,v¢ ®; where

[p0150-b0023 | equation | low] ®, = ($e CD; $.€P, Vee T,}NH4(Q)

[p0150-b0024 | ordinary-paragraph | high] and R, is defined by (A.53), (A.54). Then we define the operator 2, € Y( Hg (Q)’;

[p0150-b0025 | ordinary-paragraph | high] X,,) by:

[p0150-b0026 | equation | low] T™,V(a) = R,v(a) VWnodea of J,

[p0150-b0027 | equation | low] (2.7)

[p0150-b0028 | ordinary-paragraph | high] |( Vo) ¥) nds OF Vside? of.

[p0150-b0029 | ordinary-paragraph | high] f

[p0150-b0030 | ordinary-paragraph | high] Now assume that the family of triangulations 7, is regular in the sense of

[p0150-b0031 | definition | high] Definition A.2, i.e.

[p0150-b0032 | ordinary-paragraph | high] (2.8) hy/Pe <0 VKEF,, oc independent of h.

[p0150-b0033 | ordinary-paragraph | high] The next lemma shows that 7, satisfies Hypothesis H1 with | = 1 as well as

[p0150-b0034 | ordinary-paragraph | high] Hypothesis H3.

[p0150-b0035 | lemma | high] Lemma 2.2. If the triangulation 7, is regular, then

[p0150-b0036 | ordinary-paragraph | high] (2.9) Iv — T¥Ima< Ch ™|Ving Wwe H*(Q)?

[p0150-b0037 | ordinary-paragraph | high] form = 0 or 1 and k = 1 or 2, with a positive constant C independent of h and vy.

[p0150-b0038 | ordinary-paragraph | high] In addition, whatever the triangulation we have

## PDF 151 / printed 137



[p0151-b0003 | equation | low] (2.10)

[p0151-b0004 | equation | low] div(v - πnv)q dx = 0

[p0151-b0005 | ordinary-paragraph | low] ."ObA

[p0151-b0006 | proof | medium] Proof. As mentioned above, the second equation in (2.7) implies directly (2.10).

[p0151-b0007 | ordinary-paragraph | medium] Let k be an arbitrary triangle of T,. We infer from Remark 2.1 and the first

[p0151-b0008 | ordinary-paragraph | medium] equation in (2.7) that

[p0151-b0009 | ordinary-paragraph | medium] 3

[p0151-b0010 | equation | low] πnV1x=Rhv丨x+

[p0151-b0011 | ordinary-paragraph | low] α;Pi

[p0151-b0012 | equation | low] =1

[p0151-b0013 | ordinary-paragraph | medium] where

[p0151-b0014 | ordinary-paragraph | medium] (v- Rv)·n;ds

[p0151-b0015 | ordinary-paragraph | low] njnk ds

[p0151-b0016 | ordinary-paragraph | low] fi

[p0151-b0017 | ordinary-paragraph | low] fi

[p0151-b0018 | ordinary-paragraph | medium] First, according to Theorem A.4, the operator R, has the following local inter-

[p0151-b0019 | ordinary-paragraph | medium] polation error:

[p0151-b0020 | equation | low] 11v- Rhvllo,x + hx1v -Rnvl1.k ≤ Ch1vlk,4Vv∈ Hk(2)2,

[p0151-b0021 | equation | low] (2.11)

[p0151-b0022 | ordinary-paragraph | medium] k = 1 or 2, where , denotes the union of all elements of , that share at least a

[p0151-b0023 | ordinary-paragraph | medium] vertex with k.

[p0151-b0024 | ordinary-paragraph | medium] Next, formula (A.8) implies that

[p0151-b0025 | equation | low] 1Pi1m.,x ≤ C2|det(Bx)|1/2 1 B1 m|A;Ax lm,

[p0151-b0026 | equation | low] (2.12)

[p0151-b0027 | equation | low] ≤ C3|det(B)|1/2 1/ B-1 |m,

[p0151-b0028 | ordinary-paragraph | medium] since Ii,klm.x is a constant independent of h and k. Similarly,

[p0151-b0029 | ordinary-paragraph | low] A,Ak ds.

[p0151-b0030 | equation | low] ^,^, ds = [meas(f)/meas(f)]

[p0151-b0031 | ordinary-paragraph | medium] Jfi

[p0151-b0032 | ordinary-paragraph | medium] Finally,

[p0151-b0033 | equation | low] (v - R,v) n;ds| ≤ [meas(f)/meas(fi)] 

[p0151-b0034 | ordinary-paragraph | low] I - R,vll ds

[p0151-b0035 | ordinary-paragraph | low] IJsi

[p0151-b0036 | ordinary-paragraph | medium] and

[p0151-b0037 | equation | low] I1 -Rvllds ≤ C4l1--Rvll1,k

[p0151-b0038 | ordinary-paragraph | low] Jsi

[p0151-b0039 | ordinary-paragraph | medium] by the trace Theorem 1.1.5. But we infer from (A.7) and (A.2) that:

[p0151-b0040 | equation | low] |1  Rvll1,x ≤ Cs1det(Bx)-1/2{11v -Rnv12,x + h21v -- Rnvl²,x}1/2.

[p0151-b0041 | ordinary-paragraph | medium] Thus (2.11) yields:

[p0151-b0042 | equation | low] [α;1 ≤ C6|det(Bk)|-1/2hk1vlk,4x

## PDF 152 / printed 138



[p0152-b0003 | ordinary-paragraph | high] 2 oP:

[p0152-b0004 | ordinary-paragraph | high] SONA he

[p0152-b0005 | ordinary-paragraph | high] m,K

[p0152-b0006 | ordinary-paragraph | high] Then with another application of (2.11), we derive:

[p0152-b0007 | equation | low] lv — tVinwes Coo™h* "|v, m= Onl, (ee

[p0152-b0008 | ordinary-paragraph | high] But the regularity of 7, implies that the maximum number of occurrences of a

[p0152-b0009 | ordinary-paragraph | high] given triangle x in the sets 4, is bounded by a fixed constant M independent of

[p0152-b0010 | ordinary-paragraph | high] h and x. Hence

[p0152-b0011 | ordinary-paragraph | high] (2 i, 1/2 Ziv

[p0152-b0012 | ordinary-paragraph | high] KeT,,

[p0152-b0013 | ordinary-paragraph | high] and therefore

[p0152-b0014 | equation | low] lv — TVlm,@ < CgMo™h*™|v\;, 0.

[p0152-b0015 | ordinary-paragraph | high] In particular, when k = m = 1 this establishes the bound (1.20) of Lemma 1.1:

[p0152-b0016 | equation | low] [teVl1.0<(1+CgMo)\vl,q VveHS(Q).

[p0152-b0017 | ordinary-paragraph | high] And when k = 2 and m = 1 this yields Hypothesis H1 with / = 1. O

[p0152-b0018 | ordinary-paragraph | high] Finally, Hypothesis H2 is a direct consequence of Lemma A.5 for the L?-

[p0152-b0019 | ordinary-paragraph | high] projection p, onto Q,:

[p0152-b0020 | ordinary-paragraph | high] (2.13) la — Prdllooa<Chighio VqeH*(Q).

[p0152-b0021 | ordinary-paragraph | high] Since all the assumptions of Theorems 1.8 and 1.9 are satisfied, the following

[p0152-b0022 | ordinary-paragraph | high] convergence result is established for our first-order scheme.

[p0152-b0023 | theorem | high] Theorem 2.1. Suppose Q is a bounded, plane polygon. Let the sclution (u, p) of the

[p0152-b0024 | ordinary-paragraph | high] Stokes problem satisfy:

[p0152-b0025 | ordinary-paragraph | high] ue[H7(Q)N H3(Q)]?, pe H'(Q)N L2(Q)

[p0152-b0026 | ordinary-paragraph | high] and let the spaces X,, and M,, be defined by (2.3) and (2.4) respectively. If the family

[p0152-b0027 | ordinary-paragraph | high] of triangulations 7, is regular then the solution (u,, p;,) of (1.39) satisfies the error

[p0152-b0028 | ordinary-paragraph | high] estimate:

[p0152-b0029 | ordinary-paragraph | high] (2.14) ju—u,l1o+ |p — Pallo.a < Cy A(\uly.o + |Ply, Q):

[p0152-b0030 | ordinary-paragraph | high] In addition, if Q is convex, we have

[p0152-b0031 | ordinary-paragraph | high] (2.15) lu—ulloa< C, h?(( lujn.o0+ IPI, Q).

[p0152-b0032 | remark | high] Remark 2.2. Both upper bounds are stated in terms of seminorms of u and p

[p0152-b0033 | ordinary-paragraph | high] whereas the estimates of Theorems 1.8 and 1.9 involve full norms in their

[p0152-b0034 | ordinary-paragraph | high] right-hand sides. This slight refinement is due to the fact that both (2.11) and

[p0152-b0035 | ordinary-paragraph | high] (2.13) are formulated with seminorms only.

## PDF 153 / printed 139



[p0153-b0002 | subsection | high] 2.2. Higher-Order Approximation on Triangular Elements

[p0153-b0003 | ordinary-paragraph | high] The finite element spaces discussed in this section were introduced by Crouzeix

[p0153-b0004 | ordinary-paragraph | high] & Raviart [23] and Mansfield [56]. They are a direct generalization of the space

[p0153-b0005 | ordinary-paragraph | high] FP, (x). The reader will perhaps find them easy to grasp, but originally their

[p0153-b0006 | ordinary-paragraph | high] analysis was far from trivial on account of the inf-sup condition. Fortunately,

[p0153-b0007 | ordinary-paragraph | high] the material of Section 1.4 has considerably reduced this difficulty.

[p0153-b0008 | ordinary-paragraph | high] In this section, we assume that Q is a bounded, plane polygon. Let us fix an

[p0153-b0009 | ordinary-paragraph | high] integer | > 2. Let 7, be a triangulation of Q and let x be any triangle of 7,. Here

[p0153-b0010 | ordinary-paragraph | high] again, we want to construct velocities with components that are polynomials of

[p0153-b0011 | ordinary-paragraph | high] degree / + 1 and tangential components of degree / on each side of x. But now,

[p0153-b0012 | ordinary-paragraph | high] the higher degree of polynomials provide a simple answer to this problem for it

[p0153-b0013 | ordinary-paragraph | high] suffices that all terms of degree / + 1 vanish on the sides of x; in other words they

[p0153-b0014 | ordinary-paragraph | high] must have the common factor 4,/,/3. More precisely, let us denote by P, the

[p0153-b0015 | ordinary-paragraph | high] space of homogeneous polynomials of degree k:

[p0153-b0016 | ordinary-paragraph | high] Pa sats vies m (Oat uct

[p0153-b0017 | ordinary-paragraph | high] Then we take the velocities w in the polynomial subspace of P?,;:

[p0153-b0018 | ordinary-paragraph | high] (2.16) A(«) = [P,® {AyAgAsPi-2} 1?

[p0153-b0019 | ordinary-paragraph | high] and the pressures q in P,_,. This leads to the following choice of spaces:

[p0153-b0020 | equation | low] {"= {we OQ); whEeAlk) Vee F,},

[p0153-b0021 | ordinary-paragraph | high] DEAD

[p0153-b0022 | ordinary-paragraph | high] ie XW dio (@)

[p0153-b0023 | ordinary-paragraph | high] Oe 0, = {qeEL?(Q); q|.EP-1 Vee T,},

[p0153-b0024 | ordinary-paragraph | high] . M, = 2, L2(2).

[p0153-b0025 | ordinary-paragraph | high] The choice of degrees of freedom for the velocities w is no longer dictated by

[p0153-b0026 | ordinary-paragraph | high] the fulfillment of the inf-sup condition. Therefore we can simply take the values

[p0153-b0027 | ordinary-paragraph | high] of w associated with P, on the sides of « and the derivatives corresponding to

[p0153-b0028 | ordinary-paragraph | high] Pe, atthe center oi K,1.¢::

[p0153-b0029 | ordinary-paragraph | high] (a) w(a) on all points a of 2,f ;, | <i <3, where 2, denotes the

[p0153-b0030 | ordinary-paragraph | high] (2.19) principal lattice of order / (cf. (A.19)),

[p0153-b0031 | ordinary-paragraph | high] (b) d‘w(a,)/éxi 0x4‘ on the center a, of k,0 <i <k,O<k<I—2.

[p0153-b0032 | ordinary-paragraph | high] From a theoretical point of view, derivatives are seldom an attractive choice

[p0153-b0033 | ordinary-paragraph | high] because they require a lot of regularity; they can be replaced by the interior

[p0153-b0034 | ordinary-paragraph | high] moments:

[p0153-b0035 | ordinary-paragraph | high] (2:19) (c) |w ads Vqe P25:

[p0153-b0036 | ordinary-paragraph | high] become:

[p0153-b0037 | ordinary-paragraph | high] In particular, when / = 2, (2.19a) (2.19b) or (2.19c)

## PDF 154 / printed 140



[p0154-b0004 | ordinary-paragraph | medium] (a)

[p0154-b0005 | equation | low] w(a;) on the midpoint a; of the segment [a;,a;], 1 ≤ i < j ≤ 3,

[p0154-b0006 | ordinary-paragraph | medium] w(ar),

[p0154-b0007 | ordinary-paragraph | medium] (b)

[p0154-b0008 | ordinary-paragraph | medium] or

[p0154-b0009 | ordinary-paragraph | medium] wdx.

[p0154-b0010 | ordinary-paragraph | medium] (c)

[p0154-b0011 | ordinary-paragraph | medium] Note that all degrees of freedom (2.19) are defined separately for each component

[p0154-b0012 | ordinary-paragraph | medium] of w. The next lemma checks their unisolvence.

[p0154-b0013 | lemma | medium] Lemma 2.3. A polynomial p of Q;(k) is uniquely determined by the I(l + 5) degrees

[p0154-b0014 | ordinary-paragraph | medium] of freedom (2.19a) (2.19b) or (2.19a) (2.19c). In addition, the restriction of p to any

[p0154-b0015 | ordinary-paragraph | medium] side fi of k depends only upon the degrees of freedom defined on that side.

[p0154-b0016 | proof | medium] Proof. As the dimension of @(k) is l(l + 5) it suffices to show that p = 0 when all

[p0154-b0017 | ordinary-paragraph | medium] its degrees of freedom vanish.

[p0154-b0018 | ordinary-paragraph | medium] Let p be any component of p. If its degrees of freedom are zero on any side

[p0154-b0019 | ordinary-paragraph | medium] f; of k, we readily obtain that p vanishes identically on that side because p reduces

[p0154-b0020 | ordinary-paragraph | medium] to a polynomial of degree I on each side of r. Hence, if the degrees of freedom

[p0154-b0021 | ordinary-paragraph | medium] (2.19a) are zero, we have

[p0154-b0022 | equation | low] p = Aq with q in Pi-2.

[p0154-b0023 | ordinary-paragraph | medium] Then, if all interior degrees of freedom vanish we find in the case of (2.19c):

[p0154-b0024 | equation | low] 23q²dx = 0

[p0154-b0025 | ordinary-paragraph | medium] and in the case of (2.19b):

[p0154-b0026 | equation | low] d*g(a)/oxidx-i = 0 0 ≤i≤k,  0 ≤k≤ 1 -- 2.

[p0154-b0027 | ordinary-paragraph | medium] Each of these equalities implies that q = O in K.

[p0154-b0028 | equation | low] Thus (2.19) yields two interpolation operators:

[p0154-b0029 | ordinary-paragraph | medium] rxv(resp. r'v): the unique polynomial of Q;(k) that has the same degrees of

[p0154-b0030 | ordinary-paragraph | medium] freedom (2.19a) (2.19c) (resp. (2.19a) (2.19b)) as the function v on k. Then we define

[p0154-b0031 | ordinary-paragraph | medium] r, by:

[p0154-b0032 | equation | low] rvlx=rvVK∈h

[p0154-b0033 | ordinary-paragraph | medium] and similarly for r'. Lemma 2.3 implies that:

[p0154-b0034 | ordinary-paragraph | low] rhe (el-2(Q); W)n e([el-2(2)n H(2)]; Xn),

[p0154-b0035 | ordinary-paragraph | low] rne (6(2); W)n e([6(2)n H(2)]2; xn).

[p0154-b0036 | ordinary-paragraph | medium] Furthermore, it is easy to check that both operators r and r' are invariant under

## PDF 155 / printed 141



[p0155-b0002 | ordinary-paragraph | high] affine transformations:

[p0155-b0003 | equation | low] r=,o. V=1Tpgb, ~rv~= Trgd.

[p0155-b0004 | ordinary-paragraph | high] K

[p0155-b0005 | ordinary-paragraph | high] Therefore, since P? is invariant under both r, and r/, we can apply immediately

[p0155-b0006 | corollary | high] Corollary A.2 and derive the following interpolation result:

[p0155-b0007 | lemma | high] Lemma 2.4, If the triangulation J, is regular then the above operator r, satisfies:

[p0155-b0008 | ordinary-paragraph | high] C20) ivi, V0 = Ch’ "lying 9 Wel (OQ). m= Oor 1

[p0155-b0009 | ordinary-paragraph | high] with the integer kE[1,1] and a positive constant C that depends upon k, m, | and

[p0155-b0010 | ordinary-paragraph | high] Q but is independent of h and v.

[p0155-b0011 | ordinary-paragraph | high] Likewise, the operator r, satisfies the bound (2.20) with k = lor 1 —1.

[p0155-b0012 | remark | high] Remark 2.3. This lemma’s proof is trivial because the particularly simple inter-

[p0155-b0013 | ordinary-paragraph | high] polants r, and r, are preserved by affine transformations.

[p0155-b0014 | ordinary-paragraph | high] Now let us examine the inf-sup condition. First, observe that owing to Lemma

[p0155-b0015 | ordinary-paragraph | high] 2.2 the pair of spaces (X,,M,) defined by (2.3) (2.4) satisfies a uniform inf-sup

[p0155-b0016 | ordinary-paragraph | high] condition. Next, the space X, is obviously contained in the space X,, defined by

[p0155-b0017 | ordinary-paragraph | high] (2.17). Therefore, according to Theorem 1.12 if the pair (X,, M,,) given by (2.17)

[p0155-b0018 | ordinary-paragraph | high] (2.18) satisfies the local inf-sup condition stated in Hypothesis H4 then it will also

[p0155-b0019 | ordinary-paragraph | high] satisfy globally a uniform inf-sup condition. Now, in order to check Hypothesis

[p0155-b0020 | ordinary-paragraph | high] H4, one must first choose an appropriate partition {Q,;1 <r < R} of Q. It is

[p0155-b0021 | ordinary-paragraph | high] quite clear that this partition must bear some relation with the triangulation 7,.

[p0155-b0022 | ordinary-paragraph | high] Let us try the easiest guess which consists in taking for partition the triangulation

[p0155-b0023 | ordinary-paragraph | high] itself:

[p0155-b0024 | ordinary-paragraph | high] OF Kk, Keo,

[p0155-b0025 | ordinary-paragraph | high] r

[p0155-b0026 | ordinary-paragraph | high] Thus,

[p0155-b0027 | equation | low] Xy() = {VE A(K); Va. = O},

[p0155-b0028 | ordinary-paragraph | high] (O21) ;

[p0155-b0029 | equation | low] M,(k) = PN Lolk).

[p0155-b0030 | ordinary-paragraph | high] The next theorem establishes that this pair of spaces does indeed satisfy H4.

[p0155-b0031 | theorem | high] Theorem 2.2. Assume that 7, is a regular triangulation of Q. There exists a

[p0155-b0032 | ordinary-paragraph | high] constant 2* > 0, independent of h and x, such that

[p0155-b0033 | ordinary-paragraph | high] (2.22) sup i( gdivv ds)| Ivief ZA* Wllon VaeE M(x).

[p0155-b0034 | ordinary-paragraph | high] ve X,(k)

[p0155-b0035 | proof | high] Proof. Let qé M,(«); we must construct a vector v in X;,(«) such that

[p0155-b0036 | ordinary-paragraph | high] |

[p0155-b0037 | ordinary-paragraph | high] (2.23) (|g divvde) Ive > 2° Vow

## PDF 156 / printed 142



[p0156-b0004 | equation | low] V' grad q dx.

[p0156-b0005 | equation | low] q div v dx :

[p0156-b0006 | ordinary-paragraph | medium] K

[p0156-b0007 | ordinary-paragraph | medium] Then since grad qe P²-2, we can try:

[p0156-b0008 | equation | low] v=-gradq

[p0156-b0009 | ordinary-paragraph | medium] which belongs indeed to P;(k) and vanishes on Ok. With this choice,

[p0156-b0010 | equation | low] Na2ns ∑ (0q/ox;)² dx.

[p0156-b0011 | equation | low] qdiv v dx =

[p0156-b0012 | equation | low] (2.24)

[p0156-b0013 | ordinary-paragraph | medium] Next, a straightforward calculation shows that all polynomials Φ of (say) P

[p0156-b0014 | ordinary-paragraph | medium] satisfy:

[p0156-b0015 | equation | low] 2² dx ≥ C1111,

[p0156-b0016 | equation | low] (2.25)

[p0156-b0017 | ordinary-paragraph | medium] with a constant C, > O independent of k, h and Φ. Indeed, in terms of the reference

[p0156-b0018 | ordinary-paragraph | medium] triangle k we have:

[p0156-b0019 | ordinary-paragraph | low] dx.

[p0156-b0020 | equation | low] 2Φ² dx = [meas(k)/meas(k)]

[p0156-b0021 | ordinary-paragraph | low] k

[p0156-b0022 | ordinary-paragraph | medium] But the mapping

[p0156-b0023 | ordinary-paragraph | medium] 1/2

[p0156-b0024 | ordinary-paragraph | medium] d

[p0156-b0025 | ordinary-paragraph | medium] is a norm on P, equivalent to the L²(k)-norm. Hence

[p0156-b0026 | equation | low] A2 dx ≥ Cl/11,x = C[meas(k)/meas(k)] ll112,x

[p0156-b0027 | ordinary-paragraph | medium] This yields (2.25) with the equivalence constant C. Therefore, combining (2.24)

[p0156-b0028 | ordinary-paragraph | medium] and (2.25) we get:

[p0156-b0029 | equation | low] qdivvdx ≥ Clali,x.

[p0156-b0030 | ordinary-paragraph | medium] Finally, using the argument of Lemma A.6 (cf. formula (A.32)) we get:

[p0156-b0031 | equation | low] [vl1,x ≤ (C2/p) llvllo.x

[p0156-b0032 | ordinary-paragraph | medium] with a constant C2 independent of h, k and v. But

[p0156-b0033 | equation | low] IIvllo,x = I/ N2  gradgllo,x ≤ lal1.r.

[p0156-b0034 | ordinary-paragraph | medium] Hence

[p0156-b0035 | equation | low] [vl1,x ≤(C2/px)lal1.x

## PDF 157 / printed 143



[p0157-b0004 | equation | low] /1vls,x ≥(C/C2)pxlal1,x

[p0157-b0005 | equation | low] q div v dx

[p0157-b0006 | ordinary-paragraph | medium] Therefore the theorem is established provided we show that

[p0157-b0007 | ordinary-paragraph | low] ()"WbA

[p0157-b0008 | equation | low] llqllo.k ≤ C3h,lql1.x

[p0157-b0009 | ordinary-paragraph | medium] with a constant C3 > 0 independent of k, h and q. This will be the object of the

[p0157-b0010 | ordinary-paragraph | medium] next lemma. Assuming this result, we immediately derive that

[p0157-b0011 | equation | low] pxlql1,x ≥(1/C3)(pc/h,) liqllo,x ≥ [1/(cC)] lqllo,x

[p0157-b0012 | ordinary-paragraph | medium] on account of the regularity of Jh.

[p0157-b0013 | lemma | medium] Lemma 2.5. Let k be an N-simplex of R7. There exists a constant C > 0, indepen-

[p0157-b0014 | ordinary-paragraph | medium] dent of h and k such that the following inequality holds for all functions q in

[p0157-b0015 | ordinary-paragraph | low] H'(K) N L2(K):

[p0157-b0016 | equation | low] (2.26)

[p0157-b0017 | equation | low] llq llo,x ≤ Ch,lal1,x.

[p0157-b0018 | proof | medium] Proof. Recall that

[p0157-b0019 | ordinary-paragraph | medium] Vqe La(k).

[p0157-b0020 | equation | low] llqllo,x = inf Ilq + cllo,x 

[p0157-b0021 | ordinary-paragraph | low] CeR

[p0157-b0022 | ordinary-paragraph | medium] Therefore

[p0157-b0023 | equation | low] Ilqllo,x = |det(Bx)1/ inf Ilq + cllo,k

[p0157-b0024 | ordinary-paragraph | low] ceR

[p0157-b0025 | equation | low] ≤ |det(B)|1/2 I|4llH(t)/R

[p0157-b0026 | ordinary-paragraph | medium] Then the equivalence Theorem 1.1.9 yields:

[p0157-b0027 | equation | low] llallo,x ≤ C Idet(Bk)|1/2↓al1,k ≤ C2hlql1,x

[p0157-b0028 | ordinary-paragraph | medium] in view of (A.7) and (A.2).

[p0157-b0029 | remark | medium] Remark 2.4. We know from Theorem 1.1.9 that

[p0157-b0030 | ordinary-paragraph | medium] ()TU()HbA

[p0157-b0031 | equation | low] Ilqllo.x ≤ C(k)lal1,x 

[p0157-b0032 | ordinary-paragraph | medium] but the constant C(k) depends on k and Lemma 2.5 precises this dependence.

[p0157-b0033 | remark | medium] Remark 2.5. Observe that the crucial idea in the proof of Theorem 2.2 is that

[p0157-b0034 | equation | low] grad q belongs to X,(k)

[p0157-b0035 | ordinary-paragraph | low] 1

[p0157-b0036 | equation | low] 1≤i≤N+1

[p0157-b0037 | ordinary-paragraph | medium] whenever q belongs to M,(k). We shall see later on that this fundamental property

## PDF 158 / printed 144



[p0158-b0003 | ordinary-paragraph | high] condition (1.12):

[p0158-b0004 | lemma | high] Lemma 2.6. Let 7, be a regular triangulation of Q and let the spaces X, and M,,

[p0158-b0005 | ordinary-paragraph | high] be defined by (2.17) (2.18). Then there exists a constant p* > 0 independent of h

[p0158-b0006 | ordinary-paragraph | high] such that:

[p0158-b0007 | equation | low] sup (I Gn iV V, ix)l io} > B* \ldnllo,e Vdn€ M,.

[p0158-b0008 | ordinary-paragraph | high] V,E Xn Q

[p0158-b0009 | ordinary-paragraph | high] Again, Hypothesis H2 follows immediately from Lemma A.5 for the L?-

[p0158-b0010 | ordinary-paragraph | high] projection p, onto Q,;:

[p0158-b0011 | ordinary-paragraph | high] (2.27) ld — Prdlloe <Ch'lqh.o VqaeH(Q).

[p0158-b0012 | ordinary-paragraph | high] Thus Theorems 1.8 and 1.9 imply the convergence and error estimates for the

[p0158-b0013 | ordinary-paragraph | high] higher-order schemes.

[p0158-b0014 | theorem | high] Theorem 2.3. Assume that Q is a bounded, plane polygon. Let the solution (u, p) of

[p0158-b0015 | ordinary-paragraph | high] the Stokes problem satisfy:

[p0158-b0016 | ordinary-paragraph | high] ue lL (Q)NHG(Q)), pe H*(Q)NL4(Q)

[p0158-b0017 | ordinary-paragraph | high] for some integer k with 1 < k < | where the integer | > 2; and let the spaces X,, and

[p0158-b0018 | ordinary-paragraph | high] M,, be defined respectively by (2.17) and (2.18). If 7, is a regular family of

[p0158-b0019 | ordinary-paragraph | high] triangulations of Q then the solution (u,, p,) of (1.39) satisfies:

[p0158-b0020 | ordinary-paragraph | high] (2.28) ju — u,l,,0 + ||P — Pallo.e < C,h*((ules1.0 + |Dlx,@)-

[p0158-b0021 | ordinary-paragraph | high] If in addition Q is convex, we have the L?-estimate:

[p0158-b0022 | ordinary-paragraph | high] (2.29) ju — Urnl lo.e < Cah? (lero + |Plx,@):

[p0158-b0023 | remark | high] Remark 2.6. Of course, according to (1.45) the hypotheses of Theorem 2.1 on Q

[p0158-b0024 | ordinary-paragraph | high] and 7, guarantee the convergence of u, and p, without regularity assumption

[p0158-b0025 | ordinary-paragraph | high] on the exact solution u and p.

[p0158-b0026 | subsection | high] 2.3. The Three-Dimensional Case: First and Higher-Order Schemes

[p0158-b0027 | ordinary-paragraph | high] In this section we assume that Q is a bounded polyhedron of R? and 7, is a

[p0158-b0028 | ordinary-paragraph | high] triangulation of Q that consists of tetrahedra « with diameters bounded by h. If

[p0158-b0029 | ordinary-paragraph | high] K is a tetrahedron with vertices a,, a, a3, a4 like in Figure 9 we denote by F, the

[p0158-b0030 | ordinary-paragraph | high] face opposite a;, n; its outward unit normal and e,; the edge [a;, a;].

[p0158-b0031 | ordinary-paragraph | high] We shall develop the first and second-order schemes separately, since they

[p0158-b0032 | ordinary-paragraph | high] are particular cases. The first-order scheme is a very straightforward extension

[p0158-b0033 | ordinary-paragraph | high] of the two-dimensional scheme discussed in Section 2.1 and we shall skim

[p0158-b0034 | ordinary-paragraph | high] through it rapidly. Let « be an arbitrary tetrahedron; what we want is a velocity

## PDF 159 / printed 145



[p0159-b0003 | ordinary-paragraph | medium] 23

[p0159-b0004 | ordinary-paragraph | medium] e34

[p0159-b0005 | ordinary-paragraph | low] eL1

[p0159-b0006 | figure | medium] Figure 9

[p0159-b0007 | ordinary-paragraph | medium] with constant pressures in k. Formulas (2.1) and (2.2) suggest to take w in the

[p0159-b0008 | ordinary-paragraph | medium] space ,(x) with:

[p0159-b0009 | equation | low] (k) = P² ① span{P1,P2,P3,P4} c P3

[p0159-b0010 | ordinary-paragraph | medium] where

[p0159-b0011 | equation | low] (2.30)

[p0159-b0012 | ordinary-paragraph | low] P1 =n4, P2=n241, P3=n4, P4 =n43

[p0159-b0013 | ordinary-paragraph | medium] Note that p; vanishes on all faces F, with j ≠ i and obviously p: x n; = 0 so that

[p0159-b0014 | equation | low] P; × nlok = 0 1 ≤i ≤ 4.

[p0159-b0015 | ordinary-paragraph | medium] As far as the degrees of freedom of w are concerned we can easily take the values

[p0159-b0016 | ordinary-paragraph | medium] of w at the vertices a; of k and its flux through each face F,. The argument of

[p0159-b0017 | lemma | medium] Lemma 2.1 shows that these 16 degrees of freedom are P, (k)-unisolvent:

[p0159-b0018 | lemma | medium] Lemma 2.7. A polynomial p of P,(r) is uniquely determined by the 16 values:

[p0159-b0019 | equation | low] p(ai) 1≤i≤4,

[p0159-b0020 | equation | low] (2.31)

[p0159-b0021 | ordinary-paragraph | medium] p·n;ds

[p0159-b0022 | equation | low] 1≤i≤4.

[p0159-b0023 | ordinary-paragraph | low] Fi

[p0159-b0024 | ordinary-paragraph | medium] In addition, on any face F; of r, p depends only upon the degrees of freedom defined

[p0159-b0025 | ordinary-paragraph | medium] on that face.

[p0159-b0026 | ordinary-paragraph | medium] The corresponding velocity and pressure spaces are:

[p0159-b0027 | equation | low] Wh = {w∈(6o(2)3; wlk∈の,(k) VK∈ Th},

[p0159-b0028 | equation | low] (2.32)

[p0159-b0029 | equation | low] X, = W,NH(Q),

[p0159-b0030 | equation | low] Qh = {q∈ L²(Ω); qlx∈P。 VK∈ Th},

## PDF 160 / printed 146



[p0160-b0003 | ordinary-paragraph | high] on FY,( xk) by:

[p0160-b0004 | equation | low] r.V(a;) = V(a;), | (r,v—v):njds=0, 1<ij<4

[p0160-b0005 | ordinary-paragraph | high] F;

[p0160-b0006 | ordinary-paragraph | high] But like in the two-dimensional case, this operator will not satisfy Hypothesis

[p0160-b0007 | ordinary-paragraph | high] H3 because it is not defined on H!(Q)%. Therefore, we propose to replace the

[p0160-b0008 | ordinary-paragraph | high] values of v by those of the local regularization operator in R? developed by

[p0160-b0009 | ordinary-paragraph | high] Bernardi [9] that generalizes the two dimensional operator R,, of Section A.3.

[p0160-b0010 | ordinary-paragraph | high] There is no space here to give a detailed description of this operator (also denoted

[p0160-b0011 | ordinary-paragraph | high] by R,). All we need to know is that R,¢ £(H}(Q)*; ®) and that R,, satisfies

[p0160-b0012 | ordinary-paragraph | high] (2.11) when the triangulation 7%, is regular. Then we define the operator 7,,¢

[p0160-b0013 | ordinary-paragraph | high] L(H5(Q)°X;; ) by:

[p0160-b0014 | equation | low] m,V(a) = R,v(a) YVnodea of J,,

[p0160-b0015 | equation | low] (2.34)

[p0160-b0016 | equation | low] |( z,v—v):'nds=0 _ Vface F ofJ ,,.

[p0160-b0017 | ordinary-paragraph | high] F

[p0160-b0018 | ordinary-paragraph | high] With very minor modifications, the proof of Lemma 2.2 can be adapted to show

[p0160-b0019 | ordinary-paragraph | high] that z,, satisfies Hypothesis H1 with / = 1 and also Hypothesis H3:

[p0160-b0020 | lemma | high] Lemma 2.8. The operator 1, defined by (2.34) satisfies:

[p0160-b0021 | equation | low] |d iv(v—2,v)gdx =O VqeQ,,.

[p0160-b0022 | ordinary-paragraph | high] Q

[p0160-b0023 | ordinary-paragraph | high] Moreover, if the triangulation J, is regular, m, has the error bound:

[p0160-b0024 | ordinary-paragraph | high] (2.39) IV — 74V|m.@ <Ch*""\vI,q Ve H*(Q),

[p0160-b0025 | ordinary-paragraph | high] with m = O or 1 and k = 1 or 2.

[p0160-b0026 | ordinary-paragraph | high] Finally, applying Theorems 1.8 and 1.9 we obtain the expected estimate for this

[p0160-b0027 | ordinary-paragraph | high] first-order scheme:

[p0160-b0028 | theorem | high] Theorem 2.4. Let Q be a bounded polyhedron in R° and let the solution (u, p) of

[p0160-b0029 | ordinary-paragraph | high] the Stokes problem satisfy:

[p0160-b0030 | ordinary-paragraph | high] ue(H?(Q)1H3(Q)]}°, pe H*(Q)N L2(Q).

[p0160-b0031 | ordinary-paragraph | high] If the triangulation 7, is regular then the solution (u,, p,) of (1.39) with the spaces

[p0160-b0032 | ordinary-paragraph | high] X, and M,, defined respectively by (2.32) and (2.33) satisfies the estimate:

[p0160-b0033 | ordinary-paragraph | high] (2.36) lu — uylia+ IlP— Palloe <

[p0160-b0034 | ordinary-paragraph | high] Cyh(\uls.9+ IP|1,2).

[p0160-b0035 | ordinary-paragraph | high] Moreover, if the Stokes Problem (1.48) is regular, we have the L?-estimate:

[p0160-b0036 | ordinary-paragraph | high] (237) lu — uly lo,o <C h?( \uly9

[p0160-b0037 | ordinary-paragraph | high] + |p|,.9).

## PDF 161 / printed 147



[p0161-b0002 | ordinary-paragraph | high] Now we turn to the second-order scheme. As expected we wish to construct

[p0161-b0003 | ordinary-paragraph | high] a velocity vector w, with quadratic tangential components on the boundary of

[p0161-b0004 | ordinary-paragraph | high] k, which is compatible with affine pressures in x. In the light of the corresponding

[p0161-b0005 | ordinary-paragraph | high] scheme in R’, one is tempted to take w in the space {P, ®(A,4,A314Pp)}?.

[p0161-b0006 | ordinary-paragraph | high] Unfortunately, this space’s dimension is too small to meet the requirements of

[p0161-b0007 | ordinary-paragraph | high] the inf-sup condition with affine pressures. Following Fortin [30] and Bernardi

[p0161-b0008 | ordinary-paragraph | high] & Raugel [10], the best we can do is add to this space the cubics p; of (2.30); thus

[p0161-b0009 | ordinary-paragraph | high] we shall take w in the subspace of P?:

[p0161-b0010 | ordinary-paragraph | high] (2.38) Py (kK) = {P, ® (AyA2A344Po)}? ® span {p;, P2, P3,Pa}-

[p0161-b0011 | ordinary-paragraph | high] Right away, observe that Y, (x) < Y,(k); therefore we can try as much as possible

[p0161-b0012 | ordinary-paragraph | high] to apply the material of Section 1.4 in order to establish the inf-sup condition.

[p0161-b0013 | ordinary-paragraph | high] This means that the inf-sup condition imposes no constraint on the degrees of

[p0161-b0014 | ordinary-paragraph | high] freedom of the velocity w and thus we can choose the most convenient ones.

[p0161-b0015 | ordinary-paragraph | high] Now, the degrees of freedom naturally attached to P, are:

[p0161-b0016 | ordinary-paragraph | high] w(a;)) 1<i<4 and w(a,) where a, is the midpoint ofe;, 1<i<j<4

[p0161-b0017 | ordinary-paragraph | high] those corresponding to {p;; 1 <i < 4} are:

[p0161-b0018 | equation | low] | wnds 1<i<4,

[p0161-b0019 | ordinary-paragraph | high] F;

[p0161-b0020 | ordinary-paragraph | high] and the simplest one corresponding to the “bubble function” 4,2,4344 1s

[p0161-b0021 | ordinary-paragraph | high] w(a,) where a, is the center of x.

[p0161-b0022 | ordinary-paragraph | high] The next lemma shows that this set of moments is Y,(x«)-unisolvent.

[p0161-b0023 | lemma | high] Lemma 2.9. A polynomial p of Y,(K) is uniquely determined by the 37 values:

[p0161-b0024 | equation | low] p(a;) 1 < i < 4, p(a;;) 1 ~ i <j < 4, P(a,.),

[p0161-b0025 | equation | low] (2.39)

[p0161-b0026 | equation | low] pinjds 1<i<4.

[p0161-b0027 | ordinary-paragraph | high] F;

[p0161-b0028 | ordinary-paragraph | high] Moreover the restriction of p to any face F; of x depends exclusively upon its degrees

[p0161-b0029 | ordinary-paragraph | high] of freedom on that face.

[p0161-b0030 | proof | high] Proof. A polynomial of #,(«) has 37 coefficients which is precisely the number

[p0161-b0031 | ordinary-paragraph | high] of degrees of freedom defined by (2.39). Therefore it suffices to prove that zero

[p0161-b0032 | ordinary-paragraph | high] moments generate only the zero polynomial. Now, on any edge e;; a component

[p0161-b0033 | ordinary-paragraph | high] p of p reduces to a quadratic function of one variable. Therefore p(a;) = p(a;) =

[p0161-b0034 | ordinary-paragraph | high] p(a,) = 0 imply that p|.,, = 0. Thus if the degrees of freedom of p vanish on the

[p0161-b0035 | ordinary-paragraph | high] boundary of any face F; then necessarily p|,, = cp; and if Jr, p°n,ds = 0 then

[p0161-b0036 | ordinary-paragraph | high] C=.

[p0161-b0037 | ordinary-paragraph | high] Finally, if p|, = 0 then each component p of p is a “bubble function” and

## PDF 162 / printed 148



[p0162-b0003 | ordinary-paragraph | high] preserved by affine transformations. Note that the space F,(k) itself is not

[p0162-b0004 | ordinary-paragraph | high] invariant under affine transformations because of the normal vectors in the

[p0162-b0005 | ordinary-paragraph | high] cubics p;.

[p0162-b0006 | ordinary-paragraph | high] From the above considerations, we choose the following finite element spaces

[p0162-b0007 | ordinary-paragraph | high] for velocity and pressure:

[p0162-b0008 | ordinary-paragraph | high] guia vied Wee F,},

[p0162-b0009 | equation | low] (2.40)

[p0162-b0010 | ordinary-paragraph | high] YES WANEOl e

[p0162-b0011 | ordinary-paragraph | high] iy { 0, = {qeL?(Q); q|.EP, Vee TF;},

[p0162-b0012 | equation | low] M, = 0,9 L3(@).

[p0162-b0013 | lemma | high] Lemma 2.9 provides an adequate interpolation operator 7, such that:

[p0162-b0014 | equation | low] TrVle = TeV WKEF, Ve @(Q)%

[p0162-b0015 | ordinary-paragraph | high] where r,v is the unique polynomial of Y,(x) that has the same degrees of freedom

[p0162-b0016 | ordinary-paragraph | high] (2.39) as v on x. Clearly we have:

[p0162-b0017 | ordinary-paragraph | high] r,€ L(6°(Q)?; W,) L([6°(Q)N HG (Q)]°; X;)

[p0162-b0018 | ordinary-paragraph | high] and the following lemma checks Hypothesis H1.

[p0162-b0019 | lemma | high] Lemma 2.10. If 7, is a regular triangulation ofQ then r, satisfies the approxima-

[p0162-b0020 | ordinary-paragraph | high] tion property:

[p0162-b0021 | ordinary-paragraph | high] (2.42) lv —r,Vlmaq <Ch™|vI,q Vve H*(Q)’,

[p0162-b0022 | ordinary-paragraph | high] m = 0, 1, k = 2 or 3, with a positive constant C independent of h and v.

[p0162-b0023 | proof | high] Proof. If r,, were preserved by affine transformation the proof would be trivial;

[p0162-b0024 | ordinary-paragraph | high] nevertheless, the proof is quite short because only the moments on the faces are

[p0162-b0025 | ordinary-paragraph | high] not invariant by affine transformation.

[p0162-b0026 | ordinary-paragraph | high] Let Iv denote the polynomial of P, @ (A, 1.4344Po ) defined by:

[p0162-b0027 | equation | low] Iva) = 04) 1 4

[p0162-b0028 | equation | low] Iv(a;;) = v(a;) Vei<j4. Ina)=v@)

[p0162-b0029 | ordinary-paragraph | high] On the one hand this set of conditions determine Iv uniquely, and on the other

[p0162-b0030 | ordinary-paragraph | high] hand the operator / is invariant under affine transformation. Moreover, as I

[p0162-b0031 | ordinary-paragraph | high] preserves the polynomials of P,, the standard argument of Corollary A.2 shows

[p0162-b0032 | ordinary-paragraph | high] that

[p0162-b0033 | ordinary-paragraph | high] (243)0 Os LU S Ci Bell Bo lol. m=0, 1, ) e283.

[p0162-b0034 | ordinary-paragraph | high] Like in Remark 2.1 we find that r.v can be expressed as:

[p0162-b0035 | ordinary-paragraph | high] 4

[p0162-b0036 | equation | low] r,V = Iv + » OP; + BA A AzA4

[p0162-b0037 | equation | low] i=1

## PDF 163 / printed 149



[p0163-b0003 | ordinary-paragraph | medium] with

[p0163-b0004 | ordinary-paragraph | medium] (v - Iv)·n;ds

[p0163-b0005 | ordinary-paragraph | low] α

[p0163-b0006 | ordinary-paragraph | low] JFi

[p0163-b0007 | ordinary-paragraph | low] JFi

[p0163-b0008 | ordinary-paragraph | medium] and

[p0163-b0009 | ordinary-paragraph | medium] 4

[p0163-b0010 | ordinary-paragraph | low] Zαini.

[p0163-b0011 | equation | low] β=

[p0163-b0012 | equation | low] =1

[p0163-b0013 | ordinary-paragraph | medium] Like in Lemma 2.2 we have:

[p0163-b0014 | equation | low] [pilm.x ≤ C2 /det(B)|1/2  B1 I1 m

[p0163-b0015 | ordinary-paragraph | medium] with a similar expression for |, ^2^3^4lm.k. Likewise, we infer that

[p0163-b0016 | equation | low] k = 2, 3.

[p0163-b0017 | equation | low] [α;1 ≤ C3|det(B,)|-1/2 II B II*|vlk,n>

[p0163-b0018 | ordinary-paragraph | medium] Therefore

[p0163-b0019 | ordinary-paragraph | medium] 4

[p0163-b0020 | equation | low] ≤ C4 I/BI*I/ B1 lm|vlk,x.

[p0163-b0021 | ordinary-paragraph | low] αiPi + βA2A34

[p0163-b0022 | ordinary-paragraph | low] m.x

[p0163-b0023 | ordinary-paragraph | medium] Hence (2.43) and the regularity of , lead to

[p0163-b0024 | equation | low] IrxV--V/m,x≤Csαmhk-m|vlk,x

[p0163-b0025 | ordinary-paragraph | medium] As mentioned previously there is no need to establish directly the inf-sup

[p0163-b0026 | ordinary-paragraph | medium] condition because the space X, is contained in X, and the pair (X,, M,) satisfies

[p0163-b0027 | ordinary-paragraph | medium] a uniform inf-sup condition. Instead it suffices to show that (X,, M,) satisfies an

[p0163-b0028 | ordinary-paragraph | medium] adequate local condition. In fact, it is easy to verify that the statement and proof

[p0163-b0029 | ordinary-paragraph | medium] of Theorem 2.2 are valid without change for the pair of local spaces:

[p0163-b0030 | equation | low] Xh(k) = {v∈92(K); vloK = 0},

[p0163-b0031 | equation | low] Mh(K) = P N L(K).

[p0163-b0032 | ordinary-paragraph | medium] (Observe that the crucial point in the proof is that the function Λ, 2^34 grad q

[p0163-b0033 | ordinary-paragraph | medium] belongs to X,(k) for all q in P,). According to Theorem 1.12 this implies the global

[p0163-b0034 | ordinary-paragraph | medium] inf-sup condition (1.12):

[p0163-b0035 | lemma | medium] Lemma 2.11. Let T, be a regular triangulation of Q and let the spaces X, and M,

[p0163-b0036 | ordinary-paragraph | medium] be defined by (2.40) (2.41). There exists a constant β* > 0 independent of h such

[p0163-b0037 | ordinary-paragraph | medium] that:

[p0163-b0038 | ordinary-paragraph | low] VanE Mh.

[p0163-b0039 | equation | low] qn div vn dx

[p0163-b0040 | equation | low] {≥ β* llanllo,α

[p0163-b0041 | ordinary-paragraph | low] Vhl1,s?

[p0163-b0042 | equation | low] sup

[p0163-b0043 | ordinary-paragraph | low] VhEXn

[p0163-b0044 | ordinary-paragraph | medium] Finally, Hypothesis H2 reduces to the standard approximation property of

[p0163-b0045 | ordinary-paragraph | medium] the L2-projection operator ph onto Qn (cf. Lemma A.5):

[p0163-b0046 | equation | low] “)HbA  |y≥o b

[p0163-b0047 | equation | low] k = 1, 2.

## PDF 164 / printed 150



[p0164-b0003 | ordinary-paragraph | high] Stokes problem satisfy:

[p0164-b0004 | equation | low] ue[H(Q)N HQ), pe H*(Q)N LQ), k= 1or2.

[p0164-b0005 | ordinary-paragraph | high] Then the solution (u,,p,) of the scheme (1.39) with the spaces X,, and M,, defined

[p0164-b0006 | ordinary-paragraph | high] respectively by (2.40) and (2.41) satisfies:

[p0164-b0007 | ordinary-paragraph | high] (2.44) |u—uy,l1.e+ IP — Pallo.eS Cyh*(\Ulee1,9 + Pla) k=1,2.

[p0164-b0008 | ordinary-paragraph | high] In addition, if the Stokes problem (1.48) is regular, we have the L?-estimate:

[p0164-b0009 | ordinary-paragraph | high] (2.45) Ju=t= Culhe se( ullpero aea (p laya =e.

[p0164-b0010 | ordinary-paragraph | high] Higher-order schemes of degree ! > 3 are an easy generalization of the second-

[p0164-b0011 | ordinary-paragraph | high] order scheme. If we want a velocity space that will match a polynomial pressure

[p0164-b0012 | ordinary-paragraph | high] q of degree | — 1, we can try a velocity w in the subspace of P3.,:

[p0164-b0013 | ordinary-paragraph | high] (2.46) A(x) =[P,® {A 45434.4(F,-2 ® Bas) tales

[p0164-b0014 | ordinary-paragraph | high] Then each component of w reduces to an /-degree polynomial on the faces of «

[p0164-b0015 | ordinary-paragraph | high] and moreover 4,A,A34, grad q belongs to A(x) whenever q belongs to P,_, (cf.

[p0164-b0016 | remark | high] Remark 2.5). Thus we choose the following spaces:

[p0164-b0017 | ordinary-paragraph | high] (rierras t iea si

[p0164-b0018 | ordinary-paragraph | high] a

[p0164-b0019 | equation | low] X, = WN HG(Q),

[p0164-b0020 | ordinary-paragraph | high] {Re TSeCC lai eat aad

[p0164-b0021 | equation | low] (2.48)

[p0164-b0022 | equation | low] M, = 2,9 L3(Q).

[p0164-b0023 | ordinary-paragraph | high] Like in two dimensions, we can take for degrees of freedom of the velocity w

[p0164-b0024 | ordinary-paragraph | high] its values associated with P, on each face F; of x and its derivatives corresponding

[p0164-b0025 | ordinary-paragraph | high] to P,_, at the center of x:

[p0164-b0026 | ordinary-paragraph | high] Bas ‘e wa) WaeX.NF, 1<i<4,

[p0164-b0027 | ordinary-paragraph | high] (b) d*w(a,) for all partial derivatives of order k with 0 <k<l—2,

[p0164-b0028 | ordinary-paragraph | high] w denoting an arbitrary component of w. If necessary, the derivatives

[p0164-b0029 | ordinary-paragraph | high] can also

[p0164-b0030 | ordinary-paragraph | high] be replaced by the interior moments:

[p0164-b0031 | ordinary-paragraph | high] (2.49) (c) |w qdx YVqeP,_>.

[p0164-b0032 | ordinary-paragraph | high] K

[p0164-b0033 | ordinary-paragraph | high] On the one hand, either formula (2.49) defines a total

[p0164-b0034 | ordinary-paragraph | high] of:

[p0164-b0035 | ordinary-paragraph | high] 4 + 6dim(P,_,(R)) + 4dim(P,_3(R?)) + dim(P,_

[p0164-b0036 | ordinary-paragraph | high] ,(R°))

[p0164-b0037 | equation | low] = 47 0()—"1) ++ 20 — 2) 1) (6) =i

[p0164-b0038 | ordinary-paragraph | high] 1)

[p0164-b0039 | equation | low] = (1/6) {(? — 1)(1 + 12) + 24}

## PDF 165 / printed 151



[p0165-b0003 | ordinary-paragraph | high] space of dimension:

[p0165-b0004 | equation | low] dim(P,) + dim(P,_,) + dim(P_3), all in R?

[p0165-b0005 | equation | low] = (1/6)(2 + IU + 2). + 3) + (1/2) — 11 + (1/2)( 1— 2)(1 — 1)

[p0165-b0006 | equation | low] = (1/6) {(/? — 1)( + 12) + 24}.

[p0165-b0007 | ordinary-paragraph | high] Recalling the argument of Lemma 2.3, it is an easy matter to prove that these

[p0165-b0008 | ordinary-paragraph | high] degrees of freedom are A(xk)-unisolvent.

[p0165-b0009 | lemma | high] Lemma 2.12. Each component p of a polynomial of A(x) is uniquely determined

[p0165-b0010 | ordinary-paragraph | high] by the degrees of freedom (2.49a) (2.49b) or (2.49a) (2.49c). Moreover, on a given

[p0165-b0011 | ordinary-paragraph | high] face of k, p depends exclusively upon the degrees of freedom defined on that face.

[p0165-b0012 | ordinary-paragraph | high] This lemma yields the following interpolation operator:

[p0165-b0013 | equation | low] nV, =%v WeeF, Vve¢(Q)%,

[p0165-b0014 | ordinary-paragraph | high] where r,v is the only polynomial of A(x) that has the same degrees of freedom

[p0165-b0015 | ordinary-paragraph | high] (2.49a) (2.49c) as the function v. Obviously, the operator r, is invariant under

[p0165-b0016 | ordinary-paragraph | high] affine transformations and as a consequence we have the following result:

[p0165-b0017 | lemma | high] Lemma 2.13. The operator r, belongs to L(°(Q)?; W,) 0 L([@°(Q) 0 H4(@))°;

[p0165-b0018 | ordinary-paragraph | high] X,,). In addition, if the triangulation 7, is regular, r, has the following interpolation

[p0165-b0019 | ordinary-paragraph | high] error:

[p0165-b0020 | ordinary-paragraph | high] (2:50) NV—7,¥\0 .< .Ch "lV oe VVC (QC)? = On or 1,

[p0165-b0021 | ordinary-paragraph | high] 1 <k <, with a positive constant C independent of h and v.

[p0165-b0022 | ordinary-paragraph | high] Like for the second-order scheme, the proof of the inf-sup condition here is

[p0165-b0023 | ordinary-paragraph | high] trivially similar to that of Theorem 2.2. The local spaces involved are

[p0165-b0024 | equation | low] X,(k) = (VE A(K); Via. = 9},

[p0165-b0025 | equation | low] M,(«) = Pry NLo(2)

[p0165-b0026 | ordinary-paragraph | high] and the salient property that links them is:

[p0165-b0027 | ordinary-paragraph | high] A AzgAsA4 gradqe X,(k) VqeM,(x).

[p0165-b0028 | ordinary-paragraph | high] Hence the statement of Lemma 2.11 carries over to the pair (X,,, M,,) defined by

[p0165-b0029 | ordinary-paragraph | high] (2.47) (2.48).

[p0165-b0030 | ordinary-paragraph | high] Again Hypothesis H2 follows from the approximation property of the es

[p0165-b0031 | ordinary-paragraph | high] projection operator p, onto Q,:

[p0165-b0032 | equation | low] la — Prdllo.a<Ch*lqho VaeH"(Q), 1<k<l.
