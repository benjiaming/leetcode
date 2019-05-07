import unittest
from binary_search import Solution

class TestSolution(unittest.TestCase):
    def test_binary_search(self):
        solution = Solution()
        self.assertEqual(solution.search(nums = [-1,0,3,5,9,12], target = 9), 4)
        self.assertEqual(solution.search(nums = [-1,0,3,5,9,12], target = 2), -1)


if __name__ == '__main__':
    unittest.main()