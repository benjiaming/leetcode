import unittest
from remove_element import Solution

class TestSolution(unittest.TestCase):
    def test_remove_element(self):
        solution = Solution()
        self.assertEqual(solution.removeElement([3,2,2,3], 3), 2)
        self.assertEqual(solution.removeElement([0,1,2,2,3,0,4,2], 2), 5)
        self.assertEqual(solution.removeElement([], 2), 0)


if __name__ == '__main__':
    unittest.main()