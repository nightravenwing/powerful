from powerful.euclidean import extended_euclidean, mod_inverse


def quotient_mod_unique(n: int, a: int, p: int) -> int:
    try:
        inv_a = mod_inverse(a, p)  # modular inverse of a mod p
        return (n * inv_a) % p
    except ValueError:
        raise ValueError("No Unique Solution")


def quotient_mod(n: int, a: int, p: int) -> list[int]:
    d, _, _ = extended_euclidean(a, p)
    if n % d != 0:
        return []  # No solution exists

    a1 = a // d
    n1 = n // d
    p1 = p // d

    try:
        inv_a1 = quotient_mod_unique(1, a1, p1)
    except ValueError:
        raise ValueError("No inverse upon reduction")

    x0 = (n1 * inv_a1) % p1
    return [(x0 + k * p1) % p for k in range(d)]
