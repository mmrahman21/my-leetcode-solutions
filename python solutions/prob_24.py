# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        if head.next == None:
            return head
        
        new_head = head.next
          
        ptr = head
        
        prev = None
        
        while True:
            temp = ptr.next.next
            
            ptr.next.next = ptr
           
            
            if prev is not None:
                prev.next = ptr.next
            ptr.next = None
            

            prev = ptr
            ptr = temp
            
            if ptr is None or ptr.next is None:
                prev.next = ptr
                break
            
            
        return  new_head
            
        