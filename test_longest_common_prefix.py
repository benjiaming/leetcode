import unittest
from longest_common_prefix import Solution

class TestSolution(unittest.TestCase):
    def test_longest_common_prefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), 'fl')
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), '')
        self.assertEqual(solution.longestCommonPrefix(["aa","a"]), "a")


if __name__ == '__main__':
    unittest.main()