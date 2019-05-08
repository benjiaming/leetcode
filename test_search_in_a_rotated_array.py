import unittest
from search_in_a_rotated_array import Solution

class TestSolution(unittest.TestCase):
    def test_search_in_a_rotated_array(self):
        solution = Solution()
        self.assertEqual(solution.search(nums = [4,5,6,7,0,1,2], target = 0), 4)
        self.assertEqual(solution.search(nums = [4,5,6,7,0,1,2], target = 3), -1)

        self.assertEqual(solution.search(nums = [4,5,6,7,8,9,10,0,1,2], target = 3), -1)
        self.assertEqual(solution.search(nums = [4,5,6,7,0,1,2], target = 5), 1)
        self.assertEqual(solution.search(nums = [4,5,6,7,0], target = 6), 2)

        self.assertEqual(solution.search(nums = [3,1,2], target = 3), 0)
        self.assertEqual(solution.search(nums = [2,1], target = 3), -1)
        self.assertEqual(solution.search(nums = [2,1], target = 1), 1)
        self.assertEqual(solution.search(nums = [2], target = 3), -1)
        self.assertEqual(solution.search(nums = [2], target = 2), 0)

if __name__ == '__main__':
    unittest.main()