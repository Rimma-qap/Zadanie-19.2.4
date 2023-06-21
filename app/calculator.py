class Calculator:
    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ValueError("На ноль делить нельзя")

    def subtraction(self, x, y):
        return x - y

    def adding(self, x, y):
        return x + y
