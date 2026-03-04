class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # 成功
            if k == len(word):
                return True

            # 越界 or 不匹配
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False

            # 标记访问
            tmp = board[i][j]
            board[i][j] = "#"

            # 四个方向
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )

            # 恢复
            board[i][j] = tmp

            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False