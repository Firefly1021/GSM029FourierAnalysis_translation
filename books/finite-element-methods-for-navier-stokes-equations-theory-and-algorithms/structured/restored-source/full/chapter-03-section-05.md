# Restored-source review candidate: chapter-03-section-05



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 271 / printed 257



[p0271-b0004 | remark | high] Remark 4.7. Of course, we can use here a continuous approximation of the

[p0271-b0005 | ordinary-paragraph | high] pressure analogous to (2.36), but the error analysis of the corresponding scheme

[p0271-b0006 | ordinary-paragraph | high] is more delicate.

[p0271-b0007 | section | high] §5. A “Vector Potential-Vorticity” Scheme in Three

[p0271-b0008 | ordinary-paragraph | high] Dimensions

[p0271-b0009 | ordinary-paragraph | high] It is not easy to adapt the schemes developed in the previous paragraphs to the

[p0271-b0010 | ordinary-paragraph | high] three-dimensional Stokes problem. The obvious reason is that the conditions

[p0271-b0011 | ordinary-paragraph | high] determining the vector potential are more intricate than those defining the

[p0271-b0012 | ordinary-paragraph | high] two-dimensional stream function. Therefore we shall only attempt to extend to

[p0271-b0013 | ordinary-paragraph | high] the homogeneous Stokes problem in a very simple region of R° the “stream

[p0271-b0014 | ordinary-paragraph | high] function-vorticity” scheme of § 2.

[p0271-b0015 | ordinary-paragraph | high] Throughout this paragraph, we shall assume that Q is a bounded, simply-

[p0271-b0016 | ordinary-paragraph | high] connected open subset of R? with a polyhedral connected bounded I. Leaving the

[p0271-b0017 | ordinary-paragraph | high] approximation of the pressure to the last section, our first object is to relax the

[p0271-b0018 | ordinary-paragraph | high] regularity of the function spaces related to the biharmonic problems of Section

[p0271-b0019 | ordinary-paragraph | high] 1.5.3. The reader will discover that it suffices to work with functions in H(curl; Q).

[p0271-b0020 | ordinary-paragraph | high] This approach will lead to the construction of finite-dimensional subspaces of

[p0271-b0021 | ordinary-paragraph | high] conforming finite elements in H(curl; Q), which are not subspaces of H'(Q)’.

[p0271-b0022 | ordinary-paragraph | high] Finally, since discontinuous elements are used it is reasonable to use a

[p0271-b0023 | ordinary-paragraph | high] discontinuous approximation of the pressure, very similar to that of Section 4.4.

[p0271-b0024 | subsection | high] 5.1. A Mixed Formulation of the Three-Dimensional Stokes Problem

[p0271-b0025 | ordinary-paragraph | high] Let f be a given vector of L?(Q)? and consider the homogeneous Stokes Problem:

[p0271-b0026 | ordinary-paragraph | high] Find (u, p) in H*(Q)> x L6(Q) satisfying:

[p0271-b0027 | equation | low] —vAu + gradp = f,

[p0271-b0028 | ordinary-paragraph | high] in Q,

[p0271-b0029 | ordinary-paragraph | high] (5.1) divu=0

[p0271-b0030 | ordinary-paragraph | high] u— 0 Tonl.

[p0271-b0031 | ordinary-paragraph | high] biharmonic

[p0271-b0032 | ordinary-paragraph | high] We have seen in Section I.5.3 that this problem can be interpreted as a

[p0271-b0033 | ordinary-paragraph | high] problem for the vector potential y of u (recall that u = curl y) where w belongs

[p0271-b0034 | ordinary-paragraph | high] to the space:

[p0271-b0035 | ordinary-paragraph | high] (5.2) YW = {pe L7(Q); divde H'(Q), cuper Hyl(@)° *, @ x np = OF.

[p0271-b0036 | ordinary-paragraph | high] order to derive a mixed formulation of Problem (5.1), let us multiply both

[p0271-b0037 | ordinary-paragraph | high] In

[p0271-b0038 | ordinary-paragraph | high] with curl and determine exactly what properties we require of @.

[p0271-b0039 | ordinary-paragraph | high] sides of (5.1)

## PDF 272 / printed 258



[p0272-b0004 | ordinary-paragraph | low] ()HA(

[p0272-b0005 | equation | low] v<curl curl u, curl Φ> = (f, curl Φ)

[p0272-b0006 | ordinary-paragraph | high] where < ., . > denotes the duality between Ho(curl; Ω) and its dual space. Now, let

[p0272-b0007 | ordinary-paragraph | high] us set

[p0272-b0008 | equation | low] ① = curl u

[p0272-b0009 | equation | low] (5.3)

[p0272-b0010 | ordinary-paragraph | high] and assume that o e H(curl; Ω); then we have

[p0272-b0011 | ordinary-paragraph | low] ()HA

[p0272-b0012 | equation | low] v(curl o, curl Φ) = (f, curl Φ)

[p0272-b0013 | ordinary-paragraph | high] Finally, since

[p0272-b0014 | equation | low] u = curly with div y = O and yeY,

[p0272-b0015 | ordinary-paragraph | high] equation (5.3) can be written equivalently as:

[p0272-b0016 | ordinary-paragraph | low] E()TA

[p0272-b0017 | equation | low] (curl curl w,p) = (o,μ)

[p0272-b0018 | ordinary-paragraph | high] And by restricting μ to H(curl; Ω) this becomes:

[p0272-b0019 | ordinary-paragraph | medium] ()HA

[p0272-b0020 | equation | low] (curl w, curl μ) = (@,μ)

[p0272-b0021 | ordinary-paragraph | high] Hence, summing up we see that the following Problem (Q):

[p0272-b0022 | ordinary-paragraph | high] Find a pair (y,?)e Ho(curl; Q) x H(curl; Q) such that:

[p0272-b0023 | equation | low] (5.4)

[p0272-b0024 | equation | low] v(curl o, curl Φ) = (f, curl Φ)Φ e Ho(curl; Ω),

[p0272-b0025 | equation | low] (5.5)

[p0272-b0026 | equation | low] (curl y, curl μ) = (o, p)

[p0272-b0027 | ordinary-paragraph | low] ()HA (

[p0272-b0028 | equation | low] divv = 0,

[p0272-b0029 | equation | low] (5.6)

[p0272-b0030 | ordinary-paragraph | high] has at least one solution (w, w = -- 4w) where u = curl y and y e Y. Conversely,

[p0272-b0031 | ordinary-paragraph | high] it is easy to check that this problem has at most one solution. Indeed, if

[p0272-b0032 | equation | low] (curl w, curl Φ) = 0  VΦ ∈ Ho(curl; Ω),

[p0272-b0033 | ordinary-paragraph | low]  0 = o Aeaissons io m ('s) ui m = n pue  =  susoouo u

[p0272-b0034 | ordinary-paragraph | high] curl y = 0. Since div y = O and F has only one connected component this implies

[p0272-b0035 | ordinary-paragraph | high] that y = 0 (cf. Remark 1.3.9). Therefore, we have proved the following result:

[p0272-b0036 | theorem | high] Theorem 5.1. Assume that the solution u of Problem (5.1) satisfies

[p0272-b0037 | equation | low] curl ue H(curl; Ω).

[p0272-b0038 | ordinary-paragraph | high] Then Problem (5.4) (5.5) (5.6) has the unique solution:

[p0272-b0039 | equation | low] (W, - 4w) where curl y = u.

[p0272-b0040 | ordinary-paragraph | high] Now we want to insert Problem (Q) into the framework of Section 1.1. We set

[p0272-b0041 | equation | low] Do = {Φe Ho(curl; Ω); div Φ = 0}.

[p0272-b0042 | ordinary-paragraph | high] Clearly, Problem (Q) is equivalent to:

## PDF 273 / printed 259



[p0273-b0004 | ordinary-paragraph | medium] VpeΦo,

[p0273-b0005 | equation | low] v(curl o, curlΦ) = (f, curl Φ)

[p0273-b0006 | equation | low] (5.7)

[p0273-b0007 | equation | low] (curl y, curl μ) = (o, μ)

[p0273-b0008 | ordinary-paragraph | low] ( )Ha

[p0273-b0009 | ordinary-paragraph | medium] Next, we introduce:

[p0273-b0010 | equation | low] X = {curlΦ;Φ∈Φo} × L²(Ω)3,  N

[p0273-b0011 | equation | low] M = H(curl; Ω),

[p0273-b0012 | equation | low] ，  v = (curl Φ,0)e X,

[p0273-b0013 | equation | low] ) Vu = (curly,@),

[p0273-b0014 | equation | low] a(u,v) = v(∞, 0)

[p0273-b0015 | equation | low] b(v,μ) = (curl Φ, curl μ) - (0,μ)

[p0273-b0016 | equation | low] Vv = (curlΦ,0)e X,  μe M,

[p0273-b0017 | equation | low] Vv = (curlΦ, 0)e X.

[p0273-b0018 | equation | low] <l,v> =(f, curi Φ)

[p0273-b0019 | ordinary-paragraph | medium] With this notation, Problem (Q) takes the more familiar form:

[p0273-b0020 | ordinary-paragraph | medium] Find a pair (u, X) in X × M such that:

[p0273-b0021 | ordinary-paragraph | medium] VueX,

[p0273-b0022 | equation | low] a(u,u) + b(v,2) =<l,v)

[p0273-b0023 | equation | low] (5.8)

[p0273-b0024 | ordinary-paragraph | medium] Wue M.

[p0273-b0025 | equation | low] b(u,μ) = 0 

[p0273-b0026 | ordinary-paragraph | medium] As usual, the space V is defined by:

[p0273-b0027 | equation | low] V ={u∈X;b(u,μ) =O VμeM},

[p0273-b0028 | ordinary-paragraph | medium] i.e.

[p0273-b0029 | equation | low] V = {u = (curl Φ, 0)e X; (curl Φ,curl μ) = (0,μ)

[p0273-b0030 | ordinary-paragraph | low] {( )H A

[p0273-b0031 | ordinary-paragraph | medium] Since the mapping Φ -→ llcurl Φ lio,o is a norm on Φ。 equivalent to the norm of

[p0273-b0032 | ordinary-paragraph | medium] H(curl; Ω) (cf. Lemma I.3.4):

[p0273-b0033 | ordinary-paragraph | low] V$e Po,

[p0273-b0034 | equation | low] IΦ llo.o ≤ C ll curl Φllo,2

[p0273-b0035 | equation | low] (5.9)

[p0273-b0036 | ordinary-paragraph | medium] it follows that on the one hand we can choose the following norm on X:

[p0273-b0037 | equation | low] |lullx = (l/ curlΦll3.2 + 1|10l1,)1/2

[p0273-b0038 | equation | low] Vv = (curlΦ, 0)e X;

[p0273-b0039 | ordinary-paragraph | medium] and on the other hand we have:

[p0273-b0040 | equation | low] Vv = (curl Φ, 0)e V.

[p0273-b0041 | equation | low] Il curl Φ llo,o ≤ C l0 llo.s

[p0273-b0042 | equation | low] (5.10)

[p0273-b0043 | ordinary-paragraph | medium] Hence the mapping v = (curl Φ,0) → I/0llo.s is a norm on V equivalent to the norm

[p0273-b0044 | ordinary-paragraph | low] of x:

[p0273-b0045 | equation | low] lullx ≤ (C2 + 1)1/21I101l0,2

[p0273-b0046 | ordinary-paragraph | medium] and we set:

[p0273-b0047 | equation | low] |u| = [|0ll0o.2.

[p0273-b0048 | ordinary-paragraph | medium] As a consequence, the form a( ., .) is V-elliptic:

[p0273-b0049 | ordinary-paragraph | medium] Vue V,

[p0273-b0050 | equation | low] a(v,u) =v|ul²≥@|lu1

[p0273-b0051 | ordinary-paragraph | medium] with & = v/(C² + 1).

## PDF 274 / printed 260



[p0274-b0003 | ordinary-paragraph | high] condition:

[p0274-b0004 | equation | low] sup (b(v, w)/|lvllz) > lItllo.g =Y nM .

[p0274-b0005 | ordinary-paragraph | high] veX

[p0274-b0006 | ordinary-paragraph | high] Finally, we readily derive that here the Lagrange multiplier 4 satisfies 4 = vo.

[p0274-b0007 | remark | high] Remark 5.1. Observe the analogy between Problem (5.7) and Problem (2.20) in

[p0274-b0008 | ordinary-paragraph | high] two dimensions.

[p0274-b0009 | remark | high] Remark 5.2. Note that the first equation of (5.8) holds on a larger space than xe

[p0274-b0010 | equation | low] a(u,v) + b(v,4) = <Lv> Vv = (curl 6, 8)

[p0274-b0011 | equation | low] with (o, 8) € Ho(curl; Q) x L?(Q)°.

[p0274-b0012 | subsection | high] 5.2. Mixed Approximation in H (curl; Q2)

[p0274-b0013 | ordinary-paragraph | high] The statement of Problem (Q) induces us to define its approximation in finite-

[p0274-b0014 | ordinary-paragraph | high] dimensional subspaces of H(curl; 2). Thus, we introduce three finite-dimensional

[p0274-b0015 | ordinary-paragraph | high] spaces:

[p0274-b0016 | ordinary-paragraph | high] (Geil) ®, < H,(curl;2), M, < H(curl;Q), 0, < H3(Q)

[p0274-b0017 | ordinary-paragraph | high] and we assume that

[p0274-b0018 | equation | low] @, < M,,.

[p0274-b0019 | ordinary-paragraph | high] Since &, is not necessarily contained in H(div; Q), the divergence-free condition

[p0274-b0020 | ordinary-paragraph | high] is expressed by:

[p0274-b0021 | ordinary-paragraph | high] (5.12) (,,gradq,)=90 YVq,€O,.

[p0274-b0022 | ordinary-paragraph | high] In other words, the space ®, is approximated by:

[p0274-b0023 | ordinary-paragraph | high] (S213) Pio = (0, € ®,; o,, satisfies (5.12)},

[p0274-b0024 | ordinary-paragraph | high] which, in general, is not contained in ©). Nevertheless, it is reasonable to ask

[p0274-b0025 | ordinary-paragraph | high] that the functions of ®, 9s atisfy the same equivalence of norms as ®,, namely:

[p0274-b0026 | ordinary-paragraph | high] there exists a positive constant C* > 0 such that:

[p0274-b0027 | ordinary-paragraph | high] (5.14) IPillo.e < C*lleurl Oy |lo.o VO, Dyo-

[p0274-b0028 | ordinary-paragraph | high] With these spaces, we propose the following approximation of Problem (5.7)

[p0274-b0029 | ordinary-paragraph | high] called Problem (Q,):

[p0274-b0030 | equation | low] Find a pair (W;,,@),)€ yo < M,, such that:

[p0274-b0031 | equation | low] eee @,, curl d,) = (f,curld,) VYo,€ Pyo,

[p0274-b0032 | ordinary-paragraph | high] (5:15)

[p0274-b0033 | equation | low] (curl y,,curlp,) = (@,,H,) Va, My.

## PDF 275 / printed 261



[p0275-b0003 | ordinary-paragraph | high] following approximation of Problem (Q) which works with the entire space ©,

[p0275-b0004 | ordinary-paragraph | high] Find a pair (W,,, @),)€ Pyo < My, satisfying:

[p0275-b0005 | equation | low] ce @,, curl ,) = (f,curlo,) Vo, %,,

[p0275-b0006 | equation | low] (5.16)

[p0275-b0007 | equation | low] (curl y,, curl p,,) = (@,,H,) Va,eM,,.

[p0275-b0008 | ordinary-paragraph | high] Obviously, it is desirable that these two problems be equivalent; but this requires

[p0275-b0009 | ordinary-paragraph | high] an additional hypothesis:

[p0275-b0010 | ordinary-paragraph | high] for each function ,, of &, there exists a function Ojo Of Pyo with

[p0275-b0011 | ordinary-paragraph | high] (5.17) curl o, = curl d, 0.

[p0275-b0012 | ordinary-paragraph | high] Clearly, (5.17) implies the equivalence between Problems (5.15) and (5.16).

[p0275-b0013 | ordinary-paragraph | high] As far as the solution of these problems is concerned, uniqueness implies

[p0275-b0014 | ordinary-paragraph | high] existence, for (5.15) is a square system of linear equations. Like in the continuous

[p0275-b0015 | ordinary-paragraph | high] case, we readily infer this existence from (5.14) and the inclusion ®, < M,. Hence

[p0275-b0016 | ordinary-paragraph | high] we have the following result.

[p0275-b0017 | lemma | high] Lemma 5.1. Let the spaces ®,, M,, and @,, satisfy (5.11) with ®, < M,, and let ®,o

[p0275-b0018 | ordinary-paragraph | high] be defined by (5.13). Under the hypothesis (5.14), Problem (Q,) has a unique solution

[p0275-b0019 | ordinary-paragraph | high] (w,,@,)in ®,. x M,,. If, in addition the hypothesis (5.17) holds, then Problem (5.16)

[p0275-b0020 | ordinary-paragraph | high] is equivalent to Problem (Q,).

[p0275-b0021 | ordinary-paragraph | high] It is possible to derive directly an error bound for the solution of (Q,), but it

[p0275-b0022 | ordinary-paragraph | high] is easier and more satisfactory to place this problem into the setting of Section

[p0275-b0023 | ordinary-paragraph | high] 1.2 and use Theorem 1.2. Here, there is a slight difficulty because the natural

[p0275-b0024 | ordinary-paragraph | high] discretization of X: (curl ®,,) x M,, is not contained in X. However we can make

[p0275-b0025 | ordinary-paragraph | high] use of Remark 5.2 and observe that the crucial spaces of Problem (5.8) are in fact

[p0275-b0026 | ordinary-paragraph | high] H,( curl; Q) x L?(Q)° and V. Thus, we take

[p0275-b0027 | ordinary-paragraph | high] (5.18) X, = feurldy; b,€ Dio} x M, < {curl; o € Ho(curlQ;) } x L?(Q)?,

[p0275-b0028 | ordinary-paragraph | high] (5.19) V, = {(curl o,, ,) € X;,; (curl p,, curl w,) = (0, Mi) Vine My}.

[p0275-b0029 | ordinary-paragraph | high] Ofc ourse, V, is generally not included in V but if ®, < M, and if (5.14) holds then

[p0275-b0030 | ordinary-paragraph | high] we have the analogue of( 5.10):

[p0275-b0031 | ordinary-paragraph | high] (5.20) curl, |lo,0 < C*|9pllo,0 Wn = (curl, 0,)€ Vi,

[p0275-b0032 | ordinary-paragraph | high] which means that the mapping v,= (curl o,,9,) > || 9\;/ o,0 = Um 1s. an equivalent

[p0275-b0033 | ordinary-paragraph | high] norm on J,.

[p0275-b0034 | ordinary-paragraph | high] With this notation, Problem (Q,,) becomes:

[p0275-b0035 | ordinary-paragraph | high] Find a pair (uj, 4,)€X }, X M,, such that

[p0275-b0036 | equation | low] G(Uj, Vp) + b(v,, dn) =<Lu,> VWoy,EXn

[p0275-b0037 | equation | low] b(uy,H,) =O Vane My.

## PDF 276 / printed 262



[p0276-b0003 | ordinary-paragraph | high] solution u, = (curl y,, @,) of Problem (Q,,) satisfies the error estimate:

[p0276-b0004 | ordinary-paragraph | high] (5.21) ||@ — @llo,o <2 inf |u—v,|+ (1+ C**)? inf |l}o — pyllaceurt2 )

[p0276-b0005 | ordinary-paragraph | high] vaeVy, Phe My,

[p0276-b0006 | equation | low] llcurl(y — w,)llo.o < (1 + C*)"?

[p0276-b0007 | ordinary-paragraph | high] (5.22) e .

[p0276-b0008 | equation | low] x 1i af Ju—yllg4-C* inf |o — pyllgeanaye

[p0276-b0009 | ordinary-paragraph | high] vneVy, Hnpe My,

[p0276-b0010 | ordinary-paragraph | high] where C* is the constant of (5.14).

[p0276-b0011 | ordinary-paragraph | high] Like in the two-dimensional case, we are now faced with the evaluation of the

[p0276-b0012 | ordinary-paragraph | high] approximation error of V,: inf, -y, ||u — U,||z- It is easy to see that the statement

[p0276-b0013 | ordinary-paragraph | high] of Lemma 3.1 is still valid here.

[p0276-b0014 | lemma | high] Lemma 5.2. With the notations of Lemma 5.1 we have the upper bound for all

[p0276-b0015 | ordinary-paragraph | high] v = (curl d, 0) V:

[p0276-b0016 | equation | low] curl(d — , curl

[p0276-b0017 | ordinary-paragraph | high] inf |v — w,| < inf {2k— v,| + sup Guid mt

[p0276-b0018 | ordinary-paragraph | high] wneVn vp=(curl b;,,9;,)eXy, ,e My, IlP a llo.e

[p0276-b0019 | equation | low] (5.23)

[p0276-b0020 | ordinary-paragraph | high] and a similar upper bound for ||v — w, || with the norm |.| replaced by ||. ||z i n the

[p0276-b0021 | ordinary-paragraph | high] right-hand side side of (5.23).

[p0276-b0022 | subsection | high] 5.3. A Family of Conforming Finite Elements in H (curl; Q)

[p0276-b0023 | ordinary-paragraph | high] In this section, we present a space of finite elements developed by Nédélec [59,

[p0276-b0024 | ordinary-paragraph | high] 60]. Its construction is by no means straightforward, inasmuch as it requires

[p0276-b0025 | ordinary-paragraph | high] exactly the continuity of the tangential components at element interfaces. This

[p0276-b0026 | ordinary-paragraph | high] implies that we must work with incomplete spaces of polynomials of (say) degree

[p0276-b0027 | ordinary-paragraph | high] l, for some integer / > 1.

[p0276-b0028 | ordinary-paragraph | high] Let P, denote the space of homogeneous polynomials of degree | in R? and

[p0276-b0029 | ordinary-paragraph | high] consider the following subspaces of P;:

[p0276-b0030 | equation | low] a = {pePP ; p(x)-x = 0, x = (1x2,, x5 )},

[p0276-b0031 | equation | low] (5.24)

[p0276-b0032 | ordinary-paragraph | high] R, ae PS CD) Si.

[p0276-b0033 | ordinary-paragraph | high] Examples. Let us exhibit S, and S,. Clearly, all homogeneous polynomial vectors

[p0276-b0034 | ordinary-paragraph | high] of degree one that satisfy p(x): x = 0 must necessarily be of the form:

[p0276-b0035 | equation | low] pix) =a x x

[p0276-b0036 | ordinary-paragraph | high] where @ is an arbitrary vector of R*. Thus, S, has the basis:

[p0276-b0037 | equation | low] Pi(x) = (0, —x3,X2), — Pa(x) = (x3,0, — x),

[p0276-b0038 | equation | low] p3(x) = (—x2,X,,0) .

## PDF 277 / printed 263



[p0277-b0003 | ordinary-paragraph | high] form:

[p0277-b0004 | ordinary-paragraph | high] 3

[p0277-b0005 | equation | low] p(x) = >) «,;x;p(x) with the above p,.

[p0277-b0006 | equation | low] i, j=1

[p0277-b0007 | ordinary-paragraph | high] But the nine polynomials x;p,(x) are not all linearly independent, for they are

[p0277-b0008 | ordinary-paragraph | high] linked by one relation:

[p0277-b0009 | equation | low] X:pi(x) =x x x = 0.

[p0277-b0010 | ordinary-paragraph | high] ee

[p0277-b0011 | equation | low] i=1

[p0277-b0012 | ordinary-paragraph | high] Thus we can suppress one of these polynomials and it can be readily checked

[p0277-b0013 | ordinary-paragraph | high] that the remaining eight are linearly independent. For example, we can take for

[p0277-b0014 | ordinary-paragraph | high] S, the following eight basis functions:

[p0277-b0015 | ordinary-paragraph | high] X;Pi, X2Pi, X3Pi, %1P2, %2P2, X3P2, %1P3, %X2Ps-

[p0277-b0016 | ordinary-paragraph | high] The space R, has the following attractive property.

[p0277-b0017 | lemma | high] Lemma 5.3. If the vector field ue R, satisfies curlu = 0 then

[p0277-b0018 | equation | low] u=grapp_ with peP,.

[p0277-b0019 | proof | high] Proof. First observe that each fe P, satisfies

[p0277-b0020 | equation | low] lf = grad f -x.

[p0277-b0021 | ordinary-paragraph | high] Now, we know that u = gradp with pe P,,,. Therefore, the term in gradp that

[p0277-b0022 | ordinary-paragraph | high] belongs to S, vanishes according to the definition (5.24). Hence p has no term of

[p0277-b0023 | ordinary-paragraph | high] degree / + 1. o

[p0277-b0024 | remark | high] Remark 5.3. The definition of R, can obviously be extended to an arbitrary

[p0277-b0025 | ordinary-paragraph | high] dimension N. Then the statement of Lemma 5.3 is also valid for all dimensions.

[p0277-b0026 | ordinary-paragraph | high] CO

[p0277-b0027 | definition | high] Definition 5.1. Let « be a tetrahedron in R* with edges denoted by e and faces

[p0277-b0028 | ordinary-paragraph | high] by f and let u be a function in W''‘(x)* for some s > 2. We define the three sets

[p0277-b0029 | ordinary-paragraph | high] of moments of u on k:

[p0277-b0030 | equation | low] M,(u) = ‘|( u:t)qgde YVqeP,_,(e) for all edges e of ct.

[p0277-b0031 | ordinary-paragraph | high] where t denotes the unit vector of e;

[p0277-b0032 | ordinary-paragraph | high] M,(u) = 1|( uxn)-qds VqeP2,(f) for all aces fof x}

[p0277-b0033 | ordinary-paragraph | high] i

[p0277-b0034 | equation | low] M,(u) = ‘|u -qdx vaer st

## PDF 278 / printed 264



[p0278-b0003 | ordinary-paragraph | high] more regularity than H'(x)> because M,(u) makes no sense when u is only in

[p0278-b0004 | ordinary-paragraph | high] H(i).

[p0278-b0005 | ordinary-paragraph | high] These definitions will enable us to construct conforming finite elements in

[p0278-b0006 | ordinary-paragraph | high] H (curl; Q) provided that on the one hand, the above set of moments is unisolvent

[p0278-b0007 | ordinary-paragraph | high] on R, and on the other hand, the moments M, and M, determine entirely the

[p0278-b0008 | ordinary-paragraph | high] tangential components of polynomials of R,. This is achieved in the next lemmas.

[p0278-b0009 | lemma | high] Lemma 5.4. The total number of moments in Definition 5.1 is equal to N,, the

[p0278-b0010 | ordinary-paragraph | high] dimension of R;:

[p0278-b0011 | equation | low] N, = (1/2)1(l + 2)@ + 3).

[p0278-b0012 | proof | high] Proof. In view of Definition 5.1, we have:

[p0278-b0013 | equation | low] card(M.(u)) = 6 dim(P,_, in R) = 61,

[p0278-b0014 | equation | low] card(M,(u)) = 8dim(P,_, in R?) = 4/(/ — 1),

[p0278-b0015 | equation | low] card(M,(u)) = 3 dim(P,_3 in R*) = (1/2)/(1 — 1)(/ — 2).

[p0278-b0016 | ordinary-paragraph | high] On summing these three quantities we obtain (1/2)/(/ + 2)(/ + 3) moments.

[p0278-b0017 | ordinary-paragraph | high] On the other hand, observe that the product of an arbitrary polynomial of P?

[p0278-b0018 | ordinary-paragraph | high] by x: p(x): x yields an arbitrary polynomial of P,,,. Hence the identity p(x)-x = 0

[p0278-b0019 | ordinary-paragraph | high] amounts to dim(P,,,) independent conditions. Therefore

[p0278-b0020 | equation | low] dim(R,) = 3 dim(P, in R*) — dim(F,,,)

[p0278-b0021 | equation | low] = (1/2) + 3) + 2)0 + 1) — (1/2) 4+ 3)(-+ 2)

[p0278-b0022 | ordinary-paragraph | high] = (1 2\ee 3) eek Oo

[p0278-b0023 | ordinary-paragraph | high] The equality in Lemma 5.4 means that the polynomials of R, are uniquely

[p0278-b0024 | ordinary-paragraph | high] determined by their three sets of moments if and only if the zero moments define

[p0278-b0025 | ordinary-paragraph | high] only the zero polynomial. But this unisolvence is not easily established on an

[p0278-b0026 | ordinary-paragraph | high] arbitrary tetrahedron x. Therefore, we shall first prove that the zero moments

[p0278-b0027 | ordinary-paragraph | high] are preserved by an affine transformation and subsequently work on the reference

[p0278-b0028 | ordinary-paragraph | high] tetrahedron kK whenever it is convenient.

[p0278-b0029 | ordinary-paragraph | high] As usual, we denote by F,. the affine invertible transformation from & onto x:

[p0278-b0030 | equation | low] x» = F(x) = Bex b,.

[p0278-b0031 | ordinary-paragraph | high] Scalar functions defined on « are transformed by a composition with F,:

[p0278-b0032 | ordinary-paragraph | high] (5.25) d6=¢0F, \¢ defined on x,

[p0278-b0033 | ordinary-paragraph | high] while vector functions defined on « are transformed like gradients:

[p0278-b0034 | ordinary-paragraph | high] (5.26) a= Bi(uoF.) Vudefined on kx.

[p0278-b0035 | ordinary-paragraph | high] Recall that the unit normal and unit tangent vectors are transformed respectively

[p0278-b0036 | ordinary-paragraph | high] by

## PDF 279 / printed 265



[p0279-b0003 | ordinary-paragraph | high] (5.28) toF, = (By t)/IlB. tl.

[p0279-b0004 | ordinary-paragraph | high] The main reason for adopting the transformation (5.26) is that it preserves the

[p0279-b0005 | ordinary-paragraph | high] curl in a certain sense. Indeed, let us introduce the matrices

[p0279-b0006 | ordinary-paragraph | high] (5.29) ‘ = (Ci)i, j = (0u,/0x; as u;/OX;);, js

[p0279-b0007 | equation | low] C= (Cij)i,j = (00,/0X; = 00; /0X;);, j-

[p0279-b0008 | ordinary-paragraph | high] Then by expanding the formula (5.26) we easily derive that the matrices C and

[p0279-b0009 | ordinary-paragraph | high] C are related by:

[p0279-b0010 | ordinary-paragraph | high] (5.30) COre=(B,*).C(B.*).

[p0279-b0011 | ordinary-paragraph | high] As a consequence, curlu and curl @ vanish always simultaneously.

[p0279-b0012 | ordinary-paragraph | high] Besides that, the transformation (5.26) preserves the space R).

[p0279-b0013 | lemma | high] Lemma 5.5. The space R, is invariant under the transformation (5.26).

[p0279-b0014 | proof | high] Proof. Clearly (5.26) preserves the space P; for arbitrary k; hence we need only

[p0279-b0015 | ordinary-paragraph | high] consider u in S,. Formula (5.26) reads:

[p0279-b0016 | equation | low] 4(%) = BTu(B,% + b,)

[p0279-b0017 | equation | low] = Beu(B,,%) + p(X)

[p0279-b0018 | ordinary-paragraph | high] where the degree of p is strictly less than / and B7 u(B,.x)e P>. Now,

[p0279-b0019 | equation | low] BTu(B,2)-% = u(B,2)-(B,2) = 0

[p0279-b0020 | ordinary-paragraph | high] since ue S,. Hence fie R, on Kk. Conversely, the same argument shows that if fe R,

[p0279-b0021 | ordinary-paragraph | high] on K then ue R, on k. Cc

[p0279-b0022 | lemma | high] Lemma 5.6. The three sets of moments of a function u given by Definition 5.1 vanish

[p0279-b0023 | ordinary-paragraph | high] on k iff the moments of & vanish on R.

[p0279-b0024 | proof | high] Proof. In view of (5.26) we have:

[p0279-b0025 | equation | low] |u -qdx = |det(B,)| |a -(B.')(qo F.) dx.

[p0279-b0026 | ordinary-paragraph | high] Hence ;

[p0279-b0027 | equation | low] |u -qdx =0 aera |a gai =O Ver (Kk):

[p0279-b0028 | ordinary-paragraph | high] Next, observe that every vector q of R?® satisfies

[p0279-b0029 | equation | low] ux n-g= —q X nu.

[p0279-b0030 | ordinary-paragraph | high] Furthermore, all tangent vectors q to the affine variety f with normal n (ie. q is

[p0279-b0031 | ordinary-paragraph | high] characterized by q-n = 0) are of the form q = p x n for arbitrary p of R’. Hence

## PDF 280 / printed 266



[p0280-b0002 | equation | low] M,(u) = =| u-qds=0 VqeP2,(k) suchthat q:-n=0.

[p0280-b0003 | ordinary-paragraph | high] di

[p0280-b0004 | ordinary-paragraph | high] Therefore, applying (5.26) and (5.27) we have:

[p0280-b0005 | equation | low] M,(u) = (oy |0 B3)(qoF,)d8=0 VqeP?,(k)

[p0280-b0006 | ordinary-paragraph | high] such that (Ba }(qio f)-n.— 0

[p0280-b0007 | equation | low] <> M;() = {0}.

[p0280-b0008 | equation | low] Likewise, owing to (5.28) we readily derive that

[p0280-b0009 | ordinary-paragraph | high] M.,(u) = {0>} M,( @) = {0}. fs

[p0280-b0010 | ordinary-paragraph | high] Now we turn to the unisolvence. Let us start with a boundary result.

[p0280-b0011 | lemma | high] Lemma 5.7. A vector u of R, has all its moments zero on a given face f of k iff the

[p0280-b0012 | ordinary-paragraph | high] tangential components of u vanish on f.

[p0280-b0013 | proof | high] Proof. As all conditions involved are preserved by an affine transformation, we

[p0280-b0014 | ordinary-paragraph | high] can assume that the face f lies on the plane x, = 0. Then the tangential compo-

[p0280-b0015 | ordinary-paragraph | high] nents u, of u on f reduce to its first two components:

[p0280-b0016 | equation | low] Ur(X1,X2) = (Uy (X1X2,, 9 ), ee

[p0280-b0017 | ordinary-paragraph | high] Moreover, the conditions M,(u)= {0} and M,(u) = {0} are respectively equiva-

[p0280-b0018 | ordinary-paragraph | high] lent to:

[p0280-b0019 | ordinary-paragraph | high] (5.31) |u r'qdx,;dx,=0 VqeP-,(f),

[p0280-b0020 | ordinary-paragraph | high] i

[p0280-b0021 | ordinary-paragraph | high] (5:32) |u ;;tqde=0 VqeP_,(e).

[p0280-b0022 | ordinary-paragraph | high] Hence Green’s formula (1.2.22) in two dimensions gives:

[p0280-b0023 | equation | low] |c urlu;gdx,dx,=0 VqeP_,(/),

[p0280-b0024 | ordinary-paragraph | high] af

[p0280-b0025 | ordinary-paragraph | high] Le: curlu; =0 onf.

[p0280-b0026 | ordinary-paragraph | high] Now, it is easy to verify that u; belongs to the two-dimensional analogue of

[p0280-b0027 | ordinary-paragraph | high] R,. Therefore it follows from Lemma 5.3 and its Remark that

[p0280-b0028 | equation | low] u; =gradp with pe P(/f).

[p0280-b0029 | ordinary-paragraph | high] As a consequence, (5.32) implies that p is constant on the boundary Of of f; thus

[p0280-b0030 | ordinary-paragraph | high] we can take

[p0280-b0031 | equation | low] p=0 ond,

[p0280-b0032 | ordinary-paragraph | high] es p=A,A,A3r_ withreP,_3(f),

## PDF 281 / printed 267



[p0281-b0004 | ordinary-paragraph | medium] yields that r = 0.

[p0281-b0005 | ordinary-paragraph | low] 口

[p0281-b0006 | lemma | medium] Lemma 5.8. If the moments of the vector u of R are all zero on k then u is

[p0281-b0007 | ordinary-paragraph | medium] identically zero.

[p0281-b0008 | proof | medium] Proof. On the one hand, Lemma 5.7 shows that

[p0281-b0009 | equation | low] (5.33)

[p0281-b0010 | equation | low] u x n = 0 on Ok;

[p0281-b0011 | ordinary-paragraph | medium] on the other hand, we have

[p0281-b0012 | equation | low] (5.34)

[p0281-b0013 | ordinary-paragraph | medium] Vqe Pi-3(k).

[p0281-b0014 | equation | low] u·qdx =0 

[p0281-b0015 | ordinary-paragraph | medium] Again, since these conditions are preserved by an affine transformation, we can

[p0281-b0016 | ordinary-paragraph | medium] switch to the reference element. Then Green's formula gives:

[p0281-b0017 | equation | low] curlu·qdx = O  Vq∈ P²-2(k)

[p0281-b0018 | ordinary-paragraph | low] JK

[p0281-b0019 | ordinary-paragraph | medium] and it stems from (5.33) that

[p0281-b0020 | equation | low] curlá·n = O on dk.

[p0281-b0021 | ordinary-paragraph | medium] Now, taking advantage of the geometry of k, it is easy to prove that these

[p0281-b0022 | ordinary-paragraph | medium] conditions (together with the fact that curl áe P?- (k)) imply

[p0281-b0023 | equation | low] curlu = O in K.

[p0281-b0024 | ordinary-paragraph | medium] Hence it follows from (5.30) that

[p0281-b0025 | equation | low] curlu = O in k.

[p0281-b0026 | ordinary-paragraph | medium] Therefore, owing to Lemma 5.3,

[p0281-b0027 | equation | low] u = grad p

[p0281-b0028 | ordinary-paragraph | medium] with pe P; and plak = 0 because u x n = 0 on Ok. As a consequence, p = Λ,^2^4r

[p0281-b0029 | ordinary-paragraph | medium] with re P-4(k) and (5.34) implies that r = 0.

[p0281-b0030 | ordinary-paragraph | medium] 口

[p0281-b0031 | remark | medium] Remark 5.5. By applying the arguments of Lemmas 5.7 and 5.8 it can also be

[p0281-b0032 | ordinary-paragraph | medium] proved that every vector u of P3 with zero moments in k satisfies

[p0281-b0033 | equation | low] curl u = 0.

[p0281-b0034 | ordinary-paragraph | medium] First, observe that Lemma 5.7 shows that

[p0281-b0035 | equation | low] curl u·n = 0 on the particular face x3 = 0.

[p0281-b0036 | ordinary-paragraph | medium] But since this property is preserved by an affine transformation, it holds on each

[p0281-b0037 | ordinary-paragraph | medium] face of k. Then the argument of Lemma 5.8 yields

[p0281-b0038 | equation | low] curlu = O in k.

## PDF 282 / printed 268



[p0282-b0004 | ordinary-paragraph | medium] beginning of this section.

[p0282-b0005 | theorem | medium] Theorem 5.3. A vector field u of R, is entirely determined in a tetrahedron k by its

[p0282-b0006 | ordinary-paragraph | medium] three sets of moments: Me(u), Ms(u), Mx(u). Moreover the tangential components

[p0282-b0007 | ordinary-paragraph | medium] of u on a given face f of r depend only upon the moments M,(u) and Me(u) defined

[p0282-b0008 | ordinary-paragraph | medium] on that face.

[p0282-b0009 | ordinary-paragraph | medium] This theorem induces a natural interpolation operator in K.

[p0282-b0010 | ordinary-paragraph | low]   sy r ' go pd u a si   sh 7 < ss

[p0282-b0011 | ordinary-paragraph | medium] moments as u on k.

[p0282-b0012 | ordinary-paragraph | medium] In other words, rxu is determined by:

[p0282-b0013 | equation | low] M(rxu - u) = {0},  Ms(ru - u) = {0},  Me(ru - u) = {0}.

[p0282-b0014 | ordinary-paragraph | medium] Clearly, it follows from the invariance Lemmas 5.5 and 5.6 that

[p0282-b0015 | equation | low] (5.35)

[p0282-b0016 | equation | low] ru=ru,

[p0282-b0017 | ordinary-paragraph | medium] i.e.

[p0282-b0018 | equation | low] B[(ru)o F] = r[B(uo F)].

[p0282-b0019 | remark | medium] Remark 5.6. When ue W1,s(x)3 satisfies curl u = 0, the argument of Lemma 5.8

[p0282-b0020 | ordinary-paragraph | medium] shows that curl(r,u) = O in K.

[p0282-b0021 | ordinary-paragraph | medium] Likewise, when ue P? , Remark 5.5 establishes that

[p0282-b0022 | equation | low] curl(u -- rxu) = 0 in k.

[p0282-b0023 | ordinary-paragraph | medium] Now we are in a position to define the finite element spaces M, and Φ,. As a

[p0282-b0024 | ordinary-paragraph | medium] matter of convenience, we assume that Q is a bounded polyhcuiron. Let T, be a

[p0282-b0025 | ordinary-paragraph | medium] triangulation of Ω consisting of polyhedra k with diameters bounded by h. For

[p0282-b0026 | ordinary-paragraph | medium] each integer I ≥ 1, we set:

[p0282-b0027 | equation | low] (5.36a)

[p0282-b0028 | equation | low] Mh, = {μ,e H(curl; Q); μnlk ∈ R, VK∈ h},

[p0282-b0029 | equation | low] (5.36b)

[p0282-b0030 | equation | low] Dh = M, N Ho(curl; Ω)

[p0282-b0031 | ordinary-paragraph | medium] and we define the interpolation operator r, on M, by:

[p0282-b0032 | equation | low] (5.37)

[p0282-b0033 | equation | low] rhulk =reu onk  VkeTh

[p0282-b0034 | ordinary-paragraph | low]  ( ds) ' r ss 1n ax u 7 < s as  )siM n  

[p0282-b0035 | ordinary-paragraph | medium] a conforming approximation of H(curl; Q) (resp. Ho(curl; Ω)).

[p0282-b0036 | lemma | medium] Lemma 5.9. If ue W1.s(Q)3, then r,ue M,. Similarly, when ue W1,s(Q) with

[p0282-b0037 | ordinary-paragraph | medium] u x nlr = O then rhue Φh.

[p0282-b0038 | ordinary-paragraph | medium] We skip the proof as it is a straightforward consequence of Lemma 5.7.

## PDF 283 / printed 269



[p0283-b0003 | ordinary-paragraph | high] the triangulation 7, is regular as h tends to zero (cf. Definition A.2):

[p0283-b0004 | equation | low] hy/Pe =O <0 WeEF,, o@>O independent of h.

[p0283-b0005 | theorem | high] Theorem 5.4. Let 7, be a regular family of triangulations of Q and let M,, and r,

[p0283-b0006 | ordinary-paragraph | high] be defined by (5.36) and (5.37) for some integer | > 1. We have the upper bound for

[p0283-b0007 | ordinary-paragraph | high] all ue H'*1(Q)?:

[p0283-b0008 | ordinary-paragraph | high] (5.38) ju — T,U ||( curl) < Cyh' {Jule ae |Wlh41,Q}-

[p0283-b0009 | ordinary-paragraph | high] Moreover, the operator r, satisfies the following stability estimate:

[p0283-b0010 | ordinary-paragraph | high] (5.39) ju — 7,0 lo, + Alleurl(u — 7,0) \|o,9 < Cyhlul,0

[p0283-b0011 | ordinary-paragraph | high] for allue W**(Q)? with s > 2, where the positive constants C, and C, are indepen-

[p0283-b0012 | ordinary-paragraph | high] dent of h and u.

[p0283-b0013 | proof | high] Proof. Let us first prove (5.38). By virtue of (5.26) we have:

[p0283-b0014 | equation | low] Ju — r,U lo. < |det(B,)||"B ?. * || ||@ — reAllo,x-

[p0283-b0015 | ordinary-paragraph | high] But since the operator rz preserves the polynomials of P?,, Corollary A.1

[p0283-b0016 | ordinary-paragraph | high] implies that:

[p0283-b0017 | ordinary-paragraph | high] : [tle wail2 ,

[p0283-b0018 | equation | low] |@ — reAllo.g < Cy u A :

[p0283-b0019 | equation | low] lal, e+(1@|,, iff =1.

[p0283-b0020 | ordinary-paragraph | high] Next, combining formulas (A.7) and (5.26) we derive:

[p0283-b0021 | ordinary-paragraph | high] (5.40) [lk < Cp ||B y ||| det(B,7) Ju|le. ..

[p0283-b0022 | ordinary-paragraph | high] Therefore, these three inequalities yield:

[p0283-b0023 | equation | low] Ju — rUlloe < Cz] Be*| | By ll lal. when > 2,

[p0283-b0024 | ordinary-paragraph | high] (5.41) 5

[p0283-b0025 | ordinary-paragraph | high] lu —rUllone < C3 Bei WN Bell? (uli + Bell lule,.) when! = 1.

[p0283-b0026 | ordinary-paragraph | high] Next, let us examine curl(u — r,,u). According to (5.30), we have:

[p0283-b0027 | equation | low] l|curl(u — 7,u)|lo,< < Cgldet(B,)|"* ||B y * ||* ||eurl(@ — re) Io, ¢.

[p0283-b0028 | ordinary-paragraph | high] As mentioned in Remark 5.6, the linear mapping 4 > curl(@ — r,fi) vanishes on

[p0283-b0029 | ordinary-paragraph | high] the space P,. Therefore, a simple application of Theorem A.1 yields:

[p0283-b0030 | equation | low] |curl(@ — rg) \lo,.¢ < Cs Al +; ¢-

[p0283-b0031 | ordinary-paragraph | high] Hence

[p0283-b0032 | ordinary-paragraph | high] (5.42) l|curl(u — 7,0) lo < Coll Be 7 Bell 7 alistx :

[p0283-b0033 | ordinary-paragraph | high] Finally (5.38) stems from (5.41) and (5.42) together with (A.2) and the regularity

[p0283-b0034 | ordinary-paragraph | high] Or7,.

[p0283-b0035 | ordinary-paragraph | high] The proof of the stability estimate (5.39) is a trifle more intricate. Taking into

[p0283-b0036 | ordinary-paragraph | high] account the facts that r; preserves the constant polynomials and belongs to

## PDF 284 / printed 270



[p0284-b0003 | equation | low] |@ — reAlloe < CrlO5h, 2 -

[p0284-b0004 | ordinary-paragraph | high] Hence

[p0284-b0005 | equation | low] lu — rullo.n < Cg(meas"(7-x9) |)]B et | |B ell? las:

[p0284-b0006 | ordinary-paragraph | high] Then HO6lder’s inequality and the regularity of 7, imply that

[p0284-b0007 | equation | low] lu — r,U|lo,0 < Coh(meas(Q")|)u|?, ~,0 -

[p0284-b0008 | ordinary-paragraph | high] Likewise, we have

[p0284-b0009 | equation | low] ||curl(@ — ref) Ilo,¢ < Crolfily,s.e-

[p0284-b0010 | ordinary-paragraph | high] Therefore, we infer from the above inequalities that:

[p0284-b0011 | ordinary-paragraph | high] ||curl(u — 7,0) |lo,9 < C,1(meas(Q"|)u)|," ?0 . O

[p0284-b0012 | subsection | high] 5.4. Error Analysis for Finite Elements of Degree /

[p0284-b0013 | ordinary-paragraph | high] The spaces M, and ®, have already been defined in (5.36) and it remains to define

[p0284-b0014 | ordinary-paragraph | high] the space 9,. Here, we simply take the standard finite element space:

[p0284-b0015 | ordinary-paragraph | high] (5.43) 0, = {q,€ 6° (Q); dnleEP, VRE; Galr= O}-

[p0284-b0016 | ordinary-paragraph | high] Recall that the functions of ®,, satisfy

[p0284-b0017 | ordinary-paragraph | high] (5.12) (,,gradq,)=0 Vq,eO,.

[p0284-b0018 | ordinary-paragraph | high] The next three results check the hypotheses (5.14) and (5.17). They will lead

[p0284-b0019 | ordinary-paragraph | high] in particular to an interesting decomposition of our discrete finite element spaces.

[p0284-b0020 | ordinary-paragraph | high] Before proving that the space @,, satisfies (5.14), let us show the following

[p0284-b0021 | ordinary-paragraph | high] preliminary result.

[p0284-b0022 | lemma | high] Lemma 5.10. Let u be a function of the form:

[p0284-b0023 | equation | low] u= gradp_ with pe H5(Q)

[p0284-b0024 | ordinary-paragraph | high] and assume that wis such that r,u is well defined. Then there exists p,,in ©, such that

[p0284-b0025 | equation | low] r,U = grad p,.

[p0284-b0026 | proof | high] Proof. As curlu = 0, Remark 5.6 implies that

[p0284-b0027 | equation | low] curly,u = 0 in each xk.

[p0284-b0028 | ordinary-paragraph | high] But since p is constant on J’, we also have u x n= 0 on J” Therefore, it follows

[p0284-b0029 | ordinary-paragraph | high] from Lemma 5.9 that r,u€ Ho(curl; Q); this means that

[p0284-b0030 | equation | low] curlr,u=0 nQ, ruxn=0 onl,

[p0284-b0031 | ordinary-paragraph | high] Hence

## PDF 285 / printed 271



[p0285-b0003 | ordinary-paragraph | high] On the other hand, Lemma 5.3 implies that

[p0285-b0004 | ordinary-paragraph | high] q|.€P, for each kx.

[p0285-b0005 | ordinary-paragraph | high] Therefore qe @,,. |

[p0285-b0006 | remark | high] Remark 5.7. Lemma 5.10 shows that for each function @, in ®, that satisfies

[p0285-b0007 | ordinary-paragraph | high] curl , = 0 in Q there exists a (unique) element p, of O, such that

[p0285-b0008 | equation | low] ), = grad p,.

[p0285-b0009 | ordinary-paragraph | high] Thus {grad p,; p,€9,} = {o,€®,; curl, = 0}.

[p0285-b0010 | ordinary-paragraph | high] It follows from this last remark that @,, satisfies (5.14). But if we want to

[p0285-b0011 | ordinary-paragraph | high] check that (5.14) holds uniformly, we shall require below a uniformly regular

[p0285-b0012 | ordinary-paragraph | high] triangulation, i.e. a regular triangulation 7%, that also satisfies for some t > 0

[p0285-b0013 | ordinary-paragraph | high] independent of h:

[p0285-b0014 | equation | low] Trae = Op, VCE 7,

[p0285-b0015 | proposition | high] Proposition 5.1. Let Q be an open, bounded and convex region of R? with a

[p0285-b0016 | ordinary-paragraph | high] polyhedral boundary I. If %,,is a uniformly regular triangulation of Q, there exists

[p0285-b0017 | ordinary-paragraph | high] a constant C*, independent of h, such that:

[p0285-b0018 | ordinary-paragraph | high] (5.14) Ir Hoo < C*lleurld,llo,0 VO, Pro-

[p0285-b0019 | proof | high] Proof. The idea is to write , as the sum of a gradient and a divergence-free

[p0285-b0020 | ordinary-paragraph | high] function w, smooth enough to satisfy an inequality similar to (5.14). First, let

[p0285-b0021 | ordinary-paragraph | high] p€ H4(Q) be the unique solution of the problem:

[p0285-b0022 | equation | low] (grad p, grad q) = (,,gradq) —V qe Hg(Q).

[p0285-b0023 | ordinary-paragraph | high] Clearly the difference

[p0285-b0024 | equation | low] w = , — grad p

[p0285-b0025 | ordinary-paragraph | high] satisfies curlw = curld,, divw=0, wxnjp=0.

[p0285-b0026 | ordinary-paragraph | high] In addition, curl, belongs to L?(Q)° for all y. Therefore, since 2 is convex, it

[p0285-b0027 | ordinary-paragraph | high] follows from Remark I.3.14 that there exists a real s > 2 such that:

[p0285-b0028 | ordinary-paragraph | high] we W!5(Q)3

[p0285-b0029 | ordinary-paragraph | high] and

[p0285-b0030 | ordinary-paragraph | high] (5.44) IWllia.e <C,(@)|leurlwilo.,0 foralla with2<a<s.

[p0285-b0031 | ordinary-paragraph | high] Hence, the interpolate r,w is well defined. As @, belongs to ®,, this in turn

[p0285-b0032 | ordinary-paragraph | high] implies that r,(grad p) is also well defined and owing to Lemma 5.10, there exists

[p0285-b0033 | ordinary-paragraph | high] Pp, in O, such that

[p0285-b0034 | equation | low] r,(grad p) = grad p,.

## PDF 286 / printed 272



[p0286-b0003 | equation | low] , — r,W af grad Ph-

[p0286-b0004 | ordinary-paragraph | high] Then, applying (5.12) with q, = p, we easily derive

[p0286-b0005 | equation | low] Pr llo,a < ItrWllo,a-

[p0286-b0006 | ordinary-paragraph | high] Thus, (5.14) will be established if we show that

[p0286-b0007 | ordinary-paragraph | high] (5.45) TrW llo,a < C* |leurl >, \Io,0-

[p0286-b0008 | equation | low] Now (5.39) and (5.44) yield:

[p0286-b0009 | equation | low] |W —1,W]lo,@ < C,h|\ curl, |lo,s,a-

[p0286-b0010 | ordinary-paragraph | high] But since 7, is uniformly regular and @, is a polynomial on each k, we easily

[p0286-b0011 | ordinary-paragraph | high] obtain from (5.30) and (A.34):

[p0286-b0012 | equation | low] lleurl @,Ilo,s,@ < CshPO*? ) ||c url,Il o,0 -

[p0286-b0013 | ordinary-paragraph | high] Therefore

[p0286-b0014 | equation | low] Iw — 7,Wllo,@ < Cyh*|| cur>l, |lo,0

[p0286-b0015 | ordinary-paragraph | high] with a non negative exponent « as long as 2 < s < 6. This proves (5.45). O

[p0286-b0016 | corollary | high] Corollary 5.1. Let Q be an open, bounded polyhedron of R*. For each function w,,

[p0286-b0017 | ordinary-paragraph | high] of ®, there exists a unique function v, in ®,,. and p,, in O, such that:

[p0286-b0018 | equation | low] w, = Vv, + grad p,,

[p0286-b0019 | equation | low] (5.46)

[p0286-b0020 | ordinary-paragraph | high] IPali,a@S ||W allo.a-

[p0286-b0021 | ordinary-paragraph | high] Moreover, under the assumptions of Proposition 5.1, v, is bounded as follows:

[p0286-b0022 | ordinary-paragraph | high] (5.47) [Vllin ve urt;;2)< ( 1 + C*?)*||c”u r l w|yl o, 0.

[p0286-b0023 | proof | high] Proof. Let us take for p, the unique solution in @, of

[p0286-b0024 | equation | low] (grad p,, grad q,,) = (w,,gradq,) Vq,€9,.

[p0286-b0025 | ordinary-paragraph | high] Then the difference

[p0286-b0026 | equation | low] Vv, = W, — grad p,

[p0286-b0027 | ordinary-paragraph | high] belongs to ®,9 and (5.47) follows immediately from Proposition 5.1. fia

[p0286-b0028 | ordinary-paragraph | high] Observe that the first part of this corollary establishes (5.17).

[p0286-b0029 | ordinary-paragraph | high] From Lemmas 5.1 and 5.2, Theorems 5.1, 5.2 and 5.4, Proposition 5.1 and

[p0286-b0030 | corollary | high] Corollary 5.1, we derive the major result of this section.

[p0286-b0031 | theorem | high] Theorem 5.5. Let Q be a bounded polyhedron in R*. Then Problems (5.15) and

[p0286-b0032 | ordinary-paragraph | high] (5.16) associated with the choice of finite element spaces (5.36) and (5.43) are

[p0286-b0033 | ordinary-paragraph | high] equivalent and have a unique solution u, = (curl y,,, ,).

## PDF 287 / printed 273



[p0287-b0004 | equation | low] we H’**(Q)3, n= — Awe H'*1(Q)3

[p0287-b0005 | ordinary-paragraph | high] for some integer | > 1. Then, if Y, is a uniformly regular family of triangulations

[p0287-b0006 | ordinary-paragraph | high] of Q, u,, satisfies the error estimates:

[p0287-b0007 | equation | low] { | — @llo,a < Cy(|W Alir .o + Ao llies.a),

[p0287-b0008 | equation | low] (5.48

[p0287-b0009 | equation | low] lcurl(w — w,)llo,o < Co f(b? + h)|wWhias.o + h'llellieso}

[p0287-b0010 | ordinary-paragraph | high] with positive constants C, and C, independent of h, o and w.

[p0287-b0011 | remark | high] Remark 5.8. Like in the two-dimensional case, we observe a loss of one power of

[p0287-b0012 | ordinary-paragraph | high] h arising from the term (cf. Lemma 5.2):

[p0287-b0013 | equation | low] af |(curl(y — ,), curl p,,)|

[p0287-b0014 | equation | low] (5.49)

[p0287-b0015 | ordinary-paragraph | high] On€ Pro Mhe Mp, | Hallo.

[p0287-b0016 | ordinary-paragraph | high] If it were known that the projection B,w (for y in ,):

[p0287-b0017 | equation | low] Pow E Pro (curl(P, y — wy), curld,) =90 Vb, € Pro

[p0287-b0018 | ordinary-paragraph | high] satisfied the L?-estimate:

[p0287-b0019 | ordinary-paragraph | high] (5.50) ||Bw — Wllo.p.@ + Alleurl(B,y — W)llo,p,.0 < Ch'** | wlls+1,p,0

[p0287-b0020 | ordinary-paragraph | high] for all pe[2, ©] and se[1,/], then the argument of Section 3.1 could be applied

[p0287-b0021 | ordinary-paragraph | high] to derive a sharper estimate than (5.48) and regain part of the missing power of

[p0287-b0022 | ordinary-paragraph | high] h. In particular this would enable us to obtain an acceptable rate of convergence

[p0287-b0023 | ordinary-paragraph | high] when using first degree elements, which Theorem 5.5 fails to show.

[p0287-b0024 | ordinary-paragraph | high] Although (5.50) is still a conjecture, it does not sound unreasonable and it is

[p0287-b0025 | ordinary-paragraph | high] hoped that this problem will be solved in a near future.

[p0287-b0026 | subsection | high] 5.5. Discontinuous Approximation of the Pressure

[p0287-b0027 | ordinary-paragraph | high] This section briefly describes and analyzes a finite element method that solves

[p0287-b0028 | ordinary-paragraph | high] for the pressure term underlying Problems (5.15) and (5.16). Since the situation

[p0287-b0029 | ordinary-paragraph | high] is fairly similar to that in Section 4.4 we shall state nearly all results without

[p0287-b0030 | proof | high] proof. The reader will easily fill in the blanks.

[p0287-b0031 | ordinary-paragraph | high] It is clear that here we must construct subspaces D, of H(div; 2) such that,

[p0287-b0032 | ordinary-paragraph | high] on the one hand, curl p, belongs to D, for p,, in M, and on the other hand, div v,

[p0287-b0033 | ordinary-paragraph | high] belongs to the discrete pressure space for v, in D,. The following definition

[p0287-b0034 | ordinary-paragraph | high] generalizes the polynomial space D defined by (4.61a).

[p0287-b0035 | definition | high] Definition 5.3. 1°) For each integer / > 1, let

[p0287-b0036 | equation | low] D, = P3., © {p(x)x; pe Bs}.

## PDF 288 / printed 274



[p0288-b0004 | equation | low] nw) = |u :ngds VqeP_,(f),

[p0288-b0005 | ordinary-paragraph | high] if

[p0288-b0006 | equation | low] N,(u) = |u -qdx VWqeP?,(k).

[p0288-b0007 | ordinary-paragraph | high] We can immediately check that for uin D,, u-n belongs to P,_, on each face f of

[p0288-b0008 | ordinary-paragraph | high] k. In addition, it easy to see that when u is a divergence-free vector field of D,

[p0288-b0009 | ordinary-paragraph | high] then u belongs to P?.,.

[p0288-b0010 | ordinary-paragraph | high] As usual, let K denote the unit reference tetrahedron. Instead of (5.26), let us

[p0288-b0011 | ordinary-paragraph | high] transform vector functions defined on x by the contravariant transformation:

[p0288-b0012 | ordinary-paragraph | high] (551) a= B.'(uoF,) Vudefined on kx.

[p0288-b0013 | ordinary-paragraph | high] It coincides with the contravariant transformation (4.63), up to the multiplicative

[p0288-b0014 | ordinary-paragraph | high] factor J, which is constant here:

[p0288-b0015 | equation | low] Jp = ldet(B.))

[p0288-b0016 | ordinary-paragraph | high] As a consequence (5.51) preserves entirely the divergence:

[p0288-b0017 | ordinary-paragraph | high] (5:52) (divu)o F, = diva.

[p0288-b0018 | ordinary-paragraph | high] In addition, we have the analogue of Lemmas 5.5, 5.6 and Theorem 5.3.

[p0288-b0019 | proposition | high] Proposition 5.2. 1°) The space D, is invariant under the transformation (5.51) and

[p0288-b0020 | ordinary-paragraph | high] the moments of u given by Definition 5.3 vanish on k iff the same moments of 0

[p0288-b0021 | ordinary-paragraph | high] vanish on kK.

[p0288-b0022 | ordinary-paragraph | high] 2°) A vector field u of D, is entirely determined in a tetrahedron x by its two

[p0288-b0023 | ordinary-paragraph | high] sets of moments: N,(u), N,.(u). Moreover, the normal component of uon a given face

[p0288-b0024 | ordinary-paragraph | high] f of « depends only upon the moments N,(u) defined on that face.

[p0288-b0025 | definition | high] Definition 5.4. Let ue H'(«)°, where x is an arbitrary tetrahedron. Its interpolant

[p0288-b0026 | ordinary-paragraph | high] @,U is the unique polynomial of D, that has the same moments as u on x.

[p0288-b0027 | ordinary-paragraph | high] Thus @,.u is determined by the conditions:

[p0288-b0028 | equation | low] N,(u — @,u) = {0}, N,(u— au) = {0}.

[p0288-b0029 | ordinary-paragraph | high] Again, the invariance in Proposition 5.2 implies that

[p0288-b0030 | equation | low] O,U = Wel.

[p0288-b0031 | ordinary-paragraph | high] Moreover, we observe that

[p0288-b0032 | equation | low] divu—@,u)=0 onk VueP>

[p0288-b0033 | ordinary-paragraph | high] and that divu = 0 on xk implies that div(@,u) = 0.

## PDF 289 / printed 275



[p0289-b0004 | equation | low] D, = {u,€ (div; Q); u,|,¢D, VeeFZ, } ,

[p0289-b0005 | ordinary-paragraph | high] (553) Do, = D,N Ho (div; 2),

[p0289-b0006 | equation | low] Q1, = {PrELo(Q); Pale Ra Vee F;},

[p0289-b0007 | ordinary-paragraph | high] together with the interpolation operator @,:

[p0289-b0008 | equation | low] O,u|,=@,u onk VKEeY,,

[p0289-b0009 | ordinary-paragraph | high] and for all ue H'(Q)°. Clearly, div u, belongs to Q, for all u, in Do, and curl p,

[p0289-b0010 | ordinary-paragraph | high] belongs to Do, for all p, in ®,. Furthermore, we have the analogue of Lemma 5.9:

[p0289-b0011 | ordinary-paragraph | high] uc H'(Q)? implies w,ueD,,

[p0289-b0012 | equation | low] ue H'(Q)? withu:n=0 implies w,ueDo,.

[p0289-b0013 | ordinary-paragraph | high] The following proposition states the approximation properties of D,.

[p0289-b0014 | proposition | high] Proposition 5.3. Let 7, be a regular family of triangulations of Q and let D, be

[p0289-b0015 | ordinary-paragraph | high] defined by (5.53) for an integer | > 1. We have the estimates:

[p0289-b0016 | equation | low] Ju — @,Ullo.a<Cyh'lul.g Yue H'(Q)?,

[p0289-b0017 | ordinary-paragraph | high] (5.54) '

[p0289-b0018 | equation | low] diva — @,0)|lo,9 < Coh'|Uliq VuH'e (Q )°.

[p0289-b0019 | ordinary-paragraph | high] The next lemma establishes the desired relationship between the spaces D,

[p0289-b0020 | ordinary-paragraph | high] and M,,.

[p0289-b0021 | lemma | high] Lemma 5.11. Let Q be an open, bounded polyhedron in R? and let T;,0 <i< p,

[p0289-b0022 | ordinary-paragraph | high] denote the connected components of its boundary. A function u, of D, (resp. Don)

[p0289-b0023 | ordinary-paragraph | high] satisfies:

[p0289-b0024 | equation | low] divu,=0 inQ, [ands =o for Dit ep

[p0289-b0025 | ordinary-paragraph | high] I,

[p0289-b0026 | ordinary-paragraph | high] iff there exists a function , in M, (resp. ®,) such that:

[p0289-b0027 | equation | low] U, — curl ,.

[p0289-b0028 | proof | high] Proof. We already know that curl #, belongs to D, (resp. Do,,) whenever o,, belongs

[p0289-b0029 | ordinary-paragraph | high] to M, (resp. ®,).

[p0289-b0030 | ordinary-paragraph | high] Conversely, Theorem I.3.4 asserts that there exists @ € H'(2)° such that

[p0289-b0031 | equation | low] u, = curl®.

[p0289-b0032 | ordinary-paragraph | high] Furthermore, the fact that u,, belongs to H*(Q)°* for alla with0 < a < 1/2 implies

[p0289-b0033 | ordinary-paragraph | high] that @ belongs to H!*7(Q)? (cf. Remark 1.3.12). Thus, the interpolate of 6, 7, is

[p0289-b0034 | ordinary-paragraph | high] well defined. Let us prove that:

## PDF 290 / printed 276



[p0290-b0003 | ordinary-paragraph | high] Le; curl(d — 7,60) =90 inQ.

[p0290-b0004 | ordinary-paragraph | high] On the one hand, observe that curl(@ — r,)€| P?.,,(« ). On the other hand,

[p0290-b0005 | ordinary-paragraph | high] we have

[p0290-b0006 | equation | low] |c url(d — r,6):qdx =0 VqeP?3(k),

[p0290-b0007 | equation | low] curl(@ — r,o)-n =O oneach face f of k.

[p0290-b0008 | ordinary-paragraph | high] Hence like in Lemma 5.8, we deduce:

[p0290-b0009 | equation | low] curl(o — r,@) =0 ineachx of J,

[p0290-b0010 | ordinary-paragraph | high] and since @ — r,¢ belongs to H(curl; Q), its curl vanishes on the whole of Q.

[p0290-b0011 | ordinary-paragraph | high] It remains to establish that when u,,-n vanishes on J’ then @, may be chosen

[p0290-b0012 | ordinary-paragraph | high] such that @, x n = 0 on J. The proof follows the lines of Theorem I.3.6. We take

[p0290-b0013 | ordinary-paragraph | high] an open ball ( containing Q; then, it is easy to construct a function q in H?(@)

[p0290-b0014 | ordinary-paragraph | high] such that

[p0290-b0015 | equation | low] gradg xn=@Oxn onl.

[p0290-b0016 | ordinary-paragraph | high] Note that this requires no regularity on Q since grad q need not be divergence-

[p0290-b0017 | ordinary-paragraph | high] free. As q belongs to H*(Q), r, grad q is well defined and therefore r,(@ — grad q)

[p0290-b0018 | ordinary-paragraph | high] is the desired potential vector of u, in &,. O

[p0290-b0019 | remark | high] Remark 5.9. According to Corollary 5.1, for each divergence-free vector field u,

[p0290-b0020 | ordinary-paragraph | high] in Do, there exists a unique vector potential , in ®,, such that:

[p0290-b0021 | equation | low] u, = curl @,.

[p0290-b0022 | ordinary-paragraph | high] In addition, under the hypotheses of Proposition 5.1, we have:

[p0290-b0023 | equation | low] Ir lln curt;2) < C|UyI| Io ,

[p0290-b0024 | ordinary-paragraph | high] With this lemma and the statement of Problem (5.16), we can formulate the

[p0290-b0025 | ordinary-paragraph | high] corresponding problem in u,, @,, Dp:

[p0290-b0026 | ordinary-paragraph | high] Find a pair (u,,),) in Do, x M,, and a function p, in Q,, such that:

[p0290-b0027 | equation | low] v(curl ,, V,,) — (Pp), div v,) = (f,v,) VV, Don;

[p0290-b0028 | ordinary-paragraph | high] (5.55) (u,, curl p,) = (@,,6,) Ve,eM,,

[p0290-b0029 | equation | low] divu, =0 in Q.

[p0290-b0030 | ordinary-paragraph | high] The existence and uniqueness of p, is a consequence of the following lemma which

[p0290-b0031 | ordinary-paragraph | high] establishes the inf-sup condition relative to the space Do, x M, and Q,. Then

[p0290-b0032 | lemma | high] Lemma 5.11 implies the equivalence between this problem and (5.15) or (5.16).

[p0290-b0033 | ordinary-paragraph | high] Therefore when Q is a bounded polyhedron, Problem (5.55) has a unique solution

[p0290-b0034 | ordinary-paragraph | high] (U,,, ,, Dn)-

## PDF 291 / printed 277



[p0291-b0005 | equation | low] divvh = Ph in Ω,

[p0291-b0006 | equation | low] (Oh,Hn) = (Vh, curl μh) AμhE Mh.

[p0291-b0007 | ordinary-paragraph | medium] In addition, when J, is a regular family of triangulations of Q, we have:

[p0291-b0008 | equation | low] (5.56)

[p0291-b0009 | equation | low] 110, llo,2 + IIvn ll H(div; 2) ≤ C llPn llo,Ωs

[p0291-b0010 | ordinary-paragraph | medium] where the positive constant C is independent of h and pn.

[p0291-b0011 | ordinary-paragraph | medium] The above lemmas lead to the expected estimate for the error p - Ph.

[p0291-b0012 | theorem | medium] Theorem 5.6. Let Q be a bounded polyhedron in R3. Then Problem (5.55) has a

[p0291-b0013 | ordinary-paragraph | medium] unique solution (un,wn) in Doh × M, and ph in Qh where (u, = curlwh,wn) is the

[p0291-b0014 | ordinary-paragraph | medium] solution of Problem (5.15).

[p0291-b0015 | ordinary-paragraph | medium] Moreover, under the hypotheses of Theorem 5.5 and if the exact pressure p

[p0291-b0016 | ordinary-paragraph | medium] belongs to H'(Q) for I ≥ 1, the following error estimate holds:

[p0291-b0017 | equation | low] Ilp - Phllo,2 ≤ C(h'lpl,2 + h'll∞ lli+1,α + h'-1|wli+1,α),

[p0291-b0018 | equation | low] (5.57)

[p0291-b0019 | ordinary-paragraph | medium] with a positive constant C independent of h, p, o and y.
