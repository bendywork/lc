from typing import List
import random


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 数字到字母映射
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def dfs(index):
            # 终止条件
            if index == len(digits):
                res.append("".join(path))
                return

            # 当前数字
            letters = phone[digits[index]]

            for ch in letters:
                path.append(ch)
                dfs(index + 1)
                path.pop()

        dfs(0)
        return res

# 生成测试用例
if __name__ == '__main__':
    # 限制digits长度在3-4之间
    digits = [str(random.randint(2, 9)) for _ in range(random.randint(1, 10))][:random.randint(3, 4)]
    print(digits)
    print(Solution().letterCombinations("".join(digits)))


# def dfs(index):
#     if index == len(digits):
#         收集答案
#         return
#
#     for 每个可能字母:
#         选择
#         dfs(index+1)
#         撤销