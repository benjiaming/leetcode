import unittest
from string_compression import Solution

class TestSolution(unittest.TestCase):
    def test_string_compression(self):
        solution = Solution()
        input = ["a","a","b","b","c","c","c"]
        self.assertEqual(solution.compress(input), 6)
        input = ["a"]
        self.assertEqual(solution.compress(input), 1)
        input = []
        self.assertEqual(solution.compress(input), 0)
        input = ["a", "a"]
        self.assertEqual(solution.compress(input), 2)
        input = ["a","b"]
        self.assertEqual(solution.compress(input), 2)
        input = ["a","b","c"]
        self.assertEqual(solution.compress(input), 3)
        input = ["a","b","c","d","d","e","e","e","e","e","a","b","c","c","c","c","c","d"]
        self.assertEqual(solution.compress(input), 12)

if __name__ == '__main__':
    unittest.main()