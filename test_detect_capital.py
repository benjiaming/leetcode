import unittest
from detect_capital import Solution

class TestSolution(unittest.TestCase):
   def test_detect_capital(self):
       solution = Solution()
       self.assertEqual(solution.detectCapitalUse('USA'), True)
       self.assertEqual(solution.detectCapitalUse('flaG'), False)
       self.assertEqual(solution.detectCapitalUse('FlaG'), False)
       self.assertEqual(solution.detectCapitalUse('Flag'), True)
       self.assertEqual(solution.detectCapitalUse('uS'), False)
       self.assertEqual(solution.detectCapitalUse('uSa'), False)


if __name__ == '__main__':
    unittest.main()