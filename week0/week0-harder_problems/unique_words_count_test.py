import unittest
from unique_words_count import unique_words_count


class UniqueWordsCountTest(unittest.TestCase):

    def test_if_unique_words_count_counts_correct(self):
        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))

    def test_if_unique_words_count_counts_correct2(self):
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))

    def test_if_unique_words_count_counts_correct3(self):
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()
