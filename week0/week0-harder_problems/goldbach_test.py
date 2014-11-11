import unittest
from goldbach import is_prime
from goldbach import goldbach


class GoldbachTest(unittest.TestCase):

    def test_is_prime_function1(self):

        self.assertFalse(is_prime(1))

    def test_is_prime_function2(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_function3(self):
        self.assertFalse(is_prime(8))

    def test_is_prime_function4(self):
        self.assertTrue(is_prime(11))

    def test_is_prime_function5(self):
        self.assertFalse(is_prime(-10))

    def test_if_goldbach_returns_corect_data(self):
        self.assertEqual([(2, 2)], goldbach(4))

if __name__ == '__main__':
    unittest.main()
