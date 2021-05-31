def checkSymmetric(root_S1, root_S2):
    if not root_S1 and not root_S2:
        return True
    elif root_S1 and root_S2:
        if root_S1.val == root_S2.val:
            return checkSymmetric(root_S1.left, root_S2.right) and checkSymmetric(root_S1.right, root_S2.left)
        else:
            return False
    else:
        return False
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        left = root.left
        right = root.right
        return checkSymmetric(left, right)

       
        