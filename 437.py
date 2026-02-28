# 子数组和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from idlelib.tree import TreeNode
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1  # 空路径

        def dfs(node, curr_sum):
            if not node:
                return 0
            # 更新当前路径和
            curr_sum += node.val

            # 计算有多少条路径满足要求
            count = prefix[curr_sum - targetSum]

            # 更新前缀和表
            prefix[curr_sum] += 1

            # 递归左右子树
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # 回溯！！！！
            prefix[curr_sum] -= 1

            return count

        res = dfs(root, 0)
        print(prefix)
        return res


if __name__ == '__main__':
    # 构造测试树
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)

    root.left.right.right = TreeNode(1)

    targetSum = 8
    solution = Solution()
    res = solution.pathSum(root, targetSum)
    print(res)