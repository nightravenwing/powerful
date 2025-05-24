from numbers import Integral, Number
from random import randint

from powerful.power import power_mod

PRIME_THRESHOLD = 10000
MILLER_RABIN_DEFAULT_TRIALS = 60

# for losers who don't like probabilistic tests go eat an atom:
ATOMIC_ACCURACY = 134


class Prime(int):
    # Constructor
    def __new__(cls, p):
        if not is_prime(p):
            raise ValueError(f"{p} is not prime...")

        return super().__new__(cls, p)

    # Representation
    def __repr__(self):
        return f"Prime({self})"

    def __str__(self):
        return str(self)


def is_prime(p):
    if p < PRIME_THRESHOLD:
        return __is_genuine_prime(p)
    else:
        return miller_rabin_primality_test(p, MILLER_RABIN_DEFAULT_TRIALS)


def __is_genuine_prime(p):
    for i in range(2, int(p**0.5)):  # noqa: SIM110
        if p % i == 0:
            return False

    return True


def miller_rabin_primality_test(p, trial_quantity):
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
