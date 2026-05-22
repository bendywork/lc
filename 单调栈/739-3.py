#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/13 22:00
# @Author  : fntp
# @File    : 739-2.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(temperatures))