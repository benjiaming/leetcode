import unittest
from plus_one import Solution

class TestSolution(unittest.TestCase):
    def test_plus_one(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(solution.plusOne([4,3,2,1]), [4,3,2,2])
        self.assertEqual(solution.plusOne([1,2,9]), [1,3,0])
        self.assertEqual(solution.plusOne([9,9,9]), [1,0,0,0])
        self.assertEqual(solution.plusOne([]), [1])
        self.assertEqual(solution.plusOne([0]), [1])


if __name__ == '__main__':
    unittest.main() 