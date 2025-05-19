from powerful.quotient import quotient_mod


class TestQuotientMod:
    def test_basic(self):
        # arrange
        a = 2
        b = 5
        c = 13

        # act
        result = quotient_mod(a, b, c)

        # assert
        assert result[0] == 3

    def test_arkadii_numbers(self):
        # arrange
        a = 777777
        b = 85015134546569
        c = 747528518238452134859

        # act
        result = quotient_mod(a, b, c)

        # assert
        assert result[0] == 46066459150768868266

    def test_multiple_solutions(self):
        # arrange
        a = 2
        b = 4
        c = 8

        # act
        result = quotient_mod(b, a, c)

        # assert
        assert result == [2, 6]

    def test_no_solutions(self):
        # arrange
        a = 4
        b = 5
        c = 8

        # act
        result = quotient_mod(b, a, c)

        # assert
        assert result == []
