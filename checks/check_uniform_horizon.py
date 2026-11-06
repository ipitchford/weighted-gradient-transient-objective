from guards import require, write_receipt
"""Independent direct-iterate diagnostics for gradient_uniform_horizon.md.

This script checks a finite grid in arbitrary precision. It is not a proof of
the unrestricted theorem. It deliberately iterates spectral energy masses
directly rather than using the proof's logarithmic perturbation recurrences.
"""
import json
import platform
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

def exact_rational_checks():
    checks = 0
    for c in [Fraction(1, 2), Fraction(3, 4), Fraction(9, 10), Fraction(99, 100)]:
        for k in [Fraction(4), Fraction(10), Fraction(1000)]:
            for h in [Fraction(0), Fraction(1, 1000), Fraction(1, 2)]:
                for u, v in [(Fraction(1), Fraction(1)), (Fraction(2), Fraction(3)), (Fraction(13, 11), Fraction(17, 19))]:
                    eta = (u + v + h) / (c * u + v + h / k)
                    dc = 1 - c
                    middle = (dc * v - (c - 1 / k) * h) / (c * u + v + h / k)
                    high = -(dc * u + (1 - 1 / k) * h) / (c * u + v + h / k)
                    require(1 - c * eta == middle, 'MIDDLE_RECURRENCE')
                    require(1 - eta == high, 'HIGH_RECURRENCE')
                    require(u * (1 - c * eta) ** 2 / (v * (1 - eta) ** 2) == v / u * (1 - (c - 1 / k) * h / (dc * v)) ** 2 / (1 + (1 - 1 / k) * h / (dc * u)) ** 2, 'RATIO_RECURRENCE')
                    checks += 3
    return checks

def one_case(ell_s, c_s, exponent, horizon):
    ell = Decimal(ell_s)
    c = Decimal(c_s)
    kappa = Decimal(10) ** exponent
    nu = ell
    mu = ell
    require(ell.is_finite() and c.is_finite() and kappa.is_finite(), 'FINITE_INPUT')
    require(ell > 0 and Decimal('0.5') <= c < 1 and kappa >= 4 and isinstance(horizon, int) and horizon >= 1, 'DOMAIN_INPUT')
    delta = 1 - c
    d = delta / (1 + c)
    beta = kappa ** (-mu) * d ** (-2 * horizon)
    if beta > delta / 64:
        return None
    eigen = [Decimal(1), c * kappa, kappa]
    energy = [Decimal(1), c ** (-2 * ell - 1) * kappa ** (-1 - nu), kappa ** (-1 - nu)]
    initial = sum(energy)
    step_deviation = Decimal(0)
    for j in range(horizon):
        numerator = sum((lam ** (2 * ell + 1) * mass for lam, mass in zip(eigen, energy)))
        denominator = sum((lam ** (2 * ell + 2) * mass for lam, mass in zip(eigen, energy)))
        alpha = numerator / denominator
        beta_j = kappa ** (-mu) * d ** (-2 * j)
        scaled_deviation = abs(kappa * alpha - 2 / (1 + c)) / (4 * beta_j)
        step_deviation = max(step_deviation, scaled_deviation)
        energy = [mass * (1 - alpha * lam) ** 2 for lam, mass in zip(eigen, energy)]
    scaled_loss = kappa * (1 - sum(energy) / initial)
    centre = 4 * horizon / (1 + c)
    bound = beta + (1 + c ** (-2 * ell - 1)) * kappa ** (-nu) + Decimal(9) * horizon * horizon / (2 * kappa)
    ratio = abs(scaled_loss - centre) / bound
    require(ratio.is_finite() and step_deviation.is_finite(), 'FINITE_RESULT')
    require(ratio <= 1, 'HORIZON_BOUND')
    require(step_deviation <= 1, 'STEP_BOUND')
    return {'ell': ell_s, 'c': c_s, 'kappa_power_of_10': exponent, 'K': horizon, 'decimal_digits': int((1 + ell) * exponent) + 70, 'error_to_proved_bound': float(ratio), 'largest_step_error_to_proved_bound': float(step_deviation), 'scaled_loss_per_step': str(scaled_loss / horizon)}

def main():
    started = time.perf_counter()
    checks = exact_rational_checks()
    records = []
    skipped = 0
    for ell in ['0.1', '0.5', '1', '2']:
        for c in ['0.5', '0.75', '0.9', '0.99']:
            for exponent in [8, 24, 80, 160]:
                for horizon in [1, 2, 5, 10, 20]:
                    with localcontext() as context:
                        context.prec = int((1 + Decimal(ell)) * exponent) + 70
                        result = one_case(ell, c, exponent, horizon)
                    if result is None:
                        skipped += 1
                    else:
                        records.append(result)
    result = {'status': 'PASS', 'scope': 'Finite direct-iterate diagnostics, not proof-assistant verification', 'python': platform.python_version(), 'external_dependencies': [], 'exact_rational_identity_checks': checks, 'passed_instances': len(records), 'outside_hypothesis_skipped': skipped, 'maximum_error_ratio': max((x['error_to_proved_bound'] for x in records)), 'maximum_step_error_ratio': max((x['largest_step_error_to_proved_bound'] for x in records)), 'elapsed_seconds': time.perf_counter() - started, 'instances': records}
    write_receipt(result)
    print(json.dumps({k: v for k, v in result.items() if k != 'instances'}, indent=2))
if __name__ == '__main__':
    main()
