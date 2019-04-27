import unittest
from dominant_index import Solution

class TestSolution(unittest.TestCase):
    def test_dominant_index(self):
        solution = Solution()
        self.assertEqual(solution.dominantIndex([3, 6, 1, 0]), 1)
        self.assertEqual(solution.dominantIndex([1, 2, 3, 4]), -1)
        self.assertEqual(solution.dominantIndex([]), -1)
        self.assertEqual(solution.dominantIndex([1]), 0)
        self.assertEqual(solution.dominantIndex([0]), 0)
        self.assertEqual(solution.dominantIndex([-1, -3, -5, 1]), 3)
        self.assertEqual(solution.dominantIndex([-10, -7, -5, -10]), 2)


if __name__ == '__main__':
    unittest.main()