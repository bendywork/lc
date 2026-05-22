#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/13 21:04
# @Author  : fntp
# @File    : 155.py
# @Desc    : 最小栈
# @Software: PyCharm
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈

class MinStack:

    def __init__(self):
        self.lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return min(self.lst)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()