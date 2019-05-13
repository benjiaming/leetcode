# -*- coding: utf-8 -*-
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
def cmp(x, y):
    """
    Replacement for built-in function cmp that was removed in Python 3

    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == y
    and strictly positive if x > y.
    """

    return (x > y) - (x < y)

class Solution(object):
    def twoSumDict(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        Uses a dictionary; runs in O(n)
        """
        seen = {}
        for i, num in enumerate(numbers):
            if num in seen:
                return [seen[num]+1, i+1]
            seen[target-num] = i
        return []

    def twoSumCmp(self, numbers, target):
        # two pointer technique
        i = 0
        j = len(numbers) - 1
        while i < j:
            result = cmp(numbers[i], target - numbers[j])
            if result < 0:
                i += 1
            elif result > 0:
                j-= 1
            else:
                return [i+1, j+1]
        return []
