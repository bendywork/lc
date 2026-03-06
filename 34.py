#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/6 12:40
# @Author  : fntp
# @File    : 34.py
# @Desc    : XXXXXX
# @Software: PyCharm
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1
        while left < right:
            mid_index = (left + right) // 2
            if target == nums[mid_index]:
                res.append(mid_index)
                if mid_index - 1 >= 0 and nums[mid_index-1] == target:
                    res.append(mid_index-1)
                if mid_index + 1 <= len(nums) - 1 and nums[mid_index + 1] == target:
                    res.append(mid_index + 1)
            elif target > nums[mid_index]:
                left = mid_index + 1
            else:
                right = mid_index - 1

        if len(res) == 1:
            res.append(res[0])
            return res
        return [-1,-1]


if __name__ == '__main__':
    s = Solution()
    s.searchRange([5,7,7,8,8,10], 8)