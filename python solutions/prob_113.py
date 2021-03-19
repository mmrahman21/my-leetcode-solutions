# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        
        if root.val == targetSum and root.left is None and root.right is None:
            return [[root.val]]
        
        result = []
       
        result = [[root.val]+ l if type(l) is list else [root.val] + [l] for l in self.pathSum(root.left, targetSum - root.val)]
       
        
        result = result + [ [root.val]+ p if type(p) is list else [root.val] + [p] for p in self.pathSum(root.right, targetSum - root.val)]
            
           
        return result
        