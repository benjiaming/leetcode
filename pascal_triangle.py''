# -*- coding: utf-8 -*-
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
    https://leetcode.com/problems/pascals-triangle/

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1], [1,1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return result

        for i in range(2, numRows):
            current_row = [1]
            for prev_i, prev_el in enumerate(result[i-1]):
                if len(result[i-1]) > prev_i + 1:
                    sum_prev = prev_el + result[i-1][prev_i+1]
                else:
                    sum_prev = 1
                current_row.append(sum_prev)
            result.append(current_row)
        return result
    