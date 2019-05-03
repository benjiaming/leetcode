import unittest
from intersection_of_two_arrays_ii import Solution

class TestSolution(unittest.TestCase):
    def test_intersection_of_two_arrays(self):
        solution = Solution()
        self.assertEqual(sorted(solution.intersect([1,2,2,1], [2,2])), [2,2])
        self.assertEqual(sorted(solution.intersect([4,9,5], [9,4,9,8,4])), [4,9])


if __name__ == '__main__':
    unittest.main()