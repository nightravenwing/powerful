from powerful.euclidean import mod_inverse


def quotient_mod(n, a, p):
    inv_a = mod_inverse(a, p)
    return (n * inv_a) % p
