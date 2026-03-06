#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/6 11:46
# @Author  : fntp
# @File    : 74.py
# @Desc    : 搜索二维矩阵
# @Software: PyCharm
from typing import List


# 二维拉平到一维 index = row * n + col
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
