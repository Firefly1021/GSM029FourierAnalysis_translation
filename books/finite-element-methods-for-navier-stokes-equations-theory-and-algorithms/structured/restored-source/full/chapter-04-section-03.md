# Restored-source review candidate: chapter-04-section-03



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 311 / printed 297



[p0311-b0003 | ordinary-paragraph | high] with vector potentials in the space:

[p0311-b0004 | equation | low] Y, = {oe L7(Q)*; dive H'(Q), cudre H3l(Q) >, onl = 08.

[p0311-b0005 | section | high] § 3. Approximation of Branches of Nonsingular Solutions

[p0311-b0006 | ordinary-paragraph | high] As proved in the preceding paragraph, the Navier-Stokes equations have in

[p0311-b0007 | ordinary-paragraph | high] general more than one solution, unless the data (namely, the viscosity and

[p0311-b0008 | ordinary-paragraph | high] external forces) satisfy very stringent requirements. However, it can also be

[p0311-b0009 | ordinary-paragraph | high] shown that in many practical examples these solutions are mostly isolated, i.e.

[p0311-b0010 | ordinary-paragraph | high] there exists a neighborhood in which each solution is unique. Furthermore, it

[p0311-b0011 | ordinary-paragraph | high] can be established that the solutions depend continuously on the viscosity. Thus,

[p0311-b0012 | ordinary-paragraph | high] as the viscosity varies along an interval, each solution of the Navier-Stokes

[p0311-b0013 | ordinary-paragraph | high] equations describes an isolated branch. In particular, this means that the bifurca-

[p0311-b0014 | ordinary-paragraph | high] tion phenomenon is rare. This situation, very frequently encountered in practice,

[p0311-b0015 | ordinary-paragraph | high] is expressed mathematically by the notion of branches of nonsingular solutions.

[p0311-b0016 | ordinary-paragraph | high] This paragraph proposes and analyzes several approximations of branches

[p0311-b0017 | ordinary-paragraph | high] of nonsingular solutions pertaining to a wide class of nonlinear problems, includ-

[p0311-b0018 | ordinary-paragraph | high] ing the Navier-Stokes problem. The analysis, based on a general form of the

[p0311-b0019 | ordinary-paragraph | high] implicit function theorem, is a variant of a broader theory developed by Brezzi,

[p0311-b0020 | ordinary-paragraph | high] Rappaz & Raviart [14]. The version that we present here is due to Crouzeix [22].

[p0311-b0021 | subsection | high] 3.1. An Abstract Framework

[p0311-b0022 | ordinary-paragraph | high] Let X and Z be two Banach spaces and A a compact interval of the real line R.

[p0311-b0023 | ordinary-paragraph | high] We are given a @’-mapping (p > 1)

[p0311-b0024 | ordinary-paragraph | high] F:(AujeA x X 9 FU wer

[p0311-b0025 | ordinary-paragraph | high] and we want to solve the equation

[p0311-b0026 | ordinary-paragraph | high] (3.1) F(A,u) = 0,

[p0311-b0027 | ordinary-paragraph | high] ie. we want to find pairs (A,u)e A x X solutions of( 3.1).

[p0311-b0028 | ordinary-paragraph | high] Let {(A, u(A)); A € A} be a branch of solutions of equation (3.1). This means that

[p0311-b0029 | ordinary-paragraph | high] (3.2) 4 — u(A) is a continuous function from A into X;

[p0311-b0030 | ordinary-paragraph | high] (3.3) F(A, u(A)) = 0.

[p0311-b0031 | ordinary-paragraph | high] Moreover, we suppose that these solutions are nonsingular in the sense that:

[p0311-b0032 | ordinary-paragraph | high] (3.4) D, F(A, u(A)) is an isomorphism from X onto # for all Ae A.

[p0311-b0033 | ordinary-paragraph | high] As an immediate consequence of (3.4), it follows from the implicit function

## PDF 312 / printed 298



[p0312-b0005 | ordinary-paragraph | high] above framework. We first set:

[p0312-b0006 | equation | low] X = C = H1(Q) × L(Ω),

[p0312-b0007 | equation | low] (3.5)

[p0312-b0008 | ordinary-paragraph | high] and we introduce the intermediate space

[p0312-b0009 | equation | low] g·nds = 0,0≤i≤p

[p0312-b0010 | equation | low] (3.6)

[p0312-b0011 | equation | low] Y = H-1(Q)

[p0312-b0012 | ordinary-paragraph | low] JFi

[p0312-b0013 | ordinary-paragraph | high] Next we define a linear operator T as follows: given (f*, g*)e Y, we denote by

[p0312-b0014 | ordinary-paragraph | low]      n    xa(*a * = (* *)

[p0312-b0015 | ordinary-paragraph | high] equations:

[p0312-b0016 | equation | low] -u + grad p* = f*

[p0312-b0017 | ordinary-paragraph | high] in Ω,

[p0312-b0018 | equation | low] divu, = 0

[p0312-b0019 | equation | low] (3.7)

[p0312-b0020 | equation | low] u*ir= g*·

[p0312-b0021 | ordinary-paragraph | high] Finally, with the data (f,g)e Y we associate a ∞-mapping G from R+ x X into

[p0312-b0022 | ordinary-paragraph | high] Y defined by

[p0312-b0023 | ordinary-paragraph | low] (u;8v/0x;-f

[p0312-b0024 | equation | low] G: (A,v = (v,q)) → G(2,v) =

[p0312-b0025 | equation | low] (3.8)

[p0312-b0026 | ordinary-paragraph | high] and we set

[p0312-b0027 | equation | low] (3.9)

[p0312-b0028 | equation | low] F(,v) = v + TG(,v).

[p0312-b0029 | ordinary-paragraph | high] Now we may state:

[p0312-b0030 | lemma | high] Lemma 3.1. The pair (u, p)e H'(Q) x L?(Q) is a solution of Problem (2.1) (2.13)

[p0312-b0031 | ordinary-paragraph | high] if and only if u = (u, p/v) is a solution of (3.1) where Λ = 1/v, the spaces X and 9

[p0312-b0032 | ordinary-paragraph | high] are defined by (3.5) and the compound mapping F is defined by (3.9).

[p0312-b0033 | proof | high] Proof. We observe that the equations (2.1) may be equivalently written in the

[p0312-b0034 | ordinary-paragraph | high] form

[p0312-b0035 | ordinary-paragraph | high] N

[p0312-b0036 | equation | low] -4u + grad(p/v) = (1/v)(

[p0312-b0037 | ordinary-paragraph | high] in Ω,

[p0312-b0038 | ordinary-paragraph | low] u,0u/0xj

[p0312-b0039 | equation | low] divu = 0 in Ω,

[p0312-b0040 | equation | low] u=g onr;

[p0312-b0041 | ordinary-paragraph | high] or by (3.7)

[p0312-b0042 | equation | low] (u,p/v) = T| (1/v)( f -

[p0312-b0043 | ordinary-paragraph | low] u,du/0x

[p0312-b0044 | ordinary-paragraph | high] Hence the lemma is established using (3.8) and (3.9).

## PDF 313 / printed 299



[p0313-b0003 | ordinary-paragraph | high] N

[p0313-b0004 | equation | low] DIGOUsa) v= (:> (u;Ov/Ox,; + 1 2u/0x).0)).

[p0313-b0005 | ordinary-paragraph | high] jm

[p0313-b0006 | ordinary-paragraph | high] Hence in our example, u = (u, p/v) is a nonsingular solution of (3.1), or equivalently

[p0313-b0007 | ordinary-paragraph | high] D,F(1/v,u) is an isomorphism of X if and only if, for each w = (w,o)eX there

[p0313-b0008 | ordinary-paragraph | high] exists a unique v = (v,q) in X such that

[p0313-b0009 | ordinary-paragraph | high] N

[p0313-b0010 | ordinary-paragraph | high] —Av + gradq + (1/v) }° (ujdv/dx; + vjdu/dx;) = —Aw+ grado in Q,

[p0313-b0011 | equation | low] j=

[p0313-b0012 | equation | low] div v = divw

[p0313-b0013 | equation | low] v= Ww onl:

[p0313-b0014 | ordinary-paragraph | high] Now, this problem can be simplified because on the one hand, an obvious

[p0313-b0015 | ordinary-paragraph | high] extension of Theorem I.5.4, proved in Cattabriga [18], guarantees that for every

[p0313-b0016 | ordinary-paragraph | high] fe H '(Q)", we L*(Q) and ge H'7(/)¥ fulfilling the compatibility condition

[p0313-b0017 | equation | low] |n ar= | g-nds

[p0313-b0018 | ordinary-paragraph | high] Q fi

[p0313-b0019 | ordinary-paragraph | high] there exists a unique w = (w,a) in X solution of

[p0313-b0020 | equation | low] —Aw + grado =f

[p0313-b0021 | ordinary-paragraph | high] in Q,

[p0313-b0022 | equation | low] divw = wu

[p0313-b0023 | equation | low] w=g onl.

[p0313-b0024 | ordinary-paragraph | high] On the other hand, when pw and g satisfy the above conditions an extension of

[p0313-b0025 | lemma | high] Lemma I.2.2 shows that there exists vg in H'(Q)% such that

[p0313-b0026 | equation | low] div¥o=i% Yolr—e:

[p0313-b0027 | ordinary-paragraph | high] Therefore, applying these two results we can prove that u = (u,p/v) is a non-

[p0313-b0028 | ordinary-paragraph | high] singular solution of (3.1) if and only if the homogeneous linearized problem

[p0313-b0029 | ordinary-paragraph | high] N

[p0313-b0030 | equation | low] —vAy + )° (ujdv/Ox; + vjOu/dx,) + gradg = f,

[p0313-b0031 | equation | low] j=t in Q,

[p0313-b0032 | ordinary-paragraph | high] (3.10) dive

[p0313-b0033 | equation | low] v=0 onl

[p0313-b0034 | ordinary-paragraph | high] has a unique solution v = (v,q)eX for each f, eH '(Q)%, the mapping f, > v

[p0313-b0035 | ordinary-paragraph | high] being continuous from H~'(Q)% into X.

[p0313-b0036 | ordinary-paragraph | high] Although we do not want to give here a precise statement, it can be proved

[p0313-b0037 | ordinary-paragraph | high] that the solutions of the Dirichlet problem for the Navier-Stokes equations are

[p0313-b0038 | ordinary-paragraph | high] “in general” nonsingular. We shall only derive the following simple result.

## PDF 314 / printed 300



[p0314-b0004 | proof | high] Proof. First, using the notations of Paragraph 2.1, we note that a variational

[p0314-b0005 | ordinary-paragraph | high] form of Problem (3.10) consists in finding a pair (v, q)¢ H'(Q)" x LZ(Q) solution

[p0314-b0006 | ordinary-paragraph | high] of

[p0314-b0007 | equation | low] |a( u; v,z) + a,(v;u,z) — (q,divz) = <f,,z> VzeH3(Q)",

[p0314-b0008 | equation | low] (3.11)

[p0314-b0009 | equation | low] divv=0 inQ,

[p0314-b0010 | equation | low] | v=g, onl.

[p0314-b0011 | ordinary-paragraph | high] In order to check that the equations (3.11) have a unique solution, it is sufficient

[p0314-b0012 | ordinary-paragraph | high] to prove that the bilinear form

[p0314-b0013 | equation | low] (v,z) > c(v,Z) = a(u;v,z) + a, (Vv; u,Z)

[p0314-b0014 | ordinary-paragraph | high] is V-elliptic. But it follows from (2.5) that

[p0314-b0015 | equation | low] c(v,v) = viv|7,9 +4,(vjuv) VveV.

[p0314-b0016 | ordinary-paragraph | high] Now, assume that v > v. where vo is defined by (2.24). Then, there exists a

[p0314-b0017 | ordinary-paragraph | high] function uy € H'(Q)% such that

[p0314-b0018 | equation | low] divuy=0, wuplr=g,

[p0314-b0019 | equation | low] Vv > p(Uo) + (WILE Uo) ly)?”

[p0314-b0020 | ordinary-paragraph | high] Next, setting u = uy + w, we have by (2.10) and (2.22)

[p0314-b0021 | equation | low] |a,(uv,;¥ )|< |ay(U¥o,; ¥ )| + |a,(v;W w,v )|

[p0314-b0022 | equation | low] < (p(Uo) + V|Wli,@)|VIt,a-

[p0314-b0023 | ordinary-paragraph | high] Since (cf. Remark 2.1)

[p0314-b0024 | ordinary-paragraph | high] ||[ (f up) |ly-

[p0314-b0025 | equation | low] IWwlo< WE Wo)l ly

[p0314-b0026 | ordinary-paragraph | high] v — p(Uo)

[p0314-b0027 | ordinary-paragraph | high] we obtain

[p0314-b0028 | ordinary-paragraph | high] N | 18

[p0314-b0029 | equation | low] c(v,v) > (»— p(Up) HAG Wo)l ly Jivi.o

[p0314-b0030 | ordinary-paragraph | high] v — p(Uo)

[p0314-b0031 | ordinary-paragraph | high] i MCN ||E Uf TWo) lly

[p0314-b0032 | equation | low] =v = piu (1 VI7,293

[p0314-b0033 | ordinary-paragraph | high] so that the ellipticity property holds. O

[p0314-b0034 | ordinary-paragraph | high] In the subsequent paragraphs, we shall be essentially concerned with the ap-

[p0314-b0035 | ordinary-paragraph | high] proximation of branches of nonsingular solutions {(A,u(A) = (u(A), Ap(A))); 4€ A}

[p0314-b0036 | ordinary-paragraph | high] of the Dirichlet problem for the Navier-Stokes equations where the parameter

[p0314-b0037 | ordinary-paragraph | high] A = 1/v plays the role of the Reynolds number.

## PDF 315 / printed 301



[p0315-b0003 | ordinary-paragraph | high] Let us go back to the general abstract problem (3.1) in order to introduce

[p0315-b0004 | ordinary-paragraph | high] the

[p0315-b0005 | ordinary-paragraph | high] method of approximation. For each value of a real parameter h > 0 which

[p0315-b0006 | ordinary-paragraph | high] will

[p0315-b0007 | ordinary-paragraph | high] tend to zero, we are given a @’-mapping F,, presumably an approximation of F,

[p0315-b0008 | ordinary-paragraph | high] defined on A x X with values in 2. The problem now is to find pairs (A, u,)€

[p0315-b0009 | ordinary-paragraph | high] A x X, solutions of

[p0315-b0010 | ordinary-paragraph | high] (3.12) O10)

[p0315-b0011 | ordinary-paragraph | high] Let us assume that {(A, u(A)A)e; 4 } is a branch of nonsingular solutions of (3.1).

[p0315-b0012 | ordinary-paragraph | high] We want to find sufficient conditions ensuring the existence and uniqueness of

[p0315-b0013 | ordinary-paragraph | high] a branch {(A, u,(A)); A € 4} of solutions of (3.12) in a suitable neighborhood of the

[p0315-b0014 | ordinary-paragraph | high] branch of solutions of (3.1).

[p0315-b0015 | ordinary-paragraph | high] In a first stage, we fix Ain A and we propose to approximate the solution of

[p0315-b0016 | ordinary-paragraph | high] (3.1) by the solution u,(A) of (3.12). Let &, (= a,(A)) be an arbitrary element of X

[p0315-b0017 | ordinary-paragraph | high] and let us investigate under what conditions the mapping D,F ,(A, ii,) is invertible.

[p0315-b0018 | ordinary-paragraph | high] To this end, we introduce the two quantities:

[p0315-b0019 | ordinary-paragraph | high] (3.13) WA) = {DFA uA} I.g a.x

[p0315-b0020 | ordinary-paragraph | high] (3.14) My(A) = || DF (A, u(A)) — DF, (A, Oy) Ile x;a ):

[p0315-b0021 | lemma | high] Lemma 3.3. Under the condition

[p0315-b0022 | ordinary-paragraph | high] (3.15) VA) Mal) < 1,

[p0315-b0023 | ordinary-paragraph | high] the mapping D,F,,(A, t,,) is an isomorphism from X onto &.

[p0315-b0024 | proof | high] Proof. We set

[p0315-b0025 | equation | low] B = {D,F(A,u(A))}"*{D, F(A,u(d)) — DyF,(A, &)}.

[p0315-b0026 | ordinary-paragraph | high] Then

[p0315-b0027 | equation | low] D,F,(A, t,) = D, F(A, u(A)) {I — B}.

[p0315-b0028 | ordinary-paragraph | high] But in view of( 3.15), we have

[p0315-b0029 | equation | low] | Bll goa S V(AualA) < 1;

[p0315-b0030 | ordinary-paragraph | high] therefore J — B is an isomorphism of X and

[p0315-b0031 | equation | low] I = BY" Ig.o cxy < 1/1 — yA4)4( A) ).

[p0315-b0032 | ordinary-paragraph | high] As a consequence D,F ,,(A, v,) is also an isomorphism from X onto 2 and

[p0315-b0033 | ordinary-paragraph | high] (3.16) {DFA 3 ean < VAM = 7A oa(A))- O

[p0315-b0034 | remark | high] Remark 3.1. The above lemma relies on the fact that both F and Fk, map A x X

[p0315-b0035 | ordinary-paragraph | high] into &. This hypothesis makes the forthcoming theory simpler than when F,, and

## PDF 316 / printed 302



[p0316-b0004 | ordinary-paragraph | high] of a situation where F and F, are not defined in the same space.

[p0316-b0005 | ordinary-paragraph | high] Now, we assume that D,F,(A,i,) is an isomorphism from X onto 2 and we

[p0316-b0006 | ordinary-paragraph | high] introduce the following notations:

[p0316-b0007 | equation | low] En(A) = |F a(A, th) Ila

[p0316-b0008 | equation | low] Yl) = {Di FiA, t)}* Iga.x>

[p0316-b0009 | equation | low] (3.17)

[p0316-b0010 | equation | low] S(u;a)= {veX ; |v —ullxy< a},

[p0316-b0011 | equation | low] L,(A;a) = sup ||D,F,(A,a_) — DFA; 0) Ilg x;a y:

[p0316-b0012 | ordinary-paragraph | high] ve S(up32)

[p0316-b0013 | ordinary-paragraph | high] Clearly, the function « > L,(/;«): R, > R, is monotonically increasing.

[p0316-b0014 | ordinary-paragraph | high] The next theorem solves Problem (3.12) and gives a fundamental error

[p0316-b0015 | ordinary-paragraph | high] estimate. In addition, it shows that Problem (3.12) has no other solution in a

[p0316-b0016 | ordinary-paragraph | high] suitable neighborhood of i,.

[p0316-b0017 | theorem | high] Theorem 3.1. Under the following assumptions:

[p0316-b0018 | ordinary-paragraph | high] (3.18) D,F,(A, t,) is an isomorphism of X onto &,

[p0316-b0019 | ordinary-paragraph | high] (3.19) 2ylA)LwlAs 27n(A)En(A)) < 1,

[p0316-b0020 | ordinary-paragraph | high] then Problem (3.12) has a solution (A, u,) with

[p0316-b0021 | ordinary-paragraph | high] (3.20) Uy, € S(t; 2y,(A)E,(A)),

[p0316-b0022 | ordinary-paragraph | high] D,F,(A, u,) is an isomorphism of X onto & and

[p0316-b0023 | ordinary-paragraph | high] (3:21) | {D, F(A(,A , u,)}~ : lew: x9 <S s 2y,(A).

[p0316-b0024 | ordinary-paragraph | high] Furthermore, we have the following uniqueness result: u, is the only solution in

[p0316-b0025 | ordinary-paragraph | high] every ball S(t; «) whose radius « satisfies:

[p0316-b0026 | ordinary-paragraph | high] (3:22) Yrl(A)Lp(A; a) < 1

[p0316-b0027 | ordinary-paragraph | high] and we have the estimate:

[p0316-b0028 | ordinary-paragraph | high] (3.23) Jun — vllxS [yaAV = yalALi) (A) Fa, ole = Vo] Sp 0).

[p0316-b0029 | proof | high] Proof. Let us define the function

[p0316-b0030 | equation | low] P,(v) =v— [D,F,(A, ii,) | 1 F,(A, v) VUGLXe

[p0316-b0031 | ordinary-paragraph | high] Clearly, the pair (A,u,) is a solution of (3.12) if and only if u, is a fixed point of

[p0316-b0032 | ordinary-paragraph | high] ®,. First, we are going to establish that ®, is a strict contraction of § = S(i,;

[p0316-b0033 | ordinary-paragraph | high] 2y,(A)é,(A)) into itself.

[p0316-b0034 | ordinary-paragraph | high] 1°) Let veS ; then

## PDF 317 / printed 303



[p0317-b0004 | ordinary-paragraph | low] -Fh(A,an)].

[p0317-b0005 | ordinary-paragraph | medium] But

[p0317-b0006 | equation | low] Fh(,u) -Fh(,an) =

[p0317-b0007 | ordinary-paragraph | low] D,Fh(l,an + 0(v - un))·(v - un)d0.

[p0317-b0008 | ordinary-paragraph | medium] Thus

[p0317-b0009 | ordinary-paragraph | low] I/DuFh(,an)·(u—un) —(Fh(l,u) —Fh(,un))ll

[p0317-b0010 | ordinary-paragraph | low] {DuFh(A,an) -DuFr(n,an + 0(u -—an)}·(v-—un)dθ

[p0317-b0011 | equation | low] ≤ Lh(1; 2yh(a)8n(2))2yn()8h(2)

[p0317-b0012 | ordinary-paragraph | medium] because ve S (cf. (3.17)). Hence:

[p0317-b0013 | ordinary-paragraph | low] 11Φh(0) -un1lx ≤h()cn(2){Ln(; 2h()en(2))2n(2) + 1} < 2yh(a)8h(2),

[p0317-b0014 | ordinary-paragraph | medium] by virtue of (3.19). Therefore Φ,(v) belongs to S.

[p0317-b0015 | ordinary-paragraph | medium] 2°) Let v and w belong to S. Like above, we can write:

[p0317-b0016 | ordinary-paragraph | low] Φn(u) -Φh(w) =[DuFn(,an)]-1[DFh(,un)·(u -w) -(Fh(n,u) -Fh(n,w))]

[p0317-b0017 | ordinary-paragraph | medium] 1

[p0317-b0018 | equation | low] =[DμF(,an)]-1

[p0317-b0019 | ordinary-paragraph | low] {DuFh(l,un)

[p0317-b0020 | ordinary-paragraph | low] 0

[p0317-b0021 | ordinary-paragraph | low] -- DuF(a, w + θ(u - w))}·(o -- w)d0.

[p0317-b0022 | ordinary-paragraph | medium] Again (3.17) and (3.19) yield:

[p0317-b0023 | ordinary-paragraph | low] 11Φh(u) - Φh(w)lx ≤ yh(a)Ln(2; 2yh(2)en(2) 1lu - w1llx < (1/2) lu - wllx.

[p0317-b0024 | ordinary-paragraph | medium] Hence the mapping Φ, is a strict contraction of S into itself. As a consequence,

[p0317-b0025 | ordinary-paragraph | medium] P, has a unique fixed point in S.

[p0317-b0026 | ordinary-paragraph | medium] Let u, = u,(l) denote the fixed point of Φ, in S. It follows from the above

[p0317-b0027 | ordinary-paragraph | medium] considerations that the pair (%,u,) is the (unique) solution of (3.12) in S. In

[p0317-b0028 | ordinary-paragraph | medium] addition, observe that

[p0317-b0029 | equation | low] 1/DuFn(, un) -DuFn(,un) 1l(x;a) ≤ Ln(; 2yn(a)8n(a)

[p0317-b0030 | equation | low] < 1/(2yn(2))  owing to (3.19).

[p0317-b0031 | ordinary-paragraph | medium] Thus the assumption (3.18) and Lemma 3.3 imply that D,F,(,u,) is also an

[p0317-b0032 | ordinary-paragraph | medium] isomorphism of X onto X and (3.21) follows from (3.16).

[p0317-b0033 | ordinary-paragraph | medium] Next, let us prove that Φ, has no other fixed point than u, in the larger ball

[p0317-b0034 | ordinary-paragraph | medium] S(u,; α) with α prescribed by (3.22). Indeed, let v be another fixed point of Φ, in

[p0317-b0035 | ordinary-paragraph | medium] S(u,; α). The argument of part 2°) gives:

[p0317-b0036 | equation | low] 1lU —unllx = IΦn(u) —Φn(un) llx ≤yn(2)Ln(2;α) /u - un llx.

[p0317-b0037 | ordinary-paragraph | medium] Thus v = u, when α satisfies (3.22).

## PDF 318 / printed 304



[p0318-b0003 | equation | low] v — u, = (D,F,(A, ii,|) *( DF,( A,& ,)*(v — Up)

[p0318-b0004 | ordinary-paragraph | high] — (F,(A, v) — F(A, u;,)) + F,(A, v)J

[p0318-b0005 | ordinary-paragraph | high] (3.24) = [D,F,(A,a,)]* || {D, F(A,

[p0318-b0006 | ordinary-paragraph | high] tn)

[p0318-b0007 | ordinary-paragraph | high] — D,F,(A, u, + O(v — u,)}+(v — u,)d O + F,(A, of

[p0318-b0008 | ordinary-paragraph | high] Hence

[p0318-b0009 | ordinary-paragraph | high] lv — ualle < yal) {Lao lo — walle + AGA Olle}

[p0318-b0010 | ordinary-paragraph | high] thus proving (3.23). Oo

[p0318-b0011 | ordinary-paragraph | high] Now we allow 4 to vary in the compact interval A. We replace the fixed

[p0318-b0012 | ordinary-paragraph | high] element a, by a @°-mapping 1 > a,(/): A > X. The following lemma generalizes

[p0318-b0013 | lemma | high] Lemma 3.3.

[p0318-b0014 | lemma | high] Lemma 3.4. Under the condition:

[p0318-b0015 | ordinary-paragraph | high] (3.25) lim sup ,(A) = 0,

[p0318-b0016 | equation | low] h>O AeA

[p0318-b0017 | ordinary-paragraph | high] there exists areal h, > 0 such that for all A€ A and all h < ho, D,F,,(A, t,(4)) is an

[p0318-b0018 | ordinary-paragraph | high] isomorphism of X onto & and we have the bound:

[p0318-b0019 | ordinary-paragraph | high] (3.26) aA) = LD F(A, H(A)1 Ie @eexy < 27).

[p0318-b0020 | proof | high] Proof. Since A is compact, the function y(/) is bounded above on A. Therefore

[p0318-b0021 | ordinary-paragraph | high] (3.25) implies that for some hy > 0, we have

[p0318-b0022 | equation | low] sup {7(A)Mn(A)} < 1/2 Vh <ho.

[p0318-b0023 | ordinary-paragraph | high] AeA

[p0318-b0024 | ordinary-paragraph | high] Hence Lemma 3.3 asserts that D,F,(A, a,(A)) is an isomorphism of X onto & for

[p0318-b0025 | ordinary-paragraph | high] all A€ A and all h < ho. Moreover the bound (3.16) yields directly (3.26). oO

[p0318-b0026 | ordinary-paragraph | high] Combined with Theorem 3.1, this lemma shows that Problem (3.12) has a

[p0318-b0027 | ordinary-paragraph | high] unique branch of nonsingular solutions in a neighborhood of @,.

[p0318-b0028 | theorem | high] Theorem 3.2. Let {(A, u(A)); A A} be a branch of nonsingular solutions of (3.1) and

[p0318-b0029 | ordinary-paragraph | high] let 4 > i,(A) be a given function in @°(A; X) that satisfies

[p0318-b0030 | equation | low] lim sup 1,(A) = 0.

[p0318-b0031 | equation | low] h>0 AcA

[p0318-b0032 | ordinary-paragraph | high] If, besides that,

## PDF 319 / printed 305



[p0319-b0006 | ordinary-paragraph | medium] and

[p0319-b0007 | equation | low] lim  sup Lh(;α)

[p0319-b0008 | equation | low] (3.28)

[p0319-b0009 | equation | low] uniformly for all h ≤ ho,

[p0319-b0010 | ordinary-paragraph | low] α→0 (eA

[p0319-b0011 | ordinary-paragraph | medium] where ho is the parameter of Lemma 3.4, then there exist two real constants α > 0

[p0319-b0012 | ordinary-paragraph | medium] and h, > O and a function u,eé°(A; X) such that for all h ≤ h,:

[p0319-b0013 | ordinary-paragraph | medium] (3.29) {(l, u,(a)); 2e A} is a branch of nonsingular solutions of (3.12),

[p0319-b0014 | ordinary-paragraph | medium] for each Xe A, un() is the only solution of (3.12) in the ball S(u,(2); α) and we have

[p0319-b0015 | ordinary-paragraph | medium] the bound:

[p0319-b0016 | equation | low] IIun(l) - vllx ≤ 4y(2) l/ Fh(A, v) Ilx Vv∈ S(an(A);α).

[p0319-b0017 | equation | low] (3.30)

[p0319-b0018 | proof | medium] Proof. According to Lemma 3.4, we know that y,(l) is bounded above for all 

[p0319-b0019 | ordinary-paragraph | medium] in / and for all h ≤ ho. Therefore (3.28) implies that we can find an α > 0 such that

[p0319-b0020 | equation | low] VIeA,  Vh ≤ ho.

[p0319-b0021 | equation | low] Yn(a)Ln(l;α) < 1/2

[p0319-b0022 | equation | low] (3.31)

[p0319-b0023 | ordinary-paragraph | medium] Likewise, (3.27) implies that there exists an h' > 0 such that

[p0319-b0024 | equation | low] 2yn(a)Ln(l; 2yn(a)en(a) < 1 A∈A, Vh ≤ho.

[p0319-b0025 | ordinary-paragraph | medium] Take h, = min(ho, ho). Then it follows from Theorem 3.1 that for all Λe A and

[p0319-b0026 | ordinary-paragraph | medium] all h ≤ h,, there exists a u,() in X, unique in S(u,(^); α), such that:

[p0319-b0027 | equation | low] Fh(,un()) = 0

[p0319-b0028 | ordinary-paragraph | medium] and D, F(, u,()) is an isomorphism of X onto X. In addition Lemma 3.4 and

[p0319-b0029 | ordinary-paragraph | medium] (3.21) yield:

[p0319-b0030 | equation | low] II [DμFh(1, u(4))]-1 llg(x;x) ≤ 4y(2).

[p0319-b0031 | equation | low] (3.32)

[p0319-b0032 | ordinary-paragraph | medium] Similarly, (3.23), (3.26) and (3.31) give (3.30).

[p0319-b0033 | ordinary-paragraph | medium] Finally, the continuity of u, with respect to X is an easy consequence of (3.30),

[p0319-b0034 | ordinary-paragraph | medium] 口

[p0319-b0035 | ordinary-paragraph | medium] the continuity of u, and the continuity of Fh.

[p0319-b0036 | remark | medium] Remark 3.2. An interesting feature of this proof is that the function u, is arbitrary.

[p0319-b0037 | ordinary-paragraph | medium] The most obvious choice of function in the present case where F and F, are

[p0319-b0038 | ordinary-paragraph | medium] defined on the same space X is of course u,() = u(l), and this will be used below.

[p0319-b0039 | ordinary-paragraph | medium] When F, is defined on a space X, different from X, like in Section 3.4, we shall

[p0319-b0040 | ordinary-paragraph | medium] take for u, an adequate approximation of u.

[p0319-b0041 | remark | medium] Remark 3.3. Theorem 3.2 does not use fully the regularity of F and F, with respect

[p0319-b0042 | ordinary-paragraph | medium] to . When Λ → u,(l) is a &-mapping from A into X, it is established in Crouzeix

[p0319-b0043 | ordinary-paragraph | medium] [22] that u, is also in &"(4; X).

## PDF 320 / printed 306



[p0320-b0004 | ordinary-paragraph | medium] Let us apply the preceding theoretical approach to solve the following class of

[p0320-b0005 | ordinary-paragraph | medium] problems:

[p0320-b0006 | equation | low] F(,u) = u + TG(A,u) = 0,

[p0320-b0007 | equation | low] (3.33)

[p0320-b0008 | ordinary-paragraph | medium] where Te &(Y;X), G is a C2-mapping from A x X into Y, X and Y are two

[p0320-b0009 | ordinary-paragraph | medium] Banach spaces and A is a compact interval of R. As a consequence, here we have

[p0320-b0010 | ordinary-paragraph | medium] X = X. We have seen in Section 3.1 that the Dirichlet problem for the Navier-

[p0320-b0011 | ordinary-paragraph | medium] Stokes equations can be put into the form (3.33).

[p0320-b0012 | ordinary-paragraph | medium] To approximate Problem (3.33) we introduce an operator T e &(Y; X) in-

[p0320-b0013 | ordinary-paragraph | medium] tended to approximate T and we set:

[p0320-b0014 | equation | low] Fh(, u) = u + ThG(A,u).

[p0320-b0015 | equation | low] (3.34)

[p0320-b0016 | ordinary-paragraph | medium] The approximate problem reads:

[p0320-b0017 | ordinary-paragraph | medium] Find u,e X such that

[p0320-b0018 | equation | low] (3.35)

[p0320-b0019 | equation | low] Fh(,un) = 0.

[p0320-b0020 | ordinary-paragraph | medium] Now, suppose that Problem (3.33) has a branch of nonsingular solutions

[p0320-b0021 | ordinary-paragraph | medium] {(,u(2)); Xe A}. In order to apply Theorem 3.2 we need to make additional

[p0320-b0022 | ordinary-paragraph | medium] assumptions. First, we suppose there exists another Banach space Z contained

[p0320-b0023 | ordinary-paragraph | medium] in Y, with continuous imbedding, such that

[p0320-b0024 | equation | low] (3.36)

[p0320-b0025 | ordinary-paragraph | low] ) VΛeA,  VueX.

[p0320-b0026 | ordinary-paragraph | medium] D,G(L, u)e L(X; Z)

[p0320-b0027 | ordinary-paragraph | medium] Next, concerning the approximation properties of the operator Th, we assume

[p0320-b0028 | ordinary-paragraph | medium] that:

[p0320-b0029 | equation | low] (3.37)

[p0320-b0030 | equation | low] lim II(T - T)gllx = O  Vg∈ Y

[p0320-b0031 | ordinary-paragraph | medium] h→0

[p0320-b0032 | ordinary-paragraph | medium] and

[p0320-b0033 | equation | low] (3.38)

[p0320-b0034 | equation | low] lim II T -- Tll e(z;x) = 0.

[p0320-b0035 | ordinary-paragraph | medium] h→0

[p0320-b0036 | remark | medium] Remark 3.4. When the range of the operator T, is a finite-dimensional subspace

[p0320-b0037 | ordinary-paragraph | medium] X, of X (which is the case in finite element approximation), the assumption (3.38)

[p0320-b0038 | ordinary-paragraph | medium] implies that the operator T is compact from Z into X as the uniform limit of the

[p0320-b0039 | ordinary-paragraph | medium] sequence of compact operators T,. Hence, in that case, the operator TD, G(l, u)E

[p0320-b0040 | ordinary-paragraph | medium] ④(x; X) is compact and

[p0320-b0041 | equation | low] D,F(x,u) = I + TD,G(,u)

[p0320-b0042 | ordinary-paragraph | medium] is a compact perturbation of the identity.

[p0320-b0043 | ordinary-paragraph | medium] Note also that (3.38) is a consequence of (3.37) when the imbedding of Z into

[p0320-b0044 | ordinary-paragraph | medium] Y is compact.

## PDF 321 / printed 307



[p0321-b0004 | ordinary-paragraph | high] conditions (3.36), (3.37) and (3.38) hold and that {(A,u(A));A4A€} is a branch of

[p0321-b0005 | ordinary-paragraph | high] nonsingular solutions of (3.33). Then there exists a neighborhood© of the origin

[p0321-b0006 | ordinary-paragraph | high] in X and for h < ho small enough a unique @?-function 2€ A = u,(A)€ X such that:

[p0321-b0007 | ordinary-paragraph | high] (3.39) {(A,u,(A)); AE At is a branch of nonsingular solutions of (3.35),

[p0321-b0008 | ordinary-paragraph | high] (3.40) u,(A) — u(A)eO for allie A.

[p0321-b0009 | ordinary-paragraph | high] Furthermore, there exists a constant K > 0 independent of h and A with:

[p0321-b0010 | ordinary-paragraph | high] (3.41) l|un(A) — uA)l x < K (1, — T)GAuA)Ilx VAe A.

[p0321-b0011 | proof | high] Proof. We are going to apply Theorem 3.2 with @,(A) = u(A). Since by assump-

[p0321-b0012 | ordinary-paragraph | high] tion the mapping (4, u) > G(A,u) is G7, then (A, u) > F(A, u) is also @? and so is

[p0321-b0013 | ordinary-paragraph | high] A u(A).

[p0321-b0014 | ordinary-paragraph | high] Let us check the condition (3.25). We have

[p0321-b0015 | equation | low] (A) = |\(T— T,)D,uGA)( IAl.g ,ox) :

[p0321-b0016 | ordinary-paragraph | high] Then (3.36), (3.38) and the continuity of the mapping 4 > D,,G(A, u(A)) yield (3.25).

[p0321-b0017 | ordinary-paragraph | high] Next, we turn to (3.27). Since

[p0321-b0018 | equation | low] F(A, u(A)) = 0

[p0321-b0019 | ordinary-paragraph | high] we can write:

[p0321-b0020 | equation | low] &,(A) = ||F (A, u(A)) — FU, uA) ix

[p0321-b0021 | equation | low] = ||(T, — T)G(A, u(A)) Ilx-

[p0321-b0022 | ordinary-paragraph | high] Hence the continuity of the mapping 2 > G(A,u(A)) and (3.37) imply (3.27).

[p0321-b0023 | ordinary-paragraph | high] Finally, consider (3.28). Using (3.27) and the uniform-boundedness theorem we

[p0321-b0024 | ordinary-paragraph | high] obtain

[p0321-b0025 | ordinary-paragraph | high] IlT hllgarsxy SC.

[p0321-b0026 | ordinary-paragraph | high] Therefore,

[p0321-b0027 | equation | low] L,(A;a) <C sup || D,, G(A, u(A)) — D,G(A, v) | gcx:y):

[p0321-b0028 | ordinary-paragraph | high] ve S(u(A);a)

[p0321-b0029 | ordinary-paragraph | high] Thus, by the mean-value theorem:

[p0321-b0030 | equation | low] L,(A; 0) < aCL(a)

[p0321-b0031 | ordinary-paragraph | high] where L(a) = sup || Dz. G(A, v) lgli cxy):

[p0321-b0032 | ordinary-paragraph | high] AE A,ve S(u(A); a)

[p0321-b0033 | ordinary-paragraph | high] derive

[p0321-b0034 | ordinary-paragraph | high] As D2G is bounded on all bounded subsets of 4 x X, we immediately

[p0321-b0035 | ordinary-paragraph | high] (3.28).

[p0321-b0036 | ordinary-paragraph | high] Therefore, the conclusion of Theorem 3.2 holds, (3.41) follows readily from

## PDF 322 / printed 308



[p0322-b0004 | remark | high] Remark 3.5. The conclusion of Theorem 3.3 (apart from the @?-regularity of u,)

[p0322-b0005 | ordinary-paragraph | high] can be obtained by replacing the @-regularity of G by the Lipschitz-continuity

[p0322-b0006 | ordinary-paragraph | high] of D,,G:

[p0322-b0007 | ordinary-paragraph | high] there exists a function pw > L(y): Ry > R,, locally bounded, such that for all

[p0322-b0008 | ordinary-paragraph | high] v in S(u(A); w) and all A in A:

[p0322-b0009 | ordinary-paragraph | high] (3.42) || D,G(A, u(A)) — D,G(A, v) ||g uy < LW) ||uA) — vx.

[p0322-b0010 | remark | high] Remark 3.6. On the other hand, when G is a @’-mapping (with p > 2) and D?G

[p0322-b0011 | ordinary-paragraph | high] is bounded on all bounded subsets of A x X, then the argument of Brezzi,

[p0322-b0012 | ordinary-paragraph | high] Rappaz & Raviart [14] shows that u,(A) is a @’-mapping from A into X and

[p0322-b0013 | ordinary-paragraph | high] gives the following bound for each m withO<m<p-—l:

[p0322-b0014 | ordinary-paragraph | high] (3.43) — |]d™(ug(A) — u(A))/da"l x < Cn Y I(T, — T) d'G(A, u(A))/da'| x.

[p0322-b0015 | ordinary-paragraph | high] As a first application of Theorem 3.3, we generalize to the Navier-Stokes

[p0322-b0016 | ordinary-paragraph | high] equations (2.1) (2.13) the regularization method or penalty method introduced

[p0322-b0017 | ordinary-paragraph | high] in Section I.5.1 for the Stokes equations. We consider the following problem:

[p0322-b0018 | equation | low] given ¢ > 0 find (u‘, p*)e H'(Q)" x L$(Q) solution of

[p0322-b0019 | ordinary-paragraph | high] N

[p0322-b0020 | equation | low] —vAu’ + > u?du’/dx; + grad p’ =f

[p0322-b0021 | ordinary-paragraph | high] (3.44) = ee

[p0322-b0022 | ordinary-paragraph | high] ; p® = —(1/e)divu’

[p0322-b0023 | equation | low] w=g onl,

[p0322-b0024 | ordinary-paragraph | high] or equivalently

[p0322-b0025 | ordinary-paragraph | high] find uw’ € H'(Q)* such that

[p0322-b0026 | ordinary-paragraph | high] N

[p0322-b0027 | equation | low] —vAu’ — (1/s)grad(divu’) + 5 udu’/dx,=f

[p0322-b0028 | ordinary-paragraph | high] (3.45) ia ! > pone in Q,

[p0322-b0029 | equation | low] w=g onl.

[p0322-b0030 | ordinary-paragraph | high] In order to study the convergence of this regularization method, we consider

[p0322-b0031 | ordinary-paragraph | high] a branch of nonsingular solutions {(A,u(A) = (u(A), Ap(d)));4 = 1/veA } of the

[p0322-b0032 | ordinary-paragraph | high] equations (2.1) (2.13) in a compact interval A of R, — {0}. This means that for

[p0322-b0033 | ordinary-paragraph | high] all (u, Ap) = (u(A), Ap()), 4 = 1/ve A, the linearized problem (3.10) is well posed.

[p0322-b0034 | theorem | high] Theorem 3.4. Let N < 4 and let {(4,u(A) = (u(A), Ap(A))); 2 = 1/veA } be a branch

[p0322-b0035 | ordinary-paragraph | high] of nonsingular solutions of (2.1) (2.13). Then there exists a neighborhood © of the

[p0322-b0036 | ordinary-paragraph | high] origin in H*(Q)% x Lo(Q) and for ¢<& small enough a unique €” branch

## PDF 323 / printed 309



[p0323-b0005 | ordinary-paragraph | medium] Moreover, we get the estimate

[p0323-b0006 | equation | low] (3.46)

[p0323-b0007 | equation | low] sup(llu(l) - u() ll1,o + Ilp(2) - p(2) llo,o) ≤ Cs,

[p0323-b0008 | ordinary-paragraph | low] AeA

[p0323-b0009 | ordinary-paragraph | medium] where the constant C is independent of &.

[p0323-b0010 | proof | medium] Proof. If we define the spaces X and Y by (3.5) and (3.6) and the mappings T and

[p0323-b0011 | ordinary-paragraph | medium] G by (3.7) and (3.8) respectively, we have already seen that Problem (2.1) (2.13)

[p0323-b0012 | ordinary-paragraph | medium] fits into the framework of Section 3.1. Then, in order to apply Theorem 3.3 we

[p0323-b0013 | ordinary-paragraph | medium] take Z = Y and we define the operator T' of S(Y; X) as follows:

[p0323-b0014 | ordinary-paragraph | medium] given (f*,g*)e Y let (u,ps) = T'(f*,g*) denote the solution of the regu-

[p0323-b0015 | ordinary-paragraph | medium] larized Stokes problem

[p0323-b0016 | equation | low] -△u + grad p = f*

[p0323-b0017 | ordinary-paragraph | medium] in Ω,

[p0323-b0018 | equation | low] p = --(1/8)div us

[p0323-b0019 | equation | low] u* =g* on I.

[p0323-b0020 | ordinary-paragraph | medium] Clearly, (u, p°) is a solution of (3.44) if and only if

[p0323-b0021 | equation | low] u" + T"G(,u) = 0,

[p0323-b0022 | ordinary-paragraph | medium] where u* = (u, p/v). Moreover, Theorem I.5.3 gives for all ε ≤ &o sufficiently

[p0323-b0023 | ordinary-paragraph | medium] small:

[p0323-b0024 | equation | low] I Tev - Tll(x;x) ≤ Cev ≤ C2,

[p0323-b0025 | ordinary-paragraph | medium] with a constant C, independent of A owing to the compactness of A.

[p0323-b0026 | ordinary-paragraph | medium] Now since

[p0323-b0027 | ordinary-paragraph | low] u;0v/0x, -f

[p0323-b0028 | equation | low] G(l,u) =

[p0323-b0029 | ordinary-paragraph | medium] it follows that D2 G is independent of v:

[p0323-b0030 | ordinary-paragraph | medium] N

[p0323-b0031 | equation | low] D²G(2, v)· (u, w) = i ∑ (w;0u/0x; + u;0w/0xj).

[p0323-b0032 | ordinary-paragraph | medium] Thus the mapping D2G is bounded on all bounded subsets of A x X for N ≤ 4,

[p0323-b0033 | ordinary-paragraph | medium] by virtue of the Sobolev's Imbedding Theorem 1.1.3. (And more generally, G is

[p0323-b0034 | ordinary-paragraph | medium] ∞ and D"G is zero for all p ≥ 2). Therefore the fact that {(l,u(2); Λe A} is a

[p0323-b0035 | ordinary-paragraph | medium] branch of nonsingular solutions of

[p0323-b0036 | equation | low] F(A,u) = u + TG(,u) = 0

[p0323-b0037 | ordinary-paragraph | medium] permits to apply Theorem 3.3. In other words, if eo is small enough there exist a

[p0323-b0038 | ordinary-paragraph | medium] real a > 0 and a unique branch {(,u*(2) = (u(), Ap"(2))); Λe A} of nonsingular

## PDF 324 / printed 310



[p0324-b0005 | ordinary-paragraph | medium] such that

[p0324-b0006 | equation | low] Ilu"(2) - u(μ)llx ≤a.

[p0324-b0007 | ordinary-paragraph | medium] Moreover we have

[p0324-b0008 | equation | low] Ilu(2) - u()llx = I/u(2) - u(2)ll1,o + Allp(2) - p(x)llo,2

[p0324-b0009 | equation | low] ≤ C3I(Tv - T)G(n, u(A))Ilx

[p0324-b0010 | equation | low] ≤ C2C38l/ G(, u(a)) lx ≤ C4&.

[p0324-b0011 | ordinary-paragraph | medium] In addition Remark 3.6 implies that the mapping ^ → u*(2) is & from A into X.

[p0324-b0012 | ordinary-paragraph | medium] 口

[p0324-b0013 | ordinary-paragraph | medium] Let H be a Banach space such that

[p0324-b0014 | ordinary-paragraph | medium] XcH

[p0324-b0015 | ordinary-paragraph | medium] where as usual the sign  means that the imbedding is continuous. Now, we

[p0324-b0016 | ordinary-paragraph | medium] want to derive a sharper estimate for Ilu,(l) - u(2)ll h. To this end, we assume

[p0324-b0017 | ordinary-paragraph | medium] that there exists another Banach space W with

[p0324-b0018 | ordinary-paragraph | low] Wcx

[p0324-b0019 | ordinary-paragraph | medium] such that the following property holds:

[p0324-b0020 | ordinary-paragraph | medium] for all ve W, the operator D,G(,v) may be extended as a linear op-

[p0324-b0021 | equation | low] (3.47)

[p0324-b0022 | ordinary-paragraph | medium] erator of (H; Y), the mapping v → D,G(, v) being continuous from

[p0324-b0023 | ordinary-paragraph | medium] W into L(H; Y).

[p0324-b0024 | ordinary-paragraph | medium] Hence, for ve W, both D,F(l, v) and D,F,(, v) may be extended as operators of

[p0324-b0025 | ordinary-paragraph | medium] (H; H). Next, we suppose that:

[p0324-b0026 | equation | low] lim II T - TIl(x;n) = 0.

[p0324-b0027 | equation | low] (3.48)

[p0324-b0028 | ordinary-paragraph | medium] h→0

[p0324-b0029 | remark | medium] Remark 3.7. Note that (3.48) is again a consequence of (3.37) when the imbedding

[p0324-b0030 | ordinary-paragraph | medium] of X into H is compact.

[p0324-b0031 | ordinary-paragraph | medium] Then we can prove the following result.

[p0324-b0032 | theorem | medium] Theorem 3.5. We retain the hypotheses of Theorem 3.3 together with (3.47) and

[p0324-b0033 | ordinary-paragraph | medium] (3.48). Assume in addition that:

[p0324-b0034 | ordinary-paragraph | medium] (3.49) for each Xe A, u(l)e W and the function  → u(l)e6°(A; W);

[p0324-b0035 | ordinary-paragraph | medium] (3.50)  for each Xe A, D,F(Ω, u(a)) is an isomorphism of H.

## PDF 325 / printed 311



[p0325-b0004 | ordinary-paragraph | high] (3.51) [un(A) — uA)l n S K'{ I(T — TGA, uA) ig + lun(A) — (A) 3}.

[p0325-b0005 | proof | high] Proof. First, in view of (3.47) and (3.49), observe that:

[p0325-b0006 | ordinary-paragraph | high] || DF (A, u(A)) — DF. (A, u(A)) I gare) = I(T — T,)D Gu(A,)) ||e am

[p0325-b0007 | ordinary-paragraph | high] S ||T — Till gor: || DuGA, u(A)) Ilg ary):

[p0325-b0008 | ordinary-paragraph | high] Therefore, (3.48) implies that

[p0325-b0009 | equation | low] lim sup ||D , F(A, u(A)) — DyFa(A, u()Il.g)u rs uy = 9.

[p0325-b0010 | equation | low] h>0 AeA

[p0325-b0011 | ordinary-paragraph | high] Hence it stems from (3.50) and Lemma 3.3 that for all sufficiently small h and all

[p0325-b0012 | ordinary-paragraph | high] Ain A, D,F,(A,u(A)) is an isomorphism of H with:

[p0325-b0013 | equation | low] | (DF, (A; u(A))] ll ane < Cj.

[p0325-b0014 | ordinary-paragraph | high] Then, like in Theorem 3.1, we can write:

[p0325-b0015 | ordinary-paragraph | high] u(A) — uy(A) = (DFA, u(4)) 1 * LT, {Du GO, u(A))- (u(A) — up(A)) — (GA, u(A))

[p0325-b0016 | ordinary-paragraph | high] — G(A, u,(A)))} + FA, u(A))I-

[p0325-b0017 | ordinary-paragraph | high] But

[p0325-b0018 | ordinary-paragraph | high] G(A, u(A)) — GA, u,(A)) — D, GA, u(A)()u-(A ) — u,(A))

[p0325-b0019 | ordinary-paragraph | high] (3.52) 1

[p0325-b0020 | equation | low] = -| (1 — t)Dz,G(A,( 1 — t)u(A) + tu,(dAt-) (u)(A ) — u,(A)).

[p0325-b0021 | ordinary-paragraph | high] 0

[p0325-b0022 | ordinary-paragraph | high] Therefore the boundedness assumption on D’G together with (3.48) yield:

[p0325-b0023 | ordinary-paragraph | high] ||u(A) — uy (A)li e< Cr LCy ||u A) — ua)I e + I-AA, uA) — FA, uA) lad,

[p0325-b0024 | ordinary-paragraph | high] which proves (3.51). te

[p0325-b0025 | subsection | high] 3.4. Non-Differentiable Approximation of Branches of Nonsingular Solutions

[p0325-b0026 | ordinary-paragraph | high] So far, we have assumed that the approximate mapping F,, retained the smooth-

[p0325-b0027 | ordinary-paragraph | high] ness properties of the mapping F, because the approximation was performed on

[p0325-b0028 | ordinary-paragraph | high] the linear operator T alone and not on G. But it is sometimes necessary to

[p0325-b0029 | ordinary-paragraph | high] approximate G by a mapping G, which is no longer differentiable. This occurs,

[p0325-b0030 | ordinary-paragraph | high] for example, when an upwind discretization of the convective terms is used in

[p0325-b0031 | ordinary-paragraph | high] the Navier-Stokes equations. This situation is analyzed by the following theory,

[p0325-b0032 | ordinary-paragraph | high] which is an easy variant of the one elaborated in Sections 3.2 and 3.3. The reader

[p0325-b0033 | ordinary-paragraph | high] can refer to Rappaz [67] for a more general approach that encompasses all the

[p0325-b0034 | ordinary-paragraph | high] material of this paragraph.

## PDF 326 / printed 312



[p0326-b0005 | ordinary-paragraph | medium] the mapping F, is defined and continuous on A x X, with values in X,. Then,

[p0326-b0006 | ordinary-paragraph | medium] for a given element u, of X, and a given Xe A, we replace the notion of differen-

[p0326-b0007 | ordinary-paragraph | medium] tiability by the following assumptions:

[p0326-b0008 | ordinary-paragraph | medium] there exists an operator VuF,(2,u,)e (X,;&,) which is an iso-

[p0326-b0009 | equation | low] (3.53)

[p0326-b0010 | ordinary-paragraph | medium] morphism from X, onto X,;

[p0326-b0011 | ordinary-paragraph | medium] there exists a continuous, monotonically increasing function

[p0326-b0012 | ordinary-paragraph | medium] μ→ L(; μ): R+ → R+ such that:

[p0326-b0013 | equation | low] (3.54)

[p0326-b0014 | equation | low] Fh(,u) -Fh(, w) —VuFh(a,un)·(v -w)llg ≤ Ln(;α)|lu -wllx

[p0326-b0015 | ordinary-paragraph | medium] for all v and w e S(u,; α) N Xh.

[p0326-b0016 | ordinary-paragraph | medium] We retain the following notations:

[p0326-b0017 | equation | low] &n(2) = IFh(A,un) llα,

[p0326-b0018 | equation | low] (3.55)

[p0326-b0019 | equation | low] Yh(2) = I1[VuF(A,an)]-1 11e(nxn)

[p0326-b0020 | ordinary-paragraph | low] where the norm II Bll &(,;x, stands for supoex,(Ill Bu llx/llull e). Then we have the

[p0326-b0021 | ordinary-paragraph | medium] analogue of Theorem 3.1.

[p0326-b0022 | theorem | medium] Theorem 3.6. If (3.53) and (3.54) hold and if, in addition:

[p0326-b0023 | equation | low] (3.19)

[p0326-b0024 | equation | low] 2h(2)Ln(2; 2yn(n)en(a)) < 1

[p0326-b0025 | ordinary-paragraph | medium] then Problem (3.12) has a unique solution (l, u,(l)) such that:

[p0326-b0026 | equation | low] (3.20)

[p0326-b0027 | ordinary-paragraph | low] uh(2)∈ S(un; 2yh(t)enh(a)) N Xh.

[p0326-b0028 | ordinary-paragraph | medium] In addition, u,(7) is the only solution of (3.12) in the larger ball S(un; α) N X, for all

[p0326-b0029 | ordinary-paragraph | medium] α ≥ 2yh(l)e,(l) that satisfy

[p0326-b0030 | equation | low] (3.22)

[p0326-b0031 | equation | low] h(2)Ln(n;α) < 1

[p0326-b0032 | ordinary-paragraph | medium] and we have the estimate:

[p0326-b0033 | equation | low] Ilun(2) - vn llx ≤ [n(2)/(1 -yh(2)Ln(;α))] 1/Fn(,vn)1lx

[p0326-b0034 | equation | low] (3.23)

[p0326-b0035 | ordinary-paragraph | low] Vuh e S(uh; α)N Xh.

[p0326-b0036 | ordinary-paragraph | medium] We skip the proof since it is very similar to that of Theorem 3.1. Likewise, we

[p0326-b0037 | ordinary-paragraph | medium] can easily prove the following counterpart of Theorem 3.2.

[p0326-b0038 | theorem | medium] Theorem 3.7. Let u, be a given function in C°(A; Xh) that satisfies:

[p0326-b0039 | equation | low] (3.26)

[p0326-b0040 | equation | low] = for some ho > 0,

[p0326-b0041 | equation | low] sup y,(l)

[p0326-b0042 | equation | low] sup[s

[p0326-b0043 | equation | low] h≤hol∈A

## PDF 327 / printed 313



[p0327-b0003 | equation | low] h>0 \AcA

[p0327-b0004 | ordinary-paragraph | high] If, in addition,

[p0327-b0005 | ordinary-paragraph | high] (3.56) sup L(A; w) =L,(u) Wh < ho,

[p0327-b0006 | ordinary-paragraph | high] AeA

[p0327-b0007 | ordinary-paragraph | high] where the function L,() is monotonically increasing with respect to « and h,

[p0327-b0008 | ordinary-paragraph | high] continuous at = 0, and such that:

[p0327-b0009 | ordinary-paragraph | high] (3:57) lim L,(0) = 0

[p0327-b0010 | equation | low] h>0

[p0327-b0011 | ordinary-paragraph | high] then there exists two real constants « > 0 and h, > 0 and a function u,€ @°(A; X,)

[p0327-b0012 | ordinary-paragraph | high] such that for allh < h,:

[p0327-b0013 | equation | low] {(A, u,(A)); A€ A} is a branch of solutions of (3.12),

[p0327-b0014 | ordinary-paragraph | high] for each A€ A, u,(A) is the only solution of (3.12) in S(ti,(A); 0) NX, and we have the

[p0327-b0015 | ordinary-paragraph | high] estimate:

[p0327-b0016 | ordinary-paragraph | high] (3.30') I|un(A) — Valle S27 FAA, en)ile Vo€S nH, (A), NX,

[p0327-b0017 | remark | high] Remark 3.8. The assumption that L,() be monotonically increasing with respect

[p0327-b0018 | ordinary-paragraph | high] to his not necessary. It can be replaced by the condition that L,() be uniformly

[p0327-b0019 | ordinary-paragraph | high] continuous with respect to hat pw = 0.

[p0327-b0020 | ordinary-paragraph | high] For the sake of simplicity, we are going to apply Theorem 3.7 to solve a

[p0327-b0021 | ordinary-paragraph | high] narrower range of problems than (3.33), but the reader will easily extend the

[p0327-b0022 | ordinary-paragraph | high] forthcoming analysis to the general case. More precisely, with the notations of

[p0327-b0023 | ordinary-paragraph | high] Section 3.3 we propose to solve the problem:

[p0327-b0024 | ordinary-paragraph | high] (3.33’) F(A,u) =u + ATG(u) = 0

[p0327-b0025 | ordinary-paragraph | high] where G is a @'-mapping from X into Y, A€A , a compact interval of R, and T

[p0327-b0026 | ordinary-paragraph | high] is unchanged but we assume that Te Y(Y; V) where V is a closed subspace of

[p0327-b0027 | ordinary-paragraph | high] X. This may amount to a regularity assumption on T. Furthermore, we suppose

[p0327-b0028 | ordinary-paragraph | high] that the problem

[p0327-b0029 | equation | low] F(A, u(A)) = 0

[p0327-b0030 | ordinary-paragraph | high] has a branch of nonsingular solutions 4 — u(A) from A into X with ue @°(A; V).

[p0327-b0031 | ordinary-paragraph | high] In view of the approximation, we introduce a closed subspace V, of X,

[p0327-b0032 | ordinary-paragraph | high] equipped with the norm of X and a space Y, that contains Y with continuous

[p0327-b0033 | ordinary-paragraph | high] imbedding. To avoid confusion, we denote the norm of ¥, by ||. ||,, The mapping

[p0327-b0034 | ordinary-paragraph | high] G is approximated by a @°-mapping G, from JV, into ¥, and T is approximated

[p0327-b0035 | ordinary-paragraph | high] by an operator T,,€ #(Y,; V;,). Then we set

[p0327-b0036 | ordinary-paragraph | high] (3.58) F(A, Uj,) = Uy, + AT, GU)

## PDF 328 / printed 314



[p0328-b0005 | theorem | medium] Theorem 3.8. Under the following hypotheses:

[p0328-b0006 | ordinary-paragraph | medium] (i)

[p0328-b0007 | equation | low] II Tllg(rnrn) ≤ C,

[p0328-b0008 | equation | low] (3.59)

[p0328-b0009 | equation | low] lim I T -- T ll(x;x) = 0.

[p0328-b0010 | equation | low] (3.60)

[p0328-b0011 | ordinary-paragraph | medium] h→0

[p0328-b0012 | ordinary-paragraph | medium] (ii) There exists an operator T,E E(V; V) such that:

[p0328-b0013 | equation | low] lim |- x =O  V∈V

[p0328-b0014 | equation | low] (3.61)

[p0328-b0015 | ordinary-paragraph | medium] h→0

[p0328-b0016 | ordinary-paragraph | medium] and

[p0328-b0017 | equation | low] (3.62)

[p0328-b0018 | equation | low] lim sup I/ G(π,u(2)) - G(u(2))ll, = 0.

[p0328-b0019 | ordinary-paragraph | low] h→0 A∈ A

[p0328-b0020 | ordinary-paragraph | medium] (i) For all u, e Vh, there exists an operator VG,(un)e Φ(Vh; Yn) such that

[p0328-b0021 | equation | low] (3.63)

[p0328-b0022 | equation | low] lim sup | G;(πu(2) - DG(u(2)Il g(vn;yn) = 0

[p0328-b0023 | ordinary-paragraph | low] h-→0 xe/

[p0328-b0024 | ordinary-paragraph | medium] and

[p0328-b0025 | ordinary-paragraph | low] (3.64) 1Gn(un) - Gh(u*) -DGn(u%)·(un -u*) lh ≤ Ln(μ; Ilu Ilx) Ilun -u* 1lx

[p0328-b0026 | ordinary-paragraph | medium] for all uhe Vh, uh and u*eS(u;μ)N Vh, where Ln: R+ x R+ → R+ is a contin-

[p0328-b0027 | ordinary-paragraph | medium] uous, monotonically increasing function with respect to each variable and with

[p0328-b0028 | ordinary-paragraph | medium] respect to h, which satisfies:

[p0328-b0029 | equation | low] lim L,(O; μ) = O  VμeR+.

[p0328-b0030 | equation | low] (3.65)

[p0328-b0031 | ordinary-paragraph | medium] h→0

[p0328-b0032 | ordinary-paragraph | medium] Then there exists a neighborhood O of the origin in X and for h ≤ ho small

[p0328-b0033 | ordinary-paragraph | medium] enough, a unique C°-function u,: A → V, such that

[p0328-b0034 | equation | low] (3.66)

[p0328-b0035 | equation | low] Fh(l,un(a)) = O,  un(n)∈u(x) + 0

[p0328-b0036 | ordinary-paragraph | medium] In addition, the following error estimate holds:

[p0328-b0037 | equation | low] Ilu(a) - u(2)lx ≤ C{ Il(1 - πn)u(2)llx + IIA(T - T)G(u(2))lx

[p0328-b0038 | equation | low] (3.67)

[p0328-b0039 | ordinary-paragraph | low] + I/Gn(πhu(a) - G(u(a)lln}.

[p0328-b0040 | proof | medium] Proof. Let us apply Theorem 3.7 with u, = u,(2) = π,u(2), Vh playing the role of

[p0328-b0041 | ordinary-paragraph | medium] X,. Since by assumption, u belongs to C°(A; V) then u, belongs to &°(A; Vh). Next,

[p0328-b0042 | ordinary-paragraph | medium] let us prove (3.27). We have:

[p0328-b0043 | equation | low] En(2) = I/F(l,an(2) - F(A,u(x)Ilx,

[p0328-b0044 | ordinary-paragraph | medium] i.e.

## PDF 329 / printed 315



[p0329-b0004 | ordinary-paragraph | high] + |A| (Th — T)GU(A)|)x .

[p0329-b0005 | ordinary-paragraph | high] But on the one hand, (3.61) and Ascoli’s Lemma imply that

[p0329-b0006 | equation | low] lim uD | a,(A) — u(A)|lx = 9.

[p0329-b0007 | equation | low] h>0 AeA

[p0329-b0008 | ordinary-paragraph | high] On the other hand, (3.59) and (3.62) yield:

[p0329-b0009 | equation | low] lim sup IlT {Gi(Gx(2)) — G(u(A))} Ix = 0

[p0329-b0010 | equation | low] h>0 AeA

[p0329-b0011 | ordinary-paragraph | high] In addition, it stems from the continuity of the mapping G and (3.60) that

[p0329-b0012 | equation | low] lim sup I(T, — T)G(u(A))l x = 0

[p0329-b0013 | equation | low] h>O0 AeA

[p0329-b0014 | ordinary-paragraph | high] These three limits give immediately (3.27’).

[p0329-b0015 | ordinary-paragraph | high] Now, we turn to (3.26’). For each u,€ V,, it is natural to define V,,F,(A, u,,)€

[p0329-b0016 | ordinary-paragraph | high] L(V,; Vi) by:

[p0329-b0017 | ordinary-paragraph | high] (3.69) VF (A, u,) = I + AT,VG,(u,).

[p0329-b0018 | ordinary-paragraph | high] Then we can write:

[p0329-b0019 | ordinary-paragraph | high] (3.70) VFA, %,(A)) = ATV G,(u,(4)) — DG(u(A))} + I + AT,DG(u(A)).

[p0329-b0020 | ordinary-paragraph | high] But observe that the operator J + AT, DG(u(A)) belongs to Y(X; X)N L(Y,; V,).

[p0329-b0021 | ordinary-paragraph | high] Furthermore,

[p0329-b0022 | equation | low] I + AT,DG(u(d)) — D, F(A, u()) = ACT, — T)DG(u(A))

[p0329-b0023 | ordinary-paragraph | high] and owing to (3.60) and the differentiability of G, we have

[p0329-b0024 | equation | low] lim sup (Th — T)DG(UA)Il) ganx = 9-

[p0329-b0025 | equation | low] h>O0 A€A

[p0329-b0026 | ordinary-paragraph | high] Hence, applying Lemma 3.3 we find that there exists a real hy > 0 such that for

[p0329-b0027 | ordinary-paragraph | high] all h < hy and all A€A , I + AT, DG(u(A)) is an isomorphism of X as well as an

[p0329-b0028 | ordinary-paragraph | high] isomorphism of V,. Besides that, we have the bound:

[p0329-b0029 | ordinary-paragraph | high] (3.71) | + AT,DGUA))) IN eonayy <A + AT,D G(UA))"I.ganx

[p0329-b0030 | equation | low] <2y(4) Wh<h) and Vie,

[p0329-b0031 | ordinary-paragraph | high] where 7(A) is defined by (3.13). Likewise, it follows from (3.59) and (3.63) that

[p0329-b0032 | equation | low] lim sup || T,( VinGa(G,(4)) — DG(u(A))} Iela sy, = 9:

[p0329-b0033 | equation | low] h>0 AeA

[p0329-b0034 | ordinary-paragraph | high] Therefore, applying again Lemma 3.3 and using (3.70) and (3.71), we see that

[p0329-b0035 | ordinary-paragraph | high] there exists another h,, with 0 < h, < ho, such that for all h < h, and all A€ A,

[p0329-b0036 | ordinary-paragraph | high] VF, (A, a,(A)) is an isomorphism of V, and

[p0329-b0037 | equation | low] IV F(A, a(A))1 : ll gv; ny) <= 4y(4) Wh<h, Vie.

[p0329-b0038 | ordinary-paragraph | high] As y(A) is bounded above, this establishes (3.26’).
