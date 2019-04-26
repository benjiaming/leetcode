from collections import Counter
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        Runs in O(N) where N is number of characters in s
        """
        uniqs = Counter(s)
        for index, char in enumerate(s):
            if uniqs[char] == 1:
                return index
        return -1
