from powerful.composite import Composite


class TestComposite:
    def test_basic(self):
        # arrange
        a = 20

        # act
        b = Composite(a)

        # assert
        assert b == a

    def test_decomposition(self):
        # arrange
        a = 20

        # act
        b = Composite(a)
        b.decompose()

        # assert
        assert b.decomposition[2] == 2
