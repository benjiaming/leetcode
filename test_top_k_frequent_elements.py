import unittest
from top_k_frequent_elements import Solution

class TestSolution(unittest.TestCase):
    def test_top_k_frequent_elements(self):
        solution = Solution()
        self.assertEqual(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2), [1,2])
        self.assertEqual(solution.topKFrequent(nums = [1], k = 1), [1])


if __name__ == '__main__':
    unittest.main()