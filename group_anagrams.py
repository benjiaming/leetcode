"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

"""
#%%
from pprint import pprint
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in freq:
                freq[key].append(s)
            else:
                freq[key] = [s]
        return freq.values()

solution = Solution()
pprint(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
