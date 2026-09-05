# Restored-source review candidate: chapter-03-section-03



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 236 / printed 222



[p0236-b0005 | ordinary-paragraph | medium] This estimate is a routine consequence of (2.69), Lemma A.7 and (A.21a).

[p0236-b0006 | ordinary-paragraph | medium] The last three results call for a number of comments. The first obvious remark

[p0236-b0007 | ordinary-paragraph | medium] is that the approach of this section provides sharper estimates than the preceding

[p0236-b0008 | ordinary-paragraph | medium] section. Indeed, as long as I ≥ 2 and the stream function y belongs to H'+1(Ω),

[p0236-b0009 | ordinary-paragraph | medium] (2.70) provides an optimal error bound for Iy - yhli,s. Unfortunately, this

[p0236-b0010 | ordinary-paragraph | medium] section brings no improvement on the error estimate for the vorticity w. And

[p0236-b0011 | ordinary-paragraph | medium] furthermore, it fails just as much to establish the convergence when piecewise

[p0236-b0012 | ordinary-paragraph | medium] linear elements are used (i.e. I = 1). In this case, the loss of accuracy arises from

[p0236-b0013 | ordinary-paragraph | medium] the approximation error in the norm I . Il2,h: clearly, this norm is not adapted to

[p0236-b0014 | ordinary-paragraph | medium] piecewise linear elements.

[p0236-b0015 | ordinary-paragraph | medium] Finally, it is worth pointing out that, in this section, there is little hope of

[p0236-b0016 | ordinary-paragraph | medium] discarding the convexity hypothesis on Ω because Lemma 2.12 requires that Φ(h)

[p0236-b0017 | ordinary-paragraph | medium] belong necessarily to H?(Q).

[p0236-b0018 | remark | medium] Remark 2.9. Owing to the trace terms in Il. llo,h and Il ll2,h, (2.67) yields the

[p0236-b0019 | ordinary-paragraph | medium] additional estimates:

[p0236-b0020 | equation | low] @ - @nlo,, ≤ Chk-3/2|lk+1,2,

[p0236-b0021 | equation | low] I S(oyn/0n)llo, Fn, ≤ Chk-1/2 /1k+1,2,

[p0236-b0022 | ordinary-paragraph | medium] for 1 ≤ k ≤ l, provided of course that ↓ e H*+1 (Q). This last inequality shows that

[p0236-b0023 | ordinary-paragraph | medium] the jump of oy,/0n across interelement boundaries (as well as Oy,/on on F) tends

[p0236-b0024 | ordinary-paragraph | medium] to zero like hk-1/2.

[p0236-b0025 | section | medium] §3. Further Topics on the "Stream Function-Vorticity-Pressure'

[p0236-b0026 | ordinary-paragraph | medium] Scheme

[p0236-b0027 | ordinary-paragraph | medium] This paragraph gives further developments on the "stream function-vorticity-

[p0236-b0028 | ordinary-paragraph | medium] pressure" method for the two-dimensional Stokes problem. In particular it

[p0236-b0029 | ordinary-paragraph | medium] derives better error estimates for W, w, and p, in the general case. These can also

[p0236-b0030 | ordinary-paragraph | medium] be improved by the use of special meshes.

[p0236-b0031 | subsection | medium] 3.1. Refinement of the Error Analysis

[p0236-b0032 | ordinary-paragraph | medium] We place ourselves in the situation of Section 2.2 and, unless otherwise specified,

[p0236-b0033 | ordinary-paragraph | medium] we use the same notations and concrete spaces O, = M,, Φ, and Q, defined by

[p0236-b0034 | ordinary-paragraph | medium] (2.39). As mentioned at the section's end, the error bounds given in Theorem 2.8

[p0236-b0035 | ordinary-paragraph | medium] are quite poor because our estimate for the approximation error in V, is too

[p0236-b0036 | ordinary-paragraph | medium] coarse. Now, we are going to concentrate on this estimate. The following lemma

[p0236-b0037 | ordinary-paragraph | medium] establishes an analogue of (l1.1.16) in abstract situations.

## PDF 237 / printed 223



[p0237-b0004 | equation | low] (curl(Φ - Φh), curl μh)/

[p0237-b0005 | ordinary-paragraph | low] inf |u -wnl ≤

[p0237-b0006 | equation | low] inf

[p0237-b0007 | equation | low] 2]u - vnl + sup

[p0237-b0008 | ordinary-paragraph | low] Il μnllo,2

[p0237-b0009 | ordinary-paragraph | medium] WhEVn

[p0237-b0010 | equation | low] Un=(curl Φn,0n)e Xn L

[p0237-b0011 | ordinary-paragraph | low] μhE Mh

[p0237-b0012 | equation | low] (3.1)

[p0237-b0013 | ordinary-paragraph | medium] The same bound is valid for infwnev, Ilu — wulx with the norm I.| in the right-hand

[p0237-b0014 | ordinary-paragraph | medium] side of (3.1) replaced by Il Ilx.

[p0237-b0015 | proof | medium] Proof. Let v, = (curl Φ,, On) be an arbitrary element of X, and let t, E M, be defined

[p0237-b0016 | ordinary-paragraph | medium] by:

[p0237-b0017 | equation | low] (Th μn) = (0 - On,μn) - (curl(Φ - Φn), curl μn)

[p0237-b0018 | ordinary-paragraph | low] Wuhe Mh.

[p0237-b0019 | ordinary-paragraph | medium] Then

[p0237-b0020 | equation | low] [(curl(b -- Φn), curl μh)/

[p0237-b0021 | equation | low] (3.2)

[p0237-b0022 | equation | low] IIt,llo.s ≤ Iθ -- Onllo.o + sup

[p0237-b0023 | ordinary-paragraph | low] I μ,llo,.2

[p0237-b0024 | ordinary-paragraph | low] μhEMn

[p0237-b0025 | ordinary-paragraph | medium] Furthermore, since M, c O, the pair z, = (O, th) belongs to X,. Let us set

[p0237-b0026 | equation | low] Wh = Uh + Zh

[p0237-b0027 | ordinary-paragraph | medium] and note that w, e V, because ve V. Thus, we have

[p0237-b0028 | equation | low] [u - Wn| ≤ Iu - UnI + I/thllo,s,

[p0237-b0029 | equation | low] ||u - w,llx ≤ Ilu - Unllx + I/Ithllo,Ω

[p0237-b0030 | ordinary-paragraph | medium] and the bound (3.1) follows from (3.2) and the fact that v, is arbitrary.

[p0237-b0031 | ordinary-paragraph | medium] 口

[p0237-b0032 | ordinary-paragraph | medium] By inspecting (3.1), we see that the difficulties lie in evaluating properly the

[p0237-b0033 | ordinary-paragraph | medium] term

[p0237-b0034 | equation | low] (curl(Φ - Φh), curl μh)/

[p0237-b0035 | equation | low] sup

[p0237-b0036 | ordinary-paragraph | low] I μh ll o,S2

[p0237-b0037 | ordinary-paragraph | low] μhEMn

[p0237-b0038 | ordinary-paragraph | medium] because the numerator involves the first derivatives of μ, while the denominator

[p0237-b0039 | ordinary-paragraph | medium] does not. Of course, here we cannot resort to the simple trick of § 2 which consists

[p0237-b0040 | ordinary-paragraph | medium] in writing that

[p0237-b0041 | ordinary-paragraph | low] Vu,e Mh,

[p0237-b0042 | equation | low] Iμnl1,o ≤ (C/h)ll μ, llo,α

[p0237-b0043 | ordinary-paragraph | medium] for this process is too crude. Instead, we propose to use a clever argument due

[p0237-b0044 | ordinary-paragraph | medium] to Scholz [72]. Roughly speaking, this author remarks that by choosing

[p0237-b0045 | equation | low] Φh = PnΦ,

[p0237-b0046 | ordinary-paragraph | medium] the projection of Φ onto Φ, then the expression (curl(Φ - Φh), curl μn) reduces to

[p0237-b0047 | ordinary-paragraph | medium] a sum of integrals taken only on boundary elements. Since these elements are

[p0237-b0048 | ordinary-paragraph | medium] few compared to the total number of elements in Q, a much sharper bound can

[p0237-b0049 | ordinary-paragraph | medium] be derived for this expression. The details are given in the next lemma.

## PDF 238 / printed 224



[p0238-b0003 | ordinary-paragraph | high] regular family of triangulations of Q. Let k be an integer and p areal number such

[p0238-b0004 | ordinary-paragraph | high] that 1<k<land2<p< ©. There exists a constant C > 0, independent of h,

[p0238-b0005 | ordinary-paragraph | high] such that for allf unctions 6 € W**!?(Q) H4(Q), we have:

[p0238-b0006 | equation | low] |(curl(¢ — F,), curl ,)|

[p0238-b0007 | ordinary-paragraph | high] (3.3) = Ch elya ne

[p0238-b0008 | ordinary-paragraph | high] une O), IlM n llo,2

[p0238-b0009 | proof | high] Proof. First, note that }, < Hj(Q) because Q is convex. Next, let yu, be an

[p0238-b0010 | ordinary-paragraph | high] arbitrary element of O, and let 1, denote the function of ®, which coincides with

[p0238-b0011 | ordinary-paragraph | high] u, at all interior finite element nodes. In particular, if 2, denotes the union of the

[p0238-b0012 | ordinary-paragraph | high] boundary elements of 7, then supp(, — 4,) < 2),. Therefore since

[p0238-b0013 | equation | low] (curl(¢ — F,9),curld,)=0 Vd,€D,,

[p0238-b0014 | ordinary-paragraph | high] this implies:

[p0238-b0015 | equation | low] (curl(¢— P,¢), curl 1,) oa curl(¢ — P,¢)-curl(, — A,) dx.

[p0238-b0016 | ordinary-paragraph | high] Hence by Holder’s inequality, we have:

[p0238-b0017 | ordinary-paragraph | high] (3.4) |(curl(é — P,g), curl 4,)| <1 6 — Pyblip.2,ln— Anla.ady>

[p0238-b0018 | ordinary-paragraph | high] where

[p0238-b0019 | equation | low] 1/p+1/qg=1, with p >2.

[p0238-b0020 | ordinary-paragraph | high] Now, (A.32) and the argument of Corollary A.3 yield:

[p0238-b0021 | equation | low] n= Anlioa, Zs < C,h*(meas(2,))"** ? || uy,— Anllo,z,-

[p0238-b0022 | ordinary-paragraph | high] On the one hand

[p0238-b0023 | equation | low] Le. — Anllo,5, <C, IlH n llo,s;,

[p0238-b0024 | ordinary-paragraph | high] because yu, — 4, vanishes on all interior nodes of Y, and reduces to yu, on all

[p0238-b0025 | ordinary-paragraph | high] boundary nodes. On the other hand,

[p0238-b0026 | equation | low] meas(2},) < C,hmeas(J).

[p0238-b0027 | ordinary-paragraph | high] Therefore,

[p0238-b0028 | equation | low] le = Palaver S Cale = ll Uillg, oe

[p0238-b0029 | ordinary-paragraph | high] When substituted into (3.4), this inequality gives:

[p0238-b0030 | equation | low] |(curl(¢— P,), curl 4,)| <C yh?-"?16 — B.A, pall Mallo,c

[p0238-b0031 | ordinary-paragraph | high] and the desired result follows from the estimate (A.26), whatever the value of k

[p0238-b0032 | ordinary-paragraph | high] since p > 2. La

[p0238-b0033 | remark | high] Remark 3.1. Let us denote

[p0238-b0034 | equation | low] c(g, Hy) = (curl(p — P,@), curl ty) Veewr?(Q), Vu, e,,

## PDF 239 / printed 225



[p0239-b0005 | equation | low] c(Φ,μn) =<Cn(Φ), μn>

[p0239-b0006 | ordinary-paragraph | medium] where C,e &(Wk+1. P(Q) N H(Q); O) for all integers ke [1, I] and

[p0239-b0007 | ordinary-paragraph | medium] Therefore by interpolating between two consecutive integral values of k, we

[p0239-b0008 | ordinary-paragraph | medium] derive from Theorem 1.1.4 that Che (Wk+1.P(Ω)N H(Q); O) for all real ke

[p0239-b0009 | ordinary-paragraph | medium] [1, I] and formula (1.1.10) permits to extend (3.3) to non integral k:

[p0239-b0010 | equation | low] (curl(o - PhΦ), curl μn)1

[p0239-b0011 | equation | low] ≤Chk-1/2-1/ / lk+1,p,2

[p0239-b0012 | equation | low] (3.5)

[p0239-b0013 | ordinary-paragraph | medium] Vreal ke [1, ].

[p0239-b0014 | equation | low] sup

[p0239-b0015 | ordinary-paragraph | low] Il μn llo, 2

[p0239-b0016 | ordinary-paragraph | medium] With these two lemmas, we are able to improve the approximation result

[p0239-b0017 | ordinary-paragraph | medium] in Vh.

[p0239-b0018 | lemma | medium] Lemma 3.3. Assume that Q and J, are like in Lemma 3.2. For each real ke [1, l]

[p0239-b0019 | ordinary-paragraph | medium] and real pe [2, o], there exists a constant C > 0, independent of h, such that all

[p0239-b0020 | ordinary-paragraph | medium] functions v = (curlΦ,0 = - AΦ)e V with Φe Wk+1,P(Q)N H(Q) satisfy:

[p0239-b0021 | ordinary-paragraph | low] u0340

[p0239-b0022 | ordinary-paragraph | low] WnEVh

[p0239-b0023 | equation | low] (3.6)

[p0239-b0024 | equation | low] inf 1lu - Wnllx≤ 2 31 - Phl1,s,α + inf 110 - 0nllo.2

[p0239-b0025 | ordinary-paragraph | low] OneOn

[p0239-b0026 | ordinary-paragraph | medium] WnEVn

[p0239-b0027 | ordinary-paragraph | low] + Chk-1/2-1/ l/ k+1,p,Ω.

[p0239-b0028 | ordinary-paragraph | medium] When Φe Hl+3/2(Ω) N Wl+1. ∞(Q) (and of course Φ/r = 0), the best estimate is:

[p0239-b0029 | equation | low] inf ↓u -whl

[p0239-b0030 | ordinary-paragraph | low] WhEVn

[p0239-b0031 | equation | low] ≤ Chl-1/2(1l ll1+3/2,8 + Il l+1, ∞0,2).

[p0239-b0032 | equation | low] (3.7)

[p0239-b0033 | equation | low] inf llu - Whllx

[p0239-b0034 | ordinary-paragraph | low] WnEVh

[p0239-b0035 | proof | medium] Proof. Recall that

[p0239-b0036 | equation | low] Il(curl Φ, 0)llx = I0l1,s,2 + 1l0 llo.o.

[p0239-b0037 | ordinary-paragraph | medium] Then, the inequality (3.6) is a direct consequence of Lemmas 3.1 and 3.2 together

[p0239-b0038 | ordinary-paragraph | medium] with Remark 3.1.

[p0239-b0039 | ordinary-paragraph | low] :s 0 = d pue 1 = y ym 7' euuT (o) ,1+M U (o)z/e+H >Φ l 1xN

[p0239-b0040 | equation | low] [(curl(b -— Phb), curl μn)]

[p0239-b0041 | equation | low] ≤ Ch'-1/2 I/ lli+1, ∞,.

[p0239-b0042 | equation | low] sup

[p0239-b0043 | ordinary-paragraph | low] Il μh ll o,2

[p0239-b0044 | ordinary-paragraph | low] uneOn

[p0239-b0045 | ordinary-paragraph | medium] Moreover, since Hl+3/2(Ω) c Wl+ 1/2.s(Ω) for all s < 0, an application of (A.26)

[p0239-b0046 | ordinary-paragraph | medium] yields:

[p0239-b0047 | equation | low] |Φ - PhΦl1,s,2 ≤ C2hl-1/2 // ll+1/2,s,2 ≤ C3ht-1/2 1/ llI+3/2,Q.

## PDF 240 / printed 226



[p0240-b0003 | ordinary-paragraph | high] that:

[p0240-b0004 | equation | low] inf ||0 — 6, loa <S C, a || Wl 1/72,2CS A ”? |b lli+s/2, Q:

[p0240-b0005 | ordinary-paragraph | high] OnE On,

[p0240-b0006 | ordinary-paragraph | high] Hence (3.7) stems from (3.6) and these three inequalities. fr

[p0240-b0007 | ordinary-paragraph | high] As an immediate consequence, we derive the following corollary by using a

[p0240-b0008 | ordinary-paragraph | high] simple and classical density argument.

[p0240-b0009 | corollary | high] Corollary 3.1. Under the assumptions of Lemma 3.2, we have for all ve V:

[p0240-b0010 | equation | low] lim inf ||v — w,|lz = 0.

[p0240-b0011 | equation | low] h>0 wy eV,

[p0240-b0012 | ordinary-paragraph | high] In addition, Lemma 3.3 implies a number of error estimates for the “stream

[p0240-b0013 | ordinary-paragraph | high] function-vorticity” method. First, let us consider the simplest case where the

[p0240-b0014 | ordinary-paragraph | high] solution of the Stokes problem has sufficient regularity.

[p0240-b0015 | theorem | high] Theorem 3.1. Let Q be a bounded, convex polygon and let 7, be a uniformly regular

[p0240-b0016 | ordinary-paragraph | high] family of triangulations of Q. Assume that the solution (u = curly, p) of the Stokes

[p0240-b0017 | ordinary-paragraph | high] problem (2.1) is such that we H***?(Q)N W**1:°(Q), pe H* 17(Q)N L2(Q) for

[p0240-b0018 | ordinary-paragraph | high] some real ke€[3/2,1]. Then the solution (u, = (curly, @,),p,) of Problem (2.29)

[p0240-b0019 | ordinary-paragraph | high] (2.36) satisfies the estimate:

[p0240-b0020 | ordinary-paragraph | high] (3.8) lu — walle< ChE PW llata2.0 + IW leet, 0,0):

[p0240-b0021 | ordinary-paragraph | high] (3.9) 1p — Pallosa <C oh* ? ([Pla-ta,0 + WW llaesy2,@ + WW lett, 0,0):

[p0240-b0022 | equation | low] When 1 <k < min(3/2,1) and ye W**"*(Q), AW and pe H'(Q) we have:

[p0240-b0023 | ordinary-paragraph | high] (3.10) lu — ule < C3(hAWl | y0 g + A? Whit, 0,0)

[p0240-b0024 | ordinary-paragraph | high] (3.11) IP — Pallo.a <C alP+ Wll4W|i1 9a + A |W llcat, 0a):

[p0240-b0025 | proof | high] Proof. Owing to (3.6), Remark 2.2 and Theorems 2.6 and 2.7 we get:

[p0240-b0026 | equation | low] Ju —u,| < Ci {|o — P,@ |lo,9 + hae IY Ile+t1,c0,ah5

[p0240-b0027 | ordinary-paragraph | high] |[u — uallz <C 2X{ ||o — P,@\lo,a + |W — Pouleeo ae he perme 3

[p0240-b0028 | ordinary-paragraph | high] |p — Pallo,e <C; \hn ts Gulia a |W ie,

[p0240-b0029 | ordinary-paragraph | high] Gn€ Qn

[p0240-b0030 | equation | low] + inf (]o — Ollo,g + hla — alah

[p0240-b0031 | ordinary-paragraph | high] 0,69,

[p0240-b0032 | ordinary-paragraph | high] Applying (A.26), this gives (3.8) and (3.9) or (3.10) and (3.11) according to the value

[p0240-b0033 | ordinary-paragraph | high] of k.

[p0240-b0034 | ordinary-paragraph | high] L]

## PDF 241 / printed 227



[p0241-b0005 | ordinary-paragraph | low] Ilp - Phllo,2 ≤ Ch-1/2(lpl-1/2,2 + Iy ll+3/2,α + II ll+1, ∞,2).

[p0241-b0006 | ordinary-paragraph | medium] When I = 1, y e W2.∞(Ω), 4y and pe H'(Q) the best estimate is:

[p0241-b0007 | equation | low] Ilu - u,llx ≤ Ch(↓4yl1, + h-1/2 l/y1l2,∞,2),

[p0241-b0008 | equation | low] Il p -- Pnllo,α ≤ Ch(lpl,2 + |4yl1,2 + h-1/ lly ll2, ∞,2).

[p0241-b0009 | ordinary-paragraph | low] o sis a () 1+ oi nou  ()z+ oi soq  uum 7'e y

[p0241-b0010 | theorem | medium] Theorem 3.1 are nearly valid. More precisely, by applying Lemma 3.2 with this

[p0241-b0011 | ordinary-paragraph | medium] k and arbitrary p ≥ 2 and using Sobolev's Imbedding Theorem 1.1.3 we can

[p0241-b0012 | ordinary-paragraph | medium] replace (3.6) by:

[p0241-b0013 | equation | low] inf I/u - wnllx≤Chk-1/2-1/Pl/llk+2,2 Vp≥ 2.

[p0241-b0014 | ordinary-paragraph | low] WhEVn

[p0241-b0015 | ordinary-paragraph | medium] Hence, by letting p tend to infinity, we see that for each ε > 0 there exists a

[p0241-b0016 | ordinary-paragraph | medium] constant C(e) > 0 such that

[p0241-b0017 | equation | low] inf Ilu - w llx ≤ C(e)hk-1/2- ll llk+2.Ω.

[p0241-b0018 | ordinary-paragraph | low] WnEVh

[p0241-b0019 | ordinary-paragraph | medium] In turn, this implies the estimate

[p0241-b0020 | equation | low] |u —un|1x≤ C(e)hk-1/2-/llk+2,2,

[p0241-b0021 | ordinary-paragraph | medium] with no restriction upon k or 4y as in this case 4y belongs to H*(Q) with k ≥ 1.

[p0241-b0022 | ordinary-paragraph | medium] Here again, a standard density argument establishes that the “stream function-

[p0241-b0023 | ordinary-paragraph | medium] vorticity" method is convergent.

[p0241-b0024 | corollary | medium] Corollary 3.2. Let Ω and J, be like in Theorem 3.1 and let the solution (u = curl Φ,

[p0241-b0025 | ordinary-paragraph | medium] p) of the Stokes problem (2.1) belong to H(Q)² x L3(Q). Then the solution (un, Ph)

[p0241-b0026 | ordinary-paragraph | medium] of Problem (2.29) (2.36) satisfies:

[p0241-b0027 | equation | low] lim(ll u -- u, llx + Ilp -- Pnllo.o) = 0.

[p0241-b0028 | ordinary-paragraph | medium] h→0

[p0241-b0029 | ordinary-paragraph | medium] When studying Navier-Stokes equations in Chapter IV, we shall encounter

[p0241-b0030 | ordinary-paragraph | medium] right-hand sides f with no better than L'-regularity, 1 < r ≤ 2. Now since Ω is

[p0241-b0031 | ordinary-paragraph | medium] assumed to be convex, the solution (y,w, p) of the Stokes problem belongs to

[p0241-b0032 | ordinary-paragraph | low] z(o)7 oi ssuoq 9pis puey-iya sh! aauym (o)a1M x (o)iM x (o)sgM

[p0241-b0033 | ordinary-paragraph | medium] In this case, we cannot apply directly (A.26) to evalute lw - Pho llo.o. Instead,

[p0241-b0034 | ordinary-paragraph | medium] we prove the following approximation result.

[p0241-b0035 | lemma | medium] Lemma 3.4. We retain the hypotheses of Theorem 3.1 on Q and Jh. Let 1 < q ≤ 2

[p0241-b0036 | ordinary-paragraph | medium] and 1/p + 1/q = 1. There exists a constant C > 0 independent of h, such that:

## PDF 242 / printed 228



[p0242-b0003 | ordinary-paragraph | high] where B = Oif 1 >2 and B =1—2/pifl=1.

[p0242-b0004 | proof | high] Proof. Let R,¢L(H'(Q);@,) be the local regularization operator defined by

[p0242-b0005 | ordinary-paragraph | high] (A.53) (A.54) and let us write:

[p0242-b0006 | equation | low] |v — Pyvllo,e< lv — Ryvilo,e + Rav — Pavilo,a-

[p0242-b0007 | ordinary-paragraph | high] As R,v — P,ve€@,, Lemma A.7 implies:

[p0242-b0008 | equation | low] | Rav — Pyvllo,g < Ch*-7!"|| Ryv — Prv|lo,g.a-

[p0242-b0009 | ordinary-paragraph | high] Hence

[p0242-b0010 | ordinary-paragraph | high] lv — P,vllo.e< lv — Ryvllo.g + Ch’ 74(l10 — Ryvllo,g.a + lv — Prvllo,aa).

[p0242-b0011 | ordinary-paragraph | high] Thus (3.12) is a straightforward consequence of Theorem A.4, Jensen’s inequality

[p0242-b0012 | ordinary-paragraph | high] (A.34) and (A.26) with a logarithmic factor if q < 2. al

[p0242-b0013 | ordinary-paragraph | high] This lemma enables us to extend Theorem 3.1.

[p0242-b0014 | theorem | high] Theorem 3.2. Let Q and 7%, be like in Theorem 3.1 and assume that the stream

[p0242-b0015 | ordinary-paragraph | high] function w belongs to W?:*(Q) and the pressure p to W':*(Q) with «e[r, 2). Let

[p0242-b0016 | ordinary-paragraph | high] B satisfy 1/a + 1/B = 1. We have the following estimates:

[p0242-b0017 | equation | low] h*?\W\3.0 ifl>2

[p0242-b0018 | ordinary-paragraph | high] (3.13) ume <4

[p0242-b0019 | equation | low] hv iWlisao0 fl=1,

[p0242-b0020 | ordinary-paragraph | high] Pei.

[p0242-b0021 | ordinary-paragraph | high] (3.14) IP — Palloe <

[p0242-b0022 | ordinary-paragraph | high] Co(Wls+. IP2li.@2.a ) hve

[p0242-b0023 | equation | low] if l=1,

[p0242-b0024 | ordinary-paragraph | high] with constants C, and C, independent of h, w and p.

[p0242-b0025 | proof | high] Proof. When | > 2 we can apply the material of Section 2.3. Indeed, the argu-

[p0242-b0026 | ordinary-paragraph | high] ments of Lemmas 2.10 and 2.11 can be readily extended to obtain:

[p0242-b0027 | equation | low] inf soG—N Gy S Gh" Olea store

[p0242-b0028 | ordinary-paragraph | high] 0,69),

[p0242-b0029 | equation | low] ee lw — brllon< Ci h7? lls 4,0 for1 > 2.

[p0242-b0030 | ordinary-paragraph | high] (Note that w belongs to H?(Q) because W*:*(Q) G H?(Q)). When substituted into

[p0242-b0031 | ordinary-paragraph | high] (2.66) these two bounds yield a somewhat sharper estimate than (3.13), namely:

[p0242-b0032 | ordinary-paragraph | high] (3.15) lo — Ollo+ InY — Wallan < C3h”?lWi3,4,0 for!> 2 .

[p0242-b0033 | ordinary-paragraph | high] In turn, (2.38) and (3.13) give immediately (3.14).

[p0242-b0034 | equation | low] When / = 1, we must resort to (2.30) and (3.6):

[p0242-b0035 | ordinary-paragraph | high] (3.16) lu — unllz < Cyt hl@n — P,@|lo,.9 + |W — Palen

[p0242-b0036 | ordinary-paragraph | high] +h "IW lest, pa}

## PDF 243 / printed 229



[p0243-b0005 | ordinary-paragraph | medium] bounded by:

[p0243-b0006 | equation | low] h1/2-1/ l!y ll2,p,α ≤ Csh1/B yll3,x,2.

[p0243-b0007 | ordinary-paragraph | medium] On the other hand, another application of Theorem 1.1.3 yields W3,α(Q) 

[p0243-b0008 | ordinary-paragraph | medium] W1+2/β,r(Ω) for all p > 0. Hence (A.26) gives in particular:

[p0243-b0009 | equation | low] [ - Pnyl,s,Q ≤ Cch2/B y 13,a,2.

[p0243-b0010 | ordinary-paragraph | medium] Finally, we infer from Lemma 3.4 that:

[p0243-b0011 | equation | low] 0 -- Ph@0 llo,2 ≤ Ch2/ |1n(h)1-2/B|@l1,a,2.

[p0243-b0012 | ordinary-paragraph | medium] Thus the dominating power of h in (3.16) is h1/e. This establishes (3.13). Then

[p0243-b0013 | ordinary-paragraph | medium] (3.14) follows again from (2.38).

[p0243-b0014 | ordinary-paragraph | low] 口

[p0243-b0015 | remark | medium] Remark 3.3. When α = 2, the statement of Theorem 3.2 is still valid for l = 2 but

[p0243-b0016 | ordinary-paragraph | medium] not for I = 1 because of the last term in (3.16). Instead, like in Remark 3.2 we

[p0243-b0017 | ordinary-paragraph | medium] obtain

[p0243-b0018 | ordinary-paragraph | low] [1yl13,2

[p0243-b0019 | ordinary-paragraph | low] llu -unllx

[p0243-b0020 | equation | low] ≤ C(e)h1/2-e

[p0243-b0021 | equation | low] Ve > 0.

[p0243-b0022 | ordinary-paragraph | low] IlIp -— Pnllo,Ω

[p0243-b0023 | ordinary-paragraph | low] [Ipl1,2 + Ilyl13,

[p0243-b0024 | ordinary-paragraph | medium] Finally, by using a familiar duality argument, the following theorem com-

[p0243-b0025 | ordinary-paragraph | medium] pletes the statement of Theorem 2.10 and establishes a nearly optimal upper

[p0243-b0026 | ordinary-paragraph | medium] bound for Iy - yhl1,o when l = 1.

[p0243-b0027 | theorem | medium] Theorem 3.3. Let Ω and J, be like in Theorem 3.1. Suppose the solution u = curl y

[p0243-b0028 | ordinary-paragraph | medium] of the Stokes problem (2.1) satisfies:

[p0243-b0029 | equation | low] ↓eHk+1(Ω) for 2≤k≤l or ΦeH²(Ω) if l = 1.

[p0243-b0030 | ordinary-paragraph | medium] Then the solution u, = (curl yh, wn) of Problem (2.29) satisfies the error estimate:

[p0243-b0031 | equation | low] [Chk|lk+1,2 if 2 ≤k ≤l,

[p0243-b0032 | equation | low] (3.17)

[p0243-b0033 | equation | low] -hl1,≤

[p0243-b0034 | equation | low] C(e)h1-llyll3,2 if l = 1,

[p0243-b0035 | ordinary-paragraph | medium] where & > O is arbitrary.

[p0243-b0036 | proof | medium] Proof. When I ≥ 2, the bound (3.17) is established by Theorem 2.10. When I = 1,

[p0243-b0037 | ordinary-paragraph | medium] we use a very similar duality argument. Thus, for each ge L?(Ω), the auxiliary

[p0243-b0038 | ordinary-paragraph | medium] Stokes problem:

[p0243-b0039 | equation | low] (curl Ag, curl x) = (g, curl x) xe H(Ω),

[p0243-b0040 | equation | low] (curl Φg, curl μ) = (g,μ) μ∈ H(S),

[p0243-b0041 | ordinary-paragraph | medium] has a unique solution Ag∈ H'(Q), Φ, e H3(Q)N H(Q) and

[p0243-b0042 | equation | low] IlΦgll3,o + I/ ag ll1,o ≤ C llgllo,2.

[p0243-b0043 | equation | low] (3.18)

## PDF 244 / printed 230



[p0244-b0004 | equation | low] ( -“ - ) +(( - )( - )) =((  )

[p0244-b0005 | equation | low] + (curl(Φg - Φn),curl(o - @n))

[p0244-b0006 | ordinary-paragraph | low] “"“A

[p0244-b0007 | ordinary-paragraph | low] WonEDn.

[p0244-b0008 | ordinary-paragraph | high] On the one hand, we can choose Z, = Ph^, in the first two terms:

[p0244-b0009 | ordinary-paragraph | low] (  " - m) + ( - ( -)

[p0244-b0010 | ordinary-paragraph | low] VxheΦh.

[p0244-b0011 | ordinary-paragraph | high] On the other hand, we can split the third term as follows:

[p0244-b0012 | equation | low] (curl(Φg -- Φn), curl(o - wn)) = (curl(Φg - Φn), curl(o - Ph@))

[p0244-b0013 | equation | low] + (curl(Φg -- Φn), curl(Pho - Wn).

[p0244-b0014 | ordinary-paragraph | high] But

[p0244-b0015 | equation | low] (curl Φg, curl(Ph0 -- Wn)) = (g, Ph∞ - Wn)

[p0244-b0016 | ordinary-paragraph | high] and according to (2.33) and (2.32) we have:

[p0244-b0017 | equation | low] (Ph∞ - Wn, On) = 0  V(curl on, On)∈ Vh,

[p0244-b0018 | ordinary-paragraph | low] VonePn.

[p0244-b0019 | equation | low] (curl(P∞ - wh), curl n) = 0

[p0244-b0020 | ordinary-paragraph | high] Therefore, collecting these equalities we obtain:

[p0244-b0021 | ordinary-paragraph | medium] (g, curl(y - yn) = (curl(2g - Ph^g),curl(y - xn)) + (∞ - @n, Phg - Ag)

[p0244-b0022 | equation | low] + (curl(Φg - Φn), curl(o - Ph@)

[p0244-b0023 | equation | low] (3.19)

[p0244-b0024 | ordinary-paragraph | low] + (g -- 0n, Ph∞ — Wn)

[p0244-b0025 | ordinary-paragraph | low] VXh, Phe Pn, V(curlon, On)e Vn.

[p0244-b0026 | ordinary-paragraph | high] As Φ, and y belong at least to H?(Q) we take

[p0244-b0027 | equation | low] Xn =Inl,Φh=IhΦg

[p0244-b0028 | ordinary-paragraph | high] Then

[p0244-b0029 | equation | low] (curl(g - Ph^g), curl(y - Iny)) ≤ C2h|Agl1,oly/2,,

[p0244-b0030 | equation | low] [(∞ - wn, Phng - Ag)1 ≤ C3h|wl1,s/2gl1.s

[p0244-b0031 | equation | low] [(curl(Φ, -- InΦg), curl(o - Pho)) ≤ C4h/Φg/2,olw/1,Ω,

[p0244-b0032 | equation | low] inf  I/ Ag - 0 llo,a ≤ Cs(e)h1/2- ll g ll ,2

[p0244-b0033 | ordinary-paragraph | low] (curlon, On) e Vh

[p0244-b0034 | ordinary-paragraph | high] according to Remark 3.2 and similarly Remark 3.3 gives:

[p0244-b0035 | equation | low]  Ph@ - @n lo,α ≤ C6(e)h1/2-|@l1.2

[p0244-b0036 | equation | low] V > 0.

[p0244-b0037 | ordinary-paragraph | high] By substituting these estimates into (3.19) and applying (3.18) we find (3.17). 

## PDF 245 / printed 231



[p0245-b0004 | ordinary-paragraph | medium] In this section, we propose to study again the expression

[p0245-b0005 | equation | low] (curl(Φ - Φh), curl μn)/

[p0245-b0006 | equation | low] inf   sup

[p0245-b0007 | ordinary-paragraph | low] II μh llo,.2

[p0245-b0008 | ordinary-paragraph | low] ΦnEΦh μneOn

[p0245-b0009 | ordinary-paragraph | medium] and show that it is of the order of h', for Φ in H'+2(Ω), provided that the

[p0245-b0010 | ordinary-paragraph | medium] triangulation , has a favorable configuration. Essentially, this will be achieved

[p0245-b0011 | ordinary-paragraph | medium] by choosing the function Φ, as a suitable interpolate of Φ.

[p0245-b0012 | ordinary-paragraph | medium] To begin with, we assume that J, is composed exclusively of convex quadri-

[p0245-b0013 | ordinary-paragraph | medium] laterals and we refer to Section A.2 for the notations and approximation results

[p0245-b0014 | ordinary-paragraph | medium] pertaining to quadrilaterals. Let us fix an integer I > 1 and let

[p0245-b0015 | equation | low] 0 = αo <α <·: <α-1 <α = 1

[p0245-b0016 | ordinary-paragraph | medium] be I + 1 distinct points of the interval [0, 1]. Here, we denote by Ie &(e°(k); Q)

[p0245-b0017 | ordinary-paragraph | medium] the standard interpolation operator at the (l + 1)² points

[p0245-b0018 | equation | low] {(a;aj); 0 ≤i,j ≤1}

[p0245-b0019 | ordinary-paragraph | medium] of the reference unit square k. The following technical result gives a first approxi-

[p0245-b0020 | ordinary-paragraph | medium] mation of the difference Φ - IΦ.

[p0245-b0021 | lemma | medium] Lemma 3.5. Let Re E(Hl+1(k); Pi+1) be defined by:

[p0245-b0022 | ordinary-paragraph | low] (x; - αk).

[p0245-b0023 | ordinary-paragraph | low] (al+1 $/ax;+1)dx

[p0245-b0024 | equation | low] R(Φ) = [1/(l + 1)!] ≥

[p0245-b0025 | equation | low] k=0

[p0245-b0026 | ordinary-paragraph | medium] Then, for each integer m with 0 ≤ m ≤ l + 2, there exists a positive constant C

[p0245-b0027 | ordinary-paragraph | medium] depending only upon k, I, R, m and l, such that

[p0245-b0028 | ordinary-paragraph | low] oe Hl+2(k).

[p0245-b0029 | equation | low] -1-R()1mx ≤ ClΦl+2,x

[p0245-b0030 | equation | low] (3.20)

[p0245-b0031 | proof | medium] Proof. Suppose first that Φe el+1(t). Recall that the interpolation operator I has

[p0245-b0032 | ordinary-paragraph | medium] the expression

[p0245-b0033 | equation | low] (x,x2) =∑Lk(x1) ∑ L;(x2)(αkα)

[p0245-b0034 | equation | low] k=0

[p0245-b0035 | equation | low] j=0

[p0245-b0036 | ordinary-paragraph | medium] where Ls e P, is the polynomial of one variable such that:

[p0245-b0037 | equation | low] L;(aj) = ou，  0 ≤i,j ≤l.

[p0245-b0038 | ordinary-paragraph | medium] The well-known remainder formula for the interpolation error gives on the one

[p0245-b0039 | ordinary-paragraph | medium] hand:

[p0245-b0040 | ordinary-paragraph | low] ∑ L;(x2)(αk,α;) + [1/(l + 1)!][a+1 (αx, μx)/x+1]  (x2 - αp),

[p0245-b0041 | ordinary-paragraph | low] f(ak,x2)=

[p0245-b0042 | equation | low] p=0

[p0245-b0043 | equation | low] =0

[p0245-b0044 | ordinary-paragraph | medium] and on the other hand,

[p0245-b0045 | ordinary-paragraph | low] (x1,x2) = ∑ Lx(x1)(α,x2) + [1/(l + 1)!][a+16(v,x2)/x}+1] I(x, - αp)

[p0245-b0046 | equation | low] p=0

[p0245-b0047 | equation | low] k=0

## PDF 246 / printed 232



[p0246-b0004 | ordinary-paragraph | medium] points (α, α,). Thus we can write:

[p0246-b0005 | ordinary-paragraph | low] Lk(x)+1(akμ)/x+

[p0246-b0006 | ordinary-paragraph | low] [ (x - αp)

[p0246-b0007 | ordinary-paragraph | medium] (Φ - 16)(x,x2) = [1/(l + 1)]

[p0246-b0008 | equation | low] p=0

[p0246-b0009 | ordinary-paragraph | low] + ol+1$(v,x2)/axi+1 II (x, - αp)

[p0246-b0010 | equation | low] p=0

[p0246-b0011 | ordinary-paragraph | medium] By comparing the right-hand side of this expression with R(Φ), and using the fact

[p0246-b0012 | ordinary-paragraph | medium] that

[p0246-b0013 | equation | low] ∑ L(x) = 1 on [0, 1],

[p0246-b0014 | equation | low] k=0

[p0246-b0015 | ordinary-paragraph | medium] we readily derive that the mapping Φ →Φ - Iβ - R(Φ) vanishes on Pi+1. Since

[p0246-b0016 | ordinary-paragraph | medium] this mapping belongs to (Hl+2(k); H'+2(k)), (3.20) follows from Corollary A.1.

[p0246-b0017 | ordinary-paragraph | low] 口

[p0246-b0018 | ordinary-paragraph | medium] The next result is obtained by a simple rearrangement of terms.

[p0246-b0019 | lemma | medium] Lemma 3.6. The following identity holds for all Φ and μe H'(k):

[p0246-b0020 | ordinary-paragraph | low] (1/J)[1l0F/0x11²(0/0x,)(p/x)

[p0246-b0021 | equation | low] grad Φ· grad μ dx =

[p0246-b0022 | ordinary-paragraph | low] Jk

[p0246-b0023 | ordinary-paragraph | low] K

[p0246-b0024 | ordinary-paragraph | low] + 11oFx/ax, 11²(a/0x2)(op/ax2)]dx

[p0246-b0025 | equation | low] (3.21)

[p0246-b0026 | ordinary-paragraph | low] (1/J)(0F/0x)·(0F/0x2)[(0/x)(0p/0x2)

[p0246-b0027 | ordinary-paragraph | low] + (o$/0x2)(0p/ox,)]dx,

[p0246-b0028 | ordinary-paragraph | medium] where Il. I/ denotes the Euclidean norm of R? and Jp the Jacobian of the bilinear

[p0246-b0029 | ordinary-paragraph | medium] mapping Fx.

[p0246-b0030 | ordinary-paragraph | medium] In order to evaluate properly the right-hand side of (3.21), it is convenient to shift

[p0246-b0031 | ordinary-paragraph | medium] out of the integrals the factors involving JF and dF,/ex,. As these two quantities

[p0246-b0032 | ordinary-paragraph | medium] are not constant, we must therefore assume that their derivatives are "small". To

[p0246-b0033 | ordinary-paragraph | medium] be specific, we make the following hypothesis:

[p0246-b0034 | ordinary-paragraph | medium] there exists a constant C > O, independent of h and k, such that

[p0246-b0035 | equation | low] (3.22)

[p0246-b0036 | ordinary-paragraph | low] Vke Ih.

[p0246-b0037 | equation | low] 10² F/0x,0x2 11 ≤ Ch2

[p0246-b0038 | ordinary-paragraph | medium] Note that 02 F,/0x, 0x2 = 0 when k is a parallelogram; in fact, (3.22) holds only

[p0246-b0039 | ordinary-paragraph | medium] if k is almost a parallelogram. It easy to prove that when (3.22) holds, the full

[p0246-b0040 | ordinary-paragraph | medium] seminorm I.lx, and [.]k,x (cf. formula (A.41)) have upper bounds of the same

[p0246-b0041 | ordinary-paragraph | medium] order. More precisely, we have:

[p0246-b0042 | lemma | medium] Lemma 3.7. Let k be a convex quadrilateral that satisfies (3.22). Then for each

[p0246-b0043 | ordinary-paragraph | medium] integer k ≥ 1 there exists a constant C > 0, independent of h and k, such that:

## PDF 247 / printed 233



[p0247-b0007 | equation | low] =1

[p0247-b0008 | ordinary-paragraph | medium] Moreover there exists a constant C > O, independent of h and k, such that:

[p0247-b0009 | equation | low] 0[(1/J)(0F,/0x;)·(0F /0x;)]/0x ll0, ∞,x ≤ Co2 h,(1 + o2)

[p0247-b0010 | equation | low] (3.24)

[p0247-b0011 | ordinary-paragraph | medium] 1 ≤i,j,k≤ 2.

[p0247-b0012 | ordinary-paragraph | medium] As a consequence, if the triangulation , is regular, it follows that (3.24)

[p0247-b0013 | ordinary-paragraph | medium] implies:

[p0247-b0014 | ordinary-paragraph | medium] [(1/JF)(0F/0x;)·(0F/0x;)](x,,x2) = [(1/JF)(0F/0x;)·(oF/0x;)](1/2, 1/2) + R

[p0247-b0015 | ordinary-paragraph | medium] where the remainder R, is bounded by:

[p0247-b0016 | equation | low] [RxI ≤ Ch.

[p0247-b0017 | ordinary-paragraph | medium] Since we are specifically interested in recovering one power of h, we can neglect

[p0247-b0018 | ordinary-paragraph | medium] that remainder and it follows from (3.21) and (3.24) that the study of the expression

[p0247-b0019 | equation | low] curl(b - Φh) · curl μ, dx

[p0247-b0020 | ordinary-paragraph | low] KC

[p0247-b0021 | ordinary-paragraph | medium] reduces for us to that of the four terms

[p0247-b0022 | equation | low] [0(Φ -Φn)/ax;][oa/ox;] dx,  1 ≤i,j ≤ 2.

[p0247-b0023 | equation | low] (3.25)

[p0247-b0024 | ordinary-paragraph | medium] Furthermore, if we choose Φ, = IhΦ, where I, is the interpolation operator on K

[p0247-b0025 | ordinary-paragraph | medium] corresponding to I, then according to Lemma 3.5, f [0(Φ - fΦ)/ax;] [op/ox;] dx

[p0247-b0026 | ordinary-paragraph | medium] involves in particular factors of the form

[p0247-b0027 | ordinary-paragraph | low] d(w;)/0x;0p/0x;dx

[p0247-b0028 | equation | low] W = II (x;-αp).

[p0247-b0029 | ordinary-paragraph | medium] where

[p0247-b0030 | equation | low] 1>d>0

[p0247-b0031 | ordinary-paragraph | medium] Now, if the points α coincide with the nodes of a highly precise quadrature

[p0247-b0032 | ordinary-paragraph | medium] formula, this last integral will possibly vanish. This remark induces us to choose

[p0247-b0033 | ordinary-paragraph | medium] for the set {αk} the I + 1 nodes of the Gauss-Lobatto quadrature formula on [O, 1].

[p0247-b0034 | ordinary-paragraph | medium] Recall that this formula is exact for polynomials of degree 2l - 1. Then we have

[p0247-b0035 | ordinary-paragraph | medium] the following lemma.

[p0247-b0036 | lemma | medium] Lemma 3.8. Let k be like in Lemma 3.7 and let {αk}o<k<t be the I + 1 nodes of the

[p0247-b0037 | ordinary-paragraph | medium] Gauss-Lobatto quadrature formula. Then there exists a constant C > O, indepen-

[p0247-b0038 | ordinary-paragraph | medium] dent of h and r, such that:

[p0247-b0039 | equation | low] [0($ - I)/ox;] [op/0x;]dx ≤ Cohk ll+2.x ll μn llo,x

[p0247-b0040 | equation | low] (3.26)

[p0247-b0041 | ordinary-paragraph | low] Jk

[p0247-b0042 | ordinary-paragraph | medium] ()+HΦA

[p0247-b0043 | equation | low] i= 1,2, Vμn∈Oh, 

## PDF 248 / printed 234



[p0248-b0003 | ordinary-paragraph | high] |[ ag — 1)/6X;] Le A/o%,] ax

[p0248-b0004 | equation | low] =[1/l+ 4 | a't4 gait as| (2a (08 (08/08, 48 + E;

[p0248-b0005 | ordinary-paragraph | high] where the remainder term E; is bounded by

[p0248-b0006 | ordinary-paragraph | high] JEL < Cilblis2,0lAls.e < ColPlis2.e llA llo.

[p0248-b0007 | equation | low] < C302 NG lli+2,Ha«lllo .

[p0248-b0008 | ordinary-paragraph | high] by virtue of (3.23) and (A.45).

[p0248-b0009 | ordinary-paragraph | high] Now, a simple integration by parts shows that

[p0248-b0010 | equation | low] |(60; /0%;) (Of /0X;) dx = 0

[p0248-b0011 | ordinary-paragraph | high] because w,/; vanishes on the boundary of k (f; is the i'"-component of the normal

[p0248-b0012 | ordinary-paragraph | high] fi to kX) and the integrand w;0? f/0X? is a polynomial of Q,,_, which vanishes on

[p0248-b0013 | ordinary-paragraph | high] the set {«,}. This proves (3.26). O

[p0248-b0014 | ordinary-paragraph | high] This lemma takes care of the first two terms in (3.25). But the third and fourth

[p0248-b0015 | ordinary-paragraph | high] terms which involve

[p0248-b0016 | ordinary-paragraph | high] [a(¢ — 16)/0x,] [on/0x,]

[p0248-b0017 | ordinary-paragraph | high] with i #j are not so amenable, as can be seen by inspecting R(@). Indeed, the

[p0248-b0018 | ordinary-paragraph | high] argument of Lemma 3.8 leads to the integral of polynomials of Q,,, whereas the

[p0248-b0019 | ordinary-paragraph | high] Gauss-Lobatto formula is only exact for polynomials of degree 2] — 1. So the

[p0248-b0020 | ordinary-paragraph | high] particular choice of points {«,} is of no avail here.

[p0248-b0021 | ordinary-paragraph | high] Let us examine closely fi [a(¢ — 14)/0X;] [6 f1/0x; ]d X. To get rid of the deriva-

[p0248-b0022 | ordinary-paragraph | high] tive of f we integrate by parts with respect to X;. Applying again Lemma 3.5 and

[p0248-b0023 | ordinary-paragraph | high] using the fact that

[p0248-b0024 | equation | low] 6? R(g)/0%,0%; =0 fori ¥j

[p0248-b0025 | ordinary-paragraph | high] we obtain:

[p0248-b0026 | equation | low] |[ 0(¢ — 16)/0X,] [6n/0%,] dx = | [0(¢ — 19)/0x,]A,ads + E,

[p0248-b0027 | ordinary-paragraph | high] k an

[p0248-b0028 | ordinary-paragraph | high] where

[p0248-b0029 | ordinary-paragraph | high] (3.27) |E;| < C,o2 he ||6 lle+2.n llM allosr:

[p0248-b0030 | ordinary-paragraph | high] But for i#j, the inverse image on x of [d(¢ — T$)/0x;]n,A is continuous

[p0248-b0031 | ordinary-paragraph | high] (but with opposite signs) across interelement boundaries and vanishes on I. In

[p0248-b0032 | ordinary-paragraph | high] addition, Theorem A.3 and Lemma A.9 give only:

## PDF 249 / printed 235



[p0249-b0005 | ordinary-paragraph | low] Jok

[p0249-b0006 | equation | low] ≤ C3o2h-1 IΦl+1.xllμh llo,x

[p0249-b0007 | ordinary-paragraph | medium] Hence, in order to sharpen this estimate, we must first sum these terms over all

[p0249-b0008 | ordinary-paragraph | medium] elements k of J, and next evaluate their contribution on a given interelement

[p0249-b0009 | ordinary-paragraph | medium] boundary. Thus a better estimate can only be attained if the difference in the

[p0249-b0010 | ordinary-paragraph | medium] factor

[p0249-b0011 | equation | low] X =(1/J)(0F/0x)(0F/0x2)

[p0249-b0012 | ordinary-paragraph | medium] arising from two adjacent elements is "small'.

[p0249-b0013 | ordinary-paragraph | medium] To evaluate this difference, let k, and k2 denote two adjacent elements of h.

[p0249-b0014 | ordinary-paragraph | medium] First we remark that, in view of (3.24), it suffices to estimate the difference

[p0249-b0015 | ordinary-paragraph | medium] Xx,(a,b1) -Xx(a2,b2)

[p0249-b0016 | ordinary-paragraph | medium] where (a, b;) is an arbitrary point of k,. The simplest choice is to pick a convenient

[p0249-b0017 | ordinary-paragraph | medium] point (a, b) on the interface k' between k1 and k2 and to set

[p0249-b0018 | equation | low] (a1,b1) = (a2,b2) = (a,b).

[p0249-b0019 | ordinary-paragraph | medium] K

[p0249-b0020 | ordinary-paragraph | medium] K

[p0249-b0021 | ordinary-paragraph | medium] K2

[p0249-b0022 | ordinary-paragraph | medium] K

[p0249-b0023 | ordinary-paragraph | medium] (a,b)

[p0249-b0024 | ordinary-paragraph | medium] L1

[p0249-b0025 | ordinary-paragraph | medium] K2

[p0249-b0026 | ordinary-paragraph | medium] (a.b)

[p0249-b0027 | figure | medium] Figure 20

[p0249-b0028 | ordinary-paragraph | medium] Let i be the index such that aF,/ox; is continuous across the interface k'. Then a

[p0249-b0029 | ordinary-paragraph | medium] straightforward calculation shows that

[p0249-b0030 | ordinary-paragraph | low] [JF, JF(Xx, - Xx)(a,b)1 = 110F(a,b)/0x;11 Il(aFx,/ox;) × (0F /x;)(a, b)

[p0249-b0031 | ordinary-paragraph | medium] where j ≠ i. Now, let us choose for (a, b) one of the end points of k' and let

[p0249-b0032 | ordinary-paragraph | medium] L, and L2 denote the sides of k, and k2 (other than k') that meet at (a, b) (cf.

[p0249-b0033 | figure | medium] Figure 20). It easy to see that

[p0249-b0034 | ordinary-paragraph | medium] (3.29)  (JF, JF,(Xx, - Xk)(a,b)| = meas²(k')meas(L) meas(L2)It, : n2| 

## PDF 250 / printed 236



[p0250-b0003 | ordinary-paragraph | high] Therefore, the difference X,, — X,, is O(h) if t, -m, is also O(h); in other words if

[p0250-b0004 | ordinary-paragraph | high] L, and L, are nearly parallel. Thus with the notations of Figure 20, we make the

[p0250-b0005 | ordinary-paragraph | high] following hypothesis:

[p0250-b0006 | ordinary-paragraph | high] there exists a constant C > 0, independent of h, such that

[p0250-b0007 | ordinary-paragraph | high] (3.30) (ony) — Cr

[p0250-b0008 | ordinary-paragraph | high] for all pairs of adjacent segments L, and L, of Jj.

[p0250-b0009 | ordinary-paragraph | high] This hypothesis means that a mesh 7%, that satisfies (3.22) as well as (3.30) is

[p0250-b0010 | ordinary-paragraph | high] obtained by slightly distorting two pencils of parallel lines. Of course it is a very

[p0250-b0011 | ordinary-paragraph | high] stringent condition on the mesh and only few domains Q lend themselves readily

[p0250-b0012 | ordinary-paragraph | high] to such a triangulation. Albeit so, with (3.30) we derive the result announced at

[p0250-b0013 | ordinary-paragraph | high] the beginning of this section. First, we infer the next lemma from the above

[p0250-b0014 | ordinary-paragraph | high] considerations.

[p0250-b0015 | lemma | high] Lemma 3.9. Let Q be a bounded polygon and let 7, be a regular triangulation of

[p0250-b0016 | ordinary-paragraph | high] Q made of convex quadrilaterals satisfying (3.22) and (3.30). Then there exists a

[p0250-b0017 | ordinary-paragraph | high] constant C > 0, independent of h, such that:

[p0250-b0018 | equation | low] Be |X L6G — 16)/08,1 [60/08;] d&| < Ch'||blli+2,0ll Hallo,

[p0250-b0019 | ordinary-paragraph | high] Gaiters

[p0250-b0020 | ordinary-paragraph | high] ifxj.- VéeeH *7(2), | Vipeee

[p0250-b0021 | ordinary-paragraph | high] Then, using Lemmas 3.6 to 3.9 we can prove the following theorem.

[p0250-b0022 | theorem | high] Theorem 3.4. Let Q and 7%, be like in Lemma 3.9 and let I, be the interpolation

[p0250-b0023 | ordinary-paragraph | high] operator on x corresponding to I:

[p0250-b0024 | equation | low] (,¢)0F, =1(@oF.) oneachx,

[p0250-b0025 | ordinary-paragraph | high] where Ie £(6°(K); Q,) is the standard interpolation operator at the (I + 1)? Gauss-

[p0250-b0026 | ordinary-paragraph | high] Lobatto quadrature nodes. Then there exists a constant C > 0, independent of h,

[p0250-b0027 | ordinary-paragraph | high] such that the following bound holds for all ¢ in H'*?(Q):

[p0250-b0028 | ordinary-paragraph | high] (3.32) \(curl(¢ — I), curl y,)| < Ch'||$llis2,a-

[p0250-b0029 | ordinary-paragraph | high] Hpe 9, IlH n llo.e

[p0250-b0030 | ordinary-paragraph | high] With the material of the preceding section, we immediately derive the following

[p0250-b0031 | ordinary-paragraph | high] consequence of Theorem 3.4.

[p0250-b0032 | corollary | high] Corollary 3.3. Under the assumptions of Theorem 3.4, there exists a constant

[p0250-b0033 | ordinary-paragraph | high] C > 0, independent of h, such that:

[p0250-b0034 | equation | low] inf ||v— val<l Ceh !

[p0250-b0035 | ordinary-paragraph | high] lli+2.e

[p0250-b0036 | ordinary-paragraph | high] eVe h l¥ IP

[p0250-b0037 | ordinary-paragraph | high] (3.33) my

[p0250-b0038 | ordinary-paragraph | high] Vu = (curl ¢,0)eEV_ with 6c H'*?(Q).
