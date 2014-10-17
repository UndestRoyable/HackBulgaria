from is_an_bn import is_an_bn
import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):

        self.assertTrue(is_an_bn(""))
        
        self.assertFalse(is_an_bn("rado"))

        self.assertFalse(is_an_bn("aaabb"))

        self.assertTrue(is_an_bn("aaabbb"))

        self.assertFalse(is_an_bn("aabbaabb"))

        self.assertFalse(is_an_bn("bbbaaa"))

        self.assertTrue(is_an_bn("aaaaabbbbb"))



if __name__ == '__main__':
    unittest.main()
