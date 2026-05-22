from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path)

                path.pop()
                used[i] = False

        dfs([])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))