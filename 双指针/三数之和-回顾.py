class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tuple_ans_list = []
        nums.sort()
        for index,num in enumerate(nums):
            # print(num , index)
            target = 0 - num
            left_index, right_index = index + 1, len(nums) - 1
            if index !=0 and nums[index] == nums[index-1]:
                continue
            while left_index < right_index:
                if nums[left_index] + nums[right_index] == target:
                    tuple_ans_list.append([num,nums[left_index],nums[right_index]])
                    # 添加完数据之后需要过滤重复数据
                    while left_index < right_index and nums[left_index] == nums[left_index + 1]:
                        left_index += 1
                    while left_index < right_index and nums[right_index] == nums[right_index - 1]:
                        right_index -= 1
                    left_index += 1
                    right_index -= 1
                elif nums[left_index] + nums[right_index] < target:
                    left_index += 1
                else:
                    right_index -= 1
        return tuple_ans_list

if __name__ == '__main__':
    solution = Solution()
    solution.threeSum([-1,0,1,2,-1,-4])