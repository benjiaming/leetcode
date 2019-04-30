import unittest
from rotate_array import Solution

class TestSolution(unittest.TestCase):
    def test_reverse_range(self):
        solution = Solution()
        numbers = [1,2,3,4,5]
        solution.reverse_range(numbers, 1, 2)
        self.assertEqual(numbers, [1,3,2,4,5])
        numbers = [1,2,3,4,5]
        solution.reverse_range(numbers, 0, 3)
        self.assertEqual(numbers, [4,3,2,1,5])
        numbers = [1,2,3,4,5]
        solution.reverse_range(numbers, 0, len(numbers)-1)
        self.assertEqual(numbers, [5,4,3,2,1])

    def test_rotate_array(self):
        solution = Solution()
        numbers = []
        solution.rotate(numbers, 1)
        self.assertEqual(numbers, [])

        numbers = [2]
        solution.rotate(numbers, 1)
        self.assertEqual(numbers, [2])

        numbers = [1, 2]
        solution.rotate(numbers, 0)
        self.assertEqual(numbers, [1, 2])

        numbers = [1, 2]
        solution.rotate(numbers, 1)
        self.assertEqual(numbers, [2, 1])

        numbers = [1, 2]
        solution.rotate(numbers, 2)
        self.assertEqual(numbers, [1, 2])

        numbers = [1, 2, 3]
        solution.rotate(numbers, 1)
        self.assertEqual(numbers, [3, 1, 2])

        numbers = [1,2,3,4,5,6,7]
        solution.rotate(numbers, 3)
        self.assertEqual(numbers, [5,6,7,1,2,3,4])

        numbers = [-1,-100,3,99]
        solution.rotate(numbers, 2)
        self.assertEqual(numbers, [3,99,-1,-100])

        numbers = [1,2,3]
        solution.rotate(numbers, 6)
        self.assertEqual(numbers, [1,2,3])

        numbers = [1,2,3]
        solution.rotate(numbers, 1000)
        self.assertEqual(numbers, [3,1,2])

if __name__ == '__main__':
    unittest.main()