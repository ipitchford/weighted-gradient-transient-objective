# Response to review

This note records substantive changes to the revised manuscript without reproducing private assessments. The research remains an AI-assisted, unrefereed preprint.

## Reader context and metric ambiguity

The introduction now explains the high-mode/low-mode mechanism before the proofs: the spectrum controlling the step need not carry most ordinary objective error. A metric-and-regime table separates the measured objective, fixed horizons, sublogarithmic horizons, simultaneous intervals and fixed-matrix long-time theory. A proof roadmap directs readers to the small exact examples as an alternative entry point.

The discussion explicitly rejects an inference about twice as many iterations at a fixed accuracy. The result concerns a leading transient decrement, not a fixed-fraction convergence complexity.

## Normalization and quantifiers

The abstract now states smallest-eigenvalue normalization and its essential role for nonhomogeneous weights. The existing precise theorem assumptions and all original proof statements are retained. Horizon-dependent witnesses and one-instance simultaneous intervals are distinguished in the introductory table and in the existing remark.

## Source attribution and scope

The originating question is located in Section 6, the “Future work” paragraph, of MacDonald–Murray–Tappenden's published paper. It is a prose question with two interpretations, not a theorem claimed to have been refuted.

Huang and collaborators' comparison uses inspected arXiv:1908.07111v1 numbering: Corollary 11, equations (60)–(62), and Remark 12, equation (63). The later MacDonald–Murray–Tappenden flexible framework is added with Definition 8 and Section 2.1, Lemma 9. Its broader search directions, symmetric preconditioning and selected weighted gradient norm are distinguished from this paper's scalar gradient-direction ordinary-objective result. Inspected author-manuscript versions are pinned in references. The paper and references do not claim an exhaustive novelty guarantee.

## Quantitative proof clarification

The Lemma 6 proof now gives the positive r derivative explicitly and uses its absolute bound. The path of comparison first varies nonnegative epsilon at fixed r, then varies r at epsilon zero within the bootstrap region. This is a clarification of the existing estimate, not a changed theorem.

## Tractable finite-parameter consequence

A new subsection immediately after Lemma 6 solves its hypothesis for the integer horizon and derives a strict sufficient condition for failure of the proposed per-iteration bound. The short proof states both inequality directions. The subsection explicitly disclaims necessity, optimality and certified status for unvalidated decimal evaluation. The original theorem numbering and numbered equations remain unchanged.

No speculative extension to over-relaxation, arbitrary logarithmic crossover, general unbounded-weight growing horizons or optimal finite-condition-number constants has been added.

## Executable assurance and residual work

The removable-assert issue is an executable assurance defect, not a claimed disproof of the written argument. Checker repairs are maintained separately in checks/check_exact_examples.py, checks/check_uniform_horizon.py and checks/test_guards.py. Their intended interface requires --output NEW_PATH.json and exclusive receipt creation. Current positive, optimized and intended-failure results must be established by their saved verification record; this manuscript revision does not substitute for that run or claim that it has finalized artifact hashes.

The paper now separates exact rational checks, numerical grids, written proof and external validation. It removes dependence on inaccessible internal review records. Final publication still requires the release's current replay, artifact binding and presentation checks.

