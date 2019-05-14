import unittest
from rotate_image import Solution

class TestSolution(unittest.TestCase):
    def test_rotate_image(self):
        solution = Solution()
        input = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]
        output = [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ]
        solution.rotate(input)
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()