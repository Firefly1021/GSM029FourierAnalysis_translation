# Paragraph candidates: frontmatter

> Unreviewed candidates. Formula placeholders and every OCR uncertainty require source-image review.

## frontmatter-pc00001 | ordinary-paragraph | high | PDF 9

The material covered by this book has been taught by one of the authors in a post-graduate course on Numerical Analysis at the University Pierre et Marie Curie of Paris. It is an extended version of a previous text (cf. Girault & Raviart [32]) published in 1979 by Springer-Verlag in its series: Lecture Notes in Mathematics.

## frontmatter-pc00002 | ordinary-paragraph | high | PDF 9

In the last decade, many engineers and mathematicians have concentrated their efforts on the finite element solution of the Navier-Stokes equations for incompressible flows. The purpose of this book is to provide a fairly comprehensive treatment of the most recent developments in that field. To stay within reasonable bounds, we have restricted ourselves to the case of stationary problems although the time-dependent problems are of fundamental importance. This topic is currently evolving rapidly and we feel that it deserves to be covered by another specialized monograph. We have tried, to the best of our ability, to present a fairly exhaustive treatment of the finite element methods for inner flows. On the other hand however, we have entirely left out the subject of exterior problems which involve radically different techniques, both from a theoretical and from a practical point of view. Also, we have neither discussed the implementation of the finite element methods presented by this book, nor given any explicit numerical result. This field is extensively covered by Peyret & Taylor [64] and Thomasset [82]. Finally, we have tried as much as possible to make this text self-contained and therefore we have either proved or recalled all the theoretical results required.

## frontmatter-pc00003 | ordinary-paragraph | high | PDF 9

This book is divided into four chapters and a technical appendix. The first chapter is devoted to the theoretical aspects of the Stokes equations for an incompressible fluid flow. It includes a thoroughly complete, detailed and mostly original study of the function spaces H(div; 2) and H(curl; 2) closely associated with the Stokes problem. In particular, the reader will find here a fundamental decomposition of vector fields in two and three dimensions. The existence and uniqueness of the solution of the Stokes problem are fully proved. Finally, a number of algorithms to dissociate the velocity from the pressure are introduced.

## frontmatter-pc00004 | chapter | high | PDF 9

Chapter I deals with the finite element approximation oft he Stokes problem

## frontmatter-pc00005 | ordinary-paragraph | high | PDF 9,10

in the primitive variables (velocity and pressure). It can serve as a good introduction to the subject of mixed finite element methods, which plays an important methods available in this context and introduces some new three-dimensional elements. An original feature of this chapter is that it provides a unified treatment of the so-called B.B. compatibility condition between the velocity and pressure spaces. Although the finite element methods of Chapter II are the most popular, they do not satisfy exactly the incompressibility condition. On the contrary, Chapter III is devoted to the study of exactly incompressible finite element methods. It solves the Stokes problem using other variables such as the stream function and the vorticity or the stream function and the gradient of velocity tensor in two dimensions or even the vector potential and the vorticity in three dimensions. This chapter provides a number of useful and (seldom known) techniques for analyzing accurately these finite element schemes. Such techniques are not restricted to the Stokes problem but may be adapted to other mechanical situations like the bending of plates in elasticity.

## frontmatter-pc00006 | chapter | high | PDF 10

Chapter IV is devoted to the theory and approximation of the full Navier-

## frontmatter-pc00007 | ordinary-paragraph | high | PDF 10

Stokes problem. The existence and uniqueness theorems are entirely standard but the approximation is presented in a fairly new light. Its originality consists in extending systematically the results of the previous two chapters to this nonlinear situation. The basic result is a general theorem concerning the approximation of branches of nonsingular solutions of nonlinear problems. When it is applied to the Navier-Stokes equations, it enables one to recover optimal rates of convergence. We end this chapter by describing a number of useful algorithms for handling the Navier-Stokes nonlinearity. Finally, the appendix presents an up-to-date summary of the finite element theory which is constantly used throughout this book. We wish to thank our colleagues C. Bernardi, M. Crouzeix, O. Pironneau, G. Raugel and L. Tartar for many fruitful and exciting discussions. We are particularly grateful to R. Verfiirth for reading the manuscript and providing very helpful suggestions. For the material preparation of this work, we are above all gratefully indebted to our colleagues of the Computing Science Department who provided the microcomputer with which the manuscript was typed. We thank also Mme. Ruprechts for typing a part of the manuscript.

## frontmatter-pc00008 | ordinary-paragraph | high | PDF 10

Paris, March 1986 Vivette Girault Pierre-Arnaud Raviart

## frontmatter-pc00009 | chapter | high | PDF 11

Chapter I. Mathematical Foundation of the Stokes Problem...........

## frontmatter-pc00010 | section | high | PDF 11

§1. Generalities on Some Elliptic Boundary Value Problems .........

## frontmatter-pc00011 | ordinary-paragraph | high | PDF 11

EL. Basic ONCEDIS.OM SODOICY Spaces. 4 aeAeah een ene aah 1:2; FAD StraC tae LLIDUCMINCORY pau mete tie hear ee Ae cb, eae al 13: Example 1: Dirichlet’s Problem for the Laplace Operator.........

## frontmatter-pc00012 | subsection | high | PDF 11

1.4. Example 2: Neumann’s Problem for the Laplace Operator........

## frontmatter-pc00013 | ordinary-paragraph | high | PDF 11

is Example 3: Dirichlet’s Problem for the Biharmonic Operator .....

## frontmatter-pc00014 | section | high | PDF 11

§ 2. Punetionss paces 101. the stokes Problem) tm. eyes verge3 s

## frontmatter-pc00015 | ordinary-paragraph | high | PDF 11

DA COLINA D ye SUILS are Neier een Ida Oana eas loa baa ets igh Some Properties of Spaces Related to the Divergence Operator ... ee Some Properties of Spaces Related to the Curl Operator.........

## frontmatter-pc00016 | section | high | PDF 11

§3. AMDECOMIDOSILION Ol VCCLOL PICIOS yn at i cyte) s centre cre eee

## frontmatter-pc00017 | ordinary-paragraph | high | PDF 11

S31: Decomposition of Two-Dimensional Vector Fields.............. SEP Application to the Regularity of Functions of H(div; 2) H (curl; Q) Sop Decomposition of Three-Dimensional Vector Fields.............

## frontmatter-pc00018 | subsection | high | PDF 11

3.4. The Imbedding of H(div; 2) Ho(curl; Q) into H1(Q)?--

## frontmatter-pc00019 | subsection | high | PDF 11

3.5. The Imbedding of H,(div; 2)N H(curl; Q) into H'(Q)?)-- >

## frontmatter-pc00020 | section | high | PDF 11

§4. Analysis of an Abstract Variational Problem ...................

## frontmatter-pc00021 | subsection | high | PDF 11

4.1. PGGFOTiCTAl RC SULE men wai ee e at erste cece Ie eae toh Ae

## frontmatter-pc00022 | subsection | high | PDF 11

4.2. AySaddle- PoimhA Pproachisncin <ite fs ool Chien smal o4 AeE

## frontmatter-pc00023 | subsection | high | PDF 11

4.3. Approximation by Regularization or Penalty...................

## frontmatter-pc00024 | subsection | high | PDF 11

4.4. Mterativeamiet nods Ob Gradients ly pene sire eeucoetoe 0s clue ean es

## frontmatter-pc00025 | ordinary-paragraph | high | PDF 11,12

IBY PDH eastOke ss eat OMS eri oh cAe nosey morte eines are sie vie ol bait acties pals The Dirichlet Problem in the Velocity-Pressure Formulation ..... BZ, The Stream Function Formulation of the Dirichlet Problem in Two AB TINCTASTOLL G et aN este pati a URINE RERUN cata eRe ae 88 5:3; ‘TENS Tilp eReOslD rtanverynoGen l (GAINS. ss 60ndbocodgonunbouvosugupeoonds 90 Ale Triangular Finite Blements eae cree erect teen et ere ee 95 A» Quadrilateral Finite Elements aay cr ener teteraee n 104 A.3. Interpolation of Discontinuous Functions ...............++++-- 109

## frontmatter-pc00026 | chapter | high | PDF 12

Chapter II. Numerical Solution of the Stokes Problem in the Primitive

## frontmatter-pc00027 | ordinary-paragraph | high | PDF 12

NEGtT (eee a nr eres de MeaP eC eR era den tear ce 9 0005 112 SilieGeneral Approximation yc ace ered ee trae ee teers 112 i iwAn A bstract:A pproximation Result sr eee rt? 12" Decoupling the Computationiol ip and 7yr es. eee 120

## frontmatter-pc00028 | subsection | high | PDF 12

1.3. Application to the Homogeneous Stokes Problem............... 123

## frontmatter-pc00029 | ordinary-paragraph | high | PDF 12

4 Checkine the int-sup Comdition = 3h es ie eee eee ee 129

## frontmatter-pc00030 | section | high | PDF 12

§2. Simplicial Finite Element Methods Using Discontinuous Pressures. . 132

## frontmatter-pc00031 | subsection | high | PDF 12

2.1. A First Order Approximation on Triangular Elements........... 133

## frontmatter-pc00032 | subsection | high | PDF 12

2.2. Higher-Order Approximation on Triangular Elements........... 139

## frontmatter-pc00033 | subsection | high | PDF 12

2.3. The Three-Dimensional case: First and Higher-Order Schemes. ... 144

## frontmatter-pc00034 | section | high | PDF 12

§3. Quadrilateral Finite Element Methods Using Discontinuous Pres-

## frontmatter-pc00035 | ordinary-paragraph | high | PDF 12

152 saleeA quadrilateral Finite Blementiol Order One. ae ees 152 Sve viicher-Order OuadnilateraleBlements aucno.e gccrnea-s 156

## frontmatter-pc00036 | subsection | high | PDF 12

3.3. An Example of Checkerboard Instability: the Q, — Py Element.... 160

## frontmatter-pc00037 | subsection | high | PDF 12

3.4. Error Estimates for the 9, — P, Element 170

## frontmatter-pc00038 | section | high | PDF 12

§4. Continuous Approximation of the Pressure Las

## frontmatter-pc00039 | subsection | high | PDF 12

4.1. A First Order Method: the “Mini” Finite Element 174

## frontmatter-pc00040 | ordinary-paragraph | high | PDF 12

42. The Hood-Taylor’ Finite Blement’Method.., 25 +) see. ene ee 176

## frontmatter-pc00041 | subsection | high | PDF 12

4.3. The “Glowinski-Pironneau” Finite Element Method 183

## frontmatter-pc00042 | ordinary-paragraph | high | PDF 12

190

## frontmatter-pc00043 | chapter | high | PDF 12

Chapter III. Incompressible Mixed Finite Element Methods for Solving

## frontmatter-pc00044 | ordinary-paragraph | high | PDF 12

the Stokes Problem 193 193 193 196

## frontmatter-pc00045 | section | high | PDF 12

§2. The “Stream Function-Vorticity-Pressure” Method for the Stokes

## frontmatter-pc00046 | ordinary-paragraph | high | PDF 12

Problem in Two Dimensions 198

## frontmatter-pc00047 | subsection | high | PDF 12

2.1. A Mixed Formulation 199

## frontmatter-pc00048 | ordinary-paragraph | high | PDF 13

EDC RUCCR Ee erate de Petes Marton sath iS ¥.us'rs Liseeed BR san bcar oar

## frontmatter-pc00049 | subsection | high | PDF 13

2.3. The Technique of Mesh-Dependent Norms

## frontmatter-pc00050 | section | high | PDF 13

§3. Further Topics on the “Stream Function-Vorticity-Pressure” Scheme

## frontmatter-pc00051 | ordinary-paragraph | high | PDF 13

Sriercciinement Ol the error ANAlysis nc 6 a)4)eh dc.,e Bee es

## frontmatter-pc00052 | subsection | high | PDF 13

3.2. Super Convergence Using Quadrilateral Finite Elements of Degree |

## frontmatter-pc00053 | section | high | PDF 13

§4. A “Stream Function-Gradient of Velocity Tensor” Method in Two

## frontmatter-pc00054 | ordinary-paragraph | high | PDF 13

DyC HSIOMS Er eee yee eee Gaetan Mine Oe ac eee

## frontmatter-pc00055 | subsection | high | PDF 13

4.1. The Hellan-Herrmann-Johnson Formulation...................

## frontmatter-pc00056 | subsection | high | PDF 13

4.2. Approximation with Triangular Finite Elements of Degree! ......

## frontmatter-pc00057 | subsection | high | PDF 13

4.3. Additional Results for the Hellan-Herrmann-Johnson Scheme ....

## frontmatter-pc00058 | subsection | high | PDF 13

4.4. Discontinuous Approximation of the Pressure..................

## frontmatter-pc00059 | section | high | PDF 13

§5. A “Vector Potential-Vorticity” Scheme in Three Dimensions......

## frontmatter-pc00060 | subsection | high | PDF 13

5.1. A Mixed Formulation of the Three-Dimensional Stokes Problem...

## frontmatter-pc00061 | ordinary-paragraph | high | PDF 13

Sy eviixed Approximation ini (curl OQ) 8. 6. hn ne ses ow Reems

## frontmatter-pc00062 | subsection | high | PDF 13

5.3. A Family of Conforming Finite Elements in H(curl;Q)...........

## frontmatter-pc00063 | ordinary-paragraph | high | PDF 13

oa. Error Analysis ior Finite Elements of Degree]... once on 5). Discontinuous: Approximation of the Pressure, =... 522. 2.4.3--.-

## frontmatter-pc00064 | chapter | high | PDF 13

Chapter IV. Theory and Approximation of the Navier-Stokes Problem. .

## frontmatter-pc00065 | ordinary-paragraph | high | PDF 13

SH ARG ASS OMN ONUNCATILODICING het ys os Ae ot ol eee eee

## frontmatter-pc00066 | section | high | PDF 13

§2. Theory of the Steady-State Navier-Stokes Equations.............

## frontmatter-pc00067 | subsection | high | PDF 13

2.1. The Dirichlet Problem in the Velocity-Pressure Formulation .....

## frontmatter-pc00068 | subsection | high | PDF 13

2.2. The Stream Function Formulation of the Homogeneous Problem .

## frontmatter-pc00069 | section | high | PDF 13

§3. Approximation of Branches of Nonsingular Solutions............

## frontmatter-pc00070 | ordinary-paragraph | high | PDF 13

Bile AtivA Dsttact Pranic WOT K sya: nk lore sans aah sis rete wiv anes

## frontmatter-pc00071 | subsection | high | PDF 13

3.2. Approximation of Branches of Nonsingular Solutions ...........

## frontmatter-pc00072 | ordinary-paragraph | high | PDF 13

Sew A pplication to a Class of Nonlinear Problems\. 1.3.0.2ens «

## frontmatter-pc00073 | subsection | high | PDF 13

3.4. Non-Differentiable Approximation of Branches of Nonsingular

## frontmatter-pc00074 | ordinary-paragraph | high | PDF 13

SO UILOL IS rere acai. enya eee akt ere was 8 patches Seeeicuke eA Boa uae

## frontmatter-pc00075 | section | high | PDF 13

§4. Numerical Analysis of Centered Finite Element Schemes .........

## frontmatter-pc00076 | subsection | high | PDF 13

4.1. Formulation in Primitive Variables: Methods Using Discontinuous

## frontmatter-pc00077 | ordinary-paragraph | high | PDF 13

GESSUITCS Caen Wer ee ee ee ee ee tee ON wae aca te urea 42. Formulation in Primitive Variables: the Case of Continuous Besa is eee ee ie teas ic Bea a ad ra Na igi Ba Pontsj sU i a ee avo eas A Na a

## frontmatter-pc00078 | subsection | high | PDF 13

4.3. Mixed Incompressible Methods: the “Stream Function-Vorticity”

## frontmatter-pc00079 | ordinary-paragraph | high | PDF 13

GLIA LIONS ny eet cae net trccheen sera tee catilieinstcks th, A tiara ee Spa]

## frontmatter-pc00080 | subsection | high | PDF 13

4.4. Remarks on the “Stream Function-Gradient of Velocity Tensor”

## frontmatter-pc00081 | ordinary-paragraph | medium | PDF 13,14

S111 Cae Re tre teres RP wR eS rok ete Neo tise alta aces aah 334 336

## frontmatter-pc00082 | subsection | medium | PDF 14

5.1. Upwinding in the Stream Function-Vorticity Scheme .

## frontmatter-pc00083 | ordinary-paragraph | medium | PDF 14

340

## frontmatter-pc00084 | subsection | medium | PDF 14

5.2. Error Analysis of the Upwind Scheme. . .

## frontmatter-pc00085 | ordinary-paragraph | medium | PDF 14

350

## frontmatter-pc00086 | subsection | medium | PDF 14

5.3. Approximating the Pressure with the Upwind Scheme .

## frontmatter-pc00087 | ordinary-paragraph | medium | PDF 14

352

## frontmatter-pc00088 | section | medium | PDF 14

§6. Numerical Algorithms . 

## frontmatter-pc00089 | ordinary-paragraph | medium | PDF 14

352

## frontmatter-pc00090 | subsection | medium | PDF 14

6.1. General Methods of Descent and Application to Gradient Methods

## frontmatter-pc00091 | subsection | medium | PDF 14

6.2. Least-Squares and Gradient Methods to Solve the Navier-Stokes

## frontmatter-pc00092 | ordinary-paragraph | medium | PDF 14

357 Equations ..: 362

## frontmatter-pc00093 | subsection | medium | PDF 14

6.3. Newton's Method and the Continuation Method 

## frontmatter-pc00094 | ordinary-paragraph | medium | PDF 14

368 References.. Index of Mathematical Symbols . 372 373 Subject Index..
