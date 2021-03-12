# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def chk_height(self, root):
        
        if root == None:
            return 0
        
        elif root.left == None and root.right ==None:
            return 0
        elif root.left == None:
            return 1 + self.chk_height(root.right)
        
        elif root.right == None:
            return 1 + self.chk_height(root.left)
            
       
        return 1+ max(self.chk_height(root.right), self.chk_height(root.left))
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        
        elif root.left == None and root.right == None:
            return True
        
        elif root.left == None and self.chk_height(root.right) >=1:
            return False
        
        elif root.right == None and self.chk_height(root.left) >=1:
            return False
        
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.chk_height(root.left) - self.chk_height(root.right)) <=1
        


        
        

            
#root2 = [3,9,20,None,None,15,7]
#root2 = [1,2,2,3,3,None,None,4,4]
        
root2 = [1, None, 3, 2]

nodes = []

for i in range(len(root2)):
    nodes.append(TreeNode(val=root2[i]))
    


nodes[0].right = nodes[2]
nodes[2].left = nodes[3]
        
def preorder(root):
    if root == None:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    

# for i in range(len(root2)):
#     print(nodes[i].val)
#    

preorder(nodes[0])

print(Solution().isBalanced(nodes[0]))

            