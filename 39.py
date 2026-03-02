from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        candidates.sort()  # 有助于剪枝

        def dfs(start, remaining):
            # 成功条件
            if remaining == 0:
                res.append(path[:])
                return

            # 剪枝
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # 如果当前数已经大于剩余，后面更大，直接终止
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                dfs(i, remaining - candidates[i])  # 可以重复选
                path.pop()

        dfs(0, target)
        return res
