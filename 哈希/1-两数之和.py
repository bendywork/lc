from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for num_index, num_val in enumerate(nums):
            another_num = target - num_val
            if another_num in dict:
                return [dict[another_num], num_index]
            dict[num_val] = num_index
        return []

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))