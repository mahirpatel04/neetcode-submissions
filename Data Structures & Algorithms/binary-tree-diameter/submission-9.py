# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxHeight(n):
            if n == None:
                return 0
            return 1 + max(maxHeight(n.left), maxHeight(n.right))



        if not root:
            return 0
        
        if root.left == None and root.right == None:
            return 0

    
        leftD = self.diameterOfBinaryTree(root.left)
        rightD = self.diameterOfBinaryTree(root.right)

        width = maxHeight(root.left) + maxHeight(root.right)

        return max(leftD, rightD, width)



    
  