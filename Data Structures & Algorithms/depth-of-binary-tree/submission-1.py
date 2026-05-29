class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        nmax = 0   # this will store the maximum depth found so far

        def depth(node, c):
            nonlocal nmax     # allow updating outer variable

            if not node:
                return
            
            c += 1  # go one level deeper
            
            # if leaf node, check depth
            if node.left is None and node.right is None:
                nmax = max(nmax, c)
                return
            
            # continue exploring children
            depth(node.left, c)
            depth(node.right, c)

        depth(root, 0)
        return nmax