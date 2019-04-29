import unittest
from array_partition import Solution

class TestSolution(unittest.TestCase):
    def test_array_partition(self):
        solution = Solution()
        self.assertEqual(solution.arrayPairSum([1,4,3,2]), 4)
        self.assertEqual(solution.arrayPairSum([1,4]), 1)
        self.assertEqual(solution.arrayPairSum([3,2,5,2,1,4]), 7)
        self.assertEqual(solution.arrayPairSum([1,1,2,2]), 3)

if __name__ == '__main__':
    unittest.main()