# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, hight):
            if not node:
                return True
            

            if not (low < node.val < hight):
                return False

            return (dfs(node.right, node.val, hight) and dfs(node.left,low,node.val))
        return dfs(root,float("-inf"), float("inf"))

        