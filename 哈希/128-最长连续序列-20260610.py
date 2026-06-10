from collections import defaultdict
from typing import List


class Solution:
    ###
    def longestConsecutive(self, num_list: List[int]) -> int:
        set_list = set(num_list)
        max_len = 0
        for num in set_list:
            if num - 1 not in set_list:
                cur = num
                cur_len = 1
                while cur + 1 in set_list:
                    cur_len += 1
                    cur += 1
                max_len = max(max_len, cur_len)
        return max_len

if __name__ == '__main__':
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    solution = Solution()
    res = solution.longestConsecutive(nums)
    # res = solution.longestConsecutive(nums)
    print(res)