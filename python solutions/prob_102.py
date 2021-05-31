from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        Q = deque()
        
        if root == None:
            return None
        
        Q.append((root, 0))
        
        res = []
        
        
        while Q:
            
            v, rank = Q.popleft()
            
            if len(res) <= rank:
                res.append([v.val])
            else:
                res[rank].append(v.val)
            
 
            if v.left is not None:
                Q.append((v.left, rank + 1))
                    
                        
            if v.right is not None:
                Q.append((v.right, rank + 1))
               
        
        print(res)
        
        return res
            
        
        