import unittest
from DAY_1_PRIME_GENERATOR.program import prime_list


class PrimeGeneratorTest(unittest.TestCase):

    # First test: Passed argument is an integer.
    def test_number_is_integer(self):
        self.assertRaises(TypeError, prime_list, number='Damn')

    # Second test: Passed argument is greater than 0
    def test_number_is_greater_than_zero(self):
        self.assertRaises(ValueError, prime_list, number=0)
        self.assertRaises(ValueError, prime_list, number=-29)

    # Third test: Function returns a list
    def test_function_returns_list(self):
        self.assertTrue(type(prime_list(8)) is list, msg='Function not returning a list')

    # Fourth test: Function returns correct value when number is one
    def test_function_returns_correct_value_when_number_is_one(self):
        self.assertEqual(prime_list(1), [1], msg='Function returns wrong values when number is one')

    # Fifth test: Function returns correct value when number is two
    def test_function_returns_correct_value_when_number_is_two(self):
        self.assertEqual(prime_list(2), [1, 2], msg='Function returns wrong values when number is two')

    # Sixth test: Function returns correct value when number is prime
    def test_function_returns_correct_value_when_number_is_prime(self):
        self.assertEqual(prime_list(7), [1, 2, 3, 5, 7], msg='Function returns wrong values when number is prime')

    # Seventh test: Function returns correct value when number is non-prime
    def test_function_returns_correct_value_when_number_is_non_prime(self):
        self.assertEqual(prime_list(4), [1, 2, 3], msg='Function returns wrong values when number is non prime')

if __name__ == '__main__':
    unittest.main()
