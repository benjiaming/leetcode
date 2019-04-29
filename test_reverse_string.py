import unittest
from reverse_string import Solution

class TestSolution(unittest.TestCase):
    def test_reverse_string(self):
        solution = Solution()
        
        string = ["h","e","l","l","o"]
        solution.reverseString(string)
        self.assertEqual(string, ["o","l","l","e","h"])

        string = ["H","a","n","n","a","h"]
        solution.reverseString(string)
        self.assertEqual(string, ["h","a","n","n","a","H"])

        string = []
        solution.reverseString(string)
        self.assertEqual(string, [])

        string = ['a']
        solution.reverseString(string)
        self.assertEqual(string, ['a'])


if __name__ == '__main__':
    unittest.main()