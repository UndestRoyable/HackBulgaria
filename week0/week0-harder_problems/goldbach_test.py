import unittest
from goldbach import is_prime
from goldbach import goldbach

class GoldbachTest(unittest.TestCase):

    def test_is_prime_function(self):
        
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(-10))



    def test_if_goldbach_returns_corect_data(self):
        self.assertEqual([(2,2)], goldbach(4))

if __name__ == '__main__':
    unittest.main()
