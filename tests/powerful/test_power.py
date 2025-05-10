from powerful.power import PowerMod


class TestPowerMod:
    def test_basic(self):
        # Arrange
        a = 1
        b = 1
        c = 1

        # Act
        result = PowerMod(a, b, c)

        # Assert
        assert result == 1
