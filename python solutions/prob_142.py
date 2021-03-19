# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
                    
        if head is None or head.next is None:
            return None
        
        dict = {}
        
        ptr = head
        while ptr != None:
            if ptr in dict.keys():
                    
                return ptr
            
            else:
                dict[ptr] = 1
            ptr = ptr.next
            
        return None
        