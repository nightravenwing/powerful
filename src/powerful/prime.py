from random import random
from powerful.power import power_mod


PRIME_THRESHOLD = 10000
MILLER_RABIN_DEFAULT_TRIALS = 60


class Prime:
    def __init__(self, p) -> None:
        if not is_prime(p):
            raise ValueError(f"{p} is not prime...")
        else:
            self.p = p

    def __add__(self, n):
        return self.p + n

    def __sub__(self, n):
        return self.p - n


def is_prime(p):
    if p < PRIME_THRESHOLD:
        return __is_genuine_prime(p)
    else:
        return miller_rabin_primality_test(p, MILLER_RABIN_DEFAULT_TRIALS)


def __is_genuine_prime(p):
    for i in range(2, int(p**0.5)):
        if p % i == 0:
            return False
        else:
            return True


def miller_rabin_primality_test(p, trial_quantity):
    d, r = n - 1, 0
    while d % 2 == 0:
        d = d / 2
        r = r + 1
    for _ in range(trial_quantity):
        a = random.randrange(2, p - 1)
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
