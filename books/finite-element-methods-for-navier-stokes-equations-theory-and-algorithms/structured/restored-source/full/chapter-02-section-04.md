# Restored-source review candidate: chapter-02-section-04



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 187 / printed 173



[p0187-b0002 | ordinary-paragraph | high] Numerical results confirm this theoretical analysis but it appears most often

[p0187-b0003 | ordinary-paragraph | high] that it is the entire pressure p, that converges towards p—not the component

[p0187-b0004 | ordinary-paragraph | high] Pp, alone—. This renders the filtering of the pressure component p} seldom

[p0187-b0005 | ordinary-paragraph | high] necessary. There are cases, though, where p} does diverge; the reader can refer

[p0187-b0006 | ordinary-paragraph | high] to Boland & Nicolaides [12] for a specific example. Besides that, the reader will

[p0187-b0007 | ordinary-paragraph | high] find in Malkus & Olsen [55] other examples of currently used finite element

[p0187-b0008 | ordinary-paragraph | high] spaces which do not satisfy a uniform inf-sup condition.

[p0187-b0009 | ordinary-paragraph | high] From a practical point of view, Problem (3.36) can be solved by the penalty

[p0187-b0010 | ordinary-paragraph | high] method of Section 1.3 (cf. (1.52)). Numerical results can be found for example in

[p0187-b0011 | ordinary-paragraph | high] Carey & Krishnan [16]. But it is also possible to decouple directly the velocity

[p0187-b0012 | ordinary-paragraph | high] from the pressure by using a basis of “divergence-free” velocities, i.e. a basis of

[p0187-b0013 | ordinary-paragraph | high] V,. Following Stephens et al [76] we introduce the vector field v,¢ X,, that

[p0187-b0014 | ordinary-paragraph | high] takes the values (1, — 1), (1, 1), (— 1, 1), (— 1, —1) at the four vertices of x like in

[p0187-b0015 | figure | high] Figure 17 and (0,0) at all other nodes of 7,; then we define the set

[p0187-b0016 | equation | low] S = {y,; for all interior elements x of 7,}.

[p0187-b0017 | ordinary-paragraph | high] By inspection, we can easily ascertain that each v,¢S belongs to V, and that

[p0187-b0018 | ordinary-paragraph | high] all these functions are linearly independent. In addition, a simple dimension

[p0187-b0019 | ordinary-paragraph | high] argument yields:

[p0187-b0020 | equation | low] card(S) = dim(X,) — dim(.4@,) = dim(V,,).

[p0187-b0021 | ordinary-paragraph | high] Hence S is a convenient basis of V,. The reader will find numerical results with

[p0187-b0022 | ordinary-paragraph | high] this basis in the above reference.

[p0187-b0023 | section | high] §4. Continuous Approximation of the Pressure

[p0187-b0024 | ordinary-paragraph | high] So far, we have used approximate pressures that were (generally) discontinuous

[p0187-b0025 | ordinary-paragraph | high] across interelement boundaries. But from the engineering point of view, contin-

[p0187-b0026 | ordinary-paragraph | high] uous pressures are more natural because the pressures encountered in practice

[p0187-b0027 | ordinary-paragraph | high] are usually continuous functions. The fact is that numerical analysts found Stokes

[p0187-b0028 | ordinary-paragraph | high] solvers with ¢° pressures more difficult to analyze than those with L” pressures.

[p0187-b0029 | ordinary-paragraph | high] This difficulty accounts for the relatively meager literature on the theory of

[p0187-b0030 | ordinary-paragraph | high] important schemes of the “Hood-Taylor” type.

[p0187-b0031 | ordinary-paragraph | high] The first rigorous error analysis of the very popular Hood & Taylor [44]

[p0187-b0032 | ordinary-paragraph | high] scheme is due to Bercovier & Pironneau [7]. Later on this analysis was cleverly

[p0187-b0033 | ordinary-paragraph | high] simplified by Verfiirth [83]; but now the approach of Section 1.4 permits to insert

[p0187-b0034 | ordinary-paragraph | high] directly the Hood-Taylor method into the framework of § 1.

[p0187-b0035 | ordinary-paragraph | high] Apart from the Hood-Taylor and closely related schemes, this paragraph

[p0187-b0036 | ordinary-paragraph | high] studies an interesting variant introduced by Glowinski & Pironneau [38] which

[p0187-b0037 | ordinary-paragraph | high] approximates the Stokes problem by a sequence of discrete Dirichlet problems

[p0187-b0038 | ordinary-paragraph | high] for —Z.

## PDF 188 / printed 174



[p0188-b0003 | ordinary-paragraph | high] With minor modifications, the setting of the problem is that of Section 1.3. We

[p0188-b0004 | ordinary-paragraph | high] take for Q a bounded, plane polygon and we assume that the Stokes system

[p0188-b0005 | equation | low] ‘-—-vAu + gradp =f

[p0188-b0006 | ordinary-paragraph | high] in Q,

[p0188-b0007 | ordinary-paragraph | high] (4.1) divu = 0

[p0188-b0008 | equation | low] n=O om/l

[p0188-b0009 | ordinary-paragraph | high] is such that:

[p0188-b0010 | ordinary-paragraph | high] p belongs to H'(Q).

[p0188-b0011 | ordinary-paragraph | high] Following Arnold et al [2], we construct a triangulation 7, of Q and we

[p0188-b0012 | ordinary-paragraph | high] approximate the velocity on each element x by a polynomial of

[p0188-b0013 | ordinary-paragraph | high] (4.2) P (xk) = [P, @ span{A,A,A3}]?

[p0188-b0014 | ordinary-paragraph | high] and the pressure by a polynomial of P,. Thus we choose the following finite

[p0188-b0015 | ordinary-paragraph | high] element spaces:

[p0188-b0016 | ordinary-paragraph | high] (4.3) X, = {ve @°(Q)’; v|,EA,(k) Vee FJ, v/p = 0},

[p0188-b0017 | ordinary-paragraph | high] (4.4) Q, = {ge @°(Q); q|.EP, VKET,}, M, = Q,1L3(Q).

[p0188-b0018 | ordinary-paragraph | high] The degrees of freedom are the simplest ones, namely the values of the velocity

[p0188-b0019 | ordinary-paragraph | high] at the vertices and center of k and the values of the pressure at the vertices of k.

[p0188-b0020 | ordinary-paragraph | high] As usual, the space V, is defined by:

[p0188-b0021 | equation | low] V, = {v,€X); (divv,,q,) =0 Vq,€Q,}

[p0188-b0022 | ordinary-paragraph | high] and the approximate problem, called Problem (Q,) reads:

[p0188-b0023 | ordinary-paragraph | high] Find a pair (u,, p;,) in X, x M,, satisfying:

[p0188-b0024 | equation | low] sso —(p,, div. ¥;,) = <i.v, > VV, esx,

[p0188-b0025 | equation | low] (4.5)

[p0188-b0026 | equation | low] (divu,,q,)=0 Vq,€Q,,

[p0188-b0027 | ordinary-paragraph | high] where the bilinear form a(., .) is unchanged:

[p0188-b0028 | equation | low] a(u, Vv) == Ww(( D;;(u), Dj,(v))

[p0188-b0029 | ordinary-paragraph | high] ij

[p0188-b0030 | ordinary-paragraph | high] or

[p0188-b0031 | equation | low] a(u, v) = v(grad u, grad vy).

[p0188-b0032 | ordinary-paragraph | high] Note that because the space Q, is contained in H1(Q), the bilinear form b(., .)

[p0188-b0033 | ordinary-paragraph | high] can be written equivalently as:

[p0188-b0034 | equation | low] b(V,,49,) = —(divv,,4,) = (grad n> Vn) Vv,E Xp, Vdn€ Qh:

## PDF 189 / printed 175



[p0189-b0002 | ordinary-paragraph | high] The approximation properties of X,, and Q, are well known. For instance, if

[p0189-b0003 | ordinary-paragraph | high] the triangulation 7, is regular, the interpolation operator r, defined by:

[p0189-b0004 | equation | low] r,V(a) = v(a) on all nodes a of J,

[p0189-b0005 | ordinary-paragraph | high] (4.6) r,V(a,.) = v(a,) onthe center a, ofk, VKeZ,,

[p0189-b0006 | ordinary-paragraph | high] r,VEP,(K) oneach k,

[p0189-b0007 | ordinary-paragraph | high] satisfies

[p0189-b0008 | ordinary-paragraph | high] r,€ £(LH?(QHo) (@N)] *; Xi)

[p0189-b0009 | ordinary-paragraph | high] and

[p0189-b0010 | ordinary-paragraph | high] (4.7) IV —ThVllm.@ <Ch?-"|vlp9 VWreH?(QY, m=Oorl.

[p0189-b0011 | ordinary-paragraph | high] Indeed, r, is preserved by affine transformations on each x and leaves invariant

[p0189-b0012 | ordinary-paragraph | high] the polynomials of P?.

[p0189-b0013 | ordinary-paragraph | high] Likewise, the local regularization operator R, on P, defined by (A.53), (A.54)

[p0189-b0014 | ordinary-paragraph | high] satisfies R, €Y (L?(Q); Q,,) and

[p0189-b0015 | ordinary-paragraph | high] (4.8) la —Ridllma<Ch "gle VqeH'(Q) m=Oorl,

[p0189-b0016 | ordinary-paragraph | high] provided of course that 7, is regular.

[p0189-b0017 | ordinary-paragraph | high] Therefore the Hypotheses H1 and H2 are fulfilled and it remains to verify

[p0189-b0018 | ordinary-paragraph | high] H3, namely the inf-sup condition:

[p0189-b0019 | equation | low] (qd; div V,)

[p0189-b0020 | ordinary-paragraph | high] (4.9) sup —"——* > B* lidullo.g Vane My.

[p0189-b0021 | ordinary-paragraph | high] Yne Xn IVali,2

[p0189-b0022 | ordinary-paragraph | high] This is achieved by the next lemma.

[p0189-b0023 | lemma | high] Lemma 4.1. If the triangulation 7, is regular, the pair of spaces (X;,,M,) defined

[p0189-b0024 | ordinary-paragraph | high] by (4.3) (4.4) satisfies (4.9) with a constant B* > 0 independent of h.

[p0189-b0025 | proof | high] Proof. Let us exhibit the operator 2, of Lemma 1.1. Take an arbitrary q, in M,.

[p0189-b0026 | ordinary-paragraph | high] Since q,, € L2(Q) there exists v in Hj(Q)* such that

[p0189-b0027 | ordinary-paragraph | high] (4.10) divv=q_, |V l1,2 < Ci lld alloa-

[p0189-b0028 | ordinary-paragraph | high] Therefore, since M, < H'(Q) we want to construct a function 7,v in X,, that

[p0189-b0029 | ordinary-paragraph | high] satisfies

[p0189-b0030 | equation | low] » |m av-wrad nds = s [vada Vu€, M, .

[p0189-b0031 | ordinary-paragraph | high] KeTZ,, KeT;,

[p0189-b0032 | ordinary-paragraph | high] As grad p,€P ? on each x, this equality induces us to define z,v in X,, such that:

[p0189-b0033 | ordinary-paragraph | high] (4.11) 1,Vv(a) =(R,v)(a) Wnode a of 7,

[p0189-b0034 | ordinary-paragraph | high] and

## PDF 190 / printed 176



[p0190-b0003 | ordinary-paragraph | high] where R, denotes the now familiar local regularization operator on Pee

[p0190-b0004 | ordinary-paragraph | high] Clearly, (4.11) and (4.12) determine uniquely z,v in X, and 7,€ L(H}(Q);

[p0190-b0005 | ordinary-paragraph | high] X,,). Moreover

[p0190-b0006 | equation | low] \d iv(z,V —v)u,dx =O Vu,eM,.

[p0190-b0007 | ordinary-paragraph | high] Q

[p0190-b0008 | ordinary-paragraph | high] Finally an argument similar to that of Lemma 2.2 shows that

[p0190-b0009 | equation | low] |7nV11, GS< CyIV|1, Q

[p0190-b0010 | ordinary-paragraph | high] provided 7, is regular. This proves the lemma. O

[p0190-b0011 | ordinary-paragraph | high] These results are summarized in the following theorem.

[p0190-b0012 | theorem | high] Theorem 4.1. Let Q be a bounded plane polygon and let the solution (u, p) of the

[p0190-b0013 | ordinary-paragraph | high] Stokes system (4.1) satisfy:

[p0190-b0014 | ordinary-paragraph | high] nelH7Q)OAHA(Oy. pel OL. @).

[p0190-b0015 | ordinary-paragraph | high] If the triangulation 7, is regular, the solution (u,, p;,) of Problem (4.5) with the

[p0190-b0016 | ordinary-paragraph | high] spaces X,, and M,, defined by (4.3) and (4.4) respectively satisfies the error bound:

[p0190-b0017 | ordinary-paragraph | high] (4.13) Ju — uglie + IP — Pallooe < Crh{lulz.e + |Plia}-

[p0190-b0018 | ordinary-paragraph | high] In addition, when Q is convex, we have the L?-estimate:

[p0190-b0019 | ordinary-paragraph | high] (4.14) lu —uylloe < Ch? {lulz.0 + IP|1,a}-

[p0190-b0020 | ordinary-paragraph | high] This “mini” finite element method can easily be generalized to schemes of

[p0190-b0021 | ordinary-paragraph | high] arbitrary order. The details can be found in Arnold et al [2].

[p0190-b0022 | subsection | high] 4.2. The “‘Hood-Taylor’”’ Finite Element Method

[p0190-b0023 | ordinary-paragraph | high] The results of the preceding section can be improved by taking a more accurate

[p0190-b0024 | ordinary-paragraph | high] approximation oft he velocity. Following Hood & Taylor [44], we keep the same

[p0190-b0025 | ordinary-paragraph | high] space Q, and we replace X,, by:

[p0190-b0026 | ordinary-paragraph | high] (4.15) X, = {ve S(Q)?; v|,.€P? Vee J, vjp = 0},

[p0190-b0027 | ordinary-paragraph | high] with the function values at the principal lattice of order 2 (cf. (A.19)) as degrees

[p0190-b0028 | ordinary-paragraph | high] of freedom. Therefore the standard interpolation operator I, satisfies:

[p0190-b0029 | ordinary-paragraph | high] I,€ 2(LH*(Q)N Ho(2)]’; X,),

[p0190-b0030 | ordinary-paragraph | high] (4.16) |lv—J,VIImo< Chi "|vi,g YWeH*(Q), k=20r3, m=Oorl.

## PDF 191 / printed 177



[p0191-b0003 | ordinary-paragraph | medium] The remainder of this section is devoted to the proof of the inf-sup condition.

[p0191-b0004 | ordinary-paragraph | medium] We propose to establish it first locally and then extend it by Theorem 1.12. The

[p0191-b0005 | ordinary-paragraph | medium] reader can also refer to Verfirth [83] for a direct global proof.

[p0191-b0006 | ordinary-paragraph | medium] Here, the difficulty in a local argument lies in the choice of an adequate

[p0191-b0007 | ordinary-paragraph | medium] partition of Ω. We propose to group together all the elements which share a

[p0191-b0008 | ordinary-paragraph | medium] common vertex like in Figure 18. More precisely, we make the following assump-

[p0191-b0009 | ordinary-paragraph | medium] tion on the triangulation h:

[p0191-b0010 | ordinary-paragraph | medium] J, has a set of interior nodes {a,}=1 such that {Ω,}-1 with

[p0191-b0011 | ordinary-paragraph | medium] Uk

[p0191-b0012 | equation | low] (4.17)

[p0191-b0013 | equation | low] ='

[p0191-b0014 | ordinary-paragraph | medium] k has vertex ar

[p0191-b0015 | ordinary-paragraph | medium]  is a partition of Ω.

[p0191-b0016 | ordinary-paragraph | medium] K

[p0191-b0017 | ordinary-paragraph | low] X

[p0191-b0018 | ordinary-paragraph | low] R,

[p0191-b0019 | equation | low] Ko=K8

[p0191-b0020 | ordinary-paragraph | low] α2

[p0191-b0021 | ordinary-paragraph | medium] α

[p0191-b0022 | ordinary-paragraph | medium] α3

[p0191-b0023 | ordinary-paragraph | medium] α

[p0191-b0024 | ordinary-paragraph | medium] α6K

[p0191-b0025 | ordinary-paragraph | low] α5

[p0191-b0026 | ordinary-paragraph | medium] K

[p0191-b0027 | ordinary-paragraph | medium] K6

[p0191-b0028 | ordinary-paragraph | medium] K6

[p0191-b0029 | ordinary-paragraph | low] a,

[p0191-b0030 | equation | low] J=8

[p0191-b0031 | figure | medium] Figure 18

[p0191-b0032 | ordinary-paragraph | medium] If this assumption holds, each element k of , belongs to exactly one macro-

[p0191-b0033 | ordinary-paragraph | medium] element Q,. In addition, the fact that all the nodes a, are inside Q implies that

[p0191-b0034 | ordinary-paragraph | medium] each element k has exactly one side on the boundary of its macro-element Q, and

[p0191-b0035 | ordinary-paragraph | medium] at most one side on the boundary I of Q.

[p0191-b0036 | ordinary-paragraph | medium] In practice, it is not difficult to construct a triangulation that satisfies (4.17).

[p0191-b0037 | ordinary-paragraph | medium] The usual procedure is to start with a coarse grid and then progressively refine

[p0191-b0038 | ordinary-paragraph | medium] it by adding interior nodes.

## PDF 192 / printed 178



[p0192-b0003 | ordinary-paragraph | high] (4.18) Qn(2,) = {dlo,3 4 Qn},

[p0192-b0004 | equation | low] M,(@,) = Q,(2,) 1 Lo(Q,).

[p0192-b0005 | ordinary-paragraph | high] Let us prove that the pair (X,(Q,), M,(Q,)) satisfies a local inf-sup condition.

[p0192-b0006 | theorem | high] Theorem 4.2. Suppose that 7, is a regular triangulation of Q and that J, satisfies

[p0192-b0007 | ordinary-paragraph | high] (4.17). Then there exists a constant A* > 0, independent of h and r, such that:

[p0192-b0008 | ordinary-paragraph | high] (4.19) sup (| acivyds) Ivo, > A*\d\lo.a, VaeM,(2,).

[p0192-b0009 | ordinary-paragraph | high] ve X,(Q,) Q

[p0192-b0010 | proof | high] Proof. Let J be the number of elements x in Q, and let us number them with an

[p0192-b0011 | ordinary-paragraph | high] index i ranging from 0 to J such that x; is adjacent to x;_, and k,,, and Ky = Ky

[p0192-b0012 | ordinary-paragraph | high] (like in Figure 18): 0

[p0192-b0013 | ordinary-paragraph | high] a

[p0192-b0014 | ordinary-paragraph | high] We denote by x; the side shared by x; and x;,,, by a; the midpoint of x; and by

[p0192-b0015 | ordinary-paragraph | high] a, the vertex common to all the x; in Q,.

[p0192-b0016 | ordinary-paragraph | high] Like in Section A.3, we associate with Q, the reference set:

[p0192-b0017 | ordinary-paragraph | high] J)

[p0192-b0018 | equation | low] Q=\|)k; (cf. Figure 18)

[p0192-b0019 | ordinary-paragraph | high] through the continuous, piecewise affine function F. defined by:

[p0192-b0020 | equation | low] F(R;) — K;, F(X) — B;X =P b; VXeE R;.

[p0192-b0021 | ordinary-paragraph | high] Since the triangulation is regular, the number J is bounded above by a fixed

[p0192-b0022 | ordinary-paragraph | high] constant I independent of r and as a consequence there are at most J different

[p0192-b0023 | ordinary-paragraph | high] reference sets 2. This means that all geometrical constants related to Q and K;

[p0192-b0024 | ordinary-paragraph | high] can be bounded independently of h and r.

[p0192-b0025 | ordinary-paragraph | high] Now let q,, be an arbitrary element of Q,(Q,) and let v,, be a function in X,(Q,)

[p0192-b0026 | ordinary-paragraph | high] that satisfies v,(a,) = 0. Since y, vanishes on 0Q, and q, belongs to H!(Q,) we have:

[p0192-b0027 | ordinary-paragraph | high] J

[p0192-b0028 | equation | low] | divv,q,dx = —) | Vv, grad q,, dx.

[p0192-b0029 | ordinary-paragraph | high] Q, RAP,

[p0192-b0030 | ordinary-paragraph | high] Observe that each component v of v, is a polynomial of P, on x; that vanishes

[p0192-b0031 | ordinary-paragraph | high] at the vertices of «;. Hence the following quadrature formula holds:

[p0192-b0032 | equation | low] | vdx = meas(x;)(1/3) {v(a;) + v(a;_,)}-

[p0192-b0033 | ordinary-paragraph | high] i

[p0192-b0034 | ordinary-paragraph | high] As grad q,, is constant on each x; (say grad Gnlx, = &i), this formula yields:

[p0192-b0035 | ordinary-paragraph | high] J

[p0192-b0036 | ordinary-paragraph | high] (4.20) [ div v,q,4x = —(1/3) Zem eas(x;) {¥(o;) +

[p0192-b0037 | equation | low] v(a-1)>}g i.

## PDF 193 / printed 179



[p0193-b0002 | ordinary-paragraph | high] Next, remark that 0q,,/0t is continuous at interelements boundaries. This

[p0193-b0003 | ordinary-paragraph | high] suggests to choose

[p0193-b0004 | equation | low] v(a;) = —(g;°t,)t; = —(8i41 t,t,

[p0193-b0005 | ordinary-paragraph | high] where t; is the tangent vector to x; with length ||«;|| and (say) pointing outside

[p0193-b0006 | ordinary-paragraph | high] Q,. With this choice we obtain

[p0193-b0007 | equation | low] IPd iv v,q, 4x= (1/3)1 sm eas(«;) {(g;°t;)? + (g;° t;-1)"}

[p0193-b0008 | ordinary-paragraph | high] But according to (A.9), g-t is preserved by affine transformations. Thus, with

[p0193-b0009 | ordinary-paragraph | high] obvious notations we can write:

[p0193-b0010 | equation | low] | div v,q, 4x= (1/3) y meas(x;) {(8;"t )? + (8° ti-1)?}.

[p0193-b0011 | ordinary-paragraph | high] r

[p0193-b0012 | ordinary-paragraph | high] Clearly, each set of vectors te, ; t;} is a basis on the reference space. Therefore

[p0193-b0013 | ordinary-paragraph | high] the mapping g > {(g-t,;_,)* + (g:t,)7}1” is equivalent to the Euclidean norm on

[p0193-b0014 | ordinary-paragraph | high] the reference space. Hence, in view of

[p0193-b0015 | equation | low] 47,2, = meas(k;) ||8 7,

[p0193-b0016 | ordinary-paragraph | high] there exists a constant C, > 0 such that:

[p0193-b0017 | ordinary-paragraph | high] df

[p0193-b0018 | ordinary-paragraph | high] (4.21) | divv,q,dx > C, ¥, meas(x;,)|417,«,

[p0193-b0019 | ordinary-paragraph | high] Oy. ial

[p0193-b0020 | ordinary-paragraph | high] Next, on the one hand the definition of v, yields:

[p0193-b0021 | equation | low] IIvilld.c; < Co meas({|x|v o;s)) II?+ Ivo) I7}

[p0193-b0022 | equation | low] (4.22)

[p0193-b0023 | equation | low] < C; meas(xK;) UPAR.

[p0193-b0024 | ordinary-paragraph | high] And on the other hand, the argument of Lemma A.6 gives:

[p0193-b0025 | equation | low] alan: < C,[|| Br" | IlV alor, ]*

[p0193-b0026 | equation | low] (4.23)

[p0193-b0027 | equation | low] < Cs meas(K;) [0,141.4]?

[p0193-b0028 | ordinary-paragraph | high] by virtue of (A.2) and (4.22). Hence it stems from (4.21), (4.23) and the regularity

[p0193-b0029 | ordinary-paragraph | high] of 7, that

[p0193-b0030 | ordinary-paragraph | high] J 1/2

[p0193-b0031 | ordinary-paragraph | high] (4.24) | div v,q,dx 2 Coll/ova.a.4 3 meas(e) dif :

[p0193-b0032 | equation | low] Q, i=1

[p0193-b0033 | ordinary-paragraph | high] It remains to show that, on a regular triangulation,

[p0193-b0034 | ordinary-paragraph | high] Ap 1/2 VaeH*(2,)N Lo).

[p0193-b0035 | equation | low] > meas(e lal >Clidilo.e,

[p0193-b0036 | equation | low] i=]

[p0193-b0037 | ordinary-paragraph | high] The corresponding proof is a simple variant of that of Lemma 2.5. To begin with,

## PDF 194 / printed 180



[p0194-b0004 | equation | low] q = q -- (1/meas(Ω))

[p0194-b0005 | ordinary-paragraph | medium] q dx.

[p0194-b0006 | ordinary-paragraph | low] 02

[p0194-b0007 | ordinary-paragraph | medium] Then q and q differ by a constant and we have:

[p0194-b0008 | equation | low] llallo.2, = inf Ilq + c llo,2, ≤ Ilallo,2,-

[p0194-b0009 | ordinary-paragraph | medium] ceR

[p0194-b0010 | ordinary-paragraph | medium] But

[p0194-b0011 | equation | low] = meas(k)Ilal,x;

[p0194-b0012 | ordinary-paragraph | low] 14 l16,2, 

[p0194-b0013 | equation | low] =

[p0194-b0014 | equation | low] ≤ C, sup (h2)lali,o  since @e H'(②)N L?(@).

[p0194-b0015 | equation | low] 1≤≤J

[p0194-b0016 | ordinary-paragraph | low] meas(k:)lali,x*

[p0194-b0017 | equation | low] inf (p²:

[p0194-b0018 | equation | low] sup (h2)

[p0194-b0019 | equation | low] 1≤i<J

[p0194-b0020 | equation | low] （1≤K)

[p0194-b0021 | ordinary-paragraph | medium] Hence

[p0194-b0022 | ordinary-paragraph | medium] 1/2

[p0194-b0023 | ordinary-paragraph | low] meas(k;)al,x;(

[p0194-b0024 | equation | low] ≥(C9/o,) llallo,2r,

[p0194-b0025 | equation | low] (4.25)

[p0194-b0026 | ordinary-paragraph | medium] where

[p0194-b0027 | equation | low] inf(μx;).

[p0194-b0028 | equation | low] 0, = sup (hk)

[p0194-b0029 | equation | low] 1≤<J

[p0194-b0030 | equation | low] 1≤i≤J

[p0194-b0031 | ordinary-paragraph | medium] This finishes the proof because the regularity of , implies that (cf. Bernardi [9]):

[p0194-b0032 | equation | low] o, ≤ Co.

[p0194-b0033 | equation | low] (4.26)

[p0194-b0034 | ordinary-paragraph | low] 口

[p0194-b0035 | ordinary-paragraph | medium] Owing to Theorem 1.12, the local inf-sup condition (4.19) yields readily the

[p0194-b0036 | ordinary-paragraph | medium] required global condition.

[p0194-b0037 | corollary | medium] Corollary 4.1. Under the assumptions of Theorem 4.2 the pair of spaces (Xn, Mh)

[p0194-b0038 | ordinary-paragraph | medium] defined by (4.15) (4.4) satisfies the inf-sup condition (4.9) with a constant β* > 0

[p0194-b0039 | ordinary-paragraph | medium] independent of h.

[p0194-b0040 | proof | medium] Proof. Let X, be the finite element space defined by (2.3) and let

[p0194-b0041 | equation | low] M, = {qe L?(Ω); alo, is constant r}.

[p0194-b0042 | ordinary-paragraph | medium] Then on the one hand, X, c X, because the functions of X, are piecewise

[p0194-b0043 | ordinary-paragraph | medium] incomplete polynomials of P2. On the other hand, it follows from Lemma 2.2

[p0194-b0044 | ordinary-paragraph | medium] that the pair (X,, M,) satisfies a uniform inf-sup condition since the functions of

[p0194-b0045 | ordinary-paragraph | medium] M, are a particular case of piecewise constants. Hence the result follows from

[p0194-b0046 | ordinary-paragraph | medium] Theorems 1.12 and 4.2.

[p0194-b0047 | ordinary-paragraph | low] 口

## PDF 195 / printed 181



[p0195-b0002 | remark | high] Remark 4.1. Most technical details in the proof of Theorem 4.2 have already been

[p0195-b0003 | ordinary-paragraph | high] used by Bercovier & Pironneau [7] in establishing a weak form of the inf-sup

[p0195-b0004 | ordinary-paragraph | high] condition (4.9). Albeit simple, the above proof is long because it deals with a

[p0195-b0005 | ordinary-paragraph | high] reference region composed of several reference triangles instead of a single one.

[p0195-b0006 | ordinary-paragraph | high] The crucial point in the proof is the particular choice of v at the midpoint of the

[p0195-b0007 | ordinary-paragraph | high] interior segments. Apart from that, the major steps are essentially the same as

[p0195-b0008 | ordinary-paragraph | high] those used in proving Theorem 2.2.

[p0195-b0009 | ordinary-paragraph | high] With Theorem 4.2 and its corollary we readily derive the major result of this

[p0195-b0010 | ordinary-paragraph | high] section.

[p0195-b0011 | theorem | high] Theorem 4.3. Let Q be a bounded, plane polygon and let the solution (u, p) of the

[p0195-b0012 | ordinary-paragraph | high] Stokes system (4.1) satisfy

[p0195-b0013 | equation | low] ue[H*(Q)N HQ), pe H(Q)NL2(Q), k= 1o0r2.

[p0195-b0014 | ordinary-paragraph | high] If the triangulation Z,, is regular and like in (4.17), the solution (u,, p,) of Problem

[p0195-b0015 | ordinary-paragraph | high] (4.5) with spaces X,, and M,, defined by (4.15) (4.4) satisfies the estimate:

[p0195-b0016 | ordinary-paragraph | high] (4.27) |u—uyIlP i— Poal+le <Cih*{luh+s [1P.h0ot k= Lord.

[p0195-b0017 | ordinary-paragraph | high] When Q is convex, this can be refined:

[p0195-b0018 | ordinary-paragraph | high] (4.28) ju —u,lloa<O h ule O ar IP|x, a}:

[p0195-b0019 | ordinary-paragraph | high] Furthermore, if 7, is uniformly regular (but Q not necessarily convex) we also

[p0195-b0020 | ordinary-paragraph | high] have:

[p0195-b0021 | ordinary-paragraph | high] (4.29) p= Pleo = Gh laleeco + 'IPleo)

[p0195-b0022 | remark | high] Remark 4.2. In order to establish (4.29) we can apply Corollary 4.1 and switch

[p0195-b0023 | ordinary-paragraph | high] from ||p_ — allo.e to [Pr — Gal1,q by Corollary A.3 (this is where the uniformity

[p0195-b0024 | ordinary-paragraph | high] of 7, steps in).

[p0195-b0025 | remark | high] Remark 4.3. Obviously, Remark 2.6 is also valid here.

[p0195-b0026 | ordinary-paragraph | high] We finish this section with a quick study of a popular variant of the Hood-

[p0195-b0027 | ordinary-paragraph | high] Taylor method. Again, let 7, be a regular triangulation of Q that satisfies (4.17)

[p0195-b0028 | ordinary-paragraph | high] divide each of its triangles « into four equal triangles & by joining the

[p0195-b0029 | ordinary-paragraph | high] and let us

[p0195-b0030 | ordinary-paragraph | high] midpoints of the sides (cf. Figure 19). For the pressure, we retain the spaces Q,

[p0195-b0031 | ordinary-paragraph | high] and M, defined by (4.4) and we replace the velocity space X,, by:

[p0195-b0032 | equation | low] = {ve @°(Q)’; ve P; on each subtriangle & ofk VKe 7,

[p0195-b0033 | equation | low] (4.30)

[p0195-b0034 | equation | low] vir = 0}.

[p0195-b0035 | ordinary-paragraph | high] The approximation properties of Q, and M, are unchanged while the approxi-

[p0195-b0036 | ordinary-paragraph | high] mation properties of X,, correspond to polynomials of P,, i.e. we have:

## PDF 196 / printed 182



[p0196-b0002 | figure | high] Figure 19. Triangle K divided into four subtriangles

[p0196-b0003 | ordinary-paragraph | high] where I, €f ((H?(Q)N H3(Q)]’; X,,) is the standard interpolator at the vertices

[p0196-b0004 | ordinary-paragraph | high] of each subtriangle kK of 7,.

[p0196-b0005 | ordinary-paragraph | high] The proof of the inf-sup condition is almost exactly like above. We take the

[p0196-b0006 | ordinary-paragraph | high] same partition (4.17) and observe that the space X,(Q,) with X,, defined by (4.30)

[p0196-b0007 | ordinary-paragraph | high] involves exactly the same degrees of freedom as if the space X, were defined

[p0196-b0008 | ordinary-paragraph | high] by (4.15). Just the degree of the polynomials varies and this affects only the

[p0196-b0009 | ordinary-paragraph | high] factor 1/3 in the quadrature formula (4.20) and the reference constants C in sub-

[p0196-b0010 | ordinary-paragraph | high] sequent formulas. Hence the statement of Theorem 4.2 carries over here without

[p0196-b0011 | ordinary-paragraph | high] modification.

[p0196-b0012 | ordinary-paragraph | high] To switch from the local inf-sup condition to the global inf-sup condition,

[p0196-b0013 | ordinary-paragraph | high] we choose the same space M, but we take

[p0196-b0014 | ordinary-paragraph | high] xe — Ge

[p0196-b0015 | ordinary-paragraph | high] It is easy to prove that the pair of spaces (X,,M,) satisfies a uniform inf-sup

[p0196-b0016 | ordinary-paragraph | high] condition. This is in fact part of a more general result.

[p0196-b0017 | lemma | high] Lemma 4.2. If the triangulation 7, is regular, the spaces X,, and

[p0196-b0018 | ordinary-paragraph | high] {qe L(Q); q is constant onk VKeZ,}

[p0196-b0019 | ordinary-paragraph | high] satisfy a uniform inf-sup condition.

[p0196-b0020 | ordinary-paragraph | high] We skip the proof since it is included in the argument of Lemma 3.8: it suffices

[p0196-b0021 | ordinary-paragraph | high] to adapt the definition of the restriction operator z to the present case.

[p0196-b0022 | ordinary-paragraph | high] Summarizing, we have the analogue of Theorem 4.3.

[p0196-b0023 | theorem | high] Theorem 4.4. Let Q and 7, satisfy the hypotheses of Theorem 4.3 and suppose the

[p0196-b0024 | ordinary-paragraph | high] solution (u, p) of (4.1) belongs to H*(Q)? x [H*(Q)N L2(Q)]. Then the solution

[p0196-b0025 | ordinary-paragraph | high] (u,, Pr) of Problem (4.5) with X,, and M, defined by (4.30) (4.4) has the error bound:

[p0196-b0026 | ordinary-paragraph | high] (4.32) lu — uylia + IP — Palloa < Cyh{lul,

[p0196-b0027 | ordinary-paragraph | high] 9 + IPli,a}-

[p0196-b0028 | ordinary-paragraph | high] Moreover, when Q is convex we have the L?-estimate:

[p0196-b0029 | ordinary-paragraph | high] (4.33) lu — uy llo.g< Cah? {luo

[p0196-b0030 | ordinary-paragraph | high] + IPli,a}-

## PDF 197 / printed 183



[p0197-b0002 | remark | high] Remark 4.4. Although it is less accurate than the preceding scheme while involv-

[p0197-b0003 | ordinary-paragraph | high] ing the same number of unknowns, this last method is often preferred because it

[p0197-b0004 | ordinary-paragraph | high] leads to better conditioned linear systems.

[p0197-b0005 | subsection | high] 4.3. The “Glowinski-Pironneau” Finite Element Method

[p0197-b0006 | ordinary-paragraph | high] To begin with, let the dimension N be two or three. The numerical scheme

[p0197-b0007 | ordinary-paragraph | high] discussed in this section, introduced by Glowinski & Pironneau [38], is based

[p0197-b0008 | ordinary-paragraph | high] on a Poisson equation for the pressure. By taking the divergence of both sides

[p0197-b0009 | ordinary-paragraph | high] of the equation:

[p0197-b0010 | equation | low] —vAu+ gradp =f

[p0197-b0011 | ordinary-paragraph | high] and taking into account the condition divu = 0, we obtain:

[p0197-b0012 | equation | low] Ape Giv fein <2:

[p0197-b0013 | ordinary-paragraph | high] Hence, if we know the trace p = p|, of p on J, the Stokes equations reduce to

[p0197-b0014 | ordinary-paragraph | high] N + 1 Dirichlet problems for the Laplace operator:

[p0197-b0015 | ordinary-paragraph | high] (4.34) Ap= i v 1. in:2 .5 ap =p» sone,

[p0197-b0016 | ordinary-paragraph | high] (4.35) vAu=gradp—f inQ, u=0 onl.

[p0197-b0017 | ordinary-paragraph | high] In fact, p is the major unknown of the problem. We shall show that p can be in

[p0197-b0018 | ordinary-paragraph | high] turn determined by the constraint divu = 0.

[p0197-b0019 | ordinary-paragraph | high] More precisely, observe that u and p can be split into two components:

[p0197-b0020 | ordinary-paragraph | high] (4.36) u=u°+u(p), p=p° + p(p),

[p0197-b0021 | ordinary-paragraph | high] where p° and wu® are the solutions of the Dirichlet problems:

[p0197-b0022 | ordinary-paragraph | high] (4.37a) Ap =dvi-m®Q. p-=0 ‘on,

[p0197-b0023 | ordinary-paragraph | high] (4.37b) vAu° = gradp?—f inQ, u°=0 on/J,

[p0197-b0024 | ordinary-paragraph | high] and, for each boundary value g, p(g) and u(g) are the solutions of:

[p0197-b0025 | ordinary-paragraph | high] (4.38a) APG) =—Onsto. Op (G)i =a on,

[p0197-b0026 | ordinary-paragraph | high] (4.38b) vAu(g) = gradp(g) inQ, u(g)=0 onl.

[p0197-b0027 | ordinary-paragraph | high] The space G of the boundary functions g is chosen so that the mapping g > p(g)

[p0197-b0028 | ordinary-paragraph | high] defined by (4.38a) is an isomorphism from G onto the space

[p0197-b0029 | equation | low] {qe L?(Q); Aq = O}.

[p0197-b0030 | ordinary-paragraph | high] Then, since the solution u of (4.34) (4.35) must satisfy

[p0197-b0031 | equation | low] A(divu)=0 inQ,

## PDF 198 / printed 184



[p0198-b0003 | ordinary-paragraph | high] or equivalently by

[p0198-b0004 | ordinary-paragraph | high] (4.39) (div u(p), p(g)) = —(divu’,p(g)) VgeG.

[p0198-b0005 | ordinary-paragraph | high] We are going to see below that, for a proper choice of the space G, the equation

[p0198-b0006 | ordinary-paragraph | high] (4.39) defines a unique boundary function p.

[p0198-b0007 | ordinary-paragraph | high] In order to choose G, let us put Problem (4.38a) in variational form. Assuming

[p0198-b0008 | ordinary-paragraph | high] for the moment that the function p(g) is smooth enough, Green’s formula yields:

[p0198-b0009 | ordinary-paragraph | high] (4.40) |p (g)Apdx = |g on/énds = Wue H*(Q)N HG (2).

[p0198-b0010 | ordinary-paragraph | high] Q Vk

[p0198-b0011 | ordinary-paragraph | high] When the boundary I is @'*', we know from Theorem I.1.6 that the mapping

[p0198-b0012 | ordinary-paragraph | high] > Ou/én is continuous from H?(Q)N H3(Q) onto H'7(’). When I is a plane

[p0198-b0013 | ordinary-paragraph | high] polygon, made of segments J; for 1 <j < J, Remark I.1.1 asserts that the map-

[p0198-b0014 | ordinary-paragraph | high] ping uw > (6u/0n,; 1 <j < J) is continuous from H?(Q)N Ho(@) onto [| H*? (75).

[p0198-b0015 | ordinary-paragraph | high] These considerations suggest the following choice for G:

[p0198-b0016 | equation | low] PHL2 CP) =H ot? ail 1 sega

[p0198-b0017 | ordinary-paragraph | high] (441) G=

[p0198-b0018 | ordinary-paragraph | high] |I T wUr)| if [is a two-dimensional polygon

[p0198-b0019 | equation | low] 1<j<J

[p0198-b0020 | ordinary-paragraph | high] equipped with the usual dual norm which, for the sake of simplicity, we denote

[p0198-b0021 | ordinary-paragraph | high] in both cases by ||. ||_-1)2,r. Then, in either case, when g and p(g) are related by

[p0198-b0022 | ordinary-paragraph | high] (4.40) we have:

[p0198-b0023 | ordinary-paragraph | high] 1

[p0198-b0024 | equation | low] I9ll-yar< Cy sup (_—| gom/on is]

[p0198-b0025 | ordinary-paragraph | high] we HQ) NHK@) \IHll2,e Jr ;

[p0198-b0026 | equation | low] < /NC,||p(9)llo.c:

[p0198-b0027 | ordinary-paragraph | high] Conversely, if either [is @'*' or if Q is a convex polygon, it stems from

[p0198-b0028 | remark | high] Remark I.1.2 that for all q in L?(Q), the problem:

[p0198-b0029 | equation | low] Ab=q inQ; =O on

[p0198-b0030 | ordinary-paragraph | high] has a unique solution uw in H?(Q)N H3(Q) and |\L\|,.o< Cy\|q|lo.o. Hence

[p0198-b0031 | ordinary-paragraph | high] Problem (4.40) has a unique solution p(g) and

[p0198-b0032 | ordinary-paragraph | high] 1

[p0198-b0033 | equation | low] IIP(9)llooe < Cy sup (| P(g) Au ix)

[p0198-b0034 | ordinary-paragraph | high] we H2(Q) 1 HA(Q) lH Il2,0 Q

[p0198-b0035 | equation | low] < C319 l-12,r-

[p0198-b0036 | ordinary-paragraph | high] Moreover, using the fact that Y(Q) is dense in the space

[p0198-b0037 | equation | low] L(A; Q) = {qe L7(Q); Age L?(Q)}

[p0198-b0038 | ordinary-paragraph | high] we can readily define the trace mappping y: L(4; 2) > H~"/?(L) and establish the

## PDF 199 / printed 185



[p0199-b0003 | ordinary-paragraph | high] following Green's formula for all pe L(4; Q):

[p0199-b0004 | ordinary-paragraph | medium] ()H U ()HA

[p0199-b0005 | equation | low] (p,μ) =(p, 4μ) -

[p0199-b0006 | ordinary-paragraph | low] (yp)du/onds

[p0199-b0007 | ordinary-paragraph | low] Jr

[p0199-b0008 | ordinary-paragraph | high] Collecting these results, we find that Problems (4.38a) and (4.40) are equivalent,

[p0199-b0009 | ordinary-paragraph | high] have a unique solution p(g) for each g in G and

[p0199-b0010 | equation | low] [1/(/N C,)] Ilg ll -1/2, r ≤ Ilp(g)llo.o ≤ C llgll-1/2.r 

[p0199-b0011 | equation | low] (4.42)

[p0199-b0012 | ordinary-paragraph | low] 'bA

[p0199-b0013 | ordinary-paragraph | high] Next, we write Problem (4.38b) in variational form:

[p0199-b0014 | equation | low] (4.43)

[p0199-b0015 | equation | low] v(grad u(g), grad v) = (p(g), div v) ve H(Ω)v.

[p0199-b0016 | ordinary-paragraph | high] From this and Corollary 1.2.4 we derive immediately that

[p0199-b0017 | equation | low] (C1/v) Il p(g) IlL2(2)/r ≤ /u(g)1,2 ≤ (/N/v)Il p(g)llL2(2)/R

[p0199-b0018 | equation | low] (4.44)

[p0199-b0019 | ordinary-paragraph | high] Thus, combining (4.42) and (4.44) and using the fact that

[p0199-b0020 | equation | low] p(g + c) = p(g) + c

[p0199-b0021 | ordinary-paragraph | high] we obtain

[p0199-b0022 | ordinary-paragraph | high] C4

[p0199-b0023 | ordinary-paragraph | medium] inf Ilg + cll-1/2,r ≤ lu(g)l,α ≤(//N/v)C, inf Ilg + cll -1/2,r

[p0199-b0024 | equation | low] (4.45)

[p0199-b0025 | ordinary-paragraph | medium] vNC, ceR

[p0199-b0026 | ordinary-paragraph | low] ceR

[p0199-b0027 | ordinary-paragraph | high] Finally, by substituting (4.43) into (4.39) we derive:

[p0199-b0028 | equation | low] v(grad u(p), grad u(l)) = - (div u°, p(l))

[p0199-b0029 | ordinary-paragraph | high] VleG.

[p0199-b0030 | ordinary-paragraph | high] In other words, with the notation

[p0199-b0031 | equation | low] (4.46)

[p0199-b0032 | equation | low] a(p, l) = v(grad u(p), grad u(l)),

[p0199-b0033 | ordinary-paragraph | high] Problem (4.39) reads:

[p0199-b0034 | ordinary-paragraph | high] Find p in G/R such that:

[p0199-b0035 | equation | low] a(p,I) = -(divu,p(l)

[p0199-b0036 | equation | low] (4.47)

[p0199-b0037 | ordinary-paragraph | low] Hle G/r.

[p0199-b0038 | ordinary-paragraph | high] Clearly, in view of (4.44) and (4.45) this problem has a unique solution. Note also

[p0199-b0039 | ordinary-paragraph | high] that the bilinear form a(., .) is symmetric.

[p0199-b0040 | ordinary-paragraph | high] The above results are summarized in the following theorem.

[p0199-b0041 | theorem | high] Theorem 4.5. Let N = 2 or 3. Assume that Q is bounded with either a %1.1

[p0199-b0042 | ordinary-paragraph | high] boundary or a polygonal boundary with no reentrant corners. For f given in L?(Q)N,

[p0199-b0043 | ordinary-paragraph | high] the solution (u, p) of the Stokes system (4.1) can be split into:

[p0199-b0044 | equation | low] μ = u° + u(p),  p = p° + p(p),

[p0199-b0045 | ordinary-paragraph | high] where p is the unique solution of Problem (4.47) and the pairs (u°, p°), (u(p), p(p))

## PDF 200 / printed 186



[p0200-b0003 | ordinary-paragraph | high] The Glowinski-Pironneau scheme is a very straightforward approximation of

[p0200-b0004 | ordinary-paragraph | high] Problems (4.37) and (4.38), on a polygonal domain 2, with the Hood-Taylor

[p0200-b0005 | ordinary-paragraph | high] finite element spaces for the velocity and pressure:

[p0200-b0006 | equation | low] X,, defined by (4.15), Q,, defined by (4.4).

[p0200-b0007 | ordinary-paragraph | high] The space G/R is represented by:

[p0200-b0008 | ordinary-paragraph | high] (4.48) (Cr = Jane0 s g,(a)=90 Vnodeaof FN Q, |G .dsi— of

[p0200-b0009 | ordinary-paragraph | high] ia

[p0200-b0010 | ordinary-paragraph | high] Observe that, on the one hand the support of the functions of G, is a neigh-

[p0200-b0011 | ordinary-paragraph | high] borhood of I’. On the other hand, the additive constant of these functions is fixed

[p0200-b0012 | ordinary-paragraph | high] by the condition |;-q,ds = 0. In addition, we introduce the space

[p0200-b0013 | ordinary-paragraph | high] (4.49) &, = 0, HA(Q).

[p0200-b0014 | ordinary-paragraph | high] Note that we have the decomposition:

[p0200-b0015 | equation | low] Jane0 x |q nds = of= , ® G,,.

[p0200-b0016 | ordinary-paragraph | high] Ig

[p0200-b0017 | ordinary-paragraph | high] With these spaces, Problems (4.37) and (4.38) are discretized as follows:

[p0200-b0018 | ordinary-paragraph | high] Find p? € ®, such that:

[p0200-b0019 | ordinary-paragraph | high] (4.50) (grad p;, grad q,) = (f,gradq,) Vq,€®,;

[p0200-b0020 | ordinary-paragraph | high] Find u} € X,, such that:

[p0200-b0021 | equation | low] v(grad u,, gradv,) = —(grad pp,v,) + (fv,) Vv,6X;;

[p0200-b0022 | ordinary-paragraph | high] For g,, given in G,, find p,(g),)€Q,, such that:

[p0200-b0023 | equation | low] (grad p,(g,),gradq,)=90 Vq,€®,,

[p0200-b0024 | ordinary-paragraph | high] (4.51) Pi(Gn) — G, = 9 onl;

[p0200-b0025 | ordinary-paragraph | high] Find u,(g;,€) X; , such that:

[p0200-b0026 | equation | low] v(grad u,(g,,), grad v,) = —(grad p,(gn),Vn) VV, Xp:

[p0200-b0027 | ordinary-paragraph | high] Finally, the boundary function p is discretized by the analogue of (4.47):

[p0200-b0028 | ordinary-paragraph | high] Find p,,€ G,, satisfying:

[p0200-b0029 | ordinary-paragraph | high] (4.52) v(grad u,(p,,), grad u,(/,)) = (up, grad p,(I,)) Vl,€ G,.-

[p0200-b0030 | ordinary-paragraph | high] Then the approximate velocity and pressure calculated by the Glowinski-

[p0200-b0031 | ordinary-paragraph | high] Pironneau scheme are:

[p0200-b0032 | ordinary-paragraph | high] (4.53) u, =U, + U,(P,), Py = pe

[p0200-b0033 | ordinary-paragraph | high] + Pil Pa)»

[p0200-b0034 | ordinary-paragraph | high] where (uj, p;,) is the solution of (4.50), p, is the solution of (4.52) and (u,(p,),

[p0200-b0035 | ordinary-paragraph | high] Pp(P;,)) 1s the solution of (4.51) for this p,,.

## PDF 201 / printed 187



[p0201-b0002 | ordinary-paragraph | high] To stress the parallel with the continuous case, we set

[p0201-b0003 | equation | low] An(Gn> ln) = vigradu,(g,),gradu,(1,)) Von. ln € Gh.

[p0201-b0004 | ordinary-paragraph | high] Clearly, Problem (4.50) has a unique solution, and so does Problem (4.51) for

[p0201-b0005 | ordinary-paragraph | high] a given g,. Moreover, it is easy to check that Problem (4.52) has also a unique

[p0201-b0006 | ordinary-paragraph | high] solution p,. Indeed, if u,(p,) = 0 then

[p0201-b0007 | equation | low] (grad p;,(P),V,) =O Vv,E Xp.

[p0201-b0008 | ordinary-paragraph | high] But the inf-sup condition established by Corollary 4.1 implies that

[p0201-b0009 | equation | low] Pa(P;,) = (1/meas(Q)) (P r Pn) ax,

[p0201-b0010 | ordinary-paragraph | high] i.e. p, is constant in Q. As p,(p,) also satisfies |p ,(p,)ds = 0 we conclude that

[p0201-b0011 | ordinary-paragraph | high] P,(P;,) = 0 and in particular, p, = 0. Therefore we have the following result:

[p0201-b0012 | lemma | high] Lemma 4.3. Let the right-hand side f belong to L?(Q)? where Q is a plane, bounded

[p0201-b0013 | ordinary-paragraph | high] polygon and assume that the triangulation 7, is like in (4.17). Then the Glowinski-

[p0201-b0014 | ordinary-paragraph | high] Pironneau scheme (4.50) ... (4.53) determines a unique pair (u,, p,) with u, in X,, and

[p0201-b0015 | ordinary-paragraph | high] Pn in Qh, IrPn ds = 0.

[p0201-b0016 | ordinary-paragraph | high] Moreover, the pair (u,, p;,,) satisfies:

[p0201-b0017 | ordinary-paragraph | high] (4,54) v(grad u,, grad v,) + (grad p,,v, — grad q,)

[p0201-b0018 | equation | low] =(f,v, —gradq,) V(V,,4,)€X p x Py.

[p0201-b0019 | ordinary-paragraph | high] Note that (4.54) amounts to two independent equations: one for u, and one for

[p0201-b0020 | ordinary-paragraph | high] P,- Vhey are obtained by combining the last equations (resp. the first equations)

[p0201-b0021 | ordinary-paragraph | high] of (4.50) and (4.51).

[p0201-b0022 | ordinary-paragraph | high] It is important to point out that, although the finite element spaces coincide

[p0201-b0023 | ordinary-paragraph | high] with those of the Hood-Taylor method and (4.54) with q,, = 0 is satisfied in both

[p0201-b0024 | ordinary-paragraph | high] cases, the above pair (u,, p;,) is not, in general, the solution of the Hood-Taylor

[p0201-b0025 | ordinary-paragraph | high] algorithm because it does not satisfy the discrete divergence-free constraint:

[p0201-b0026 | equation | low] (u,,gradg,)=90 Vq,E€Q,.-

[p0201-b0027 | ordinary-paragraph | high] Indeed, it follows from (4.51) that we have:

[p0201-b0028 | equation | low] (grad p,(g,),4,) = —v(gradu,(g,), grad u,)

[p0201-b0029 | equation | low] —v(grad u,(g,), grad(uy + u,(,)))

[p0201-b0030 | equation | low] = —(uy, grad p,(g,)) — v(grad u,(g;,), grad uy;)

[p0201-b0031 | ordinary-paragraph | high] by virtue of (4.52). Hence, another application of (4.51) shows that we have:

[p0201-b0032 | equation | low] (grad p,(g,),4,) =9 Von,eG,.

[p0201-b0033 | ordinary-paragraph | high] Unlike the continuous case, this equality does not necessarily carry over to all

## PDF 202 / printed 188



[p0202-b0003 | ordinary-paragraph | high] (4.55) (grad 4, grad q,) = (u,,gradq,) Vq,E®,

[p0202-b0004 | ordinary-paragraph | high] then the sum u, — grad /, does satisfy:

[p0202-b0005 | equation | low] (u, — grad/,,gradq,)=9 Vq,€Q,.

[p0202-b0006 | ordinary-paragraph | high] Indeed, let gq, € Q,, with [-q,ds = O and let g, € G, denote the boundary value of q;:

[p0202-b0007 | equation | low] dalr = Gnlr-

[p0202-b0008 | ordinary-paragraph | high] Then gq, has the orthogonal decomposition (with respect to |.|;,9):

[p0202-b0009 | equation | low] dn = An(Gn) + Ine

[p0202-b0010 | ordinary-paragraph | high] where q,,(g,) is the solution of (4.51) and q? e ®,. We have:

[p0202-b0011 | equation | low] (u,, grad q,) = (u,, grad q,)

[p0202-b0012 | equation | low] = (grad /,,gradq?) by (4.55)

[p0202-b0013 | equation | low] = (grad 4,,gradq,) in view of (4.51).

[p0202-b0014 | ordinary-paragraph | high] We shall see below that 4, is indeed small, so that u, is nearly “divergence-free”.

[p0202-b0015 | ordinary-paragraph | high] In addition, although 4, has only been introduced here for a theoretical purpose,

[p0202-b0016 | ordinary-paragraph | high] it will prove to be useful in practice for solving efficiently (4.52).

[p0202-b0017 | remark | high] Remark 4.5. The triple (u,,, p,,4,) can also be introduced directly as the unique

[p0202-b0018 | ordinary-paragraph | high] solution in X, x (Q,/R) x @, of:

[p0202-b0019 | equation | low] v(grad u,, grad v,) + (grad p,,v, — grad q,,) = (f,v, — grad q,)

[p0202-b0020 | ordinary-paragraph | high] V(VWan >EX , X D,,

[p0202-b0021 | equation | low] (u, — grad /,,gradq,)=90 Yq,€Q,.

[p0202-b0022 | ordinary-paragraph | high] But the advantage of the formulations (4.50)...(4.53) is that it appears as the

[p0202-b0023 | ordinary-paragraph | high] solution of a sequence of decoupled Dirichlet problems for the Laplace operator.

[p0202-b0024 | ordinary-paragraph | high] The error analysis closely resembles that of the corresponding Problem (4.5).

[p0202-b0025 | ordinary-paragraph | high] In particular, its inf-sup condition is precisely (4.9) and therefore, Theorem 4.2

[p0202-b0026 | ordinary-paragraph | high] and its corollary are valid.

[p0202-b0027 | theorem | high] Theorem 4.6. Let Q be a bounded, convex, plane polygon and suppose the right-

[p0202-b0028 | ordinary-paragraph | high] hand side f of the Stokes Problem (4.1) belongs to L?(Q)?. If the solution (u, p) of

[p0202-b0029 | ordinary-paragraph | high] (4.1) has the regularity:

[p0202-b0030 | equation | low] ucH(Q), pe HQ) L2(Q) fork = 1,2

[p0202-b0031 | ordinary-paragraph | high] and if the triangulation J, is uniformly regular and like in (4.17), we have the error

[p0202-b0032 | ordinary-paragraph | high] estimates:

[p0202-b0033 | equation | low] (4.56)

[p0202-b0034 | ordinary-paragraph | high] u — u,lia + IAnli.e eine = Puilo,a < One Olh een ae IP\k.a}

## PDF 203 / printed 189



[p0203-b0003 | equation | low] (4.57)

[p0203-b0004 | equation | low] Ip- Pnl1,α ≤ C2hk-1{1ulk+1,α + Iplk,2},

[p0203-b0005 | equation | low] (4.58)

[p0203-b0006 | equation | low] u - un + grad A,llo,2 ≤ C3hk+1 {lulk+1,2 + Iplk,2},

[p0203-b0007 | ordinary-paragraph | high] where (un, Pn) is the solution of (4.50)...(4.53), An is given by (4.55) and pn is the

[p0203-b0008 | ordinary-paragraph | high] representative of p, in L?(Q).

[p0203-b0009 | proof | high] Proof. We have:

[p0203-b0010 | equation | low] v(grad(u - un),grad vn) + (grad(p - pn),vh - grad an) = 0

[p0203-b0011 | equation | low] (4.59)

[p0203-b0012 | ordinary-paragraph | low] (vh,gn)∈ Xh x Dn,

[p0203-b0013 | ordinary-paragraph | low] "O"bA

[p0203-b0014 | equation | low] (uh - grad Ah, grad qn) = 0

[p0203-b0015 | ordinary-paragraph | high] Let us restrict the pair (vh 9h) to the space:

[p0203-b0016 | equation | low] Bh = {(vh,an)∈Xh x Φh;(Vh - grad qhgrad μn) = O μn∈Qh}.

[p0203-b0017 | ordinary-paragraph | high] Note that (u,, A,)e B,. Then (4.59) reads:

[p0203-b0018 | equation | low] 0 = ("b pei8 - "A (un - d)pe18) + ("A pe.1a ("n - n)peu8)4

[p0203-b0019 | ordinary-paragraph | medium] (vh,qh)∈ Bh,

[p0203-b0020 | ordinary-paragraph | low] ."0uA

[p0203-b0021 | ordinary-paragraph | high] To get rid of grad qh, we choose μ, = Php, the H'-projection of p on M, defined

[p0203-b0022 | ordinary-paragraph | high] by (A.25). Hence

[p0203-b0023 | ordinary-paragraph | low] (Vh,Ih)e Bh.

[p0203-b0024 | equation | low] v(grad(u - un),grad vh) = (div vh, P - Php)

[p0203-b0025 | ordinary-paragraph | high] As (u, ,)e B, this equation readily implies:

[p0203-b0026 | equation | low] [u - ul1.o ≤ 2|u - Wnl1, + (/2/v)lp - Phpllo,2

[p0203-b0027 | ordinary-paragraph | low] V(wh, Ih)e Bh.

[p0203-b0028 | ordinary-paragraph | high] Clearly, we may choose here the pair (w, 0) with w, in V, and since the spaces

[p0203-b0029 | ordinary-paragraph | high] (Xh, M,) satisfy the inf-sup condition (4.9) we can apply (1.16):

[p0203-b0030 | equation | low] inf |u - whli,o ≤(1 + √2/β*) inf |u - vhl1,2.

[p0203-b0031 | ordinary-paragraph | low] WneVn

[p0203-b0032 | ordinary-paragraph | low] VhEXn

[p0203-b0033 | ordinary-paragraph | high] As a consequence,

[p0203-b0034 | ordinary-paragraph | low] [u - ul1.o ≤ 2(1 + √/2/β*) inf ↓u -vnl1,α + (2/v) llp -- Phpllo,2,

[p0203-b0035 | ordinary-paragraph | low] VnE Xh

[p0203-b0036 | ordinary-paragraph | high] and the velocity bound in (4.56) follows from (4.16) and (A.26). Notice that it is

[p0203-b0037 | ordinary-paragraph | high] (A.26) alone which requires the convexity of Q and the uniform regularity of h.

[p0203-b0038 | ordinary-paragraph | high] The bound for A, is obtained from the above inequality and the fact that

[p0203-b0039 | ordinary-paragraph | high] div u = 0:

[p0203-b0040 | equation | low] "0="bA

[p0203-b0041 | equation | low] (grad An, grad qh) = --(u - un, grad qh)

[p0203-b0042 | equation | low] (4.60)

[p0203-b0043 | ordinary-paragraph | high] Therefore

[p0203-b0044 | equation | low] [Ahl1,o ≤ lu -- u, llo,s.

## PDF 204 / printed 190



[p0204-b0004 | ordinary-paragraph | high] Glam):

[p0204-b0005 | equation | low] lp — Drlloo <1 + \/2/B*) inf |p — dallo,o + /B*)|u — Unlio-

[p0204-b0006 | ordinary-paragraph | high] qne My,

[p0204-b0007 | ordinary-paragraph | high] This yields (4.56); in turn a familiar argument gives (4.57).

[p0204-b0008 | ordinary-paragraph | high] Finally we establish an L?-estimate for the velocity. The proof is an easy

[p0204-b0009 | ordinary-paragraph | high] variant of that of Theorem 1.2. As Q is convex, there exists a unique pair (4, 1)

[p0204-b0010 | ordinary-paragraph | high] in [VN H?7(Q)?] x [H1(Q)N LZ(Q)] such that

[p0204-b0011 | equation | low] (g,u — u,) = v(grad , grad(u — u,)) + (grad y,u — u,),

[p0204-b0012 | equation | low] (4.61)

[p0204-b0013 | equation | low] IPll2.0+ [Hl1,0 < Cllgiloa-

[p0204-b0014 | ordinary-paragraph | high] Combining this equality with (4.59) we readily derive:

[p0204-b0015 | equation | low] (g,u —u,) = v(grad( — ,), grad(u — u,)) + (p — Pr» div(b;, — ))

[p0204-b0016 | equation | low] — (H — Gp, div(u — u,)) + (grad 4, grad(u — G,))

[p0204-b0017 | ordinary-paragraph | high] —(g,gradi,) YVo,EX,, Vq,EQh.-

[p0204-b0018 | ordinary-paragraph | high] (Here we use the fact that 4u = divg in Q). Therefore choosing q, = P, we

[p0204-b0019 | ordinary-paragraph | high] obtain:

[p0204-b0020 | ordinary-paragraph | high] (g,u —u, + grad /,,) = v(grad( — @,), grad(u — u,)) + (p — p,, div(, — ))

[p0204-b0021 | equation | low] —(u— P,u,div(u—u,)) Vo,e X;,.

[p0204-b0022 | ordinary-paragraph | high] In view of (4.56) and (4.61) this yields (4.58). O

[p0204-b0023 | remark | high] Remark 4.6. It does not appear possible to find an L? bound like (4.58) for u — u,

[p0204-b0024 | ordinary-paragraph | high] alone. On the contrary, (4.60) implies that

[p0204-b0025 | equation | low] lu —u, + grad A,||5,0 = lu — uy lld.o — |Aali.e

[p0204-b0026 | ordinary-paragraph | high] so that neither u — u, nor A, can be isolated from (4.58). But this is not surprising

[p0204-b0027 | ordinary-paragraph | high] since 4, acts as a correction on the velocity u,.

[p0204-b0028 | ordinary-paragraph | high] The same analysis can be applied when X,, is defined by (4.30) (and M,, is

[p0204-b0029 | ordinary-paragraph | high] unchanged). Because of (4.31), the statement of Theorem 4.6 holds only with

[p0204-b0030 | ordinary-paragraph | high] eve

[p0204-b0031 | subsection | high] 4.4. Implementation of the Glowinski-Pironneau Scheme

[p0204-b0032 | ordinary-paragraph | high] It is not absolutely straightforward to compute the solution of (4.50) (4.51) (4.52)

[p0204-b0033 | ordinary-paragraph | high] because the test function |, does not appear explicitly in the left-hand side of

[p0204-b0034 | ordinary-paragraph | high] (4.52). It is easier to split the computation by calculating the auxiliary function

[p0204-b0035 | ordinary-paragraph | high] A, defined by (4.55), that compensates for the fact that u, does not satisfy the

[p0204-b0036 | ordinary-paragraph | high] discrete divergence-free constraint.

## PDF 205 / printed 191



[p0205-b0003 | ordinary-paragraph | medium] To be specific, following the pattern of the equations (4.50) and (4.51), let us

[p0205-b0004 | ordinary-paragraph | medium] define An(gn) and x by:

[p0205-b0005 | ordinary-paragraph | low]  ∈ Pn,

[p0205-b0006 | ordinary-paragraph | low] VahE Φh,

[p0205-b0007 | equation | low] (grad A, grad qh) = (u, grad qh)

[p0205-b0008 | equation | low] (4.62)

[p0205-b0009 | ordinary-paragraph | low] VaheΦn.

[p0205-b0010 | equation | low] h(gn)∈ Φh, (grad Ah(gn), grad qn) = (un(gn),grad qh)

[p0205-b0011 | ordinary-paragraph | medium] Then

[p0205-b0012 | equation | low] n = + n(pn)

[p0205-b0013 | ordinary-paragraph | medium] and we have an alternate expression for the bilinear form a,( ., .).

[p0205-b0014 | lemma | medium] Lemma 4.4. We have:

[p0205-b0015 | ordinary-paragraph | medium] Agh, Ihe Gn.

[p0205-b0016 | equation | low] (4.63)

[p0205-b0017 | equation | low] an(gn, Ih) = (grad n(gn) - un(gn),grad In)

[p0205-b0018 | ordinary-paragraph | medium] Likewise, the right-hand side of (4.52) reads:

[p0205-b0019 | equation | low] (u%, grad ph(ln)) = --(grad A - u%,grad Ih)

[p0205-b0020 | ordinary-paragraph | low] Hlhe Gh.

[p0205-b0021 | equation | low] (4.64)

[p0205-b0022 | proof | medium] Proof. By definition and (4.51) we have:

[p0205-b0023 | equation | low] an(gh, Ih) =v(grad un(gn),grad un(lh)) =- (grad ph(ln),un(9h))

[p0205-b0024 | equation | low] =—(grad(pn(ln) -lh),un(gn))-(grad Ih,un(gn))

[p0205-b0025 | equation | low] =—(grad An(gn), grad(pn(lnh) — lh)) —(grad ln,un(gn)

[p0205-b0026 | ordinary-paragraph | medium] by (4.62). Then (4.51) implies that

[p0205-b0027 | equation | low] an(gn, In) =(grad 2n(gn) --un(gn),grad In),

[p0205-b0028 | ordinary-paragraph | medium] thus proving (4.63). The proof of (4.64) is similar.

[p0205-b0029 | ordinary-paragraph | medium] Hence the Problem (4.52) takes the more manageable form:

[p0205-b0030 | ordinary-paragraph | medium] Find p, in G, such that:

[p0205-b0031 | ordinary-paragraph | medium] (4.65) (gradA,(Pn) - un(Pn), grad Ih) = (grad A --u%,grad In)

[p0205-b0032 | ordinary-paragraph | low] Vlhe Gh.

[p0205-b0033 | ordinary-paragraph | medium] From the preceding lemma and the definition of the bilinear form a,(., .) we

[p0205-b0034 | ordinary-paragraph | medium] know that the left-hand side of (4.65) is a bilinear, symmetric and positive definite

[p0205-b0035 | ordinary-paragraph | medium] form on G, x G,. Let us show briefly how (4.65) is solved in practice; the reader

[p0205-b0036 | ordinary-paragraph | medium] will find more details in Glowinski et al., Chapter 13 [37].

[p0205-b0037 | ordinary-paragraph | medium] Assume that the nodes of , N I are numbered from 1 to N, and let {μ}1<i≤Nn

[p0205-b0038 | ordinary-paragraph | medium] be the set of basis functions of Q, defined by:

[p0205-b0039 | equation | low] μ;(a;) = 1   for each node a; of J,N F,

[p0205-b0040 | equation | low] μ;(b) = O for all other nodes of h.

## PDF 206 / printed 192



[p0206-b0003 | equation | low] Gr = yy gi; with g; = g,(4;).

[p0206-b0004 | equation | low] i=1

[p0206-b0005 | ordinary-paragraph | high] With this notation, (4.65) is equivalent to:

[p0206-b0006 | ordinary-paragraph | high] Nn

[p0206-b0007 | equation | low] DY Pj 4n(HjHsi ) = —(grad An — uy, grady;) 1<i<N,.

[p0206-b0008 | equation | low] j=l

[p0206-b0009 | ordinary-paragraph | high] In other words we have to solve the system of linear equations:

[p0206-b0010 | ordinary-paragraph | high] (4.66) A,p =b

[p0206-b0011 | ordinary-paragraph | high] where

[p0206-b0012 | equation | low] (A,)i,j = Ay Lj Li) = (grad An (Lj) — u,(L4;), grad 1;),

[p0206-b0013 | equation | low] b, = —(grad 2; — u;, grad j1;).

[p0206-b0014 | ordinary-paragraph | high] To compute b, we have to solve the three Dirichlet problems (4.50) to find up

[p0206-b0015 | ordinary-paragraph | high] plus the first Dirichlet problem (4.62) to obtain 4?—a total of four Dirichlet

[p0206-b0016 | ordinary-paragraph | high] problems. To compute the j‘" column of the matrix A, we must solve the three

[p0206-b0017 | ordinary-paragraph | high] Dirichlet problems (4.51) with g, = yu; to find u,(u;) plus the second problem (4.62)

[p0206-b0018 | ordinary-paragraph | high] to get ,(4;)—again a total of four Dirichlet problems.

[p0206-b0019 | ordinary-paragraph | high] From the above considerations, it follows that the matrix A, is symmetric

[p0206-b0020 | ordinary-paragraph | high] and semi-positive definite with zero as a simple eigenvalue. Furthermore, when

[p0206-b0021 | ordinary-paragraph | high] the nodes of Y, are properly numbered, it can be shown that Ker(A,) is the

[p0206-b0022 | ordinary-paragraph | high] constant vector and that the principal block A, = (a,(Hj , Hi))1 <i,j<w,,-1 18 positive

[p0206-b0023 | ordinary-paragraph | high] definite. Therefore, setting py, = 0, we can solve (4.66) by the Cholesky factorisa-

[p0206-b0024 | ordinary-paragraph | high] tion for the first N, — 1 components of a representative p of p. Then the solution

[p0206-b0025 | ordinary-paragraph | high] pn Of (4.65) that satisfies | p,ds = 0 is given by:

[p0206-b0026 | ordinary-paragraph | high] P, — (1/meas(I’)) a ds.

[p0206-b0027 | ordinary-paragraph | high] Once p,, is known, the pressure p,(,,) and velocity u,(p,) are computed by solving

[p0206-b0028 | ordinary-paragraph | high] the three Dirichlet problems (4.51).

[p0206-b0029 | ordinary-paragraph | high] The problem (4.65) can also be solved by the conjugate-gradient algorithm

[p0206-b0030 | ordinary-paragraph | high] (cf. Glowinski et al. loc. cit.).
