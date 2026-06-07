# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.inorder_map = {val:i for i,val in enumerate(inorder)}

        self.poi = 0
        
        def dfs(left,right):
            if left > right:
                return 
            rootval = preorder[self.poi]
            self.poi += 1

            root = TreeNode(rootval)
            mid = self.inorder_map[rootval]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        

        return dfs(0,len(inorder)-1)



        