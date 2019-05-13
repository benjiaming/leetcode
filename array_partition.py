"""
 Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:

    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        sorted_nums = sorted(nums)
        len_nums = len(sorted_nums)
        if len_nums == 2:
            return sorted_nums[0]
        for i in range(0, len_nums-1, 2):
            smaller = min(sorted_nums[i], sorted_nums[i+1])
            total += smaller
        return total
