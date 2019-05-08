import unittest
from guess_number import Solution, my_num

class TestSolution(unittest.TestCase):
    def test_guess_number(self):
        solution = Solution()
        self.assertEqual(solution.guessNumber(10), my_num)


if __name__ == '__main__':
    unittest.main()