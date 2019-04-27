# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs:
            return prefix
        first_string = strs[0]
        for i, char in enumerate(first_string):
            for other_string in strs:
                if other_string == first_string:
                    continue
                if len(other_string) <= i or other_string[i] != char:
                    return prefix
            prefix += char
        return prefix