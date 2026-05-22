from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(path):
            print("进入 dfs, path =", path, "used =", used)
            # 终止条件
            if len(path) == len(nums):
                print("找到结果:", path)
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # 选择
                print("  选择", nums[i])
                path.append(nums[i])
                used[i] = True

                # 递归
                dfs(path)

                # 回溯
                print("  回溯，弹出", nums[i])
                path.pop()
                used[i] = False

        dfs([])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))