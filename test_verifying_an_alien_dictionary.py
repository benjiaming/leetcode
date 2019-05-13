import unittest
from verifying_an_alien_dictionary import Solution

class TestSolution(unittest.TestCase):
    def test_verifying_an_alien_dictionary(self):
        solution = Solution()
        self.assertTrue(solution.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
        self.assertFalse(solution.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
        self.assertFalse(solution.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))


if __name__ == '__main__':
    unittest.main()