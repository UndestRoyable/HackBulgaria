from is_an_bn import is_an_bn
import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_an_bn(""))

    def test_two(self):
        self.assertFalse(is_an_bn("rado"))

    def test_three(self):
        self.assertFalse(is_an_bn("aaabb"))

    def test_four(self):
        self.assertTrue(is_an_bn("aaabbb"))

    def test_five(self):
        self.assertFalse(is_an_bn("aabbaabb"))

    def test_six(self):
        self.assertFalse(is_an_bn("bbbaaa"))

    def test_seven(self):
        self.assertTrue(is_an_bn("aaaaabbbbb"))


if __name__ == '__main__':
    unittest.main()
