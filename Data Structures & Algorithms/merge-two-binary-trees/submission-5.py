# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2

        elif root2 is None:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1             
        
        # elif root1 != None and root2 != None:
        #     root = TreeNode(root1.val + root2.val)
        #     root.left = self.mergeTrees(root1.left, root2.left)
        #     root.right = self.mergeTrees(root1.right, root2.right)
        #     return root

        # elif root1 != None:
        #     root = TreeNode(root1.val)
        #     root.left = self.mergeTrees(root1.left, None)
        #     root.right = self.mergeTrees(root1.right, None)
        #     return root

        # elif root2 != None:
        #     root = TreeNode(root2.val)
        #     root.left = self.mergeTrees(root2.left, None)
        #     root.right = self.mergeTrees(root2.right, None)
        #     return root

        
        