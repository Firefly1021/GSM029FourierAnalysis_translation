# Restored-source review candidate: frontmatter



> This file is reconstructed from scan OCR and remains subject to source-image and formula review.



## PDF 9 / printed v



[p0009-b0002 | ordinary-paragraph | high] The material covered by this book has been taught by one of the authors in a

[p0009-b0003 | ordinary-paragraph | high] post-graduate course on Numerical Analysis at the University Pierre et Marie

[p0009-b0004 | ordinary-paragraph | high] Curie of Paris. It is an extended version of a previous text (cf. Girault & Raviart

[p0009-b0005 | ordinary-paragraph | high] [32]) published in 1979 by Springer-Verlag in its series: Lecture Notes in

[p0009-b0006 | ordinary-paragraph | high] Mathematics.

[p0009-b0007 | ordinary-paragraph | high] In the last decade, many engineers and mathematicians have concentrated

[p0009-b0008 | ordinary-paragraph | high] their efforts on the finite element solution of the Navier-Stokes equations for

[p0009-b0009 | ordinary-paragraph | high] incompressible flows. The purpose of this book is to provide a fairly comprehen-

[p0009-b0010 | ordinary-paragraph | high] sive treatment of the most recent developments in that field. To stay within

[p0009-b0011 | ordinary-paragraph | high] reasonable bounds, we have restricted ourselves to the case of stationary prob-

[p0009-b0012 | ordinary-paragraph | high] lems although the time-dependent problems are of fundamental importance.

[p0009-b0013 | ordinary-paragraph | high] This topic is currently evolving rapidly and we feel that it deserves to be covered

[p0009-b0014 | ordinary-paragraph | high] by another specialized monograph. We have tried, to the best of our ability,

[p0009-b0015 | ordinary-paragraph | high] to present a fairly exhaustive treatment of the finite element methods for inner

[p0009-b0016 | ordinary-paragraph | high] flows. On the other hand however, we have entirely left out the subject of exterior

[p0009-b0017 | ordinary-paragraph | high] problems which involve radically different techniques, both from a theoretical

[p0009-b0018 | ordinary-paragraph | high] and from a practical point of view. Also, we have neither discussed the implemen-

[p0009-b0019 | ordinary-paragraph | high] tation of the finite element methods presented by this book, nor given any explicit

[p0009-b0020 | ordinary-paragraph | high] numerical result. This field is extensively covered by Peyret & Taylor [64] and

[p0009-b0021 | ordinary-paragraph | high] Thomasset [82]. Finally, we have tried as much as possible to make this text

[p0009-b0022 | ordinary-paragraph | high] self-contained and therefore we have either proved or recalled all the theoretical

[p0009-b0023 | ordinary-paragraph | high] results required.

[p0009-b0024 | ordinary-paragraph | high] This book is divided into four chapters and a technical appendix. The first

[p0009-b0025 | ordinary-paragraph | high] chapter is devoted to the theoretical aspects of the Stokes equations for an

[p0009-b0026 | ordinary-paragraph | high] incompressible fluid flow. It includes a thoroughly complete, detailed and mostly

[p0009-b0027 | ordinary-paragraph | high] original study of the function spaces H(div; 2) and H(curl; 2) closely associated

[p0009-b0028 | ordinary-paragraph | high] with the Stokes problem. In particular, the reader will find here a fundamental

[p0009-b0029 | ordinary-paragraph | high] decomposition of vector fields in two and three dimensions. The existence and

[p0009-b0030 | ordinary-paragraph | high] uniqueness of the solution of the Stokes problem are fully proved. Finally, a

[p0009-b0031 | ordinary-paragraph | high] number of algorithms to dissociate the velocity from the pressure are introduced.

[p0009-b0032 | chapter | high] Chapter I deals with the finite element approximation oft he Stokes problem

[p0009-b0033 | ordinary-paragraph | high] in the primitive variables (velocity and pressure). It can serve as a good introduc-

[p0009-b0034 | ordinary-paragraph | high] tion to the subject of mixed finite element methods, which plays an important

## PDF 10 / printed vi



[p0010-b0004 | ordinary-paragraph | high] methods available in this context and introduces some new three-dimensional

[p0010-b0005 | ordinary-paragraph | high] elements. An original feature of this chapter is that it provides a unified treatment

[p0010-b0006 | ordinary-paragraph | high] of the so-called B.B. compatibility condition between the velocity and pressure

[p0010-b0007 | ordinary-paragraph | high] spaces.

[p0010-b0008 | ordinary-paragraph | high] Although the finite element methods of Chapter II are the most popular, they

[p0010-b0009 | ordinary-paragraph | high] do not satisfy exactly the incompressibility condition. On the contrary, Chapter

[p0010-b0010 | ordinary-paragraph | high] III is devoted to the study of exactly incompressible finite element methods. It

[p0010-b0011 | ordinary-paragraph | high] solves the Stokes problem using other variables such as the stream function and

[p0010-b0012 | ordinary-paragraph | high] the vorticity or the stream function and the gradient of velocity tensor in two

[p0010-b0013 | ordinary-paragraph | high] dimensions or even the vector potential and the vorticity in three dimensions.

[p0010-b0014 | ordinary-paragraph | high] This chapter provides a number of useful and (seldom known) techniques for

[p0010-b0015 | ordinary-paragraph | high] analyzing accurately these finite element schemes. Such techniques are not re-

[p0010-b0016 | ordinary-paragraph | high] stricted to the Stokes problem but may be adapted to other mechanical situations

[p0010-b0017 | ordinary-paragraph | high] like the bending of plates in elasticity.

[p0010-b0018 | chapter | high] Chapter IV is devoted to the theory and approximation of the full Navier-

[p0010-b0019 | ordinary-paragraph | high] Stokes problem. The existence and uniqueness theorems are entirely standard

[p0010-b0020 | ordinary-paragraph | high] but the approximation is presented in a fairly new light. Its originality consists in

[p0010-b0021 | ordinary-paragraph | high] extending systematically the results of the previous two chapters to this nonlinear

[p0010-b0022 | ordinary-paragraph | high] situation. The basic result is a general theorem concerning the approximation of

[p0010-b0023 | ordinary-paragraph | high] branches of nonsingular solutions of nonlinear problems. When it is applied to

[p0010-b0024 | ordinary-paragraph | high] the Navier-Stokes equations, it enables one to recover optimal rates of conver-

[p0010-b0025 | ordinary-paragraph | high] gence. We end this chapter by describing a number of useful algorithms for

[p0010-b0026 | ordinary-paragraph | high] handling the Navier-Stokes nonlinearity.

[p0010-b0027 | ordinary-paragraph | high] Finally, the appendix presents an up-to-date summary of the finite element

[p0010-b0028 | ordinary-paragraph | high] theory which is constantly used throughout this book.

[p0010-b0029 | ordinary-paragraph | high] We wish to thank our colleagues C. Bernardi, M. Crouzeix, O. Pironneau,

[p0010-b0030 | ordinary-paragraph | high] G. Raugel and L. Tartar for many fruitful and exciting discussions. We are

[p0010-b0031 | ordinary-paragraph | high] particularly grateful to R. Verfiirth for reading the manuscript and providing

[p0010-b0032 | ordinary-paragraph | high] very helpful suggestions. For the material preparation of this work, we are above

[p0010-b0033 | ordinary-paragraph | high] all gratefully indebted to our colleagues of the Computing Science Department

[p0010-b0034 | ordinary-paragraph | high] who provided the microcomputer with which the manuscript was typed. We

[p0010-b0035 | ordinary-paragraph | high] thank also Mme. Ruprechts for typing a part of the manuscript.

[p0010-b0036 | ordinary-paragraph | high] Paris, March 1986 Vivette Girault

[p0010-b0037 | ordinary-paragraph | high] Pierre-Arnaud Raviart

## PDF 11 / printed vii



[p0011-b0002 | chapter | high] Chapter I. Mathematical Foundation of the Stokes Problem...........

[p0011-b0003 | section | high] §1. Generalities on Some Elliptic Boundary Value Problems .........

[p0011-b0004 | ordinary-paragraph | high] EL. Basic ONCEDIS.OM SODOICY Spaces. 4 aeAeah een ene aah

[p0011-b0005 | ordinary-paragraph | high] 1:2; FAD StraC tae LLIDUCMINCORY pau mete tie hear ee Ae cb, eae al

[p0011-b0006 | ordinary-paragraph | high] 13: Example 1: Dirichlet’s Problem for the Laplace Operator.........

[p0011-b0007 | subsection | high] 1.4. Example 2: Neumann’s Problem for the Laplace Operator........

[p0011-b0008 | ordinary-paragraph | high] is Example 3: Dirichlet’s Problem for the Biharmonic Operator .....

[p0011-b0009 | section | high] § 2. Punetionss paces 101. the stokes Problem) tm. eyes verge3 s

[p0011-b0010 | ordinary-paragraph | high] DA COLINA D ye SUILS are Neier een Ida Oana eas loa baa ets

[p0011-b0011 | ordinary-paragraph | high] igh Some Properties of Spaces Related to the Divergence Operator ...

[p0011-b0012 | ordinary-paragraph | high] ee Some Properties of Spaces Related to the Curl Operator.........

[p0011-b0013 | section | high] §3. AMDECOMIDOSILION Ol VCCLOL PICIOS yn at i cyte) s centre cre eee

[p0011-b0014 | ordinary-paragraph | high] S31: Decomposition of Two-Dimensional Vector Fields..............

[p0011-b0015 | ordinary-paragraph | high] SEP Application to the Regularity of Functions of H(div; 2) H (curl; Q)

[p0011-b0016 | ordinary-paragraph | high] Sop Decomposition of Three-Dimensional Vector Fields.............

[p0011-b0017 | subsection | high] 3.4. The Imbedding of H(div; 2) Ho(curl; Q) into H1(Q)?--

[p0011-b0018 | subsection | high] 3.5. The Imbedding of H,(div; 2)N H(curl; Q) into H'(Q)?)-- >

[p0011-b0019 | section | high] §4. Analysis of an Abstract Variational Problem ...................

[p0011-b0020 | subsection | high] 4.1. PGGFOTiCTAl RC SULE men wai ee e at erste cece Ie eae toh Ae

[p0011-b0021 | subsection | high] 4.2. AySaddle- PoimhA Pproachisncin <ite fs ool Chien smal o4 AeE

[p0011-b0022 | subsection | high] 4.3. Approximation by Regularization or Penalty...................

[p0011-b0023 | subsection | high] 4.4. Mterativeamiet nods Ob Gradients ly pene sire eeucoetoe 0s clue ean es

[p0011-b0024 | ordinary-paragraph | high] IBY PDH eastOke ss eat OMS eri oh cAe nosey morte eines are sie vie ol bait acties

[p0011-b0025 | ordinary-paragraph | high] pals The Dirichlet Problem in the Velocity-Pressure Formulation .....

[p0011-b0026 | ordinary-paragraph | high] BZ, The Stream Function Formulation of the Dirichlet Problem in Two

[p0011-b0027 | ordinary-paragraph | high] AB TINCTASTOLL G et aN este pati a URINE RERUN cata eRe ae 88

[p0011-b0028 | ordinary-paragraph | high] 5:3; ‘TENS Tilp eReOslD rtanverynoGen l (GAINS. ss 60ndbocodgonunbouvosugupeoonds 90

## PDF 12 / printed viii



[p0012-b0003 | ordinary-paragraph | high] Ale Triangular Finite Blements eae cree erect teen et ere ee 95

[p0012-b0004 | ordinary-paragraph | high] A» Quadrilateral Finite Elements aay cr ener teteraee n 104

[p0012-b0005 | ordinary-paragraph | high] A.3. Interpolation of Discontinuous Functions ...............++++-- 109

[p0012-b0006 | chapter | high] Chapter II. Numerical Solution of the Stokes Problem in the Primitive

[p0012-b0007 | ordinary-paragraph | high] NEGtT (eee a nr eres de MeaP eC eR era den tear ce 9 0005 112

[p0012-b0008 | ordinary-paragraph | high] SilieGeneral Approximation yc ace ered ee trae ee teers 112

[p0012-b0009 | ordinary-paragraph | high] i iwAn A bstract:A pproximation Result sr eee rt?

[p0012-b0010 | ordinary-paragraph | high] 12" Decoupling the Computationiol ip and 7yr es. eee 120

[p0012-b0011 | subsection | high] 1.3. Application to the Homogeneous Stokes Problem............... 123

[p0012-b0012 | ordinary-paragraph | high] 4 Checkine the int-sup Comdition = 3h es ie eee eee ee 129

[p0012-b0013 | section | high] §2. Simplicial Finite Element Methods Using Discontinuous Pressures. . 132

[p0012-b0014 | subsection | high] 2.1. A First Order Approximation on Triangular Elements........... 133

[p0012-b0015 | subsection | high] 2.2. Higher-Order Approximation on Triangular Elements........... 139

[p0012-b0016 | subsection | high] 2.3. The Three-Dimensional case: First and Higher-Order Schemes. ... 144

[p0012-b0017 | section | high] §3. Quadrilateral Finite Element Methods Using Discontinuous Pres-

[p0012-b0018 | ordinary-paragraph | high] 152

[p0012-b0019 | ordinary-paragraph | high] saleeA quadrilateral Finite Blementiol Order One. ae ees 152

[p0012-b0020 | ordinary-paragraph | high] Sve viicher-Order OuadnilateraleBlements aucno.e gccrnea-s 156

[p0012-b0021 | subsection | high] 3.3. An Example of Checkerboard Instability: the Q, — Py Element.... 160

[p0012-b0022 | subsection | high] 3.4. Error Estimates for the 9, — P, Element 170

[p0012-b0023 | section | high] §4. Continuous Approximation of the Pressure Las

[p0012-b0024 | subsection | high] 4.1. A First Order Method: the “Mini” Finite Element 174

[p0012-b0025 | ordinary-paragraph | high] 42. The Hood-Taylor’ Finite Blement’Method.., 25 +) see. ene ee 176

[p0012-b0026 | subsection | high] 4.3. The “Glowinski-Pironneau” Finite Element Method 183

[p0012-b0027 | ordinary-paragraph | high] 190

[p0012-b0028 | chapter | high] Chapter III. Incompressible Mixed Finite Element Methods for Solving

[p0012-b0029 | ordinary-paragraph | high] the Stokes Problem 193

[p0012-b0030 | ordinary-paragraph | high] 193

[p0012-b0031 | ordinary-paragraph | high] 193

[p0012-b0032 | ordinary-paragraph | high] 196

[p0012-b0033 | section | high] §2. The “Stream Function-Vorticity-Pressure” Method for the Stokes

[p0012-b0034 | ordinary-paragraph | high] Problem in Two Dimensions 198

[p0012-b0035 | subsection | high] 2.1. A Mixed Formulation 199

## PDF 13 / printed ix



[p0013-b0003 | ordinary-paragraph | high] EDC RUCCR Ee erate de Petes Marton sath iS ¥.us'rs Liseeed BR san bcar oar

[p0013-b0004 | subsection | high] 2.3. The Technique of Mesh-Dependent Norms

[p0013-b0005 | section | high] §3. Further Topics on the “Stream Function-Vorticity-Pressure” Scheme

[p0013-b0006 | ordinary-paragraph | high] Sriercciinement Ol the error ANAlysis nc 6 a)4)eh dc.,e Bee es

[p0013-b0007 | subsection | high] 3.2. Super Convergence Using Quadrilateral Finite Elements of Degree |

[p0013-b0008 | section | high] §4. A “Stream Function-Gradient of Velocity Tensor” Method in Two

[p0013-b0009 | ordinary-paragraph | high] DyC HSIOMS Er eee yee eee Gaetan Mine Oe ac eee

[p0013-b0010 | subsection | high] 4.1. The Hellan-Herrmann-Johnson Formulation...................

[p0013-b0011 | subsection | high] 4.2. Approximation with Triangular Finite Elements of Degree! ......

[p0013-b0012 | subsection | high] 4.3. Additional Results for the Hellan-Herrmann-Johnson Scheme ....

[p0013-b0013 | subsection | high] 4.4. Discontinuous Approximation of the Pressure..................

[p0013-b0014 | section | high] §5. A “Vector Potential-Vorticity” Scheme in Three Dimensions......

[p0013-b0015 | subsection | high] 5.1. A Mixed Formulation of the Three-Dimensional Stokes Problem...

[p0013-b0016 | ordinary-paragraph | high] Sy eviixed Approximation ini (curl OQ) 8. 6. hn ne ses ow Reems

[p0013-b0017 | subsection | high] 5.3. A Family of Conforming Finite Elements in H(curl;Q)...........

[p0013-b0018 | ordinary-paragraph | high] oa. Error Analysis ior Finite Elements of Degree]... once on

[p0013-b0019 | ordinary-paragraph | high] 5). Discontinuous: Approximation of the Pressure, =... 522. 2.4.3--.-

[p0013-b0020 | chapter | high] Chapter IV. Theory and Approximation of the Navier-Stokes Problem. .

[p0013-b0021 | ordinary-paragraph | high] SH ARG ASS OMN ONUNCATILODICING het ys os Ae ot ol eee eee

[p0013-b0022 | section | high] §2. Theory of the Steady-State Navier-Stokes Equations.............

[p0013-b0023 | subsection | high] 2.1. The Dirichlet Problem in the Velocity-Pressure Formulation .....

[p0013-b0024 | subsection | high] 2.2. The Stream Function Formulation of the Homogeneous Problem .

[p0013-b0025 | section | high] §3. Approximation of Branches of Nonsingular Solutions............

[p0013-b0026 | ordinary-paragraph | high] Bile AtivA Dsttact Pranic WOT K sya: nk lore sans aah sis rete wiv anes

[p0013-b0027 | subsection | high] 3.2. Approximation of Branches of Nonsingular Solutions ...........

[p0013-b0028 | ordinary-paragraph | high] Sew A pplication to a Class of Nonlinear Problems\. 1.3.0.2ens «

[p0013-b0029 | subsection | high] 3.4. Non-Differentiable Approximation of Branches of Nonsingular

[p0013-b0030 | ordinary-paragraph | high] SO UILOL IS rere acai. enya eee akt ere was 8 patches Seeeicuke eA Boa uae

[p0013-b0031 | section | high] §4. Numerical Analysis of Centered Finite Element Schemes .........

[p0013-b0032 | subsection | high] 4.1. Formulation in Primitive Variables: Methods Using Discontinuous

[p0013-b0033 | ordinary-paragraph | high] GESSUITCS Caen Wer ee ee ee ee ee tee ON wae aca te urea

[p0013-b0034 | ordinary-paragraph | high] 42. Formulation in Primitive Variables: the Case of Continuous

[p0013-b0035 | ordinary-paragraph | high] Besa is eee ee ie teas ic Bea a ad ra Na igi Ba Pontsj sU i a ee avo eas A Na a

[p0013-b0036 | subsection | high] 4.3. Mixed Incompressible Methods: the “Stream Function-Vorticity”

[p0013-b0037 | ordinary-paragraph | high] GLIA LIONS ny eet cae net trccheen sera tee catilieinstcks th, A tiara ee Spa]

[p0013-b0038 | subsection | high] 4.4. Remarks on the “Stream Function-Gradient of Velocity Tensor”

[p0013-b0039 | ordinary-paragraph | high] S111 Cae Re tre teres RP wR eS rok ete Neo tise alta aces aah 334

## PDF 14 / printed x



[p0014-b0005 | ordinary-paragraph | medium] 336

[p0014-b0006 | subsection | medium] 5.1. Upwinding in the Stream Function-Vorticity Scheme .

[p0014-b0007 | ordinary-paragraph | medium] 340

[p0014-b0008 | subsection | medium] 5.2. Error Analysis of the Upwind Scheme. . .

[p0014-b0009 | ordinary-paragraph | medium] 350

[p0014-b0010 | subsection | medium] 5.3. Approximating the Pressure with the Upwind Scheme .

[p0014-b0011 | ordinary-paragraph | medium] 352

[p0014-b0012 | section | medium] §6. Numerical Algorithms . 

[p0014-b0013 | ordinary-paragraph | medium] 352

[p0014-b0014 | subsection | medium] 6.1. General Methods of Descent and Application to Gradient Methods

[p0014-b0015 | subsection | medium] 6.2. Least-Squares and Gradient Methods to Solve the Navier-Stokes

[p0014-b0016 | ordinary-paragraph | medium] 357

[p0014-b0017 | ordinary-paragraph | medium] Equations ..:

[p0014-b0018 | ordinary-paragraph | medium] 362

[p0014-b0019 | subsection | medium] 6.3. Newton's Method and the Continuation Method 

[p0014-b0020 | ordinary-paragraph | medium] 368

[p0014-b0021 | ordinary-paragraph | medium] References..

[p0014-b0022 | ordinary-paragraph | medium] Index of Mathematical Symbols .

[p0014-b0023 | ordinary-paragraph | medium] 372

[p0014-b0024 | ordinary-paragraph | medium] 373

[p0014-b0025 | ordinary-paragraph | medium] Subject Index..
