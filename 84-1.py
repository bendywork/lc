#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/16 11:02
# @Author  : fntp
# @File    : 84-1.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        stack = []
        n = len(heights)
        heights.append(0)  # 哨兵
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                h = heights[idx]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))