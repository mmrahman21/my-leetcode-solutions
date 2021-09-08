# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr_root = root
        
        while curr_root:
            if p.val == curr_root.val:
                return p
            elif q.val == curr_root.val:
                return q
            elif p.val < curr_root.val and q.val > curr_root.val:
                return curr_root
            elif q.val < curr_root.val and p.val > curr_root.val:
                return curr_root
            elif p.val > curr_root.val and q.val > curr_root.val:
                curr_root = curr_root.right
            else:
                curr_root = curr_root.left
           
        