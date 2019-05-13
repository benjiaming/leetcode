# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
#%%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        positions = {}
        last_match = -1
        for i, n in enumerate(s):
            if n in positions and last_match < positions[n]:
                last_match = positions[n]
            positions[n] = i
            max_len = max(max_len, i - last_match)
        return max_len
    

solution = Solution()
print(solution.lengthOfLongestSubstring("abba"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("bbbb"))
print(solution.lengthOfLongestSubstring("dvdf"))



#%%
