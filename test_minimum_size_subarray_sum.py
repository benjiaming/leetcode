import unittest
from minimum_size_subarray_sum import Solution

class TestSolution(unittest.TestCase):
    def test_minimum_size_subarray_sum(self):
        solution = Solution()
        self.assertEqual(solution.minSubArrayLen(7,[2,3,1,2,4,3]), 2)
        self.assertEqual(solution.minSubArrayLen(8,[2,3,1,2,4,3]), 3)


if __name__ == '__main__':
    unittest.main()