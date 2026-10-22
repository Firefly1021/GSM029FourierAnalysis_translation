# Chapter 4, Section 4.3: source observations

Scope: PDF 183-188 / printed 171-176, ending before Section 4.4. All three subsections, seed-switching subsubsection, seven numbered equations, all three complete algorithms and all discussion of generalized shifted systems are retained. Original rendered pages were checked against the bilingual source.

1. The generalized-system discussion asserts unequal Krylov spaces whenever i differs from j, without qualifying possible coincidences of shifts or invariant spaces. The exact inequality and its stated strength are preserved rather than weakened to a generic or possible case.
2. Source equation 4.26 uses the ordered unknowns [y;x], C^top in the lower block and -C^top in the shifted block. The sign, ordering and transposes are preserved without an alternative linearization.
3. The seed-switching formulas use beta_n, alpha_i and beta_j without the original-seed superscript s in the relevant occurrences. Those unindexed source quantities are retained; no silent harmonization is applied.
4. Algorithm 4.5 line 4's first denominator factor contains A^(sigma_s), whereas its second factor and surrounding algorithm use A^(s). The printed sigma_s is confirmed in both the original page and native extraction and is retained.
5. Algorithm 4.6's input initializes beta_(-1), although its loop begins at n=1 and uses beta_0. Output quantifies over Latin l while x is indexed by k; line 7 uses ell. These distinctions and the absence of further initialization are retained.
6. Algorithm 4.6 line 9 delegates to lines 9-24 of Algorithm 4.3. The cross-reference is explicit; the prior algorithm is neither duplicated nor silently modified.
7. The QMR_SYM properties discuss A^(s) and seed products whereas the printed complex symmetric Lanczos algorithm uses A. The original mismatch remains recorded.
8. The final discussion declares that a Hermitian matrix with complex shifts is neither Hermitian nor complex symmetric, without spelling out exceptions. The source statement is retained, not replaced by added qualifications.
9. The prose preceding equation 4.27 uses unshifted x_n, while the equation itself uses x_n^(k). The source distinction is retained. The normalization g_1 and the QMR_SYM algorithm use the conjugated first factor in the bilinear product, not the Hermitian-MINRES normalization.

External locators 158 section 3 and 67 Corollary 1 remain publication metadata. The future shifted-BiCG subsection target was visually verified on PDF 188 / printed 176. These observations are reviewed and nonblocking; no unreadable symbol or unresolved local reference remains.
