import unittest
from move_zeroes import Solution

class TestSolution(unittest.TestCase):
    def test_move_zeroes(self):
        solution = Solution()

        nums = []
        solution.moveZeroes(nums)
        self.assertEqual(nums, [])

        nums = [0]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

        nums = [0,1,1]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1,1,0])

        nums = [0,0,1]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1,0,0])

        nums = [1,1,0]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1,1,0])

        nums = [0,1,0,3,12]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])


if __name__ == '__main__':
    unittest.main()