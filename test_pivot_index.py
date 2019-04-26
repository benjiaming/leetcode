import unittest
from pivot_index import Solution

class TestSolution(unittest.TestCase):
    def test_pivot_index(self):
        solution = Solution()
        self.assertEqual(solution.pivotIndex([1, 7, 3, 6, 5, 6]), 3) # 11 == 11 @ [3]
        self.assertEqual(solution.pivotIndex([1, 2, 3]), -1) # no pivot
        self.assertEqual(solution.pivotIndex([-1, -1, -1, -1, -1, 0]), 2) # -2 == -2 @ [2]
        self.assertEqual(solution.pivotIndex([-1, -1, -1, -1, 0, 1]), 1) # -1 == -1 @ [1]
        self.assertEqual(solution.pivotIndex([-1, -1, -1, 0, 1, 1]), 0) # 0 == 0 @ [0] (most left pivot)
        self.assertEqual(solution.pivotIndex([-1, -1, 0, 1, 1, 0]), 5)  # 0 == 0 @ [5] (right most pivot)    
        self.assertEqual(solution.pivotIndex([-1, -1, 0, 1, 1, -1]), 0) # 0 == 0 @ [0] (most left pivot)       
        self.assertEqual(solution.pivotIndex([-1, -1, 1, 1, 0, 0]), 4)  # 0 == 0 @ [4] (second right most pivot)      


if __name__ == '__main__':
    unittest.main()