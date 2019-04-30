import unittest
from pascal_triangle_ii import Solution

class TestSolution(unittest.TestCase):
    def test_pascal_triangle_ii(self):
        solution = Solution()
        self.assertEqual(solution.getRow(0), [1])
        self.assertEqual(solution.getRow(1), [1,1])
        self.assertEqual(solution.getRow(2), [1,2,1])
        self.assertEqual(solution.getRow(3), [1,3,3,1])
        self.assertEqual(solution.getRow(4), [1,4,6,4,1])
        self.assertEqual(solution.getRow(5), [1,5,10,10,5,1])        


if __name__ == '__main__':
    unittest.main()