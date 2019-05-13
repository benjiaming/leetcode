# -*- coding: utf-8 -*-
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""
class Solution(object):
    def reverse_range(self, nums, start, end):
        while start < end:
            swap = nums[start]
            nums[start] = nums[end]
            nums[end] = swap
            start += 1
            end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Reverses the whole list and then again first k and last n-k numbers.

        Runs in O(n). Space complexity: O(1)
        (64 ms 12.1 MB)
        """
        len_nums = len(nums)
        if not len_nums:
            return []
        k %= len_nums
        self.reverse_range(nums, 0, len_nums-1)
        self.reverse_range(nums, 0, k-1)
        self.reverse_range(nums, k, len_nums-1)

    def rotate_swap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Swaps using temporary variables.

        Runs in O(n). Space complexity: O(1)
        (52 ms 11.9 MB)
        """
        if not nums:
            return []
        len_num = len(nums)
        k %= len_num
        count = 0
        start = -1
        while count < len_num:
            start += 1
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len_num
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
                if start == current:
                    break

