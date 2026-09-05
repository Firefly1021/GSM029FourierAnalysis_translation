# Restored-source review candidate: chapter-04-section-06



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 366 / printed 352



[p0366-b0003 | ordinary-paragraph | high] qn€ Qn

[p0366-b0004 | ordinary-paragraph | high] (5.53) +yv inf (lo — 4,llo,9 + h?!"|c o— 01,10)

[p0366-b0005 | ordinary-paragraph | high] 6,69,

[p0366-b0006 | ordinary-paragraph | high] +h?T h — Vila Wali.a.0 + hah

[p0366-b0007 | ordinary-paragraph | high] where 1/y + 1/t =1, u, = (u, = curly,,@,) and u =(u=curly,q@) denote the

[p0366-b0008 | ordinary-paragraph | high] solutions of (5.18) and (5.7) respectively.

[p0366-b0009 | ordinary-paragraph | high] It follows readily from (5.53) and (5.48) that the pressure p, has the same order

[p0366-b0010 | ordinary-paragraph | high] of convergence as the velocity:

[p0366-b0011 | theorem | high] Theorem 5.3. Under the assumptions of Theorem 5.1 the pressure p, defined by

[p0366-b0012 | ordinary-paragraph | high] Problem (5.51) converges to p with the same order of accuracy as the velocity.

[p0366-b0013 | ordinary-paragraph | high] Namely, if fe L'(Q)? for te[r, 2) we have:

[p0366-b0014 | equation | low] l/y ifl=1,

[p0366-b0015 | equation | low] Sup PA) — PalA)llooa< Cih® a= {

[p0366-b0016 | equation | low] 2/y if l=2,

[p0366-b0017 | ordinary-paragraph | high] where 1/y + 1/t = 1. When w belongs to W”’”(Q) or when | > 2, this bound can

[p0366-b0018 | ordinary-paragraph | high] be extended to t = 2. When 1 = 1 and t = 2 we have:

[p0366-b0019 | equation | low] sup IPA) — PalA)llo,a < Co(eht™*.

[p0366-b0020 | ordinary-paragraph | high] Finally when the mapping A > (W(A), p(A)) is continuous from A into

[p0366-b0021 | ordinary-paragraph | high] [H™*?(Q)

[p0366-b0022 | ordinary-paragraph | high] wm*si2,°(Q)] x H™(Q) for some real me [1,1 — 1/2] we have

[p0366-b0023 | equation | low] a |D (A) — palA)llo,.g < C3h”™.

[p0366-b0024 | section | high] §6. Numerical Algorithms

[p0366-b0025 | ordinary-paragraph | high] Navier-Stokes equations are difficult to solve in practice because they are non-

[p0366-b0026 | ordinary-paragraph | high] linear. We present here a few simple converging algorithms that permit to handle

[p0366-b0027 | ordinary-paragraph | high] the nonlinearity. Although they are intended to solve the discrete systems of

[p0366-b0028 | ordinary-paragraph | high] (nonlinear) equations, it is simpler to introduce these algorithms in connection

[p0366-b0029 | ordinary-paragraph | high] with the continuous problem. The reader will verify easily that the convergence

[p0366-b0030 | ordinary-paragraph | high] theorems below are also valid for the approximate problems.

[p0366-b0031 | subsection | high] 6.1. General Methods of Descent and Application to Gradient Methods

[p0366-b0032 | ordinary-paragraph | high] Like every nonlinear problem, the Navier-Stokes equations can be put into the

[p0366-b0033 | ordinary-paragraph | high] framework of an optimization problem. Therefore we shall consider first the

## PDF 367 / printed 353



[p0367-b0003 | ordinary-paragraph | high] X. Let ||.||y and (.,.), denote respectively the norm and associated scalar

[p0367-b0004 | ordinary-paragraph | high] product ofX and let J be a @*-mapping from _X into R. We propose to minimize

[p0367-b0005 | ordinary-paragraph | high] J over an adequate subset D of X, chosen as follows. First, since we are only

[p0367-b0006 | ordinary-paragraph | high] interested in a minimum of J we restrict the discussion to the set

[p0367-b0007 | equation | low] {vX;e J( v) < Cy}

[p0367-b0008 | ordinary-paragraph | high] for some constant Cy; of course, we suppose that this set is not empty and we

[p0367-b0009 | ordinary-paragraph | high] take for D one of its connected components. In other words, D is a non empty

[p0367-b0010 | ordinary-paragraph | high] connected component of:

[p0367-b0011 | ordinary-paragraph | high] (6.1) {veX ; J(v)< Co}.

[p0367-b0012 | ordinary-paragraph | high] Now, we assume that the functional J is strictly convex in D, namely:

[p0367-b0013 | ordinary-paragraph | high] there exist two constants « > 0 and M > 0 such that all v in D satisfy

[p0367-b0014 | ordinary-paragraph | high] (6.2) al|wilx < D°J(v)-(<w ,Mlwlw)i y Vwex.

[p0367-b0015 | ordinary-paragraph | high] Then it is well known that the problem

[p0367-b0016 | ordinary-paragraph | high] (6.3) inf J(v)

[p0367-b0017 | ordinary-paragraph | high] veD

[p0367-b0018 | ordinary-paragraph | high] has a unique solution u in D characterized by

[p0367-b0019 | ordinary-paragraph | high] (6.4) DJ(u) = 0.

[p0367-b0020 | ordinary-paragraph | high] As usual, we associate with DJ the gradient g defined by:

[p0367-b0021 | equation | low] (g(v), W)x = <DJ(v),w> VweX,

[p0367-b0022 | ordinary-paragraph | high] where <., .> denotes the duality pairing X and X’.

[p0367-b0023 | ordinary-paragraph | high] To solve Problem (6.3) we introduce the following general method of descent

[p0367-b0024 | ordinary-paragraph | high] starting from u° € D:

[p0367-b0025 | ordinary-paragraph | high] i 1°) for all m > 0, choose a direction of descent we X and define pe R, by

[p0367-b0026 | ordinary-paragraph | high] (6.5) J(u" — p™w™)= inf J(u" — pw”),

[p0367-b0027 | ordinary-paragraph | high] p20

[p0367-b0028 | ordinary-paragraph | high] u™—pwMeD

[p0367-b0029 | ordinary-paragraph | high] 2°) set

[p0367-b0030 | ordinary-paragraph | high] (6.6) = Uo we D:

[p0367-b0031 | ordinary-paragraph | high] As shown below, this algorithm converges under reasonable assumptions.

[p0367-b0032 | theorem | high] Theorem 6.1. Let D be a non empty, connected subset of X satisfying (6.1) and

[p0367-b0033 | ordinary-paragraph | high] let J satisfy (6.2) in D. If, for each m, the direction of descent we X is such

[p0367-b0034 | ordinary-paragraph | high] that

[p0367-b0035 | ordinary-paragraph | high] (6.7) (g(u™),w™)x = Bilgu™)|lwl"x l x

[p0367-b0036 | ordinary-paragraph | high] for some constant B > 0 independent of m, then the algorithm of descent (6.5) (6.6)

## PDF 368 / printed 354



[p0368-b0003 | ordinary-paragraph | high] we have for all v, and v, in D:

[p0368-b0004 | equation | low] J(Ov, + (1 — O)v2) < OJ(v,;) + (1 — AJ(v,) Ve, 1]

[p0368-b0005 | equation | low] <C,_ by virtue of (6.1).

[p0368-b0006 | ordinary-paragraph | high] Since D is connected, this means that 0v, + (1 — 0)v,€D.

[p0368-b0007 | ordinary-paragraph | high] Next, we set

[p0368-b0008 | equation | low] D’ = {veD; J(v) < J(u°)}

[p0368-b0009 | ordinary-paragraph | high] and we assume that the starting value u° is not the solution of (6.3) (otherwise

[p0368-b0010 | ordinary-paragraph | high] the algorithm of descent yields the constant value u™ = u°). Again, D’ is convex

[p0368-b0011 | ordinary-paragraph | high] and because J is continuous, D’ is obviously a closed subset of X. Let us establish

[p0368-b0012 | ordinary-paragraph | high] that D’ is bounded. Taylor’s formula gives:

[p0368-b0013 | ordinary-paragraph | high] J(v) = J(u®) + <DJ(u°), v— u°> + (1/2)D?J(u® + t(v — u°))-(v — u®, v— u°)

[p0368-b0014 | ordinary-paragraph | high] for some t €(0, 1). To simplify, we denote

[p0368-b0015 | equation | low] g™ = g(u™).

[p0368-b0016 | ordinary-paragraph | high] Then, for all v in D’, the convexity of D’ and (6.2) imply

[p0368-b0017 | ordinary-paragraph | high] (6.8) J(v) > J(u°) — Ig? lixlle — lly + (@/2) lo — uli.

[p0368-b0018 | ordinary-paragraph | high] But since J(v) < J(u°) this yields:

[p0368-b0019 | equation | low] J(u) > J(u?) — Ig? Ixlle — uly + (@/2) lo — uP Ix:

[p0368-b0020 | ordinary-paragraph | high] in other words:

[p0368-b0021 | ordinary-paragraph | high] (6.9) lv — u? lly < (2/x) 19° lly.

[p0368-b0022 | ordinary-paragraph | high] This proves the boundedness of D’.

[p0368-b0023 | ordinary-paragraph | high] Observe also that J is bounded below in D’ because (6.8) and (6.9) imply

[p0368-b0024 | ordinary-paragraph | high] (6.10) J(v) > J(u) — (2/a) lg? Ilz-

[p0368-b0025 | ordinary-paragraph | high] Now we remark that the equation (6.5) defines a unique p™ > 0 for each pair

[p0368-b0026 | ordinary-paragraph | high] u™ and w™ satisfying (6.7). Indeed, since by construction u”™ belongs to the interior

[p0368-b0027 | ordinary-paragraph | high] of D, the mapping p > J(u” — pw") is strictly convex for all p such that u™ —

[p0368-b0028 | ordinary-paragraph | high] pw™eD . Hence J(u™ — pw") has a unique minimum in D and this minimum is

[p0368-b0029 | ordinary-paragraph | high] realized by a unique interior element of D, u" — p™w”™, with p™ > 0. Therefore

[p0368-b0030 | ordinary-paragraph | high] u™ — p™w™ is characterized by:

[p0368-b0031 | equation | low] [dJ(u™ — pw™)/dp)| _ im = —<{DJ(u™ — p™w™),w™»> = 0.

[p0368-b0032 | ordinary-paragraph | high] With (6.6) this can also be written:

[p0368-b0033 | ordinary-paragraph | high] (6.11) CDI (a)W E, = ("aw tl).

[p0368-b0034 | ordinary-paragraph | high] Note also that (6.11) gives:

## PDF 369 / printed 355



[p0369-b0004 | ordinary-paragraph | medium] for some t e (0, 1), i.e.

[p0369-b0005 | equation | low] (6.12)

[p0369-b0006 | equation | low] (gm, wm)x = pmD² J(um - tpmwm)·(wm, wm).

[p0369-b0007 | ordinary-paragraph | medium] Thus it follows from the convexity of D, (6.2) and (6.7) that

[p0369-b0008 | equation | low] βllgm1lx1/ wmIlx ≤pmM|/ wm|1x

[p0369-b0009 | ordinary-paragraph | medium] whence we derive the following lower bound for pm:

[p0369-b0010 | equation | low] (6.13)

[p0369-b0011 | equation | low] pm ≥ (β/M)(llgmI/x// wmIlx).

[p0369-b0012 | ordinary-paragraph | medium] Next, the sequence J(um) is by construction monotonically decreasing and so

[p0369-b0013 | ordinary-paragraph | medium] the sequence (u") is contained in D'. We have in particular:

[p0369-b0014 | equation | low] J(um+i) ≤ J(um -- pwm)  for all p with 0 ≤ p ≤ pm.

[p0369-b0015 | ordinary-paragraph | medium] Therefore

[p0369-b0016 | equation | low] (uM uM).(uMd -un)fzq(Z/zd) +x(uM ub)d -(un)r ≥(+un)f

[p0369-b0017 | ordinary-paragraph | medium] with t e (0, 1). Using again (6.7) and (6.2) we obtain:

[p0369-b0018 | equation | low] lluMll(z/d)W + xlluml/ xlu6l/gd - (un)r ≥ (r+un)r

[p0369-b0019 | ordinary-paragraph | medium] In view of (6.13) we can choose p = (B/M)( ll gm Il x/ ll wm Il x) thus getting

[p0369-b0020 | equation | low] xlubll(W/<d)(z/1)-≥(un)r -(+un)r

[p0369-b0021 | equation | low] (6.14)

[p0369-b0022 | ordinary-paragraph | medium] As the sequence J(um) is monotonically decreasing and bounded below (cf.

[p0369-b0023 | ordinary-paragraph | medium] (6.10)), it converges. In particular, (6.14) implies that

[p0369-b0024 | equation | low] 0 = [(+un)r - (un)r] u! (zd/W)z > xllubl u!

[p0369-b0025 | equation | low] (6.15)

[p0369-b0026 | ordinary-paragraph | low] α←u

[p0369-b0027 | ordinary-paragraph | low] 81m

[p0369-b0028 | ordinary-paragraph | medium] Besides that we have

[p0369-b0029 | equation | low] DJ(um+p) - DJ(um) = D² J(um + tum+p)·(um+p --um)

[p0369-b0030 | ordinary-paragraph | medium] with t e (0, 1). Thus (6.2) gives

[p0369-b0031 | equation | low] <un—d+un(un)f—(d+un)rα>≥llun——d+unl/x

[p0369-b0032 | equation | low] ≤(gm+p -- g",um+p - um)x,

[p0369-b0033 | ordinary-paragraph | medium] i.e.

[p0369-b0034 | equation | low] ·X1lu6 —d+u6|l(∞/I)≥x1un —d+unll 

[p0369-b0035 | ordinary-paragraph | medium] Since (g) converges in X, this means that (um) is a Cauchy sequence in X, and

[p0369-b0036 | ordinary-paragraph | medium] therefore a converging sequence in X. Thus there exists u in D' with

[p0369-b0037 | equation | low] lim um = u

[p0369-b0038 | ordinary-paragraph | medium] m→8

[p0369-b0039 | ordinary-paragraph | medium] and furthermore (6.15) and the continuity of DJ imply that

## PDF 370 / printed 356



[p0370-b0003 | ordinary-paragraph | high] Hence

[p0370-b0004 | ordinary-paragraph | high] J(u) = Min J(v). LJ

[p0370-b0005 | ordinary-paragraph | high] veD

[p0370-b0006 | ordinary-paragraph | high] The simple gradient and conjugate-gradient algorithms are among the most

[p0370-b0007 | ordinary-paragraph | high] popular applications of the method of descent. The gradient algorithm is obtained

[p0370-b0008 | ordinary-paragraph | high] by taking w™ = g” as direction of descent. Obviously this choice satisfies (6.7) and

[p0370-b0009 | ordinary-paragraph | high] therefore Theorem 6.1 guarantees the local convergence of the simple gradient

[p0370-b0010 | ordinary-paragraph | high] algorithm (6.5) (6.6) with w” = g”.

[p0370-b0011 | ordinary-paragraph | high] The Polack-Ribiere variant of the conjugate-gradient algorithm is defined by

[p0370-b0012 | ordinary-paragraph | high] choosing

[p0370-b0013 | equation | low] w? = g°

[p0370-b0014 | equation | low] (6.16)

[p0370-b0015 | equation | low] w™ = of af o™yw™ 1

[p0370-b0016 | ordinary-paragraph | high] with

[p0370-b0017 | ordinary-paragraph | high] eG Ganda) 3 WV

[p0370-b0018 | equation | low] (6.17)

[p0370-b0019 | ordinary-paragraph | high] ei — (Geeen d ee)

[p0370-b0020 | ordinary-paragraph | high] (compare with formula (I.4.68)). Again, Theorem 6.1 implies that this scheme is

[p0370-b0021 | ordinary-paragraph | high] convergent.

[p0370-b0022 | theorem | high] Theorem 6.2. Let D be defined by (6.1) and (6.2) and let u® belong to D. Then the

[p0370-b0023 | ordinary-paragraph | high] conjugate-gradient algorithm (6.5) (6.6) (6.16) and (6.17) converges in D.

[p0370-b0024 | proof | high] Proof. Let us show that w™ defined by (6.16) and (6.17) satisfies (6.7). First observe

[p0370-b0025 | ordinary-paragraph | high] that the property (6.11) and its consequence (6.12) established in Theorem 6.1 do

[p0370-b0026 | ordinary-paragraph | high] not require (6.7) but only that (g”, w”)y be positive. Now, this positivity is easily

[p0370-b0027 | ordinary-paragraph | high] proved by induction as it obviously holds for m = 0 and if it is true for m — 1

[p0370-b0028 | ordinary-paragraph | high] then (6.11) and (6.16) yield:

[p0370-b0029 | equation | low] (gw) a= OM (Ge we) lg ie.

[p0370-b0030 | ordinary-paragraph | high] Hence

[p0370-b0031 | ordinary-paragraph | high] Furthermore, (6.12) implies

[p0370-b0032 | ordinary-paragraph | high] (6.18) e™ = Clg" x ]/[D7J™-(w™w™,) J

[p0370-b0033 | ordinary-paragraph | high] with

[p0370-b0034 | equation | low] D? J" = D? J(u™ — to™w"), t defined by (6.12).

[p0370-b0035 | ordinary-paragraph | high] Likewise, with the same notation we have

## PDF 371 / printed 357



[p0371-b0005 | ordinary-paragraph | low] Ilgm-112

[p0371-b0006 | ordinary-paragraph | low] IIgm-1 11x

[p0371-b0007 | ordinary-paragraph | low] llgm-1 H12

[p0371-b0008 | ordinary-paragraph | medium] D2 Jm-1.(wm-1,gm)

[p0371-b0009 | ordinary-paragraph | medium] D2 Jm-1.(wm-1,wm-1)

[p0371-b0010 | ordinary-paragraph | medium] in view of (6.18). Therefore (6.2) yields:

[p0371-b0011 | equation | low] (xIl I-umI/ xll u6I1)(o/W) ≥ Iu|

[p0371-b0012 | ordinary-paragraph | medium] whence

[p0371-b0013 | equation | low] I/ wmll x = I/lgm + omwm-1 llx ≤ (1 + M/α)llgmllx.

[p0371-b0014 | ordinary-paragraph | medium] Thus

[p0371-b0015 | equation | low] (∞/W + 1)/[xllum|1xllu6l|] <llu6ll =x(uMu6)

[p0371-b0016 | ordinary-paragraph | medium] proving (6.7) with β = 1/(1 + M/α).

[p0371-b0017 | subsection | medium] 6.2. Least-Squares and Gradient Methods to Solve the Navier-Stokes Equations

[p0371-b0018 | ordinary-paragraph | medium] We propose first to decouple the divergence-free constraint and the nonlinearity

[p0371-b0019 | ordinary-paragraph | medium] in the Navier-Stokes equations by means of a heuristic alternating direction

[p0371-b0020 | ordinary-paragraph | medium] method introduced by Glowinski [36]. Then we shall solve the resulting nonlinear

[p0371-b0021 | ordinary-paragraph | medium] equations with the gradient methods of the preceding section.

[p0371-b0022 | ordinary-paragraph | medium] Following the Peaceman-Rachford alternating directions algorithm we con-

[p0371-b0023 | ordinary-paragraph | medium] struct a sequence (u", pm) starting from an initial pair (u°, p°) by:

[p0371-b0024 | ordinary-paragraph | medium] N

[p0371-b0025 | ordinary-paragraph | medium] umoum/ax; + rmum in Ω,

[p0371-b0026 | equation | low] (6.19)

[p0371-b0027 | equation | low] divum+1/2 = 0 in Ω,

[p0371-b0028 | equation | low] um+1/2 = 0 on F;

[p0371-b0029 | ordinary-paragraph | medium] N

[p0371-b0030 | ordinary-paragraph | medium] 0um+1/0x; + rmum+1

[p0371-b0031 | ordinary-paragraph | medium] -V4um+1

[p0371-b0032 | equation | low] (6.20)

[p0371-b0033 | equation | low] = f — grad pm+1/2 + rmum+1/2

[p0371-b0034 | equation | low] um+1 =0 on I,

[p0371-b0035 | ordinary-paragraph | medium] where the parameters rm are to be chosen as best as possible. Clearly, Problem

[p0371-b0036 | ordinary-paragraph | medium] (6.19) is like the Stokes problem which has been thoroughly studied in the

## PDF 372 / printed 358



[p0372-b0003 | ordinary-paragraph | high] no incompressibility constraint and is purely nonlinear.

[p0372-b0004 | ordinary-paragraph | high] Problem (6.20) is of the form:

[p0372-b0005 | ordinary-paragraph | high] N

[p0372-b0006 | equation | low] —vAu+ 5 udu/ox,+cu=f inQ,

[p0372-b0007 | ordinary-paragraph | high] (6.21) ds : ;

[p0372-b0008 | equation | low] u=0 onl

[p0372-b0009 | ordinary-paragraph | high] with both a linear elliptic and a nonlinear term in the left-hand side. This problem

[p0372-b0010 | ordinary-paragraph | high] can be easily and conveniently generalized to fit into the abstract setting of

[p0372-b0011 | ordinary-paragraph | high] Section 6.1.

[p0372-b0012 | ordinary-paragraph | high] Let ||.||,, denote the familiar dual norm of X’ and let Ae P(X;X’ ) be a

[p0372-b0013 | ordinary-paragraph | high] symmetric and X-elliptic operator in X, i.e.

[p0372-b0014 | ordinary-paragraph | high] (6.22) <Av,>v yll>vl| ]z VoexX,y>0.

[p0372-b0015 | ordinary-paragraph | high] Let G be a @?-mapping from X into X’ (with p > 2) and set

[p0372-b0016 | ordinary-paragraph | high] (6.23) F(v) = Av + G(v)

[p0372-b0017 | ordinary-paragraph | high] which is clearly a @’-mapping from X into X’. Our problem is:

[p0372-b0018 | ordinary-paragraph | high] (6.24) Find uin X such that F(u) = 0.

[p0372-b0019 | ordinary-paragraph | high] Obviously, Problem (6.21) is a particular case of (6.24) with

[p0372-b0020 | equation | low] Ke= (Gy) ee A= ee Gy) = Y,v j0v/ox, —f.

[p0372-b0021 | equation | low] ‘=

[p0372-b0022 | ordinary-paragraph | high] We intend to solve Problem (6.24) by replacing it with an equivalent least-

[p0372-b0023 | ordinary-paragraph | high] squares problem. To this end, consider the functional:

[p0372-b0024 | equation | low] J(v) = (1/2) ||F O) |

[p0372-b0025 | ordinary-paragraph | high] where ||. ||, is defined by

[p0372-b0026 | ordinary-paragraph | high] (6.25) Ifllx = <A 6A”.

[p0372-b0027 | ordinary-paragraph | high] We are going to see below that, because A is symmetric and elliptic, ||. ||, is a

[p0372-b0028 | ordinary-paragraph | high] norm on X’ equivalent to the dual norm and the corresponding functional J is

[p0372-b0029 | ordinary-paragraph | high] strictly convex and has a unique minimum.

[p0372-b0030 | lemma | high] Lemma 6.1. The mapping f > <A~‘f, f>*? is anorm on X' equivalent to the dual

[p0372-b0031 | ordinary-paragraph | high] norm.

[p0372-b0032 | proof | high] Proof. From (6.22) we infer that

[p0372-b0033 | ordinary-paragraph | high] ASL eA Tig.

[p0372-b0034 | equation | low] JASl x < (1/) IF lle

## PDF 373 / printed 359



[p0373-b0004 | equation | low] <A-f,f>≤(1/v)IIfI1

[p0373-b0005 | ordinary-paragraph | medium] On the other hand, we set

[p0373-b0006 | equation | low] K = I| A llg(x;x)-

[p0373-b0007 | ordinary-paragraph | medium] Therefore

[p0373-b0008 | equation | low] Ilfll ≤ KIA-1f Ilx

[p0373-b0009 | ordinary-paragraph | medium] and thus

[p0373-b0010 | equation | low] <A-f,f>≥(/K²)11f11

[p0373-b0011 | ordinary-paragraph | medium] Summing up, we get

[p0373-b0012 | equation | low] (6.26)

[p0373-b0013 | equation | low] *llfll(x/1)≥<f->≥ lfl(X/)

[p0373-b0014 | theorem | medium] Theorem 6.3. Let u be a nonsingular solution of Problem (6.24). Then the functional 

[p0373-b0015 | ordinary-paragraph | medium] J defined by

[p0373-b0016 | equation | low] (6.27)

[p0373-b0017 | equation | low] J(v) = (1/2)<A-1(F(v)), F(v)>

[p0373-b0018 | ordinary-paragraph | medium] is strictly convex in a neighborhood of u.

[p0373-b0019 | proof | medium] Proof. Taking into account the symmetry of A-', the first two derivatives of J

[p0373-b0020 | ordinary-paragraph | medium] have the expression:

[p0373-b0021 | equation | low] DJ(v)· w = <A-1(DF(v)· w), F(v))

[p0373-b0022 | equation | low] (6.28)

[p0373-b0023 | equation | low] =<A-1(F(v), DF(v)· w>,

[p0373-b0024 | ordinary-paragraph | medium] (6.29) D² J(v)·(w, z) =(A-1(DF(u)· 2), DF(v)· w> + <A-1(F(v)), D² F(v)·(w, 2)>.

[p0373-b0025 | ordinary-paragraph | medium] Now, recall that u is a nonsingular solution of Problem (6.24) if

[p0373-b0026 | equation | low] F(u) = O  and  DF(u)  is an isomorphism from X onto X'.

[p0373-b0027 | ordinary-paragraph | medium] Hence (6.29) yields:

[p0373-b0028 | equation | low] D² J(u)·(w, w) = (A-1(DF(u)· w), DF(u)· w).

[p0373-b0029 | equation | low] (6.30)

[p0373-b0030 | ordinary-paragraph | medium] Thus (6.26) implies that

[p0373-b0031 | equation | low] D² J(u)· (w, w) ≥ (/K²) 1/DF(u)· w I1

[p0373-b0032 | equation | low] ≥ol|wllx

[p0373-b0033 | equation | low] > 0,

[p0373-b0034 | ordinary-paragraph | medium] since DF(u) is an isomorphism of X onto X'. But the mapping D? J is continuous

[p0373-b0035 | ordinary-paragraph | medium] in X (because F is a C'-mapping); therefore there exists p > 0 such that

[p0373-b0036 | equation | low] IID² J(u) - D² J(v)I1 ≤ 8/2

[p0373-b0037 | ordinary-paragraph | medium] for all ve S(u; p) = {ve X; Ilu - ull x ≤ p}. Hence

## PDF 374 / printed 360



[p0374-b0003 | ordinary-paragraph | high] ie. J is strictly convex in S(u; p). CL]

[p0374-b0004 | equation | low] As a consequence, Problem (6.24) is equivalent to solve:

[p0374-b0005 | ordinary-paragraph | high] (6.32) inf (1/2)<A*F(v), F(v))

[p0374-b0006 | ordinary-paragraph | high] ve S(u;p)

[p0374-b0007 | ordinary-paragraph | high] and this solution can be achieved by the gradient and conjugate-gradient methods

[p0374-b0008 | ordinary-paragraph | high] of Section 6.1. Indeed, assume that D*G is bounded on all bounded subsets of

[p0374-b0009 | ordinary-paragraph | high] X so that F, DF and D’F are also bounded there, and assume that u is a

[p0374-b0010 | ordinary-paragraph | high] nonsingular solution of (6.24). Then we already know that the first part of (6.2)

[p0374-b0011 | ordinary-paragraph | high] holds on the ball S(u;p), while the second part stems from (6.30), (6.26), the

[p0374-b0012 | ordinary-paragraph | high] isomorphism property of DF(u) and the continuity of D?J. In addition, the

[p0374-b0013 | ordinary-paragraph | high] boundedness of F implies that J is bounded in S(u;p). Thus, by choosing a

[p0374-b0014 | ordinary-paragraph | high] starting value u° in S(u; p) and setting J° = J(u°) we can take

[p0374-b0015 | equation | low] D = {veX ; J(v) < J(u®)} NS(u;p )

[p0374-b0016 | ordinary-paragraph | high] and Theorems 6.1 and 6.2 guarantee the convergence of the gradient and conjugate-

[p0374-b0017 | ordinary-paragraph | high] gradient algorithms.

[p0374-b0018 | ordinary-paragraph | high] Let us examine the practical implementation of the simple gradient method.

[p0374-b0019 | ordinary-paragraph | high] The symmetry and ellipticity of A induce us to equip X with the scalar product:

[p0374-b0020 | equation | low] (u, 0), = (Au, >

[p0374-b0021 | ordinary-paragraph | high] and associated norm ||u||, = <Au,u>"*. Hence, in view of(6 .28), the gradient g(v)

[p0374-b0022 | ordinary-paragraph | high] is defined by

[p0374-b0023 | equation | low] <Ag(v),w> = <DJ(v), w>

[p0374-b0024 | equation | low] = (A F(v), DF(v):w >

[p0374-b0025 | equation | low] = ((DF(Av“) F)(v ), w>,

[p0374-b0026 | ordinary-paragraph | high] Le:

[p0374-b0027 | ordinary-paragraph | high] (6.33) g(v) = A“'(DF(v)A)! F(v).

[p0374-b0028 | ordinary-paragraph | high] Thus one step of the simple gradient algorithm can be decomposed into the

[p0374-b0029 | ordinary-paragraph | high] following operations:

[p0374-b0030 | ordinary-paragraph | high] 1°) compute gata Sku),

[p0374-b0031 | equation | low] ge = Ase (DB(G™)2\"

[p0374-b0032 | ordinary-paragraph | high] 2°) then minimize J(u” — pg™) with respect to p, where

[p0374-b0033 | equation | low] J(u" — pg™) = (1/2)<A* F(u™ — pg”™), F(u™ — pg™)>.

[p0374-b0034 | ordinary-paragraph | high] Each iteration requires the resolution of two linear problems relative to the

[p0374-b0035 | ordinary-paragraph | high] operator A plus the determination of p”. As an example, let us explicit the

## PDF 375 / printed 361



[p0375-b0004 | ordinary-paragraph | medium] pw) is a fourth-degree polynomial because F is a polynomial of degree two.

[p0375-b0005 | ordinary-paragraph | medium] Therefore Taylor's expansion of J(um - pg") reduces to:

[p0375-b0006 | equation | low] (μ8μa).(un)fza(Z/zd) + u8.(un)rqd - (un)f = (uad -un)f

[p0375-b0007 | equation | low] (6.34)

[p0375-b0008 | ordinary-paragraph | medium] —-(p3/6)D3 J(um) ·(gm, g"m, gm)

[p0375-b0009 | ordinary-paragraph | medium] + (p4 /24)D4 J(um)·(gm,g",g",gm),

[p0375-b0010 | ordinary-paragraph | medium] where the third and fourth derivatives of J have the simple expression:

[p0375-b0011 | equation | low] <(u8 u8).(un)dcau8.(un)da1-V>e = (ua u8 u8).(un)f ea

[p0375-b0012 | ordinary-paragraph | low] <(uu).(u)dzq(uw8).(un)dz-V>=(u8uuu8).(un)a

[p0375-b0013 | ordinary-paragraph | medium] Summing up, to solve Problem (6.21), each iteration of the simple gradient

[p0375-b0014 | ordinary-paragraph | medium] algorithm runs as follows:

[p0375-b0015 | ordinary-paragraph | medium] 1°) given u" e H(Q), compute the solution zm e H (Q) of

[p0375-b0016 | ordinary-paragraph | medium] N

[p0375-b0017 | ordinary-paragraph | low] Cuy(oum/0x;) -f in Ω,

[p0375-b0018 | equation | low] -v△zm + czm = -v4um + cum + >

[p0375-b0019 | equation | low] zm = 0 on I;

[p0375-b0020 | ordinary-paragraph | medium] 2°) find the solution g" e H1(Q) of

[p0375-b0021 | ordinary-paragraph | medium] v(grad g", grad v) + c(g", v) = v(grad z", grad v)

[p0375-b0022 | ordinary-paragraph | medium] N

[p0375-b0023 | equation | low] + c(zm,v) + ∑ (uμ0v/0x; + v;0um/0xj,zm)

[p0375-b0024 | ordinary-paragraph | medium] Vve H(2), g" = 0 on F;

[p0375-b0025 | ordinary-paragraph | medium] 3°) compute

[p0375-b0026 | equation | low] {uz+u|}(z/1) =(un)

[p0375-b0027 | equation | low] (6.35)

[p0375-b0028 | equation | low] DJ(um) · gm = (1/2){vlgm1²,2 + cllgm 12,α};

[p0375-b0029 | equation | low] (6.36)

[p0375-b0030 | ordinary-paragraph | medium] 4°) find the solution vm e H'(Q) of

[p0375-b0031 | ordinary-paragraph | medium] N

[p0375-b0032 | ordinary-paragraph | low] v4vm + cvm = -v4gm + cgm + ∑ (u0gm/0x; + gm0um/0x) in Ω,

[p0375-b0033 | equation | low] j=1

[p0375-b0034 | equation | low] v" =0 on I;

[p0375-b0035 | ordinary-paragraph | medium] 5°) compute

[p0375-b0036 | ordinary-paragraph | medium] N

[p0375-b0037 | ordinary-paragraph | medium] gm0gm/0xj,

[p0375-b0038 | equation | low] tm = D² F(um)·(g",gm) = 2 ∑

[p0375-b0039 | equation | low] =1

[p0375-b0040 | equation | low] D² J(um)-(gm, gm) = v/vm|2, + cl/ vm//1,2 + (zm, tm).

[p0375-b0041 | equation | low] (6.37)

[p0375-b0042 | equation | low] D3 J(um)·(g",gm,gm) = 3(tm, vm);

[p0375-b0043 | equation | low] (6.38)

## PDF 376 / printed 362



[p0376-b0003 | equation | low] —vAw" + cw™=t" inQ,

[p0376-b0004 | equation | low] w”=0 onT;

[p0376-b0005 | ordinary-paragraph | high] 7°) compute

[p0376-b0006 | ordinary-paragraph | high] (6.39) D* J(u”): (g”,8", 8", 8") = vIw"lt,o + cllw"llo,03

[p0376-b0007 | ordinary-paragraph | high] 8°) find the positive root p” of

[p0376-b0008 | equation | low] dJ(u™ — p"g)/dp = 0

[p0376-b0009 | ordinary-paragraph | high] and update u”™ by:

[p0376-b0010 | equation | low] Uo m+1 =U ps.

[p0376-b0011 | ordinary-paragraph | high] Each iteration requires the solution of four Dirichlet problems.

[p0376-b0012 | ordinary-paragraph | high] The implementation of the conjugate-gradient algorithm is much like above

[p0376-b0013 | ordinary-paragraph | high] and is left as an exercise.

[p0376-b0014 | subsection | high] 6.3. Newton’s Method and the Continuation Method

[p0376-b0015 | ordinary-paragraph | high] The methods discussed here are intended to solve the complete Navier-Stokes

[p0376-b0016 | ordinary-paragraph | high] equations: incompressible and nonlinear. More generally, we want to solve

[p0376-b0017 | ordinary-paragraph | high] equations of the type introduced in Section 3.1, namely:

[p0376-b0018 | ordinary-paragraph | high] (6.40) F(A,u) = 0,

[p0376-b0019 | ordinary-paragraph | high] where F is a @?-mapping (p > 1) defined on A x X with values in 2, X and &

[p0376-b0020 | ordinary-paragraph | high] being two Banach spaces and A an interval of R. Let us fix 4 for the moment and

[p0376-b0021 | ordinary-paragraph | high] assume that u = u(J)e X is a nonsingular solution of (6.40), 1.c.

[p0376-b0022 | equation | low] F(j,u) =0, D,F(A,u) is an isomorphism from X onto 2.

[p0376-b0023 | ordinary-paragraph | high] Then we know from the inverse function theorem (and also from the material of

[p0376-b0024 | ordinary-paragraph | high] Section 3.2) that there exists a closed ball S(u;«) where the equation (6.40) has

[p0376-b0025 | ordinary-paragraph | high] no other solution than u.

[p0376-b0026 | ordinary-paragraph | high] Since u is an isolated solution of (6.40) and since F is at least differentiable,

[p0376-b0027 | ordinary-paragraph | high] an efficient way to approximate u is the Newton’s algorithm:

[p0376-b0028 | ordinary-paragraph | high] starting from an initial guess u°, construct the sequence (u") in X by:

[p0376-b0029 | ordinary-paragraph | high] (6.41) tt" Dar uel OR et) See)

[p0376-b0030 | ordinary-paragraph | high] or equivalently

[p0376-b0031 | equation | low] D,F(A,u")-(u"** — u") = —F(A,u").

[p0376-b0032 | ordinary-paragraph | high] As D,F(A,u) is a linear operator, each step of Newton’s method requires the

[p0376-b0033 | ordinary-paragraph | high] solution of a different linear problem relative to D, F(A, u"). If this is too costly,

## PDF 377 / printed 363



[p0377-b0003 | ordinary-paragraph | high] (6.42) u™* =u" —[D,F(A,u°))!-FA,u")

[p0377-b0004 | equation | low] n> 0,

[p0377-b0005 | ordinary-paragraph | high] or equivalently

[p0377-b0006 | equation | low] DEE) tw = a”),

[p0377-b0007 | ordinary-paragraph | high] We are going to prove that both schemes are convergent.

[p0377-b0008 | theorem | high] Theorem 6.3. Assume that D, F(A, v) is Lipschitz-continuous with respect to

[p0377-b0009 | ordinary-paragraph | high] v in the

[p0377-b0010 | ordinary-paragraph | high] ball S(u; a), i.e. there exists a constant K > 0 such that

[p0377-b0011 | ordinary-paragraph | high] (6.43) ||D ,(4F,v ) —D ,F(A, 0*|) g ax,a)< K||—v v* ly Vo, v* e S(u;.@).

[p0377-b0012 | ordinary-paragraph | high] Then there exists an x with 0 < « < « such that for each initial guess u° in S(u; a’)

[p0377-b0013 | ordinary-paragraph | high] the Newton’s algorithm (6.41) determines a unique sequence (u") < S(u;«’) that

[p0377-b0014 | ordinary-paragraph | high] converges to the solution u of (6.40). Furthermore the convergence is quadratic:

[p0377-b0015 | ordinary-paragraph | high] (6.44) ull ln” = ul2um C10,

[p0377-b0016 | ordinary-paragraph | high] Likewise, there exists an x" with 0 < «" < « such that for each initial value u°

[p0377-b0017 | ordinary-paragraph | high] in S(u; a”) the scheme (6.42) determines a unique sequence (u") < S(u; a”) that

[p0377-b0018 | ordinary-paragraph | high] converges to u. But the convergence is only linear:

[p0377-b0019 | ordinary-paragraph | high] (6.45) tee ail Clu — ail Cre 1.

[p0377-b0020 | proof | high] Proof. To begin with, it follows from (6.43) and Lemma 3.3 that there exists an

[p0377-b0021 | ordinary-paragraph | high] a with O < « < «such that D, F(A, v) is an isomorphism ofX onto & for all v in

[p0377-b0022 | ordinary-paragraph | high] S(u; x’). Indeed, if we take F, = F, a, = v,y = ||[D, F(A, wu) | ga-xy),U = ||D FO,

[p0377-b0023 | ordinary-paragraph | high] u) — D, F(A, v)|| yx.) then Lemma 3.3 says that D, F(A, v) is an isomorphism of

[p0377-b0024 | ordinary-paragraph | high] X onto % provided that yu < 1. In view of( 6.43), this inequality holds if we choose

[p0377-b0025 | ordinary-paragraph | high] a’ < Min(«, 1/(yK)). In particular, we can take

[p0377-b0026 | ordinary-paragraph | high] (6.46) a’ < 1/(2yK)

[p0377-b0027 | ordinary-paragraph | high] and formula (3.16) gives the bound

[p0377-b0028 | ordinary-paragraph | high] (6.47) ILD, F(A, 0%1) Ilg @sx)< 27.

[p0377-b0029 | ordinary-paragraph | high] Now let us prove that when u° belongs to S(u; «’) with «’ satisfying (6.46) then

[p0377-b0030 | ordinary-paragraph | high] the scheme (6.41) defines a sequence (u”) in S(u; «’) that converges to u. We proceed

[p0377-b0031 | ordinary-paragraph | high] by induction: suppose that u” belongs to S(u; a’); then [D, F(A, u")]~' exists and

[p0377-b0032 | equation | low] ut? _—_y=y"—ut [D,F(A,u")]* -(F(A,u) — F(A,u")).

[p0377-b0033 | ordinary-paragraph | high] In other words

[p0377-b0034 | ordinary-paragraph | high] Pe y= DEA)L F Ou) — Fu") = DF,4") -(u— u")|

[p0377-b0035 | ordinary-paragraph | high] 1

[p0377-b0036 | ordinary-paragraph | high] = pari.uy” | [D,F(A,u" + t(u — u")) — D,F(A,u")]-(u — u") dt.

[p0377-b0037 | ordinary-paragraph | high] 0

## PDF 378 / printed 364



[p0378-b0004 | equation | low] |lun+1 —ulx≤yK|lu-—u~11x

[p0378-b0005 | ordinary-paragraph | medium] and since α'yK ≤ 1/2 this yields

[p0378-b0006 | equation | low] Il un+1 -- ullx ≤(1/2) llun - ullx.

[p0378-b0007 | ordinary-paragraph | medium] Hence un+1 belongs to S(u; α') and these two inequalities show that the sequence

[p0378-b0008 | ordinary-paragraph | medium] (u") converges quadratically to u.

[p0378-b0009 | ordinary-paragraph | medium] Next, consider the scheme (6.42). Like above, we start with u? in S(u; α") for

[p0378-b0010 | ordinary-paragraph | medium] some α" ≤ α' that we shall specify subsequently. Then (6.42) determines a unique

[p0378-b0011 | ordinary-paragraph | medium] sequence (u") and similarly, we have:

[p0378-b0012 | ordinary-paragraph | medium] un+1 - u =[DF(n,u°)]-1

[p0378-b0013 | ordinary-paragraph | medium] [DuF(,un + t(u - u")) - DuF(,u°)]·(u - u")dt.

[p0378-b0014 | ordinary-paragraph | low] Jo

[p0378-b0015 | ordinary-paragraph | medium] Hence assuming that u belongs also to S(u; α") we derive:

[p0378-b0016 | equation | low] lun+1 ——ullx≤K(llun-—u|1x + 1|lu-u|1x)llu-u1x

[p0378-b0017 | equation | low] ≤3α"yKllu" -— ullx.

[p0378-b0018 | ordinary-paragraph | medium] Therefore, by choosing

[p0378-b0019 | equation | low] α" < 1/(3yK)

[p0378-b0020 | ordinary-paragraph | medium] we find that un+1 belongs to S(u;, α") and that the sequence (u^) converges linearly

[p0378-b0021 | ordinary-paragraph | medium] to u.

[p0378-b0022 | ordinary-paragraph | medium] 口

[p0378-b0023 | ordinary-paragraph | medium] Let us apply Theorem 6.3 to solve the familiar class of problems

[p0378-b0024 | equation | low] (6.48)

[p0378-b0025 | equation | low] F(A,u) = u + TG(,u) = 0 = v∈ 4,

[p0378-b0026 | ordinary-paragraph | medium] where X and Y are two Banach spaces, 4 is a compact interval of R, Te (Y; X)

[p0378-b0027 | ordinary-paragraph | medium] and G is a &?-mapping from A x X into Y with D²G bounded on all bounded

[p0378-b0028 | ordinary-paragraph | medium] subsets of 4 x X. This last property implies the Lipschitz condition (6.43).

[p0378-b0029 | ordinary-paragraph | medium] Therefore, if X → u() is a branch of nonsingular solutions of (6.48), Newton's

[p0378-b0030 | ordinary-paragraph | medium] method defines a locally (and quadratically) convergent algorithm:

[p0378-b0031 | equation | low] (1 + TD,G(l,u"))·un+1 = T[DG(1,u")·un -- G(n,u")].

[p0378-b0032 | equation | low] (6.49)

[p0378-b0033 | ordinary-paragraph | medium] Likewise, the variant (6.42) is also locally (but linearly) convergent:

[p0378-b0034 | equation | low] (6.50)

[p0378-b0035 | equation | low] (1 + TDG(a,u))· un+1 = T[DG(,u%)·u" - G(x,u")].

[p0378-b0036 | ordinary-paragraph | medium] As an example, consider the Navier-Stokes equations:

[p0378-b0037 | ordinary-paragraph | low] N

[p0378-b0038 | ordinary-paragraph | medium] -vu+

[p0378-b0039 | equation | low] u;(ou/0x;) + grad p = f,

[p0378-b0040 | equation | low] =

[p0378-b0041 | ordinary-paragraph | medium] in Q

[p0378-b0042 | equation | low] (6.51)

[p0378-b0043 | equation | low] div u = 0, 

[p0378-b0044 | equation | low] u =o on F.

## PDF 379 / printed 365



[p0379-b0004 | ordinary-paragraph | medium] the following correspondence:

[p0379-b0005 | ordinary-paragraph | medium] X = H(Ω) × L(Ω),

[p0379-b0006 | equation | low] Y = H-1(Q),  T = the Stokes operator,

[p0379-b0007 | ordinary-paragraph | medium] N

[p0379-b0008 | equation | low]  = 1/v, 

[p0379-b0009 | equation | low] G(入,u) = 2

[p0379-b0010 | ordinary-paragraph | low] u;(du/0x;) -

[p0379-b0011 | ordinary-paragraph | medium] Moreover, (u, p) is a solution of (6.51) iff u = (u, p/v) is a solution of (6.48). Then

[p0379-b0012 | ordinary-paragraph | medium] Newton's algorithm (6.49) reads:

[p0379-b0013 | ordinary-paragraph | medium] Find (ur+1, pn+1)eH(Q) × L2(Ω) such that

[p0379-b0014 | ordinary-paragraph | medium] N

[p0379-b0015 | equation | low] -4u+1 + (1/v)  [u;(@u+1/0x,) + u+(0u"/0x;)] + grad pn+1

[p0379-b0016 | equation | low] =1

[p0379-b0017 | equation | low] =(1/v)(

[p0379-b0018 | ordinary-paragraph | medium] u,(0u/0x;) + f

[p0379-b0019 | ordinary-paragraph | low] (M

[p0379-b0020 | equation | low] (6.52) 

[p0379-b0021 | ordinary-paragraph | medium] in Ω,

[p0379-b0022 | equation | low] divun+1 = 0 in Ω,

[p0379-b0023 | equation | low] u"+1 = 0 

[p0379-b0024 | ordinary-paragraph | medium] on F.

[p0379-b0025 | ordinary-paragraph | medium] Similarly, the simpler variant (6.50) reads:

[p0379-b0026 | ordinary-paragraph | medium] Find (un+1, pn+1)∈ H(Q) x L(Ω) such that

[p0379-b0027 | ordinary-paragraph | medium] N

[p0379-b0028 | equation | low] -4u+1 + (1/v)  [u(@u+1/0x;) + u+1(u/0x,)] + grad pn+1

[p0379-b0029 | ordinary-paragraph | medium] N

[p0379-b0030 | ordinary-paragraph | low] [(①u"/Cx;)(u} - u,) + u)(①u/0x;)] + f

[p0379-b0031 | equation | low] =(1/v)

[p0379-b0032 | equation | low] (6.53)

[p0379-b0033 | equation | low] divun+1 = 0 in Ω,

[p0379-b0034 | equation | low] un+1 =0 on I.

[p0379-b0035 | ordinary-paragraph | medium] Note that in either case, the next iterate (un+1, pn+1) is independent of p". Also,

[p0379-b0036 | ordinary-paragraph | medium] DuF(, u) is obviously Lipschitz-continuous since D² G(, u) is constant. Hence, if

[p0379-b0037 | ordinary-paragraph | medium] (u, p) is a nonsingular solution of (6.51), starting from an initial guess u? sufficiently

[p0379-b0038 | ordinary-paragraph | medium] near u and an arbitrary p°, the scheme (6.52) (resp. (6.53)) determines a unique

[p0379-b0039 | ordinary-paragraph | medium] sequence (u, p") that converges quadratically (resp. linearly) to u = (u, p/v). Of

[p0379-b0040 | ordinary-paragraph | medium] course, if u = u(l) belongs to a branch of nonsingular solutions on a compact

[p0379-b0041 | ordinary-paragraph | medium] interval A, this result stays valid for all X in A with constants independent of X.

[p0379-b0042 | ordinary-paragraph | medium] The drawback of Newton's method is that its convergence can only be insured

[p0379-b0043 | ordinary-paragraph | medium] when the first guess u° is sufficiently near the solution u. If this solution is part

[p0379-b0044 | ordinary-paragraph | medium] of a branch of nonsingular solutions and if we know the solution at a neighboring

[p0379-b0045 | ordinary-paragraph | medium] point, say u(A - Ax) for an adequate increment AX, then we can derive from

[p0379-b0046 | ordinary-paragraph | medium] this value the first guess to start Newton's algorithm. This is the method of

[p0379-b0047 | ordinary-paragraph | medium] continuation; let us describe it more precisely. Assume that X → u(l) is a branch

## PDF 380 / printed 366



[p0380-b0004 | ordinary-paragraph | medium] u(2) and we can differentiate both sides of (6.40):

[p0380-b0005 | ordinary-paragraph | low] VAeA,

[p0380-b0006 | equation | low] DuF(,u(2))·(du(2)/dx) + D,F(A,u(a)) = 0

[p0380-b0007 | equation | low] (6.54)

[p0380-b0008 | ordinary-paragraph | medium] i.e. we find a first order differential equation of the form

[p0380-b0009 | equation | low] (6.55)

[p0380-b0010 | equation | low] du(2)/d = -Φ(2)

[p0380-b0011 | ordinary-paragraph | medium] where

[p0380-b0012 | equation | low] Φ(2) = [DuF(, u(A)]-1 Dx F(A,u(2).

[p0380-b0013 | ordinary-paragraph | medium] The simplest way to solve (6.55) is to use the one-step, explicit, Euler's method;

[p0380-b0014 | ordinary-paragraph | medium] this induces us to choose

[p0380-b0015 | equation | low] (6.56)

[p0380-b0016 | equation | low] u(n) = u( - △x) - Φ( - 4)· 4.

[p0380-b0017 | ordinary-paragraph | medium] In other words u°(l) is defined by

[p0380-b0018 | ordinary-paragraph | low] D,F( - 4,u( - 42))·(u(2) -u(2 - A))

[p0380-b0019 | equation | low] (6.57)

[p0380-b0020 | equation | low] = -DF( - ,u( - △A))· .

[p0380-b0021 | ordinary-paragraph | medium] Let us estimate the error u(l) - u°(2). From (6.55) we infer that:

[p0380-b0022 | ordinary-paragraph | low] 入

[p0380-b0023 | equation | low] u(2) = u( - 42)

[p0380-b0024 | ordinary-paragraph | medium] Φ(μ)dμ;

[p0380-b0025 | ordinary-paragraph | low] Jx-

[p0380-b0026 | ordinary-paragraph | medium] subtracting (6.56) we obtain

[p0380-b0027 | equation | low] u(x) -u(2) =

[p0380-b0028 | ordinary-paragraph | low] p(μ)dμ - Φ( -- △x)· 4

[p0380-b0029 | ordinary-paragraph | medium] -

[p0380-b0030 | ordinary-paragraph | low] p'(0u)·(u - A + 4x)dμ.

[p0380-b0031 | ordinary-paragraph | low] J-

[p0380-b0032 | ordinary-paragraph | medium] Hence

[p0380-b0033 | equation | low] Ilu(2) - u(2)llx ≤ [(42)²/2] Max  I1Φ'(0)lx.

[p0380-b0034 | ordinary-paragraph | low] D∈(A-,A)

[p0380-b0035 | ordinary-paragraph | medium] Thus Il u(2) - u°(4)Il x is O(42)²) and if 4X is small enough, u(2) defined by (6.56)

[p0380-b0036 | ordinary-paragraph | medium] is an adequate starting value for Newton's algorithm.

[p0380-b0037 | ordinary-paragraph | medium] As an example, let us explicit formula (6.57) for the Navier-Stokes equation

[p0380-b0038 | ordinary-paragraph | medium] (6.51). To simplify, we set

[p0380-b0039 | equation | low] Su(2) = u(a) - u( - △2).

[p0380-b0040 | ordinary-paragraph | medium] Then (6.57) amounts to

[p0380-b0041 | ordinary-paragraph | low] [D .((D -r)nD - )'a + ()ng·((D - r)nD - )"a]L- = ()ng

[p0380-b0042 | ordinary-paragraph | medium] or equivalently

## PDF 381 / printed 367



[p0381-b0006 | equation | low] =

[p0381-b0007 | ordinary-paragraph | low] + ou;(2)(du(2 - 4x)/0xj]

[p0381-b0008 | ordinary-paragraph | low] u;(2 - 4x)(0u(2 - 42)/0xj) -

[p0381-b0009 | ordinary-paragraph | low] +

[p0381-b0010 | ordinary-paragraph | medium] Setting du(l) = (Su(4), ( - 42)8p(2)), this problem also reads:

[p0381-b0011 | ordinary-paragraph | medium] Find (8u(2), op(a))∈ H(Q) × L(Ω) such that

[p0381-b0012 | ordinary-paragraph | medium] N

[p0381-b0013 | ordinary-paragraph | low] -(1/(x - 42))u(2) + >

[p0381-b0014 | ordinary-paragraph | low] ∑ [u;(1 - 4)(08u(2)/0xj) + ou;(a)(0u(2 - A2)/0x;)]

[p0381-b0015 | equation | low] ∑u;(2 - 42)(0u(A - 4)/0x)

[p0381-b0016 | ordinary-paragraph | medium] + grad 8p(2) = (4x/( - 4))| f -

[p0381-b0017 | ordinary-paragraph | medium] in S,

[p0381-b0018 | equation | low] =

[p0381-b0019 | equation | low] div du(a) = 0 in Ω,

[p0381-b0020 | equation | low] u(l) = O on I.

[p0381-b0021 | ordinary-paragraph | medium] Note that this problem is analogous to one iteration of Newton's algorithm.

[p0381-b0022 | remark | medium] Remark 6.1. By using a suitable discrete derivative, a Newton-type algorithm can

[p0381-b0023 | ordinary-paragraph | medium] also be derived to solve non differentiable schemes like the ones analyzed in

[p0381-b0024 | ordinary-paragraph | medium] Sections 3.4 and 5.1. Under adequate hypotheses a nearly quadratic convergence

[p0381-b0025 | ordinary-paragraph | medium] can be achieved (cf. Girault & Raviart [34]).

[p0381-b0026 | remark | medium] Remark 6.2. We can also solve (6.55) with a Runge-Kutta method or with an

[p0381-b0027 | ordinary-paragraph | medium] explicit multistep method. The proof of the corresponding error estimate is pretty

[p0381-b0028 | ordinary-paragraph | medium] much like above.
