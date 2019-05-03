import unittest
from contains_duplicate_ii import Solution

class TestSolution(unittest.TestCase):
    def test_contains_duplicate_ii(self):
        solution = Solution()
        self.assertEqual(solution.containsNearbyDuplicate([1,2,3,1], 3), True)
        self.assertEqual(solution.containsNearbyDuplicate([1,0,1,1], 1), True)
        self.assertEqual(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2), False)
        self.assertEqual(solution.containsNearbyDuplicate([1], 2), False)
        self.assertEqual(solution.containsNearbyDuplicate([], 2), False)


if __name__ == '__main__':
    unittest.main()