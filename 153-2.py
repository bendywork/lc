#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 11:23
# @Author  : fntp
# @File    : 153.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]




