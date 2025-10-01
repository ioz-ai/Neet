# You are given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        print(m)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m[j][i]=matrix[i][j]
        return m