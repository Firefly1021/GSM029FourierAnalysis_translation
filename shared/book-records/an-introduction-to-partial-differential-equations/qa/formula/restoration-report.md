# Formula restoration

16 displayed formula regions and 38 inline math regions registered. All were
agent-reviewed against the scan. High confidence: 54; low confidence: 0.
Inline crop bounding boxes identify their parent blocks, not individual tokens.
Checks include bold vectors versus scalar components, both Jacobian matrices,
diagonal and vertical ellipses, upper/lower integral limits, t-minus/t-plus,
membership/subset signs, hats, strict versus weak inequalities, 1/3 and 3/2
exponents, and all five equation numbers. No mathematical error correction made.
Source/translation math multisets match per block; displayed formulas match in
order. These automated comparisons do not replace the recorded scan inspection.
Independent human sample approval is pending.

User-authorized rendering change on 2026-11-15: use bm for mathematical bold.
This changes the bold font command, not the variables, indices, accents, ranges
or inequalities. The original scan remains authoritative; its typography is
not silently equated with the user's new rendering choice. Semantic formula
IDs remain stable; content-derived registry hashes reflect the new command.

Further user-authorized typography on 2026-11-15: upright differential d and
display-style formula bodies. Removed explicit textstyle from the iteration;
used dfrac for fraction style inside matrices/cases. This affects rendering,
not differential variables, partial derivative operators, bounds or signs.
