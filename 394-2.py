#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/13 21:27
# @Author  : fntp
# @File    : 394-2.py
# @Desc    : XXXXXX
# @Software: PyCharm
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        num = 0
        res = ""

        for c in s:

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '[':
                stack.append((num, res))
                num = 0
                res = ""

            elif c == ']':
                k, prev = stack.pop()
                res = prev + k * res

            else:
                res += c

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[a2[c]]"))