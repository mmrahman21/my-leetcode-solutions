# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            level_list = [i.val for i in queue]
            result.append(level_list)
            queue2 = []
            
            while queue:
                node = queue.pop(0)
                
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
                    
            queue = queue2
        
        return result[::-1]
        