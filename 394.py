#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/13 21:08
# @Author  : fntp
# @File    : 394.py
# @Desc    : 字符串解码 - 给定一个经过编码的字符串，返回它解码后的字符串。
# @Software: PyCharm

class Solution:

    def decodeString(self, s: str) -> str:
        self.i = 0
        def dfs():
            res = ""
            num = 0
            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    num = num * 10 + int(c)

                elif c == '[':
                    self.i += 1
                    sub = dfs()
                    res += num * sub
                    num = 0

                elif c == ']':
                    return res

                else:
                    res += c

                self.i += 1
            return res

        return dfs()