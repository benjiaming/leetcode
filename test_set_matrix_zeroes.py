import unittest
from set_matrix_zeroes import Solution

class TestSolution(unittest.TestCase):
    def test_set_matrix_zeroes(self):
        solution = Solution()

        input = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
        output = [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
        solution.setZeroes(input)
        self.assertEqual(input, output)        

        input = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ]
        output = [
            [0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]
        ]
        solution.setZeroes(input)
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()