from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_set = set()
        cloumn_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    cloumn_set.add(j)
        for i in range(m):
            for j in range(n):
                if i in row_set or j in cloumn_set:
                    matrix[i][j] = 0