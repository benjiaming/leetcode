# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from collections import Counter
class Solution(object):
    def singleNumber_most_common(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime complexity: O(n). Space complexity: O(n)
        """
        return Counter(nums).most_common()[-1][0]

    def singleNumber_sorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime complexity: O(n*logn). Space complexity: O(1)
        """
        nums.sort()

        if len(nums) == 1 or nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for j in range(1, len(nums)-1):
            if nums[j-1] != nums[j] and nums[j+1] != nums[j]:
                return nums[j]
        return -1

    def singleNumber_xor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime complexity: O(n). Space complexity: O(1)
        """
        # 
        # 0 ^ 10 == 10
        # 10 ^ 10 == 0
        # nums = (1,5,3,3,5)
        # 0 ^ 1 ^ 5 ^ 3 ^ 3 ^ 5 == 1
        candidate_num = 0
        for num in nums:
            candidate_num ^= num
        return candidate_num

