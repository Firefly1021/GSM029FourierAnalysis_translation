# Chapter 4, Section 4.4: source observations

Scope: PDF 188-200 / printed 176-188. All four subsections, the complete Theorem 4.1 and its proof, Corollary 4.1, all five algorithms and all displayed derivation chains are retained. The corollary has no proof in the original; no additional proof is supplied.

1. Theorem 4.1 puts unshifted x_i in K_i(A,b)^perp but shifted x_i^sigma in K_i(A,b) without that complement. Both source statements are retained. Its polynomial definition sums c_k A^i, with exponent i rather than the summation index k; that printed exponent is retained.
2. The same theorem first defines the shifted residual with no subscript i, then uses r_i^sigma. The proof prints K_(i+1)(A,b)=i+1 without a dimension operator. These source forms remain unchanged.
3. Algorithm 4.7's input gives sigma_s for all k and the shadow update uses conjugated alpha_n without the s superscript. The bar on beta_(n-1) in the shadow-direction recurrence and the bar on alpha_n are verified against the original image and retained.
4. Algorithm 4.8 uses alpha_k and beta_k in lines 12 and 16, whereas the loop is over n, and uses sigma without a k subscript in the shifted loop. These printed indices are retained. The algorithm also uses shifted t_n^(k) without an explicit update line; no missing line is invented.
5. In equations 4.41 and 4.42 the middle expression omits the argument (A) on Q_n and Q_(n+1), although adjacent expressions include it. No argument is silently inserted.
6. Algorithm 4.9's h^(k) setup occurs before its k loop. Line 20 uses conjugated s_n and c_n without k superscripts, while neighboring lines use them. Its prose refers to an unshifted g when the displayed update uses g^(k). These forms are preserved.
7. The restart discussion on PDF 195 uses K_n(A,b) after a restart and ends with right-hand side b^sigma instead of b. These original distinctions are not repaired.
8. Algorithm 4.10 line 9 uses V_m y_m^(k) for an x_n^(k) update. The original m and n indices are retained. All eight equivalence steps leading to equation 4.45 are retained, rather than replaced by only the final system.
9. Corollary 4.1 states a common subspace result for nonzero omega_j^(i) without additional relations among those parameters, and takes S in R^n. Its precise statement is preserved, not strengthened with guessed hypotheses. No proof absent from the source is added.
10. Equation 4.50 has an extra italic v directly before r_(k-l), whereas 4.52 omits it. Original rendered page and native extraction both show the extra character. Both source formulas are retained as printed.
11. The prose preceding equation 4.57 calls the unknown omega_k^sigma, whereas the displayed system uses omega_j^sigma. The differing source indices are retained.
12. Algorithm 4.11 input uses P in C^(n by s), lowercase n. Its line 28 skips from gamma_j to gamma_(j+2). Both the original index and the skipped subscript are retained, not silently replaced.
13. Algorithm 4.11 retains every one of its 41 numbered lines, including two separate shifted loops, both stopping-condition tests, all history-vector updates and the modulo-operation note. No presumed redundant branch or vector update is removed.

These are reviewed, nonblocking source observations, not mathematical approval of the original statements or algorithms. Suspected errors are kept distinct from draft transcription corrections. No unreadable symbol or uncertain reference target remains.
