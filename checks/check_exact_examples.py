from guards import require, write_receipt
"""Exact finite certificates for the gradient manuscript's stated examples.

This uses only the Python standard library. The finite arithmetic checks are
not a formal verification of the universally quantified analytic theorems.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import platform
import time

def iterate(eigenvalues, initial_x, weight_exponent, steps):
    x = list(initial_x)
    initial_energy = sum((lam * value * value for lam, value in zip(eigenvalues, x)))
    alphas = []
    for _ in range(steps):
        gradient = [lam * value for lam, value in zip(eigenvalues, x)]
        numerator = sum((lam ** weight_exponent * g * g for lam, g in zip(eigenvalues, gradient)))
        denominator = sum((lam ** (weight_exponent + 1) * g * g for lam, g in zip(eigenvalues, gradient)))
        alpha = numerator / denominator
        alphas.append(alpha)
        x = [value - alpha * g for value, g in zip(x, gradient)]
    energy = sum((lam * value * value for lam, value in zip(eigenvalues, x)))
    return (alphas, energy / initial_energy)

def two_mode_checks():
    count = 0
    for rho in [F(101, 100), F(2), F(3), F(10), F(100)]:
        for psi_high in [F(1, 10), F(1), F(2), F(100)]:
            for w_high in [F(1, 100), F(1, 10), F(1), F(10)]:
                masses = [F(1), w_high]
                eigenvalues = [F(1), rho]
                psi = [F(1), psi_high]
                initial = sum(masses)
                ratio = psi_high * rho * w_high
                gamma = (rho - 1) ** 2 / (rho * (ratio + 1 / ratio) + rho ** 2 + 1)
                for j in range(2):
                    numerator = sum((p * lam * mass for p, lam, mass in zip(psi, eigenvalues, masses)))
                    denominator = sum((p * lam * lam * mass for p, lam, mass in zip(psi, eigenvalues, masses)))
                    alpha = numerator / denominator
                    masses = [mass * (1 - alpha * lam) ** 2 for lam, mass in zip(eigenvalues, masses)]
                    if j == 0:
                        require(psi_high * rho * masses[1] / masses[0] == 1 / ratio, 'TWO_MODE_INVERSION')
                require(sum(masses) / initial == gamma * gamma, 'TWO_MODE_SCALAR')
                require(gamma * gamma <= ((rho - 1) / (rho + 1)) ** 4, 'TWO_MODE_BOUND')
                count += 1
    return count

def main():
    started = time.perf_counter()
    records = []
    inputs = [{'name': 'standard minimal gradient, kappa=100', 'eigenvalues': [F(1), F(60), F(100)], 'x0': [F(1), F(1, 100), F(1, 250)], 'weight_exponent': 1, 'expected_alphas': [F(193, 14485), F(7013813, 446629608)], 'expected_ratio': F(830774224427957654527687, 887449697831729589460572), 'expected_difference': F(1202635053150759637694223270715, 92348371423698611602832496009372)}, {'name': 'ell=1, kappa=10', 'eigenvalues': [F(1), F(6), F(10)], 'x0': [F(1), F(1, 10), F(1, 25)], 'weight_exponent': 2, 'expected_alphas': [F(749, 5969), F(285369, 1748690)], 'expected_ratio': F(145981491016797622500, 293076563677580674949), 'expected_difference': F(214439675688327182682111, 4290933968803458661928309)}]
    for case in inputs:
        alphas, ratio = iterate(case['eigenvalues'], case['x0'], case['weight_exponent'], 2)
        kappa = max(case['eigenvalues']) / min(case['eigenvalues'])
        comparison = ((kappa - 1) / (kappa + 1)) ** 4
        difference = ratio - comparison
        require(alphas == case['expected_alphas'], 'EXACT_STEPS')
        require(ratio == case['expected_ratio'], 'EXACT_RATIO')
        require(difference == case['expected_difference'], 'EXACT_DIFFERENCE')
        require(difference > 0, 'STRICT_FAILURE')
        records.append({'name': case['name'], 'alphas': list(map(str, alphas)), 'objective_ratio': str(ratio), 'comparison': str(comparison), 'positive_difference': str(difference)})
    n = F(4)
    alphas, ratio = iterate([F(1), n ** 4 / 4, n ** 4], [F(1), 8 / n ** 5, 1 / n ** 5], 1, 2)
    comparison = ((n ** 4 - 1) / (n ** 4 + 1)) ** 4
    require(ratio > comparison, 'RATIONAL_FAMILY')
    records.append({'name': 'rational family, N=4', 'objective_ratio': str(ratio), 'objective_ratio_decimal': float(ratio), 'comparison': str(comparison), 'positive_difference': str(ratio - comparison)})
    manuscript = Path(__file__).resolve()
    result = {'status': 'PASS', 'python': platform.python_version(), 'external_dependencies': [], 'checker_sha256': sha256(manuscript.read_bytes()).hexdigest(), 'exact_counterexamples': records, 'exact_two_mode_parameter_cases': two_mode_checks(), 'scope': 'Exact certificates for finite examples; universal proofs reviewed separately', 'elapsed_seconds': time.perf_counter() - started}
    write_receipt(result)
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()
