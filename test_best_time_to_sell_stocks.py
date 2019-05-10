import unittest
from best_time_to_sell_stocks import Solution

class TestSolution(unittest.TestCase):
    def test_best_time_to_sell_stocks(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), 0)


if __name__ == '__main__':
    unittest.main()