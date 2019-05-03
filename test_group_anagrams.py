import unittest
from group_anagrams import Solution

class TestSolution(unittest.TestCase):
    def test_group_anagrams(self):
        solution = Solution()
        anagrams = [
                ["ate","eat","tea"],
                ["nat","tan"],
                ["bat"]
        ] 
        result = solution.groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"]
        )
        self.assertEqual(
            sorted([sorted(r) for r in result]), 
            sorted(anagrams)
        )


if __name__ == '__main__':
    unittest.main()