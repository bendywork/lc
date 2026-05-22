# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        
        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            
            root_val = preorder[pl]
            root = TreeNode(root_val)
            
            mid = index[root_val]
            left_size = mid - il
            
            root.left = dfs(pl + 1, pl + left_size, il, mid - 1)
            root.right = dfs(pl + left_size + 1, pr, mid + 1, ir)
            
            return root
        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)