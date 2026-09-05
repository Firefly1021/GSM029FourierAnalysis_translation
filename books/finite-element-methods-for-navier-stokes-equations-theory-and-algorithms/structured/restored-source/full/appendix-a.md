# Restored-source review candidate: appendix-a



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 109 / printed 95



[p0109-b0003 | equation | low] curl-(w x n) = 0,

[p0109-b0004 | ordinary-paragraph | high] where the subscript I" indicates that the operators div and curl are

[p0109-b0005 | ordinary-paragraph | high] surface

[p0109-b0006 | ordinary-paragraph | high] operators. We refer to Roux [69] for more details.

[p0109-b0007 | ordinary-paragraph | high] Appendix A. Results of Standard Finite Element Approximation

[p0109-b0008 | ordinary-paragraph | high] This short chapter gathers most of the properties of the classical finite element

[p0109-b0009 | ordinary-paragraph | high] approximation that will be required subsequently. The more familiar results are

[p0109-b0010 | ordinary-paragraph | high] stated without proof; for detailed proofs and further material, the reader can refer

[p0109-b0011 | ordinary-paragraph | high] to the very complete texts of Ciarlet [19] and Strang & Fix [77]. In addition,

[p0109-b0012 | ordinary-paragraph | high] we include a brief mention of new or nonstandard material, developed among

[p0109-b0013 | ordinary-paragraph | high] others by Clément [21], Bernardi [9], Scott [73], Lenoir [50], that will also be

[p0109-b0014 | ordinary-paragraph | high] very useful later on.

[p0109-b0015 | ordinary-paragraph | high] A.1. Triangular Finite Elements

[p0109-b0016 | definition | high] Definition A.1. For each integer k > 0, we denote by P, the space of all poly-

[p0109-b0017 | ordinary-paragraph | high] nomials defined on R¥, of degree less than or equal to k.

[p0109-b0018 | ordinary-paragraph | high] Recall that an N-simplex of R™ is the convex hull « of N + 1 points a;,

[p0109-b0019 | ordinary-paragraph | high] 1 <j <N +1, called the vertices of x, which are not all located in a single

[p0109-b0020 | ordinary-paragraph | high] hyperplane. For instance, a 2-simplex is a non degenerate triangle and a 3-simplex

[p0109-b0021 | ordinary-paragraph | high] is a non degenerate tetrahedron. The size and shape of an N-simplex x are

[p0109-b0022 | ordinary-paragraph | high] specified by two quantities:

[p0109-b0023 | equation | low] h,. = diameter of x

[p0109-b0024 | ordinary-paragraph | high] and

[p0109-b0025 | equation | low] p, = sup {diameter of B; B is a ball contained in x}.

[p0109-b0026 | ordinary-paragraph | high] In addition, the regularity of « is measured by the ratio

[p0109-b0027 | equation | low] On = Ny /P x

[p0109-b0028 | ordinary-paragraph | high] We denote by & the reference unit simplex in the (X,,...,%y) space with

[p0109-b0029 | ordinary-paragraph | high] vertices 4; = (6); <i<n, for 1 <j < N, and dy, = (0); <icy. If is an N-simplex

[p0109-b0030 | ordinary-paragraph | high] with vertices a;, 1 <j < N + 1, there exists exactly one affine mapping

[p0109-b0031 | ordinary-paragraph | high] (A.1) F.(%) = B,% +b,

[p0109-b0032 | ordinary-paragraph | high] that maps &o nto xw ith F,.(d;) = a,for1 <i< N + 1 (cf. Figure 3). Furthermore,

## PDF 110 / printed 96



[p0110-b0003 | ordinary-paragraph | low] a3

[p0110-b0004 | ordinary-paragraph | medium] K

[p0110-b0005 | ordinary-paragraph | low] 10.1)a2

[p0110-b0006 | ordinary-paragraph | low] R

[p0110-b0007 | ordinary-paragraph | low] Ta3

[p0110-b0008 | ordinary-paragraph | low] a

[p0110-b0009 | ordinary-paragraph | medium] (1,0)

[p0110-b0010 | equation | low] (0.0)

[p0110-b0011 | figure | medium] Figure 3. Triangle K and its reference unit triangle R (N = 2)

[p0110-b0012 | ordinary-paragraph | medium] it can be easily shown that the matrix B, is nonsingular and satisfies the following

[p0110-b0013 | ordinary-paragraph | medium] bounds:

[p0110-b0014 | equation | low] IIBll ≤h</Pt,  II B-1 ll ≤ hz/Px,

[p0110-b0015 | ordinary-paragraph | medium] (A.2)

[p0110-b0016 | ordinary-paragraph | medium] where | . 1l stands for both the Euclidean norm of R? and its subordinate matrix

[p0110-b0017 | ordinary-paragraph | medium] norm. In addition, owing that

[p0110-b0018 | ordinary-paragraph | medium] (A.3)

[p0110-b0019 | equation | low] [det(B)/ = meas(k)/meas(k),

[p0110-b0020 | ordinary-paragraph | medium] there exist two positive constants C, (N), C2(N) depending only upon N, such that

[p0110-b0021 | ordinary-paragraph | medium] (A.4)

[p0110-b0022 | equation | low] C2(N)p ≤ Idet(B)I ≤ C(N)h.

[p0110-b0023 | ordinary-paragraph | medium] According to convenience, we shall sometimes replace the Euclidean coor-

[p0110-b0024 | ordinary-paragraph | medium] dinates of the point x of R? by its barycentric coordinates, X, = X,(x), with respect

[p0110-b0025 | ordinary-paragraph | medium] to the vertices a, 1 ≤ i ≤ N + 1, defined by:

[p0110-b0026 | equation | low] l;e P,  A(a;) = o; for 1 ≤i,j ≤ N + 1.

[p0110-b0027 | ordinary-paragraph | medium] (A.5)

[p0110-b0028 | ordinary-paragraph | medium] The barycentric coordinates satisfy the following useful identities in R?:

[p0110-b0029 | ordinary-paragraph | medium] N+1

[p0110-b0030 | ordinary-paragraph | medium] N+1

[p0110-b0031 | equation | low] ∑ = 1, p= ∑ p(a) VpeP.

[p0110-b0032 | ordinary-paragraph | medium] (A.6)

[p0110-b0033 | equation | low] =

[p0110-b0034 | equation | low] =1

[p0110-b0035 | ordinary-paragraph | medium] Moreover, it can be easily checked that

[p0110-b0036 | equation | low] K = {x∈ R; 0 ≤ A;(x) ≤ 1, 1 ≤i ≤ N + 1}.

[p0110-b0037 | ordinary-paragraph | medium] As mentioned above, the mapping x = F,(x) establishes a one-to-one corre-

[p0110-b0038 | ordinary-paragraph | medium] spondence between K and k. The composition with F:

[p0110-b0039 | equation | low] (v: K →R) →(0 = vo F: r →R)

## PDF 111 / printed 97



[p0111-b0003 | equation | low] (6:k > R) > (v = 60 F,': x >R)

[p0111-b0004 | ordinary-paragraph | high] are of constant use because they enable us to work exclusively on the reference

[p0111-b0005 | ordinary-paragraph | high] element &. The effects of this change of variable are described in the next lemma.

[p0111-b0006 | lemma | high] Lemma A.1. For each integerm > Oand for allreal pw ith 1 < p < «, the mapping

[p0111-b0007 | ordinary-paragraph | high] v > 6 = voOF, is an isomorphism from W™?(k) onto W™?(k) and the following

[p0111-b0008 | ordinary-paragraph | high] bounds hold:

[p0111-b0009 | ordinary-paragraph | high] (A.7) |Blm.p.k < Cy || By ||™\det(B,)}-2?|0|

[p0111-b0010 | ordinary-paragraph | high] Yoew™ (x),

[p0111-b0011 | ordinary-paragraph | high] m,p,K

[p0111-b0012 | ordinary-paragraph | high] (A.8) [lmp .x< Co || Bo? ||"™|det(B, )|*/"|6|

[p0111-b0013 | ordinary-paragraph | high] Vie w™?(R).

[p0111-b0014 | ordinary-paragraph | high] m, p,K

[p0111-b0015 | ordinary-paragraph | high] Note that the gradient of a function and the unit normal vector have the

[p0111-b0016 | ordinary-paragraph | high] simple expressions (cf. for instance Babuska & al [5]):

[p0111-b0017 | ordinary-paragraph | high] (A.9) grad; 6(X) = (BY grad, v) 0 F(X),

[p0111-b0018 | ordinary-paragraph | high] (A.10) A(X) = [(Ben)/|| Bin||] o F,(%),

[p0111-b0019 | ordinary-paragraph | high] where n (resp. fi) denotes the unit exterior normal to x (resp. k).

[p0111-b0020 | ordinary-paragraph | high] The following theorem (which is an extension of Theorem I.1.9) and its

[p0111-b0021 | ordinary-paragraph | high] consequences are fundamental tools of the finite element theory.

[p0111-b0022 | theorem | high] Theorem A.1. For each integer k > 0 and real p with 1 < p < «, there exists a

[p0111-b0023 | ordinary-paragraph | high] constant C > 0, depending only on k, p and k, such that:

[p0111-b0024 | ordinary-paragraph | high] (A.11) inf |]@+ Cllestne<Clalesipe Vhe W***?(0)/P,.

[p0111-b0025 | ordinary-paragraph | high] te P,

[p0111-b0026 | corollary | high] Corollary A.1. Let k > 0,m > 0 be integers and p = 1, q > 1 be reals such that

[p0111-b0027 | ordinary-paragraph | high] WEEP (Ric Wisk).

[p0111-b0028 | ordinary-paragraph | high] Let Re L(W**1?(k); W™ 4k) satisfy:

[p0111-b0029 | equation | low] tt=t VteP,.

[p0111-b0030 | ordinary-paragraph | high] Then there exists a constant C > 0 depending on k, m, p, q, K and t only, such that

[p0111-b0031 | ordinary-paragraph | high] (A.12) 6 — 40 imge <ClOleri,p.2 WOE WHE ?(2),

[p0111-b0032 | ordinary-paragraph | high] When combined with Lemma A.1, (A.2) and (A.3), Corollary A.1 yields:

[p0111-b0033 | corollary | high] Corollary A.2. Let k, m, p, q and ft be like in Corollary A.1. Let « be an N-simplex

[p0111-b0034 | ordinary-paragraph | high] of R® and let the operator ne LY(W**""(k); W™4(k)) be defined by:

[p0111-b0035 | ordinary-paragraph | high] (A.13) (nv)oF, =2#(voOF,) (ie. m0 = t #6).

[p0111-b0036 | ordinary-paragraph | high] Then there exists a constant C > 0, depending only on k, m, p, q, K and % such that

## PDF 112 / printed 98



[p0112-b0003 | ordinary-paragraph | high] (A.14) |v — T0| mq < Coe (mea4 sPA(Tk D)la), pr:

[p0112-b0004 | ordinary-paragraph | high] We shall assume henceforth that the dimension N equals two, although some

[p0112-b0005 | ordinary-paragraph | high] results will be stated in the N-dimensional case. In addition, to simplify the

[p0112-b0006 | ordinary-paragraph | high] discussion we shall assume that Q is a bounded domain with a polygonal

[p0112-b0007 | ordinary-paragraph | high] boundary I. The technical difficulties inherent to curved boundaries can be

[p0112-b0008 | ordinary-paragraph | high] conveniently handled with the general elements introduced by Bernardi [9], but

[p0112-b0009 | ordinary-paragraph | high] there is no space to discuss them here.

[p0112-b0010 | ordinary-paragraph | high] For each h > 0, let J, be a triangulation of Q made of closed triangles « with

[p0112-b0011 | ordinary-paragraph | high] diameters bounded by h. In other words,

[p0112-b0012 | ordinary-paragraph | high] Gps Ni Pele

[p0112-b0013 | ordinary-paragraph | high] Ke,

[p0112-b0014 | ordinary-paragraph | high] where any two triangles are either disjoint or share exactly either one side or one

[p0112-b0015 | ordinary-paragraph | high] vertex.

[p0112-b0016 | ordinary-paragraph | high] Definitions A.2. 1°) A family 7, of triangulations of Q is said to be regular as h

[p0112-b0017 | ordinary-paragraph | high] tends to zero if there exists a number o > 0, independent of h and x, such that

[p0112-b0018 | ordinary-paragraph | high] (A.15) C= 0 VNKET,.

[p0112-b0019 | ordinary-paragraph | high] 2°) In addition, %, is said to be uniformly regular (or quasi-uniform) as h

[p0112-b0020 | ordinary-paragraph | high] tends to zero if there exists another constant t > 0 such that

[p0112-b0021 | ordinary-paragraph | high] (A.16) Timah op Ker,

[p0112-b0022 | remark | high] Remark A.1. When 7, is regular, the error estimate (A.14) simplifies to:

[p0112-b0023 | ordinary-paragraph | high] (ALF) le alyg g SORE ole se, NUS Veen (ie):

[p0112-b0024 | ordinary-paragraph | high] where the constant C is independent of v, h and x. Because of the inclusion

[p0112-b0025 | ordinary-paragraph | high] We (ela th),

[p0112-b0026 | ordinary-paragraph | high] we have:

[p0112-b0027 | equation | low] k+1—N(1/mq —1+/p) >0

[p0112-b0028 | ordinary-paragraph | high] and therefore the above factor h, can be bounded by h.

[p0112-b0029 | ordinary-paragraph | high] Now, we fix the integer k > 1 and we introduce the standard finite element

[p0112-b0030 | ordinary-paragraph | high] spaces:

[p0112-b0031 | equation | low] O, = {0,€6°(Q); 41.6 WKET;,},

[p0112-b0032 | ordinary-paragraph | high] (A.18)

[p0112-b0033 | equation | low] ®, = 0, Ho (@).

[p0112-b0034 | ordinary-paragraph | high] Note that they are both finite-dimensional subspaces of W!”(Q); but their

## PDF 113 / printed 99



[p0113-b0004 | ordinary-paragraph | medium] we define an interpolation operator. Of course, the simplest choice consists in

[p0113-b0005 | ordinary-paragraph | medium] interpolating the functions at an appropriate set of points of the N-simplex K

[p0113-b0006 | ordinary-paragraph | medium] such as the principal lattice of order k:

[p0113-b0007 | ordinary-paragraph | medium] N+1

[p0113-b0008 | ordinary-paragraph | medium] N+1

[p0113-b0009 | equation | low] A;a;  n; = 1, A;∈{0, 1/k.,..,(k - 1)/k, 1},

[p0113-b0010 | equation | low] ∑=<x=

[p0113-b0011 | ordinary-paragraph | medium] (A.19)

[p0113-b0012 | equation | low] 1≤j≤N+1

[p0113-b0013 | ordinary-paragraph | medium] (cf. Figure 4 for k = 3). This yieids a widely used interpolation operator I, with

[p0113-b0014 | ordinary-paragraph | medium] well known properties, valid in all dimensions N.

[p0113-b0015 | ordinary-paragraph | medium] (a)

[p0113-b0016 | ordinary-paragraph | medium] (b)

[p0113-b0017 | figure | medium] Figure 4. Principal lattice of order 3 for (a) triangle (b) quadrilateral

[p0113-b0018 | lemma | medium] Lemma A.2. Let T, be a regular triangulation of Q. For real p > N/2, the interpo-

[p0113-b0019 | ordinary-paragraph | low] Yona u pauifap (Φ :(o)a.(M U (o)azM)b U(0 :(o)azM) =I doinuado uo)

[p0113-b0020 | ordinary-paragraph | medium] element r by:

[p0113-b0021 | equation | low] Inulk∈Pk,Ihu(x) = u(x) Vx∈Ex,

[p0113-b0022 | ordinary-paragraph | medium] (A.20)

[p0113-b0023 | ordinary-paragraph | medium] satisfies the following error estimate for all integers m and real s with O < m ≤

[p0113-b0024 | ordinary-paragraph | medium] s + 1, 1 ≤ s≤ k:

[p0113-b0025 | equation | low] [u — Ihulm,p,2 ≤ Chs+1-m|uls+1,p,2  Vue Ws+1,p(2).

[p0113-b0026 | ordinary-paragraph | medium] (A.21a)

[p0113-b0027 | ordinary-paragraph | low] pup N < b 1pau 11p uof (*Φ :(o). M)F U(0 :(o)b.1M) ="1 daaoauoW

[p0113-b0028 | ordinary-paragraph | low] (A.21b) Iu - Inu/m,q,2 ≤ C2h1-m|ul1,q,2 Vu∈ W1,a(2),

[p0113-b0029 | equation | low] m = 0, 1.

[p0113-b0030 | ordinary-paragraph | medium] Both constants C, and C2 are positive and independent of h and v.

[p0113-b0031 | ordinary-paragraph | medium] However, in the forthcoming applications it will sometimes be handy to work

[p0113-b0032 | ordinary-paragraph | medium] with a slightly different interpolant, given here when N = 2.

## PDF 114 / printed 100



[p0114-b0003 | ordinary-paragraph | high] polynomial I,.v€ P , such that:

[p0114-b0004 | equation | low] ( T.v(a,)=0(@,) 1<i<3,

[p0114-b0005 | ordinary-paragraph | high] Vsixd’eo sf k ,

[p0114-b0006 | equation | low] te |d o —ofas=0 fe Py_2(x’),

[p0114-b0007 | ordinary-paragraph | high] (py

[p0114-b0008 | equation | low] hike |( .v—v)fdx=0 VfeEP,_3(x).

[p0114-b0009 | proof | high] Proof. First, we remark that (A.22) consists of (1/2)(k + 1)(k + 2) equations,

[p0114-b0010 | ordinary-paragraph | high] which is precisely the dimension of P,. Hence (A.22) is a square system of linear

[p0114-b0011 | ordinary-paragraph | high] equations and it suffices to prove that its solution is unique. Thus, we assume

[p0114-b0012 | ordinary-paragraph | high] that pe P, satisfies:

[p0114-b0013 | ordinary-paragraph | high] (i) pia)=0 1<i<3,

[p0114-b0014 | ordinary-paragraph | high] (ii) | p(s)f(s)\ds =O VWfeEP,_.(k'), Vsides x’ of x,

[p0114-b0015 | ordinary-paragraph | high] (ili) |D (x)f(x)dx =0 Vfe P,-3(x).

[p0114-b0016 | ordinary-paragraph | high] Suppose for the moment that k > 3. Note that the restriction of p to each x’

[p0114-b0017 | ordinary-paragraph | high] is a polynomial of degree k of the single variable s. Then it follows from (i) and

[p0114-b0018 | ordinary-paragraph | high] (ii) that:

[p0114-b0019 | equation | low] cs | p(s)(d* p(s)/ds*) ds = -| (dp(s)/ds)? ds.

[p0114-b0020 | ordinary-paragraph | high] K

[p0114-b0021 | ordinary-paragraph | high] Hence p = 0 on 6x and pcan be expressed in terms of barycentric coordinates as:

[p0114-b0022 | equation | low] p=2,4,A3q, where qe P,_3.

[p0114-b0023 | ordinary-paragraph | high] Then (iii) implies that

[p0114-b0024 | equation | low] |4 4243(9x7)d x = 0,

[p0114-b0025 | ordinary-paragraph | high] ie. gq= 0 since the integrand is non negative. Hence p = 0 on x.

[p0114-b0026 | ordinary-paragraph | high] The case k < 2 is trivial. Cc

[p0114-b0027 | ordinary-paragraph | high] It is a matter of routine to check that Ie Y(W?:?(x); P,), the value of T.v on

[p0114-b0028 | ordinary-paragraph | high] each side x’ of « depends only on the value of v on x’ and of course

[p0114-b0029 | equation | low] [p=p VpeP,.

[p0114-b0030 | ordinary-paragraph | high] Furthermore, the operator it satisfies the fundamental relation (A.13):

[p0114-b0031 | equation | low] <a

[p0114-b0032 | equation | low] Iv = I, 6.

[p0114-b0033 | ordinary-paragraph | high] By collecting these properties and using Corollary A.2 and Remark A.1 we derive:

## PDF 115 / printed 101



[p0115-b0004 | ordinary-paragraph | high] tion operator I,e 2(W?-?(Q); 01) L(W*?(Q) 0 Wl? (Q);

[p0115-b0005 | ordinary-paragraph | high] ®,) donned in each

[p0115-b0006 | ordinary-paragraph | high] element k by:

[p0115-b0007 | equation | low] Tvl =Tv Ve J,

[p0115-b0008 | ordinary-paragraph | high] satisfies the following error estimate for all integers m and real s with

[p0115-b0009 | ordinary-paragraph | high] 0 <m =

[p0115-b0010 | ordinary-paragraph | high] s+tli,l<s<k:

[p0115-b0011 | ordinary-paragraph | high] (A.23) lv — Iv] Ch “ltl, Vvoe Ws ?(0),

[p0115-b0012 | ordinary-paragraph | high] mM, P, as

[p0115-b0013 | ordinary-paragraph | high] where the constant C > 0 is independent of h and v.

[p0115-b0014 | ordinary-paragraph | high] Apart from these two interpolants, the projection operator will play a funda-

[p0115-b0015 | ordinary-paragraph | high] mental part in the subsequent theory. To be specific, for real p > 1, let

[p0115-b0016 | ordinary-paragraph | high] Pre L(Wo(Q);®,), Phe LW*?(Q); O,)

[p0115-b0017 | ordinary-paragraph | high] be defined respectively by

[p0115-b0018 | ordinary-paragraph | high] (A.24) (grad(P,v — v),grad¢,)=0 Vd,e%,, Woe WE(Q);

[p0115-b0019 | ordinary-paragraph | high] (A.25) (grad(P,hv — v),grad0h, )=0 V6,h€e6@p, ,

[p0115-b0020 | ordinary-paragraph | high] Voe W?P(Q).

[p0115-b0021 | equation | low] (P,v — v, 1) =0.

[p0115-b0022 | ordinary-paragraph | high] Note that P,v can also be interpreted as the finite element solution of the

[p0115-b0023 | ordinary-paragraph | high] homogeneous Dirichlet problem:

[p0115-b0024 | ordinary-paragraph | high] AU ay ee eee) on ae

[p0115-b0025 | ordinary-paragraph | high] and P,v as the finite element solution of the non-homogeneous Neumann

[p0115-b0026 | ordinary-paragraph | high] problem:

[p0115-b0027 | equation | low] —Av=f inQ, dv/on=g onT,

[p0115-b0028 | ordinary-paragraph | high] with the compatibility condition

[p0115-b0029 | equation | low] |f dx = <g,1>r,

[p0115-b0030 | ordinary-paragraph | high] Q

[p0115-b0031 | ordinary-paragraph | high] its uniqueness proceeding from the second condition of(A .25). Now, since PB, and

[p0115-b0032 | ordinary-paragraph | high] P,, are projections for the seminorm of H'(Q), it is easy to prove error estimates

[p0115-b0033 | ordinary-paragraph | high] in the L? and H' norms, provided ve H'(Q); but it is much more difficult to

[p0115-b0034 | ordinary-paragraph | high] establish optimal L’ and W':” estimates. The following theorem is the achieve-

[p0115-b0035 | ordinary-paragraph | high] ment of many years of work contributed by several mathematicians; cf. for

[p0115-b0036 | example | high] example Douglas, Dupont & Whalbin [25], Nitsche [62], Rannacher & Scott

[p0115-b0037 | ordinary-paragraph | high] [66] and Scott [73]. Although it is by no means standard, its proof is omitted

[p0115-b0038 | ordinary-paragraph | high] as it is far beyond the scope of this book.

[p0115-b0039 | theorem | high] Theorem A.2. Assume that Q is a convex polygon. Let Y,, be a uniformly regular

[p0115-b0040 | ordinary-paragraph | high] triangulation of Q and let the reals s and p be such that0 <s <kand1<p<o.

[p0115-b0041 | ordinary-paragraph | high] For k > 2or fork = 1 and2 < p < , there exists a constant C > 0, independent

## PDF 116 / printed 102



[p0116-b0004 | ordinary-paragraph | high] Voe W5*1-2(Q) (resp. Wve WS*1-?(Q)N Wo?(Q)).

[p0116-b0005 | ordinary-paragraph | high] When k = 1 and peé[1, 2), the estimate (A.26) holds with the additional factor

[p0116-b0006 | ordinary-paragraph | high] [In h|?7/?

[p0116-b0007 | ordinary-paragraph | high] in the right-hand side. When k = 1 and p = ©, the L®-estimate in (A.26) becomes

[p0116-b0008 | ordinary-paragraph | high] (A.27) lv — Prvllo,o,.@ < ClInh|h*" ||v lls+1, 0,2

[p0116-b0009 | ordinary-paragraph | high] while the W‘:®-estimate is unchanged.

[p0116-b0010 | ordinary-paragraph | high] The proof of Theorem A.2 relies on the fact that the Laplacian operator is

[p0116-b0011 | ordinary-paragraph | high] an isomorphism from W,):?(Q)1 W??(Q) onto L?(Q) for all pe(1,2 + ¢), for

[p0116-b0012 | ordinary-paragraph | high] some ¢ > 0. According to Remark I.1.2, this isomorphism holds on a smooth

[p0116-b0013 | ordinary-paragraph | high] domain or on a convex polygon. This accounts for the convexity hypothesis in

[p0116-b0014 | ordinary-paragraph | high] the statement of Theorem A.2. Let us point out that the occurrence of the

[p0116-b0015 | ordinary-paragraph | high] logarithmic factor is a well-known phenomenon in L®-estimates. Finally, as

[p0116-b0016 | ordinary-paragraph | high] mentioned above, (A.26) can be established directly when p = 2 and for all k > 1;

[p0116-b0017 | ordinary-paragraph | high] if s is an integer, this yields the familiar estimate for P, (resp. P,):

[p0116-b0018 | ordinary-paragraph | high] (A.28) |v — P,V|lo,e an Le P,U|1,0 < Che lel. eo

[p0116-b0019 | ordinary-paragraph | high] Voe H™*1(Q) (resp. Wve H™*1(Q)N HE (Q)).

[p0116-b0020 | remark | high] Remark A.2. When the function v is not continuous, neither its interpolant J,,v

[p0116-b0021 | ordinary-paragraph | high] nor I,v are defined. If Q is convex and the triangulation uniformly regular, they

[p0116-b0022 | ordinary-paragraph | high] may be conveniently replaced by the projection P,v (or P,v if v vanishes on I’).

[p0116-b0023 | ordinary-paragraph | high] When 22 is not convex or a uniformly regular triangulation is not available, other

[p0116-b0024 | ordinary-paragraph | high] interpolants obtained by local regularization may be used. They also have the

[p0116-b0025 | ordinary-paragraph | high] advantage, over the projection, of being defined locally and not globally. The

[p0116-b0026 | ordinary-paragraph | high] reader will find some information about this technique in Section A.3.

[p0116-b0027 | ordinary-paragraph | high] We shall also use subsequently a local L? projection. To be precise, for

[p0116-b0028 | ordinary-paragraph | high] ve L?(Q) and each integer k > 0, we define:

[p0116-b0029 | ordinary-paragraph | high] (A.29) Prl EP |( pu viLde—0> Vier. Vre7,:

[p0116-b0030 | ordinary-paragraph | high] Clearly the operator p, satisfies the hypotheses of Corollary A.2 and we have the

[p0116-b0031 | ordinary-paragraph | high] following result valid in all dimensions N.

[p0116-b0032 | lemma | high] Lemma A.5. Let ve H*(Q) for some real se[0,k + 1]. The L? projection p, satis-

[p0116-b0033 | ordinary-paragraph | high] fies the error estimate:

[p0116-b0034 | ordinary-paragraph | high] (A.30) 0 — prvl<l Coh'.|v|a,

[p0116-b0035 | ordinary-paragraph | high] 0,

[p0116-b0036 | ordinary-paragraph | high] with a constant C > 0 independent of h and v.

[p0116-b0037 | ordinary-paragraph | high] Note that this lemma requires no regularity of the triangulation.

## PDF 117 / printed 103



[p0117-b0003 | ordinary-paragraph | high] arbitrary N, by the functions of 6,.

[p0117-b0004 | lemma | high] Lemma A.6. Let r and p be reals with 1 <r, p < co. Under the assumption that 7,

[p0117-b0005 | ordinary-paragraph | high] is regular if 1/r — 1/p > 1/N or J, is uniformly regular otherwise, there exists a

[p0117-b0006 | ordinary-paragraph | high] constant C > 0 independent of h and x such that:

[p0117-b0007 | ordinary-paragraph | high] (A.31) lin SCANHy , =W KEF, We.

[p0117-b0008 | proof | high] Proof. Let ve O,; owing to (A.8), (A.2) and (A.3) we have:

[p0117-b0009 | equation | low] [lsr e < C1 (1/p,) (meas(x))"”"|6]2,.

[p0117-b0010 | ordinary-paragraph | high] But since 6 belongs to the finite-dimensional space P, on kK, we have

[p0117-b0011 | ordinary-paragraph | high] lols. e S Coll bllop.x

[p0117-b0012 | ordinary-paragraph | high] where the constant C, depends only on r, p, k, N and the geometry of &. Then

[p0117-b0013 | ordinary-paragraph | high] applying (A.7) and (A.3) we get:

[p0117-b0014 | ordinary-paragraph | high] (A.32) [ltr x < C3(1/p,)(meas(x))|"vI~ l"o,?y x :

[p0117-b0015 | ordinary-paragraph | high] In view of (A.4), if N(1/r — 1/p) > 1 the right-hand side of (A.32) involves a

[p0117-b0016 | ordinary-paragraph | high] positive power of h, and hence the regularity of 7, is sufficient to yield (A.31).

[p0117-b0017 | ordinary-paragraph | high] Otherwise, the uniform regularity of 7, is necessary to draw the same conclusion.

[p0117-b0018 | ordinary-paragraph | high] O

[p0117-b0019 | corollary | high] Corollary A.3. Let r andp be like in Lemma A.6 and assume J, is a uniformly

[p0117-b0020 | ordinary-paragraph | high] regular triangulation of 2. There exists a constant C > 0 independent of h such

[p0117-b0021 | ordinary-paragraph | high] that:

[p0117-b0022 | ordinary-paragraph | high] (A.33) ee Chae NENTS Io Vee O,.

[p0117-b0023 | proof | high] Proof. If r > p we derive (A.33) from (A.31) and Jensen’s inequality:

[p0117-b0024 | ordinary-paragraph | high] I Ir I 1/p

[p0117-b0025 | ordinary-paragraph | high] (A.34) (5a ) < (xa i”)

[p0117-b0026 | equation | low] i=1 i=1

[p0117-b0027 | ordinary-paragraph | high] which holds for every finite sum.

[p0117-b0028 | ordinary-paragraph | high] If r < p, we use the discrete version of Holder’s inequality:

[p0117-b0029 | ordinary-paragraph | high] I 1/r I I/p/ I 1/r—1/p

[p0117-b0030 | ordinary-paragraph | high] (A.35) (sj ai") < iya i") (x2 ) :

[p0117-b0031 | equation | low] t= i=1 i=1

[p0117-b0032 | ordinary-paragraph | high] with |a;| = ||0 |lo,p ,x» 5; = meas(x) and the summation runs over all « of 7;,. Thus

[p0117-b0033 | ordinary-paragraph | high] the uniform regularity of 7%, and (A.32) yield:

[p0117-b0034 | ordinary-paragraph | high] [ls,.,.9 < C3Lo/(th)]( meas(Q))"||"vl o?,p, 0- O

[p0117-b0035 | lemma | high] Lemma A.7. Let r and p be like in Lemma A.6 and let m be a non-negative integer.

## PDF 118 / printed 104



[p0118-b0003 | ordinary-paragraph | high] (A.36) Il anes (Clee Molar Yve@,.

[p0118-b0004 | proof | high] Proof. Clearly, (A.36) is obvious when r < p. When r > p, the proof is quite

[p0118-b0005 | ordinary-paragraph | high] similar to that of (A.33) and is left to the reader. O

[p0118-b0006 | ordinary-paragraph | high] A.2. Quadrilateral Finite Elements

[p0118-b0007 | ordinary-paragraph | high] This section is devoted exclusively to plane polygonal domains. Unless otherwise

[p0118-b0008 | ordinary-paragraph | high] specified, the notation is that of the preceding section. In addition, since several

[p0118-b0009 | ordinary-paragraph | high] properties of triangular finite elements are still valid for quadrilateral finite

[p0118-b0010 | ordinary-paragraph | high] elements, we shall focus our attention on those properties which are specific to

[p0118-b0011 | ordinary-paragraph | high] quadrilaterals.

[p0118-b0012 | definition | high] Definition A.3. For each integer k > 0, we denote by Q, the space of all polyno-

[p0118-b0013 | ordinary-paragraph | high] mials in the reference space (X,, X,) of the form:

[p0118-b0014 | equation | low] q(x) = Gees.

[p0118-b0015 | ordinary-paragraph | high] where the sum ranges over all integers i and j such that 0 <i,j < k.

[p0118-b0016 | ordinary-paragraph | high] G3

[p0118-b0017 | ordinary-paragraph | high] a,

[p0118-b0018 | figure | high] Figure 5. Quadrilateral K and its reference unit square K

[p0118-b0019 | ordinary-paragraph | high] Of course Q, coincides with P, but for all k > 1 we have the strict

[p0118-b0020 | ordinary-paragraph | high] inclusion

[p0118-b0021 | ordinary-paragraph | high] Pear

[p0118-b0022 | ordinary-paragraph | high] Let K denote the reference unit square [0,1] x [0,1] in the (X,,X,) reference

[p0118-b0023 | ordinary-paragraph | high] space, with vertices denoted by d,, 1 <j < 4, like in Figure 5. With the notations

[p0118-b0024 | ordinary-paragraph | high] of this figure, for each convex quadrilateral k with vertices a;, there exists

[p0118-b0025 | ordinary-paragraph | high] exactly

[p0118-b0026 | ordinary-paragraph | high] one invertible mapping F,,€ Qj that maps & onto x and is such that

[p0118-b0027 | equation | low] F.(4)=4, 1l<j<4.

## PDF 119 / printed 105



[p0119-b0003 | ordinary-paragraph | high] course d, coincides with a,). Note that unless x is a parallelogram, the mapping

[p0119-b0004 | ordinary-paragraph | high] F.. is not affine, but nevertheless it maps the sides of K onto the corresponding

[p0119-b0005 | ordinary-paragraph | high] sides of « and in fact the restriction of F, to the sides of & is affine.

[p0119-b0006 | ordinary-paragraph | high] For each &, let DF,(%) = [0F;,(%)/08,];Z,(;R¢* ; R*) denote the derivative of

[p0119-b0007 | ordinary-paragraph | high] F, at the point ¥ with the following norm:

[p0119-b0008 | equation | low] DE cose = sup || DF,.(X) ll,

[p0119-b0009 | ordinary-paragraph | high] where as usual ||. || stands for the subordinate Euclidean norm, and let J; denote

[p0119-b0010 | ordinary-paragraph | high] the Jacobian of F,., 1.e.

[p0119-b0011 | equation | low] J p(x) = det(DFAS)):

[p0119-b0012 | ordinary-paragraph | high] Then, if F-' denotes the inverse of F, with Jacobian J;-1, we have:

[p0119-b0013 | ordinary-paragraph | high] (A.37) DPS) ohe= (DE )\re Wp o l= Loe

[p0119-b0014 | ordinary-paragraph | high] Note again that when F, is affine, DF, = B,, D(F,') = (Be)* and Jp = det(B,.).

[p0119-b0015 | ordinary-paragraph | high] Of course, since J; is not constant the simple relation (A.3) does not hold here

[p0119-b0016 | ordinary-paragraph | high] but a plain calculation shows that J, belongs to P;. Hence, its extrema are

[p0119-b0017 | ordinary-paragraph | high] attained at the vertices of k. Thus it is easy to check that

[p0119-b0018 | equation | low] Max J;(x) = 2 Max meas(S;),

[p0119-b0019 | equation | low] Bers 1<i<4

[p0119-b0020 | ordinary-paragraph | high] (A.38) 4 :

[p0119-b0021 | equation | low] Min J,(x) = 2 Min meas(S;),

[p0119-b0022 | equation | low] XEK 1<i<4

[p0119-b0023 | ordinary-paragraph | high] and observe that

[p0119-b0024 | equation | low] Jp(X) > 0

[p0119-b0025 | ordinary-paragraph | high] because Kk is convex. Furthermore,

[p0119-b0026 | equation | low] J,(1/2, 1/2) = meas(x).

[p0119-b0027 | ordinary-paragraph | high] Hence, a glance at (A.37) and (A.38) shows that a convenient choice of parameters

[p0119-b0028 | ordinary-paragraph | high] to describe the geometry of x is:

[p0119-b0029 | equation | low] h,. = diameter of k,

[p0119-b0030 | equation | low] p, = 2 Min {diameter of circle inscribed in S;}-

[p0119-b0031 | equation | low] 1<i<4

[p0119-b0032 | ordinary-paragraph | high] This choice leads to the following upper bounds:

[p0119-b0033 | equation | low] | DF lloe <CiMes —e lleoe < Cale

[p0119-b0034 | ordinary-paragraph | high] (A.39)

[p0119-b0035 | equation | low] ||D F." Nheges < C2 (ie) pe), | Jp Ween < Cap.)

[p0119-b0036 | ordinary-paragraph | high] where all constants involved are independent of the geometry of k.

[p0119-b0037 | ordinary-paragraph | high] We use the same concept for the triangulation 7, except that here it is made

[p0119-b0038 | ordinary-paragraph | high] the above parameters, we

[p0119-b0039 | ordinary-paragraph | high] of convex quadrilaterals instead of triangles and with

[p0119-b0040 | ordinary-paragraph | high] triangulation. Note that

## PDF 120 / printed 106



[p0120-b0004 | ordinary-paragraph | high] Next, we turn to the finite element spaces. It stems from the geometry of

[p0120-b0005 | ordinary-paragraph | high] quadrilaterals that the basis functions here are not polynomials of P, but rather

[p0120-b0006 | ordinary-paragraph | high] are images of polynomials of Q,. To be specific, for each integer k > 0, and for

[p0120-b0007 | ordinary-paragraph | high] each element « of 7,, we introduce the finite-dimensional space:

[p0120-b0008 | ordinary-paragraph | high] (A.40) O.(k) = {4 = Go’; geQ}

[p0120-b0009 | ordinary-paragraph | high] and observe that O,(k) < @%(xk), but (unless « is a parallelogram) Q,(x) is not a

[p0120-b0010 | ordinary-paragraph | high] space of polynomials. Then, in order to study the approximation error in such a

[p0120-b0011 | ordinary-paragraph | high] space, we must modify slightly the statements of Theorem A.1 and its corollaries.

[p0120-b0012 | ordinary-paragraph | high] This is achieved by a change of seminorm: for each integer k > 0 and real p > 0,

[p0120-b0013 | ordinary-paragraph | high] we set

[p0120-b0014 | ordinary-paragraph | high] (A.41) [v]x,p.0 = (0*0/Ox4 18,p. 0 + []*v/0x3 118,p .0)"'?.

[p0120-b0015 | ordinary-paragraph | high] Clearly, [.Jo,».@ = ll-llo.p,@ and [-J1,p,9 =1-l1,p,93 in addition, this seminorm

[p0120-b0016 | ordinary-paragraph | high] has the following important property proved by Aronszajn & Smith (cf. Smith

[p0120-b0017 | ordinary-paragraph | high] [74]):

[p0120-b0018 | lemma | high] Lemma A.8. Let Q be a bounded domain of R? with a Lipschitz-continuous

[p0120-b0019 | ordinary-paragraph | high] boundary. For each integer k > 0 and real p > 0 there exists a positive constant C

[p0120-b0020 | ordinary-paragraph | high] such that

[p0120-b0021 | ordinary-paragraph | high] (A.42) lPllnne <C{IPllop,.e+ (hpe} Vor W%?(Q).

[p0120-b0022 | ordinary-paragraph | high] Now, Theorem A.1 and its first corollary have the following counterpart:

[p0120-b0023 | theorem | high] Theorem A.3. Let k > 0, m > 0 be integers and p > 1, gq > 1 be reals such that

[p0120-b0024 | ordinary-paragraph | high] Wir ER ices Was en).

[p0120-b0025 | ordinary-paragraph | high] Let Re L(W**! (Rk); W™4(R)) satisfy

[p0120-b0026 | ordinary-paragraph | high] hot Le Or

[p0120-b0027 | ordinary-paragraph | high] Then there exists a positive constant C that depends only on k, m, p, q, & and f,

[p0120-b0028 | ordinary-paragraph | high] such that

[p0120-b0029 | ordinary-paragraph | high] (A.43) |6 = £6|mae S CLOhs1,p,2 VOeW*? (2).

[p0120-b0030 | ordinary-paragraph | high] Thus, in order to estimate the interpolation error in Q,(x), we must derive an

[p0120-b0031 | ordinary-paragraph | high] upper bound for |v|,,,4,. in terms of 6 and for [6], +;,,,¢ in terms of v. This is the

[p0120-b0032 | ordinary-paragraph | high] object of the next lemma (compare with Lemma A.1). The material for the proof

[p0120-b0033 | ordinary-paragraph | high] can be found in Cartan [17].

[p0120-b0034 | lemma | high] Lemma A.9. Let « be a convex quadrilateral. For each integer m > 0 and real

[p0120-b0035 | ordinary-paragraph | high] pe[1, 0] there exist positive constants C,,C, and C; independent of the geometry

## PDF 121 / printed 107



[p0121-b0004 | equation | low] [Ulo. p,x ≤ Ch2/1P|0lo.p,x

[p0121-b0005 | ordinary-paragraph | medium] (A.44)

[p0121-b0006 | ordinary-paragraph | medium] 1/p

[p0121-b0007 | equation | low] [vm,p,x ≤ C2(hk/ pk)3m-2(h2/ / 

[p0121-b0008 | equation | low] m ≥ 1,

[p0121-b0009 | ordinary-paragraph | low] 创l,p,k

[p0121-b0010 | equation | low] [0]m,p,r ≤ Cs(hm/ p2/) |0lm,p,xs

[p0121-b0011 | equation | low] m≥0.

[p0121-b0012 | ordinary-paragraph | medium] (A.45)

[p0121-b0013 | ordinary-paragraph | medium] Then, we have the following analogue of Corollary A.2 (compare with Remark

[p0121-b0014 | ordinary-paragraph | medium] A.1).

[p0121-b0015 | corollary | medium] Corollary A.5. Let k be a convex quadrilateral and let k, m, p, q and f be like in

[p0121-b0016 | theorem | medium] Theorem A.3. We define the operator πE Q(Wk+1.P(k); Wm,a(k)) by:

[p0121-b0017 | equation | low] πU =O.

[p0121-b0018 | ordinary-paragraph | medium] Then there exists a positive constant C, independent of the geometry of k, such

[p0121-b0019 | ordinary-paragraph | medium] that:

[p0121-b0020 | ordinary-paragraph | low] K

[p0121-b0021 | equation | low] m≥1

[p0121-b0022 | ordinary-paragraph | medium] (A.46)

[p0121-b0023 | ordinary-paragraph | low] ()dI+M ≥aA

[p0121-b0024 | ordinary-paragraph | medium] When k belongs to a regular triangulation Jh, these two inequalities reduce to:

[p0121-b0025 | ordinary-paragraph | medium] (A.47)

[p0121-b0026 | remark | medium] Remark A.3. For all m ≥ 2, a simple exercise on the differentiation of compound

[p0121-b0027 | ordinary-paragraph | medium] functions shows that, unlike [o]m.p.x, the full seminorm |0im.p.x satisfies a very

[p0121-b0028 | ordinary-paragraph | medium] x. The trouble arises from the cross deriva-

[p0121-b0029 | ordinary-paragraph | medium] poor upper bound in terms of Ilullm.p,x:

[p0121-b0030 | ordinary-paragraph | medium] factor 0²F/0x,0x2 instead of products of the form (oF/ox,)(oF,/ox;). And,

[p0121-b0031 | ordinary-paragraph | medium] unless k is nearly a parallelogram, 02 F,/ox, 0x is only of the order of h, whereas

[p0121-b0032 | ordinary-paragraph | medium] (0F,/ox)(oF,/0x) is of the order of h2. This is why the seminorm [. Jm.p.2 plays

[p0121-b0033 | ordinary-paragraph | medium] a vital part in deriving accurate error estimates for quadrilateral finite elements.

[p0121-b0034 | remark | medium] Remark A.4. Observe that the exponent of the regularity factor o, is much higher

[p0121-b0035 | ordinary-paragraph | medium] in (A.46) than in (A.17). This comes from the fact that the transformation F is

[p0121-b0036 | ordinary-paragraph | medium] not affine.

[p0121-b0037 | ordinary-paragraph | medium] Like in the preceding section, we fix an integer k > 1 and we introduce similar

[p0121-b0038 | ordinary-paragraph | medium] finite element spaces:

[p0121-b0039 | equation | low] On = {0n∈6(); Onlx∈Qk(K) Vre gh},

[p0121-b0040 | equation | low] Dh = O, N H(Ω).

[p0121-b0041 | ordinary-paragraph | medium] We obtain the analogue of the interpolant I, by interpolating first the function

## PDF 122 / printed 108



[p0122-b0004 | equation | low] E= {(i/k,j/k); 0 ≤i,j ≤k},

[p0122-b0005 | ordinary-paragraph | medium] i.e. for each 0e C"(k), we set

[p0122-b0006 | ordinary-paragraph | low] Ite Qk,

[p0122-b0007 | ordinary-paragraph | low] VXeEx.

[p0122-b0008 | equation | low] [0(x) = 0(x)

[p0122-b0009 | ordinary-paragraph | medium] (A.48)

[p0122-b0010 | ordinary-paragraph | medium] Then, if J, is regular the interpolation operator I, defined on each k of Z, by

[p0122-b0011 | equation | low] Ihu = I0

[p0122-b0012 | ordinary-paragraph | low] (0)083A

[p0122-b0013 | ordinary-paragraph | medium] satisfies the conclusions of Lemma A.2, namely:

[p0122-b0014 | ordinary-paragraph | low] ()aI+sM aA

[p0122-b0015 | equation | low] |u — Inulm,p,2 ≤ Chs+1-m|Dls+1,p,2

[p0122-b0016 | ordinary-paragraph | medium] (A.49)

[p0122-b0017 | equation | low] 0≤m≤ s+ 1,

[p0122-b0018 | equation | low] VmeN,  Vs, pe R with p > 1,

[p0122-b0019 | ordinary-paragraph | medium] and

[p0122-b0020 | equation | low] Vu∈Wl,a(Ω),  q> 2,

[p0122-b0021 | ordinary-paragraph | medium] (A.50) Iu -- Inulm,g,α ≤ Chi-m|ul1,q,2

[p0122-b0022 | ordinary-paragraph | medium] m = 0, 1.

[p0122-b0023 | ordinary-paragraph | medium] Similarly, we define the interpolation operator I on W2.e(k) for p > 1 by:

[p0122-b0024 | ordinary-paragraph | low] TRueQk,

[p0122-b0025 | equation | low] Iu(a:;) = 0(ai)

[p0122-b0026 | equation | low] 1≤i≤ 4,

[p0122-b0027 | equation | low] (I - 0)fds =0  Vf∈Pk-2(k'),

[p0122-b0028 | ordinary-paragraph | medium] Vsides k' of k,

[p0122-b0029 | ordinary-paragraph | medium] ifk≥ 2

[p0122-b0030 | equation | low] (Ix - 0)fdx = O  Vf∈Qk-2(k).

[p0122-b0031 | ordinary-paragraph | medium] Following the lines of Lemma A.3, it can be easily proved that this system of

[p0122-b0032 | ordinary-paragraph | medium] linear equations defines I uniquely. Then, if , is regular, the operator I, defined

[p0122-b0033 | ordinary-paragraph | medium] in each k of J, by

[p0122-b0034 | equation | low] Vue W2,p(Ω) with p > 1

[p0122-b0035 | equation | low] IhU=I6

[p0122-b0036 | ordinary-paragraph | medium] satisfies the statement of Lemma A.4.

[p0122-b0037 | ordinary-paragraph | medium] Likewise, the projections P, and P, can be extended to the case of quadrilat-

[p0122-b0038 | ordinary-paragraph | medium] erals and it can be shown that they have the same properties as in the triangular

[p0122-b0039 | ordinary-paragraph | medium] case. Similarly, the L² projection p, defined by:

[p0122-b0040 | ordinary-paragraph | low] pu∈Qk

[p0122-b0041 | ordinary-paragraph | medium] on k

[p0122-b0042 | ordinary-paragraph | medium] (A.51)

[p0122-b0043 | equation | low] (po - 0)fdx = 0  Vf∈Qk)

[p0122-b0044 | ordinary-paragraph | low] K

[p0122-b0045 | ordinary-paragraph | low] ()TA 6A

[p0122-b0046 | equation | low] PnU =po

[p0122-b0047 | ordinary-paragraph | medium] satisfies the statement of Lemma A.5 provided the triangulation is regular.

[p0122-b0048 | ordinary-paragraph | medium] Finally, Lemma A.6 and Corollary A.3 remain valid in the case of quadrilat-

## PDF 123 / printed 109



[p0123-b0003 | ordinary-paragraph | high] Nevertheless these two values of m are sufficient for subsequent applications.

[p0123-b0004 | remark | high] Remark A.5. It is sometimes very useful to construct triangulations which contain

[p0123-b0005 | ordinary-paragraph | high] triangles as well as quadrilaterals. All the results which are valid for both triangles

[p0123-b0006 | ordinary-paragraph | high] and quadrilaterals can be applied to these triangulations.

[p0123-b0007 | ordinary-paragraph | high] A.3. Interpolation of Discontinuous Functions

[p0123-b0008 | ordinary-paragraph | high] The interpolation of L' functions was first analyzed by Clément [21] who

[p0123-b0009 | ordinary-paragraph | high] proposed a local regularization operator. This technique was later generalized by

[p0123-b0010 | ordinary-paragraph | high] Bernardi [9] who introduced more general finite elements in order to interpolate

[p0123-b0011 | ordinary-paragraph | high] essentially functions that were either discontinuous or that were defined on

[p0123-b0012 | ordinary-paragraph | high] domains with curved boundaries. We have no space here to describe “curved”

[p0123-b0013 | ordinary-paragraph | high] finite elements but we shall discuss briefly the interpolation of functions that

[p0123-b0014 | ordinary-paragraph | high] are not supposed to be continuous. For the sake of simplicity, we shall restrict

[p0123-b0015 | ordinary-paragraph | high] ourselves to the finite element space O, defined by (A.18) on triangular finite

[p0123-b0016 | ordinary-paragraph | high] elements. The forthcoming results are valid for higher dimensions and quadrilat-

[p0123-b0017 | ordinary-paragraph | high] eral finite elements and also for spaces with other boundary conditions, like for

[p0123-b0018 | example | high] example 0,9 Hj(2).

[p0123-b0019 | ordinary-paragraph | high] Let 7, be the triangulation of Q corresponding to @, and let

[p0123-b0020 | equation | low] X,= U = tas 1<i<N,},

[p0123-b0021 | ordinary-paragraph | high] KeT,

[p0123-b0022 | ordinary-paragraph | high] all the points a; being distinct. For each integer i, 1 <i < N,, there exists exactly

[p0123-b0023 | ordinary-paragraph | high] one function 6; € 0, such that

[p0123-b0024 | equation | low] 6;(a;) = Oij> iN,

[p0123-b0025 | ordinary-paragraph | high] The set {0,;1 <i < N,} isa basis of 0,. Now, for each i, let

[p0123-b0026 | equation | low] \ = (J {xe J; supp(0,) 1k 4 $}

[p0123-b0027 | ordinary-paragraph | high] A.52

[p0123-b0028 | ordinary-paragraph | high] rae = |) {ke F,; a;€ Kk}.

[p0123-b0029 | ordinary-paragraph | high] If the triangulation 7, is regular, it can be shown that on the one hand, the

[p0123-b0030 | ordinary-paragraph | high] say M, independent of h

[p0123-b0031 | ordinary-paragraph | high] number of triangles « in 4; is bounded by a constant,

[p0123-b0032 | ordinary-paragraph | high] macro-elements 4; containing a given

[p0123-b0033 | ordinary-paragraph | high] and i: on the other hand, the number of

[p0123-b0034 | ordinary-paragraph | high] of « and h. In addition, for

[p0123-b0035 | ordinary-paragraph | high] triangle x is also bounded by a constant independent

[p0123-b0036 | ordinary-paragraph | high] pair of triangles « and x’ in the same macro-element 4; we have:

[p0123-b0037 | ordinary-paragraph | high] any

[p0123-b0038 | equation | low] h, < Ch, with a constant C independent of h and i.

[p0123-b0039 | ordinary-paragraph | high] macro-elements 4; can only assume a finite number of different

[p0123-b0040 | ordinary-paragraph | high] Thus, the

[p0123-b0041 | ordinary-paragraph | high] To each configuration, there corresponds a reference region 4;,

[p0123-b0042 | ordinary-paragraph | high] configurations.

[p0123-b0043 | ordinary-paragraph | high] the unit disc{%;||X|| <1}, and composed of at most M equal

[p0123-b0044 | ordinary-paragraph | high] contained in

[p0123-b0045 | example | high] example of Figure 6). Further-

[p0123-b0046 | ordinary-paragraph | high] triangles with a common vertex at X = 0 (see the

## PDF 124 / printed 110



[p0124-b0004 | ordinary-paragraph | medium] that

[p0124-b0005 | ordinary-paragraph | medium] Fa;lx,  is an affine mapping from k; onto Kj

[p0124-b0006 | ordinary-paragraph | medium] for all k; contained in A.

[p0124-b0007 | equation | low] (0.0)

[p0124-b0008 | equation | low] (0.0)

[p0124-b0009 | ordinary-paragraph | low] △

[p0124-b0010 | ordinary-paragraph | low] .

[p0124-b0011 | ordinary-paragraph | low] Ai

[p0124-b0012 | ordinary-paragraph | low] △:

[p0124-b0013 | ordinary-paragraph | medium] 1

[p0124-b0014 | figure | medium] Figure 6. Examples of regions A; and their reference regions 

[p0124-b0015 | ordinary-paragraph | medium] Now, we are in a position to define an interpolation operator R, e Φ(L'(Q);

[p0124-b0016 | ordinary-paragraph | medium] n) by a local L? projection. Let 4; be any macro-element, A; its reference region

[p0124-b0017 | equation | low] (R;0 - 0)pdx = 0

[p0124-b0018 | ordinary-paragraph | medium] (A.53)

[p0124-b0019 | ordinary-paragraph | medium] Vpe P(Ai).

[p0124-b0020 | ordinary-paragraph | medium] Then, for ve L'(Ω) we define R,u e O, by

[p0124-b0021 | ordinary-paragraph | medium] Nn

[p0124-b0022 | ordinary-paragraph | low] R;(uoF)(a;)0i,

[p0124-b0023 | equation | low] R,u =

[p0124-b0024 | ordinary-paragraph | medium] (A.54)

[p0124-b0025 | ordinary-paragraph | low] 台

[p0124-b0026 | ordinary-paragraph | medium] where a; = F7;(a:). It is proved in Clément [21] and Bernardi (loc. cit.) that this

## PDF 125 / printed 111



[p0125-b0004 | ordinary-paragraph | medium] the advantage that it works on rough functions. The major local interpolation

[p0125-b0005 | ordinary-paragraph | medium] result is:

[p0125-b0006 | theorem | medium] Theorem A.4. Let J, be a regular triangulation of Q, k an arbitrary triangle of Jh,

[p0125-b0007 | ordinary-paragraph | medium] I and m two positive integers with 0 ≤ l ≤ k + 1 and p and q two real numbers in

[p0125-b0008 | ordinary-paragraph | medium] [1, o] such that:

[p0125-b0009 | ordinary-paragraph | medium] (x)nuM  (x)aM

[p0125-b0010 | ordinary-paragraph | medium] Let A denote the union of all macro-elements A; containing k. Then for all functions

[p0125-b0011 | ordinary-paragraph | medium] Ue Wl,r() we have the estimate:

[p0125-b0012 | ordinary-paragraph | medium] (A.55)

[p0125-b0013 | ordinary-paragraph | medium] with a constant C independent of k, h and v.
