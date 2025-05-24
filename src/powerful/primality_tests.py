"""This module gives various tests for primality.

Some of these tests are probabilistic, while others are deterministic.
"""

from numbers import Integral
from random import randint

from powerful.power import power_mod

MILLER_RABIN_DEFAULT_TRIALS = 60


def trial_division_primality_test(p: Integral) -> bool:
    return all(p % i != 0 for i in range(2, int(p**0.5)))


def miller_rabin_primality_test(p, trial_quantity: int = MILLER_RABIN_DEFAULT_TRIALS):
    d, r = p - 1, 0
    while d % 2 == 0:
        d = d // 2
        r = r + 1
    for _ in range(trial_quantity):
        a = randint(2, p - 1)
        x = power_mod(a, d, p)

        if x == 1 or x == p - 1:
            continue

        for _ in range(r - 1):
            x = power_mod(x, 2, p)

            if x == p - 1:
                break
            else:
                return False
    return True
