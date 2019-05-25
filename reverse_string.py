"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
from functools import reduce
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return []

        i = 0
        j = len(s) - 1
        while i < j:
            s[j], s[i] = s[i], s[j]
            i += 1
            j -= 1


    def reverseReduce(self, s):
        """
        :type s: List[str]
        :rtype: str Reversed string
        """
        return list(reduce(lambda x,y: y+x, s))

