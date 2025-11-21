from typing import List


class Solution:
    def findKthLargest(self, nums: List[int]) -> List[int]:
        # 先写一版本快速排序
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        base_num = nums[0]
        left = []
        right = []
        for num in nums[1:]:
            if num <= base_num:
                left.append(num)
            else:
                right.append(num)
        return findKthLargest(left) + [base_num] + findKthLargest(right)




if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = Solution().(nums, k)
    print(res)
