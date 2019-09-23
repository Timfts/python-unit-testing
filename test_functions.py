from unittest import TestCase
from functions import divide, multiply

class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expect_result = 5.0

        self.assertAlmostEqual(divide(dividend,divisor), expect_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0

        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)
    
    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0

        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        self.assertRaises(ValueError, lambda: divide(25, 0))

    def test_multiply_empty(self):
        self.assertRaises(ValueError, lambda: multiply())

    def test_multiply_different_values(self):
        self.assertEqual(multiply(2,2), 4)
        self.assertEqual(multiply(1,5,6), 30)

    def test_multiply_zero(self):
        self.assertEqual(multiply(1,2,4,0), 0)
        self.assertEqual(multiply(1,0), 0)
        self.assertEqual(multiply(0), 0)
        self.assertEqual(multiply(0,0), 0)
    
    def test_multiply_negative(self):
        self.assertEqual(multiply(1,-2,4,2), -16)
        self.assertEqual(multiply(-1,0), 0)
        self.assertEqual(multiply(-2, -5), 10)
