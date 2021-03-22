from pytest import raises
from Day1.main import get_multiplication


class TestDay1:
    def test_two_numbers(self):
        assert get_multiplication(2020, 2) == 365619

    def test_three_numbers(self):
        assert get_multiplication(2020, 3) == 236873508

    def test_no_numbers(self):
        assert get_multiplication(2020, 0) == 0

    def test_sum_value_zero(self):
        assert get_multiplication(0, 2) == 0

    def test_bad_values_provided(self):
        with raises(TypeError):
            get_multiplication("a", "b")

    def test_missing_arguments(self):
        with raises(TypeError):
            get_multiplication()
