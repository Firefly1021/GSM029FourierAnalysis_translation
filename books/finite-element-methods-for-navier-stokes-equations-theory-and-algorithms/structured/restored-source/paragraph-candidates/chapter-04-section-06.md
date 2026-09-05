# Paragraph candidates: chapter-04-section-06

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-04-section-06-pc00001 | ordinary-paragraph | high | PDF 366

qn€ Qn (5.53) +yv inf (lo — 4,llo,9 + h?!"|c o— 01,10) 6,69, +h?T h — Vila Wali.a.0 + hah where 1/y + 1/t =1, u, = (u, = curly,,@,) and u =(u=curly,q@) denote the solutions of (5.18) and (5.7) respectively. It follows readily from (5.53) and (5.48) that the pressure p, has the same order of convergence as the velocity:

## chapter-04-section-06-pc00002 | theorem | high | PDF 366

Theorem 5.3. Under the assumptions of Theorem 5.1 the pressure p, defined by

## chapter-04-section-06-pc00003 | ordinary-paragraph | high | PDF 366

Problem (5.51) converges to p with the same order of accuracy as the velocity. Namely, if fe L'(Q)? for te[r, 2) we have:

## chapter-04-section-06-pc00004 | equation | low | PDF 366

[[FORMULA:f-p0366-06082]]

## chapter-04-section-06-pc00005 | equation | low | PDF 366

[[FORMULA:f-p0366-06083]]

## chapter-04-section-06-pc00006 | equation | low | PDF 366

[[FORMULA:f-p0366-06084]]

## chapter-04-section-06-pc00007 | ordinary-paragraph | high | PDF 366

where 1/y + 1/t = 1. When w belongs to W”’”(Q) or when | > 2, this bound can be extended to t = 2. When 1 = 1 and t = 2 we have:

## chapter-04-section-06-pc00008 | equation | low | PDF 366

[[FORMULA:f-p0366-06087]]

## chapter-04-section-06-pc00009 | ordinary-paragraph | high | PDF 366

Finally when the mapping A > (W(A), p(A)) is continuous from A into [H™*?(Q) wm*si2,°(Q)] x H™(Q) for some real me [1,1 — 1/2] we have

## chapter-04-section-06-pc00010 | equation | low | PDF 366

[[FORMULA:f-p0366-06089]]

## chapter-04-section-06-pc00011 | section | high | PDF 366

§6. Numerical Algorithms

## chapter-04-section-06-pc00012 | ordinary-paragraph | high | PDF 366

Navier-Stokes equations are difficult to solve in practice because they are nonlinear. We present here a few simple converging algorithms that permit to handle the nonlinearity. Although they are intended to solve the discrete systems of (nonlinear) equations, it is simpler to introduce these algorithms in connection with the continuous problem. The reader will verify easily that the convergence theorems below are also valid for the approximate problems.

## chapter-04-section-06-pc00013 | subsection | high | PDF 366

6.1. General Methods of Descent and Application to Gradient Methods

## chapter-04-section-06-pc00014 | ordinary-paragraph | high | PDF 366,367

Like every nonlinear problem, the Navier-Stokes equations can be put into the framework of an optimization problem. Therefore we shall consider first the X. Let ||.||y and (.,.), denote respectively the norm and associated scalar product ofX and let J be a @*-mapping from _X into R. We propose to minimize J over an adequate subset D of X, chosen as follows. First, since we are only interested in a minimum of J we restrict the discussion to the set

## chapter-04-section-06-pc00015 | equation | low | PDF 367

[[FORMULA:f-p0367-06090]]

## chapter-04-section-06-pc00016 | ordinary-paragraph | high | PDF 367

for some constant Cy; of course, we suppose that this set is not empty and we take for D one of its connected components. In other words, D is a non empty connected component of: (6.1) {veX ; J(v)< Co}. Now, we assume that the functional J is strictly convex in D, namely: there exist two constants « > 0 and M > 0 such that all v in D satisfy (6.2) al|wilx < D°J(v)-(<w ,Mlwlw)i y Vwex. Then it is well known that the problem (6.3) inf J(v) veD has a unique solution u in D characterized by (6.4) DJ(u) = 0. As usual, we associate with DJ the gradient g defined by:

## chapter-04-section-06-pc00017 | equation | low | PDF 367

[[FORMULA:f-p0367-06096]]

## chapter-04-section-06-pc00018 | ordinary-paragraph | high | PDF 367

where <., .> denotes the duality pairing X and X’. To solve Problem (6.3) we introduce the following general method of descent starting from u° € D: i 1°) for all m > 0, choose a direction of descent we X and define pe R, by (6.5) J(u" — p™w™)= inf J(u" — pw”), p20 u™—pwMeD 2°) set (6.6) = Uo we D: As shown below, this algorithm converges under reasonable assumptions.

## chapter-04-section-06-pc00019 | theorem | high | PDF 367

Theorem 6.1. Let D be a non empty, connected subset of X satisfying (6.1) and

## chapter-04-section-06-pc00020 | ordinary-paragraph | high | PDF 367,368

let J satisfy (6.2) in D. If, for each m, the direction of descent we X is such that (6.7) (g(u™),w™)x = Bilgu™)|lwl"x l x for some constant B > 0 independent of m, then the algorithm of descent (6.5) (6.6) we have for all v, and v, in D:

## chapter-04-section-06-pc00021 | equation | low | PDF 368

[[FORMULA:f-p0368-06106]]

## chapter-04-section-06-pc00022 | equation | low | PDF 368

[[FORMULA:f-p0368-06107]]

## chapter-04-section-06-pc00023 | ordinary-paragraph | high | PDF 368

Since D is connected, this means that 0v, + (1 — 0)v,€D. Next, we set

## chapter-04-section-06-pc00024 | equation | low | PDF 368

[[FORMULA:f-p0368-06108]]

## chapter-04-section-06-pc00025 | ordinary-paragraph | high | PDF 368

and we assume that the starting value u° is not the solution of (6.3) (otherwise the algorithm of descent yields the constant value u™ = u°). Again, D’ is convex and because J is continuous, D’ is obviously a closed subset of X. Let us establish that D’ is bounded. Taylor’s formula gives: J(v) = J(u®) + <DJ(u°), v— u°> + (1/2)D?J(u® + t(v — u°))-(v — u®, v— u°) for some t €(0, 1). To simplify, we denote

## chapter-04-section-06-pc00026 | equation | low | PDF 368

[[FORMULA:f-p0368-06112]]

## chapter-04-section-06-pc00027 | ordinary-paragraph | high | PDF 368

Then, for all v in D’, the convexity of D’ and (6.2) imply (6.8) J(v) > J(u°) — Ig? lixlle — lly + (@/2) lo — uli. But since J(v) < J(u°) this yields:

## chapter-04-section-06-pc00028 | equation | low | PDF 368

[[FORMULA:f-p0368-06116]]

## chapter-04-section-06-pc00029 | ordinary-paragraph | high | PDF 368

in other words: (6.9) lv — u? lly < (2/x) 19° lly. This proves the boundedness of D’. Observe also that J is bounded below in D’ because (6.8) and (6.9) imply (6.10) J(v) > J(u) — (2/a) lg? Ilz- Now we remark that the equation (6.5) defines a unique p™ > 0 for each pair u™ and w™ satisfying (6.7). Indeed, since by construction u”™ belongs to the interior of D, the mapping p > J(u” — pw") is strictly convex for all p such that u™ — pw™eD . Hence J(u™ — pw") has a unique minimum in D and this minimum is realized by a unique interior element of D, u" — p™w”™, with p™ > 0. Therefore u™ — p™w™ is characterized by:

## chapter-04-section-06-pc00030 | equation | low | PDF 368

[[FORMULA:f-p0368-06124]]

## chapter-04-section-06-pc00031 | ordinary-paragraph | medium | PDF 368,369

With (6.6) this can also be written: (6.11) CDI (a)W E, = ("aw tl). Note also that (6.11) gives: for some t e (0, 1), i.e.

## chapter-04-section-06-pc00032 | equation | low | PDF 369

[[FORMULA:f-p0369-06128]]

## chapter-04-section-06-pc00033 | equation | low | PDF 369

[[FORMULA:f-p0369-06129]]

## chapter-04-section-06-pc00034 | ordinary-paragraph | medium | PDF 369

Thus it follows from the convexity of D, (6.2) and (6.7) that

## chapter-04-section-06-pc00035 | equation | low | PDF 369

[[FORMULA:f-p0369-06131]]

## chapter-04-section-06-pc00036 | ordinary-paragraph | medium | PDF 369

whence we derive the following lower bound for pm:

## chapter-04-section-06-pc00037 | equation | low | PDF 369

[[FORMULA:f-p0369-06132]]

## chapter-04-section-06-pc00038 | equation | low | PDF 369

[[FORMULA:f-p0369-06133]]

## chapter-04-section-06-pc00039 | ordinary-paragraph | medium | PDF 369

Next, the sequence J(um) is by construction monotonically decreasing and so the sequence (u") is contained in D'. We have in particular:

## chapter-04-section-06-pc00040 | equation | low | PDF 369

[[FORMULA:f-p0369-06134]]

## chapter-04-section-06-pc00041 | ordinary-paragraph | medium | PDF 369

Therefore

## chapter-04-section-06-pc00042 | equation | low | PDF 369

[[FORMULA:f-p0369-06135]]

## chapter-04-section-06-pc00043 | ordinary-paragraph | medium | PDF 369

with t e (0, 1). Using again (6.7) and (6.2) we obtain:

## chapter-04-section-06-pc00044 | equation | low | PDF 369

[[FORMULA:f-p0369-06137]]

## chapter-04-section-06-pc00045 | ordinary-paragraph | medium | PDF 369

In view of (6.13) we can choose p = (B/M)( ll gm Il x/ ll wm Il x) thus getting

## chapter-04-section-06-pc00046 | equation | low | PDF 369

[[FORMULA:f-p0369-06139]]

## chapter-04-section-06-pc00047 | equation | low | PDF 369

[[FORMULA:f-p0369-06140]]

## chapter-04-section-06-pc00048 | ordinary-paragraph | medium | PDF 369

As the sequence J(um) is monotonically decreasing and bounded below (cf. (6.10)), it converges. In particular, (6.14) implies that

## chapter-04-section-06-pc00049 | equation | low | PDF 369

[[FORMULA:f-p0369-06142]]

## chapter-04-section-06-pc00050 | equation | low | PDF 369

[[FORMULA:f-p0369-06143]]

## chapter-04-section-06-pc00051 | ordinary-paragraph | low | PDF 369

α←u 81m Besides that we have

## chapter-04-section-06-pc00052 | equation | low | PDF 369

[[FORMULA:f-p0369-06144]]

## chapter-04-section-06-pc00053 | ordinary-paragraph | medium | PDF 369

with t e (0, 1). Thus (6.2) gives

## chapter-04-section-06-pc00054 | equation | low | PDF 369

[[FORMULA:f-p0369-06146]]

## chapter-04-section-06-pc00055 | equation | low | PDF 369

[[FORMULA:f-p0369-06147]]

## chapter-04-section-06-pc00056 | ordinary-paragraph | medium | PDF 369

i.e.

## chapter-04-section-06-pc00057 | equation | low | PDF 369

[[FORMULA:f-p0369-06148]]

## chapter-04-section-06-pc00058 | ordinary-paragraph | medium | PDF 369

Since (g) converges in X, this means that (um) is a Cauchy sequence in X, and therefore a converging sequence in X. Thus there exists u in D' with

## chapter-04-section-06-pc00059 | equation | low | PDF 369

[[FORMULA:f-p0369-06149]]

## chapter-04-section-06-pc00060 | ordinary-paragraph | medium | PDF 369,370

m→8 and furthermore (6.15) and the continuity of DJ imply that Hence J(u) = Min J(v). LJ veD The simple gradient and conjugate-gradient algorithms are among the most popular applications of the method of descent. The gradient algorithm is obtained by taking w™ = g” as direction of descent. Obviously this choice satisfies (6.7) and therefore Theorem 6.1 guarantees the local convergence of the simple gradient algorithm (6.5) (6.6) with w” = g”. The Polack-Ribiere variant of the conjugate-gradient algorithm is defined by choosing

## chapter-04-section-06-pc00061 | equation | low | PDF 370

[[FORMULA:f-p0370-06154]]

## chapter-04-section-06-pc00062 | equation | low | PDF 370

[[FORMULA:f-p0370-06155]]

## chapter-04-section-06-pc00063 | equation | low | PDF 370

[[FORMULA:f-p0370-06156]]

## chapter-04-section-06-pc00064 | ordinary-paragraph | high | PDF 370

with eG Ganda) 3 WV

## chapter-04-section-06-pc00065 | equation | low | PDF 370

[[FORMULA:f-p0370-06157]]

## chapter-04-section-06-pc00066 | ordinary-paragraph | high | PDF 370

ei — (Geeen d ee) (compare with formula (I.4.68)). Again, Theorem 6.1 implies that this scheme is convergent.

## chapter-04-section-06-pc00067 | theorem | high | PDF 370

Theorem 6.2. Let D be defined by (6.1) and (6.2) and let u® belong to D. Then the

## chapter-04-section-06-pc00068 | ordinary-paragraph | high | PDF 370

conjugate-gradient algorithm (6.5) (6.6) (6.16) and (6.17) converges in D.

## chapter-04-section-06-pc00069 | proof | high | PDF 370

Proof. Let us show that w™ defined by (6.16) and (6.17) satisfies (6.7). First observe

## chapter-04-section-06-pc00070 | ordinary-paragraph | high | PDF 370

that the property (6.11) and its consequence (6.12) established in Theorem 6.1 do not require (6.7) but only that (g”, w”)y be positive. Now, this positivity is easily proved by induction as it obviously holds for m = 0 and if it is true for m — 1 then (6.11) and (6.16) yield:

## chapter-04-section-06-pc00071 | equation | low | PDF 370

[[FORMULA:f-p0370-06165]]

## chapter-04-section-06-pc00072 | ordinary-paragraph | high | PDF 370

Hence

## chapter-04-section-06-pc00073 | ordinary-paragraph | high | PDF 370

Furthermore, (6.12) implies (6.18) e™ = Clg" x ]/[D7J™-(w™w™,) J with

## chapter-04-section-06-pc00074 | equation | low | PDF 370

[[FORMULA:f-p0370-06168]]

## chapter-04-section-06-pc00075 | ordinary-paragraph | low | PDF 370,371

Likewise, with the same notation we have Ilgm-112 IIgm-1 11x llgm-1 H12 D2 Jm-1.(wm-1,gm) D2 Jm-1.(wm-1,wm-1) in view of (6.18). Therefore (6.2) yields:

## chapter-04-section-06-pc00076 | equation | low | PDF 371

[[FORMULA:f-p0371-06170]]

## chapter-04-section-06-pc00077 | ordinary-paragraph | medium | PDF 371

whence

## chapter-04-section-06-pc00078 | equation | low | PDF 371

[[FORMULA:f-p0371-06171]]

## chapter-04-section-06-pc00079 | ordinary-paragraph | medium | PDF 371

Thus

## chapter-04-section-06-pc00080 | equation | low | PDF 371

[[FORMULA:f-p0371-06172]]

## chapter-04-section-06-pc00081 | ordinary-paragraph | medium | PDF 371

proving (6.7) with β = 1/(1 + M/α).

## chapter-04-section-06-pc00082 | subsection | medium | PDF 371

6.2. Least-Squares and Gradient Methods to Solve the Navier-Stokes Equations

## chapter-04-section-06-pc00083 | ordinary-paragraph | medium | PDF 371

We propose first to decouple the divergence-free constraint and the nonlinearity in the Navier-Stokes equations by means of a heuristic alternating direction method introduced by Glowinski [36]. Then we shall solve the resulting nonlinear equations with the gradient methods of the preceding section. Following the Peaceman-Rachford alternating directions algorithm we construct a sequence (u", pm) starting from an initial pair (u°, p°) by:

## chapter-04-section-06-pc00084 | ordinary-paragraph | medium | PDF 371

N umoum/ax; + rmum in Ω,

## chapter-04-section-06-pc00085 | equation | low | PDF 371

[[FORMULA:f-p0371-06174]]

## chapter-04-section-06-pc00086 | equation | low | PDF 371

[[FORMULA:f-p0371-06175]]

## chapter-04-section-06-pc00087 | equation | low | PDF 371

[[FORMULA:f-p0371-06176]]

## chapter-04-section-06-pc00088 | ordinary-paragraph | medium | PDF 371

N 0um+1/0x; + rmum+1 -V4um+1

## chapter-04-section-06-pc00089 | equation | low | PDF 371

[[FORMULA:f-p0371-06177]]

## chapter-04-section-06-pc00090 | equation | low | PDF 371

[[FORMULA:f-p0371-06178]]

## chapter-04-section-06-pc00091 | equation | low | PDF 371

[[FORMULA:f-p0371-06179]]

## chapter-04-section-06-pc00092 | ordinary-paragraph | medium | PDF 371,372

where the parameters rm are to be chosen as best as possible. Clearly, Problem (6.19) is like the Stokes problem which has been thoroughly studied in the no incompressibility constraint and is purely nonlinear. Problem (6.20) is of the form: N

## chapter-04-section-06-pc00093 | equation | low | PDF 372

[[FORMULA:f-p0372-06182]]

## chapter-04-section-06-pc00094 | ordinary-paragraph | high | PDF 372

(6.21) ds : ;

## chapter-04-section-06-pc00095 | equation | low | PDF 372

[[FORMULA:f-p0372-06184]]

## chapter-04-section-06-pc00096 | ordinary-paragraph | high | PDF 372

with both a linear elliptic and a nonlinear term in the left-hand side. This problem can be easily and conveniently generalized to fit into the abstract setting of Section 6.1. Let ||.||,, denote the familiar dual norm of X’ and let Ae P(X;X’ ) be a symmetric and X-elliptic operator in X, i.e. (6.22) <Av,>v yll>vl| ]z VoexX,y>0. Let G be a @?-mapping from X into X’ (with p > 2) and set (6.23) F(v) = Av + G(v) which is clearly a @’-mapping from X into X’. Our problem is: (6.24) Find uin X such that F(u) = 0. Obviously, Problem (6.21) is a particular case of (6.24) with

## chapter-04-section-06-pc00097 | equation | low | PDF 372

[[FORMULA:f-p0372-06190]]

## chapter-04-section-06-pc00098 | equation | low | PDF 372

[[FORMULA:f-p0372-06191]]

## chapter-04-section-06-pc00099 | ordinary-paragraph | high | PDF 372

We intend to solve Problem (6.24) by replacing it with an equivalent leastsquares problem. To this end, consider the functional:

## chapter-04-section-06-pc00100 | equation | low | PDF 372

[[FORMULA:f-p0372-06193]]

## chapter-04-section-06-pc00101 | ordinary-paragraph | high | PDF 372

where ||. ||, is defined by (6.25) Ifllx = <A 6A”. We are going to see below that, because A is symmetric and elliptic, ||. ||, is a norm on X’ equivalent to the dual norm and the corresponding functional J is strictly convex and has a unique minimum.

## chapter-04-section-06-pc00102 | lemma | high | PDF 372

Lemma 6.1. The mapping f > <A~‘f, f>*? is anorm on X' equivalent to the dual

## chapter-04-section-06-pc00103 | ordinary-paragraph | high | PDF 372

norm.

## chapter-04-section-06-pc00104 | proof | high | PDF 372

Proof. From (6.22) we infer that

## chapter-04-section-06-pc00105 | ordinary-paragraph | high | PDF 372

ASL eA Tig.

## chapter-04-section-06-pc00106 | equation | low | PDF 372

[[FORMULA:f-p0372-06197]]

## chapter-04-section-06-pc00107 | equation | low | PDF 373

[[FORMULA:f-p0373-06198]]

## chapter-04-section-06-pc00108 | ordinary-paragraph | medium | PDF 373

On the other hand, we set

## chapter-04-section-06-pc00109 | equation | low | PDF 373

[[FORMULA:f-p0373-06199]]

## chapter-04-section-06-pc00110 | ordinary-paragraph | medium | PDF 373

Therefore

## chapter-04-section-06-pc00111 | equation | low | PDF 373

[[FORMULA:f-p0373-06200]]

## chapter-04-section-06-pc00112 | ordinary-paragraph | medium | PDF 373

and thus

## chapter-04-section-06-pc00113 | equation | low | PDF 373

[[FORMULA:f-p0373-06201]]

## chapter-04-section-06-pc00114 | ordinary-paragraph | medium | PDF 373

Summing up, we get

## chapter-04-section-06-pc00115 | equation | low | PDF 373

[[FORMULA:f-p0373-06202]]

## chapter-04-section-06-pc00116 | equation | low | PDF 373

[[FORMULA:f-p0373-06203]]

## chapter-04-section-06-pc00117 | theorem | medium | PDF 373

Theorem 6.3. Let u be a nonsingular solution of Problem (6.24). Then the functional 

## chapter-04-section-06-pc00118 | ordinary-paragraph | medium | PDF 373

J defined by

## chapter-04-section-06-pc00119 | equation | low | PDF 373

[[FORMULA:f-p0373-06205]]

## chapter-04-section-06-pc00120 | equation | low | PDF 373

[[FORMULA:f-p0373-06206]]

## chapter-04-section-06-pc00121 | ordinary-paragraph | medium | PDF 373

is strictly convex in a neighborhood of u.

## chapter-04-section-06-pc00122 | proof | medium | PDF 373

Proof. Taking into account the symmetry of A-', the first two derivatives of J

## chapter-04-section-06-pc00123 | ordinary-paragraph | medium | PDF 373

have the expression:

## chapter-04-section-06-pc00124 | equation | low | PDF 373

[[FORMULA:f-p0373-06207]]

## chapter-04-section-06-pc00125 | equation | low | PDF 373

[[FORMULA:f-p0373-06208]]

## chapter-04-section-06-pc00126 | equation | low | PDF 373

[[FORMULA:f-p0373-06209]]

## chapter-04-section-06-pc00127 | ordinary-paragraph | medium | PDF 373

(6.29) D² J(v)·(w, z) =(A-1(DF(u)· 2), DF(v)· w> + <A-1(F(v)), D² F(v)·(w, 2)>.

## chapter-04-section-06-pc00128 | ordinary-paragraph | medium | PDF 373

Now, recall that u is a nonsingular solution of Problem (6.24) if

## chapter-04-section-06-pc00129 | equation | low | PDF 373

[[FORMULA:f-p0373-06212]]

## chapter-04-section-06-pc00130 | ordinary-paragraph | medium | PDF 373

Hence (6.29) yields:

## chapter-04-section-06-pc00131 | equation | low | PDF 373

[[FORMULA:f-p0373-06214]]

## chapter-04-section-06-pc00132 | equation | low | PDF 373

[[FORMULA:f-p0373-06215]]

## chapter-04-section-06-pc00133 | ordinary-paragraph | medium | PDF 373

Thus (6.26) implies that

## chapter-04-section-06-pc00134 | equation | low | PDF 373

[[FORMULA:f-p0373-06217]]

## chapter-04-section-06-pc00135 | equation | low | PDF 373

[[FORMULA:f-p0373-06218]]

## chapter-04-section-06-pc00136 | equation | low | PDF 373

[[FORMULA:f-p0373-06219]]

## chapter-04-section-06-pc00137 | ordinary-paragraph | medium | PDF 373

since DF(u) is an isomorphism of X onto X'. But the mapping D? J is continuous in X (because F is a C'-mapping); therefore there exists p > 0 such that

## chapter-04-section-06-pc00138 | equation | low | PDF 373

[[FORMULA:f-p0373-06221]]

## chapter-04-section-06-pc00139 | ordinary-paragraph | medium | PDF 373,374

for all ve S(u; p) = {ve X; Ilu - ull x ≤ p}. Hence ie. J is strictly convex in S(u; p). CL]

## chapter-04-section-06-pc00140 | equation | low | PDF 374

[[FORMULA:f-p0374-06223]]

## chapter-04-section-06-pc00141 | ordinary-paragraph | high | PDF 374

(6.32) inf (1/2)<A*F(v), F(v)) ve S(u;p) and this solution can be achieved by the gradient and conjugate-gradient methods of Section 6.1. Indeed, assume that D*G is bounded on all bounded subsets of X so that F, DF and D’F are also bounded there, and assume that u is a nonsingular solution of (6.24). Then we already know that the first part of (6.2) holds on the ball S(u;p), while the second part stems from (6.30), (6.26), the isomorphism property of DF(u) and the continuity of D?J. In addition, the boundedness of F implies that J is bounded in S(u;p). Thus, by choosing a starting value u° in S(u; p) and setting J° = J(u°) we can take

## chapter-04-section-06-pc00142 | equation | low | PDF 374

[[FORMULA:f-p0374-06228]]

## chapter-04-section-06-pc00143 | ordinary-paragraph | high | PDF 374

and Theorems 6.1 and 6.2 guarantee the convergence of the gradient and conjugategradient algorithms. Let us examine the practical implementation of the simple gradient method. The symmetry and ellipticity of A induce us to equip X with the scalar product:

## chapter-04-section-06-pc00144 | equation | low | PDF 374

[[FORMULA:f-p0374-06229]]

## chapter-04-section-06-pc00145 | ordinary-paragraph | high | PDF 374

and associated norm ||u||, = <Au,u>"*. Hence, in view of(6 .28), the gradient g(v) is defined by

## chapter-04-section-06-pc00146 | equation | low | PDF 374

[[FORMULA:f-p0374-06231]]

## chapter-04-section-06-pc00147 | equation | low | PDF 374

[[FORMULA:f-p0374-06232]]

## chapter-04-section-06-pc00148 | equation | low | PDF 374

[[FORMULA:f-p0374-06233]]

## chapter-04-section-06-pc00149 | ordinary-paragraph | high | PDF 374

Le: (6.33) g(v) = A“'(DF(v)A)! F(v). Thus one step of the simple gradient algorithm can be decomposed into the following operations: 1°) compute gata Sku),

## chapter-04-section-06-pc00150 | equation | low | PDF 374

[[FORMULA:f-p0374-06235]]

## chapter-04-section-06-pc00151 | ordinary-paragraph | high | PDF 374

2°) then minimize J(u” — pg™) with respect to p, where

## chapter-04-section-06-pc00152 | equation | low | PDF 374

[[FORMULA:f-p0374-06236]]

## chapter-04-section-06-pc00153 | ordinary-paragraph | medium | PDF 374,375

Each iteration requires the resolution of two linear problems relative to the operator A plus the determination of p”. As an example, let us explicit the pw) is a fourth-degree polynomial because F is a polynomial of degree two. Therefore Taylor's expansion of J(um - pg") reduces to:

## chapter-04-section-06-pc00154 | equation | low | PDF 375

[[FORMULA:f-p0375-06237]]

## chapter-04-section-06-pc00155 | equation | low | PDF 375

[[FORMULA:f-p0375-06238]]

## chapter-04-section-06-pc00156 | ordinary-paragraph | medium | PDF 375

—-(p3/6)D3 J(um) ·(gm, g"m, gm) + (p4 /24)D4 J(um)·(gm,g",g",gm), where the third and fourth derivatives of J have the simple expression:

## chapter-04-section-06-pc00157 | equation | low | PDF 375

[[FORMULA:f-p0375-06239]]

## chapter-04-section-06-pc00158 | ordinary-paragraph | low | PDF 375

<(uu).(u)dzq(uw8).(un)dz-V>=(u8uuu8).(un)a Summing up, to solve Problem (6.21), each iteration of the simple gradient algorithm runs as follows:

## chapter-04-section-06-pc00159 | ordinary-paragraph | low | PDF 375

1°) given u" e H(Q), compute the solution zm e H (Q) of N Cuy(oum/0x;) -f in Ω,

## chapter-04-section-06-pc00160 | equation | low | PDF 375

[[FORMULA:f-p0375-06242]]

## chapter-04-section-06-pc00161 | equation | low | PDF 375

[[FORMULA:f-p0375-06243]]

## chapter-04-section-06-pc00162 | ordinary-paragraph | medium | PDF 375

2°) find the solution g" e H1(Q) of v(grad g", grad v) + c(g", v) = v(grad z", grad v) N

## chapter-04-section-06-pc00163 | equation | low | PDF 375

[[FORMULA:f-p0375-06245]]

## chapter-04-section-06-pc00164 | ordinary-paragraph | medium | PDF 375

Vve H(2), g" = 0 on F; 3°) compute

## chapter-04-section-06-pc00165 | equation | low | PDF 375

[[FORMULA:f-p0375-06247]]

## chapter-04-section-06-pc00166 | equation | low | PDF 375

[[FORMULA:f-p0375-06248]]

## chapter-04-section-06-pc00167 | equation | low | PDF 375

[[FORMULA:f-p0375-06249]]

## chapter-04-section-06-pc00168 | equation | low | PDF 375

[[FORMULA:f-p0375-06250]]

## chapter-04-section-06-pc00169 | ordinary-paragraph | low | PDF 375

4°) find the solution vm e H'(Q) of N v4vm + cvm = -v4gm + cgm + ∑ (u0gm/0x; + gm0um/0x) in Ω,

## chapter-04-section-06-pc00170 | equation | low | PDF 375

[[FORMULA:f-p0375-06252]]

## chapter-04-section-06-pc00171 | equation | low | PDF 375

[[FORMULA:f-p0375-06253]]

## chapter-04-section-06-pc00172 | ordinary-paragraph | medium | PDF 375

5°) compute N gm0gm/0xj,

## chapter-04-section-06-pc00173 | equation | low | PDF 375

[[FORMULA:f-p0375-06254]]

## chapter-04-section-06-pc00174 | equation | low | PDF 375

[[FORMULA:f-p0375-06255]]

## chapter-04-section-06-pc00175 | equation | low | PDF 375

[[FORMULA:f-p0375-06256]]

## chapter-04-section-06-pc00176 | equation | low | PDF 375

[[FORMULA:f-p0375-06257]]

## chapter-04-section-06-pc00177 | equation | low | PDF 375

[[FORMULA:f-p0375-06258]]

## chapter-04-section-06-pc00178 | equation | low | PDF 375

[[FORMULA:f-p0375-06259]]

## chapter-04-section-06-pc00179 | equation | low | PDF 376

[[FORMULA:f-p0376-06260]]

## chapter-04-section-06-pc00180 | equation | low | PDF 376

[[FORMULA:f-p0376-06261]]

## chapter-04-section-06-pc00181 | ordinary-paragraph | high | PDF 376

7°) compute (6.39) D* J(u”): (g”,8", 8", 8") = vIw"lt,o + cllw"llo,03 8°) find the positive root p” of

## chapter-04-section-06-pc00182 | equation | low | PDF 376

[[FORMULA:f-p0376-06263]]

## chapter-04-section-06-pc00183 | ordinary-paragraph | high | PDF 376

and update u”™ by:

## chapter-04-section-06-pc00184 | equation | low | PDF 376

[[FORMULA:f-p0376-06264]]

## chapter-04-section-06-pc00185 | ordinary-paragraph | high | PDF 376

Each iteration requires the solution of four Dirichlet problems. The implementation of the conjugate-gradient algorithm is much like above and is left as an exercise.

## chapter-04-section-06-pc00186 | subsection | high | PDF 376

6.3. Newton’s Method and the Continuation Method

## chapter-04-section-06-pc00187 | ordinary-paragraph | high | PDF 376

The methods discussed here are intended to solve the complete Navier-Stokes equations: incompressible and nonlinear. More generally, we want to solve equations of the type introduced in Section 3.1, namely: (6.40) F(A,u) = 0, where F is a @?-mapping (p > 1) defined on A x X with values in 2, X and & being two Banach spaces and A an interval of R. Let us fix 4 for the moment and assume that u = u(J)e X is a nonsingular solution of (6.40), 1.c.

## chapter-04-section-06-pc00188 | equation | low | PDF 376

[[FORMULA:f-p0376-06268]]

## chapter-04-section-06-pc00189 | ordinary-paragraph | high | PDF 376

Then we know from the inverse function theorem (and also from the material of Section 3.2) that there exists a closed ball S(u;«) where the equation (6.40) has no other solution than u. Since u is an isolated solution of (6.40) and since F is at least differentiable, an efficient way to approximate u is the Newton’s algorithm: starting from an initial guess u°, construct the sequence (u") in X by: (6.41) tt" Dar uel OR et) See) or equivalently

## chapter-04-section-06-pc00190 | equation | low | PDF 376

[[FORMULA:f-p0376-06272]]

## chapter-04-section-06-pc00191 | ordinary-paragraph | high | PDF 376,377

As D,F(A,u) is a linear operator, each step of Newton’s method requires the solution of a different linear problem relative to D, F(A, u"). If this is too costly, (6.42) u™* =u" —[D,F(A,u°))!-FA,u")

## chapter-04-section-06-pc00192 | equation | low | PDF 377

[[FORMULA:f-p0377-06274]]

## chapter-04-section-06-pc00193 | ordinary-paragraph | high | PDF 377

or equivalently

## chapter-04-section-06-pc00194 | equation | low | PDF 377

[[FORMULA:f-p0377-06275]]

## chapter-04-section-06-pc00195 | ordinary-paragraph | high | PDF 377

We are going to prove that both schemes are convergent.

## chapter-04-section-06-pc00196 | theorem | high | PDF 377

Theorem 6.3. Assume that D, F(A, v) is Lipschitz-continuous with respect to

## chapter-04-section-06-pc00197 | ordinary-paragraph | high | PDF 377

v in the ball S(u; a), i.e. there exists a constant K > 0 such that (6.43) ||D ,(4F,v ) —D ,F(A, 0*|) g ax,a)< K||—v v* ly Vo, v* e S(u;.@). Then there exists an x with 0 < « < « such that for each initial guess u° in S(u; a’) the Newton’s algorithm (6.41) determines a unique sequence (u") < S(u;«’) that converges to the solution u of (6.40). Furthermore the convergence is quadratic: (6.44) ull ln” = ul2um C10,

## chapter-04-section-06-pc00198 | ordinary-paragraph | high | PDF 377

Likewise, there exists an x" with 0 < «" < « such that for each initial value u° in S(u; a”) the scheme (6.42) determines a unique sequence (u") < S(u; a”) that converges to u. But the convergence is only linear: (6.45) tee ail Clu — ail Cre 1.

## chapter-04-section-06-pc00199 | proof | high | PDF 377

Proof. To begin with, it follows from (6.43) and Lemma 3.3 that there exists an

## chapter-04-section-06-pc00200 | ordinary-paragraph | high | PDF 377

a with O < « < «such that D, F(A, v) is an isomorphism ofX onto & for all v in S(u; x’). Indeed, if we take F, = F, a, = v,y = ||[D, F(A, wu) | ga-xy),U = ||D FO, u) — D, F(A, v)|| yx.) then Lemma 3.3 says that D, F(A, v) is an isomorphism of X onto % provided that yu < 1. In view of( 6.43), this inequality holds if we choose a’ < Min(«, 1/(yK)). In particular, we can take (6.46) a’ < 1/(2yK) and formula (3.16) gives the bound (6.47) ILD, F(A, 0%1) Ilg @sx)< 27.

## chapter-04-section-06-pc00201 | ordinary-paragraph | high | PDF 377

Now let us prove that when u° belongs to S(u; «’) with «’ satisfying (6.46) then the scheme (6.41) defines a sequence (u”) in S(u; «’) that converges to u. We proceed by induction: suppose that u” belongs to S(u; a’); then [D, F(A, u")]~' exists and

## chapter-04-section-06-pc00202 | equation | low | PDF 377

[[FORMULA:f-p0377-06295]]

## chapter-04-section-06-pc00203 | ordinary-paragraph | high | PDF 377

In other words Pe y= DEA)L F Ou) — Fu") = DF,4") -(u— u")|

## chapter-04-section-06-pc00204 | ordinary-paragraph | high | PDF 377

1 = pari.uy” | [D,F(A,u" + t(u — u")) — D,F(A,u")]-(u — u") dt. 0

## chapter-04-section-06-pc00205 | equation | low | PDF 378

[[FORMULA:f-p0378-06298]]

## chapter-04-section-06-pc00206 | ordinary-paragraph | medium | PDF 378

and since α'yK ≤ 1/2 this yields

## chapter-04-section-06-pc00207 | equation | low | PDF 378

[[FORMULA:f-p0378-06300]]

## chapter-04-section-06-pc00208 | ordinary-paragraph | low | PDF 378

Hence un+1 belongs to S(u; α') and these two inequalities show that the sequence (u") converges quadratically to u. Next, consider the scheme (6.42). Like above, we start with u? in S(u; α") for some α" ≤ α' that we shall specify subsequently. Then (6.42) determines a unique sequence (u") and similarly, we have: un+1 - u =[DF(n,u°)]-1 [DuF(,un + t(u - u")) - DuF(,u°)]·(u - u")dt. Jo Hence assuming that u belongs also to S(u; α") we derive:

## chapter-04-section-06-pc00209 | equation | low | PDF 378

[[FORMULA:f-p0378-06304]]

## chapter-04-section-06-pc00210 | equation | low | PDF 378

[[FORMULA:f-p0378-06305]]

## chapter-04-section-06-pc00211 | ordinary-paragraph | medium | PDF 378

Therefore, by choosing

## chapter-04-section-06-pc00212 | equation | low | PDF 378

[[FORMULA:f-p0378-06306]]

## chapter-04-section-06-pc00213 | ordinary-paragraph | medium | PDF 378

we find that un+1 belongs to S(u;, α") and that the sequence (u^) converges linearly to u. 口 Let us apply Theorem 6.3 to solve the familiar class of problems

## chapter-04-section-06-pc00214 | equation | low | PDF 378

[[FORMULA:f-p0378-06308]]

## chapter-04-section-06-pc00215 | equation | low | PDF 378

[[FORMULA:f-p0378-06309]]

## chapter-04-section-06-pc00216 | ordinary-paragraph | medium | PDF 378

where X and Y are two Banach spaces, 4 is a compact interval of R, Te (Y; X) and G is a &?-mapping from A x X into Y with D²G bounded on all bounded subsets of 4 x X. This last property implies the Lipschitz condition (6.43). Therefore, if X → u() is a branch of nonsingular solutions of (6.48), Newton's method defines a locally (and quadratically) convergent algorithm:

## chapter-04-section-06-pc00217 | equation | low | PDF 378

[[FORMULA:f-p0378-06312]]

## chapter-04-section-06-pc00218 | equation | low | PDF 378

[[FORMULA:f-p0378-06313]]

## chapter-04-section-06-pc00219 | ordinary-paragraph | medium | PDF 378

Likewise, the variant (6.42) is also locally (but linearly) convergent:

## chapter-04-section-06-pc00220 | equation | low | PDF 378

[[FORMULA:f-p0378-06315]]

## chapter-04-section-06-pc00221 | equation | low | PDF 378

[[FORMULA:f-p0378-06316]]

## chapter-04-section-06-pc00222 | ordinary-paragraph | low | PDF 378

As an example, consider the Navier-Stokes equations: N -vu+

## chapter-04-section-06-pc00223 | equation | low | PDF 378

[[FORMULA:f-p0378-06317]]

## chapter-04-section-06-pc00224 | equation | low | PDF 378

[[FORMULA:f-p0378-06318]]

## chapter-04-section-06-pc00225 | ordinary-paragraph | medium | PDF 378

in Q

## chapter-04-section-06-pc00226 | equation | low | PDF 378

[[FORMULA:f-p0378-06319]]

## chapter-04-section-06-pc00227 | equation | low | PDF 378

[[FORMULA:f-p0378-06320]]

## chapter-04-section-06-pc00228 | equation | low | PDF 378

[[FORMULA:f-p0378-06321]]

## chapter-04-section-06-pc00229 | ordinary-paragraph | medium | PDF 379

the following correspondence: X = H(Ω) × L(Ω),

## chapter-04-section-06-pc00230 | equation | low | PDF 379

[[FORMULA:f-p0379-06323]]

## chapter-04-section-06-pc00231 | ordinary-paragraph | medium | PDF 379

N

## chapter-04-section-06-pc00232 | equation | low | PDF 379

[[FORMULA:f-p0379-06324]]

## chapter-04-section-06-pc00233 | equation | low | PDF 379

[[FORMULA:f-p0379-06325]]

## chapter-04-section-06-pc00234 | ordinary-paragraph | low | PDF 379

u;(du/0x;) - Moreover, (u, p) is a solution of (6.51) iff u = (u, p/v) is a solution of (6.48). Then Newton's algorithm (6.49) reads: Find (ur+1, pn+1)eH(Q) × L2(Ω) such that N

## chapter-04-section-06-pc00235 | equation | low | PDF 379

[[FORMULA:f-p0379-06328]]

## chapter-04-section-06-pc00236 | equation | low | PDF 379

[[FORMULA:f-p0379-06329]]

## chapter-04-section-06-pc00237 | equation | low | PDF 379

[[FORMULA:f-p0379-06330]]

## chapter-04-section-06-pc00238 | ordinary-paragraph | low | PDF 379

u,(0u/0x;) + f (M

## chapter-04-section-06-pc00239 | equation | low | PDF 379

[[FORMULA:f-p0379-06331]]

## chapter-04-section-06-pc00240 | ordinary-paragraph | medium | PDF 379

in Ω,

## chapter-04-section-06-pc00241 | equation | low | PDF 379

[[FORMULA:f-p0379-06332]]

## chapter-04-section-06-pc00242 | equation | low | PDF 379

[[FORMULA:f-p0379-06333]]

## chapter-04-section-06-pc00243 | ordinary-paragraph | medium | PDF 379

on F. Similarly, the simpler variant (6.50) reads: Find (un+1, pn+1)∈ H(Q) x L(Ω) such that N

## chapter-04-section-06-pc00244 | equation | low | PDF 379

[[FORMULA:f-p0379-06335]]

## chapter-04-section-06-pc00245 | ordinary-paragraph | low | PDF 379

N [(①u"/Cx;)(u} - u,) + u)(①u/0x;)] + f

## chapter-04-section-06-pc00246 | equation | low | PDF 379

[[FORMULA:f-p0379-06336]]

## chapter-04-section-06-pc00247 | equation | low | PDF 379

[[FORMULA:f-p0379-06337]]

## chapter-04-section-06-pc00248 | equation | low | PDF 379

[[FORMULA:f-p0379-06338]]

## chapter-04-section-06-pc00249 | equation | low | PDF 379

[[FORMULA:f-p0379-06339]]

## chapter-04-section-06-pc00250 | ordinary-paragraph | medium | PDF 379

Note that in either case, the next iterate (un+1, pn+1) is independent of p". Also, DuF(, u) is obviously Lipschitz-continuous since D² G(, u) is constant. Hence, if (u, p) is a nonsingular solution of (6.51), starting from an initial guess u? sufficiently near u and an arbitrary p°, the scheme (6.52) (resp. (6.53)) determines a unique sequence (u, p") that converges quadratically (resp. linearly) to u = (u, p/v). Of course, if u = u(l) belongs to a branch of nonsingular solutions on a compact interval A, this result stays valid for all X in A with constants independent of X.

## chapter-04-section-06-pc00251 | ordinary-paragraph | low | PDF 379,380

The drawback of Newton's method is that its convergence can only be insured when the first guess u° is sufficiently near the solution u. If this solution is part of a branch of nonsingular solutions and if we know the solution at a neighboring point, say u(A - Ax) for an adequate increment AX, then we can derive from this value the first guess to start Newton's algorithm. This is the method of continuation; let us describe it more precisely. Assume that X → u(l) is a branch u(2) and we can differentiate both sides of (6.40): VAeA,

## chapter-04-section-06-pc00252 | equation | low | PDF 380

[[FORMULA:f-p0380-06345]]

## chapter-04-section-06-pc00253 | equation | low | PDF 380

[[FORMULA:f-p0380-06346]]

## chapter-04-section-06-pc00254 | ordinary-paragraph | medium | PDF 380

i.e. we find a first order differential equation of the form

## chapter-04-section-06-pc00255 | equation | low | PDF 380

[[FORMULA:f-p0380-06347]]

## chapter-04-section-06-pc00256 | equation | low | PDF 380

[[FORMULA:f-p0380-06348]]

## chapter-04-section-06-pc00257 | ordinary-paragraph | medium | PDF 380

where

## chapter-04-section-06-pc00258 | equation | low | PDF 380

[[FORMULA:f-p0380-06349]]

## chapter-04-section-06-pc00259 | ordinary-paragraph | medium | PDF 380

The simplest way to solve (6.55) is to use the one-step, explicit, Euler's method; this induces us to choose

## chapter-04-section-06-pc00260 | equation | low | PDF 380

[[FORMULA:f-p0380-06351]]

## chapter-04-section-06-pc00261 | equation | low | PDF 380

[[FORMULA:f-p0380-06352]]

## chapter-04-section-06-pc00262 | ordinary-paragraph | low | PDF 380

In other words u°(l) is defined by D,F( - 4,u( - 42))·(u(2) -u(2 - A))

## chapter-04-section-06-pc00263 | equation | low | PDF 380

[[FORMULA:f-p0380-06353]]

## chapter-04-section-06-pc00264 | equation | low | PDF 380

[[FORMULA:f-p0380-06354]]

## chapter-04-section-06-pc00265 | ordinary-paragraph | low | PDF 380

Let us estimate the error u(l) - u°(2). From (6.55) we infer that: 入

## chapter-04-section-06-pc00266 | equation | low | PDF 380

[[FORMULA:f-p0380-06356]]

## chapter-04-section-06-pc00267 | ordinary-paragraph | low | PDF 380

Φ(μ)dμ; Jxsubtracting (6.56) we obtain

## chapter-04-section-06-pc00268 | equation | low | PDF 380

[[FORMULA:f-p0380-06358]]

## chapter-04-section-06-pc00269 | ordinary-paragraph | low | PDF 380

p(μ)dμ - Φ( -- △x)· 4 p'(0u)·(u - A + 4x)dμ. J- Hence

## chapter-04-section-06-pc00270 | equation | low | PDF 380

[[FORMULA:f-p0380-06359]]

## chapter-04-section-06-pc00271 | ordinary-paragraph | low | PDF 380

D∈(A-,A) Thus Il u(2) - u°(4)Il x is O(42)²) and if 4X is small enough, u(2) defined by (6.56) is an adequate starting value for Newton's algorithm. As an example, let us explicit formula (6.57) for the Navier-Stokes equation (6.51). To simplify, we set

## chapter-04-section-06-pc00272 | equation | low | PDF 380

[[FORMULA:f-p0380-06363]]

## chapter-04-section-06-pc00273 | ordinary-paragraph | low | PDF 380

Then (6.57) amounts to [D .((D -r)nD - )'a + ()ng·((D - r)nD - )"a]L- = ()ng or equivalently

## chapter-04-section-06-pc00274 | equation | low | PDF 381

[[FORMULA:f-p0381-06366]]

## chapter-04-section-06-pc00275 | ordinary-paragraph | low | PDF 381

+ ou;(2)(du(2 - 4x)/0xj] u;(2 - 4x)(0u(2 - 42)/0xj) - + Setting du(l) = (Su(4), ( - 42)8p(2)), this problem also reads:

## chapter-04-section-06-pc00276 | ordinary-paragraph | low | PDF 381

Find (8u(2), op(a))∈ H(Q) × L(Ω) such that N -(1/(x - 42))u(2) + > ∑ [u;(1 - 4)(08u(2)/0xj) + ou;(a)(0u(2 - A2)/0x;)]

## chapter-04-section-06-pc00277 | equation | low | PDF 381

[[FORMULA:f-p0381-06370]]

## chapter-04-section-06-pc00278 | ordinary-paragraph | medium | PDF 381

+ grad 8p(2) = (4x/( - 4))| f in S,

## chapter-04-section-06-pc00279 | equation | low | PDF 381

[[FORMULA:f-p0381-06372]]

## chapter-04-section-06-pc00280 | equation | low | PDF 381

[[FORMULA:f-p0381-06373]]

## chapter-04-section-06-pc00281 | equation | low | PDF 381

[[FORMULA:f-p0381-06374]]

## chapter-04-section-06-pc00282 | ordinary-paragraph | medium | PDF 381

Note that this problem is analogous to one iteration of Newton's algorithm.

## chapter-04-section-06-pc00283 | remark | medium | PDF 381

Remark 6.1. By using a suitable discrete derivative, a Newton-type algorithm can

## chapter-04-section-06-pc00284 | ordinary-paragraph | medium | PDF 381

also be derived to solve non differentiable schemes like the ones analyzed in Sections 3.4 and 5.1. Under adequate hypotheses a nearly quadratic convergence can be achieved (cf. Girault & Raviart [34]).

## chapter-04-section-06-pc00285 | remark | medium | PDF 381

Remark 6.2. We can also solve (6.55) with a Runge-Kutta method or with an

## chapter-04-section-06-pc00286 | ordinary-paragraph | medium | PDF 381

explicit multistep method. The proof of the corresponding error estimate is pretty much like above.
