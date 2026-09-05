# Paragraph candidates: chapter-03-section-04

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## chapter-03-section-04-pc00001 | equation | low | PDF 251

[[FORMULA:f-p0251-03972]]

## chapter-03-section-04-pc00002 | equation | low | PDF 251

[[FORMULA:f-p0251-03973]]

## chapter-03-section-04-pc00003 | ordinary-paragraph | low | PDF 251

provided the solution of the Stokes Problem (2.1) has its stream function Φ in dyi f! pauinin s! Koninoon fo uopuo auns ayi xaauos iou s! ? uaym (o)z+iH vorticity w belongs to Hl+1(Q).

## chapter-03-section-04-pc00004 | ordinary-paragraph | low | PDF 251

Finally, if the solution (u = (curl y,w), p) of Problem (2.1) has the regularity: nssaud ayi aof anunsa ayi aany am xaauos s!  pun (o),Hsd o)z+Hep solution of Problem (2.36):

## chapter-03-section-04-pc00005 | equation | low | PDF 251

[[FORMULA:f-p0251-03977]]

## chapter-03-section-04-pc00006 | equation | low | PDF 251

[[FORMULA:f-p0251-03978]]

## chapter-03-section-04-pc00007 | ordinary-paragraph | medium | PDF 251

$4. A “Stream Function-Gradient of Velocity Tensor" Method in Two Dimensions

## chapter-03-section-04-pc00008 | ordinary-paragraph | medium | PDF 251

The method discussed in this paragraph is obtained by taking for dependent variables the stream function y and the gradient of the velocity:

## chapter-03-section-04-pc00009 | equation | low | PDF 251

[[FORMULA:f-p0251-03979]]

## chapter-03-section-04-pc00010 | equation | low | PDF 251

[[FORMULA:f-p0251-03980]]

## chapter-03-section-04-pc00011 | ordinary-paragraph | medium | PDF 251

In other words it solves for the stream function and all its second derivatives instead of the Laplacian, as was the case of the previous method. The reader will discover that this approach leads to a scheme -called the Hellan-Herrmann- Johnson scheme--which is economical and optimal. This, and related schemes, are thoroughly analyzed in Brezzi & Raviart [15]. The analysis presented here is a slight variant of this analysis, proposed by Babuska et al [5]. It is an elegant application of the use of mesh-dependent norms.

## chapter-03-section-04-pc00012 | subsection | medium | PDF 251

4.1. The Hellan-Herrmann-Johnson Formulation

## chapter-03-section-04-pc00013 | ordinary-paragraph | medium | PDF 251

Let (u, p) denote the solution of Problem (2.1), but instead of the vorticity w, let us first introduce the non-symmetric gradient of velocity tensor Λ = (;):

## chapter-03-section-04-pc00014 | equation | low | PDF 251

[[FORMULA:f-p0251-03983]]

## chapter-03-section-04-pc00015 | equation | low | PDF 251

[[FORMULA:f-p0251-03984]]

## chapter-03-section-04-pc00016 | equation | low | PDF 251

[[FORMULA:f-p0251-03985]]

## chapter-03-section-04-pc00017 | ordinary-paragraph | medium | PDF 251

as a new dependent variable. Then the equations of Problem (2.1) read:

## chapter-03-section-04-pc00018 | ordinary-paragraph | medium | PDF 251

2

## chapter-03-section-04-pc00019 | equation | low | PDF 251

[[FORMULA:f-p0251-03987]]

## chapter-03-section-04-pc00020 | ordinary-paragraph | medium | PDF 251

in Q

## chapter-03-section-04-pc00021 | equation | low | PDF 251

[[FORMULA:f-p0251-03988]]

## chapter-03-section-04-pc00022 | equation | low | PDF 251

[[FORMULA:f-p0251-03989]]

## chapter-03-section-04-pc00023 | ordinary-paragraph | medium | PDF 251

whence a new formulation will be deduced by suitable integrations by parts.

## chapter-03-section-04-pc00024 | ordinary-paragraph | high | PDF 252

continuous boundary @x, unit exterior normal n= (n,,n,) and unit tangent vector t =(—n,,n,). For a vector v in H'(x)? and a tensor t = (t,;) in H*(k)* Green’s formula gives:

## chapter-03-section-04-pc00025 | ordinary-paragraph | high | PDF 252

K K OK Using the fact that v; = (v-n)n; + (v-t)t;, i = 1, 2, the boundary integral in (4.3) can also be written as:

## chapter-03-section-04-pc00026 | equation | low | PDF 252

[[FORMULA:f-p0252-03993]]

## chapter-03-section-04-pc00027 | ordinary-paragraph | high | PDF 252

Ox OK K Thus summing over all i and j and defining the quantities: 2

## chapter-03-section-04-pc00028 | equation | low | PDF 252

[[FORMULA:f-p0252-03994]]

## chapter-03-section-04-pc00029 | equation | low | PDF 252

[[FORMULA:f-p0252-03995]]

## chapter-03-section-04-pc00030 | ordinary-paragraph | high | PDF 252

(4.4) i, j=1

## chapter-03-section-04-pc00031 | ordinary-paragraph | high | PDF 252

the identity (4.3) becomes:

## chapter-03-section-04-pc00032 | equation | low | PDF 252

[[FORMULA:f-p0252-03998]]

## chapter-03-section-04-pc00033 | equation | low | PDF 252

[[FORMULA:f-p0252-03999]]

## chapter-03-section-04-pc00034 | ordinary-paragraph | high | PDF 252,253

— | v-nM,,(t)ds + | v-tM,,,(t) ds. ey OK Or, with the well-known summation convention that a repeated index corresponds to a sum, we have the more compact expression: (4.5) |( 0v;/0x,)t,;dx = -| v;(0t;;/0x;d)x + | v-nM,,(t)d s Ox +| v°tM,,(t)ds, VveH(k)*, VreH'(x)*. Ox Together with (4.2), this identity is the foundation of several schemes, including the Hellan-Herrmann-Johnson scheme. Here again, there are several ways of formulating the present method; we propose a mesh-dependent formulation closely related to that of Section 2.3. So, we assume that Q is a bounded domain of R? with a polygonal boundary I and we introduce a triangulation 7, of Q made of triangles and/or convex quadrilaterals with diameters bounded by h. Like in Section 2.3, assume that the velocity u and right-hand side f satisfy: ue H*(Q)’, fe L*(Q)’. Let us examine the equations (4.2) in the light of (4.1) and (4.5). Observe that if the tensor t belongs globally to H'(Q)* and if the vector field v belongs to then the sum of the surface integrals: )’,. <7, Jor ¥°0M,,(t) ds is zero. Therefore the assumption that u belongs to H*(Q)? permits to apply (4.5) to the first equations (4.2), thus giving:

## chapter-03-section-04-pc00035 | ordinary-paragraph | high | PDF 253

ES: ‘|A ,;(0v;/0x;) dx -| My(d)¥-tds} -| pdiv v dx = f-vdx (4.6) KeT;, kK OK Q Q

## chapter-03-section-04-pc00036 | ordinary-paragraph | high | PDF 253

Vve H(div;Q) withv|,¢H'(k)? VWKeZJ,. Likewise, to match (4.6) we can also express the relation (4.1) between u and J by: (4.7) (A ytyax= 5 4{c s(Ouloxadx — | My(o)u-tds} Veen (Q)e

## chapter-03-section-04-pc00037 | ordinary-paragraph | high | PDF 253

Py K Ox since the sum

## chapter-03-section-04-pc00038 | ordinary-paragraph | high | PDF 253

» M,,(t)u-tds Ke ZT, J 0K is zero for uin H}(Q)? and t in H}(Q)*.

## chapter-03-section-04-pc00039 | ordinary-paragraph | high | PDF 253

Finally a look at (4.6) and (4.7) shows that while the regularity of the test function vy can hardly be decreased, the test tensor t need not belong globally to H1(Q)*. In fact, (4.7) makes sense if t belongs to H'(x)* on each x. Besides that, it is convenient to assume that M,,(t) is continuous across interelement boundaries—.e. across all segments of J;,.

## chapter-03-section-04-pc00040 | ordinary-paragraph | high | PDF 253

Summing up, we see that if (u, p) is the solution of the Stokes problem (2.1) with u in (H7(Q)M H3(Q))? and p in H'(Q) L3(@) then the triple (u, A, p) with

## chapter-03-section-04-pc00041 | ordinary-paragraph | high | PDF 253

is also a solution of:

## chapter-03-section-04-pc00042 | equation | low | PDF 253

[[FORMULA:f-p0253-04015]]

## chapter-03-section-04-pc00043 | ordinary-paragraph | high | PDF 253

A€H'(x)* Wee, with M,,(A) continuous on J, and

## chapter-03-section-04-pc00044 | equation | low | PDF 253

[[FORMULA:f-p0253-04016]]

## chapter-03-section-04-pc00045 | ordinary-paragraph | high | PDF 253

ys ‘|a y(ousex)ax — | My(2}¥- tds}- | p divv d x (4.8) KeT;, K OK Q

## chapter-03-section-04-pc00046 | equation | low | PDF 253

[[FORMULA:f-p0253-04018]]

## chapter-03-section-04-pc00047 | ordinary-paragraph | high | PDF 253

Q

## chapter-03-section-04-pc00048 | equation | low | PDF 253

[[FORMULA:f-p0253-04019]]

## chapter-03-section-04-pc00049 | ordinary-paragraph | high | PDF 253,254

|A igtig Ax — S ‘|T Q KET, K OK VteH'(k)* VeeZ%Z, with M,,(t) continuous on J;,. Conversely, a routine argument shows that Problem (4.8) has at most one solution. Indeed, the second equations (4.8) imply: and in turn divu = 0 in Q. Then, supposing that the right-hand side f = 0 we easily derive that 4,, = 0 for all i,j . Thus, u is constant in each x and moreover

## chapter-03-section-04-pc00050 | equation | low | PDF 254

[[FORMULA:f-p0254-04024]]

## chapter-03-section-04-pc00051 | ordinary-paragraph | high | PDF 254

kK JOK VteH'(x)* with M,,(t) continuous across the segments of J;,. In view of the fact that u belongs to Ho(div; Q), this last relation readily implies that u = 0 in Q. As a consequence, Problem (4.8) is an equivalent formulation of the Stokes problem (2.1) whenever the solution of Problem (2.1) has sufficient regularity. To eliminate the pressure, Problem (4.8) can also be expressed in terms of stream functions. Indeed, recall that v¢ H,(div; Q) satisfies div v = 0 iff: v=curld with de® = {¢eH'(Q); d|,, = 0, |p is constant, 1 <i < p}. If in addition v|, €¢ H'(x)* then ¢|, ¢ H*(x) and conversely. Then we can rewrite directly Problem (4.8) in terms of stream functions, but the netations are simplified if instead of working with the tensor 4 we now introduce the symmetric tensor a:

## chapter-03-section-04-pc00052 | ordinary-paragraph | high | PDF 254

The correspondence between o and / is:

## chapter-03-section-04-pc00053 | equation | low | PDF 254

[[FORMULA:f-p0254-04032]]

## chapter-03-section-04-pc00054 | ordinary-paragraph | high | PDF 254

(4.10) M,,.(A) = —M,(0),

## chapter-03-section-04-pc00055 | equation | low | PDF 254

[[FORMULA:f-p0254-04034]]

## chapter-03-section-04-pc00056 | ordinary-paragraph | high | PDF 254

This induces us to define the following space of tensors: Ost A =ye = (Jel (OQ); eH (k) VRE). t= ty, , M,,(t) is continuous on each segment of /,}, together with the space ¥ of stream functions (already introduced in Section 2.3): (4.12) P = {¢e@; d|,€H?*(k) Vee J;}. With these spaces and the above correspondence, the sum of the surface integrals in (4.8) has also the following expression:

## chapter-03-section-04-pc00057 | equation | low | PDF 254

[[FORMULA:f-p0254-04038]]

## chapter-03-section-04-pc00058 | ordinary-paragraph | high | PDF 254,255

Ke TZ, J 0K Ty, where S(y) denotes the jump of y over the segments of 7%, (cf. Section 2.3). Therefore, Problem (4.8) has the following equivalent formulation, called the Hellan-Herrmann-Johnson formulation: Find a pair (o,W)eX x ¥ satisfying: KeZ, kK Ty, (4.13) =| \,f- ccuurrl lédx VdeY,P

## chapter-03-section-04-pc00059 | ordinary-paragraph | high | PDF 255

|O T dx — » |1 40° w/0x,0x,dx — | M,,(t)S(@w/én) is} Q Ke 7, Jk ifs, lee Voew. Here again, it is possible to express (4.13) by means of two bilinear forms a,(., .) and b,(., .): (4.14) G,\G.0). = |g ,t,4x Vtensors o and 7 in L?(Q)4,

## chapter-03-section-04-pc00060 | ordinary-paragraph | high | PDF 255

Q 6/0x,0x;dx + ifM, ,(t)S(6@/¢n) ds (4.15) by(t, @) = = |1 0°

## chapter-03-section-04-pc00061 | ordinary-paragraph | high | PDF 255

Vted, VhdeEH'(Q) with g|,¢H*(x). Then Problem (4.13) reads:

## chapter-03-section-04-pc00062 | ordinary-paragraph | high | PDF 255

Find a pair (o, W)eX x ¥ such that:

## chapter-03-section-04-pc00063 | equation | low | PDF 255

[[FORMULA:f-p0255-04045]]

## chapter-03-section-04-pc00064 | ordinary-paragraph | high | PDF 255

(4.13’)

## chapter-03-section-04-pc00065 | equation | low | PDF 255

[[FORMULA:f-p0255-04046]]

## chapter-03-section-04-pc00066 | ordinary-paragraph | high | PDF 255

Note the analogy with Problems (2.48) and (2.48’) of Section 2.3. Observe also that when t belongs to © H1(Q)* and ¢ belongs to ¥, b,(t, #) reduces to: (4.16) b(t.) = |( 6¢,/0x;)(04/0x,d)x ,

## chapter-03-section-04-pc00067 | ordinary-paragraph | high | PDF 255

Q a property which is similar to (2.51a).

## chapter-03-section-04-pc00068 | ordinary-paragraph | high | PDF 255

The following theorem summarizes the results of this section.

## chapter-03-section-04-pc00069 | theorem | high | PDF 255

Theorem 4.1. Let Q be a bounded plane polygon and 7, a triangulation of Q.

## chapter-03-section-04-pc00070 | ordinary-paragraph | high | PDF 255

Suppose that the solution (u = curl w, p) of the Stokes problem (2.1) has the regularity:

## chapter-03-section-04-pc00071 | ordinary-paragraph | high | PDF 255

ue(H7(Q)NH5(Q))?, pe H'(Q)NL4(2). Then

## chapter-03-section-04-pc00072 | ordinary-paragraph | high | PDF 255

1°) the triple (u,(A,;= 0u,/Ox;), p) is the unique solution of Problem (4.8); 2°) the pair ((o;; = Gas Ox,), W) is the unique solution of Problem (4.13). In the next section, we shall assume that: (4.17) We ta(2) em pen \2), in order to be able to work with either Problem (4.8) or Problem (4.13).

## chapter-03-section-04-pc00073 | ordinary-paragraph | high | PDF 256

We propose to approximate Problem (4.13). To simplify the discussion, we assume that 7, consists of triangles, but the present method can easily be extended to the case where Y, also contains quadrilaterals. First, we choose the finite element spaces. As usual, we take (4.18) 0, = {0e¢°(Q); 0|,EP, Vee F,}, G,=9,N9, for some integer | > 1. But as far as tensors are concerned, since the tensors of » need not be globally continuous, we can approximate it with a space }, that involves less degrees of freedom: (4.19) Jp At = ()e2) Tel VRE7, 5: With these spaces, Problem (4.13) is discretized by the following Problem (Q,,): Find a pair (6, W,)€+ }, X D, satisfying:

## chapter-03-section-04-pc00074 | equation | low | PDF 256

[[FORMULA:f-p0256-04059]]

## chapter-03-section-04-pc00075 | ordinary-paragraph | high | PDF 256

KET, JK Th,

## chapter-03-section-04-pc00076 | equation | low | PDF 256

[[FORMULA:f-p0256-04060]]

## chapter-03-section-04-pc00077 | equation | low | PDF 256

[[FORMULA:f-p0256-04061]]

## chapter-03-section-04-pc00078 | ordinary-paragraph | high | PDF 256

|( o,)jt4x — >, | (0? W,/0x,0x,)t,4x -| M,,(t)S(éy,/6n) ds Q Ee KET), JK

## chapter-03-section-04-pc00079 | ordinary-paragraph | high | PDF 256

When expressed in terms of the bilinear forms a,(., .) and b,(., .) defined by (4.14) and (4.15), the equations (4.20) can be written more compactly as:

## chapter-03-section-04-pc00080 | equation | low | PDF 256

[[FORMULA:f-p0256-04065]]

## chapter-03-section-04-pc00081 | ordinary-paragraph | high | PDF 256

(4.20’)

## chapter-03-section-04-pc00082 | equation | low | PDF 256

[[FORMULA:f-p0256-04066]]

## chapter-03-section-04-pc00083 | ordinary-paragraph | high | PDF 256

In order to analyze Problem (Q,), we must first study thoroughly the above finite element spaces and in particular equip them with appropriate norms and specify their degrees of freedom. As far as norms are concerned, the expression of the bilinear form b,(., .) suggests to choose: i 1/2 (4.21) IT lon = It llo,a + AlMl,( 7) laf Vred, i wi 1 1/2

## chapter-03-section-04-pc00084 | equation | low | PDF 256

[[FORMULA:f-p0256-04068]]

## chapter-03-section-04-pc00085 | ordinary-paragraph | high | PDF 256

(4.22) on Ke7, Vode H'(Q) with d|,¢H7(x). Observe again the analogy with (2.52) and (2.53). Note also that [atsP O)< Wt llowll@llan, VreX, Whe H*(Q) with ¢|,,¢H7(x),

## chapter-03-section-04-pc00086 | equation | low | PDF 256

[[FORMULA:f-p0256-04072]]

## chapter-03-section-04-pc00087 | lemma | high | PDF 257

Lemma 4.1. Let & be the reference unit triangle. A symmetric tensor-valued func-

## chapter-03-section-04-pc00088 | ordinary-paragraph | high | PDF 257

tion te P*, is uniquely determined on & by the following moments:

## chapter-03-section-04-pc00089 | ordinary-paragraph | high | PDF 257

| M,(t)qds YVqeP,_,(k’) for all sides k' of R, (4.23) -

## chapter-03-section-04-pc00090 | ordinary-paragraph | high | PDF 257

|T q aX Vqe P,_2(k), ESSE, MRE),

## chapter-03-section-04-pc00091 | proof | high | PDF 257

Proof. To begin with, we observe that (4.23) consists of

## chapter-03-section-04-pc00092 | equation | low | PDF 257

[[FORMULA:f-p0257-04075]]

## chapter-03-section-04-pc00093 | ordinary-paragraph | high | PDF 257

degrees of freedom and that

## chapter-03-section-04-pc00094 | equation | low | PDF 257

[[FORMULA:f-p0257-04076]]

## chapter-03-section-04-pc00095 | ordinary-paragraph | high | PDF 257

Thus it suffices to prove that the set of homogeneous equations:

## chapter-03-section-04-pc00096 | equation | low | PDF 257

[[FORMULA:f-p0257-04077]]

## chapter-03-section-04-pc00097 | ordinary-paragraph | high | PDF 257

(4.24) :

## chapter-03-section-04-pc00098 | equation | low | PDF 257

[[FORMULA:f-p0257-04079]]

## chapter-03-section-04-pc00099 | ordinary-paragraph | high | PDF 257

K has the unique solution t = 0.

## chapter-03-section-04-pc00100 | ordinary-paragraph | high | PDF 257

Now the first equation of( 4.24) is equivalent to M,(t) = 0 on Ok. And, taking advantage of the position and shape of k, this amounts to:

## chapter-03-section-04-pc00101 | ordinary-paragraph | high | PDF 257

tq 0 Oxnk — 0,

## chapter-03-section-04-pc00102 | equation | low | PDF 257

[[FORMULA:f-p0257-04082]]

## chapter-03-section-04-pc00103 | equation | low | PDF 257

[[FORMULA:f-p0257-04083]]

## chapter-03-section-04-pc00104 | ordinary-paragraph | high | PDF 257

Next, by taking q = 01,,/0X, in the second equation of (4.24), we obtain:

## chapter-03-section-04-pc00105 | equation | low | PDF 257

[[FORMULA:f-p0257-04085]]

## chapter-03-section-04-pc00106 | ordinary-paragraph | high | PDF 257

Combining with the three equations above, this yields first that t = 0 on X, + %, = 1 and then that t = 0 on OK.

## chapter-03-section-04-pc00107 | ordinary-paragraph | high | PDF 257

Then (4.24) immediately implies that t = 0 on the whole of K. O In order to extend Lemma 4.1 to an arbitrary triangle x, we must introduce a suitable transformation that maps a symmetric tensor on kK into a symmetric tensor on x while preserving in some sense M,(.) on 0x. To this end, we recall on the one hand that the normal n to x and the normal fi to & are related by:

## chapter-03-section-04-pc00108 | equation | low | PDF 257

[[FORMULA:f-p0257-04089]]

## chapter-03-section-04-pc00109 | ordinary-paragraph | high | PDF 258

where x = F(X) = B,& + b, and B,, is a nonsingular matrix with constant coefficients. On the other hand, we remark that

## chapter-03-section-04-pc00110 | equation | low | PDF 258

[[FORMULA:f-p0258-04091]]

## chapter-03-section-04-pc00111 | ordinary-paragraph | high | PDF 258

where ((., .)) denotes the Euclidean scalar product of R* associated with ||. ||. Thus, we can write

## chapter-03-section-04-pc00112 | equation | low | PDF 258

[[FORMULA:f-p0258-04092]]

## chapter-03-section-04-pc00113 | ordinary-paragraph | high | PDF 258

This suggests to establish (in each x) the correspondence between tensor-valued functions: (4.25a) = B(CO Fe |B 4.4), or equivalently (4.25b) t= Dac Or (Be =e (Gc) The first equation can be written explicitly as follows: Zz

## chapter-03-section-04-pc00114 | equation | low | PDF 258

[[FORMULA:f-p0258-04095]]

## chapter-03-section-04-pc00115 | equation | low | PDF 258

[[FORMULA:f-p0258-04096]]

## chapter-03-section-04-pc00116 | ordinary-paragraph | high | PDF 258

Obviously, the transformation Y. preserves the symmetry and regularity of tensors and furthermore: (4.26) M,(2) = |\(BAel*)?) M,"C) , or (4.26') M(t) = |B (n0 F,) |? My(2). since

## chapter-03-section-04-pc00117 | equation | low | PDF 258

[[FORMULA:f-p0258-04099]]

## chapter-03-section-04-pc00118 | ordinary-paragraph | high | PDF 258

Hence it is easy to check that the statement of Lemma 4.1 carries over to an arbitrary triangle x of 7,,. As a consequence, we can take the following values as degrees of freedom for the tensors t of 2,: | M,(t)qds VqeP,_,(k’), VK' of I,

## chapter-03-section-04-pc00119 | ordinary-paragraph | high | PDF 258

|t yqdx~ “NG ePi5(«),0 wisi] S120) Vine Teenie:

## chapter-03-section-04-pc00120 | remark | high | PDF 258

Remark 4.1. The simplest example of spaces 2}, corresponds to | = 1:

## chapter-03-section-04-pc00121 | equation | low | PDF 258

[[FORMULA:f-p0258-04101]]

## chapter-03-section-04-pc00122 | ordinary-paragraph | high | PDF 258

M,,(t) is continuous on each segment of I}.

## chapter-03-section-04-pc00123 | ordinary-paragraph | low | PDF 259

s         e from Z onto Z, with attractive properties. First, if t is a symmetric tensor of L'(k)4 with M,(t)e L'(ok) we define the symmetric tensor π,t of Pi-, by:

## chapter-03-section-04-pc00124 | equation | low | PDF 259

[[FORMULA:f-p0259-04102]]

## chapter-03-section-04-pc00125 | ordinary-paragraph | low | PDF 259

Vsides k' of k, Vq∈Pi-i(k)

## chapter-03-section-04-pc00126 | equation | low | PDF 259

[[FORMULA:f-p0259-04103]]

## chapter-03-section-04-pc00127 | equation | low | PDF 259

[[FORMULA:f-p0259-04104]]

## chapter-03-section-04-pc00128 | ordinary-paragraph | medium | PDF 259

Then for te E, we define n,te E, by:

## chapter-03-section-04-pc00129 | equation | low | PDF 259

[[FORMULA:f-p0259-04105]]

## chapter-03-section-04-pc00130 | equation | low | PDF 259

[[FORMULA:f-p0259-04106]]

## chapter-03-section-04-pc00131 | ordinary-paragraph | medium | PDF 259

Clearly, π,t is a symmetric tensor and the continuity of M,(t) implies that M,(,t) is continuous across each interelement boundary k'. Therefore 7,t belongs indeed to E,. In addition, we readily derive from (4.25a) and (4.26) that (4.27) holds iff

## chapter-03-section-04-pc00132 | ordinary-paragraph | medium | PDF 259

Vsides k' of k,

## chapter-03-section-04-pc00133 | equation | low | PDF 259

[[FORMULA:f-p0259-04108]]

## chapter-03-section-04-pc00134 | equation | low | PDF 259

[[FORMULA:f-p0259-04109]]

## chapter-03-section-04-pc00135 | equation | low | PDF 259

[[FORMULA:f-p0259-04110]]

## chapter-03-section-04-pc00136 | equation | low | PDF 259

[[FORMULA:f-p0259-04111]]

## chapter-03-section-04-pc00137 | equation | low | PDF 259

[[FORMULA:f-p0259-04112]]

## chapter-03-section-04-pc00138 | ordinary-paragraph | medium | PDF 259

where, as usual, k denotes the unit reference triangle. Hence, applying the definition (4.27) to k, we find that 7, is preserved by affine transformations:

## chapter-03-section-04-pc00139 | equation | low | PDF 259

[[FORMULA:f-p0259-04114]]

## chapter-03-section-04-pc00140 | equation | low | PDF 259

[[FORMULA:f-p0259-04115]]

## chapter-03-section-04-pc00141 | ordinary-paragraph | medium | PDF 259

The remaining properties of n, are stated in the next lemma.

## chapter-03-section-04-pc00142 | lemma | medium | PDF 259

Lemma 4.2. Assume that the triangulation J, is regular. The operator π, defined

## chapter-03-section-04-pc00143 | ordinary-paragraph | medium | PDF 259

by (4.27) and (4.28) is a linear mapping from 2 onto E, and satisfies:

## chapter-03-section-04-pc00144 | equation | low | PDF 259

[[FORMULA:f-p0259-04117]]

## chapter-03-section-04-pc00145 | equation | low | PDF 259

[[FORMULA:f-p0259-04118]]

## chapter-03-section-04-pc00146 | ordinary-paragraph | low | PDF 259

VteE.

## chapter-03-section-04-pc00147 | equation | low | PDF 259

[[FORMULA:f-p0259-04119]]

## chapter-03-section-04-pc00148 | equation | low | PDF 259

[[FORMULA:f-p0259-04120]]

## chapter-03-section-04-pc00149 | ordinary-paragraph | medium | PDF 259

Moreover, if t e H*(Q)4 N E for some real ke [1, l], the following estimate holds:

## chapter-03-section-04-pc00150 | equation | low | PDF 259

[[FORMULA:f-p0259-04121]]

## chapter-03-section-04-pc00151 | equation | low | PDF 259

[[FORMULA:f-p0259-04122]]

## chapter-03-section-04-pc00152 | proof | medium | PDF 259

Proof. It is clear from (4.27) that the operator n, is a linear mapping from  onto

## chapter-03-section-04-pc00153 | ordinary-paragraph | medium | PDF 259

E,. Besides that, (4.31) follows immediately from (4.27), the expression (4.15) of bh(., .) and the definition of Oh.

## chapter-03-section-04-pc00154 | ordinary-paragraph | medium | PDF 259

Let us turn to (4.32). To begin with, we observe from (4.27) that

## chapter-03-section-04-pc00155 | equation | low | PDF 259

[[FORMULA:f-p0259-04126]]

## chapter-03-section-04-pc00156 | ordinary-paragraph | low | PDF 259

'3A 

## chapter-03-section-04-pc00157 | equation | low | PDF 259

[[FORMULA:f-p0259-04127]]

## chapter-03-section-04-pc00158 | ordinary-paragraph | high | PDF 260

(4.35) ItnTIlo,a <Clltllon Vrer, where, for the sake of simplicity, the norms of tensors and scalars are denoted alike. For each x of 7, (4.30) and (4.25a) imply:

## chapter-03-section-04-pc00159 | equation | low | PDF 260

[[FORMULA:f-p0260-04130]]

## chapter-03-section-04-pc00160 | ordinary-paragraph | high | PDF 260

But it follows easily from (4.29) that

## chapter-03-section-04-pc00161 | equation | low | PDF 260

[[FORMULA:f-p0260-04132]]

## chapter-03-section-04-pc00162 | ordinary-paragraph | high | PDF 260

where the constant C, is independent of h. Next, (4.26) implies:

## chapter-03-section-04-pc00163 | equation | low | PDF 260

[[FORMULA:f-p0260-04134]]

## chapter-03-section-04-pc00164 | ordinary-paragraph | high | PDF 260

Likewise, we derive from (4.25b) that

## chapter-03-section-04-pc00165 | equation | low | PDF 260

[[FORMULA:f-p0260-04135]]

## chapter-03-section-04-pc00166 | ordinary-paragraph | high | PDF 260

Collecting these four inequalities and applying (A.2) and (A.4) we obtain: THO. S Co(eIT U O + Fe Mell Ma(™) M10, 0n)- Since 7, is regular, this proves (4.35) and in turn (4.32). Finally, let us establish (4.33). Like above, we have

## chapter-03-section-04-pc00167 | equation | low | PDF 260

[[FORMULA:f-p0260-04138]]

## chapter-03-section-04-pc00168 | ordinary-paragraph | high | PDF 260

As the mapping z,; leaves invariant the symmetric tensors with coefficients in Pros (Ac 12) gives: [eee R: Hiei! According to (4.25b), we have:

## chapter-03-section-04-pc00169 | equation | low | PDF 260

[[FORMULA:f-p0260-04139]]

## chapter-03-section-04-pc00170 | ordinary-paragraph | high | PDF 260

and in view of (A.7) this becomes (4.36) tlie < C5 llB ellB et |? det(B7, I)he : Since 7, is regular, the above inequalities yield: [7,7 —Tllo.a Coh*|thk,0: Similarly, it stems from (4.26’) that:

## chapter-03-section-04-pc00171 | equation | low | PDF 260

[[FORMULA:f-p0260-04141]]

## chapter-03-section-04-pc00172 | ordinary-paragraph | high | PDF 260

and the trace Theorem I.1.5 implies:

## chapter-03-section-04-pc00173 | equation | low | PDF 260

[[FORMULA:f-p0260-04142]]

## chapter-03-section-04-pc00174 | ordinary-paragraph | high | PDF 260

Therefore, owing to (4.36) and the regularity of 7,, we get:

## chapter-03-section-04-pc00175 | equation | low | PDF 260

[[FORMULA:f-p0260-04144]]

## chapter-03-section-04-pc00176 | ordinary-paragraph | low | PDF 260,261

thus establishing (4.33). O (4.37) {bn(th,Φh) = 0 VΦh∈Φn} iff {bn(tn,Φ) = 0 VΦ∈PnC(S)}.

## chapter-03-section-04-pc00177 | proof | medium | PDF 261

Proof. Obviously, it is the "only if" part of (4.37) which must be established. To

## chapter-03-section-04-pc00178 | ordinary-paragraph | medium | PDF 261

this end, let us take Φ in C°(Ω) with Φlx eH²(k) (in which case Φe H'(Q)) and prove that

## chapter-03-section-04-pc00179 | equation | low | PDF 261

[[FORMULA:f-p0261-04148]]

## chapter-03-section-04-pc00180 | equation | low | PDF 261

[[FORMULA:f-p0261-04149]]

## chapter-03-section-04-pc00181 | ordinary-paragraph | medium | PDF 261

where I, is the interpolation operator defined by (A.22).

## chapter-03-section-04-pc00182 | ordinary-paragraph | low | PDF 261

Indeed, two integrations by parts yield: f02Φ/0x;0x;dx = (0²f/0x;0x;)Φ dx - (of/ox;)pn; ds + f(oΦ/0x;)n;ds Jor JaK KC Vf, Φe H'(k). Thus, when f e Pi-1, the formulas (A.22) give:

## chapter-03-section-04-pc00183 | ordinary-paragraph | low | PDF 261

fo²(Φ - IhΦ)/@x;0x;dx = ,  VfePi-i· ()HA  S fn;0(Φ -InΦ)/0x;ds Jak Substituting into the definition (4.15) of b, we obtain:

## chapter-03-section-04-pc00184 | equation | low | PDF 261

[[FORMULA:f-p0261-04153]]

## chapter-03-section-04-pc00185 | ordinary-paragraph | low | PDF 261

Mnt(th)o(o - Inb)/ot ds. KegnJor (') u aide p ae go y ss a uo sd q ii u we readily find that b,(th, Φ - IhΦ) = 0. This proves (4.37).

## chapter-03-section-04-pc00186 | ordinary-paragraph | medium | PDF 261

From the definition (A.22) it is easy to derive that the statement of Lemma 2.11 holds with 0, = Iu:

## chapter-03-section-04-pc00187 | equation | low | PDF 261

[[FORMULA:f-p0261-04156]]

## chapter-03-section-04-pc00188 | equation | low | PDF 261

[[FORMULA:f-p0261-04157]]

## chapter-03-section-04-pc00189 | ordinary-paragraph | medium | PDF 261

provided the triangulation J, is regular. Thus, combining (4.38) and (4.39) we have the next result.

## chapter-03-section-04-pc00190 | corollary | medium | PDF 261

Corollary 4.1. The operator I, defined by (A.22) satisfies:

## chapter-03-section-04-pc00191 | ordinary-paragraph | low | PDF 261

“"A

## chapter-03-section-04-pc00192 | equation | low | PDF 261

[[FORMULA:f-p0261-04159]]

## chapter-03-section-04-pc00193 | ordinary-paragraph | medium | PDF 261

In addition, if J, is a regular triangulation of Ω, there exists a constant C > 0, independent of h and Φ, such that:

## chapter-03-section-04-pc00194 | equation | low | PDF 261

[[FORMULA:f-p0261-04161]]

## chapter-03-section-04-pc00195 | ordinary-paragraph | medium | PDF 261

()HA provided the real k belongs to [2, I + 1].

## chapter-03-section-04-pc00196 | ordinary-paragraph | medium | PDF 261,262

Now we turn to the inf-sup condition. Let us first restrict ourselves to the space of tensors Z N o and more specifically to tensors of the form All such tensors satisfy

## chapter-03-section-04-pc00197 | equation | low | PDF 262

[[FORMULA:f-p0262-04163]]

## chapter-03-section-04-pc00198 | ordinary-paragraph | high | PDF 262

and talldvn rs 2 || nll5,.0 ae h|| O,\ld,r,- Hence applying Lemma 2.12 we obtain the preliminary result:

## chapter-03-section-04-pc00199 | equation | low | PDF 262

[[FORMULA:f-p0262-04164]]

## chapter-03-section-04-pc00200 | ordinary-paragraph | high | PDF 262

te LO? | Tallon where f* is the constant of Lemma 2.12, provided Q is convex and the triangulation is uniformly regular. By virtue of (4.31) and (4.32) this condition implies the inf-sup condition on the space 2).

## chapter-03-section-04-pc00201 | lemma | high | PDF 262

Lemma 4.4. Let Q be a bounded, convex polygon and let 7, be a uniformly regular

## chapter-03-section-04-pc00202 | ordinary-paragraph | high | PDF 262

triangulation of Q. Then we have:

## chapter-03-section-04-pc00203 | equation | low | PDF 262

[[FORMULA:f-p0262-04167]]

## chapter-03-section-04-pc00204 | ordinary-paragraph | high | PDF 262

Tey, Tallon where B* and C, are the constants of (2.63) and (4.32) respectively.

## chapter-03-section-04-pc00205 | remark | high | PDF 262

Remark 4.2. Owing to Remark 2.8, we also have

## chapter-03-section-04-pc00206 | equation | low | PDF 262

[[FORMULA:f-p0262-04169]]

## chapter-03-section-04-pc00207 | equation | low | PDF 262

[[FORMULA:f-p0262-04170]]

## chapter-03-section-04-pc00208 | ordinary-paragraph | high | PDF 262

Thus, the assumptions of Lemma 4.4 imply the additional inf-sup condition: oO) 5 TH V2C)Wldrli..o

## chapter-03-section-04-pc00209 | equation | low | PDF 262

[[FORMULA:f-p0262-04172]]

## chapter-03-section-04-pc00210 | ordinary-paragraph | high | PDF 262

TEL, IT llo.n

## chapter-03-section-04-pc00211 | remark | high | PDF 262

Remark 4.3. The construction of Lemma 4.4 can also be applied to prove that

## chapter-03-section-04-pc00212 | ordinary-paragraph | high | PDF 262

Problem (4.20) has a unique solution without restriction on Q and 7,. Indeed, since we are working with finite-dimensional spaces, all we need to show is that the set {4,€ ®,; b,(t,,, %,) = 0 Vt, €2),} is reduced to the zero function. Now, by proceeding like above, we construct te X @f such that b,(t,¢,) = |¢al7.e = b, (7,7, ,) = 0. Hence ¢, = 0. Finally when 7, is uniformly regular we can show like in Lemma 2.7 that Il- lon and ||. ||o,q are two uniformly equivalent norms on &,. The proof, which is left as an exercise, stems from the inequality:

## chapter-03-section-04-pc00213 | equation | low | PDF 262

[[FORMULA:f-p0262-04177]]

## chapter-03-section-04-pc00214 | ordinary-paragraph | low | PDF 262,263

We are now in a position to establish optimal error estimates for Problem (4.20). the solution (u = curl y,p) of the Stokes Problem (2.1) satisfies (4.17); let o = (024/0x;0xj)i,j

## chapter-03-section-04-pc00215 | ordinary-paragraph | medium | PDF 263

1°) If the triangulation J, is regular, we have the bound

## chapter-03-section-04-pc00216 | equation | low | PDF 263

[[FORMULA:f-p0263-04180]]

## chapter-03-section-04-pc00217 | equation | low | PDF 263

[[FORMULA:f-p0263-04181]]

## chapter-03-section-04-pc00218 | equation | low | PDF 263

[[FORMULA:f-p0263-04182]]

## chapter-03-section-04-pc00219 | ordinary-paragraph | medium | PDF 263

if  e Hk+2(Q). If in addition Ω is convex, we have either

## chapter-03-section-04-pc00220 | equation | low | PDF 263

[[FORMULA:f-p0263-04183]]

## chapter-03-section-04-pc00221 | equation | low | PDF 263

[[FORMULA:f-p0263-04184]]

## chapter-03-section-04-pc00222 | ordinary-paragraph | low | PDF 263

or (4.42) Iμ -nli.o ≤ Chk|ylk+1.   Vk∈[2,I]  if l ≥ 2 and ∈Hk+1(Ω).

## chapter-03-section-04-pc00223 | ordinary-paragraph | medium | PDF 263

2°) If J, is uniformly regular, we have:

## chapter-03-section-04-pc00224 | equation | low | PDF 263

[[FORMULA:f-p0263-04186]]

## chapter-03-section-04-pc00225 | equation | low | PDF 263

[[FORMULA:f-p0263-04187]]

## chapter-03-section-04-pc00226 | equation | low | PDF 263

[[FORMULA:f-p0263-04188]]

## chapter-03-section-04-pc00227 | ordinary-paragraph | medium | PDF 263

and if in addition Q is convex, we have:

## chapter-03-section-04-pc00228 | equation | low | PDF 263

[[FORMULA:f-p0263-04189]]

## chapter-03-section-04-pc00229 | equation | low | PDF 263

[[FORMULA:f-p0263-04190]]

## chapter-03-section-04-pc00230 | equation | low | PDF 263

[[FORMULA:f-p0263-04191]]

## chapter-03-section-04-pc00231 | ordinary-paragraph | medium | PDF 263

()+H pup

## chapter-03-section-04-pc00232 | proof | medium | PDF 263

Proof. As usual, we have:

## chapter-03-section-04-pc00233 | equation | low | PDF 263

[[FORMULA:f-p0263-04192]]

## chapter-03-section-04-pc00234 | equation | low | PDF 263

[[FORMULA:f-p0263-04193]]

## chapter-03-section-04-pc00235 | equation | low | PDF 263

[[FORMULA:f-p0263-04194]]

## chapter-03-section-04-pc00236 | ordinary-paragraph | medium | PDF 263

Owing to Lemma 4.2 and Corollary 4.1, the relations (4.45) yield:

## chapter-03-section-04-pc00237 | equation | low | PDF 263

[[FORMULA:f-p0263-04196]]

## chapter-03-section-04-pc00238 | equation | low | PDF 263

[[FORMULA:f-p0263-04197]]

## chapter-03-section-04-pc00239 | ordinary-paragraph | medium | PDF 263

and observe that these equalities hold without constraint on Q and ,. Now, the last equation implies directly that

## chapter-03-section-04-pc00240 | equation | low | PDF 263

[[FORMULA:f-p0263-04198]]

## chapter-03-section-04-pc00241 | equation | low | PDF 263

[[FORMULA:f-p0263-04199]]

## chapter-03-section-04-pc00242 | ordinary-paragraph | medium | PDF 263

In addition, when J, is uniformly regular, the equivalence between the norms Il . Ilo, and Il Ilo,o gives

## chapter-03-section-04-pc00243 | equation | low | PDF 263

[[FORMULA:f-p0263-04200]]

## chapter-03-section-04-pc00244 | equation | low | PDF 263

[[FORMULA:f-p0263-04201]]

## chapter-03-section-04-pc00245 | ordinary-paragraph | medium | PDF 263

Therefore (4.40) and (4.43) follow from (4.33).

## chapter-03-section-04-pc00246 | ordinary-paragraph | medium | PDF 263

Next, the second equation (4.45) and Corollary 4.1 yield:

## chapter-03-section-04-pc00247 | equation | low | PDF 263

[[FORMULA:f-p0263-04204]]

## chapter-03-section-04-pc00248 | equation | low | PDF 263

[[FORMULA:f-p0263-04205]]

## chapter-03-section-04-pc00249 | ordinary-paragraph | medium | PDF 263,264

Therefore, when Ω is convex and , uniformly regular, it stems from Lemma 4.4 that Hence (4.44) follows from (4.48), (4.40) and Corollary 4.1. To establish (4.41) and (4.42) we use a familiar duality argument. For g in L?(Q)* we introduce the auxiliary Stokes Problem:

## chapter-03-section-04-pc00250 | equation | low | PDF 264

[[FORMULA:f-p0264-04208]]

## chapter-03-section-04-pc00251 | equation | low | PDF 264

[[FORMULA:f-p0264-04209]]

## chapter-03-section-04-pc00252 | equation | low | PDF 264

[[FORMULA:f-p0264-04210]]

## chapter-03-section-04-pc00253 | ordinary-paragraph | high | PDF 264

Since Q is convex, the solution (p,, 4 ,) belongs to H'(Q)* x H?(Q) with (4.50) Hgllio + WAglls.o < CsllSllo,a- Then a straightforward combination of (4.45), (4.49), (4.31) and Corollary 4.1 leads to:

## chapter-03-section-04-pc00254 | equation | low | PDF 264

[[FORMULA:f-p0264-04213]]

## chapter-03-section-04-pc00255 | ordinary-paragraph | high | PDF 264

+ b,(o — Ty,A, —Ty4g) VbneD,, Vt,E 2p. When | > 2, Corollary 4.1, (4.33) and (4.50) yield: IY — Walia <C vn in lw — Prllon + Ilo — Grllo,a + aE lo — toa

## chapter-03-section-04-pc00256 | equation | low | PDF 264

[[FORMULA:f-p0264-04216]]

## chapter-03-section-04-pc00257 | ordinary-paragraph | high | PDF 264

When ! = 1, we only have:

## chapter-03-section-04-pc00258 | equation | low | PDF 264

[[FORMULA:f-p0264-04218]]

## chapter-03-section-04-pc00259 | ordinary-paragraph | high | PDF 264

(4.52) bao Coat all Gs ta llorn- TEL, In view of (4.40), Corollary 4.1 and (4.33), this implies (4.42) and (4.41). O

## chapter-03-section-04-pc00260 | corollary | high | PDF 264

Corollary 4.2. We retain all the assumptions of Theorem 4.2. If w belongs to

## chapter-03-section-04-pc00261 | ordinary-paragraph | high | PDF 264

H**?(Q) for some real ke[1,1] with | > 1, we have: (4.53) IY — Walis.o <C A |Whe+2,@ for each s > 2.

## chapter-03-section-04-pc00262 | proof | high | PDF 264

Proof. Formula (4.47) and the inf-sup condition proved in Remark 4.2 give:

## chapter-03-section-04-pc00263 | ordinary-paragraph | high | PDF 264

(4.54) IT.— Vilis.a < C(S) lo — ollo,0- Hence (4.53) follows from (4.40) and (A.23). O

## chapter-03-section-04-pc00264 | remark | high | PDF 264

Remark 4.4. The above theorem calls for a number of comments. First of all, it

## chapter-03-section-04-pc00265 | ordinary-paragraph | medium | PDF 264,265

is obvious that this approach yields very neatly optimal error estimates for polynomials of all degrees. In addition, the scheme considered is fairly inexpensive. On the other hand, all results are stated for a right-hand side f in L?(Q)? whereas one is often interested in solving the Stokes problem when the right-hand side is in L’(Q)? withr < 2. The next section extends the error analysis to this case. case where the right-hand side f belongs to L'(Q)² with 1 < r < 2. Since the spaces of Problem (4.20) are finite-dimensional, and in particular Φ, is included in W1, ∞(Q), it is clear that Problem (4.20) still has a unique solution when the right-hand side f is only in L'(Ω), for 1 < r < 2. Thus, we must focus our attention on the equations (4.13) of the continuous problem and see how to adapt them to such a right-hand side. This is achieved much like in Section 2.1: the regularity of the tensor-valued functions t is decreased while that of the test stream functions Φ is increased.

## chapter-03-section-04-pc00266 | ordinary-paragraph | medium | PDF 265

If the solution (u = curly,p) of the Stokes Problem (2.1) is such that y e W3,"(Ω), then o belongs to W1.(Q)4 and therefore, according to Sobolev's Imbedding Theorem 1.1.3 and the trace Theorem I.1.5 we have:

## chapter-03-section-04-pc00267 | ordinary-paragraph | low | PDF 265

("1)(-T(o)"W ()T0 Hence we replace the space of tensors E by:

## chapter-03-section-04-pc00268 | equation | low | PDF 265

[[FORMULA:f-p0265-04233]]

## chapter-03-section-04-pc00269 | ordinary-paragraph | medium | PDF 265

on each segment of Fh}. Likewise, since f is only in L'(Q)², we replace the space Y by

## chapter-03-section-04-pc00270 | equation | low | PDF 265

[[FORMULA:f-p0265-04234]]

## chapter-03-section-04-pc00271 | ordinary-paragraph | medium | PDF 265

Then, it is a matter of routine to verify that the pair (y,o = (o?/ox;ox,)) is the unique solution of:

## chapter-03-section-04-pc00272 | ordinary-paragraph | low | PDF 265

()sMUA f·curlΦ dx

## chapter-03-section-04-pc00273 | equation | low | PDF 265

[[FORMULA:f-p0265-04236]]

## chapter-03-section-04-pc00274 | equation | low | PDF 265

[[FORMULA:f-p0265-04237]]

## chapter-03-section-04-pc00275 | ordinary-paragraph | low | PDF 265

JQ

## chapter-03-section-04-pc00276 | equation | low | PDF 265

[[FORMULA:f-p0265-04238]]

## chapter-03-section-04-pc00277 | ordinary-paragraph | medium | PDF 265

Now, a glance at Theorem 4.2 and its corollary shows that, in order to derive adequate error estimates in this case, we must verify that (4.46a), (4.48) and (4.54) are still valid here. To begin with, (4.46a) is a consequence of (4.45) together with the equations:

## chapter-03-section-04-pc00278 | ordinary-paragraph | low | PDF 265

on∈n,

## chapter-03-section-04-pc00279 | equation | low | PDF 265

[[FORMULA:f-p0265-04241]]

## chapter-03-section-04-pc00280 | equation | low | PDF 265

[[FORMULA:f-p0265-04242]]

## chapter-03-section-04-pc00281 | ordinary-paragraph | medium | PDF 265

But for y in W3.r(Ω) and o in W1.r(Ω)4, both Iny and π,o are well-defined and satisfy the above equations. And of course the equations (4.45) hold here. Therefore (4.46a) is verified. Likewise, (4.48) and (4.54) stem from (4.47) and the inf-sup conditions of Lemma 4.4 and Remark 4.2. Since the finite element spaces are unchanged, the inf-sup conditions carry over without modification; and the above considerations show that (4.47) is still valid here. The next lemma summarizes these results.

## chapter-03-section-04-pc00282 | ordinary-paragraph | high | PDF 266

of the Stokes Problem (2.1) satisfy: (4.56) weWw*"(Q), peW"(Q) for some reé(1,2]. Then (4.46a) is valid. If in addition Q is convex and J, is uniformly regular, then (4.48) and (4.54) also hold. Next, it is easy to extend the approximation property of Lemma 4.2 to the case where t€ W!’"(Q)*.

## chapter-03-section-04-pc00283 | lemma | high | PDF 266

Lemma 4.6. Let 7, be a regular family of triangulations of Q. We have:

## chapter-03-section-04-pc00284 | ordinary-paragraph | high | PDF 266

(4.57) Wpe = og Craie cl e for all symmetric tensors t in W'*"(Q)* with 1 <r < 2. Finally, combining these two lemmas we easily obtain the desired extension of Theorem 4.2 and its corollary.

## chapter-03-section-04-pc00285 | theorem | high | PDF 266

Theorem 4.3. Suppose that the regularity conditions (4.56) hold. If the triangulation

## chapter-03-section-04-pc00286 | ordinary-paragraph | high | PDF 266

7, is regular, the solution (o,,, W;,) of Problem (4.20) satisfies the estimate: (4.58) lo — allo.a < Ch|E| 3 ,,,0, where o = (0*y/0x;0x;). If in addition 7, is uniformly regular and Q is convex, then for each real B > 2, there exists a constant C,() such that: (4.59) IW — Waltp.a < Co(B"h|rW |e3,, ,0. Furthermore, when the polynomials are of degree | > 2 we also have: 1/2 (4.60) (e la Vale) < CshO Mls... KET),

## chapter-03-section-04-pc00287 | subsection | high | PDF 266

4.4. Discontinuous Approximation of the Pressure

## chapter-03-section-04-pc00288 | ordinary-paragraph | high | PDF 266

This section is devoted to a brief analysis of a numerical method that recovers the pressure in the Hellan-Herrmann-Johnson scheme. The pressure is obtained by a suitable approximation of Problem (4.8)—suitable in the sense that it reduces to the equations (4.20) when divergence-free test functions are used. The reader will find that it corresponds to a discontinuous approximation of the pressure. To be specific, we want to construct finite-dimensional subspaces Do, of H (div; Q) and Q,, of L$(@) that satisfy:

## chapter-03-section-04-pc00289 | equation | low | PDF 266

[[FORMULA:f-p0266-04263]]

## chapter-03-section-04-pc00290 | ordinary-paragraph | medium | PDF 266,267

together with an adequate inf-sup condition. Let us start with the reference element x. If « is the unit triangle, we introduce the polynomial space of dimenwhere P. denotes the space of homogeneous polynomials of degree k. If k is the unit square, we simply take the space of dimension 2l(l + 1):

## chapter-03-section-04-pc00291 | equation | low | PDF 267

[[FORMULA:f-p0267-04265]]

## chapter-03-section-04-pc00292 | equation | low | PDF 267

[[FORMULA:f-p0267-04266]]

## chapter-03-section-04-pc00293 | ordinary-paragraph | medium | PDF 267

where exceptionally Qr.s denotes the space of all polynomials of degree at most r in x, and s in x2. Then, it is easy to check that:

## chapter-03-section-04-pc00294 | equation | low | PDF 267

[[FORMULA:f-p0267-04267]]

## chapter-03-section-04-pc00295 | ordinary-paragraph | medium | PDF 267

Ker(div) = curl(P) if k is the unit triangle,

## chapter-03-section-04-pc00296 | equation | low | PDF 267

[[FORMULA:f-p0267-04269]]

## chapter-03-section-04-pc00297 | ordinary-paragraph | medium | PDF 267

Ker(div) = curl(Q)  if k is the unit square. In addition, owing to the geometry of k, v·n reduces to a polynomial of Pi-1 on Ok for v in D.

## chapter-03-section-04-pc00298 | ordinary-paragraph | medium | PDF 267

As a consequence, we can choose the following degrees of freedom for the vectors v of D:

## chapter-03-section-04-pc00299 | ordinary-paragraph | low | PDF 267

(i) the boundary moments of order I - 1 for v·n: ·nf ds   Vf e Pi-1  on each side k' of k; JR' (4.62)  (ii) the interior moments of order I -- 2 for v:

## chapter-03-section-04-pc00300 | ordinary-paragraph | low | PDF 267

P-2  if k is a triangle, ·fdx A Qi-2.l-1 × Qi-1.l-2  if k is a square. It is a matter of routine to check that (4.62) defines a unique vector  of D and that the restriction of ·Λ on each side k' depends only upon the l values prescribed on this side.

## chapter-03-section-04-pc00301 | ordinary-paragraph | medium | PDF 267

To switch from k to an arbitrary element k, we introduce the following contravariant transformation between the vector function v = (v1, v2) defined on K and v = (01,02) defined on k:

## chapter-03-section-04-pc00302 | equation | low | PDF 267

[[FORMULA:f-p0267-04275]]

## chapter-03-section-04-pc00303 | equation | low | PDF 267

[[FORMULA:f-p0267-04276]]

## chapter-03-section-04-pc00304 | ordinary-paragraph | medium | PDF 267

The choice of F, is justified by the fact that, roughly speaking, it preserves the divergence, curl and normal component:

## chapter-03-section-04-pc00305 | equation | low | PDF 267

[[FORMULA:f-p0267-04278]]

## chapter-03-section-04-pc00306 | equation | low | PDF 267

[[FORMULA:f-p0267-04279]]

## chapter-03-section-04-pc00307 | ordinary-paragraph | low | PDF 267

(Φ o F)(F-i v)· nds.

## chapter-03-section-04-pc00308 | equation | low | PDF 267

[[FORMULA:f-p0267-04280]]

## chapter-03-section-04-pc00309 | ordinary-paragraph | low | PDF 267

Jok Jor Then we fix I distinct points on each segment k' of I, and we set:

## chapter-03-section-04-pc00310 | ordinary-paragraph | low | PDF 267

Doh = {vhe L²(Q)²; vhlk = F,veD VkeJ, vn·nis continuous (resp. 0) at the I points of each interior (resp. boundary)

## chapter-03-section-04-pc00311 | equation | low | PDF 267

[[FORMULA:f-p0267-04282]]

## chapter-03-section-04-pc00312 | ordinary-paragraph | medium | PDF 267

segment k' of Ih}.

## chapter-03-section-04-pc00313 | ordinary-paragraph | medium | PDF 268

dictated by the above requirements and considerations. Clearly, we must choose

## chapter-03-section-04-pc00314 | equation | low | PDF 268

[[FORMULA:f-p0268-04283]]

## chapter-03-section-04-pc00315 | equation | low | PDF 268

[[FORMULA:f-p0268-04284]]

## chapter-03-section-04-pc00316 | ordinary-paragraph | medium | PDF 268

according that k is a triangle or a quadrilateral}. It follows immediately that:

## chapter-03-section-04-pc00317 | equation | low | PDF 268

[[FORMULA:f-p0268-04285]]

## chapter-03-section-04-pc00318 | equation | low | PDF 268

[[FORMULA:f-p0268-04286]]

## chapter-03-section-04-pc00319 | equation | low | PDF 268

[[FORMULA:f-p0268-04287]]

## chapter-03-section-04-pc00320 | remark | medium | PDF 268

Remark 4.5. When l = 1, the functions of Qh are constants in each k while the

## chapter-03-section-04-pc00321 | ordinary-paragraph | medium | PDF 268

functions of D have the form:

## chapter-03-section-04-pc00322 | equation | low | PDF 268

[[FORMULA:f-p0268-04289]]

## chapter-03-section-04-pc00323 | equation | low | PDF 268

[[FORMULA:f-p0268-04290]]

## chapter-03-section-04-pc00324 | ordinary-paragraph | medium | PDF 268

)if k is the unit square. From the degrees of freedom (4.62) we deduce a straightforward restriction operator t from H'(k) onto D: t is the unique polynomial of D that has the same degrees of freedom (4.62) on k as v. Then the transformation  yields the following restriction operator

## chapter-03-section-04-pc00325 | equation | low | PDF 268

[[FORMULA:f-p0268-04293]]

## chapter-03-section-04-pc00326 | equation | low | PDF 268

[[FORMULA:f-p0268-04294]]

## chapter-03-section-04-pc00327 | equation | low | PDF 268

[[FORMULA:f-p0268-04295]]

## chapter-03-section-04-pc00328 | ordinary-paragraph | medium | PDF 268

The operator T, satisfies Lemma II.1.1. More precisely, we have the following crucial result.

## chapter-03-section-04-pc00329 | theorem | medium | PDF 268

Theorem 4.4. If the triangulation J, is regular, the operator T, defined by (4.66)

## chapter-03-section-04-pc00330 | ordinary-paragraph | low | PDF 268

satisfies for all ve H1(Q)2: 1/2 + h-2/s /πnv - vllo,s,2 ≤ C(s)lvl1,2  Vs ≥ 2,

## chapter-03-section-04-pc00331 | equation | low | PDF 268

[[FORMULA:f-p0268-04298]]

## chapter-03-section-04-pc00332 | ordinary-paragraph | low | PDF 268

(xeTn

## chapter-03-section-04-pc00333 | equation | low | PDF 268

[[FORMULA:f-p0268-04299]]

## chapter-03-section-04-pc00334 | equation | low | PDF 268

[[FORMULA:f-p0268-04300]]

## chapter-03-section-04-pc00335 | ordinary-paragraph | medium | PDF 268

In addition, whatever the triangulation, we have:

## chapter-03-section-04-pc00336 | equation | low | PDF 268

[[FORMULA:f-p0268-04301]]

## chapter-03-section-04-pc00337 | equation | low | PDF 268

[[FORMULA:f-p0268-04302]]

## chapter-03-section-04-pc00338 | ordinary-paragraph | medium | PDF 268

Finally, when J, is made exclusively of triangles, the inequality (4.68) holds with C = 1 and no regularity requirement on Th.

## chapter-03-section-04-pc00339 | proof | medium | PDF 268

Proof. The properties (4.68) and (4.69) are an easy consequence of the definition

## chapter-03-section-04-pc00340 | ordinary-paragraph | medium | PDF 268,269

of π. (4.70) § = grad + curld where q is the solution of

## chapter-03-section-04-pc00341 | equation | low | PDF 269

[[FORMULA:f-p0269-04307]]

## chapter-03-section-04-pc00342 | ordinary-paragraph | high | PDF 269

Since k is convex, Theorem I.1.8 says that g ¢ H*(k) with

## chapter-03-section-04-pc00343 | equation | low | PDF 269

[[FORMULA:f-p0269-04308]]

## chapter-03-section-04-pc00344 | ordinary-paragraph | high | PDF 269

As a consequence we can find ¢ in H?(k) that satisfies (4.70) and

## chapter-03-section-04-pc00345 | ordinary-paragraph | high | PDF 269

Io? b/OX5N13,4 + 1078/03 18,

## chapter-03-section-04-pc00346 | equation | low | PDF 269

[[FORMULA:f-p0269-04310]]

## chapter-03-section-04-pc00347 | ordinary-paragraph | high | PDF 269

Thus a straightforward application of Theorem A.3 yields: (4.71) [#0 — G1. ¢< C5{ 00; /0%213,¢ + 1002/82, [2.¢ + diO1v2 e} *?, and a similar upper bound (with a different constant) for ||#¥ — ¥||o,,,.z- In view of (4.63) and the regularity of 7,, a simple calculation now leads to (4.67).

## chapter-03-section-04-pc00348 | theorem | high | PDF 269

Theorem 4.4 gives us the following inf-sup condition:

## chapter-03-section-04-pc00349 | ordinary-paragraph | high | PDF 269

for each q,€Q,, there exists v,€ Do, such that

## chapter-03-section-04-pc00350 | equation | low | PDF 269

[[FORMULA:f-p0269-04314]]

## chapter-03-section-04-pc00351 | ordinary-paragraph | high | PDF 269

and

## chapter-03-section-04-pc00352 | ordinary-paragraph | high | PDF 269

1/2

## chapter-03-section-04-pc00353 | equation | low | PDF 269

[[FORMULA:f-p0269-04315]]

## chapter-03-section-04-pc00354 | ordinary-paragraph | high | PDF 269

KeT,, With the spaces Do, and Q, we propose the following discretization of Problem (4.8):

## chapter-03-section-04-pc00355 | ordinary-paragraph | high | PDF 269

Find a function p,, in Q,, satisfying

## chapter-03-section-04-pc00356 | equation | low | PDF 269

[[FORMULA:f-p0269-04317]]

## chapter-03-section-04-pc00357 | ordinary-paragraph | high | PDF 269

Q Q (G72) +v) ‘|( Aj,)ij(Ov}i/0X;d) x — | Malia) tds]

## chapter-03-section-04-pc00358 | ordinary-paragraph | high | PDF 269

KeT;, * OK Vv,€ Dons where the tensor A, is related by (4.10) to the solution o, € %, of (4.20).

## chapter-03-section-04-pc00359 | ordinary-paragraph | high | PDF 269

Problem (4.20) can be solved independently of Problem (4.72), then owing Since

## chapter-03-section-04-pc00360 | ordinary-paragraph | high | PDF 269,270

Q,. to the above inf-sup condition Problem (4.72) has a unique solution p,, in Moreover, we have the following error estimate: regular triangulation of Q. If the solution (u, p) of the Stokes Problem (2.1) has the regularity: ue H**1(Q)?, pe H*(Q)N L3(Q) for some ke [1,1], then the solution p, of Problem (4.72) satisfies the error estimate: (4.73) IP — Palloa < Ch*{|Uls1,0 + |Pli,a}-

## chapter-03-section-04-pc00361 | proof | high | PDF 270

Proof. In view of (4.10), for each q, in Q, we have:

## chapter-03-section-04-pc00362 | equation | low | PDF 270

[[FORMULA:f-p0270-04325]]

## chapter-03-section-04-pc00363 | ordinary-paragraph | high | PDF 270

Q 1/2 te Vie rllo.a( Ss alt] KET, + v||M,(o — o)llo,7,S(O¥lDln o,°7;, - Then, according to the inf-sup condition, we can choose v, in Do, such that Gn Palo, a <Cy{Ndn — Plloe + VIG — Allo, 2} dn — Prllo,e + v||M,(o — o%) lon, SW" Ollo,r,- It remains to estimate S(v,:t). To this end, we use the fact that Vi — Tl,V with divv =q,— Ph |Vl1,@< Call—a Panll o,a; ve Hg (Q). Since S(v-t) = 0 we can write

## chapter-03-section-04-pc00364 | ordinary-paragraph | high | PDF 270

Hence the argument of Theorem 4.4 gives: IS(Vn* Olloe S CaP) van 00; /0%2|lo,0 + |062/0%4 llo,4 + I|d iv #5, eSa re. Therefore

## chapter-03-section-04-pc00365 | equation | low | PDF 270

[[FORMULA:f-p0270-04330]]

## chapter-03-section-04-pc00366 | ordinary-paragraph | high | PDF 270

and consequently,

## chapter-03-section-04-pc00367 | equation | low | PDF 270

[[FORMULA:f-p0270-04331]]

## chapter-03-section-04-pc00368 | ordinary-paragraph | high | PDF 270

Then (4.73) follows from (4.43) and Lemma A.5 or (A.51). Observe that just (4.43) requires the uniformity of 7,,. Gl

## chapter-03-section-04-pc00369 | remark | high | PDF 270

Remark 4.6. It is also possible to associate this discontinuous approximation of

## chapter-03-section-04-pc00370 | ordinary-paragraph | high | PDF 270

the pressure with the “stream function-vorticity” scheme studied in §2. The discrete version of the first equation (2.13) is:

## chapter-03-section-04-pc00371 | equation | low | PDF 270

[[FORMULA:f-p0270-04335]]

## chapter-03-section-04-pc00372 | ordinary-paragraph | high | PDF 270

(4.74) (Pp, div v,) = v(curl@,,v,) — (f,v,) Vv, Don.
