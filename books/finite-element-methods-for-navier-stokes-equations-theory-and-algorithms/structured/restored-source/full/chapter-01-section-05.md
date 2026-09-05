# Restored-source review candidate: chapter-01-section-05



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 92 / printed 78



[p0092-b0004 | equation | low] gm = c(g"m, gm)/c(gm-1,gm-1)

[p0092-b0005 | equation | low] only if m ≥ 1,

[p0092-b0006 | equation | low] @wm = gm+ omcm-1

[p0092-b0007 | equation | low] w° = g? otherwise,

[p0092-b0008 | equation | low] (4.70)

[p0092-b0009 | equation | low] A,zm = B'o)m,

[p0092-b0010 | equation | low] pm = c(gm,gm)/b(zm, gm),

[p0092-b0011 | equation | low] Am+1 =Am—pmcom,

[p0092-b0012 | equation | low] um+1 = um + pmzm.

[p0092-b0013 | ordinary-paragraph | medium] Note that the volume of computation per iteration is slightly larger than that of

[p0092-b0014 | ordinary-paragraph | medium] the simple-gradient algorithm; but the bulk of the computation still lies in the

[p0092-b0015 | ordinary-paragraph | medium] inversion of A,.

[p0092-b0016 | ordinary-paragraph | medium] Finally, it is easy to prove the convergence of this scheme.

[p0092-b0017 | corollary | medium] Corollary 4.6. Under the hypotheses of Corollary 4.4, the conjugate-gradient al-

[p0092-b0018 | ordinary-paragraph | medium] gorithm (4.70) is convergent.

[p0092-b0019 | proof | medium] Proof. Observe that the convergence criterion (4.58) is equivalent to:

[p0092-b0020 | equation | low] (4.71)

[p0092-b0021 | equation | low] p" ≥ α'llg" ll m/llo" Il m  for some constant α' > 0.

[p0092-b0022 | ordinary-paragraph | medium] Indeed, in view of (4.57) and the expression of z" we have

[p0092-b0023 | equation | low] pm =c(gm,wm)/b(zm,cm)

[p0092-b0024 | equation | low] = c(gm,wm)/D²K,·(@m, ∞m).

[p0092-b0025 | ordinary-paragraph | medium] Hence, (4.58) and (4.59) imply (4.71) with α' = α/t,; conversely (4.71) and (4.59)

[p0092-b0026 | ordinary-paragraph | medium] yield (4.58) with α = α'8,.

[p0092-b0027 | ordinary-paragraph | medium] Next, note that

[p0092-b0028 | equation | low] D²K·(∞m,gm) = D²K·(∞m,∞m) > 0

[p0092-b0029 | ordinary-paragraph | low] 'uA

[p0092-b0030 | ordinary-paragraph | medium] Therefore (4.71) is an immediate consequence of (4.68). Hence the scheme is

[p0092-b0031 | ordinary-paragraph | medium] convergent.

[p0092-b0032 | ordinary-paragraph | medium] 口

[p0092-b0033 | ordinary-paragraph | medium] s 5. The Stokes Equations

[p0092-b0034 | ordinary-paragraph | medium] Let us consider the Navier-Stokes equations describing the N-dimensional mo-

[p0092-b0035 | ordinary-paragraph | medium] tion of an incompressible viscous fluid:

[p0092-b0036 | ordinary-paragraph | low] N 00u

[p0092-b0037 | ordinary-paragraph | low] (dui

[p0092-b0038 | ordinary-paragraph | medium] dui

[p0092-b0039 | ordinary-paragraph | medium] N

[p0092-b0040 | equation | low] =pf，1≤i≤N,

[p0092-b0041 | equation | low] (5.1)

[p0092-b0042 | ordinary-paragraph | low] dt

[p0092-b0043 | ordinary-paragraph | medium] N

[p0092-b0044 | equation | low]  ∑ D:(u) = 0 (incompressibility condition),

[p0092-b0045 | equation | low] (5.2)

[p0092-b0046 | equation | low] divu =

[p0092-b0047 | equation | low] =

## PDF 93 / printed 79



[p0093-b0004 | equation | low] (5.3)

[p0093-b0005 | equation | low] j = -P8ij+ 2μD(u),

[p0093-b0006 | equation | low] 1≤i,j≤ N,

[p0093-b0007 | ordinary-paragraph | medium] and

[p0093-b0008 | equation | low] D;(u) = (1/2)(0u;/0x; + du;/0xi).

[p0093-b0009 | ordinary-paragraph | medium] In these equations, u = (u1,..., un) is the velocity of the fluid, p is its density

[p0093-b0010 | ordinary-paragraph | medium] (assumed to be constant), μ > 0 is its viscosity (also assumed to be constant) and

[p0093-b0011 | ordinary-paragraph | medium] P is its pressure; (o;) is the stress tensor and f = (fi,..., Jn) represents a density

[p0093-b0012 | ordinary-paragraph | medium] of body forces per unit mass (gravity for instance).

[p0093-b0013 | ordinary-paragraph | medium] As usual, we set

[p0093-b0014 | equation | low] (5.4)

[p0093-b0015 | equation | low] p = P/p,  v = μ/p.

[p0093-b0016 | ordinary-paragraph | medium] Here, p is the kinematic pressure and v is the kinematic viscosity but for the sake

[p0093-b0017 | ordinary-paragraph | medium] of simplicity, they will be called in the sequel pressure and viscosity. With these

[p0093-b0018 | ordinary-paragraph | medium] notations, the Navier-Stokes equations become

[p0093-b0019 | ordinary-paragraph | low] μ aD,(u)

[p0093-b0020 | ordinary-paragraph | medium] dui

[p0093-b0021 | ordinary-paragraph | medium] N

[p0093-b0022 | ordinary-paragraph | medium] dui

[p0093-b0023 | ordinary-paragraph | low] op

[p0093-b0024 | ordinary-paragraph | low] -2v

[p0093-b0025 | equation | low] =f, 1≤i≤N,

[p0093-b0026 | ordinary-paragraph | low] 0xj

[p0093-b0027 | ordinary-paragraph | low] at

[p0093-b0028 | equation | low] (5.5)

[p0093-b0029 | equation | low] div u = 0.

[p0093-b0030 | ordinary-paragraph | medium] Note that, when div u = O, the following identity holds

[p0093-b0031 | ordinary-paragraph | low] N aD;(μ)

[p0093-b0032 | ordinary-paragraph | low] 0²uj

[p0093-b0033 | ordinary-paragraph | low] (0²u;

[p0093-b0034 | ordinary-paragraph | medium] N

[p0093-b0035 | equation | low] =(1/2)

[p0093-b0036 | equation | low] (5.6)

[p0093-b0037 | equation | low] = (1/2)4u;

[p0093-b0038 | ordinary-paragraph | low] 0x;0xj

[p0093-b0039 | ordinary-paragraph | low] axj

[p0093-b0040 | ordinary-paragraph | low] 0x

[p0093-b0041 | ordinary-paragraph | medium] so that (5.5) can be written more conveniently

[p0093-b0042 | ordinary-paragraph | low] Cu

[p0093-b0043 | ordinary-paragraph | medium] N

[p0093-b0044 | ordinary-paragraph | medium] Cu

[p0093-b0045 | equation | low] - v4u + grad p = f,

[p0093-b0046 | ordinary-paragraph | low] 0xj

[p0093-b0047 | equation | low] (5.7)

[p0093-b0048 | ordinary-paragraph | low] 1e

[p0093-b0049 | equation | low] =1

[p0093-b0050 | equation | low] div u = 0.

[p0093-b0051 | ordinary-paragraph | medium] introducing a parameter (the Reynolds number) which measures the effect of

[p0093-b0052 | ordinary-paragraph | medium] viscosity on the flow. For a given problem, let L be a characteristic length and

[p0093-b0053 | ordinary-paragraph | medium] U a characteristic velocity. This determines a characteristic time T = L/U. Then,

[p0093-b0054 | ordinary-paragraph | medium] we introduce the dimensionless quantities

[p0093-b0055 | equation | low] x' = x/L,  u' = u/U， t' = t/T.

[p0093-b0056 | ordinary-paragraph | medium] Using this change of variables, it is easy to check that the Navier-Stokes equa-

[p0093-b0057 | ordinary-paragraph | medium] tions become (with obvious notations):

[p0093-b0058 | ordinary-paragraph | low] du'

[p0093-b0059 | ordinary-paragraph | medium] N

[p0093-b0060 | ordinary-paragraph | low] du'

[p0093-b0061 | ordinary-paragraph | low] V

[p0093-b0062 | equation | low] 4'u' + grad' p' = f'

[p0093-b0063 | ordinary-paragraph | medium] +

[p0093-b0064 | ordinary-paragraph | medium] Ot'

[p0093-b0065 | ordinary-paragraph | medium] 0x'

[p0093-b0066 | ordinary-paragraph | medium] LU

## PDF 94 / printed 80



[p0094-b0004 | equation | low] p' = P/(pU²),  f' = Lf/U2.

[p0094-b0005 | ordinary-paragraph | medium] Now, if we define the Reynolds number Re to be the dimensionless number

[p0094-b0006 | equation | low] Re = LU/v,

[p0094-b0007 | ordinary-paragraph | medium] we find that the Navier-Stokes equations may be written in dimensionless

[p0094-b0008 | ordinary-paragraph | medium] variables

[p0094-b0009 | ordinary-paragraph | medium] N

[p0094-b0010 | ordinary-paragraph | low] du

[p0094-b0011 | ordinary-paragraph | medium] 1

[p0094-b0012 | ordinary-paragraph | low] du

[p0094-b0013 | equation | low] u + grad p = f,

[p0094-b0014 | ordinary-paragraph | medium] Re

[p0094-b0015 | ordinary-paragraph | low] 1e

[p0094-b0016 | equation | low] (5.8)

[p0094-b0017 | equation | low] div u = 0.

[p0094-b0018 | ordinary-paragraph | medium] We obtain again the equations (5.7) with v replaced by 1/Re.

[p0094-b0019 | ordinary-paragraph | medium] For the time being, we introduce two simplifications in the equations (5.5) or

[p0094-b0020 | ordinary-paragraph | medium] (5.7). We only consider the steady-state (or stationary) case, that is 0u/ot = 0, and

[p0094-b0021 | ordinary-paragraph | medium] furthermore we assume that the velocity u is sufficiently small for ignoring the

[p0094-b0022 | ordinary-paragraph | medium] nonlinear convection terms u;(?u;/ox,). Thus we are led to the Stokes equations

[p0094-b0023 | ordinary-paragraph | low] 0D,(u)

[p0094-b0024 | ordinary-paragraph | low] V

[p0094-b0025 | ordinary-paragraph | low] dp

[p0094-b0026 | equation | low] =f，1≤i≤N,

[p0094-b0027 | ordinary-paragraph | medium] 2v

[p0094-b0028 | ordinary-paragraph | low] 0xi

[p0094-b0029 | equation | low] (5.9)

[p0094-b0030 | ordinary-paragraph | medium] 0x;

[p0094-b0031 | equation | low] =1

[p0094-b0032 | equation | low] div u = 0,

[p0094-b0033 | ordinary-paragraph | medium] which can be written more conveniently

[p0094-b0034 | equation | low] - v4u + grad p = f

[p0094-b0035 | equation | low] (5.10)

[p0094-b0036 | equation | low] div u = 0.

[p0094-b0037 | ordinary-paragraph | medium] The Stokes equations are linear but nevertheless they deserve special atten-

[p0094-b0038 | ordinary-paragraph | medium] tion because of the incompressibility condition div u = O. In this paragraph, we

[p0094-b0039 | ordinary-paragraph | medium] shall establish the existence and uniqueness of the solution of the Stokes equa-

[p0094-b0040 | ordinary-paragraph | medium] tions and we shall derive several variational formulations that will be used later

[p0094-b0041 | ordinary-paragraph | medium] on for approximation purposes.

[p0094-b0042 | subsection | medium] 5.1. The Dirichlet Problem in the Velocity-Pressure Formulation

[p0094-b0043 | ordinary-paragraph | medium] In order to get a well-posed problem for the Stokes equations (5.10), we have

[p0094-b0044 | ordinary-paragraph | medium] to complete them with appropriate boundary conditions. We begin with the

[p0094-b0045 | ordinary-paragraph | medium] Dirichlet boundary conditions.

[p0094-b0046 | theorem | medium] Theorem 5.1. Let Q be a bounded and connected open subset of RN with a Lipschitz-

[p0094-b0047 | ordinary-paragraph | medium] continuous boundary F. Given fe H-1(Q) and ge H1/2(F) such that

[p0094-b0048 | equation | low] (5.11)

[p0094-b0049 | equation | low] g·nds = 0,

[p0094-b0050 | ordinary-paragraph | low] JF

## PDF 95 / printed 81



[p0095-b0004 | equation | low] [-v4u + gradp = f in Ω,

[p0095-b0005 | equation | low] (5.12)

[p0095-b0006 | equation | low] divu = 0 in Ω,

[p0095-b0007 | equation | low] u=g on I.

[p0095-b0008 | proof | medium] Proof. By virtue of (5.11) and Lemma 2.2, there exists a function uo e H' (Q) such

[p0095-b0009 | ordinary-paragraph | medium] that

[p0095-b0010 | equation | low] divuo = 0 in Ω, 

[p0095-b0011 | equation | low] uo =g on I.

[p0095-b0012 | ordinary-paragraph | medium] Now, let us put Problem (5.12) into the framework of Paragraph 4. We set:

[p0095-b0013 | equation | low] X = H(Ω), M = L(Ω)

[p0095-b0014 | equation | low] with norms I . Ilx = I.l1,Ω,

[p0095-b0015 | equation | low] Il llm = Il llo,&,

[p0095-b0016 | ordinary-paragraph | low] du; Ov;

[p0095-b0017 | ordinary-paragraph | medium] N

[p0095-b0018 | equation | low] (5.13)

[p0095-b0019 | equation | low] a(u,v) =v ∑

[p0095-b0020 | equation | low]  v(grad u, grad v),

[p0095-b0021 | equation | low] ij=1(0x²0xj

[p0095-b0022 | equation | low] b(v,q) = -(q, divv),

[p0095-b0023 | equation | low] <l,v> = <f,v> - a(uo, v),  x = 0.

[p0095-b0024 | ordinary-paragraph | medium] Then

[p0095-b0025 | equation | low] V = {ve H(Ω); divv = 0}.

[p0095-b0026 | ordinary-paragraph | medium] We must check that the form a(., . ) is V-elliptic and the form b(., .) satisfies the

[p0095-b0027 | ordinary-paragraph | medium] inf-sup condition (4.9). On the one hand, the ellipticity property is obvious since

[p0095-b0028 | equation | low] a(v, v) = v/v/li,2.

[p0095-b0029 | ordinary-paragraph | medium] On the other hand, the inf-sup condition says that

[p0095-b0030 | equation | low] (q, div v)

[p0095-b0031 | equation | low] ≥βllallo.s

[p0095-b0032 | ordinary-paragraph | medium] Vqe La(Ω).

[p0095-b0033 | equation | low] (5.14)

[p0095-b0034 | equation | low] sup

[p0095-b0035 | ordinary-paragraph | low] veH(2)N  IVl1.0

[p0095-b0036 | ordinary-paragraph | medium] Let qe L?(Q); by virtue of Corollary 2.4, there exists a unique function ve V1

[p0095-b0037 | ordinary-paragraph | medium] such that

[p0095-b0038 | equation | low] Ivl1.o ≤ C llallo.2.

[p0095-b0039 | equation | low] divv = q,

[p0095-b0040 | ordinary-paragraph | medium] Hence

[p0095-b0041 | ordinary-paragraph | low] Ivl1,2

[p0095-b0042 | ordinary-paragraph | medium] [vl1.2

[p0095-b0043 | ordinary-paragraph | medium] from which (5.14) follows with β = 1/C.

[p0095-b0044 | ordinary-paragraph | medium] We are now in a position to apply Corollary 4.1: there exists a unique pair

[p0095-b0045 | ordinary-paragraph | medium] of functions (w, p)e Hl(Q) x L?(Ω) such that

## PDF 96 / printed 82



[p0096-b0005 | equation | low] b(w,q) = 0  Vq∈ L(Ω).

[p0096-b0006 | ordinary-paragraph | medium] Equivalently (u = uo + w, p)e [uo + H(Ω)*] x L2(Ω) is the solution of the

[p0096-b0007 | ordinary-paragraph | medium] equations

[p0096-b0008 | ordinary-paragraph | low] ()HA

[p0096-b0009 | equation | low] v(grad u, grad v) - (p, div v) = <f, v)

[p0096-b0010 | equation | low] (q, divu) = 0  Vqe L?(Ω).

[p0096-b0011 | ordinary-paragraph | medium] Moreover, ueuo + H(Q) if and only if

[p0096-b0012 | equation | low] ulr = g.

[p0096-b0013 | ordinary-paragraph | medium] ue H'(Q),

[p0096-b0014 | ordinary-paragraph | medium] Hence, there exists a unique pair (u, p)e H'(Q) x L2(Q) such that

[p0096-b0015 | ordinary-paragraph | low] N()HA

[p0096-b0016 | equation | low] v(grad u, grad v) - (p, div v) = <f, v)

[p0096-b0017 | equation | low] div u = 0,

[p0096-b0018 | equation | low] ulr = g.

[p0096-b0019 | ordinary-paragraph | medium] Now, using classical arguments, it is easy to show that this last problem is

[p0096-b0020 | ordinary-paragraph | medium] equivalent to Problem (5.12).

[p0096-b0021 | ordinary-paragraph | low] 口

[p0096-b0022 | remark | medium] Remark 5.1. The choice M = L?(Q) in (5.13) is only a matter of convenience and

[p0096-b0023 | ordinary-paragraph | medium] we can just as well take M = L?(Q)/R. On the other hand, we can also choose

[p0096-b0024 | ordinary-paragraph | medium] in the above proof

[p0096-b0025 | ordinary-paragraph | medium] N

[p0096-b0026 | equation | low] a(u, v) = 2v ∑

[p0096-b0027 | ordinary-paragraph | medium] D;(u) D;(v) dx.

[p0096-b0028 | equation | low] i,j=1 JΩ

[p0096-b0029 | ordinary-paragraph | medium] This is a consequence of the following identity:

[p0096-b0030 | ordinary-paragraph | medium] N

[p0096-b0031 | equation | low] (5.15)

[p0096-b0032 | equation | low] i.j=1 JQ

[p0096-b0033 | ordinary-paragraph | medium] which holds for all ue H'(Q) with div u = 0 and all ve H(Q)*. In fact, using

[p0096-b0034 | ordinary-paragraph | medium] the symmetry of the operator D; with respect to i and j, we have

[p0096-b0035 | ordinary-paragraph | low] Dvi dx.

[p0096-b0036 | equation | low] D;(u)D;(v)dx =

[p0096-b0037 | ordinary-paragraph | medium] D;(u)

[p0096-b0038 | ordinary-paragraph | low] 0xj

[p0096-b0039 | equation | low] i,j=1 JΩ

[p0096-b0040 | equation | low] i,j=1

[p0096-b0041 | ordinary-paragraph | low] 1JQ

[p0096-b0042 | ordinary-paragraph | medium] Moreover, we get

[p0096-b0043 | equation | low] du, 0i dx =

[p0096-b0044 | ordinary-paragraph | medium] adivu

[p0096-b0045 | ordinary-paragraph | low] -0

[p0096-b0046 | ordinary-paragraph | medium] Jo0x; 0xj

[p0096-b0047 | ordinary-paragraph | low] 0x

[p0096-b0048 | ordinary-paragraph | medium] from which (5.15) follows.

[p0096-b0049 | remark | medium] Remark 5.2. Problem (5.12) has the following variational formulations of (Q) and

[p0096-b0050 | ordinary-paragraph | medium] (P) types respectively:

## PDF 97 / printed 83



[p0097-b0004 | equation | low] a(u, v) - (p, div v) = <f,v)

[p0097-b0005 | ordinary-paragraph | low] ()HA

[p0097-b0006 | equation | low] (5.16)

[p0097-b0007 | equation | low] (q, div u) = 0

[p0097-b0008 | ordinary-paragraph | medium] Vqe L?(Ω),

[p0097-b0009 | equation | low] u=g on I,

[p0097-b0010 | ordinary-paragraph | medium] and

[p0097-b0011 | ordinary-paragraph | medium] Find ue H'(Q) such that

[p0097-b0012 | equation | low] a(u, v) = <f,v)

[p0097-b0013 | equation | low] (5.17)

[p0097-b0014 | equation | low] divu = 0 in Ω,

[p0097-b0015 | ordinary-paragraph | medium] on F,

[p0097-b0016 | equation | low] μ=g

[p0097-b0017 | ordinary-paragraph | medium] where

[p0097-b0018 | equation | low] v(grad u, grad v),

[p0097-b0019 | equation | low] a(u,v) =

[p0097-b0020 | ordinary-paragraph | medium] N

[p0097-b0021 | ordinary-paragraph | medium] (D,(u), Dy(v)).

[p0097-b0022 | ordinary-paragraph | medium] 2v

[p0097-b0023 | ordinary-paragraph | low] ?

[p0097-b0024 | remark | medium] Remark 5.3. Corollary 4.1 yields the bound:

[p0097-b0025 | equation | low] I|ull 1,2 + Il pllo,2 ≤ C(llfll -1. + Iluo ll1.)

[p0097-b0026 | ordinary-paragraph | medium] for all functions uo in H'(Q) satisfying divuo = O, uolr = g. By taking the

[p0097-b0027 | ordinary-paragraph | medium] infimum with respect to uo, this becomes

[p0097-b0028 | equation | low] IIu ll ,2 + Ilpll o,o ≤ C(lfll-1,2 + Ilg ll 1/2,r).

[p0097-b0029 | ordinary-paragraph | medium] Problem (5.12) can also be expressed as a saddle-point problem. With the

[p0097-b0030 | ordinary-paragraph | medium] above notations, we set

[p0097-b0031 | equation | low] (5.18)

[p0097-b0032 | equation | low] J(v) = (1/2)a(v,v) -<f,v),

[p0097-b0033 | equation | low] (5.19)

[p0097-b0034 | equation | low] (v,q) = J(v) -- (q, div v).

[p0097-b0035 | theorem | medium] Theorem 5.2. Under the hypotheses of Theorem 5.1, the solution (u, p) of (5.12) is

[p0097-b0036 | ordinary-paragraph | medium] characterized by:

[p0097-b0037 | equation | low] (u,p) = Min  sup_ E(v,q)

[p0097-b0038 | ordinary-paragraph | low] ()()HA

[p0097-b0039 | equation | low] vr=g

[p0097-b0040 | equation | low] (5.20)

[p0097-b0041 | equation | low] inf Y(v,q).

[p0097-b0042 | ordinary-paragraph | medium] Max

[p0097-b0043 | ordinary-paragraph | low] ()H3A(2)7 b

[p0097-b0044 | equation | low] vlr=g

[p0097-b0045 | proof | medium] Proof. We use the notations (5.13). Since the form a(.,.) is symmetric and

[p0097-b0046 | ordinary-paragraph | medium] H(Q) elliptic and the form b( ., . ) satisfies the inf-sup condition (5.14), we may

[p0097-b0047 | ordinary-paragraph | medium] apply Theorem 4.2. We find that the pair (u - uo, p) is the unique saddle-point

## PDF 98 / printed 84



[p0098-b0004 | ordinary-paragraph | high] over the product space H(Q) x L?(Ω). By taking into account that div uo =

[p0098-b0005 | ordinary-paragraph | high] div u = O, this exactly means that

[p0098-b0006 | ordinary-paragraph | low] VveH(Ω), q∈ L(Ω)

[p0098-b0007 | equation | low] L(u,q) = L(u, p) ≤ L(v + uo, p)

[p0098-b0008 | ordinary-paragraph | high] and therefore that (u, p) is the unique saddle-point of the functional Φ over

[p0098-b0009 | ordinary-paragraph | medium] [uo + H(2)"] × L2(Ω).

[p0098-b0010 | ordinary-paragraph | high] Now, using

[p0098-b0011 | equation | low] uo + H(Ω) = {veH(Ω); vlr = g}

[p0098-b0012 | ordinary-paragraph | high] and arguing as in the proof of Corollary 4.2, we obtain the characterization (5.20).

[p0098-b0013 | ordinary-paragraph | medium] 口

[p0098-b0014 | ordinary-paragraph | high] By adapting the arguments of Paragraph 4.2 to the present situation, we find

[p0098-b0015 | ordinary-paragraph | high] that u is characterized by

[p0098-b0016 | equation | low] inf  J(v).

[p0098-b0017 | equation | low] J(u) =

[p0098-b0018 | equation | low] (5.21)

[p0098-b0019 | ordinary-paragraph | low] veH1(2)

[p0098-b0020 | equation | low] divv=0,vlr=g

[p0098-b0021 | ordinary-paragraph | high] On the other hand, with any qe L2(Q), we associate the solution u(q)e H'(Q)

[p0098-b0022 | ordinary-paragraph | high] of the boundary value problem

[p0098-b0023 | equation | low] -v4u(q) = f - gradq in Ω,

[p0098-b0024 | equation | low] (5.22)

[p0098-b0025 | equation | low] u =g on I.

[p0098-b0026 | ordinary-paragraph | high] Then setting

[p0098-b0027 | equation | low] (5.23)

[p0098-b0028 | equation | low] K(q) = (1/2)a(w(q), w(q))

[p0098-b0029 | ordinary-paragraph | high] where w(q) = u(q) - uo with div uo = O, uolr = g, we find that the function p∈

[p0098-b0030 | ordinary-paragraph | high] L?(Q) is characterized by

[p0098-b0031 | equation | low] (5.24)

[p0098-b0032 | equation | low] K(p) = Min K(q).

[p0098-b0033 | ordinary-paragraph | low] qe L(S)

[p0098-b0034 | ordinary-paragraph | high] In order to eliminate the pressure, we can use the regularization method or

[p0098-b0035 | ordinary-paragraph | high] penalty method introduced in Section 4.3. We consider the following problem:

[p0098-b0036 | equation | low] Given & > 0, find (u, p)e H1(Q) x L?(Ω) such that

[p0098-b0037 | equation | low] -v4u + grad p' = f in Ω,

[p0098-b0038 | equation | low] (5.25)

[p0098-b0039 | equation | low] p = -(1/8)divu in Ω,

[p0098-b0040 | equation | low] u' =g on I.

[p0098-b0041 | ordinary-paragraph | high] By eliminating p', we get an equivalent second order elliptic problem in u*:

[p0098-b0042 | equation | low] -v4u - (1/8)grad div u = f in Ω,

[p0098-b0043 | equation | low] (5.26)

[p0098-b0044 | equation | low] u' =g on Ω.

## PDF 99 / printed 85



[p0099-b0004 | ordinary-paragraph | medium] pair of functions (u*, p)e H'(Q)7 × L?(Ω) solution of the equations (5.25). More-

[p0099-b0005 | ordinary-paragraph | medium] over, we get the estimate:

[p0099-b0006 | equation | low] (5.27)

[p0099-b0007 | ordinary-paragraph | low] Ilu - ull1,2 + Ilp - pllo,2 ≤ C(llfll-1, + Ilgll1/2,r),

[p0099-b0008 | ordinary-paragraph | medium] where the constant C is independent of e, f and g.

[p0099-b0009 | proof | medium] Proof. Like in Theorem 5.1, we easily obtain the existence and uniqueness of the

[p0099-b0010 | ordinary-paragraph | medium] solution pair (u', p°) of Problem (5.25). Next, considering that the difference u* - u

[p0099-b0011 | ordinary-paragraph | medium] vanishes on I, the argument of Theorem 4.3 immediately gives:

[p0099-b0012 | equation | low] Ilu -- ull1,o + ll p - pllo,o ≤ C&llpllo,αs

[p0099-b0013 | ordinary-paragraph | medium] with a constant C, that is independent of ε. Hence (5.27) follows from Remark

[p0099-b0014 | ordinary-paragraph | medium] 5.3.

[p0099-b0015 | ordinary-paragraph | medium] 口

[p0099-b0016 | ordinary-paragraph | medium] Similarly, we can also apply Theorem 4.4. We obtain that the problems

[p0099-b0017 | equation | low] -v4u, + grad pn = 0 in Ω,

[p0099-b0018 | equation | low] (5.28)

[p0099-b0019 | equation | low] divun = --Pn-1 in Ω,

[p0099-b0020 | equation | low] un =0 on I,

[p0099-b0021 | ordinary-paragraph | medium] starting with po = p, uniquely define by induction a sequence (u, Pn) in H(Q) x

[p0099-b0022 | ordinary-paragraph | medium] L2(Ω). Furthermore, we get for all M > 1 and ε small enough

[p0099-b0023 | ordinary-paragraph | medium] M

[p0099-b0024 | ordinary-paragraph | medium] M

[p0099-b0025 | equation | low] u-u- ∑e"un 

[p0099-b0026 | equation | low] ∑e"pn

[p0099-b0027 | ordinary-paragraph | medium] p-p-

[p0099-b0028 | ordinary-paragraph | low] +

[p0099-b0029 | equation | low] (5.29)

[p0099-b0030 | equation | low] n=1

[p0099-b0031 | equation | low] n=1

[p0099-b0032 | equation | low] 10.2

[p0099-b0033 | ordinary-paragraph | low] 1,0

[p0099-b0034 | equation | low] ≤ CmeM+1(l/fll -1,2 + Ilg1l1/2,r),

[p0099-b0035 | ordinary-paragraph | medium] where Cm is a constant independent of e, f and g.

[p0099-b0036 | remark | medium] Remark 5.4. If we choose

[p0099-b0037 | ordinary-paragraph | medium] N

[p0099-b0038 | equation | low] a(u, v) = 2v ∑

[p0099-b0039 | ordinary-paragraph | medium] D;(u)D;(v) dx,

[p0099-b0040 | equation | low] i,j=1 JΩ

[p0099-b0041 | ordinary-paragraph | medium] we obtain a different regularized problem:

[p0099-b0042 | ordinary-paragraph | low]  aDy(u)  ap

[p0099-b0043 | equation | low] =f inΩ, 1≤i≤ N,

[p0099-b0044 | ordinary-paragraph | medium] 2v

[p0099-b0045 | ordinary-paragraph | low] +

[p0099-b0046 | ordinary-paragraph | low] 0xj

[p0099-b0047 | ordinary-paragraph | low] ax;

[p0099-b0048 | equation | low] p = -(1/e)divu in Ω,

[p0099-b0049 | equation | low] u' =g on I.

[p0099-b0050 | ordinary-paragraph | medium] By eliminating p', we get the penalized problem

[p0099-b0051 | equation | low] -v4u - (v + 1/e)grad div u = f in Ω,

[p0099-b0052 | equation | low] u'=g on I.

## PDF 100 / printed 86



[p0100-b0004 | ordinary-paragraph | high] namely:

[p0100-b0005 | ordinary-paragraph | high] N

[p0100-b0006 | equation | low] ∑ II D,(v)l16,2 + IIdiv vll6,2

[p0100-b0007 | equation | low] (5.30)

[p0100-b0008 | equation | low] i,j=1

[p0100-b0009 | equation | low] αo > 0.

[p0100-b0010 | ordinary-paragraph | medium] Vve H(Q),

[p0100-b0011 | equation | low] ≥αolvli,2

[p0100-b0012 | ordinary-paragraph | high] But Remark 5.1 establishes that

[p0100-b0013 | ordinary-paragraph | high] N

[p0100-b0014 | equation | low] {<中(nA!p)peB>+ <Φnp>}(z/)- =(Φ)q(n)a)

[p0100-b0015 | equation | low] i.j=1

[p0100-b0016 | equation | low] = (1/2) {(grad u, grad Φ) + (div u, div Φ)}

[p0100-b0017 | ordinary-paragraph | medium] for all ue H1(Q), for all Φe O(Q). Hence

[p0100-b0018 | ordinary-paragraph | high] N

[p0100-b0019 | equation | low] (5.31)

[p0100-b0020 | equation | low] IIDy(v)Il6,o = v(Ivli,2 + 1/ divvll6,2).

[p0100-b0021 | ordinary-paragraph | high] 2

[p0100-b0022 | equation | low] i,j=1

[p0100-b0023 | ordinary-paragraph | high] Therefore the analogue of Theorem 5.3 holds in that case.

[p0100-b0024 | remark | high] Remark 5.5. The inequality (5.31) is also related to the classical Korn's Inequalit y:

[p0100-b0025 | ordinary-paragraph | high] N

[p0100-b0026 | equation | low] Vve H'(Ω),  x > 0.

[p0100-b0027 | equation | low] ∑ IID,(v)16.o + 11v1l6,o ≥α, llvl1i.2

[p0100-b0028 | equation | low] (5.31)

[p0100-b0029 | equation | low] i,j=1

[p0100-b0030 | ordinary-paragraph | high] For the sake of completeness, here is a concise proof of (5.31') given by Duvaut

[p0100-b0031 | ordinary-paragraph | high] & Lions [26] in the case of a bounded, Lipschitz-continuous open subset of R?.

[p0100-b0032 | ordinary-paragraph | high] Observe that formally the following identity holds:

[p0100-b0033 | ordinary-paragraph | low] 02v;

[p0100-b0034 | ordinary-paragraph | low] d(Du(v) ， 0(D;(v))

[p0100-b0035 | ordinary-paragraph | low] 0(Dk(v))

[p0100-b0036 | equation | low] I ≤i,j, k≤ N.

[p0100-b0037 | ordinary-paragraph | low] 十

[p0100-b0038 | ordinary-paragraph | low] xx0.x0

[p0100-b0039 | ordinary-paragraph | low] xe

[p0100-b0040 | ordinary-paragraph | low] x0

[p0100-b0041 | ordinary-paragraph | low] 0xi

[p0100-b0042 | ordinary-paragraph | high] Hence for v in H'(Q) we have

[p0100-b0043 | ordinary-paragraph | low] N

[p0100-b0044 | equation | low] II grad(@v;/0x,) -1.o ≤ C ∑ Ilgrad(D,(v)ll-1.2

[p0100-b0045 | equation | low] i,j=1

[p0100-b0046 | ordinary-paragraph | high] N

[p0100-b0047 | equation | low] ≤ C2 ∑ IID,(v)llo,s.

[p0100-b0048 | equation | low] i.j=1

[p0100-b0049 | ordinary-paragraph | high] Therefore, applying Theorem 2.2 to grad v; yields immediately (5.31).

[p0100-b0050 | ordinary-paragraph | high] Now, let us turn to the gradient methods to solve Problem (5.12). Again, we

[p0100-b0051 | ordinary-paragraph | high] take

[p0100-b0052 | equation | low] c(p,q) = (p, q),

[p0100-b0053 | ordinary-paragraph | high] so that

[p0100-b0054 | equation | low] a,(u, v) = v(grad u, grad v) + r(div u, div v)

[p0100-b0055 | ordinary-paragraph | high] which is clearly elliptic on H(Q)*. Thus, defining u,(q) by:

## PDF 101 / printed 87



[p0101-b0005 | equation | low] u,(q) =g on I,

[p0101-b0006 | ordinary-paragraph | medium] we find in view of (5.23):

[p0101-b0007 | equation | low] a,(Du, · μ,v) = (div v, μ)

[p0101-b0008 | ordinary-paragraph | medium] Wve H(Q),

[p0101-b0009 | equation | low] Du,'μ =O on F,

[p0101-b0010 | equation | low] DK,(q) = div u,(q),

[p0101-b0011 | equation | low] D² K,· μ = div(Du, · μ).

[p0101-b0012 | ordinary-paragraph | medium] Hence the simple gradient algorithm with optimal parameter reads as follows:

[p0101-b0013 | ordinary-paragraph | medium] 1°) Given p°e L?(Ω), solve the non-homogeneous elliptic boundary value

[p0101-b0014 | ordinary-paragraph | medium] problem:

[p0101-b0015 | equation | low] -(v4 + rgrad div)u° = f - grad p° in Ω,

[p0101-b0016 | equation | low] u° =g on I.

[p0101-b0017 | ordinary-paragraph | medium] 2°) For m ≥ 0, knowing (u", pm) in Hl(Q) × L2(Ω) with umlr = g, solve the

[p0101-b0018 | ordinary-paragraph | medium] homogeneous problem:

[p0101-b0019 | equation | low] -(v4 + r grad div)zm = grad div um  in Ω,

[p0101-b0020 | equation | low] z" =0 on I;

[p0101-b0021 | ordinary-paragraph | medium] then compute pm e R and the next pair (um+1, pm+1)e H′(Q) x L?(Ω) by:

[p0101-b0022 | equation | low] pm = - I/ div um Il?,2/(div zm, div um),

[p0101-b0023 | equation | low] pm+1 = pm -- pmdivum,

[p0101-b0024 | equation | low] um+1 = um + pmzm.

[p0101-b0025 | ordinary-paragraph | medium] It can be readily checked that the statement of Theorem 4.6 holds, namely the

[p0101-b0026 | ordinary-paragraph | medium] above scheme is always convergent. This is still true when p is not the optimal

[p0101-b0027 | ordinary-paragraph | medium] parameter, provided that

[p0101-b0028 | equation | low] 0 < infpm ≤ sup pm < 2αr.

[p0101-b0029 | ordinary-paragraph | medium] m

[p0101-b0030 | ordinary-paragraph | medium] m

[p0101-b0031 | ordinary-paragraph | medium] A simple calculation shows that

[p0101-b0032 | equation | low] a, ≤r + v/N.

[p0101-b0033 | ordinary-paragraph | medium] The conjugate-gradient algorithm has the same starting procedure n?°1 while

[p0101-b0034 | ordinary-paragraph | medium] step n°2 is replaced by:

[p0101-b0035 | ordinary-paragraph | medium] 2°) For m ≥ 0, knowing (um, pm) in H1(Ω) × L(Ω) with umlr = g, compute

[p0101-b0036 | ordinary-paragraph | medium] om e R and wm e L?(Ω) by:

[p0101-b0037 | equation | low] gm =1ldiv um/0.2/ div um-1 1.2,

[p0101-b0038 | equation | low] only if m ≥ 1,

[p0101-b0039 | equation | low] @m = divum + om@m-1

[p0101-b0040 | equation | low] ①° = div u° otherwise,

## PDF 102 / printed 88



[p0102-b0003 | equation | low] —(vd + rgraddiv)z” = gradw” in Q,

[p0102-b0004 | equation | low] { Zz = 09<onlly,

[p0102-b0005 | ordinary-paragraph | high] and compute pe R and the next pair (u"*?, p™*')e H'(Q)* x L6(Q) by:

[p0102-b0006 | ordinary-paragraph | high] n _ _ _(divu" 3,0

[p0102-b0007 | equation | low] (div z™, divu”)’

[p0102-b0008 | equation | low] ins = De = Oe

[p0102-b0009 | equation | low] u”™*t = u” An. (Degas

[p0102-b0010 | ordinary-paragraph | high] Here again, Corollary 4.6 guarantees that the conjugate-gradient algorithm is

[p0102-b0011 | ordinary-paragraph | high] convergent.

[p0102-b0012 | ordinary-paragraph | high] We end this section with a theorem due to Cattabriga [18] concerning the

[p0102-b0013 | ordinary-paragraph | high] existence and regularity of the solution of the Stokes problem (5.12) in more

[p0102-b0014 | ordinary-paragraph | high] general Sobolev spaces when the boundary J is sufficiently smooth.

[p0102-b0015 | theorem | high] Theorem 5.4. In addition to the hypotheses of Theorem 5.1, suppose that the

[p0102-b0016 | ordinary-paragraph | high] boundary T is of class @™*@:"™*), fe W™"(Q)® and geW™*?—U"r(L)® for some

[p0102-b0017 | ordinary-paragraph | high] integerm > —1and some realr with1 <r < oo. Then, Problem (5.12) has a unique

[p0102-b0018 | ordinary-paragraph | high] solution (u, p)e W"**"(Q)" x W™*!"(Q) with Jo pdx = 0 and there exists a con-

[p0102-b0019 | ordinary-paragraph | high] stant C independent of f and g such that

[p0102-b0020 | ordinary-paragraph | high] (02) IU ||m +2,7,2 oe ll P\m-+1.r,2 < C(||fll mer. oF lS llne+2—1/r.r.0):

[p0102-b0021 | remark | high] Remark 5.6. In the case of a polyhedral domain Q, the regularity properties of

[p0102-b0022 | ordinary-paragraph | high] the solution of Problem (5.12) are clearly weaker. In particular, when N = 2 and

[p0102-b0023 | ordinary-paragraph | high] Q is a convex polygon, the conclusions of the theorem are still valid for m < 0

[p0102-b0024 | ordinary-paragraph | high] and 1 <r < 2 (cf. Grisvard [43]).

[p0102-b0025 | subsection | high] 5.2. The Stream Function Formulation of the Dirichlet Problem in Two

[p0102-b0026 | ordinary-paragraph | high] Dimensions

[p0102-b0027 | ordinary-paragraph | high] Let us again denote by /;, 0 <i < p, the components of the boundary I like in

[p0102-b0028 | figure | high] Figure 2. Now, instead of (5.11), we assume the stronger condition

[p0102-b0029 | ordinary-paragraph | high] (5.33) | g-nds=0, O<i<p.

[p0102-b0030 | ordinary-paragraph | high] T;

[p0102-b0031 | ordinary-paragraph | high] Then, according to Theorems 3.1 and 3.4, the velocity field u given by Theorem

[p0102-b0032 | ordinary-paragraph | high] 5.1 may be expressed as the curl of a stream function w (N = 2) or a vector

[p0102-b0033 | ordinary-paragraph | high] potential y(N = 3). Weare going to show that this stream function or this vector

[p0102-b0034 | ordinary-paragraph | high] potential can be characterized as the solution of a biharmonic problem in Q.

[p0102-b0035 | ordinary-paragraph | high] We begin with the case N = 2. Then, the stream function w is unique up to

[p0102-b0036 | ordinary-paragraph | high] an additive constant. But, as y € H7(Q) s @°(Q), w can be uniquely determined

[p0102-b0037 | ordinary-paragraph | high] by fixing its value in one point of Q. At first, we set (x9) = 0, where x, is an

## PDF 103 / printed 89



[p0103-b0003 | ordinary-paragraph | high] which satisfies

[p0103-b0004 | ordinary-paragraph | high] (5.34) dyjet=g-n onl, (xo) =0.

[p0103-b0005 | ordinary-paragraph | high] Since 0¢/0t = g-non J, it follows that

[p0103-b0006 | ordinary-paragraph | high] NM OM 1%.

[p0103-b0007 | equation | low] y=

[p0103-b0008 | equation | low] eC ee OM se lem) <p.

[p0103-b0009 | ordinary-paragraph | high] where the constants c; are fixed but unknown.

[p0103-b0010 | theorem | high] Theorem 5.5. Let N = 2 and let the hypotheses of Theorem 5.1 be satisfied together

[p0103-b0011 | ordinary-paragraph | high] with (5.33). Then, the associated stream function of u may be characterized as the

[p0103-b0012 | ordinary-paragraph | high] unique function € H?(Q) solution of the equations

[p0103-b0013 | ordinary-paragraph | high] (5.35) v(Aw,4¢) = <f,curlg> Vode (ef. (3.11)),

[p0103-b0014 | ordinary-paragraph | high] 5.36) Vive onl.o W==X yet, Onl. pls iD,p

[p0103-b0015 | equation | low] Ow/on = —g-t onT,

[p0103-b0016 | ordinary-paragraph | high] where x is chosen according to (5.34).

[p0103-b0017 | proof | high] Proof. We have already shown that the velocity field u is the unique solution of

[p0103-b0018 | ordinary-paragraph | high] (5.17). Now, the function u satisfies the conditions

[p0103-b0019 | equation | low] divi— 0) in?) .u—< 2 ond

[p0103-b0020 | ordinary-paragraph | high] if and only if u= curl y where the stream function wy € H?(Q) satisfies the bound-

[p0103-b0021 | ordinary-paragraph | high] ary conditions (5.36). Besides that, according to Corollary 3.2, ve V if and only

[p0103-b0022 | ordinary-paragraph | high] if v = curl ¢ with ge Y. Thus, the theorem will be proved if we show that

[p0103-b0023 | ordinary-paragraph | high] 637) (gradu, gradv) = (4y,4¢) Vv=curld, g¢eY.

[p0103-b0024 | ordinary-paragraph | high] Here, we use the identities stated at the beginning of Section 2.3. First, we have

[p0103-b0025 | ordinary-paragraph | high] (Aw, 4¢) = (curl(curl ~), curl(curl ¢)) = (curl u, curl y).

[p0103-b0026 | ordinary-paragraph | high] Next, we take vin VY = {ve YQ)’; divy = 0} and recall that according to Cor-

[p0103-b0027 | ordinary-paragraph | high] ollary 2.5, V is dense in V. In the sense of distributions, we have:

[p0103-b0028 | equation | low] (curl u, curl vy) = ¢curl(curl u), v>

[p0103-b0029 | equation | low] =<—Au,v> because divu=0O,

[p0103-b0030 | equation | low] = (grad u, grad y).

[p0103-b0031 | ordinary-paragraph | high] Thus the density of Y in V yields (5.37). O

[p0103-b0032 | ordinary-paragraph | high] It remains to interpret Problem (5.35) (5.36). By applying (formally) Green’s

[p0103-b0033 | ordinary-paragraph | high] formula, we can easily show that w is the only solution of the boundary value

## PDF 104 / printed 90



[p0104-b0003 | ordinary-paragraph | high] pay onl), Wee 7 ond; “Vip,

[p0104-b0004 | equation | low] Ow/=o —ng- t onl,

[p0104-b0005 | equation | low] | (vo(AW)/on —f-t)ds=0, 1<i <p.

[p0104-b0006 | ordinary-paragraph | high] Fi;

[p0104-b0007 | ordinary-paragraph | high] Note that this last condition makes sense if fe H(curl; Q).

[p0104-b0008 | subsection | high] 5.3. The Three-Dimensional Case

[p0104-b0009 | ordinary-paragraph | high] Now consider the case N = 3. To simplify the discussion, we first examine the

[p0104-b0010 | ordinary-paragraph | high] case of a homogeneous boundary condition g = 0. We know from Section 3.3

[p0104-b0011 | ordinary-paragraph | high] that the velocity field u can be expressed as:

[p0104-b0012 | equation | low] u=curly with divyw=0 inQ.

[p0104-b0013 | ordinary-paragraph | high] When Q is simply-connected, the vector potential y is uniquely determined by

[p0104-b0014 | ordinary-paragraph | high] either:

[p0104-b0015 | ordinary-paragraph | high] (5.38) wen=0 onl

[p0104-b0016 | ordinary-paragraph | high] or

[p0104-b0017 | ordinary-paragraph | high] (5.39) wxn=0 onl “and |,w enas=0 Orsi ap.

[p0104-b0018 | ordinary-paragraph | high] I

[p0104-b0019 | ordinary-paragraph | high] As u vanishes on J’, we can add the boundary condition:

[p0104-b0020 | ordinary-paragraph | high] (5.40) culy=0 onl

[p0104-b0021 | ordinary-paragraph | high] but observe that this condition reduces to

[p0104-b0022 | ordinary-paragraph | high] (5.40') (curly) x n=0 onl

[p0104-b0023 | ordinary-paragraph | high] when y satisfies the first of (5.39) (cf. Remark 2.5). As far as the regularity of y

[p0104-b0024 | ordinary-paragraph | high] is concerned, all we want is that w satisfy a biharmonic problem. Thus, it seems

[p0104-b0025 | ordinary-paragraph | high] reasonable to ask that yw belong to L?(Q)°. In view of the identity

[p0104-b0026 | ordinary-paragraph | high] (5.41) —A®@ = curl curl0 — grad(div 8)

[p0104-b0027 | ordinary-paragraph | high] and the fact that cuyre Hl'(Q) °* we see that this amounts to ask that divwe

[p0104-b0028 | ordinary-paragraph | high] H'(Q). Of course, this is always the case when yw is divergence-free, but in practice

[p0104-b0029 | ordinary-paragraph | high] a divergence-free condition is unattractive and we are going to relax it entirely.

[p0104-b0030 | ordinary-paragraph | high] At this stage, it is important to point out that the vector potential y has no

[p0104-b0031 | ordinary-paragraph | high] straightforward characterization on a multiply-connected domain Q. For this

[p0104-b0032 | ordinary-paragraph | high] reason, we shall only discuss briefly this last situation and restrict ourselves

[p0104-b0033 | ordinary-paragraph | high] mainly to simply-connected regions.

[p0104-b0034 | ordinary-paragraph | high] Let us begin with vector potentials that satisfy (5.39). In the light of the above

[p0104-b0035 | ordinary-paragraph | high] considerations, we introduce the space

## PDF 105 / printed 91



[p0105-b0003 | equation | low] <Φ∈ L²(Ω)3; div Φe H'(Ω), curlΦe H(Ω)3, Φ x nl r = 0,

[p0105-b0004 | equation | low] Φ·nds = 0,0 ≤i≤p

[p0105-b0005 | ordinary-paragraph | medium] JF:

[p0105-b0006 | ordinary-paragraph | high] normed by

[p0105-b0007 | equation | low] IΦll = {Il+1l6,2 + I/divΦll,o + Ilcurl Φ1l1,2}1/2.

[p0105-b0008 | ordinary-paragraph | high] Note that the functions of Y are not divergence-free but satisfy fo div Φ dx = 0.

[p0105-b0009 | ordinary-paragraph | high] Now, let u be the solution of Problem (5.12) with g = 0. As mentioned above,

[p0105-b0010 | ordinary-paragraph | high] when Q is simply-connected, u has a unique divergence-free vector potential v

[p0105-b0011 | ordinary-paragraph | high] in Y:

[p0105-b0012 | equation | low] -v4(curl w) + grad p = f in H-1(Ω)3,

[p0105-b0013 | equation | low] (5.42)

[p0105-b0014 | equation | low] divw =O inΩ,  weY.

[p0105-b0015 | ordinary-paragraph | high] As div(curl y) = 0, (5.42) reduces to:

[p0105-b0016 | equation | low] v curl curl(curl w) + grad p = f.

[p0105-b0017 | ordinary-paragraph | high] Let us multiply both sides of this equation with curlΦ for Φ in Y. Then

[p0105-b0018 | ordinary-paragraph | high] (curl curl(curl y), curl Φ> = (curl(curl y), curl(curl Φ))

[p0105-b0019 | ordinary-paragraph | high] since curlΦ e H(Q)3. Thus it suffices to show that

[p0105-b0020 | equation | low] (5.43)

[p0105-b0021 | equation | low] (curl curl y, grad div Φ) = 0

[p0105-b0022 | ordinary-paragraph | high] in order to obtain that

[p0105-b0023 | equation | low] -<4(curl y), curl Φ> = (4, 4Φ)

[p0105-b0024 | ordinary-paragraph | low] Vpe Y.

[p0105-b0025 | ordinary-paragraph | high] But (5.43) holds as soon as curl ye Hd(Q)3. Hence we have established that q

[p0105-b0026 | ordinary-paragraph | high] is a solution of the biharmonic problem:

[p0105-b0027 | ordinary-paragraph | low] imy1 yons M u M pu!y

[p0105-b0028 | equation | low] (5.44)

[p0105-b0029 | ordinary-paragraph | low] 中A

[p0105-b0030 | equation | low] v(4, 4Φ) = <f, curlΦ>

[p0105-b0031 | ordinary-paragraph | high] Conversely, it is easy to prove that (5.44) has at most one solution. Indeed, if

[p0105-b0032 | ordinary-paragraph | high] ye Y satisfies 4y = 0 then curly = 0 in Ω, for curl y is the solution of the

[p0105-b0033 | ordinary-paragraph | high] Dirichlet problem:

[p0105-b0034 | equation | low] 4(curl w) = 0 in Ω,  curl wlr = 0.

[p0105-b0035 | ordinary-paragraph | high] In turn, this implies that grad(div y) = 0. Hence div w = 0, since ∫o div w dx = 0.

[p0105-b0036 | ordinary-paragraph | high] Therefore w = 0 (cf. Remark 3.9). Thus we have proved the following result:

[p0105-b0037 | lemma | high] Lemma 5.1. When Q is simply-connected and satisfies the hypotheses of Theorem

[p0105-b0038 | ordinary-paragraph | high] 5.1, the biharmonic problem (5.44) has a unique solution y. Furthermore div y = 0

[p0105-b0039 | ordinary-paragraph | high] and curl y is the unique solution of the Stokes problem (5.12) with g = 0.

## PDF 106 / printed 92



[p0106-b0003 | ordinary-paragraph | high] if Q is simply-connected. However, it is worth mentioning that Problem (5.44) is

[p0106-b0004 | ordinary-paragraph | high] well-posed even when Q is multiply-connected. In fact, we can easily prove the

[p0106-b0005 | ordinary-paragraph | high] following equivalence of norms.

[p0106-b0006 | lemma | high] Lemma 5.2. In addition to the hypotheses of Theorem 5.1, assume that either I’ is

[p0106-b0007 | ordinary-paragraph | high] €'! or that Q is simply-connected. Then the mapping y > ||A W||9,q is a norm on

[p0106-b0008 | ordinary-paragraph | high] VY equivalent to ||\ \.

[p0106-b0009 | proof | high] Proof. First, observe that ||y || is equivalent on ¥ to:

[p0106-b0010 | ordinary-paragraph | high] {Iwlla.ot Ildivwil7.o + leuwirt ol}' ?

[p0106-b0011 | ordinary-paragraph | high] by virtue of Theorem 1.1. Next, remark that (5.41) is simply the orthogonal

[p0106-b0012 | ordinary-paragraph | high] decomposition of the vector 40. This orthogonality yields:

[p0106-b0013 | equation | low] | Ay [3,0 = lleurlcurl y||2,0 + [div wi3,0.

[p0106-b0014 | ordinary-paragraph | high] But since curl y € H4(Q)°, we infer from Remark 2.7 that

[p0106-b0015 | equation | low] lcurl y|, 9 = |/curlcyu|\ro l0 .

[p0106-b0016 | ordinary-paragraph | high] Besides that, the fact that {o div y dx = 0 implies that:

[p0106-b0017 | equation | low] div WIl,0 = IdivVl;,0.

[p0106-b0018 | ordinary-paragraph | high] Indeed, a straightforward application of Theorem 2.1,3°) yields:

[p0106-b0019 | ordinary-paragraph | high] 2\ 1/2

[p0106-b0020 | ordinary-paragraph | high] Iolo (Ioe+ |v dx ) Vue H*(Q).

[p0106-b0021 | ordinary-paragraph | high] Q

[p0106-b0022 | ordinary-paragraph | high] Hence it remains to establish that

[p0106-b0023 | ordinary-paragraph | high] (5.45) IWllo.a < C{lldivwllo.o + leurly|loa}"? Vywe¥.

[p0106-b0024 | ordinary-paragraph | high] When & is simply-connected, this is proved by Lemma 3.4. Indeed, even if J’h as

[p0106-b0025 | ordinary-paragraph | high] several components, its argument shows that:

[p0106-b0026 | ordinary-paragraph | high] IWllo.g<Clleurly|iog VweP with divy =0.

[p0106-b0027 | ordinary-paragraph | high] And if divw #4 0, we can always obtain a divergence-free function in ¥ by

[p0106-b0028 | ordinary-paragraph | high] considering the difference y — w where we Hj(Q)? satisfies (cf. Corollary 2.4):

[p0106-b0029 | equation | low] divw=divy, |wi,o<Clldivwlloo.

[p0106-b0030 | ordinary-paragraph | high] When J is @'*', (5.45) is an easy consequence of Theorems 3.7, 2.1 and

[p0106-b0031 | remark | high] Remark 3.9. Oo

[p0106-b0032 | remark | high] Remark 5.8. It can also be proved (cf. Dominguez [24]) that when Q is multiply-

[p0106-b0033 | ordinary-paragraph | high] connected, the solution of Problem (5.44) is not the potential of the original

[p0106-b0034 | ordinary-paragraph | high] Stokes problem.

## PDF 107 / printed 93



[p0107-b0004 | ordinary-paragraph | high] has the following interpretation:

[p0107-b0005 | equation | low] v4*y=curlf in H~?(Q)°,

[p0107-b0006 | equation | low] divw=0 inQ,

[p0107-b0007 | equation | low] (5.46)

[p0107-b0008 | equation | low] (curly) x nj-=0, wy x njp=0,

[p0107-b0009 | equation | low] | wends=0, O<i<p.

[p0107-b0010 | ordinary-paragraph | high] T;

[p0107-b0011 | ordinary-paragraph | high] A very similar analysis can be applied to vector potentials that satisfy the

[p0107-b0012 | ordinary-paragraph | high] boundary condition (5.38). Here we choose the space:

[p0107-b0013 | equation | low] ¥, = {be L*(Q)*; dive H'(Q), cur€ Hlj( Q) *, o-n|- = 0}

[p0107-b0014 | ordinary-paragraph | high] equipped with the same norm as ¥. Then we have the analogues of Lemmas 5.1

[p0107-b0015 | ordinary-paragraph | high] and 5.2. More precisely, we can first prove an equivalence of norms:

[p0107-b0016 | lemma | high] Lemma 5.3. When Q is like in Lemma 5.1, the mapping y > ||A W|lo,q is a norm

[p0107-b0017 | ordinary-paragraph | high] on ¥, equivalent to |||].

[p0107-b0018 | ordinary-paragraph | high] Owing to Lemma 5.3, the biharmonic problem:

[p0107-b0019 | ordinary-paragraph | high] Find y in ¥, such that

[p0107-b0020 | ordinary-paragraph | high] (5.47) v(4y,4o) = <f,curld> VoeY,,

[p0107-b0021 | ordinary-paragraph | high] has a unique solution yw in ¥,,. It is easy to check that w is the vector potential

[p0107-b0022 | ordinary-paragraph | high] of u and hence divy = 0.

[p0107-b0023 | lemma | high] Lemma 5.4. Assume Q is like in Lemma 5.1. The biharmonic problem (5.47) has a

[p0107-b0024 | ordinary-paragraph | high] unique solution y in , and divy = 0, curly = u where u is the solution of the

[p0107-b0025 | ordinary-paragraph | high] homogeneous Stokes problem (5.12).

[p0107-b0026 | remark | high] Remark 5.10. Problem (5.47) has the following interpretation:

[p0107-b0027 | ordinary-paragraph | high] vA*w—curlf in ~(Q)*,

[p0107-b0028 | ordinary-paragraph | high] (5.48) divw=0 inQ,

[p0107-b0029 | equation | low] curly|;=90, w-en|p=0.

[p0107-b0030 | ordinary-paragraph | high] Finally, let us turn to the non-homogeneous Stokes problem. On the one

[p0107-b0031 | ordinary-paragraph | high] hand, we must assume that the boundary value g satisfies:

[p0107-b0032 | ordinary-paragraph | high] (5.49) | g:nds=0, O<i<p,

[p0107-b0033 | ordinary-paragraph | high] I

## PDF 108 / printed 94



[p0108-b0003 | ordinary-paragraph | high] the boundary condition (5.39) because it implies (curl y)-n|- = 0. However, it is

[p0108-b0004 | ordinary-paragraph | high] possible to prescribe condition (5.38). Thus a reasonable choice for the space of

[p0108-b0005 | ordinary-paragraph | high] vector potentials is:

[p0108-b0006 | equation | low] WY, = {pe L?(Q); divde H'(Q), curlge H*(Q)*, o- np = 0}.

[p0108-b0007 | ordinary-paragraph | high] Likewise, let us take Y, as space of test functions. Then consider the biharmonic

[p0108-b0008 | ordinary-paragraph | high] problem:

[p0108-b0009 | equation | low] Find y in ¥, with curyl| - = g such that

[p0108-b0010 | ordinary-paragraph | high] (5.50) v(4y, 46) = <f,curld> VoeY¥,.

[p0108-b0011 | ordinary-paragraph | high] It is easy to check that this problem has a unique solution but the relation

[p0108-b0012 | ordinary-paragraph | high] between y and u is not altogether trivial because (5.43) no longer holds for all

[p0108-b0013 | ordinary-paragraph | high] in Y,. However, observe that y and the divergence-free potential yo of u in

[p0108-b0014 | ordinary-paragraph | high] Y (curl y,. = u, div yo = 0, Wo-n|- = 0) both satisfy:

[p0108-b0015 | ordinary-paragraph | high] v(curl cury,l cu rlcurl) = <f,curlo> Voe¥, with divd =0.

[p0108-b0016 | ordinary-paragraph | high] Thus, setting

[p0108-b0017 | equation | low] w = curl(w — wo) eEV,

[p0108-b0018 | ordinary-paragraph | high] we derive curl w = 0 and hence w = 0. Therefore y is a vector potential of u, but

[p0108-b0019 | ordinary-paragraph | high] it is not necessarily divergence-free.

[p0108-b0020 | theorem | high] Theorem 5.6. Let Q be like in Lemma 5.1 and let g satisfy (5.49). The biharmonic

[p0108-b0021 | ordinary-paragraph | high] problem (5.50) has a unique selution wy in Y, and curly is the unique solution of

[p0108-b0022 | ordinary-paragraph | high] the non-homogeneous Stokes problem (5.12).

[p0108-b0023 | remark | high] Remark 5.11. The divergence of y is the solution 4 of the Neumann’s problem:

[p0108-b0024 | equation | low] AA= 010) \L ax= 0;

[p0108-b0025 | ordinary-paragraph | high] Q

[p0108-b0026 | equation | low] 0A/on = (curlu)-n on TJ.

[p0108-b0027 | ordinary-paragraph | high] Therefore div y = 0 iff (curlu):n|- = 0.

[p0108-b0028 | remark | high] Remark 5.12. If we want a biharmonic problem whose solution is yy, we must

[p0108-b0029 | ordinary-paragraph | high] include the constraint (div p)| = 0 in the spaces ¥, and ¥,.

[p0108-b0030 | remark | high] Remark 5.13. It is also possible to prescribe the condition (curl w)|;= g, by

[p0108-b0031 | ordinary-paragraph | high] setting on the one hand

[p0108-b0032 | equation | low] (curx ln=ygx)n _ onT,

[p0108-b0033 | ordinary-paragraph | high] and on the other hand
