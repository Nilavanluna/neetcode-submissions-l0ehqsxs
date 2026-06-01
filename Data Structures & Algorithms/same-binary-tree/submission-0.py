# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.v=True
        def same(n1,n2):
          
            if (not n1 and  n2) or (n1 and not n2):
                self.v=False
                return 
            elif not n1 and not n2:
                return
            same(n1.left,n2.left)
            if n1.val!=n2.val:
                self.v=False 
            same(n1.right,n2.right)
            print(n1.val,n2.val)
            if n1.val!=n2.val:
                self.v=False 
        same(p,q)
        
        return self.v