from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        steps = 0
        end = 0
        farthest = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == end:
                #落在区间内，说明可以返回
                steps += 1
                end = farthest
                if end >= n-1:
                    break
        return steps
