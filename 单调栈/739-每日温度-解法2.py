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

        res = []

        for i in range(len(temperatures)):

            for j in range(i + 1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
            else:
                res.append(0)

        return res