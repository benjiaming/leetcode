import unittest
from four_sum_ii import Solution

class TestSolution(unittest.TestCase):
    def test_4sum_ii(self):
        solution = Solution()
        self.assertEqual(solution.fourSumCount([1, 2], [-2,-1], [-1, 2], [0, 2]), 2)


if __name__ == '__main__':
    unittest.main()