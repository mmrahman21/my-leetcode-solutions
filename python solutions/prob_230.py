# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root: TreeNode):
    
    res = []
    if root.left:
        res.extend(inorder(root.left))
    res.extend([root.val])
    
    if root.right:
        res.extend(inorder(root.right))
    
    return res
        
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        res = inorder(root)
        
        return res[k-1]
        