from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            # 走到头了
            if index == len(nums):
                res.append(path[:])
                return

            # ① 不选当前元素
            dfs(index + 1, path)

            # ② 选当前元素
            path.append(nums[index])
            dfs(index + 1, path)

            # 回溯
            path.pop()

        dfs(0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
