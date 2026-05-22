from typing import List


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         # m 行，n 列
#         # 二维 (i, j)  → 一维 index = i * n + j
#         m = len(matrix)
#         n = len(matrix[0])
#         res = [0] * (m*n)
#         for i in range(m):
#             for j in range(n):
#                 res[i * n + j] = matrix[i][j]
#         return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. 左到右
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # 2. 上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # 3. 右到左
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # 4. 下到上
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
