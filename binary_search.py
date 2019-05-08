# -*- coding: utf-8 -*-
"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Note:

    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].

"""
#%%
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Runs in O(log N). Space complexity: O(1)
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
            middle = left + (right - left) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return -1

solution = Solution()
print(solution.search(nums = [-1,0,3,5,9,12], target = 9))
print(solution.search(nums = [12], target = 12))

#%%
