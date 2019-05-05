import unittest
from jewels_and_stones import Solution

class TestSolution(unittest.TestCase):
    def test_jewels_and_stones(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(solution.numJewelsInStones("z", "ZZ"), 0)

if __name__ == '__main__':
    unittest.main()