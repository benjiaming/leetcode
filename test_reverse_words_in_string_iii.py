import unittest
from reverse_words_in_string_iii import Solution

class TestSolution(unittest.TestCase):
    def test_reverse_words_in_string_iii(self):
        solution = Solution()
        self.assertEqual(solution.reverseWords(""), "")
        self.assertEqual(solution.reverseWords("  "), "")
        self.assertEqual(solution.reverseWords("Let's take LeetCode   contest"), "s'teL ekat edoCteeL tsetnoc")

if __name__ == '__main__':
    unittest.main()