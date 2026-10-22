# Preface

Review status: verified against the original scan.

Source provenance: PDF pages 9--10, printed pages v--vi, `workspace/pages/original/full-360dpi/page-009.png` and `page-010.png`. The table of contents on PDF pages 11--14 will be generated from the reviewed chapter and section headings and is not duplicated as body text.

## p0009-preface-001

The material covered by this book has been taught by one of the authors in a post-graduate course on Numerical Analysis at the University Pierre et Marie Curie of Paris. It is an extended version of a previous text (cf. Girault & Raviart [32]) published in 1979 by Springer-Verlag in its series: Lecture Notes in Mathematics.

## p0009-preface-002

In the last decade, many engineers and mathematicians have concentrated their efforts on the finite element solution of the Navier-Stokes equations for incompressible flows. The purpose of this book is to provide a fairly comprehensive treatment of the most recent developments in that field. To stay within reasonable bounds, we have restricted ourselves to the case of stationary problems although the time-dependent problems are of fundamental importance. This topic is currently evolving rapidly and we feel that it deserves to be covered by another specialized monograph. We have tried, to the best of our ability, to present a fairly exhaustive treatment of the finite element methods for inner flows. On the other hand however, we have entirely left out the subject of exterior problems which involve radically different techniques, both from a theoretical and from a practical point of view. Also, we have neither discussed the implementation of the finite element methods presented by this book, nor given any explicit numerical result. This field is extensively covered by Peyret & Taylor [64] and Thomasset [82]. Finally, we have tried as much as possible to make this text self-contained and therefore we have either proved or recalled all the theoretical results required.

## p0009-preface-003

This book is divided into four chapters and a technical appendix. The first chapter is devoted to the theoretical aspects of the Stokes equations for an incompressible fluid flow. It includes a thoroughly complete, detailed and mostly original study of the function spaces $H(\operatorname{div};\Omega)$ and $H(\operatorname{curl};\Omega)$ closely associated with the Stokes problem. In particular, the reader will find here a fundamental decomposition of vector fields in two and three dimensions. The existence and uniqueness of the solution of the Stokes problem are fully proved. Finally, a number of algorithms to dissociate the velocity from the pressure are introduced.

Chapter II deals with the finite element approximation of the Stokes problem in the primitive variables (velocity and pressure). It can serve as a good introduction to the subject of mixed finite element methods, which plays an important part in a wide range of applications. It describes most of the finite element methods available in this context and introduces some new three-dimensional elements. An original feature of this chapter is that it provides a unified treatment of the so-called B.B. compatibility condition between the velocity and pressure spaces.

## p0010-preface-004

Although the finite element methods of Chapter II are the most popular, they do not satisfy exactly the incompressibility condition. On the contrary, Chapter III is devoted to the study of exactly incompressible finite element methods. It solves the Stokes problem using other variables such as the stream function and the vorticity or the stream function and the gradient of velocity tensor in two dimensions or even the vector potential and the vorticity in three dimensions. This chapter provides a number of useful and (seldom known) techniques for analyzing accurately these finite element schemes. Such techniques are not restricted to the Stokes problem but may be adapted to other mechanical situations like the bending of plates in elasticity.

## p0010-preface-005

Chapter IV is devoted to the theory and approximation of the full Navier-Stokes problem. The existence and uniqueness theorems are entirely standard but the approximation is presented in a fairly new light. Its originality consists in extending systematically the results of the previous two chapters to this nonlinear situation. The basic result is a general theorem concerning the approximation of branches of nonsingular solutions of nonlinear problems. When it is applied to the Navier-Stokes equations, it enables one to recover optimal rates of convergence. We end this chapter by describing a number of useful algorithms for handling the Navier-Stokes nonlinearity.

## p0010-preface-006

Finally, the appendix presents an up-to-date summary of the finite element theory which is constantly used throughout this book.

## p0010-preface-007

We wish to thank our colleagues C. Bernard, M. Crouzeix, O. Pironneau, G. Raugel and L. Tartar for many fruitful and exciting discussions. We are particularly grateful to R. Verfürth for reading the manuscript and providing very helpful suggestions. For the material preparation of this work, we are above all gratefully indebted to our colleagues of the Computing Science Department who provided the microcomputer with which the manuscript was typed. We thank also Mme. Ruprechts for typing a part of the manuscript.

Paris, March 1986

Vivette Girault

Pierre-Arnaud Raviart
