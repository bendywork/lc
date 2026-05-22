#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/13 21:46
# @Author  : fntp
# @File    : 739.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(temperatures):
            flag = 0
            cur = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > cur:
                    res.append(j - i)
                    flag = 1
                    break
                j += 1
            if flag == 0:
                res.append(flag)
            i += 1
        return res
