Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

from collections import Counter

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
