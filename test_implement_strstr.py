import unittest
from implement_strstr import Solution

class TestSolution(unittest.TestCase):
    def test_implement_strstr(self):
        solution = Solution()
        # self.assertEqual(solution.strStr("hello", "ll"), 2)
        # self.assertEqual(solution.strStr("aaaaa", "bba"), -1)
        # self.assertEqual(solution.strStr("hello", ""), 0)
        self.assertEqual(solution.strStr("a", "a"), 0)

if __name__ == '__main__':
    unittest.main() 