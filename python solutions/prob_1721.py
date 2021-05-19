# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        count = 1
        
        ptr = head 
        
        while count < k:
            ptr = ptr.next
            count += 1
        
        left = ptr
        
        right = head
        ptr = ptr.next
        
        while ptr:
            
            right = right.next    
            ptr = ptr.next
           
        temp = left.val
        left.val = right.val
        right.val = temp
        
        return head
            
            
        