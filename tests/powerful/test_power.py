from powerful.power import power_mod


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
