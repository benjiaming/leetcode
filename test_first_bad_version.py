import unittest
from first_bad_version import Solution, _bad_version

class TestSolution(unittest.TestCase):
    def test_first_bad_version(self):
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(100), _bad_version)


if __name__ == '__main__':
    unittest.main()