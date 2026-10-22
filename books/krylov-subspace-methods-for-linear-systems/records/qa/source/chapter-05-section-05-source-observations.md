# Sections 5.4-5.5 source observations

Original PDF pages 210-215 / printed 198-203 were visually compared. No silent correction is applied.

1. The direct-truncation paragraph (PDF 211) truncates at degree m, but says the truncation error may be small for small n. The symbols m and n are retained in their respective places.
2. The matrix-vector cost paragraph (PDF 213) says "where n is a matrix of size n x n". This wording is retained in both source and translation rather than silently replacing n with A.
3. The Krylov polynomial paragraph (PDF 213) calls p_m a degree-m polynomial while assigning its product to K_m. The degree and subspace index are not reconciled by the translator.
4. The projected-cost paragraph (PDF 214) says the Padé-vector product requires H_m^{-1} v and assigns O(m^2) cost to the solve. The printed statement is retained without a computational-complexity correction.
5. Algorithm 5.7 (PDF 215) calls Im(X) the imaginary part of A and Re(X) the real part of A. Both formulas and both annotations are preserved; A is not replaced by X in the annotations.
6. The bound in Theorem 5.7 uses ||x_0||_2 on the left but ||x_0|| in c=10||x_0||. Both norms are retained with their original subscripts or absence thereof.

The two footnotes on printed page 199 are retained. The citation [133, p.12] and Theorem 2 within publication [99] are external publication locators, not targets in this book. All local object and clause references are generated from labels.
