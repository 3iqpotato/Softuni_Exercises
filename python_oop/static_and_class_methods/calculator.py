import math


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        x = args[0]
        for y in args[1:]:
            x *= y

        return x

    @staticmethod
    def divide(*args):
        x = args[0]
        for y in args[1:]:
            x /= y

        return x

    @staticmethod
    def subtract(*args):
        x = args[0]
        for y in args[1:]:
            x -= y
        return x


import unittest


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(5, 10, 4)
        self.assertEqual(result, 19)

    def test_multiply(self):
        result = Calculator.multiply(1, 2, 3, 5)
        self.assertEqual(result, 30)

    def test_divide(self):
        result = Calculator.divide(100, 2)
        self.assertEqual(result, 50.0)

    def test_subtract(self):
        result = Calculator.subtract(90, 20, -50, 43, 7)
        self.assertEqual(result, 70)


if __name__ == "__main__":
    unittest.main()
