import unittest
from prepare_meal import prepare_meal 

class PrepareMealTest (unittest.TestCase):

    def test_for_correct_output1(self):
        pass
  #      self.assertEqual("eggs",prepare_meal(5))
    def test_for_correct_output2(self):
        self.assertEqual("spam",prepare_meal(3))
    def test_for_correct_output3(self):
        self.assertEqual("spam spam spam", prepare_meal(27))
    def test_for_correct_output4(self):
        self.assertEqual("spam and eggs",prepare_meal(15))
    def test_for_correct_output5(self):
        self.assertEqual("spam spam and eggs",prepare_meal(45))
    def test_for_correct_output6(self):
        self.assertEqual("",prepare_meal(7))

if __name__ == '__main__':
    unittest.main()