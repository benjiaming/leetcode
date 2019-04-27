# -*- coding: utf-8 -*-
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution(object):
    MIN_INT = -2147483648
    MAX_INT = 2147483647

    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Runtime: 24 ms, faster than 100.00% of Python online submissions for Reverse Integer.
        Memory Usage: 11.7 MB, less than 5.56% of Python online submissions for Reverse Integer.
        """
        sign = -1 if x < 0 else 1
        result = str(abs(x))[::-1].lstrip('0')
        num_result = int(result) if result else 0
        if num_result < self.MIN_INT or num_result > self.MAX_INT:
            num_result = 0
        return sign * num_result


    def reverse_math(self, x):
        """
        :type x: int
        :rtype: int

        Runtime: 32 ms, faster than 31.52% of Python online submissions for Reverse Integer.
        Memory Usage: 11.7 MB, less than 5.56% of Python online submissions for Reverse Integer.
        """
        # 325 / 100 = 3 (25)
        # 25 / 10 = 2 (5)
        # 5 / 1 = 5 (0)
        from math import log10
        def num_of_digits(num): 
            return int(log10(num)+1)

        if not x:
            return 0
        sign = -1 if x < 0 else 1
        remainder = abs(x)
        list = []
        total_digits = num_of_digits(remainder)
        for i in range(total_digits-1, -1, -1):
            list.append(int(remainder / 10**i))
            remainder = remainder % 10**i

        result = 0
        for i in range(total_digits-1, -1, -1):
            result += list[i] * 10**i
        signed_result = sign * result
        if signed_result < self.MIN_INT or signed_result > self.MAX_INT:
            return 0
        return signed_result