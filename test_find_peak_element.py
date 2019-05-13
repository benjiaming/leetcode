import unittest
from find_peak_element import Solution

class TestSolution(unittest.TestCase):
    def test_find_peak_element(self):
        solution = Solution()
        self.assertEqual(solution.findPeakElement([1,2,3,1]), 2)
        self.assertTrue(solution.findPeakElement([1,2,1,3,5,6,4]) in [1,5])
        self.assertTrue(solution.findPeakElement([2,1,2]) in [0,2])
        self.assertEqual(solution.findPeakElement([1,2,3,1]), 2)
        self.assertEqual(solution.findPeakElement([1]), 0)
        self.assertEqual(solution.findPeakElement([1,3,2,1]), 1)
        


if __name__ == '__main__':
    unittest.main()