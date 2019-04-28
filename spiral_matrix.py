# -*- coding: utf-8 -*-
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        Runs in O(N) where num_cols * num_rows
        """
        result = []
        if not matrix:
            return result
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        total_elements = num_cols * num_rows

        smaller = min(num_rows, num_cols)
        if smaller % 2:
            smaller += 1
        number_of_steps = int(smaller / 2)

        for step in range(number_of_steps):
            # go right
            for a in range(step, num_cols-step):
                result.append(matrix[step][a])
                if len(result) == total_elements:
                    return result
            # go down
            for a in range(step+1, num_rows-1-step):
                result.append(matrix[a][num_cols-1-step])
                if len(result) == total_elements:
                    return result
            # go left
            for a in range(num_cols-1-step, step, -1):
                result.append(matrix[num_rows-1-step][a])
                if len(result) == total_elements:
                    return result
            # go up
            for a in range(num_rows-1-step, step, -1):
                result.append(matrix[a][step])
                if len(result) == total_elements:
                    return result
        return result            



