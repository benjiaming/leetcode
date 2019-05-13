import unittest
from one_away import Solution

class TestSolution(unittest.TestCase):
    def test_one_away(self):
        solution = Solution()
        self.assertEqual(solution.isOneAway('pale', 'pale'), True)
        self.assertEqual(solution.isOneAway('pale', 'ple'), True)
        self.assertEqual(solution.isOneAway('pales', 'pale'), True)
        self.assertEqual(solution.isOneAway('pale', 'bale'), True)
        self.assertEqual(solution.isOneAway('pale', 'bake'), False)
        self.assertEqual(solution.isOneAway('p', 'bake'), False)
        self.assertEqual(solution.isOneAway('p', 'b'), True)
        self.assertEqual(solution.isOneAway('p', ''), True)
        self.assertEqual(solution.isOneAway('', ''), True)
        self.assertEqual(solution.isOneAway('', 'x'), True)
        self.assertEqual(solution.isOneAway('', 'xx'), False)
        self.assertEqual(solution.isOneAway('a', 'xx'), False)
        self.assertEqual(solution.isOneAway('a', 'xa'), True)
        self.assertEqual(solution.isOneAway('a', 'xaa'), False)

if __name__ == '__main__':
    unittest.main()