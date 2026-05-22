#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/4 9:50
# @Author  : fntp
# @File    : Hw.py
# @Desc    : 回文字符串判断方式，双指针法则
# @Software: PyCharm
class Hw:

    @staticmethod
    def is_hui_wen(target_str):
        str_length = len(target_str)
        if str_length <= 1:
            return True
        left_index,right_index = 0, str_length-1
        while left_index < right_index:
            if target_str[left_index] != target_str[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True



