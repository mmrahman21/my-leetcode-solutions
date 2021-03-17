# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        dict = {}
        
        ptr = head
        while ptr != None:
            if ptr in dict.keys():
                return True
            else:
                dict[ptr] = 1
            ptr = ptr.next
            
        return False
        
        