
from typing import Literal, assert_never


from powerful.primality_tests import (
    miller_rabin_primality_test,
    trial_division_primality_test,
)

LARGE_PRIME_THRESHOLD = 10000
DEFAULT_LARGE_NUMBER_PRIMALITY_TEST: Literal["miller_rabin", "trial_division"] = (
    "miller_rabin"
)


class Prime(int):
    # Constructor
    def __new__(cls, p: int) -> Self:
        if not is_prime(p):
            raise ValueError(f"{p} is not prime...")

        return super().__new__(cls, p)

    # Representation
    def __repr__(self) -> str:
        return f"Prime({self})"

    def __str__(self) -> str:
        return str(self)
      
def is_prime(p):
    if p < LARGE_PRIME_THRESHOLD:
        return trial_division_primality_test(p)

    if DEFAULT_LARGE_NUMBER_PRIMALITY_TEST == "trial_division":
        return trial_division_primality_test(p)
    elif DEFAULT_LARGE_NUMBER_PRIMALITY_TEST == "miller_rabin":
        return miller_rabin_primality_test(p)
    else:
        assert_never(DEFAULT_LARGE_NUMBER_PRIMALITY_TEST)