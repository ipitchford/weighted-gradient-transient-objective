# Machine-readable reading guide

## Identity and assurance

Version 0.1.0-candidate; date 6 November 2026; reserved DOI 10.5281/zenodo.24001734. DOI reservation does not establish provider publication.

Title: Transient objective convergence of spectrally weighted gradient descent. Creator: Anonymous. Status: AI-assisted unrefereed candidate. Read [paper.md](paper.md) or [paper.pdf](paper.pdf) as the scientific argument; [VERIFICATION.md](VERIFICATION.md) describes bounded computational evidence. No formal verification or independent external reproduction is claimed.

## Claim to proof to evidence

| Claim | Proof location in paper | Dependencies and evidence | Boundary |
|---|---|---|---|
| Monotone weights give an objective comparison bound | Proposition 1, Corollary 2 | Covariance identity and scalar quadratic comparison | Elementary supporting argument; no priority claim |
| Fixed-horizon sharp deficit 2 omega K/kappa | Theorem 3, Corollary 4 | Proposition 1 and two-/three-mode recurrence | Positive nondecreasing unbounded fixed weight; lambda_min=1; fixed K and omega |
| Two active eigenvalues cannot give unrelaxed two-step failure | Proposition 5 | Exact reciprocal ratio map and scalar two-step multiplier | Inherited two-point structure, self-contained proof |
| Uniform finite-parameter control | Lemma 6 | Explicit logarithmic bootstrap | Power weights, omega=1, admissibility beta_K<=delta/64 |
| Explicit horizon and sufficient failure test | Subsection after Lemma 6 | Logarithm of admissibility condition and upper deviation side of Lemma 6 | Sufficient only, not optimal/necessary; numerical certification requires enclosures |
| Sharp sublogarithmic horizon deficit | Theorem 7 | Lemma 6, horizon-dependent separation | Fixed positive power exponent; K=o(log kappa) |
| Simultaneous logarithmic interval of failure | Corollary 8, Remark 9 | Fixed separation and uniform Lemma 6 error | One instance per kappa, no arbitrary logarithmic crossover |
| Three displayed rational witnesses | Exact rational counterexamples section | [exact checker](checks/check_exact_examples.py) | Exact finite examples, not universal proof |
| Recurrence identities and bounded numerical grid | Lemma 6 proof | [grid checker](checks/check_uniform_horizon.py) | Fraction identities exact; Decimal grid diagnostic only |

## Checker trust boundaries

[guards.py](checks/guards.py) supplies explicit exceptions and exclusive receipt creation; [test_guards.py](checks/test_guards.py) checks intended failures under deliberate corruption. [VERIFICATION.md](VERIFICATION.md) records tested source hashes and normal/optimized results. Guard coverage does not prove that all possible faults are caught.

[RESEARCH_GATES.json](RESEARCH_GATES.json) records retrospective source/extension coverage rather than a final archive pass. [SOURCES.md](SOURCES.md) and [CITATION_AUDIT.md](CITATION_AUDIT.md) distinguish source versions and exact inspected passages. [LIMITATIONS.md](LIMITATIONS.md) lists excluded parameter regimes and inference boundaries; [RESPONSE_TO_REVIEW.md](RESPONSE_TO_REVIEW.md) gives substantive repair dispositions.

## Files and dependencies

[paper.tex](paper.tex) builds [paper.pdf](paper.pdf); [refs.bib](refs.bib) mirrors its embedded bibliography. [requirements.txt](requirements.txt) declares no third-party Python packages. [ENVIRONMENT.txt](ENVIRONMENT.txt) records observed tools. [LICENSES.md](LICENSES.md) separates original prose, code and third-party citations. Provider identifiers and immutable archive identities must be read from final release metadata, not inferred from this guide.

