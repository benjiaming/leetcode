import unittest
from intersection_of_two_arrays import Solution

class TestSolution(unittest.TestCase):
    def test_intersection_of_two_arrays(self):
        solution = Solution()
        self.assertEqual(solution.intersection([1,2,2,1], [2,2]), [2])
        self.assertEqual(solution.intersection([4,9,5], [9,4,9,8,4]), [9,4])


if __name__ == '__main__':
    unittest.main()