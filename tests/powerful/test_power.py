from powerful.power import power_mod
from powerful.prime import Prime


class TestPowerMod:
    def test_basic(self):
        # Arrange
        a = 1
        b = 1
        c = 1

        # Act
        result = power_mod(a, b, c)

        # Assert
        assert result == 0

    def test_mixed(self):
        # Arrange
        a = 2
        b = 3
        c = 4

        # Act
        result = power_mod(a, b, c)

        # Assert
        assert result == 0

    def test_high_numbers(self):
        # Arrange
        a = 11111
        b = 2345
        c = 17

        # Act
        result = power_mod(a, b, c)

        # Assert (tested with GAP)
        assert result == 7

    def test_arkadii_numbers(self):
        # Arrange
        a = 4919804113995030623
        b = 4568442163565
        c = 747528518238452134859

        # Act
        result = power_mod(a, b, c)

        # assert
        assert result == 711191711059966602217

    def test_prime(self):
        # arrange
        a = 4
        b = 2
        p = Prime(13)

        # act
        result = power_mod(a, b, p)

        # arrange
        assert result == 3
