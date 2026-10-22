# Source observations preserved without correction

These are readable statements or formulas in the supplied PDF. They are not OCR ambiguities. The translation preserves them; this record does not authorize correcting the book.

| PDF / printed | Original observation | Treatment |
| --- | --- | --- |
| 10 / ix | Acknowledgements says three editors but lists four names. | Translate three and retain all four names. |
| 14 / 1 | Right-hand side is printed as b in C rather than C^N. | Preserve the printed space. |
| 15 / 2 | A-norm is printed as x^T A x without a square root. | Preserve the expression. |
| 16 / 3 | Theorem 1.2, item (4) prints norm_1 <= norm_F. | Preserve the inequality and its direction. |
| 17 / 4 | Prose says p-norm of x, immediately before a bound for Delta x. | Preserve the prose and displayed formula separately. |
| 21 / 8 | Algorithm 1.3, line 7 says swap the ith column and q_i th row of matrix P. | Retain column, row and P, rather than silently substituting Q. |
| 23 / 10 | LDL^T existence statement says nonnegative leading principal minors; Algorithm 1.6 starts i=2 and does not print initialization of d_11. | Preserve the condition and the exact loop bounds without inserting initialization. |
| 25 / 12 | The prose equates l_32, l_42 and l_43 as nonzero, while the displayed factor has different nonzero fractions. | Preserve both the prose and matrix entries. |
| 40 / 27 | The rectangular bi-Lanczos relation prints W_(n+1) T_(n+1,n)^H. | Preserve the printed product; do not repair the dimensions by inference. |

Visual mathematical checks also recovered information absent from plain extraction: conjugation of the initial w_1 denominator, bar alpha_n, bar gamma_(n-1), bar beta_n, w_0 = bar v_0, and the conjugated first arguments in complex-symmetric Lanczos bilinear products.

The term grade remains the user-approved 阶. No mathematical source correction has been made.
