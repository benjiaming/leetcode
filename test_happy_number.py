import unittest
from happy_number import Solution

class TestSolution(unittest.TestCase):
    def test_happy_number(self):
        solution = Solution()
        self.assertEqual(solution.isHappy(1), True)
        self.assertEqual(solution.isHappy(11), False)
        self.assertEqual(solution.isHappy(12), False)
        self.assertEqual(solution.isHappy(19), True)
        self.assertEqual(solution.isHappy(100), True)

if __name__ == '__main__':
    unittest.main()