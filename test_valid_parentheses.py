import unittest
from valid_parentheses import Solution

class TestSolution(unittest.TestCase):
    def test_valid_parentheses(self):
        solution = Solution()
        self.assertEqual(solution.isValid('()'), True)
        self.assertEqual(solution.isValid("()[]{}"), True)
        self.assertEqual(solution.isValid("(]"), False)
        self.assertEqual(solution.isValid("([)]"), False)
        self.assertEqual(solution.isValid("{[]}"), True)
        self.assertEqual(solution.isValid("]"), False)
        self.assertEqual(solution.isValid("["), False)


if __name__ == '__main__':
    unittest.main()