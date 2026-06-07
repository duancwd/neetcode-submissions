# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,good_sofar):
            if not node:
                return 0
            
            count = 0
            if node.val >= good_sofar:
                count = 1
            good_sofar = max(good_sofar,node.val)

            count +=dfs(node.left,good_sofar)
            count +=dfs(node.right,good_sofar)

            return count
        return dfs(root, root.val)
        