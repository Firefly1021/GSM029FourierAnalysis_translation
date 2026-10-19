# Section 3.3 original-source observations

Scope: PDF 111-158 / printed 99-146, ending before Section 3.4. These observations preserve what is printed; they do not authorize mathematical corrections. The original PDF is authoritative. No source ambiguity currently prevents transcription. External-publication locators remain external citation metadata.

1. PDF 112 calls the condition number of the normal matrix “twice as large”, not “the square”. This wording is translated literally, without silently replacing it by a standard condition-number statement.
2. PDF 113 equation (3.57) and PDF 114's subsequent stacked iterate definition use different component orderings. Both are preserved.
3. PDF 114's second bilinear reduction prints a comma before its first equality and an unusual bracketed expression. Its printed mathematical arrangement is retained rather than repaired by dimension arguments.
4. PDF 116's displayed auxiliary shadow vector uses the unstarred residual in its first term; Algorithm 3.13 line 7 on PDF 118 uses the starred residual. Both printed versions are retained.
5. PDF 118 Algorithm 3.13 line 12 defines alpha without a subscript, while subsequent lines use alpha_n. The distinction is retained.
6. PDF 118 Algorithm 3.13 line 25 has an unstarred final y_(n+1) in the shadow update. It is retained. A draft's spurious alpha coefficient on the first shadow residual was removed after a high-resolution crop check; that extra coefficient is NOT in the source.
7. PDF 121's far-symmetric-results prose prints b_1=b_2=b_3=0.1; Figure 3.2's caption prints 10. The contradictory prose and caption are both retained.
8. PDF 123 Algorithm 3.15 does not initialize w_1 or p_(-1),p_0 in its printed input, nor explicitly assign the t entries before their first rotations. No missing initialization is supplied. The comma in line 21 is retained.
9. PDF 124-125 Proposition 3.4 alternates m and n, and epsilon_n and epsilon^(n); all printed indices and forms are retained.
10. PDF 125 says the value of epsilon_n depends on convergence speed. The translation does not reverse that dependency to make it sound more natural mathematically.
11. PDF 126 Algorithm 3.17 prints “while convergence”, not “while not converged”. Its wording is retained.
12. PDF 126 defines z^(k) using j-indexed approximate solutions. No k-index substitution is introduced.
13. PDF 129 first gives y_i=(Av_i,r_n), then gives y_i=(Av_i,r_0). Both are preserved.
14. PDF 130 uses unweighted inner products in the expansion argument, and ends its sum with c_i even though j is fixed. Neither weights nor a different terminal index are inserted.
15. PDF 132 property (G5) prints i>=j, although j does not otherwise occur in its equality. This condition is retained.
16. PDF 133 prints R=(A-A)^T/2. The translation does not replace it by the standard skew-symmetric part.
17. PDF 133 Orthomin(k) line 5 has one index interval and line 6 uses a sum starting at 1; line 7 has another upper limit. The original ranges are preserved.
18. PDF 140's displayed zeta formula has t_n^H A t_n in its numerator, whereas Algorithm 3.22 uses (At_n,t_n). Both printed expressions are retained, including conjugation distinctions.
19. PDF 140's BiCGSTAB residual identity ends with r_n^(BiCG), not r_(n+1)^(BiCG). The printed index is retained.
20. PDF 145's dimension proof and corollary alternate omega_j/omega_(j+1) and i/j subscripts. All original indices are retained.
21. PDF 146 equation (3.108) has calligraphic S on the left of its equivalence and italic matrix S on the right. Font metadata and the original rendering confirm this distinction. It is retained, not changed to a mathematically more plausible condition.
22. PDF 147's solution extraction prints x_7=x_7-... and x_8=x_8-.... No previous-iterate indices are substituted.
23. PDF 150 repeats A^H s_1 in its four displayed orthogonality conditions, while the next span also includes A^H s_2. Both versions are retained.
24. PDF 151 describes negative numbers as true relative residual norms, without explicitly saying logarithms in that sentence. No missing logarithm is added to the translation.
25. PDF 152 and Algorithms 3.25-3.26 print an N-by-s initial X_0; the algorithm input prints a lowercase n in P's dimensions. These are retained rather than conformed to the earlier N-by-m right-hand-side matrix.
26. PDF 154 says R_3,R_4,R_5 also belong to G_2, despite the preceding list containing R_6,R_7,R_8. The repeated triple is retained.
27. PDF 149 refers to Definition 3.1 for a later B-space definition. The semantic reference still targets the original Definition 3.1, not an inferred replacement Definition 3.2.
28. PDF 154-156 explicitly use a black-square superscript on the block difference matrices. This is mathematical notation, not an OCR placeholder or proof-ending symbol, and is preserved.
29. PDF 155's prose describes obtaining R_3,R_4 while the following display computes R_4,R_5. Both printed descriptions are retained.

The final source/translation formula inventory checks exact expression tokens per aligned block; this is supplemented by rendered original-page comparison. Token agreement between the two authored languages alone is not treated as proof that the transcription matches the source.
