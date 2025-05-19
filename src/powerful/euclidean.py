from powerful.power import power_mod
from powerful.prime import Prime


def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)


def mod_inverse(a, p):
    if type(p) is Prime:
        return power_mod(a, p - 1, p)
    gcd, x, _ = extended_euclidean(a, p)
    if gcd != 1:
        raise ValueError("NOT COPRIME: GCD ", gcd)
    return x % p
