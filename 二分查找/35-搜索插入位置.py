from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)


if __name__ == '__main__':
    nums = [1,3,5,6]
    k = 2
    res = Solution().searchInsert(nums, k)
    print(res)
