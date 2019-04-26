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
