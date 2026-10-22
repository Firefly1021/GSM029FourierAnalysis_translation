# Chapter 4, Section 4.2: source observations

Scope: PDF 177-183 / printed 165-171, ending before Section 4.3. All three subsections, nineteen numbered equations and the complete 19-, 11- and 25-line algorithms are retained. Original page images were inspected, not just extracted text.

1. The footnote infers that sigma is real from Hermitian A^(k), without separately stating a Hermitian assumption on the unshifted A. No additional premise is silently supplied.
2. Equation 4.5 states that the nested-space intersection has dimension one without explicitly qualifying the iteration range before Krylov-space stabilization. Its source assertion and equality are retained.
3. The sentence before equation 4.7 explicitly cites source equation 3.18, not the later three-term recurrence 3.21. The actual printed reference is linked to the residual/direction polynomial formula; the more plausible later formula is not substituted. The later reference preceding 4.15 does explicitly cite 3.21 and is linked separately.
4. Algorithm 4.1's second Input line says A and sigma_s for k=1,...,m, not sigma_k. The condition in line 7 uses pi_n^(k), while subsequent lines use pi_n^(s,k). These exact printed indices are retained. Its tolerance is epsilon_2, not epsilon squared.
5. The shifted-CG algorithms begin at n=0 and contain ratios involving alpha_(-1), but no alpha_(-1) initialization is printed. No initialization or first-step special case is invented.
6. In the CR noncollinearity argument, the source writes A K_n(...)^perp and A^(k) K_n(...)^perp without parenthesizing the product inside the orthogonal complement. This literal placement is preserved; no repaired mathematical meaning is imposed. The source's inequality between the intersections is also retained at its stated logical strength.
7. Algorithm 4.3 Input initializes beta_(-1), whereas the loop begins at n=1 and uses beta_0 and v_0 in its first Lanczos update. The source does not initialize those quantities there. No extra input or line is added.
8. Algorithm 4.3 Output uses the Latin l rather than k. Line 7 has sigma_ell but t entries indexed by k, and appears before the k loop. Line 24 uses g^(k) while quantifying over ell. These source index distinctions are retained.
9. The shifted-MINRES guard in Algorithm 4.3 line 10 uses g_(n+1) before its update in line 18. No unprinted preliminary value or changed guard is supplied.
10. The prose following Algorithm 4.3 describes A^(s) products and a seed-system property, whereas the displayed Lanczos algorithm uses A. This original mismatch is not silently harmonized.

These observations are reviewed and nonblocking because the source is readable and faithfully transcribed. They are not mathematical validation of the original algorithms. The future Section 4.4.3 target is verified on PDF 192 / printed 180 and remains an explicitly untranslated source locator.
