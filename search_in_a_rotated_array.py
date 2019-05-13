"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
#%%
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if not len_nums:
            return -1
        if len_nums == 1:
            if target == nums[0]:
                return 0
            return -1
        left = 0
        right = len_nums - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[middle] == target:
                return middle

            if nums[left] < nums[middle] and nums[left] < target and target < nums[middle]:
                right = middle - 1
            elif nums[left] > nums[middle] and (target > nums[left] or target < nums[middle]):
                right = middle - 1
            elif nums[middle] < nums[right] and nums[middle] < target and target < nums[right]:
                left = middle + 1
            elif nums[middle] > nums[right] and (target < nums[right] and target < nums[middle]
                    or target > nums[right] and target > nums[middle]):
                left = middle + 1
            else:
                return -1
        return -1

solution = Solution()

print(solution.search(nums = [4,5,6,7,8,9,10,0,1,2], target = 3))
print(solution.search(nums = [4,5,6,7,0,1,2], target = 5))
print(solution.search(nums = [4,5,6,7,0], target = 6))

print(solution.search(nums = [3,1,2], target = 3))
print(solution.search(nums = [2,1], target = 3))
print(solution.search(nums = [2,1], target = 1))

#%%
