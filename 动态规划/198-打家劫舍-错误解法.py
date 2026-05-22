from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            current = nums[i]
            while i < len(nums) and i<= len(nums)-2:
                i += 2
                current  += nums[i]
            res.append(current)

        return  max(res)