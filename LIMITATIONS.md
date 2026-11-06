# Scope and limitations

The paper concerns a specified single-gradient-direction update on finite-dimensional, real symmetric positive-definite quadratics. It does not claim an algorithmic lower bound for conjugate gradients, multidirectional methods, preconditioned algorithms as a class, or arbitrary optimization procedures.

- **Normalization:** the general-weight theorem fixes the smallest eigenvalue to one. A nonhomogeneous weight need not be invariant under rescaling the matrix. Power weights allow the usual scaling reduction.
- **Metrics:** ordinary objective error is not the residual norm or the weighted gradient norm used to select the step. The transformed steepest-descent representation does not identify these metrics.
- **Fixed horizons:** the sharp leading coefficient is a condition-number limit at fixed weight, relaxation and iteration count. It is not an exact finite-condition-number worst-case formula.
- **Growing horizons:** the sublogarithmic and simultaneous logarithmic results are for fixed positive power exponent and no relaxation. They are not proved for every unbounded monotone weight.
- **Order of limits:** matrices and starts vary with condition number. The sublogarithmic construction can also depend on the chosen horizon. Only the separate simultaneous-interval result supplies one instance at each condition number that works throughout its stated interval.
- **Finite test:** the consequence of Lemma 6 is sufficient, not necessary or optimal. Its hypothesis can fail even when the displayed rational example violates the proposed rate. Certified arithmetic is required when numerical evaluation of real powers or logarithms is used as a rigorous certificate.
- **Long time and accuracy:** no sharp logarithmic crossover or fixed-matrix long-time obstruction is proved. The transient coefficient comparison does not imply twice as many iterations for a fixed target accuracy.
- **Relaxation:** the fixed-horizon result covers 0 < omega <= 1; the moving-horizon result is unrelaxed. Over-relaxation requires a separate argument.
- **Evidence:** exact rational examples and identities support finite claims. Decimal grids are numerical sanity checks, not interval certificates or universal proof. The general results depend on written arguments. No proof-assistant formalisation, external human peer review or independent external reproduction is claimed.
- **Prior art:** the comparison covers the cited objective question, classical weighted-gradient asymptotics, minimal-residual root factors and the later flexible framework. It is bounded, not proof of exhaustive historical priority. The source's prose question is not presented as a disproved theorem.

