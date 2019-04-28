import unittest
from spiral_matrix import Solution

class TestSolution(unittest.TestCase):
    def test_spiral_matrix(self):
        solution = Solution()
        self.assertEqual(solution.spiralOrder([]), [])
        self.assertEqual(solution.spiralOrder([[]]), [])
        self.assertEqual(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), [1,2,3,4,8,12,11,10,9,5,6,7])
        self.assertEqual(solution.spiralOrder([[1,2,3]]), [1,2,3])
        self.assertEqual(solution.spiralOrder([[1],[2],[3]]), [1,2,3])
        self.assertEqual(solution.spiralOrder([[1,2],[3,4],[5,6]]), [1,2,4,6,5,3])


if __name__ == '__main__':
    unittest.main() 