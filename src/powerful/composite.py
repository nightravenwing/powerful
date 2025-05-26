from powerful.prime import is_prime


class Composite(int):
    # Constructor
    def __new__(cls, p: int):
        if is_prime(p):
            raise ValueError(f"{p} is a prime number!...")

        return super().__new__(cls, p)

    def decompose(self):
        self.decomposition = Decomposition(self)


class Decomposition(dict):
    def __new__(cls, n: int):
        decomp = {}
        a = 2
        rootn = int(n**0.5) + 1
        while a <= rootn and n > 1:
            if n % a == 0:
                decomp[a] = decomp.get(a, 0) + 1
                n = n // a
                rootn = int(n**0.5) + 1
            else:
                a += 1
        if n > 1:
            decomp[n] = decomp.get(n, 0) + 1
        return decomp
