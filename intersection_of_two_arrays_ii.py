"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
#%%
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap1 = Counter(nums1)
        hashmap2 = Counter(nums2)
    
        result = []
        for n in hashmap2.keys():
            if n in hashmap1:
                result.extend([n for _ in range(min(hashmap1[n], hashmap2[n]))])
        return result
        
solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))
print(solution.intersect([4,9,5], [9,4,9,8,4]))
