# -*- coding: utf-8 -*-
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""
#%%
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x <= 3:
            return 1
        left = 0
        right = x/2
        middle_x_middle = -1

        while left <= right:
            middle = left + (right - left) // 2
            middle_x_middle = middle * middle
            if middle_x_middle == x:
                return middle
            elif middle_x_middle > x:
                right = middle - 1
            else:
                left = middle + 1

        return left - 1
        
solution = Solution()
print(solution.mySqrt(0))
print(solution.mySqrt(4))
print(solution.mySqrt(8))
print(solution.mySqrt(20))
print(solution.mySqrt(100))
print(solution.mySqrt(101))


#%%
