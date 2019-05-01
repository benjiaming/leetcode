import unittest
from remove_duplicates_from_sorted_array import Solution

class TestSolution(unittest.TestCase):
    def test_remove_duplicates_from_sorted_array(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates([]), 0)
        self.assertEqual(solution.removeDuplicates([1]), 1)
        self.assertEqual(solution.removeDuplicates([1,1]), 1)
        self.assertEqual(solution.removeDuplicates([1,2]), 2)
        self.assertEqual(solution.removeDuplicates([1,1,2]), 2)
        self.assertEqual(solution.removeDuplicates([1,3,3]), 2)
        self.assertEqual(solution.removeDuplicates([1,2,2]), 2)
        self.assertEqual(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)


if __name__ == '__main__':
    unittest.main()