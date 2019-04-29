import unittest
from add_binary import Solution

class TestSolution(unittest.TestCase):
    def test_add_binary(self):
        solution = Solution()
        self.assertEqual(solution.addBinary('0', '0'), '0')
        self.assertEqual(solution.addBinary("11", "1"), '100')
        self.assertEqual(solution.addBinary("1010", "1011"), '10101')


if __name__ == '__main__':
    unittest.main()