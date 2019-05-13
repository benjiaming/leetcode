"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
#%%
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, n in enumerate(nums):
            previous_n = seen.get(n, None)
            if previous_n is not None and i - previous_n <= k:
                return True
            else:
                seen[n] = i
        return False
        
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))
