def power_mod(x: int, n: int, p: int) -> int:
    binary = bin(n)
    has_reached_one = False
    m = x % p

    for i in binary[2 : len(binary)]:
        if has_reached_one:
            m = m**2 % p

            if i == "1":
                m = m * x % p

        if not has_reached_one and i == "1":
            has_reached_one = True

    return m
