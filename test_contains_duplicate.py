import unittest
from contains_duplicate import Solution

class TestSolution(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([]), False)
        self.assertEqual(solution.containsDuplicate([0]), False)
        self.assertEqual(solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
        

if __name__ == '__main__':
    unittest.main()