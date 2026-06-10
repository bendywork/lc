from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 原地操作 + 数组 双指针优先
        slow_index = 0
        for fast_index in range(len(nums)):
            if nums[fast_index] != 0:
                nums[slow_index], nums[fast_index] = nums[fast_index], nums[slow_index]
                slow_index += 1



if __name__ == '__main__':
    nums = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)