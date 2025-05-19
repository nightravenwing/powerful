from powerful.euclidean import extended_euclidean, mod_inverse


class TestExtendedEuclidean:
    def test_basic(self):
        # arrange
        a = 1
        b = 1

        # Act
        result = extended_euclidean(a, b)

        # Assert
        assert result == (1, 0, 1)

    def test_gcd_one_two(self):
        # arrange
        a = 1
        b = 2

        # Act
        result, _, _ = extended_euclidean(a, b)

        # assert
        assert result == 1

    def test_even(self):
        # arrange
        a = 2
        b = 4
        c = 6
        d = 10

        # Act
        result_one = extended_euclidean(a, b)
        result_two = extended_euclidean(b, c)
        result_three = extended_euclidean(b, d)
        # Assert
        assert result_one == (2, 1, 0)
        assert result_two == (2, -1, 1)
        assert result_three == (2, -2, 1)

    def test_inverse(self):
        # arrange
        p = 13
        a = 5
        b = 6

        # act
        result_1 = mod_inverse(a, p)
        result_2 = mod_inverse(b, p)

        # assert
        assert result_1 == 8
        assert result_2 == 11

    def test_not_coprime(self):
        # arrange
        p = 10
        a = 5

        # act
        try:
            result = mod_inverse(a, p)
        except ValueError:
            print(ValueError)
            result = "Error"

        # assert
        assert result == "Error"

    def test_arkadii_numbers(self):
        # arrange
        p = 747528518238452134859
        a = 85015134546569

        # act
        result = mod_inverse(a, p)

        # assert
        assert result == 387364492044334893871
