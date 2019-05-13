# -*- coding: utf-8 -*-
"""
There are three types of edits that can be performed on strings: insert a character, remove a character or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

Example:

Input: a = pale, b = pale
Output: True

Input: a = pales, b = pale
Output: True

Input: a = pale, b = bale
Output: True

Input: a = pale, b = bake
Output: False
"""
#%%
from collections import Counter

class Solution(object):
    def isOneAway(self, a, b):
        """
        :type a  List[str]
        :type: b List[str]
        :rtype: True if b is one-away from a
        """
        if a == b:
            return True
        a_count = Counter(a)
        b_count = Counter(b)
        already_has_change = False
        modificator = 0
        if len(a) + 1 == len(b): # insert
            modificator = 1
        elif len(a) == len(b) + 1: # remove
            modificator = -1
        elif len(a) == len(b): # replace
            pass
        else: # different lengths
            return False

        for ac in a_count:
            a_num = a_count[ac]
            if ac in b_count:
                b_num = b_count[ac]
                del b_count[ac]
                if a_num == b_num + modificator:
                    if modificator and already_has_change:
                        return False
                    already_has_change = True
                elif a_num == b_num:
                    continue
                else:
                    return False
            else:
                if a_num != 1:
                    return False
                else:
                    if not modificator and already_has_change:
                        return False
                    already_has_change = True
        if len(b_count) == 0 or len(b_count) > 1:
            return True
        for b in b_count:
            if b_count[b] != 1:
                return False
        return True
        

solution = Solution()
print(solution.isOneAway('a', 'bb'))
print(solution.isOneAway('pale', 'ple'))
print(solution.isOneAway('ple', 'pale'))
print(solution.isOneAway('ple', 'pales'))
print(solution.isOneAway('ple', 'plles'))

#%%
