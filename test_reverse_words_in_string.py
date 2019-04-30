import unittest
from reverse_words_in_string import Solution

class TestSolution(unittest.TestCase):
    def test_reverse_words_in_string(self):
        solution = Solution()
        self.assertEqual(solution.reverseWords(""), "")
        self.assertEqual(solution.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(solution.reverseWords("  hello world!  "), "world! hello")
        self.assertEqual(solution.reverseWords("a good   example"), "example good a")


if __name__ == '__main__':
    unittest.main()