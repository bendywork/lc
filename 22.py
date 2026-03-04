from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        left , right = 0, 0

        def dfs(left_dfs, right_dfs, path_dfs):
            if len(path_dfs) == 2*n:
                res.append(path_dfs)
                return
            if left_dfs < n:
                dfs(left_dfs+1, right_dfs, path_dfs+"(")
            if left_dfs > right_dfs:
                dfs(left_dfs, right_dfs+1, path_dfs +")")

        dfs(left,right,path)
        return res

