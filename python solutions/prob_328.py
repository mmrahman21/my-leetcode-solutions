# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        even = None
        even_ptr = head.next
        
        
        ptr = head
        
        
        while ptr:
            
            last = ptr
            
            if even is not None:
                even.next = ptr.next
                
                if ptr.next is not None:
                    ptr.next = ptr.next.next
                even = even.next
                
                if even is not None:
                    even.next = None
            else:
                even = ptr.next
               
                if ptr.next is not None:
                    ptr.next = ptr.next.next
                
                if even is not None:
                    even.next = None
                
            ptr = ptr.next
        
        last.next = even_ptr
        
        return head
        
        
               
            
           
        