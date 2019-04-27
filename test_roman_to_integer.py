import unittest
from roman_to_integer import Solution

class TestSolution(unittest.TestCase):
    def test_roman_to_integer(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('III'), 3)
        self.assertEqual(solution.romanToInt('IV'), 4)
        self.assertEqual(solution.romanToInt('IX'), 9)
        self.assertEqual(solution.romanToInt('LVIII'), 58)
        self.assertEqual(solution.romanToInt('MCMXCIV'), 1994)
        self.assertEqual(solution.romanToInt('MCDLXXVI'), 1476)

if __name__ == '__main__':
    unittest.main()