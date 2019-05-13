import unittest
from palindrome_permutation import Solution

class TestSolution(unittest.TestCase):
    def test_palindrome_permutation(self):
        solution = Solution()
        self.assertEqual(solution.canPermutePalindrome('code'), False)
        self.assertEqual(solution.canPermutePalindrome('aab'), True)
        self.assertEqual(solution.canPermutePalindrome('carerac'), True)
        self.assertEqual(solution.canPermutePalindrome('abc'), False)
        self.assertEqual(solution.canPermutePalindrome('aac'), True)
        self.assertEqual(solution.canPermutePalindrome('jhsabckuj ahjsbckj'), True)
        self.assertEqual(solution.canPermutePalindrome('Able was I ere I saw Elba'), True)
        self.assertEqual(solution.canPermutePalindrome('So patient a nurse to nurse a patient so'), False)
        self.assertEqual(solution.canPermutePalindrome('Random Words'), False)
        self.assertEqual(solution.canPermutePalindrome('Not a Palindrome'), False)
        self.assertEqual(solution.canPermutePalindrome('Tact Coa'), True)
        self.assertEqual(solution.canPermutePalindrome('atco cta'), True)
        self.assertEqual(solution.canPermutePalindrome(''), True)
        self.assertEqual(solution.canPermutePalindrome('x'), True)

if __name__ == '__main__':
    unittest.main()