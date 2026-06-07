# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = 0

        def inoder(node):

            if not node:
                return 
            
            inoder(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return
            inoder(node.right)

        inoder(root)

        return self.answer

            
        