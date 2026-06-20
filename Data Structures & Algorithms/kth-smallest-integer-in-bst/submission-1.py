# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def kth(node,l):
            if not node:
              return
            l.append(node.val)
           
            kth(node.left,l)
            kth(node.right,l)
         
        kth(root,l)
        l.sort()
     
        return l[k-1]
         



        