# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # 当前节点作为“拐点”
            current_sum = node.val + left_gain  + right_gain

            # 更新全局最大
            self.max_sum = max(self.max_sum, current_sum)

            # 向上返回单边最大贡献
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum