import unittest
from pascal_triangle import Solution

class TestSolution(unittest.TestCase):
    def test_pascal_triangle(self):
        solution = Solution()
        self.assertEqual(solution.generate(0), [])
        self.assertEqual(solution.generate(1), [[1]])
        self.assertEqual(solution.generate(2), [[1],[1,1]])
        
        five_rows = [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ] 
        self.assertEqual(solution.generate(5), five_rows)


if __name__ == '__main__':
    unittest.main() 