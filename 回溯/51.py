#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/4 10:33
# @Author  : fntp
# @File    : 51.py
# @Desc    : N皇后
# @Software: PyCharm

class Solution:
    def solveNQueens(self, n: int):
        res = []
        path = []

        def is_valid(row, col):
            for r in range(row):
                if path[r] == col:
                    return False
                    # 主对角线
                if r - path[r] == row - col:
                    return False
                # 副对角线
                if r + path[r] == row + col:
                    return False
            return True

        def dfs(row):
            if row == n:
                board = []
                for col in path:
                    line = "." * col + "Q" + "." * (n - col - 1)
                    board.append(line)
                res.append(board)
                return
            for col in range(n):
                if is_valid(row, col):
                    path.append(col)
                    dfs(row + 1)
                    path.pop()

        dfs(0)
        return res