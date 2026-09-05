# Restored-source review candidate: chapter-03-section-01



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 207 / printed 193



[p0207-b0001 | chapter | high] Chapter III. Incompressible Mixed Finite

[p0207-b0002 | ordinary-paragraph | high] Element Methods for Solving the Stokes

[p0207-b0003 | ordinary-paragraph | high] Problem

[p0207-b0004 | section | high] §1. Mixed Approximation of an Abstract Problem

[p0207-b0005 | ordinary-paragraph | high] In this paragraph, we concentrate again upon the abstract problem studied in

[p0207-b0006 | chapter | high] Chapter I § 4, but we put it into a weaker setting leading to a (generally) different

[p0207-b0007 | ordinary-paragraph | high] mixed formulation. The mixed approximation derived from this formulation will

[p0207-b0008 | ordinary-paragraph | high] give rise to the important class of exactly incompressible methods to solve the

[p0207-b0009 | ordinary-paragraph | high] Stokes and Navier-Stokes equations.

[p0207-b0010 | subsection | high] 1.1. A Mixed Variational Problem

[p0207-b0011 | ordinary-paragraph | high] We put ourselves into the situation of Section 1.4.1. Recall that X and M are two

[p0207-b0012 | ordinary-paragraph | high] Hilbert spaces and that a(.,.) and b(., .) are two continuous bilinear forms on

[p0207-b0013 | ordinary-paragraph | high] X x X and X x M respectively. Recall that Problem (Q) is:

[p0207-b0014 | ordinary-paragraph | high] For (I, x) given in X' x M’, find a pair (u, A) in X x M with:

[p0207-b0015 | ordinary-paragraph | high] (1.1) a(u,v) + b(v,A)=<lv> VveX,

[p0207-b0016 | ordinary-paragraph | high] (1.2) blu, uw) = <u> VueM.

[p0207-b0017 | ordinary-paragraph | high] As usual, we set

[p0207-b0018 | equation | low] Vip) = {ve X; bw) =<~ > Vue M},

[p0207-b0019 | equation | low] V = 10):

[p0207-b0020 | ordinary-paragraph | high] Again, we assume that a(., .) and b(., .) satisfy the two hypotheses:

[p0207-b0021 | ordinary-paragraph | high] there exists a constant « > 0 such that

[p0207-b0022 | ordinary-paragraph | high] (1.3) a(v,> vall)v|| z VWvoeV;

[p0207-b0023 | ordinary-paragraph | high] there exists a constant B > 0 such that

[p0207-b0024 | ordinary-paragraph | high] b(v, 1)

[p0207-b0025 | ordinary-paragraph | high] (1.4) 2B\ulm VueM.

[p0207-b0026 | ordinary-paragraph | high] vex IVllx

## PDF 208 / printed 194



[p0208-b0004 | ordinary-paragraph | medium] Ipy1 yons (X)4 u1 n puid

[p0208-b0005 | ordinary-paragraph | low] A

[p0208-b0006 | equation | low] a(u,u) =<l,v)

[p0208-b0007 | equation | low] (1.5)

[p0208-b0008 | ordinary-paragraph | medium] are well posed.

[p0208-b0009 | ordinary-paragraph | medium] Let us elaborate a weaker formulation of Problem (Q) better suited to the

[p0208-b0010 | ordinary-paragraph | medium] approximation we have in mind. We introduce two reflexive Banach spaces X

[p0208-b0011 | ordinary-paragraph | medium] and M normed respectively by Il . lx and Il Il  such that:

[p0208-b0012 | ordinary-paragraph | low] XcX,  Mc M,

[p0208-b0013 | ordinary-paragraph | medium] d

[p0208-b0014 | ordinary-paragraph | medium] d

[p0208-b0015 | ordinary-paragraph | medium] where the sign  means that the imbedding is dense and continuous.

[p0208-b0016 | ordinary-paragraph | medium] Next, we consider two continuous bilinear forms:

[p0208-b0017 | ordinary-paragraph | medium] a(.,.): X×X→R,  b(.,.): Xx M→R,

[p0208-b0018 | ordinary-paragraph | medium] with the norms:

[p0208-b0019 | ordinary-paragraph | medium] b(v, μ)

[p0208-b0020 | ordinary-paragraph | medium] a(u, v)

[p0208-b0021 | equation | low] 6 = 

[p0208-b0022 | equation | low] all = sup

[p0208-b0023 | equation | low] sup

[p0208-b0024 | ordinary-paragraph | low] uvex|lulxl

[p0208-b0025 | ordinary-paragraph | low] vex.μeMllullxμ1M

[p0208-b0026 | ordinary-paragraph | medium] These two bilinear forms are extensions of a and b in the sense that

[p0208-b0027 | equation | low] (1.6)

[p0208-b0028 | ordinary-paragraph | low] 'Xaa'na

[p0208-b0029 | equation | low] a(u,v) = a(u,u)

[p0208-b0030 | equation | low] b(u,μ) =b(u,μ)

[p0208-b0031 | ordinary-paragraph | low] Vue M.

[p0208-b0032 | equation | low] (1.7)

[p0208-b0033 | ordinary-paragraph | low] 'XA

[p0208-b0034 | ordinary-paragraph | medium] In addition, we assume that the right-hand side I of (1.1) belongs to the dual space

[p0208-b0035 | ordinary-paragraph | medium] X' of X and we denote by <., . > the duality pairing between X and X'. Then we

[p0208-b0036 | ordinary-paragraph | medium] introduce the following Problem (Q):

[p0208-b0037 | ordinary-paragraph | medium] Find a pair (a, i)e X x M such that:

[p0208-b0038 | equation | low] (1.8)

[p0208-b0039 | ordinary-paragraph | low] 'XaA

[p0208-b0040 | equation | low] a(u,v) + b(v,x) =<lu>

[p0208-b0041 | equation | low] b(u,μ)=<xμ>Vμ∈M.

[p0208-b0042 | equation | low] (1.9)

[p0208-b0043 | ordinary-paragraph | medium] For each xe M' we define the affine variety:

[p0208-b0044 | equation | low] V(x) = {v∈X; b(u,μ) =<x,μ) Vμ∈ M},

[p0208-b0045 | equation | low] (1.10)

[p0208-b0046 | ordinary-paragraph | medium] and the following closed subspace of X:

[p0208-b0047 | equation | low] V = V(O) = {veX; b(u, μ) = 0 Vμe M}.

[p0208-b0048 | equation | low] (1.11)

[p0208-b0049 | ordinary-paragraph | medium] Equality (1.7) implies that:

[p0208-b0050 | equation | low] (X)A > (x)A >A

[p0208-b0051 | equation | low] (1.12)

[p0208-b0052 | ordinary-paragraph | medium] With the Problem (Q) we associate the following Problem (P):

[p0208-b0053 | ordinary-paragraph | medium] Find i in V(x) such that

## PDF 209 / printed 195



[p0209-b0002 | ordinary-paragraph | high] In order to analyze conveniently Problems (P) and (0) we make the following

[p0209-b0003 | ordinary-paragraph | high] assumption on d(., .):

[p0209-b0004 | ordinary-paragraph | high] the form G(., .) is V-elliptic, i.e. there exists a constant & > 0 such that:

[p0209-b0005 | ordinary-paragraph | high] (1.14) G(v,v) >al\lvl|J= We.

[p0209-b0006 | ordinary-paragraph | high] Note that on the one hand (1.14) does not stem from (1.3) because V is (usually)

[p0209-b0007 | ordinary-paragraph | high] a larger space than V. On the other hand there is no inf-sup condition on b(.,.)

[p0209-b0008 | ordinary-paragraph | high] except the one which follows from (1.4) and (1.7):

[p0209-b0009 | ordinary-paragraph | high] (1.15) sup cee Cte

[p0209-b0010 | equation | low] > (B/C) lula VueeM,

[p0209-b0011 | ordinary-paragraph | high] ve X | lx ve X llv llx

[p0209-b0012 | ordinary-paragraph | high] where C is the continuity constant of the imbedding X < X. Strictly speaking,

[p0209-b0013 | ordinary-paragraph | high] this is not sufficient to ensure that Problem (Q) is well posed. The next theorem

[p0209-b0014 | ordinary-paragraph | high] tackles this difficulty.

[p0209-b0015 | theorem | high] Theorem 1.1. Let (u, 4) be the solution of Problem (Q) and let satisfy (1.14).

[p0209-b0016 | ordinary-paragraph | high] 1°) Problem (P) has exactly one solution i in V(x). Moreover, if i also belongs

[p0209-b0017 | ordinary-paragraph | high] to V(x) or if V is dense in V then a = u.

[p0209-b0018 | ordinary-paragraph | high] 2°) In addition, if 4 belongs to M then the pair (u,A) is the only solution of

[p0209-b0019 | ordinary-paragraph | high] Problem (Q~ ).

[p0209-b0020 | proof | high] Proof. To begin with, recall that the theory of Section I.4.1 applies also to reflexive

[p0209-b0021 | ordinary-paragraph | high] Banach spaces (cf. Remark 1.4.2).

[p0209-b0022 | ordinary-paragraph | high] 1°) The inf-sup condition (1.4) on b(., .) implies that V(y) is not empty; hence

[p0209-b0023 | ordinary-paragraph | high] (x) is not empty. Then the ellipticity of @ implies that Problem (P) has one and

[p0209-b0024 | ordinary-paragraph | high] only one solution a in V(x). If ie V(x), we see from (1.6) that @ is a solution of

[p0209-b0025 | ordinary-paragraph | high] Problem (P); therefore a = u since (P) has exactly one solution. Otherwise, we

[p0209-b0026 | ordinary-paragraph | high] assume that V is dense in V; then (1.5) and (1.6) imply that u is a solution of

[p0209-b0027 | ordinary-paragraph | high] Problem (P). Thus u = @.

[p0209-b0028 | ordinary-paragraph | high] 2°) In addition, suppose that Ae M. Then by virtue of (1.6) and (1.7), (1.1)

[p0209-b0029 | ordinary-paragraph | high] becomes:

[p0209-b0030 | equation | low] a(u,v) + b(v,A) = <l,v> VWweXx.

[p0209-b0031 | ordinary-paragraph | high] As X is dense in X, this shows that the pair (u, 4) is a solution of Problem (Q).

[p0209-b0032 | ordinary-paragraph | high] Finally, we must prove that it is the only solution of (Q). Obviously, the first

[p0209-b0033 | ordinary-paragraph | high] component u is unique. Then assume that

[p0209-b0034 | equation | low] b(v,A4)=0 Wex.

[p0209-b0035 | ordinary-paragraph | high] Og

[p0209-b0036 | ordinary-paragraph | high] With (1.15) this implies that 4 = 0.

[p0209-b0037 | remark | high] Remark 1.1. The assumption A€ M is in fact a regularity condition.

## PDF 210 / printed 196



[p0210-b0004 | ordinary-paragraph | high] Throughout this section we assume that the hypotheses of Theorem 1.1 hold.

[p0210-b0005 | ordinary-paragraph | high] For each h let X, and M, be two finite-dimensional subspaces of X and M

[p0210-b0006 | ordinary-paragraph | high] respectively. We approximate Problem (Q) by Problem (Qh):

[p0210-b0007 | ordinary-paragraph | medium] Find a pair (un, Λn)e X, x M, such that

[p0210-b0008 | equation | low] "x="aA

[p0210-b0009 | equation | low] a(unsUn) +b(unn)=<l,Un>

[p0210-b0010 | equation | low] (1.16)

[p0210-b0011 | equation | low] b(unμn)=<xμn>

[p0210-b0012 | ordinary-paragraph | low] Vune Mh.

[p0210-b0013 | equation | low] (1.17)

[p0210-b0014 | ordinary-paragraph | high] Again we define

[p0210-b0015 | equation | low] Vh(x)={Un∈Xn;b(unμn) =<xμn>μn∈Mh},

[p0210-b0016 | equation | low] (1.18)

[p0210-b0017 | equation | low] Vh = V(0).

[p0210-b0018 | ordinary-paragraph | high] Next we associate with Problem (Qh) the following Problem (P,):

[p0210-b0019 | ordinary-paragraph | medium] Find u, e Vn(x) such that

[p0210-b0020 | equation | low] (1.19)

[p0210-b0021 | equation | low] "="aA

[p0210-b0022 | equation | low] a(unUn)=<l,Un)

[p0210-b0023 | ordinary-paragraph | high] Here also V, is generally not included in V and therefore Problem (Ph) is an

[p0210-b0024 | ordinary-paragraph | high] external approximation of Problem (P).

[p0210-b0025 | ordinary-paragraph | high] In order to derive error estimates for u, and X, we make the following

[p0210-b0026 | ordinary-paragraph | high] assumptions, analogous to (1.14) and (1.15):

[p0210-b0027 | equation | low] i) there exists a constant α* > 0 such that

[p0210-b0028 | equation | low] (1.20)

[p0210-b0029 | equation | low] :">"aA

[p0210-b0030 | equation | low] a(UnUn)≥α*|/0n11x

[p0210-b0031 | equation | low] i) there exists a constant β* > 0 such that

[p0210-b0032 | ordinary-paragraph | low] b(Unμn)

[p0210-b0033 | equation | low] (1.21)

[p0210-b0034 | equation | low] ≥β*1|/μnl M

[p0210-b0035 | ordinary-paragraph | low] Vuh e Mh.

[p0210-b0036 | equation | low] sup

[p0210-b0037 | ordinary-paragraph | low] vhexnltunllx

[p0210-b0038 | ordinary-paragraph | high] The next theorem is a natural extension of Theorem 11.1.1.

[p0210-b0039 | theorem | high] Theorem 1.2. 1°) Suppose V(x) is not empty and a(., .) satisfies (1.20). Then

[p0210-b0040 | ordinary-paragraph | high] Problem (Ph) has a unique solution u, e Vh(x) and the following error bound holds:

[p0210-b0041 | ordinary-paragraph | low] b(un—μn)

[p0210-b0042 | ordinary-paragraph | medium] Ilu-u,llx≤(1+llall/α*) inf |lu-vnllx+(1/α*) inf 

[p0210-b0043 | equation | low] sup

[p0210-b0044 | ordinary-paragraph | low] Ivnll x

[p0210-b0045 | equation | low] (x)A =4a

[p0210-b0046 | ordinary-paragraph | low] μn∈Mn une Vn

[p0210-b0047 | equation | low] (1.22)

[p0210-b0048 | ordinary-paragraph | high] 2°) Suppose moreover that b(., .) satisfies (1.21). Then Vh(x) is not empty and

[p0210-b0049 | ordinary-paragraph | high] Problem (Qn) has exactly one solution (un, Λh) where u, is the solution of Problem

[p0210-b0050 | ordinary-paragraph | high] (Ph). Furthermore N, satisfies the error estimate:

[p0210-b0051 | ordinary-paragraph | medium] /llall

[p0210-b0052 | ordinary-paragraph | low] 1161

[p0210-b0053 | ordinary-paragraph | low] 11—μnl+1—μnllm{

[p0210-b0054 | ordinary-paragraph | low] 1 -llm≤

[p0210-b0055 | equation | low] Iu -— unllx+  inf

[p0210-b0056 | ordinary-paragraph | low] β*

[p0210-b0057 | ordinary-paragraph | high] B*

[p0210-b0058 | ordinary-paragraph | low] μhEMh

## PDF 211 / printed 197



[p0211-b0002 | proof | high] Proof. 1°) The idea of the proof is very similar to that of Theorem II.1.1. The

[p0211-b0003 | ordinary-paragraph | high] existence and uniqueness of the solution u, of Problem (P,,) follow from (1.20)

[p0211-b0004 | ordinary-paragraph | high] and Lax & Milgram’s Theorem I.1.7, provided V,(y) is not empty.

[p0211-b0005 | ordinary-paragraph | high] Now, let w, be any element of V,(x) and let v, = u, — w,€ V,. Then formula

[p0211-b0006 | ordinary-paragraph | high] (II.1.15) holds:

[p0211-b0007 | equation | low] A(V,,0,) = A(U — Wy, Vp) + b(v,, A —Hn) VoneM,, Vw,eV,(2)-

[p0211-b0008 | ordinary-paragraph | high] Thus (1.20) implies:

[p0211-b0009 | ordinary-paragraph | high] {PtsA — by)

[p0211-b0010 | ordinary-paragraph | high] a* ||v,llz < [4] |u — wally + sup 5 VunEM,, VwneVi(”)

[p0211-b0011 | ordinary-paragraph | high] vpE,e V y, lon lle

[p0211-b0012 | ordinary-paragraph | high] and this gives immediately (1.22).

[p0211-b0013 | ordinary-paragraph | high] 2°) Since the dimension of M, is finite, the condition (1.21) implies the classical

[p0211-b0014 | ordinary-paragraph | high] inf-sup condition on M,, eventually with a constant that depends upon h.

[p0211-b0015 | ordinary-paragraph | high] Therefore V,(x) is not empty and Problem (Q,) has exactly one solution (u,, A,)

[p0211-b0016 | ordinary-paragraph | high] where u, satisfies Problem (P,,). Moreover, the following equality holds for any

[p0211-b0017 | ordinary-paragraph | high] v, in X, and pw, in M,:

[p0211-b0018 | ordinary-paragraph | high] (1.24) Bp An— Mn) = G(u — Uy, Vp) + B(V,, A — My):

[p0211-b0019 | ordinary-paragraph | high] Then it stems from (1.21) that:

[p0211-b0020 | equation | low] B* An — Mallar <4 lu — walle + BIA = walla

[p0211-b0021 | ordinary-paragraph | high] and (1.23) is established. fai]

[p0211-b0022 | ordinary-paragraph | high] Note that the estimate (1.23) is not optimal inasmuch as it gives an upper

[p0211-b0023 | ordinary-paragraph | high] bound for ||/A — A, ||, in terms of || — 4, ||,q while the two norms are usually not

[p0211-b0024 | ordinary-paragraph | high] meant to be equivalent. The examples of §3 will show how to overcome this

[p0211-b0025 | ordinary-paragraph | high] defect.

[p0211-b0026 | ordinary-paragraph | high] Observe also that it is often difficult to evaluate directly an expression like

[p0211-b0027 | equation | low] inf ||ju — v,||<z.

[p0211-b0028 | ordinary-paragraph | high] vp € Vi,(X)

[p0211-b0029 | ordinary-paragraph | high] Like in Chapter IJ, it is possible to reduce this term to the approximation error

[p0211-b0030 | ordinary-paragraph | high] in X,, although here the process is not always optimal. As M, is finite-dimensional,

[p0211-b0031 | ordinary-paragraph | high] there exists a constant K(h) > 0 such that

[p0211-b0032 | ordinary-paragraph | high] (1.25) Wella < KA) ella =Yue M,,.

[p0211-b0033 | ordinary-paragraph | high] With this we readily prove the following result.

[p0211-b0034 | corollary | high] Corollary 1.1. With the assumptions (1.20) and (1.21) each v in V(x) satisfies:

[p0211-b0035 | ordinary-paragraph | high] (1.26) inf |v — lle < C1 + KA)(N611/6*)] a lv — vlyl e.

[p0211-b0036 | ordinary-paragraph | high] vp E Vn (X) vnE Xp
