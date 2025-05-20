from random import randint

from powerful.power import power_mod

PRIME_THRESHOLD = 10000
MILLER_RABIN_DEFAULT_TRIALS = 60

# for losers who don't like probabilistic tests go eat an atom:
ATOMIC_ACCURACY = 134


class Prime:
    # Constructor
    def __init__(self, p) -> None:
        if not is_prime(p):
            raise ValueError(f"{p} is not prime...")
        else:
            self.p = p

    # Prime Specific Functions

    # Arithmetic
    def __add__(self, other):
        return self.p + other

    def __sub__(self, other):
        return self.p - other

    def __mul__(self, other):
        return self.p * other

    def __truediv__(self, other):
        return self.p / other

    def __floordiv__(self, other):
        return self.p // other

    def __mod__(self, other):
        return self.p % other

    def __pow__(self, other):
        return self.p**other

    # Reflected arithmetic
    def __radd__(self, other):
        return other + self.p

    def __rsub__(self, other):
        return other - self.p

    def __rmul__(self, other):
        return other * self.p

    def __rtruediv__(self, other):
        return other / self.p

    def __rfloordiv__(self, other):
        return other // self.p

    def __rmod__(self, other):
        return other % self.p

    def __rpow__(self, other):
        return other**self.p

    # Unary operations
    def __neg__(self):
        return -self.p

    def __pos__(self):
        return +self.p

    def __abs__(self):
        return abs(self.p)

    # Comparison
    def __eq__(self, other):
        return self.p == other

    def __ne__(self, other):
        return self.p != other

    def __lt__(self, other):
        return self.p < other

    def __le__(self, other):
        return self.p <= other

    def __gt__(self, other):
        return self.p > other

    def __ge__(self, other):
        return self.p >= other

    # Type conversion
    def __int__(self):
        return int(self.p)

    def __float__(self):
        return float(self.p)

    # Representation
    def __repr__(self):
        return f"Prime({self.p})"

    def __str__(self):
        return str(self.p)


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
