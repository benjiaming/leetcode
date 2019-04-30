# -*- coding: utf-8 -*-
"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
    
    https://leetcode.com/problems/pascals-triangle-ii/

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        count = 0
        while count < rowIndex:
            row = [x + y for x, y in zip([0] + row, row + [0])]
            count += 1
        return row
