from app.calculator import Calculator
import pytest


class TestCalc:
    def setup_class(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 30, 5) == 35

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 30, 5) == 25

    def test_division_success(self):
        assert self.calc.division(self, 30, 5) == 6

        with pytest.raises(ValueError) as exc_info:
            self.calc.division(self, 30, 0)
        assert exc_info.value.args[0] == "На ноль делить нельзя"

    def test_multiply_success(self):
        assert self.calc.multiply(self, 30, 5) == 150

    def teardown(self):
        print("Тест успешно пройден")
