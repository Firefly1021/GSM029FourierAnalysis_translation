# Theorem-environment regression report

## Scope

- User source style: `input/template/style/Mystyle.sty` (read-only and unchanged).
- Authorized override layer: `tex/translation-adapter.sty`.
- Regression document: `tex/chapters/sample.tex` through `tex/sample-main.tex`.

## Environment behavior

| Environment | Counter | Title structure | Preserved visual treatment |
|---|---|---|---|
| `Theorem` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | `KuangNei` background; hidden frame; breakable box; italic Chinese body |
| `Definition` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; italic Chinese body |
| `Lemma` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; italic Chinese body |
| `Proposition` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; italic Chinese body |
| `Corollary` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; italic Chinese body |
| `Example` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; normal body font |
| `Remark` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; normal body font |
| `Exercise` | shared `thmcount`, advanced by `\refstepcounter` | number, optional name, ASCII colon, body | plain layout; normal body font |

Theorem no longer uses a separate `tcolorbox` title region. Its frame is hidden, its background remains `KuangNei`, and `breakable` remains enabled. Optional names follow the number in ASCII parentheses, and every title ends with an ASCII colon.

## Cross-reference verification

- The sample defines 16 theorem-like labels and the auxiliary file resolves them to the expected sequence `2.1` through `2.16`.
- Every requested statement environment advances the referenceable shared counter with `\refstepcounter{thmcount}` before a following `\label` can bind.
- The compiled PDF contains 16 `thmcount` named destinations and working link annotations for statement references.
- No duplicate labels, undefined references, multiply-defined-label warnings, or duplicate-destination warnings were found after two XeLaTeX passes.
- A separate two-pass smoke document instantiated all eight requested environments. Its auxiliary file resolved the labels consecutively as `1.1` through `1.8`, all on `thmcount` destinations, with no reference warning.

## Input integrity

- `input/template/style/Mystyle.sty`: SHA-256 `0421c7f0f344f28796fc0bd3fcacc86f5aabccca3926f3b4f6636c745b0e69a4`.
- The recorded hash is unchanged; all behavior changes are confined to the authorized adapter and translated output.

## Result

Pass.

## Chapter 1 cumulative regression

The Chapter 1 cumulative build resolves 23 statement labels consecutively as `1.1` through `1.23`, on `thmcount` destinations. The final third XeLaTeX pass contains no undefined reference, multiply-defined label, duplicate destination, or rerun warning. Visual inspection confirmed that long statements and proofs remain breakable and that statement titles preserve the established number, optional name, ASCII-parenthesis, and ASCII-colon structure.
