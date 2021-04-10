# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head is None:
            return head
        
        
        smaller_head = None
        smaller_top = None
        
        larger_head = None
        larger_top = None
        
        ptr = head 
        
        while ptr is not None:
            
            if ptr.val < x:
                if smaller_head is None:
                    smaller_top = ptr
                    smaller_head = ptr
                    ptr = ptr.next
                    smaller_head.next = None
                    
                else:
                    smaller_head.next = ptr
                    smaller_head = smaller_head.next
                    ptr = ptr.next
                    smaller_head.next = None
            else:
                if larger_head is None:
                    larger_top = ptr
                    larger_head = ptr
                    ptr = ptr.next
                    larger_head.next = None
                else:
                    larger_head.next = ptr
                    larger_head = larger_head.next
                    ptr = ptr.next
                    larger_head.next = None
        
        if smaller_top is not None:
            smaller_head.next = larger_top
            return smaller_top
        else:
            return larger_top
            
        
        
        
        