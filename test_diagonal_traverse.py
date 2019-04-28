import unittest
from diagonal_traverse import Solution

class TestSolution(unittest.TestCase):
    def test_diagonal_traverse(self):
        solution = Solution()
        self.assertEqual(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(solution.findDiagonalOrder([]), [])
        self.assertEqual(solution.findDiagonalOrder([[2,3]]), [2,3])
        self.assertEqual(solution.findDiagonalOrder([[2,5],[8,4],[0,-1]]), [2,5,8,0,4,-1])
        self.assertEqual(solution.findDiagonalOrder([[1,2,3,4,5,6,7,8,9,10]]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(solution.findDiagonalOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(solution.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [1,2,5,9,6,3,4,7,10,13,14,11,8,12,15,16])

if __name__ == '__main__':
    unittest.main()

