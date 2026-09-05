# Restored-source review candidate: chapter-03-section-04



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 251 / printed 237



[p0251-b0005 | equation | low] Ilu -- u,llx ≤ Ch'lly lli+2.s,

[p0251-b0006 | equation | low] (3.34)

[p0251-b0007 | ordinary-paragraph | medium] provided the solution of the Stokes Problem (2.1) has its stream function Φ in

[p0251-b0008 | ordinary-paragraph | low] dyi f! pauinin s! Koninoon fo uopuo auns ayi xaauos iou s! ? uaym (o)z+iH

[p0251-b0009 | ordinary-paragraph | medium] vorticity w belongs to Hl+1(Q).

[p0251-b0010 | ordinary-paragraph | medium] Finally, if the solution (u = (curl y,w), p) of Problem (2.1) has the regularity:

[p0251-b0011 | ordinary-paragraph | low] nssaud ayi aof anunsa ayi aany am xaauos s!  pun (o),Hsd o)z+Hep

[p0251-b0012 | ordinary-paragraph | medium] solution of Problem (2.36):

[p0251-b0013 | equation | low] (3.35)

[p0251-b0014 | equation | low] Il p - Phllo,o ≤ Ch'<{Ipl,o + Ilylli+2,s}.

[p0251-b0015 | ordinary-paragraph | medium] $4. A “Stream Function-Gradient of Velocity Tensor" Method in

[p0251-b0016 | ordinary-paragraph | medium] Two Dimensions

[p0251-b0017 | ordinary-paragraph | medium] The method discussed in this paragraph is obtained by taking for dependent

[p0251-b0018 | ordinary-paragraph | medium] variables the stream function y and the gradient of the velocity:

[p0251-b0019 | equation | low] 0y=0²4/0x;0xj,

[p0251-b0020 | equation | low] _1 ≤i,j≤ 2.

[p0251-b0021 | ordinary-paragraph | medium] In other words it solves for the stream function and all its second derivatives

[p0251-b0022 | ordinary-paragraph | medium] instead of the Laplacian, as was the case of the previous method. The reader will

[p0251-b0023 | ordinary-paragraph | medium] discover that this approach leads to a scheme -called the Hellan-Herrmann-

[p0251-b0024 | ordinary-paragraph | medium] Johnson scheme--which is economical and optimal. This, and related schemes,

[p0251-b0025 | ordinary-paragraph | medium] are thoroughly analyzed in Brezzi & Raviart [15]. The analysis presented here is

[p0251-b0026 | ordinary-paragraph | medium] a slight variant of this analysis, proposed by Babuska et al [5]. It is an elegant

[p0251-b0027 | ordinary-paragraph | medium] application of the use of mesh-dependent norms.

[p0251-b0028 | subsection | medium] 4.1. The Hellan-Herrmann-Johnson Formulation

[p0251-b0029 | ordinary-paragraph | medium] Let (u, p) denote the solution of Problem (2.1), but instead of the vorticity w, let

[p0251-b0030 | ordinary-paragraph | medium] us first introduce the non-symmetric gradient of velocity tensor Λ = (;):

[p0251-b0031 | equation | low]  1≤i,j≤ 2

[p0251-b0032 | equation | low] Nij = 0u;/0xj,

[p0251-b0033 | equation | low] (4.1)

[p0251-b0034 | ordinary-paragraph | medium] as a new dependent variable. Then the equations of Problem (2.1) read:

[p0251-b0035 | ordinary-paragraph | medium] 2

[p0251-b0036 | equation | low] v ∑ 0l;/0x; + 0p/0x; = f,  i = 1,2

[p0251-b0037 | ordinary-paragraph | medium] in Q

[p0251-b0038 | equation | low] (4.2)

[p0251-b0039 | equation | low] =O,

[p0251-b0040 | ordinary-paragraph | medium] whence a new formulation will be deduced by suitable integrations by parts.

## PDF 252 / printed 238



[p0252-b0003 | ordinary-paragraph | high] continuous boundary @x, unit exterior normal n= (n,,n,) and unit tangent

[p0252-b0004 | ordinary-paragraph | high] vector t =(—n,,n,). For a vector v in H'(x)? and a tensor t = (t,;) in H*(k)*

[p0252-b0005 | ordinary-paragraph | high] Green’s formula gives:

[p0252-b0006 | ordinary-paragraph | high] K K OK

[p0252-b0007 | ordinary-paragraph | high] Using the fact that v; = (v-n)n; + (v-t)t;, i = 1, 2, the boundary integral in (4.3)

[p0252-b0008 | ordinary-paragraph | high] can also be written as:

[p0252-b0009 | equation | low] | vjnjtds = | (v°n)t,;njn;ds + | (v-t)t,;n;t; ds.

[p0252-b0010 | ordinary-paragraph | high] Ox OK K

[p0252-b0011 | ordinary-paragraph | high] Thus summing over all i and j and defining the quantities:

[p0252-b0012 | ordinary-paragraph | high] 2

[p0252-b0013 | equation | low] M,(t) = Y tynjn

[p0252-b0014 | equation | low] Diadiagt>

[p0252-b0015 | ordinary-paragraph | high] (4.4) i, j=1

[p0252-b0016 | ordinary-paragraph | high] the identity (4.3) becomes:

[p0252-b0017 | equation | low] |x (0v;/0x;)t,;dx = -| v;(07,;/0X;) dx

[p0252-b0018 | equation | low] Kits i=e

[p0252-b0019 | ordinary-paragraph | high] — | v-nM,,(t)ds + | v-tM,,,(t) ds.

[p0252-b0020 | ordinary-paragraph | high] ey

[p0252-b0021 | ordinary-paragraph | high] OK

[p0252-b0022 | ordinary-paragraph | high] Or, with the well-known summation convention that a repeated index corre-

[p0252-b0023 | ordinary-paragraph | high] sponds to a sum, we have the more compact expression:

[p0252-b0024 | ordinary-paragraph | high] (4.5) |( 0v;/0x,)t,;dx = -| v;(0t;;/0x;d)x + | v-nM,,(t)d s

[p0252-b0025 | ordinary-paragraph | high] Ox

[p0252-b0026 | ordinary-paragraph | high] +| v°tM,,(t)ds, VveH(k)*, VreH'(x)*.

[p0252-b0027 | ordinary-paragraph | high] Ox

[p0252-b0028 | ordinary-paragraph | high] Together with (4.2), this identity is the foundation of several schemes, including

[p0252-b0029 | ordinary-paragraph | high] the Hellan-Herrmann-Johnson scheme.

[p0252-b0030 | ordinary-paragraph | high] Here again, there are several ways of formulating the present method; we

[p0252-b0031 | ordinary-paragraph | high] propose a mesh-dependent formulation closely related to that of Section 2.3. So,

[p0252-b0032 | ordinary-paragraph | high] we assume that Q is a bounded domain of R? with a polygonal boundary I and

[p0252-b0033 | ordinary-paragraph | high] we introduce a triangulation 7, of Q made of triangles and/or convex quadri-

[p0252-b0034 | ordinary-paragraph | high] laterals with diameters bounded by h.

[p0252-b0035 | ordinary-paragraph | high] Like in Section 2.3, assume that the velocity u and right-hand side f satisfy:

[p0252-b0036 | ordinary-paragraph | high] ue H*(Q)’, fe L*(Q)’. Let us examine the equations (4.2) in the light of (4.1) and

[p0252-b0037 | ordinary-paragraph | high] (4.5). Observe that if the tensor t belongs globally to H'(Q)* and if the vector

[p0252-b0038 | ordinary-paragraph | high] field v belongs to

## PDF 253 / printed 239



[p0253-b0003 | ordinary-paragraph | high] then the sum of the surface integrals: )’,. <7, Jor ¥°0M,,(t) ds is zero. Therefore the

[p0253-b0004 | ordinary-paragraph | high] assumption that u belongs to H*(Q)? permits to apply (4.5) to the first equations

[p0253-b0005 | ordinary-paragraph | high] (4.2), thus giving:

[p0253-b0006 | ordinary-paragraph | high] ES: ‘|A ,;(0v;/0x;) dx -| My(d)¥-tds} -| pdiv v dx = f-vdx

[p0253-b0007 | ordinary-paragraph | high] (4.6) KeT;, kK OK Q Q

[p0253-b0008 | ordinary-paragraph | high] Vve H(div;Q) withv|,¢H'(k)? VWKeZJ,.

[p0253-b0009 | ordinary-paragraph | high] Likewise, to match (4.6) we can also express the relation (4.1) between u and J by:

[p0253-b0010 | ordinary-paragraph | high] (4.7) (A ytyax= 5 4{c s(Ouloxadx — | My(o)u-tds} Veen (Q)e

[p0253-b0011 | ordinary-paragraph | high] Py K Ox

[p0253-b0012 | ordinary-paragraph | high] since the sum

[p0253-b0013 | ordinary-paragraph | high] » M,,(t)u-tds

[p0253-b0014 | ordinary-paragraph | high] Ke ZT, J 0K

[p0253-b0015 | ordinary-paragraph | high] is zero for uin H}(Q)? and t in H}(Q)*.

[p0253-b0016 | ordinary-paragraph | high] Finally a look at (4.6) and (4.7) shows that while the regularity of the test

[p0253-b0017 | ordinary-paragraph | high] function vy can hardly be decreased, the test tensor t need not belong globally

[p0253-b0018 | ordinary-paragraph | high] to H1(Q)*. In fact, (4.7) makes sense if t belongs to H'(x)* on each x. Besides

[p0253-b0019 | ordinary-paragraph | high] that, it is convenient to assume that M,,(t) is continuous across interelement

[p0253-b0020 | ordinary-paragraph | high] boundaries—.e. across all segments of J;,.

[p0253-b0021 | ordinary-paragraph | high] Summing up, we see that if (u, p) is the solution of the Stokes problem (2.1)

[p0253-b0022 | ordinary-paragraph | high] with u in (H7(Q)M H3(Q))? and p in H'(Q) L3(@) then the triple (u, A, p) with

[p0253-b0023 | ordinary-paragraph | high] is also a solution of:

[p0253-b0024 | equation | low] ueH,(div;Q) withu|,eH'(k)* Wee,

[p0253-b0025 | ordinary-paragraph | high] A€H'(x)* Wee, with M,,(A) continuous on J, and

[p0253-b0026 | equation | low] Avi ar A>? — 0, Delaise).

[p0253-b0027 | ordinary-paragraph | high] ys ‘|a y(ousex)ax — | My(2}¥- tds}- | p divv d x

[p0253-b0028 | ordinary-paragraph | high] (4.8) KeT;, K OK Q

[p0253-b0029 | equation | low] =| f-vdx VveH,(div;2) withv|,eH'(k)? VWeeY,,

[p0253-b0030 | ordinary-paragraph | high] Q

[p0253-b0031 | equation | low] ,j(Ou;/Ox;)dx — | Maieu-tds| =i)

[p0253-b0032 | ordinary-paragraph | high] |A igtig Ax — S ‘|T

[p0253-b0033 | ordinary-paragraph | high] Q KET, K OK

[p0253-b0034 | ordinary-paragraph | high] VteH'(k)* VeeZ%Z, with M,,(t) continuous on J;,.

[p0253-b0035 | ordinary-paragraph | high] Conversely, a routine argument shows that Problem (4.8) has at most one

[p0253-b0036 | ordinary-paragraph | high] solution. Indeed, the second equations (4.8) imply:

## PDF 254 / printed 240



[p0254-b0003 | ordinary-paragraph | high] and in turn divu = 0 in Q. Then, supposing that the right-hand side f = 0 we

[p0254-b0004 | ordinary-paragraph | high] easily derive that 4,, = 0 for all i,j . Thus, u is constant in each x and moreover

[p0254-b0005 | equation | low] | M,y(c)u-tds = 0

[p0254-b0006 | ordinary-paragraph | high] kK JOK

[p0254-b0007 | ordinary-paragraph | high] VteH'(x)* with M,,(t) continuous across the segments of J;,.

[p0254-b0008 | ordinary-paragraph | high] In view of the fact that u belongs to Ho(div; Q), this last relation readily implies

[p0254-b0009 | ordinary-paragraph | high] that u = 0 in Q. As a consequence, Problem (4.8) is an equivalent formulation of

[p0254-b0010 | ordinary-paragraph | high] the Stokes problem (2.1) whenever the solution of Problem (2.1) has sufficient

[p0254-b0011 | ordinary-paragraph | high] regularity.

[p0254-b0012 | ordinary-paragraph | high] To eliminate the pressure, Problem (4.8) can also be expressed in terms of

[p0254-b0013 | ordinary-paragraph | high] stream functions. Indeed, recall that v¢ H,(div; Q) satisfies div v = 0 iff:

[p0254-b0014 | ordinary-paragraph | high] v=curld with de® = {¢eH'(Q); d|,, = 0, |p is constant, 1 <i < p}.

[p0254-b0015 | ordinary-paragraph | high] If in addition v|, €¢ H'(x)* then ¢|, ¢ H*(x) and conversely. Then we can rewrite

[p0254-b0016 | ordinary-paragraph | high] directly Problem (4.8) in terms of stream functions, but the netations are sim-

[p0254-b0017 | ordinary-paragraph | high] plified if instead of working with the tensor 4 we now introduce the symmetric

[p0254-b0018 | ordinary-paragraph | high] tensor a:

[p0254-b0019 | ordinary-paragraph | high] The correspondence between o and / is:

[p0254-b0020 | equation | low] Avy = —Ag=2 01 2, Ani = —G11, At= % 2,

[p0254-b0021 | ordinary-paragraph | high] (4.10) M,,.(A) = —M,(0),

[p0254-b0022 | equation | low] M,(A) = M,,(9).

[p0254-b0023 | ordinary-paragraph | high] This induces us to define the following space of tensors:

[p0254-b0024 | ordinary-paragraph | high] Ost A =ye = (Jel (OQ); eH (k) VRE). t= ty,

[p0254-b0025 | ordinary-paragraph | high] , M,,(t) is continuous on each segment of /,},

[p0254-b0026 | ordinary-paragraph | high] together with the space ¥ of stream functions (already introduced in Section 2.3):

[p0254-b0027 | ordinary-paragraph | high] (4.12) P = {¢e@; d|,€H?*(k) Vee J;}.

[p0254-b0028 | ordinary-paragraph | high] With these spaces and the above correspondence, the sum of the surface

[p0254-b0029 | ordinary-paragraph | high] integrals in (4.8) has also the following expression:

[p0254-b0030 | equation | low] »), | Maliju-tds = | M,,(c)S(dw/énd)s ,

[p0254-b0031 | ordinary-paragraph | high] Ke TZ, J 0K Ty,

[p0254-b0032 | ordinary-paragraph | high] where S(y) denotes the jump of y over the segments of 7%, (cf. Section 2.3).

[p0254-b0033 | ordinary-paragraph | high] Therefore, Problem (4.8) has the following equivalent formulation, called the

[p0254-b0034 | ordinary-paragraph | high] Hellan-Herrmann-Johnson formulation:

[p0254-b0035 | ordinary-paragraph | high] Find a pair (o,W)eX x ¥ satisfying:

## PDF 255 / printed 241



[p0255-b0003 | ordinary-paragraph | high] KeZ, kK Ty,

[p0255-b0004 | ordinary-paragraph | high] (4.13) =| \,f- ccuurrl lédx VdeY,P

[p0255-b0005 | ordinary-paragraph | high] |O T dx — » |1 40° w/0x,0x,dx — | M,,(t)S(@w/én) is}

[p0255-b0006 | ordinary-paragraph | high] Q Ke 7, Jk ifs,

[p0255-b0007 | ordinary-paragraph | high] lee Voew.

[p0255-b0008 | ordinary-paragraph | high] Here again, it is possible to express (4.13) by means of two bilinear forms a,(., .)

[p0255-b0009 | ordinary-paragraph | high] and b,(., .):

[p0255-b0010 | ordinary-paragraph | high] (4.14) G,\G.0). = |g ,t,4x Vtensors o and 7 in L?(Q)4,

[p0255-b0011 | ordinary-paragraph | high] Q

[p0255-b0012 | ordinary-paragraph | high] 6/0x,0x;dx + ifM, ,(t)S(6@/¢n) ds

[p0255-b0013 | ordinary-paragraph | high] (4.15) by(t, @) = = |1 0°

[p0255-b0014 | ordinary-paragraph | high] Vted, VhdeEH'(Q) with g|,¢H*(x).

[p0255-b0015 | ordinary-paragraph | high] Then Problem (4.13) reads:

[p0255-b0016 | ordinary-paragraph | high] Find a pair (o, W)eX x ¥ such that:

[p0255-b0017 | equation | low] b,(c,¢) = —(1/v)(f,curld) Vee ¥,

[p0255-b0018 | ordinary-paragraph | high] (4.13’)

[p0255-b0019 | equation | low] { a(o,t)+5,(4,~)=0 Vre2.

[p0255-b0020 | ordinary-paragraph | high] Note the analogy with Problems (2.48) and (2.48’) of Section 2.3. Observe also

[p0255-b0021 | ordinary-paragraph | high] that when t belongs to © H1(Q)* and ¢ belongs to ¥, b,(t, #) reduces to:

[p0255-b0022 | ordinary-paragraph | high] (4.16) b(t.) = |( 6¢,/0x;)(04/0x,d)x ,

[p0255-b0023 | ordinary-paragraph | high] Q

[p0255-b0024 | ordinary-paragraph | high] a property which is similar to (2.51a).

[p0255-b0025 | ordinary-paragraph | high] The following theorem summarizes the results of this section.

[p0255-b0026 | theorem | high] Theorem 4.1. Let Q be a bounded plane polygon and 7, a triangulation of Q.

[p0255-b0027 | ordinary-paragraph | high] Suppose that the solution (u = curl w, p) of the Stokes problem (2.1) has the regularity:

[p0255-b0028 | ordinary-paragraph | high] ue(H7(Q)NH5(Q))?, pe H'(Q)NL4(2).

[p0255-b0029 | ordinary-paragraph | high] Then

[p0255-b0030 | ordinary-paragraph | high] 1°) the triple (u,(A,;= 0u,/Ox;), p) is the unique solution of Problem (4.8);

[p0255-b0031 | ordinary-paragraph | high] 2°) the pair ((o;; = Gas Ox,), W) is the unique solution of Problem (4.13).

[p0255-b0032 | ordinary-paragraph | high] In the next section, we shall assume that:

[p0255-b0033 | ordinary-paragraph | high] (4.17) We ta(2) em pen \2),

[p0255-b0034 | ordinary-paragraph | high] in order to be able to work with either Problem (4.8) or Problem (4.13).

## PDF 256 / printed 242



[p0256-b0003 | ordinary-paragraph | high] We propose to approximate Problem (4.13). To simplify the discussion, we

[p0256-b0004 | ordinary-paragraph | high] assume that 7, consists of triangles, but the present method can easily be

[p0256-b0005 | ordinary-paragraph | high] extended to the case where Y, also contains quadrilaterals. First, we choose the

[p0256-b0006 | ordinary-paragraph | high] finite element spaces. As usual, we take

[p0256-b0007 | ordinary-paragraph | high] (4.18) 0, = {0e¢°(Q); 0|,EP, Vee F,}, G,=9,N9,

[p0256-b0008 | ordinary-paragraph | high] for some integer | > 1. But as far as tensors are concerned, since the tensors of

[p0256-b0009 | ordinary-paragraph | high] » need not be globally continuous, we can approximate it with a space }, that

[p0256-b0010 | ordinary-paragraph | high] involves less degrees of freedom:

[p0256-b0011 | ordinary-paragraph | high] (4.19) Jp At = ()e2) Tel VRE7, 5:

[p0256-b0012 | ordinary-paragraph | high] With these spaces, Problem (4.13) is discretized by the following Problem (Q,,):

[p0256-b0013 | ordinary-paragraph | high] Find a pair (6, W,)€+ }, X D, satisfying:

[p0256-b0014 | equation | low] v > | (67¢/0x;0x;)(o,), 4x — | M,,(o,)S(0¢/6n) ds

[p0256-b0015 | ordinary-paragraph | high] KET, JK Th,

[p0256-b0016 | equation | low] =(f,curld) VdeE@,,

[p0256-b0017 | equation | low] (4.20)

[p0256-b0018 | ordinary-paragraph | high] |( o,)jt4x — >, | (0? W,/0x,0x,)t,4x -| M,,(t)S(éy,/6n) ds

[p0256-b0019 | ordinary-paragraph | high] Q Ee

[p0256-b0020 | ordinary-paragraph | high] KET), JK

[p0256-b0021 | ordinary-paragraph | high] When expressed in terms of the bilinear forms a,(., .) and b,(., .) defined by (4.14)

[p0256-b0022 | ordinary-paragraph | high] and (4.15), the equations (4.20) can be written more compactly as:

[p0256-b0023 | equation | low] eee = —(1/v)(f,eurl¢,) V¢,e%,,

[p0256-b0024 | ordinary-paragraph | high] (4.20’)

[p0256-b0025 | equation | low] Ay(Fns Th) + D,(t,,W,) = O VT, Xp.

[p0256-b0026 | ordinary-paragraph | high] In order to analyze Problem (Q,), we must first study thoroughly the above

[p0256-b0027 | ordinary-paragraph | high] finite element spaces and in particular equip them with appropriate norms and

[p0256-b0028 | ordinary-paragraph | high] specify their degrees of freedom. As far as norms are concerned, the expression

[p0256-b0029 | ordinary-paragraph | high] of the bilinear form b,(., .) suggests to choose:

[p0256-b0030 | ordinary-paragraph | high] i 1/2

[p0256-b0031 | ordinary-paragraph | high] (4.21) IT lon = It llo,a + AlMl,( 7) laf Vred,

[p0256-b0032 | ordinary-paragraph | high] i wi 1

[p0256-b0033 | ordinary-paragraph | high] 1/2

[p0256-b0034 | equation | low] Plan = Dd 1lo,6 + (L/h) iste6am 3,5}

[p0256-b0035 | ordinary-paragraph | high] (4.22) on

[p0256-b0036 | ordinary-paragraph | high] Ke7,

[p0256-b0037 | ordinary-paragraph | high] Vode H'(Q) with d|,¢H7(x).

[p0256-b0038 | ordinary-paragraph | high] Observe again the analogy with (2.52) and (2.53). Note also that

[p0256-b0039 | ordinary-paragraph | high] [atsP O)< Wt llowll@llan, VreX, Whe H*(Q) with ¢|,,¢H7(x),

[p0256-b0040 | equation | low] lan(t, I< WItlloellHlloe Vt, we L?(Q)*.

## PDF 257 / printed 243



[p0257-b0004 | lemma | high] Lemma 4.1. Let & be the reference unit triangle. A symmetric tensor-valued func-

[p0257-b0005 | ordinary-paragraph | high] tion te P*, is uniquely determined on & by the following moments:

[p0257-b0006 | ordinary-paragraph | high] | M,(t)qds YVqeP,_,(k’) for all sides k' of R,

[p0257-b0007 | ordinary-paragraph | high] (4.23) -

[p0257-b0008 | ordinary-paragraph | high] |T q aX Vqe P,_2(k), ESSE, MRE),

[p0257-b0009 | proof | high] Proof. To begin with, we observe that (4.23) consists of

[p0257-b0010 | equation | low] 31 + (3/2)l — 1) = (3/2)10. + 1)

[p0257-b0011 | ordinary-paragraph | high] degrees of freedom and that

[p0257-b0012 | equation | low] dimer 4 t= 47 = (3/210 + 1);

[p0257-b0013 | ordinary-paragraph | high] Thus it suffices to prove that the set of homogeneous equations:

[p0257-b0014 | equation | low] | M,(t)qds=0 VqeP,_,(k’), for all sides k’ of K,

[p0257-b0015 | ordinary-paragraph | high] (4.24) :

[p0257-b0016 | equation | low] |t yqdaX =O VqeP_,(k), 1<ij <2,

[p0257-b0017 | ordinary-paragraph | high] K

[p0257-b0018 | ordinary-paragraph | high] has the unique solution t = 0.

[p0257-b0019 | ordinary-paragraph | high] Now the first equation of( 4.24) is equivalent to M,(t) = 0 on Ok. And, taking

[p0257-b0020 | ordinary-paragraph | high] advantage of the position and shape of k, this amounts to:

[p0257-b0021 | ordinary-paragraph | high] tq 0 Oxnk — 0,

[p0257-b0022 | equation | low] i, 10 one, = 0;

[p0257-b0023 | equation | low] T11 + 212 + T2, = 0 on x, + xX, =1.

[p0257-b0024 | ordinary-paragraph | high] Next, by taking q = 01,,/0X, in the second equation of (4.24), we obtain:

[p0257-b0025 | equation | low] |s imat=0 OTK el el et Se

[p0257-b0026 | ordinary-paragraph | high] Combining with the three equations above, this yields first that t = 0 on X, +

[p0257-b0027 | ordinary-paragraph | high] %, = 1 and then that t = 0 on OK.

[p0257-b0028 | ordinary-paragraph | high] Then (4.24) immediately implies that t = 0 on the whole of K. O

[p0257-b0029 | ordinary-paragraph | high] In order to extend Lemma 4.1 to an arbitrary triangle x, we must introduce

[p0257-b0030 | ordinary-paragraph | high] a suitable transformation that maps a symmetric tensor on kK into a symmetric

[p0257-b0031 | ordinary-paragraph | high] tensor on x while preserving in some sense M,(.) on 0x. To this end, we recall

[p0257-b0032 | ordinary-paragraph | high] on the one hand that the normal n to x and the normal fi to & are related by:

[p0257-b0033 | equation | low] f = [(BenB)en/||| J|o F ,

## PDF 258 / printed 244



[p0258-b0003 | ordinary-paragraph | high] where x = F(X) = B,& + b, and B,, is a nonsingular matrix with constant coeffi-

[p0258-b0004 | ordinary-paragraph | high] cients. On the other hand, we remark that

[p0258-b0005 | equation | low] M,(7)(x) = ((t(x)n(x), n(%)))

[p0258-b0006 | ordinary-paragraph | high] where ((., .)) denotes the Euclidean scalar product of R* associated with ||. ||.

[p0258-b0007 | ordinary-paragraph | high] Thus, we can write

[p0258-b0008 | equation | low] (M,(1)) oF, = |(Be*)7 All 7 (Be*(t 0 F,)(Be"")A ,f i).

[p0258-b0009 | ordinary-paragraph | high] This suggests to establish (in each x) the correspondence between tensor-valued

[p0258-b0010 | ordinary-paragraph | high] functions:

[p0258-b0011 | ordinary-paragraph | high] (4.25a) = B(CO Fe |B 4.4),

[p0258-b0012 | ordinary-paragraph | high] or equivalently

[p0258-b0013 | ordinary-paragraph | high] (4.25b) t= Dac Or (Be =e (Gc)

[p0258-b0014 | ordinary-paragraph | high] The first equation can be written explicitly as follows:

[p0258-b0015 | ordinary-paragraph | high] Zz

[p0258-b0016 | equation | low] Tij = (fy: Oo F*)(6F,/02,) (OF,/0,).

[p0258-b0017 | equation | low] r,s=1

[p0258-b0018 | ordinary-paragraph | high] Obviously, the transformation Y. preserves the symmetry and regularity of

[p0258-b0019 | ordinary-paragraph | high] tensors and furthermore:

[p0258-b0020 | ordinary-paragraph | high] (4.26) M,(2) = |\(BAel*)?) M,"C) ,

[p0258-b0021 | ordinary-paragraph | high] or

[p0258-b0022 | ordinary-paragraph | high] (4.26') M(t) = |B (n0 F,) |? My(2).

[p0258-b0023 | ordinary-paragraph | high] since

[p0258-b0024 | equation | low] |Be(no F,)|| = (Be") "all.

[p0258-b0025 | ordinary-paragraph | high] Hence it is easy to check that the statement of Lemma 4.1 carries over to an

[p0258-b0026 | ordinary-paragraph | high] arbitrary triangle x of 7,,. As a consequence, we can take the following values as

[p0258-b0027 | ordinary-paragraph | high] degrees of freedom for the tensors t of 2,:

[p0258-b0028 | ordinary-paragraph | high] | M,(t)qds VqeP,_,(k’), VK' of I,

[p0258-b0029 | ordinary-paragraph | high] |t yqdx~ “NG ePi5(«),0 wisi] S120) Vine Teenie:

[p0258-b0030 | remark | high] Remark 4.1. The simplest example of spaces 2}, corresponds to | = 1:

[p0258-b0031 | equation | low] 2, = {te L*(Q)*; 1, = ty, Tyl, = a constant c, Vx of J,

[p0258-b0032 | ordinary-paragraph | high] M,,(t) is continuous on each segment of I}.

## PDF 259 / printed 245



[p0259-b0005 | ordinary-paragraph | low]   s         e 

[p0259-b0006 | ordinary-paragraph | medium] from Z onto Z, with attractive properties. First, if t is a symmetric tensor of

[p0259-b0007 | ordinary-paragraph | medium] L'(k)4 with M,(t)e L'(ok) we define the symmetric tensor π,t of Pi-, by:

[p0259-b0008 | equation | low] M(πt - t)qds = 0

[p0259-b0009 | ordinary-paragraph | medium] Vsides k' of k,

[p0259-b0010 | ordinary-paragraph | low] Vq∈Pi-i(k)

[p0259-b0011 | equation | low] (4.27)

[p0259-b0012 | equation | low] (nt - t)ijq dx = 0  Vq∈P-2(k),  1 ≤i,j ≤ 2, if l ≥ 2.

[p0259-b0013 | ordinary-paragraph | medium] Then for te E, we define n,te E, by:

[p0259-b0014 | equation | low] (4.28)

[p0259-b0015 | equation | low] πhtlx=πK(tlx)K∈h.

[p0259-b0016 | ordinary-paragraph | medium] Clearly, π,t is a symmetric tensor and the continuity of M,(t) implies that M,(,t)

[p0259-b0017 | ordinary-paragraph | medium] is continuous across each interelement boundary k'. Therefore 7,t belongs

[p0259-b0018 | ordinary-paragraph | medium] indeed to E,. In addition, we readily derive from (4.25a) and (4.26) that (4.27)

[p0259-b0019 | ordinary-paragraph | medium] holds iff

[p0259-b0020 | ordinary-paragraph | medium] Vsides k' of k,

[p0259-b0021 | equation | low] Mn(πxt - t)qds = 0  Vq∈Pi-1(k)

[p0259-b0022 | equation | low] (4.29)

[p0259-b0023 | equation | low] ifl ≥ 2,

[p0259-b0024 | equation | low] (π-t）)jqdx=0

[p0259-b0025 | equation | low] Vq∈ Pi-2(k),  1 ≤i,j≤ 2,

[p0259-b0026 | ordinary-paragraph | medium] where, as usual, k denotes the unit reference triangle. Hence, applying the

[p0259-b0027 | ordinary-paragraph | medium] definition (4.27) to k, we find that 7, is preserved by affine transformations:

[p0259-b0028 | equation | low] πt=ntKegh.

[p0259-b0029 | equation | low] (4.30)

[p0259-b0030 | ordinary-paragraph | medium] The remaining properties of n, are stated in the next lemma.

[p0259-b0031 | lemma | medium] Lemma 4.2. Assume that the triangulation J, is regular. The operator π, defined

[p0259-b0032 | ordinary-paragraph | medium] by (4.27) and (4.28) is a linear mapping from 2 onto E, and satisfies:

[p0259-b0033 | equation | low] bn（t-πnt,Φn) =O VΦn∈Φn

[p0259-b0034 | equation | low] (4.31)

[p0259-b0035 | ordinary-paragraph | low] VteE.

[p0259-b0036 | equation | low] πnt llo,h ≤ C llT llo,h

[p0259-b0037 | equation | low] (4.32)

[p0259-b0038 | ordinary-paragraph | medium] Moreover, if t e H*(Q)4 N E for some real ke [1, l], the following estimate holds:

[p0259-b0039 | equation | low] πnt --tllo,n ≤C2hk}tk,

[p0259-b0040 | equation | low] (4.33)

[p0259-b0041 | proof | medium] Proof. It is clear from (4.27) that the operator n, is a linear mapping from  onto

[p0259-b0042 | ordinary-paragraph | medium] E,. Besides that, (4.31) follows immediately from (4.27), the expression (4.15) of

[p0259-b0043 | ordinary-paragraph | medium] bh(., .) and the definition of Oh.

[p0259-b0044 | ordinary-paragraph | medium] Let us turn to (4.32). To begin with, we observe from (4.27) that

[p0259-b0045 | equation | low] II M,(mnt)llo, r, ≤ I/ M,(t) llo, Tn

[p0259-b0046 | ordinary-paragraph | low] '3A 

[p0259-b0047 | equation | low] (4.34)

## PDF 260 / printed 246



[p0260-b0003 | ordinary-paragraph | high] (4.35) ItnTIlo,a <Clltllon Vrer,

[p0260-b0004 | ordinary-paragraph | high] where, for the sake of simplicity, the norms of tensors and scalars are denoted

[p0260-b0005 | ordinary-paragraph | high] alike. For each x of 7, (4.30) and (4.25a) imply:

[p0260-b0006 | equation | low] Iz. Tll5,0 < Idet(B,)| | By l* ll 2 Ilo,¢ -

[p0260-b0007 | ordinary-paragraph | high] But it follows easily from (4.29) that

[p0260-b0008 | equation | low] tet oe < Ci tld.¢ + I Ma@lloc,x ),

[p0260-b0009 | ordinary-paragraph | high] where the constant C, is independent of h. Next, (4.26) implies:

[p0260-b0010 | equation | low] Malt) II5,¢ <(Co/p,.) Bet |M i@llo0 Vsides x’ of x.

[p0260-b0011 | ordinary-paragraph | high] Likewise, we derive from (4.25b) that

[p0260-b0012 | equation | low] Elld.e < [det(B,)|7 B et I* It llo..-

[p0260-b0013 | ordinary-paragraph | high] Collecting these four inequalities and applying (A.2) and (A.4) we obtain:

[p0260-b0014 | ordinary-paragraph | high] THO. S Co(eIT U O + Fe Mell Ma(™) M10, 0n)-

[p0260-b0015 | ordinary-paragraph | high] Since 7, is regular, this proves (4.35) and in turn (4.32).

[p0260-b0016 | ordinary-paragraph | high] Finally, let us establish (4.33). Like above, we have

[p0260-b0017 | equation | low] t,t — Ton < |det(B,)] | Byl I* tet — Fld.

[p0260-b0018 | ordinary-paragraph | high] As the mapping z,; leaves invariant the symmetric tensors with coefficients in

[p0260-b0019 | ordinary-paragraph | high] Pros (Ac 12) gives:

[p0260-b0020 | ordinary-paragraph | high] [eee R: Hiei!

[p0260-b0021 | ordinary-paragraph | high] According to (4.25b), we have:

[p0260-b0022 | equation | low] tle < Be? U7 120 Fele,s

[p0260-b0023 | ordinary-paragraph | high] and in view of (A.7) this becomes

[p0260-b0024 | ordinary-paragraph | high] (4.36) tlie < C5 llB ellB et |? det(B7, I)he :

[p0260-b0025 | ordinary-paragraph | high] Since 7, is regular, the above inequalities yield:

[p0260-b0026 | ordinary-paragraph | high] [7,7 —Tllo.a Coh*|thk,0:

[p0260-b0027 | ordinary-paragraph | high] Similarly, it stems from (4.26’) that:

[p0260-b0028 | equation | low] Mn. 7— Hho, < CphByyl l*||| M|a(t et — Alle

[p0260-b0029 | ordinary-paragraph | high] and the trace Theorem I.1.5 implies:

[p0260-b0030 | equation | low] | Malet — A)lld,e < Colltet — tlle < Coltlze.

[p0260-b0031 | ordinary-paragraph | high] Therefore, owing to (4.36) and the regularity of 7,, we get:

[p0260-b0032 | equation | low] | M,,(7,.7 a T) MO ,x° < Gone AES

[p0260-b0033 | ordinary-paragraph | high] thus establishing (4.33). O

## PDF 261 / printed 247



[p0261-b0005 | ordinary-paragraph | low] (4.37) {bn(th,Φh) = 0 VΦh∈Φn} iff {bn(tn,Φ) = 0 VΦ∈PnC(S)}.

[p0261-b0006 | proof | medium] Proof. Obviously, it is the "only if" part of (4.37) which must be established. To

[p0261-b0007 | ordinary-paragraph | medium] this end, let us take Φ in C°(Ω) with Φlx eH²(k) (in which case Φe H'(Q)) and

[p0261-b0008 | ordinary-paragraph | medium] prove that

[p0261-b0009 | equation | low] bn(Tn-In)=Otn∈En

[p0261-b0010 | equation | low] (4.38)

[p0261-b0011 | ordinary-paragraph | medium] where I, is the interpolation operator defined by (A.22).

[p0261-b0012 | ordinary-paragraph | medium] Indeed, two integrations by parts yield:

[p0261-b0013 | ordinary-paragraph | low] f02Φ/0x;0x;dx =

[p0261-b0014 | ordinary-paragraph | medium] (0²f/0x;0x;)Φ dx -

[p0261-b0015 | ordinary-paragraph | medium] (of/ox;)pn; ds +

[p0261-b0016 | ordinary-paragraph | medium] f(oΦ/0x;)n;ds

[p0261-b0017 | ordinary-paragraph | low] Jor

[p0261-b0018 | ordinary-paragraph | low] JaK

[p0261-b0019 | ordinary-paragraph | low] KC

[p0261-b0020 | ordinary-paragraph | low] Vf, Φe H'(k).

[p0261-b0021 | ordinary-paragraph | medium] Thus, when f e Pi-1, the formulas (A.22) give:

[p0261-b0022 | ordinary-paragraph | low] fo²(Φ - IhΦ)/@x;0x;dx =

[p0261-b0023 | ordinary-paragraph | low] ,  VfePi-i·

[p0261-b0024 | ordinary-paragraph | low] ()HA  S

[p0261-b0025 | ordinary-paragraph | low] fn;0(Φ -InΦ)/0x;ds

[p0261-b0026 | ordinary-paragraph | low] Jak

[p0261-b0027 | ordinary-paragraph | medium] Substituting into the definition (4.15) of b, we obtain:

[p0261-b0028 | equation | low] bn(th-Ih)=-∑

[p0261-b0029 | ordinary-paragraph | low] Mnt(th)o(o - Inb)/ot ds.

[p0261-b0030 | ordinary-paragraph | low] KegnJor

[p0261-b0031 | ordinary-paragraph | low] (') u aide p ae go y ss a uo sd q ii u

[p0261-b0032 | ordinary-paragraph | medium] we readily find that b,(th, Φ - IhΦ) = 0. This proves (4.37).

[p0261-b0033 | ordinary-paragraph | medium] From the definition (A.22) it is easy to derive that the statement of Lemma

[p0261-b0034 | ordinary-paragraph | medium] 2.11 holds with 0, = Iu:

[p0261-b0035 | equation | low] |U—Inull2,n ≤ Chk-2|u/k, Vv∈ H*(S),

[p0261-b0036 | equation | low] (4.39)

[p0261-b0037 | ordinary-paragraph | medium] provided the triangulation J, is regular. Thus, combining (4.38) and (4.39) we

[p0261-b0038 | ordinary-paragraph | medium] have the next result.

[p0261-b0039 | corollary | medium] Corollary 4.1. The operator I, defined by (A.22) satisfies:

[p0261-b0040 | ordinary-paragraph | low] “"A

[p0261-b0041 | equation | low] bn(tn, - Ihd) =0  VΦ∈(S) with dlk∈H²(K),

[p0261-b0042 | ordinary-paragraph | medium] In addition, if J, is a regular triangulation of Ω, there exists a constant C > 0,

[p0261-b0043 | ordinary-paragraph | medium] independent of h and Φ, such that:

[p0261-b0044 | equation | low] 11b — Ihb112,h ≤ Chk-2|Φlk.s2 

[p0261-b0045 | ordinary-paragraph | medium] ()HA

[p0261-b0046 | ordinary-paragraph | medium] provided the real k belongs to [2, I + 1].

[p0261-b0047 | ordinary-paragraph | medium] Now we turn to the inf-sup condition. Let us first restrict ourselves to the

[p0261-b0048 | ordinary-paragraph | medium] space of tensors Z N o and more specifically to tensors of the form

## PDF 262 / printed 248



[p0262-b0003 | ordinary-paragraph | high] All such tensors satisfy

[p0262-b0004 | equation | low] by,( Tas $n) = (curl 6,,curld,) Vo,e,

[p0262-b0005 | ordinary-paragraph | high] and

[p0262-b0006 | ordinary-paragraph | high] talldvn rs 2 || nll5,.0 ae h|| O,\ld,r,-

[p0262-b0007 | ordinary-paragraph | high] Hence applying Lemma 2.12 we obtain the preliminary result:

[p0262-b0008 | equation | low] bith» Pr) > (1/,/2)B* \ldullo.n Vbne Drs

[p0262-b0009 | ordinary-paragraph | high] te LO? | Tallon

[p0262-b0010 | ordinary-paragraph | high] where f* is the constant of Lemma 2.12, provided Q is convex and the triangula-

[p0262-b0011 | ordinary-paragraph | high] tion is uniformly regular. By virtue of (4.31) and (4.32) this condition implies the

[p0262-b0012 | ordinary-paragraph | high] inf-sup condition on the space 2).

[p0262-b0013 | lemma | high] Lemma 4.4. Let Q be a bounded, convex polygon and let 7, be a uniformly regular

[p0262-b0014 | ordinary-paragraph | high] triangulation of Q. Then we have:

[p0262-b0015 | equation | low] sup itmPH )5 11 /2C,)1IBda *lla .n VOne Pr,

[p0262-b0016 | ordinary-paragraph | high] Tey, Tallon

[p0262-b0017 | ordinary-paragraph | high] where B* and C, are the constants of (2.63) and (4.32) respectively.

[p0262-b0018 | remark | high] Remark 4.2. Owing to Remark 2.8, we also have

[p0262-b0019 | equation | low] sup —Da—(—Th s—P r ) > (y(8)//Dldrlts.o Vreals>2, Vo,e%,.

[p0262-b0020 | equation | low] ne =No4 IIlTallovn

[p0262-b0021 | ordinary-paragraph | high] Thus, the assumptions of Lemma 4.4 imply the additional inf-sup condition:

[p0262-b0022 | ordinary-paragraph | high] oO) 5 TH V2C)Wldrli..o

[p0262-b0023 | equation | low] reals >2, Wed,

[p0262-b0024 | ordinary-paragraph | high] TEL, IT llo.n

[p0262-b0025 | remark | high] Remark 4.3. The construction of Lemma 4.4 can also be applied to prove that

[p0262-b0026 | ordinary-paragraph | high] Problem (4.20) has a unique solution without restriction on Q and 7,. Indeed,

[p0262-b0027 | ordinary-paragraph | high] since we are working with finite-dimensional spaces, all we need to show is that

[p0262-b0028 | ordinary-paragraph | high] the set {4,€ ®,; b,(t,,, %,) = 0 Vt, €2),} is reduced to the zero function. Now, by

[p0262-b0029 | ordinary-paragraph | high] proceeding like above, we construct te X @f such that b,(t,¢,) = |¢al7.e =

[p0262-b0030 | ordinary-paragraph | high] b, (7,7, ,) = 0. Hence ¢, = 0.

[p0262-b0031 | ordinary-paragraph | high] Finally when 7, is uniformly regular we can show like in Lemma 2.7 that

[p0262-b0032 | ordinary-paragraph | high] Il- lon and ||. ||o,q are two uniformly equivalent norms on &,. The proof, which is

[p0262-b0033 | ordinary-paragraph | high] left as an exercise, stems from the inequality:

[p0262-b0034 | equation | low] IMa(z)llo.n, <(C/h) Ito, =V ed,

[p0262-b0035 | ordinary-paragraph | high] We are now in a position to establish optimal error estimates for Problem

[p0262-b0036 | ordinary-paragraph | high] (4.20).

## PDF 263 / printed 249



[p0263-b0005 | ordinary-paragraph | medium] the solution (u = curl y,p) of the Stokes Problem (2.1) satisfies (4.17); let o =

[p0263-b0006 | ordinary-paragraph | low] (024/0x;0xj)i,j

[p0263-b0007 | ordinary-paragraph | medium] 1°) If the triangulation J, is regular, we have the bound

[p0263-b0008 | equation | low] (4.40)

[p0263-b0009 | equation | low] Ilo - onllo,o ≤ Ch*|ylk+2,2  Vk∈ [1, I],

[p0263-b0010 | equation | low]  1≥ 1,

[p0263-b0011 | ordinary-paragraph | medium] if  e Hk+2(Q). If in addition Ω is convex, we have either

[p0263-b0012 | equation | low] (4.41)

[p0263-b0013 | equation | low] [y - hli, ≤ C2hlyl3,o if l = 1 and y∈H²(Ω),

[p0263-b0014 | ordinary-paragraph | medium] or

[p0263-b0015 | ordinary-paragraph | low] (4.42) Iμ -nli.o ≤ Chk|ylk+1.   Vk∈[2,I]  if l ≥ 2 and ∈Hk+1(Ω).

[p0263-b0016 | ordinary-paragraph | medium] 2°) If J, is uniformly regular, we have:

[p0263-b0017 | equation | low] (4.43)

[p0263-b0018 | equation | low] llα -- onllo,h ≤ C4hk/ylk+2,2

[p0263-b0019 | equation | low] Vk∈[1,],  I≥ 1

[p0263-b0020 | ordinary-paragraph | medium] and if in addition Q is convex, we have:

[p0263-b0021 | equation | low]  —Wn2,n ≤ Csh*1ylk+2,

[p0263-b0022 | equation | low] Vke[1,l - 1], if l≥ 2

[p0263-b0023 | equation | low] (4.44)

[p0263-b0024 | ordinary-paragraph | medium] ()+H pup

[p0263-b0025 | proof | medium] Proof. As usual, we have:

[p0263-b0026 | equation | low] bn(o—On>Φn) =0 VΦn∈Φn,

[p0263-b0027 | equation | low] (4.45)

[p0263-b0028 | equation | low] an(C-Ohtn)+bn(th—yn)=0Vtn∈Eh

[p0263-b0029 | ordinary-paragraph | medium] Owing to Lemma 4.2 and Corollary 4.1, the relations (4.45) yield:

[p0263-b0030 | equation | low] bn（πnG—OnΦn)=OVΦn∈Φn,

[p0263-b0031 | equation | low] an(o - On,πnO - Oh) = 0

[p0263-b0032 | ordinary-paragraph | medium] and observe that these equalities hold without constraint on Q and ,. Now, the

[p0263-b0033 | ordinary-paragraph | medium] last equation implies directly that

[p0263-b0034 | equation | low] lo - onllo,a ≤ Ilo -— Tno llo,g.

[p0263-b0035 | equation | low] (4.46a)

[p0263-b0036 | ordinary-paragraph | medium] In addition, when J, is uniformly regular, the equivalence between the norms

[p0263-b0037 | ordinary-paragraph | medium] Il . Ilo, and Il Ilo,o gives

[p0263-b0038 | equation | low] Ilo - ohllo,h ≤ Ci llo - Thollo,h.

[p0263-b0039 | equation | low] (4.46b)

[p0263-b0040 | ordinary-paragraph | medium] Therefore (4.40) and (4.43) follow from (4.33).

[p0263-b0041 | ordinary-paragraph | medium] Next, the second equation (4.45) and Corollary 4.1 yield:

[p0263-b0042 | equation | low] bh（tnIhy—n)=an(on-Otn)Vtn∈En.

[p0263-b0043 | equation | low] (4.47)

[p0263-b0044 | ordinary-paragraph | medium] Therefore, when Ω is convex and , uniformly regular, it stems from Lemma 4.4

[p0263-b0045 | ordinary-paragraph | medium] that

## PDF 264 / printed 250



[p0264-b0003 | ordinary-paragraph | high] Hence (4.44) follows from (4.48), (4.40) and Corollary 4.1.

[p0264-b0004 | ordinary-paragraph | high] To establish (4.41) and (4.42) we use a familiar duality argument. For g in

[p0264-b0005 | ordinary-paragraph | high] L?(Q)* we introduce the auxiliary Stokes Problem:

[p0264-b0006 | equation | low] b,(u,,%) = (g,curld) Vee ¥,

[p0264-b0007 | equation | low] (4.49)

[p0264-b0008 | equation | low] A,(Hg,t) + b,(t,4,)=0 Vrer.

[p0264-b0009 | ordinary-paragraph | high] Since Q is convex, the solution (p,, 4 ,) belongs to H'(Q)* x H?(Q) with

[p0264-b0010 | ordinary-paragraph | high] (4.50) Hgllio + WAglls.o < CsllSllo,a-

[p0264-b0011 | ordinary-paragraph | high] Then a straightforward combination of (4.45), (4.49), (4.31) and Corollary 4.1

[p0264-b0012 | ordinary-paragraph | high] leads to:

[p0264-b0013 | equation | low] (g, curl (i a Wn) ae byl Lg on Tp Lg, W = 8) ar a,(o — Gn, Ug — Th Hg)

[p0264-b0014 | ordinary-paragraph | high] + b,(o — Ty,A, —Ty4g) VbneD,, Vt,E 2p.

[p0264-b0015 | ordinary-paragraph | high] When | > 2, Corollary 4.1, (4.33) and (4.50) yield:

[p0264-b0016 | ordinary-paragraph | high] IY — Walia <C vn in lw — Prllon + Ilo — Grllo,a + aE lo — toa

[p0264-b0017 | equation | low] (4.51)

[p0264-b0018 | ordinary-paragraph | high] When ! = 1, we only have:

[p0264-b0019 | equation | low] dala < CoP}i nt lw — Prllo.n+ |a ~ elo.o}

[p0264-b0020 | ordinary-paragraph | high] (4.52) bao

[p0264-b0021 | ordinary-paragraph | high] Coat all Gs ta llorn-

[p0264-b0022 | ordinary-paragraph | high] TEL,

[p0264-b0023 | ordinary-paragraph | high] In view of (4.40), Corollary 4.1 and (4.33), this implies (4.42) and (4.41). O

[p0264-b0024 | corollary | high] Corollary 4.2. We retain all the assumptions of Theorem 4.2. If w belongs to

[p0264-b0025 | ordinary-paragraph | high] H**?(Q) for some real ke[1,1] with | > 1, we have:

[p0264-b0026 | ordinary-paragraph | high] (4.53) IY — Walis.o <C A |Whe+2,@ for each s > 2.

[p0264-b0027 | proof | high] Proof. Formula (4.47) and the inf-sup condition proved in Remark 4.2 give:

[p0264-b0028 | ordinary-paragraph | high] (4.54) IT.— Vilis.a < C(S) lo — ollo,0-

[p0264-b0029 | ordinary-paragraph | high] Hence (4.53) follows from (4.40) and (A.23). O

[p0264-b0030 | remark | high] Remark 4.4. The above theorem calls for a number of comments. First of all, it

[p0264-b0031 | ordinary-paragraph | high] is obvious that this approach yields very neatly optimal error estimates for

[p0264-b0032 | ordinary-paragraph | high] polynomials of all degrees. In addition, the scheme considered is fairly inexpensive.

[p0264-b0033 | ordinary-paragraph | high] On the other hand, all results are stated for a right-hand side f in L?(Q)?

[p0264-b0034 | ordinary-paragraph | high] whereas one is often interested in solving the Stokes problem when the right-hand

[p0264-b0035 | ordinary-paragraph | high] side is in L’(Q)? withr < 2. The next section extends the error analysis to this case.

## PDF 265 / printed 251



[p0265-b0005 | ordinary-paragraph | medium] case where the right-hand side f belongs to L'(Q)² with 1 < r < 2. Since the

[p0265-b0006 | ordinary-paragraph | medium] spaces of Problem (4.20) are finite-dimensional, and in particular Φ, is included

[p0265-b0007 | ordinary-paragraph | medium] in W1, ∞(Q), it is clear that Problem (4.20) still has a unique solution when the

[p0265-b0008 | ordinary-paragraph | medium] right-hand side f is only in L'(Ω), for 1 < r < 2. Thus, we must focus our

[p0265-b0009 | ordinary-paragraph | medium] attention on the equations (4.13) of the continuous problem and see how to adapt

[p0265-b0010 | ordinary-paragraph | medium] them to such a right-hand side. This is achieved much like in Section 2.1: the

[p0265-b0011 | ordinary-paragraph | medium] regularity of the tensor-valued functions t is decreased while that of the test

[p0265-b0012 | ordinary-paragraph | medium] stream functions Φ is increased.

[p0265-b0013 | ordinary-paragraph | medium] If the solution (u = curly,p) of the Stokes Problem (2.1) is such that

[p0265-b0014 | ordinary-paragraph | medium] y e W3,"(Ω), then o belongs to W1.(Q)4 and therefore, according to Sobolev's

[p0265-b0015 | ordinary-paragraph | medium] Imbedding Theorem 1.1.3 and the trace Theorem I.1.5 we have:

[p0265-b0016 | ordinary-paragraph | low] ("1)(-T(o)"W ()T0

[p0265-b0017 | ordinary-paragraph | medium] Hence we replace the space of tensors E by:

[p0265-b0018 | equation | low] ∑ = {t∈ L²(Q)4; tlk ∈ W1,r(k)4, T12 = t21, M,(t) is continuous

[p0265-b0019 | ordinary-paragraph | medium] on each segment of Fh}.

[p0265-b0020 | ordinary-paragraph | medium] Likewise, since f is only in L'(Q)², we replace the space Y by

[p0265-b0021 | equation | low] 'I = a/1 + s/1  ()s1M U

[p0265-b0022 | ordinary-paragraph | medium] Then, it is a matter of routine to verify that the pair (y,o = (o?/ox;ox,)) is the

[p0265-b0023 | ordinary-paragraph | medium] unique solution of:

[p0265-b0024 | ordinary-paragraph | low] ()sMUA

[p0265-b0025 | ordinary-paragraph | medium] f·curlΦ dx

[p0265-b0026 | equation | low] bn(o,Φ) = -(1/v) 

[p0265-b0027 | equation | low] (4.55)

[p0265-b0028 | ordinary-paragraph | low] JQ

[p0265-b0029 | equation | low] an(o, t) + bn(t,y) = O Vte E.

[p0265-b0030 | ordinary-paragraph | medium] Now, a glance at Theorem 4.2 and its corollary shows that, in order to derive

[p0265-b0031 | ordinary-paragraph | medium] adequate error estimates in this case, we must verify that (4.46a), (4.48) and (4.54)

[p0265-b0032 | ordinary-paragraph | medium] are still valid here. To begin with, (4.46a) is a consequence of (4.45) together with

[p0265-b0033 | ordinary-paragraph | medium] the equations:

[p0265-b0034 | ordinary-paragraph | low] on∈n,

[p0265-b0035 | equation | low] bn(α -- Th, Φn) = 0

[p0265-b0036 | equation | low] bn(th—Ihy)=OVh∈Eh.

[p0265-b0037 | ordinary-paragraph | medium] But for y in W3.r(Ω) and o in W1.r(Ω)4, both Iny and π,o are well-defined and

[p0265-b0038 | ordinary-paragraph | medium] satisfy the above equations. And of course the equations (4.45) hold here. There-

[p0265-b0039 | ordinary-paragraph | medium] fore (4.46a) is verified. Likewise, (4.48) and (4.54) stem from (4.47) and the inf-sup

[p0265-b0040 | ordinary-paragraph | medium] conditions of Lemma 4.4 and Remark 4.2. Since the finite element spaces are

[p0265-b0041 | ordinary-paragraph | medium] unchanged, the inf-sup conditions carry over without modification; and the

[p0265-b0042 | ordinary-paragraph | medium] above considerations show that (4.47) is still valid here. The next lemma sum-

[p0265-b0043 | ordinary-paragraph | medium] marizes these results.

## PDF 266 / printed 252



[p0266-b0003 | ordinary-paragraph | high] of the Stokes Problem (2.1) satisfy:

[p0266-b0004 | ordinary-paragraph | high] (4.56) weWw*"(Q), peW"(Q) for some reé(1,2].

[p0266-b0005 | ordinary-paragraph | high] Then (4.46a) is valid. If in addition Q is convex and J, is uniformly regular, then

[p0266-b0006 | ordinary-paragraph | high] (4.48) and (4.54) also hold.

[p0266-b0007 | ordinary-paragraph | high] Next, it is easy to extend the approximation property of Lemma 4.2 to the

[p0266-b0008 | ordinary-paragraph | high] case where t€ W!’"(Q)*.

[p0266-b0009 | lemma | high] Lemma 4.6. Let 7, be a regular family of triangulations of Q. We have:

[p0266-b0010 | ordinary-paragraph | high] (4.57) Wpe = og Craie cl e

[p0266-b0011 | ordinary-paragraph | high] for all symmetric tensors t in W'*"(Q)* with 1 <r < 2.

[p0266-b0012 | ordinary-paragraph | high] Finally, combining these two lemmas we easily obtain the desired extension

[p0266-b0013 | ordinary-paragraph | high] of Theorem 4.2 and its corollary.

[p0266-b0014 | theorem | high] Theorem 4.3. Suppose that the regularity conditions (4.56) hold. If the triangulation

[p0266-b0015 | ordinary-paragraph | high] 7, is regular, the solution (o,,, W;,) of Problem (4.20) satisfies the estimate:

[p0266-b0016 | ordinary-paragraph | high] (4.58) lo — allo.a < Ch|E| 3 ,,,0,

[p0266-b0017 | ordinary-paragraph | high] where o = (0*y/0x;0x;).

[p0266-b0018 | ordinary-paragraph | high] If in addition 7, is uniformly regular and Q is convex, then for each real B > 2,

[p0266-b0019 | ordinary-paragraph | high] there exists a constant C,() such that:

[p0266-b0020 | ordinary-paragraph | high] (4.59) IW — Waltp.a < Co(B"h|rW |e3,, ,0.

[p0266-b0021 | ordinary-paragraph | high] Furthermore, when the polynomials are of degree | > 2 we also have:

[p0266-b0022 | ordinary-paragraph | high] 1/2

[p0266-b0023 | ordinary-paragraph | high] (4.60) (e la Vale) < CshO Mls...

[p0266-b0024 | ordinary-paragraph | high] KET),

[p0266-b0025 | subsection | high] 4.4. Discontinuous Approximation of the Pressure

[p0266-b0026 | ordinary-paragraph | high] This section is devoted to a brief analysis of a numerical method that recovers

[p0266-b0027 | ordinary-paragraph | high] the pressure in the Hellan-Herrmann-Johnson scheme. The pressure is obtained

[p0266-b0028 | ordinary-paragraph | high] by a suitable approximation of Problem (4.8)—suitable in the sense that it

[p0266-b0029 | ordinary-paragraph | high] reduces to the equations (4.20) when divergence-free test functions are used. The

[p0266-b0030 | ordinary-paragraph | high] reader will find that it corresponds to a discontinuous approximation of the

[p0266-b0031 | ordinary-paragraph | high] pressure.

[p0266-b0032 | ordinary-paragraph | high] To be specific, we want to construct finite-dimensional subspaces Do, of

[p0266-b0033 | ordinary-paragraph | high] H (div; Q) and Q,, of L$(@) that satisfy:

[p0266-b0034 | equation | low] {V,€ Do, and (q;,divv,)=0 Vq,eQ,'=>v, =curl¢g, with ¢, in %,,

[p0266-b0035 | ordinary-paragraph | high] together with an adequate inf-sup condition. Let us start with the reference

[p0266-b0036 | ordinary-paragraph | high] element x. If « is the unit triangle, we introduce the polynomial space of dimen-

## PDF 267 / printed 253



[p0267-b0006 | ordinary-paragraph | medium] where P. denotes the space of homogeneous polynomials of degree k. If k is the

[p0267-b0007 | ordinary-paragraph | medium] unit square, we simply take the space of dimension 2l(l + 1):

[p0267-b0008 | equation | low] D = Qi.-1 x Qi-1.1

[p0267-b0009 | equation | low] (4.61b)

[p0267-b0010 | ordinary-paragraph | medium] where exceptionally Qr.s denotes the space of all polynomials of degree at most

[p0267-b0011 | ordinary-paragraph | medium] r in x, and s in x2. Then, it is easy to check that:

[p0267-b0012 | equation | low] div(D) = Pi-1,I

[p0267-b0013 | ordinary-paragraph | medium] Ker(div) = curl(P) if k is the unit triangle,

[p0267-b0014 | equation | low] div(D) = Qi-1,

[p0267-b0015 | ordinary-paragraph | medium] Ker(div) = curl(Q)  if k is the unit square.

[p0267-b0016 | ordinary-paragraph | medium] In addition, owing to the geometry of k, v·n reduces to a polynomial of Pi-1 on

[p0267-b0017 | ordinary-paragraph | medium] Ok for v in D.

[p0267-b0018 | ordinary-paragraph | medium] As a consequence, we can choose the following degrees of freedom for the

[p0267-b0019 | ordinary-paragraph | medium] vectors v of D:

[p0267-b0020 | ordinary-paragraph | medium] (i) the boundary moments of order I - 1 for v·n:

[p0267-b0021 | ordinary-paragraph | low] ·nf ds   Vf e Pi-1  on each side k' of k;

[p0267-b0022 | ordinary-paragraph | low] JR'

[p0267-b0023 | ordinary-paragraph | medium] (4.62)  (ii) the interior moments of order I -- 2 for v:

[p0267-b0024 | ordinary-paragraph | medium] P-2  if k is a triangle,

[p0267-b0025 | ordinary-paragraph | medium] ·fdx

[p0267-b0026 | ordinary-paragraph | low] A

[p0267-b0027 | ordinary-paragraph | medium] Qi-2.l-1 × Qi-1.l-2  if k is a square.

[p0267-b0028 | ordinary-paragraph | medium] It is a matter of routine to check that (4.62) defines a unique vector  of D and

[p0267-b0029 | ordinary-paragraph | medium] that the restriction of ·Λ on each side k' depends only upon the l values

[p0267-b0030 | ordinary-paragraph | medium] prescribed on this side.

[p0267-b0031 | ordinary-paragraph | medium] To switch from k to an arbitrary element k, we introduce the following

[p0267-b0032 | ordinary-paragraph | medium] contravariant transformation between the vector function v = (v1, v2) defined on

[p0267-b0033 | ordinary-paragraph | medium] K and v = (01,02) defined on k:

[p0267-b0034 | equation | low] v =  where voF =(1/JF)DF·.

[p0267-b0035 | equation | low] (4.63)

[p0267-b0036 | ordinary-paragraph | medium] The choice of F, is justified by the fact that, roughly speaking, it preserves the

[p0267-b0037 | ordinary-paragraph | medium] divergence, curl and normal component:

[p0267-b0038 | equation | low] (divv)o F = (1/J)div(-1v),

[p0267-b0039 | equation | low] -1(curly) = curl(y o F),

[p0267-b0040 | ordinary-paragraph | low] (Φ o F)(F-i v)· nds.

[p0267-b0041 | equation | low] pv·nds = 

[p0267-b0042 | ordinary-paragraph | low] Jok

[p0267-b0043 | ordinary-paragraph | low] Jor

[p0267-b0044 | ordinary-paragraph | medium] Then we fix I distinct points on each segment k' of I, and we set:

[p0267-b0045 | ordinary-paragraph | low] Doh = {vhe L²(Q)²; vhlk = F,veD VkeJ, vn·nis continuous

[p0267-b0046 | ordinary-paragraph | medium] (resp. 0) at the I points of each interior (resp. boundary)

[p0267-b0047 | equation | low] (4.64)

[p0267-b0048 | ordinary-paragraph | medium] segment k' of Ih}.

## PDF 268 / printed 254



[p0268-b0004 | ordinary-paragraph | medium] dictated by the above requirements and considerations. Clearly, we must choose

[p0268-b0005 | equation | low] Qh = {an∈ L2(Ω); ahlk ∈ Pi-1 Or Qi-1(k)

[p0268-b0006 | equation | low] (4.65)

[p0268-b0007 | ordinary-paragraph | medium] according that k is a triangle or a quadrilateral}.

[p0268-b0008 | ordinary-paragraph | medium] It follows immediately that:

[p0268-b0009 | equation | low] Don C Ho(div; Ω),

[p0268-b0010 | equation | low] {Vh∈ Don and (qh, divvn) = 0 Vqn∈Qh} → divvn = 0

[p0268-b0011 | equation | low] > Vh = curl Φn  for a unique Φ, in Φh.

[p0268-b0012 | remark | medium] Remark 4.5. When l = 1, the functions of Qh are constants in each k while the

[p0268-b0013 | ordinary-paragraph | medium] functions of D have the form:

[p0268-b0014 | equation | low]  = (c1 + cox1,C2 + cox2)  if k is the unit triangle,

[p0268-b0015 | equation | low] =(c1 + c3x1,C2 + c4x2)

[p0268-b0016 | ordinary-paragraph | medium] )if k is the unit square.

[p0268-b0017 | ordinary-paragraph | medium] From the degrees of freedom (4.62) we deduce a straightforward restriction

[p0268-b0018 | ordinary-paragraph | medium] operator t from H'(k) onto D:

[p0268-b0019 | ordinary-paragraph | medium] t is the unique polynomial of D that has the same degrees of freedom (4.62)

[p0268-b0020 | ordinary-paragraph | medium] on k as v.

[p0268-b0021 | ordinary-paragraph | medium] Then the transformation  yields the following restriction operator

[p0268-b0022 | equation | low] T,E (Ho(div; Q) N H'(Q)²; Don):

[p0268-b0023 | equation | low] (4.66)

[p0268-b0024 | equation | low] ThVIx =F()K∈Jh.

[p0268-b0025 | ordinary-paragraph | medium] The operator T, satisfies Lemma II.1.1. More precisely, we have the following

[p0268-b0026 | ordinary-paragraph | medium] crucial result.

[p0268-b0027 | theorem | medium] Theorem 4.4. If the triangulation J, is regular, the operator T, defined by (4.66)

[p0268-b0028 | ordinary-paragraph | medium] satisfies for all ve H1(Q)2:

[p0268-b0029 | ordinary-paragraph | medium] 1/2

[p0268-b0030 | ordinary-paragraph | low] + h-2/s /πnv - vllo,s,2 ≤ C(s)lvl1,2  Vs ≥ 2,

[p0268-b0031 | equation | low] (4.67)

[p0268-b0032 | ordinary-paragraph | low] (xeTn

[p0268-b0033 | equation | low] II div(π,v -- v)llo,o ≤ Cl| div v llo.o.

[p0268-b0034 | equation | low] (4.68)

[p0268-b0035 | ordinary-paragraph | medium] In addition, whatever the triangulation, we have:

[p0268-b0036 | equation | low] (4.69)

[p0268-b0037 | equation | low] (qh, div(πhV - v)) = O an∈Qh.

[p0268-b0038 | ordinary-paragraph | medium] Finally, when J, is made exclusively of triangles, the inequality (4.68) holds with

[p0268-b0039 | ordinary-paragraph | medium] C = 1 and no regularity requirement on Th.

[p0268-b0040 | proof | medium] Proof. The properties (4.68) and (4.69) are an easy consequence of the definition

[p0268-b0041 | ordinary-paragraph | medium] of π.

## PDF 269 / printed 255



[p0269-b0004 | ordinary-paragraph | high] (4.70) § = grad + curld

[p0269-b0005 | ordinary-paragraph | high] where q is the solution of

[p0269-b0006 | equation | low] Ag= divw ink, g@\a, = 0.

[p0269-b0007 | ordinary-paragraph | high] Since k is convex, Theorem I.1.8 says that g ¢ H*(k) with

[p0269-b0008 | equation | low] Glloe < Cyl div ¥llo¢-

[p0269-b0009 | ordinary-paragraph | high] As a consequence we can find ¢ in H?(k) that satisfies (4.70) and

[p0269-b0010 | ordinary-paragraph | high] Io? b/OX5N13,4 + 1078/03 18,

[p0269-b0011 | equation | low] < Cy{ ||0 6, /0%2 |I5,¢ + 1662/0% llo,¢ + Iidiv V1ld, 2}.

[p0269-b0012 | ordinary-paragraph | high] Thus a straightforward application of Theorem A.3 yields:

[p0269-b0013 | ordinary-paragraph | high] (4.71) [#0 — G1. ¢< C5{ 00; /0%213,¢ + 1002/82, [2.¢ + diO1v2 e} *?,

[p0269-b0014 | ordinary-paragraph | high] and a similar upper bound (with a different constant) for ||#¥ — ¥||o,,,.z- In view

[p0269-b0015 | ordinary-paragraph | high] of (4.63) and the regularity of 7,, a simple calculation now leads to (4.67).

[p0269-b0016 | theorem | high] Theorem 4.4 gives us the following inf-sup condition:

[p0269-b0017 | ordinary-paragraph | high] for each q,€Q,, there exists v,€ Do, such that

[p0269-b0018 | equation | low] (dy, div v;,) = Ild ullo,a.

[p0269-b0019 | ordinary-paragraph | high] and

[p0269-b0020 | ordinary-paragraph | high] 1/2

[p0269-b0021 | equation | low] YY Hale Valo. ||d iv v, loa S C(s) |d allo,e Vs > 2.

[p0269-b0022 | ordinary-paragraph | high] KeT,,

[p0269-b0023 | ordinary-paragraph | high] With the spaces Do, and Q, we propose the following discretization of

[p0269-b0024 | ordinary-paragraph | high] Problem (4.8):

[p0269-b0025 | ordinary-paragraph | high] Find a function p,, in Q,, satisfying

[p0269-b0026 | equation | low] |p , div v, dx = -| f-v,,dx

[p0269-b0027 | ordinary-paragraph | high] Q Q

[p0269-b0028 | ordinary-paragraph | high] (G72) +v) ‘|( Aj,)ij(Ov}i/0X;d) x — | Malia) tds]

[p0269-b0029 | ordinary-paragraph | high] KeT;, * OK

[p0269-b0030 | ordinary-paragraph | high] Vv,€ Dons

[p0269-b0031 | ordinary-paragraph | high] where the tensor A, is related by (4.10) to the solution o, € %, of (4.20).

[p0269-b0032 | ordinary-paragraph | high] Problem (4.20) can be solved independently of Problem (4.72), then owing

[p0269-b0033 | ordinary-paragraph | high] Since

[p0269-b0034 | ordinary-paragraph | high] Q,.

[p0269-b0035 | ordinary-paragraph | high] to the above inf-sup condition Problem (4.72) has a unique solution p,, in

[p0269-b0036 | ordinary-paragraph | high] Moreover, we have the following error estimate:

## PDF 270 / printed 256



[p0270-b0003 | ordinary-paragraph | high] regular triangulation of Q. If the solution (u, p) of the Stokes Problem (2.1) has the

[p0270-b0004 | ordinary-paragraph | high] regularity:

[p0270-b0005 | ordinary-paragraph | high] ue H**1(Q)?, pe H*(Q)N L3(Q) for some ke [1,1],

[p0270-b0006 | ordinary-paragraph | high] then the solution p, of Problem (4.72) satisfies the error estimate:

[p0270-b0007 | ordinary-paragraph | high] (4.73) IP — Palloa < Ch*{|Uls1,0 + |Pli,a}-

[p0270-b0008 | proof | high] Proof. In view of (4.10), for each q, in Q, we have:

[p0270-b0009 | equation | low] |( 4, — Pp) div v,4x| < |ldn — Pllo,all4iv Vallo.e

[p0270-b0010 | ordinary-paragraph | high] Q 1/2

[p0270-b0011 | ordinary-paragraph | high] te Vie rllo.a( Ss alt]

[p0270-b0012 | ordinary-paragraph | high] KET,

[p0270-b0013 | ordinary-paragraph | high] + v||M,(o — o)llo,7,S(O¥lDln o,°7;, -

[p0270-b0014 | ordinary-paragraph | high] Then, according to the inf-sup condition, we can choose v, in Do, such that

[p0270-b0015 | ordinary-paragraph | high] Gn Palo, a <Cy{Ndn — Plloe + VIG — Allo, 2} dn — Prllo,e

[p0270-b0016 | ordinary-paragraph | high] + v||M,(o — o%) lon, SW" Ollo,r,-

[p0270-b0017 | ordinary-paragraph | high] It remains to estimate S(v,:t). To this end, we use the fact that

[p0270-b0018 | ordinary-paragraph | high] Vi — Tl,V

[p0270-b0019 | ordinary-paragraph | high] with divv =q,— Ph |Vl1,@< Call—a Panll o,a; ve Hg (Q).

[p0270-b0020 | ordinary-paragraph | high] Since S(v-t) = 0 we can write

[p0270-b0021 | ordinary-paragraph | high] Hence the argument of Theorem 4.4 gives:

[p0270-b0022 | ordinary-paragraph | high] IS(Vn* Olloe S CaP) van 00; /0%2|lo,0 + |062/0%4 llo,4 + I|d iv #5, eSa re.

[p0270-b0023 | ordinary-paragraph | high] Therefore

[p0270-b0024 | equation | low] Sn Ollon, < Cah"? dn — Pallo.a

[p0270-b0025 | ordinary-paragraph | high] and consequently,

[p0270-b0026 | equation | low] ln — Pallose <C s{d n — Pllo,a + Vile — Gllo,nh}s :

[p0270-b0027 | ordinary-paragraph | high] Then (4.73) follows from (4.43) and Lemma A.5 or (A.51).

[p0270-b0028 | ordinary-paragraph | high] Observe that just (4.43) requires the uniformity of 7,,. Gl

[p0270-b0029 | remark | high] Remark 4.6. It is also possible to associate this discontinuous approximation of

[p0270-b0030 | ordinary-paragraph | high] the pressure with the “stream function-vorticity” scheme studied in §2. The

[p0270-b0031 | ordinary-paragraph | high] discrete version of the first equation (2.13) is:

[p0270-b0032 | equation | low] Find p,€Q,, defined by (4.65), solution of

[p0270-b0033 | ordinary-paragraph | high] (4.74) (Pp, div v,) = v(curl@,,v,) — (f,v,) Vv, Don.
