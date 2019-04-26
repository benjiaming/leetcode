import unittest
from first_uniq_char import Solution

class TestSolution(unittest.TestCase):
    def test_first_uniq_char(self):
        solution = Solution()
        self.assertEqual(solution.firstUniqChar('leetcode'), 0)
        self.assertEqual(solution.firstUniqChar('loveleetcode'), 2)
        self.assertEqual(solution.firstUniqChar(''), -1)

if __name__ == '__main__':
    unittest.main()