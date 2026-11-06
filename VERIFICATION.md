# Verification scope

Recorded 6 November 2026. The following is a substantive public summary of producer-side checks, not external peer review.

## Written arguments

Full internal AI-assisted inspection found no unresolved load-bearing defect. A targeted final check of the revision verified the finite-parameter horizon floor, strict sufficient failure implication, and the Lemma 6 derivative comparison. The inspected Markdown SHA-256 was be0d2ef2affc5298de8bdc282ef516d97a0b2db5f217cd3e4df4e6eb38bba224. Universal asymptotics and bootstrap estimates remain written proofs, not consequences of a finite grid.

## Executable checks actually recorded

Python 3.14.7, standard library only. Each of the three commands in README was run normally and with -O, using -B and fresh output paths. All six exited zero.

- Exact checker: three rational witnesses and 80 exact two-mode parameter cases.
- Horizon checker: 324 rational recurrence identity comparisons; 195 admissible Decimal grid cases; 125 combinations excluded by the hypothesis.
- Negative controls: 16 intended semantic guards pass in both execution modes. A failure in an earlier unintended guard does not count.
- Static inspection: no scientific AST Assert nodes remain. Normal and optimized scientific JSON agrees apart from timing.
- Receipt protection: attempted overwrite raised FileExistsError and preserved the old bytes.

The Decimal maximum error/bound ratio was 0.7703703703703704; maximum step-error ratio was 0.16666666666666666. These are bounded numerical diagnostics, not rigorous enclosures or universal proof.

## Source identity

| Checker | SHA-256 |
|---|---|
| checks/check_exact_examples.py | dafd04926477d1bd14485e2e342752dff47d1a9d941f35e990460134404b5ebe |
| checks/check_uniform_horizon.py | 3af4cce38c187231a0a7ff634c5029a59cf42d400ce350d47f8fa52170ce27e8 |
| checks/guards.py | 1de7b9e7f4e40888fdb27a36fc5b65ecb286342242596b4630640514fcbf9c64 |
| checks/test_guards.py | 59abd93030b7a803be75f9a6548aa7650cc9ac6b9d433fbfa2471784d6902e22 |

The source hashes were compared again during package preparation and were unchanged; the six unchanged computational checks were not repeated. Final archive replay and exact artifact binding are separate release operations, not asserted by this preparation record.

## Negative coverage

TWO_MODE_INVERSION, TWO_MODE_SCALAR, TWO_MODE_BOUND, EXACT_STEPS, EXACT_RATIO, EXACT_DIFFERENCE, STRICT_FAILURE, RATIONAL_FAMILY, MIDDLE_RECURRENCE, HIGH_RECURRENCE, RATIO_RECURRENCE, FINITE_RESULT, HORIZON_BOUND, STEP_BOUND, FINITE_INPUT and DOMAIN_INPUT.

## Reproduction and limitations

See README for six fresh-output commands. Checks reject an existing output path. No proof assistant, interval-arithmetic verification of the Decimal grid, finite-precision algorithm stability study, or independent external reproduction was performed. Successful execution is not mathematical adequacy.

