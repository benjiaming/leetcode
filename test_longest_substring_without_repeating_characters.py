import unittest
from longest_substring_without_repeating_characters import Solution

class TestSolution(unittest.TestCase):
    def test_longest_substring_without_repeating_characters(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("abba"), 2)
        


if __name__ == '__main__':
    unittest.main()