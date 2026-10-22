# Chapter 3, Section 3.4: source observations

Scope: PDF 158-163 / printed 146-151, excluding the already accepted Algorithm 3.26 and the following Section 3.5. Original rendered pages were compared with all eighteen bilingual blocks. The four complete algorithms retain 7, 7, 10 and 25 numbered lines, respectively. Both the multi-line CGNE minimization chain and all three initial Lanczos steps are retained in full.

1. PDF 160 / printed 148 says the condition number of A^H A (or AA^H) is *twice* that of A. The translation preserves “两倍”, not a silent replacement by “平方”. The same wording was already present in Section 3.3.
2. PDF 161 / printed 149 first defines h with subscript 0,1 and then prints h with subscript 01 without a comma. Both forms are retained in their respective occurrences.
3. PDF 162 / printed 150 says that y is determined by residual minimization, although the approximate-solution formula uses y_n. The unindexed y in that sentence is retained.
4. Algorithm 3.30 (PDF 163 / printed 151) uses t entries and g_n in the Givens steps without explicitly giving their initialization from the bidiagonal entries or the initial right-hand side. It also uses p_(n-1) at n=1 without explicitly initializing p_0. No missing initialization or extra update was supplied by the translation.
5. The source uses transpose, not conjugate transpose, on the real bidiagonal B and coordinate e in the Golub--Kahan matrix recurrence. The indicated transpose symbols are retained. The zero block in the augmented matrix is the letter O, not the scalar digit 0.

6. The CGNE introduction on PDF 159 explicitly cites source equation 3.16 (the coordinate representation), not 3.17 (the later transformed least-squares formula). Source-number lookup caught a draft target mismatch, which was corrected before acceptance. The reference follows the actual printed source target even if another formula might appear more relevant.

These are reviewed, nonblocking source observations. No uncertain target or unreadable formula remains in this batch. They are not claims that compilation validates the mathematics.
