# Transient objective convergence of spectrally weighted gradient descent

Anonymous · AI-assisted, unrefereed research candidate · 6 November 2026.

Version 0.1.0-candidate · DOI: [10.5281/zenodo.24001734](https://doi.org/10.5281/zenodo.24001734). This DOI was reserved before archive publication; reservation alone is not evidence that the deposit is public.

A method can choose a good step for one error metric while reducing another slowly. This paper studies ordinary quadratic objective error for spectrally weighted gradient steps. Small high-frequency components control the step while a low-frequency component carries nearly all objective error.

## Read first

- [Paper PDF](paper.pdf), [accessible manuscript](paper.md), [LaTeX source](paper.tex).
- [Claim-to-proof guide](AI_INDEX.md), [limitations](LIMITATIONS.md).
- [Verification scope and commands](VERIFICATION.md), [source comparison](SOURCES.md), [citation audit](CITATION_AUDIT.md).
- [Revision response](RESPONSE_TO_REVIEW.md), [provenance](PROVENANCE.md), [licence map](LICENSES.md).

## Results and boundary

For positive nondecreasing unbounded weights, with smallest eigenvalue normalized to one, the worst-case objective ratio after fixed K steps has leading deficit 2 omega K/kappa. Three dimensions suffice; two suffice for strict under-relaxation. For positive power weights without relaxation, the coefficient persists for K=o(log kappa). A separate three-dimensional family violates the proposed per-iteration Kantorovich bound simultaneously over a stated logarithmic interval.

The two-step question has a weak reading that is true and a stronger reading that fails. This does not refute a proved theorem in the originating paper. The algorithm, conjugacy and two-mode recurrence are inherited. The contribution is an objective-specific transient construction and quantitative horizon control. The finite-parameter sufficient test is an elementary consequence, not a new optimal bound.

## Reproduce bounded checks

Python 3.14.7 was used; only the standard library is required. From this directory, choose a new output directory for every replay:

```sh
python3 -B checks/check_exact_examples.py --output replay-new/exact.json
python3 -B checks/check_uniform_horizon.py --output replay-new/grid.json
python3 -B checks/test_guards.py --output replay-new/negative.json
python3 -B -O checks/check_exact_examples.py --output replay-new/exact-optimized.json
python3 -B -O checks/check_uniform_horizon.py --output replay-new/grid-optimized.json
python3 -B -O checks/test_guards.py --output replay-new/negative-optimized.json
```

Existing receipt paths are rejected. These finite checks do not prove the universal analytic statements. Decimal diagnostics are not interval certificates. Internal AI-assisted checking is not external peer review, formal verification or independent external reproduction.

Build the manuscript with two invocations of `pdflatex -interaction=nonstopmode -halt-on-error paper.tex`. Its embedded bibliography permits a standalone build; refs.bib provides the same five references for machine use.

Original prose and records: CC0-1.0. Original checker code: MIT. Third-party works are cited, not relicensed.

