#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 12:11
# @Author  : fntp
# @File    : 4.py.py
# @Desc    : 寻找两个正序数组的中位数
# @Software: PyCharm
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        l1, l2 = len(nums1)-1, len(nums2)-1
        new_lst = []
        while i <= l1 or j <= l2:
            if j > l2 or (i <= l1 and nums1[i] <= nums2[j]):
                new_lst.append(nums1[i])
                i += 1
            else:
                if j <= l2:
                    new_lst.append(nums2[j])
                    j += 1
        print(new_lst)
        n = len(new_lst)

        return new_lst[n // 2] if n % 2 else (new_lst[n // 2 - 1] + new_lst[n // 2]) / 2

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))