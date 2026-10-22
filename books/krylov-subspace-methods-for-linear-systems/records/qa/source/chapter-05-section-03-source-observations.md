# Section 5.3 source observations

Original PDF 206-210 / printed 194-198 was visually reviewed. The following source forms are retained, not corrected.

1. PDF 207 describes U as an "upper tridiagonal matrix" in the Schur square-root derivation; PDF 209 similarly calls both U and U^p upper tridiagonal. No replacement with "upper triangular" is made.
2. The general five-step Newton scheme on PDF 208 begins its loop at k=1 after setting X_0. Formal Algorithms 5.2, 5.3, 5.5 and 5.6 begin at k=0. These different starts remain as printed.
3. The convergence paragraph on PDF 208 uses A^{1/2}X_0, without an inverse, in its right-half-plane spectral condition. No inverse is inserted.
4. Algorithm 5.3 starts with X_0=A and E_0=(I-A)/2; Algorithm 5.6 instead starts with X_0=I and E_0=(A-I)/p. The initializations are not unified.
5. The Schur pth-root algorithm keeps every printed v superscript and summation range, including p-k-1, p-k, k-ell+1, and the sum ending at k-1. No algebraic simplification is applied.
6. Theorem 5.4 does not separately state a range for p in its hypothesis. No extra assumption is added to the translated statement.

The external page locator [97, p.140] and external equation locators [102, Eqs. (3.6), (3.9)] refer to cited publications. They remain external citation metadata, not links to this book's equations or pages. All book-local references use semantic labels. No unresolved or unreadable mathematical token remains in this section.
