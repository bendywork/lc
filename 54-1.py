from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # 右边界
        right_max_index = len(matrix[0])
        # 下边界
        bottom_max_index = 0
        # 从左边开始出发顺时针
        left_index = 0
        # 最高点
        high_max_index = len(matrix)
        while high_max_index > bottom_max_index and left_index < right_max_index:
            for i in range(right_max_index):
                res.append(matrix[high_max_index][i])
            for i in range(high_max_index):
                res.append(matrix[i][high_max_index])
            if left_index < right_max_index:
                
