import pytest

from powerful.prime import Prime, is_prime


class TestPrime:
    def test_basic(self):
        # arrange
        a = 2

        # act
        result = is_prime(a)

        # assert
        assert result

    def test_big_number(self):
        # arrange
        p = 131

        # act
        result = is_prime(p)

        # assert
        assert result

    def test_arkadii_number(self):
        # arrange
        p = 115756986668303657898962467957

        # act
        result = is_prime(p)

        # assert
        assert result

    def test_miller_rabin_falsehood(self):
        # arrange
        p = 1332141235453512342314655513

        # act
        result = is_prime(p)

        # assert
        assert not result

    def test_prime_creation(self):
        # arrange
        p = 7

        # act
        prime = Prime(p)

        # assert
        assert prime == 7

    def test_prime_creation_failure(self):
        # arrange
        p = 1332141235453512342314655513

        # act
        with pytest.raises(ValueError, match="not prime"):
            Prime(p)

    class TestAdd:
        def test_two_primes(self):
            # arrange
            p1 = Prime(3)
            p2 = Prime(5)

            # act
            result = p1 + p2

            # assert
            assert result == 8

        def test_prime_and_int(self):
            # arrange
            p = Prime(7)
            i = 3

            # act
            result = p + i

            # assert
            assert result == 10

        def test_int_and_prime(self):
            # arrange
            i = 4
            p = Prime(11)

            # act
            result = i + p

            # assert
            assert result == 15

        def test_prime_and_float(self):
            # arrange
            p = Prime(13)
            f = 2.5

            # act
            result = p + f

            # assert
            assert result == 15.5
