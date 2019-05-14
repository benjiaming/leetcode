"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""
#%%
from typing import List
class Solution:
    def setZeroesMN(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Runtime: O(m*n). Uses O(m+n) space.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for x in rows:
            matrix[x] = [0 for _ in range(len(matrix[0]))]

        for y in cols:
            for j in range(len(matrix)):
                matrix[j][y] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Runtime: O(m*n). Uses O(1) space.
        """
        first_row_has_zeroes = 0 in matrix[0]
        first_col_has_zeroes = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zeroes = True
                break

        # mark first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # clear columns
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        # clear rows
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(len(matrix[i]))]        

        # clean 1st row
        if first_row_has_zeroes:
            matrix[0] = [0 for _ in range(len(matrix[0]))]

        # clean 1st column
        if not first_col_has_zeroes:
            return
        for i in range(len(matrix)):
            matrix[i][0] = 0
        

solution = Solution()
input = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
solution.setZeroes(input)
print(input)

input = [
    [0,1,2,0],
    [3,4,5,2],
    [1,1,1,5]
]
solution.setZeroes(input)
print(input)
