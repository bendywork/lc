#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/6 13:25
# @Author  : fntp
# @File    : 34-1.py
# @Desc    : XXXXXX
# @Software: PyCharm
class Solution:
    def searchRange(self, nums, target):

        def left_bound():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

                if nums[mid] == target:
                    ans = mid

            return ans

        def right_bound():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    ans = mid

            return ans

        return [left_bound(), right_bound()]