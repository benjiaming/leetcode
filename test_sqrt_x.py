import unittest
from sqrt_x import Solution

class TestSolution(unittest.TestCase):
    def test_sqrt_x(self):
        solution = Solution()    
        self.assertEqual(solution.mySqrt(0), 0)
        self.assertEqual(solution.mySqrt(4), 2)
        self.assertEqual(solution.mySqrt(8), 2)
        self.assertEqual(solution.mySqrt(10), 3)
        self.assertEqual(solution.mySqrt(15), 3)
        self.assertEqual(solution.mySqrt(16), 4)
        self.assertEqual(solution.mySqrt(20), 4)
        self.assertEqual(solution.mySqrt(24), 4)
        self.assertEqual(solution.mySqrt(25), 5)
        self.assertEqual(solution.mySqrt(100), 10)
        self.assertEqual(solution.mySqrt(101), 10)
        self.assertEqual(solution.mySqrt(1234567890), 35136)
        self.assertEqual(solution.mySqrt(519194475), 22785
)

if __name__ == '__main__':
    unittest.main()