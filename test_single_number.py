import unittest
from single_number import Solution

class TestSolution(unittest.TestCase):
    def test_single_number_most_common(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber_most_common([1]), 1)
        self.assertEqual(solution.singleNumber_most_common([1,1,2]), 2)
        self.assertEqual(solution.singleNumber_most_common([1,1,2,2,3]), 3)
        self.assertEqual(solution.singleNumber_most_common([1,1,2,3,3]), 2)
        self.assertEqual(solution.singleNumber_most_common([1,2,2,3,3]), 1)
        self.assertEqual(solution.singleNumber_most_common([1,1,2,2,3,3,4]), 4)
        self.assertEqual(solution.singleNumber_most_common([2,2,1]), 1)
        self.assertEqual(solution.singleNumber_most_common([4,1,2,1,2]), 4)
        self.assertEqual(solution.singleNumber_most_common([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]), 16)

    def test_single_number_sorted(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber_sorted([1]), 1)
        self.assertEqual(solution.singleNumber_sorted([1,1,2]), 2)
        self.assertEqual(solution.singleNumber_sorted([1,1,2,2,3]), 3)
        self.assertEqual(solution.singleNumber_sorted([1,1,2,3,3]), 2)
        self.assertEqual(solution.singleNumber_sorted([1,2,2,3,3]), 1)
        self.assertEqual(solution.singleNumber_sorted([1,1,2,2,3,3,4]), 4)
        self.assertEqual(solution.singleNumber_sorted([2,2,1]), 1)
        self.assertEqual(solution.singleNumber_sorted([4,1,2,1,2]), 4)
        self.assertEqual(solution.singleNumber_sorted([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]), 16)

    def test_single_number(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber_xor([1]), 1)
        self.assertEqual(solution.singleNumber_xor([1,1,2]), 2)
        self.assertEqual(solution.singleNumber_xor([1,1,2,2,3]), 3)
        self.assertEqual(solution.singleNumber_xor([1,1,2,3,3]), 2)
        self.assertEqual(solution.singleNumber_xor([1,2,2,3,3]), 1)
        self.assertEqual(solution.singleNumber_xor([1,1,2,2,3,3,4]), 4)
        self.assertEqual(solution.singleNumber_xor([2,2,1]), 1)
        self.assertEqual(solution.singleNumber_xor([4,1,2,1,2]), 4)
        self.assertEqual(solution.singleNumber_xor([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]), 16)


if __name__ == '__main__':
    unittest.main()