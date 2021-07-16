# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        ptr1 = headA
        ptr2 = headB
        
        add = {}
       
        while ptr1:
            
            add[ptr1] =  add.get(ptr1, 0) + 1
            ptr1 = ptr1.next
            
 
        while ptr2:
            add[ptr2] = add.get(ptr2, 0) + 1
            
            if add[ptr2] == 2:
                return ptr2
            
            ptr2 = ptr2.next
           
                 
        
        return None
        
       