import unittest
from reduce_file_path import reduce_file_path

class ReduceFilePathTest(unittest.TestCase):
    def test_correct_output(self):
        self.assertEqual("/",reduce_file_path("/"))
    def test_correct_output1(self):
        self.assertEqual("/",reduce_file_path("/srv/../"))
    def test_correct_output2(self):
        self.assertEqual("/srv/www/htdocs/wtf",reduce_file_path("/srv/www/htdocs/wtf/"))
    def test_correct_output3(self):
        self.assertEqual("/srv/www/htdocs/wtf",reduce_file_path("/srv/www/htdocs/wtf"))
    def test_correct_output4(self):
        self.assertEqual("/srv",reduce_file_path("/srv/./././././"))
    def test_correct_output5(self):
        self.assertEqual("/etc/wtf",reduce_file_path("/etc//wtf/"))
    def test_correct_output6(self):
        self.assertEqual("/",reduce_file_path("/etc/../etc/../etc/../"))
    def test_correct_output7(self):
        self.assertEqual("/",reduce_file_path("//////////////"))
    def test_correct_output8(self):
        self.assertEqual("/",reduce_file_path("/../"))


if __name__ == '__main__':
    unittest.main()