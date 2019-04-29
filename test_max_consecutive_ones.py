import unittest
from max_consecutive_ones import Solution

class TestSolution(unittest.TestCase):
    def test_max_consecutive_ones(self):
        solution = Solution()
        self.assertEqual(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)
        self.assertEqual(solution.findMaxConsecutiveOnes([0,0,0,0,0]), 0)
        self.assertEqual(solution.findMaxConsecutiveOnes([1,1,1,1,1]), 5)
        self.assertEqual(solution.findMaxConsecutiveOnes([0,1,1,1,1,1,0]), 5)


if __name__ == '__main__':
    unittest.main()