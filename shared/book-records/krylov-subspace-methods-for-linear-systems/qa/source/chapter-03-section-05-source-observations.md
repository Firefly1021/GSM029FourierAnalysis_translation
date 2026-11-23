# Chapter 3, Section 3.5: source observations

Scope: PDF 163-174 / printed 151-162. All five subsections, five algorithms, the original sparse-pattern matrix and all four 9-by-9 fill-level matrices are retained. Source pages were inspected visually; no mathematical correction is inferred from plausibility.

1. PDF 164 says that left preconditioning no longer preserves the h.p.d. property, then splits K as K_1 K_1^H without separately restating a positivity assumption on K. This assumption is not silently added to the translation.
2. PDF 166's input A display uses uppercase A_(1,N) and A_(2,N) amid lowercase scalar a entries. These capitals are retained.
3. Equation 3.134 includes k up to min{i,j}, rather than a strictly smaller upper bound. Its printed range is retained without substituting another fill-level recurrence.
4. The level-one, level-two and final fill matrices are transcribed entry by entry. The level-two matrix already has a 2 at position (6,9). This entry is retained at that stage; no reconstructed alternative ordering is imposed. Each matrix has all 81 entries.
5. PDF 170's Frobenius-norm definition uses the sum of a_(i,j)^2, without absolute values, although surrounding algorithms allow complex matrices. No modulus signs are added.
6. Algorithm 3.35 line 11 prints z_i and z_i^(i-1) even though earlier recurrences use v. Line 12 prints V for both the v-column matrix and the w-column matrix. The printed z and repeated V are retained, not silently repaired to v or W. This is separate from ordinary prose translating the algorithm's purpose.
7. The same AINV algorithm uses a_i^H against v and c_i^H against w, with a_i and c_i described as columns of A and A^H. These adjoint signs and column definitions are retained exactly.
8. PDF 172's Jacobi diagonal ends at a_(n,n), lowercase n, while preceding system dimensions use uppercase N. The lowercase source index is retained.
9. The SSOR preconditioner is printed without an additional scalar normalization factor. Its exact expression is retained. The two complete Eisenstat algebraic chains are not replaced by their final lines.
10. The source spells the ordering name Cuthill--Mckee, with lowercase k, and the surname Tůma with a ring on u. These source forms are preserved. English source typography's dash between the two names is represented by the project's existing LaTeX double-hyphen convention.
11. The AINV algorithm floats after the Section 3.5.3 heading in the original; it belongs to the preceding discussion. Its source page and ordering are retained in the bilingual record, and it is not omitted or counted twice.

All observations are reviewed and nonblocking. External publication page locators (147, pp.77-78; 151, p.334) remain publication metadata, not local object numbers. No unreadable formula or unresolved local reference target remains.
