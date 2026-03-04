from typing import List

from sympy import false


class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # 终止
            if k == len(word):
                return True

            # 非法判断

            # 标记访问
            
            # 四个方向

            # 恢复

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False