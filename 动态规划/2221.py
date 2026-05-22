from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = [[]]
        j = 0
        if len(nums) == 1:
            return nums[0]
        while len(res) < len(nums):
            length = len(nums) if j == 0 else len(res[j])
            cal = nums if j == 0 else res[j]
            temp_res = []
            for i in range(length - 1):
                res_num = (cal[i] + cal[i + 1]) % 10
                temp_res.append(res_num)
            j += 1
            res.append(temp_res)
        return res[-1][0]