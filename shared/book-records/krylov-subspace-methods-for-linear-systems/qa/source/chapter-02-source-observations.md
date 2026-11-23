# Chapter 2 original-source observations

These observations describe the original PDF, not editorial corrections. The original expressions and wording remain in both reconstructed English and Chinese translation. The source is readable; these are non-blocking source warnings, not license to repair formulas. A clean compile does not certify mathematical correctness.

- PDF 46 / printed 34: the definitions of the grid unknowns and some displayed boundary indices do not follow the ordering pictured in Figure 2.1. Preserve all printed definitions, equations and matrix entries independently.
- PDF 47 / printed 35: the generic Kronecker product uses a last column index m and last row index n, while later dimension declarations use a different convention. Preserve the printed indices.
- PDF 49 / printed 37: the proof of the product-eigenpair corollary drops the superscripted matrix identifiers on lambda_i and lambda_j. Preserve these literal tokens.
- PDF 51 / printed 39: the final row of Equation 2.15 ends with (4-h^2 sigma^2)u_3, not u_6. Preserve u_3.
- PDF 52 / printed 40: the second cosine argument is (1/2) times (h/2), then h/4. Preserve both forms, rather than changing them to h/2.
- PDF 52 / printed 40: a is defined by sqrt(sigma^2-1/4) after Equation 2.16. Preserve this definition instead of substituting a value suggested by the earlier stencil.
- PDF 53 / printed 41: the operator uses scalar c while the subsequent prose defines bold c=[c_1,c_2,c_3]^T. Preserve both.
- PDF 54 / printed 42: the prose gives u(x_i,y_i,z_i), g(x_i,y_i,z_i), rather than independent j and k indices. Preserve the printed indices.
- PDF 56 / printed 44: the source passes from the whole-domain integral to an elementwise equality and states disjoint elements. Preserve these claims without adding qualifications absent from the source.
- PDF 56 / printed 44: the text specifies clockwise triangle numbering; Figure 2.6 is retained unchanged, with no attempt to reconcile orientation or determinant signs.
- PDF 59 / printed 47: the text links the two finite-element types to Equation 2.8. Preserve this source target rather than substituting Equation 2.32.
- PDF 63 / printed 51: the reported approximate solution values are copied literally, without replacing them by newly computed values.
- PDF 64 / printed 52: the Hamiltonian integral contains -hbar/(2m), without a squared hbar. Preserve the original expression.
- PDF 66 / printed 54: the source's examples of D(x;y) for N=2 and its discussion of lattice directions are retained without supplying unprinted boundary conditions or extra neighbor contributions.
- PDF 68 / printed 56: Equation 2.42 contains theta_1 f_1 + theta_2 f_2 + theta_m f_m, with no printed ellipsis between the second and final terms. Preserve the three printed terms.
- PDF 74 / printed 62: the source defines (M)_{i,j}=f_i(x_j); the normalization and subsequent class-specific kernel expansion are retained as written, without changing matrix orientation or summation ranges.
- PDF 76 / printed 64: the stacked blocks in the vectorization proof finish with index n as printed, even where dimension conventions suggest a different index.
- PDF 77 / printed 65: the third equivalence in the T-congruence derivation prints vec(I_n tensor A) vec(X). Preserve the extra vec exactly.
- PDF 79 / printed 67: the SVD prose uses V^H and the following tensor expression uses V^T. Preserve both distinctions.
- PDF 80 / printed 68: the approximate minimizer is initially written x_n and subsequent steps use x_k. Preserve these indices.
- PDF 82 / printed 70: the derivative contraction line uses Y_{k-perp}C_k on the left and Z on the right. Preserve the literal line and surrounding explanations.
- PDF 82 / printed 70: one prose occurrence spells the manifold name Grassman, whereas other occurrences spell it Grassmann. Preserve the two exact source spellings separately.
- PDF 83 / printed 71: the source invokes A=A^T in the Rayleigh-quotient example although the opening only states its dimensions. Preserve the original logical wording; do not add an earlier symmetry assumption.
- PDF 84 / printed 72: Equation 2.74 has a bar over f. Preserve it; the subsequent prose names the unknown C rather than C_k and describes Q_k as the thin QR factorization. Preserve that wording without explanatory additions.

The original has independent theorem and corollary numbering series, while the approved user template intentionally shares a statement counter. The source-number-to-label-to-rendered-number mapping is recorded in the cross-reference registry. Body references use labels; the shared template is not modified to imitate the original counters.
