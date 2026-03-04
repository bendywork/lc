#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/4 10:05
# @Author  : fntp
# @File    : 131.py
# @Desc    : 子串回文字符串
# @Software: PyCharm

class Solution:
    def partition(self, s: str):
        res = []
        path = []

        def is_hui_wen(st):
            left, right = 0, len(st) - 1
            while left < right:
                if st[left] != st[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            # 如果切到末尾，说明是一种合法方案
            if start == len(s):
                res.append(path[:])
                return

            # 枚举子串
            for end in range(start, len(s)):
                substring = s[start:end+1]

                if is_hui_wen(substring):
                    path.append(substring)
                    dfs(end + 1)
                    path.pop()   # 回溯

        dfs(0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.partition("abcdcba"))
