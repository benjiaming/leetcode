# -*- coding: utf-8 -*-
"""


Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true

Modification from CrackingTheCodeInterview.com: Tact Coa == True
"""
#%%
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        counts = Counter(s.lower())
        already_has_single = False
        for c in counts:
            if c == ' ':
                continue
            if counts[c] == 1:
                if already_has_single:
                    return False
                else:
                    already_has_single = True
            elif counts[c] % 2 != 0: 
                return False 
        return True

solution = Solution()
print(solution.canPermutePalindrome('Tact Coa'))
