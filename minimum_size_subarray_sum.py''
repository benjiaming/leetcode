# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""
MAXINT=2147483647

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        Runs in O(n). O(1) for space.
        """
        left = 0
        total = 0
        ans = MAXINT
        for i, num in enumerate(nums):
            total += num
            while total >= s:
                ans = min(ans, i + 1 - left)
                total -= nums[left]
                left += 1
        return 0 if ans == MAXINT else ans

