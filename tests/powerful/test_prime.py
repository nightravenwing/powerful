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
        assert prime.p == 7

    def test_prime_creation_failure(self):
        # arrange
        p = 1332141235453512342314655513

        # act
        with pytest.raises(ValueError, match="not prime"):
            Prime(p)
