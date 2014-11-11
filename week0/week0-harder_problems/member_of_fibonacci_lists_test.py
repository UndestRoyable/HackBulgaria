import unittest
from member_of_fibonacci_lists import member_of_nth_fib_lists


class FibonacciListsTest(unittest.TestCase):

    def test_for_corect_output_true(self):
        # return True tests
        self.assertTrue(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
        self.assertTrue(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))

    def test_for_corect_output_false(self):
        #return False tests
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertFalse(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    unittest.main()
