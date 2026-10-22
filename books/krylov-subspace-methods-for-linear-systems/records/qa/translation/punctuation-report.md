# Punctuation review

The existing shared Chinese-prose punctuation checker runs over canonical book TeX files. It protects math, commands, comments, labels, reference keys and other excluded contexts.

Chinese prose uses ASCII punctuation. Source en dashes in personal names are serialized as LaTeX -- and render the original punctuation. Names are not normalized as Chinese prose.

Actual violation counts are recorded in qa/latest-compilation.json.
