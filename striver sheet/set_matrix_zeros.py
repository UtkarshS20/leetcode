from typing import List
"""
# brute solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_to_zero = []
        col_to_zero = []
        for m, arr in enumerate(matrix):
            for n, val in enumerate(arr):
                if val == 0:
                    row_to_zero.append(m)
                    col_to_zero.append(n)
        for m, arr in enumerate(matrix):
            for n, val in enumerate(arr):
                if m in row_to_zero:
                    arr[n] = 0*arr[n]
                if n in col_to_zero:
                    arr[n] = 0
"""
matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

sol = Solution()
sol.setZeroes(matrix)
print(matrix)