# -*- coding: utf-8 -*-
"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
https://assets.leetcode.com/uploads/2018/10/12/diagonal_traverse.png

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Runs in O(matrix_length * element_length)
        """

        result = []
        if not matrix:
            return result 
        go_right = True
        matrix_length = len(matrix)
        element_length = len(matrix[0])
        size = matrix_length + element_length

        for total in range(size - 1):
            if go_right:
                if total < matrix_length:
                    col = 0
                else:
                    col = total - matrix_length + 1
                row = total - col
                while col < element_length and col <= total and row < matrix_length:
                    row = total - col
                    result.append(matrix[row][col])
                    col += 1

            if not go_right:
                if total > element_length - 1:
                    row = total - element_length + 1
                else:
                    row = 0
                col = total - row
                while row < matrix_length and row <= total and col < element_length:
                    col = total - row
                    result.append(matrix[row][col])
                    row += 1
            go_right = not go_right

        return result
