import unittest
from isomorphic_strings import Solution

class TestSolution(unittest.TestCase):
    def test_isomorphic_strings_dict(self):
        solution = Solution()
        self.assertEqual(solution.isIsomorphic_dict('egg', 'add'), True)
        self.assertEqual(solution.isIsomorphic_dict('foo', 'bar'), False)
        self.assertEqual(solution.isIsomorphic_dict('paper', 'title'), True)
        self.assertEqual(solution.isIsomorphic_dict('ab', 'aa'), False)
        self.assertEqual(solution.isIsomorphic_dict('a', 'a'), True)
        self.assertEqual(solution.isIsomorphic_dict('ab', 'dd'), False)

    def test_isomorphic_strings(self):
        solution = Solution()
        self.assertEqual(solution.isIsomorphic('egg', 'add'), True)
        self.assertEqual(solution.isIsomorphic('foo', 'bar'), False)
        self.assertEqual(solution.isIsomorphic('paper', 'title'), True)
        self.assertEqual(solution.isIsomorphic('ab', 'aa'), False)
        self.assertEqual(solution.isIsomorphic('a', 'a'), True)
        self.assertEqual(solution.isIsomorphic('ab', 'dd'), False)

if __name__ == '__main__':
    unittest.main()