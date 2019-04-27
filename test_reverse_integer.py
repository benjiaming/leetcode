import unittest
from reverse_integer import Solution

class TestSolution(unittest.TestCase):
    def test_reverse_integer(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(+123), 321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)
        self.assertEqual(solution.reverse(1534236469), 0)        
      
        self.assertEqual(solution.reverse_math(123), 321)
        self.assertEqual(solution.reverse_math(-123), -321)
        self.assertEqual(solution.reverse_math(+123), 321)
        self.assertEqual(solution.reverse_math(120), 21)
        self.assertEqual(solution.reverse_math(0), 0)
        self.assertEqual(solution.reverse_math(1534236469), 0)        

if __name__ == '__main__':
    unittest.main()