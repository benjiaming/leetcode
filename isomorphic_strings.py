# -*- coding: utf-8 -*-
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""
class Solution(object):
    def isIsomorphic_dict(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        reverse_seen = {}
        for i, n in enumerate(s):
            previous_n = seen.get(n, None)
            if previous_n and previous_n != t[i]:
                return False
            previous_t = reverse_seen.get(t[i], None)
            if previous_t:
                matching_n = seen.get(previous_t, None)
                if matching_n and previous_t != n:
                    return False
            seen[n] = t[i]
            reverse_seen[t[i]] = n
        return True

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(i) for i in s] == [t.find(i) for i in t]
        