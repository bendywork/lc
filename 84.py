#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/16 10:34
# @Author  : fntp
# @File    : 84.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List
# 错误做法

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        n = len(heights)
        if not heights:
            return -1
        if n == 1:
            return heights[0]
        temp = []
        for i in range(n):
            j = i + 1
            temp.append(heights[i])
            if j < n and heights[j] < heights[i]:
                max_area = max(2 * heights[j], max_area)
                continue
            while j < n and i < n:
                temp.append(heights[j])
                max_area = max(len(temp) * min(temp), max_area)
                i = j
                j = j + 1
            temp = []
        return max_area


if __name__ == '__main__':
    s = Solution()
    # print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([0,9]))