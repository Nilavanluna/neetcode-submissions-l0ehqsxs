# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.de=True
        def bal(node):
         if not node:
            return 0
         l=bal(node.left)
         r=bal(node.right)
         print(l,r,node.val)
         if (abs(l-r)>1):
            self.de=False
         
         return 1+max(l,r)
        bal(root)
        return self.de
        
        
        