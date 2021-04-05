# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr = head
        
        count = 0
        
        while count < n:
            ptr = ptr.next
            count += 1
        
        node_ptr = head
        prev = None
        while ptr is not None:
            ptr = ptr.next
            prev = node_ptr
            node_ptr = node_ptr.next
        
        if prev is not None:
            prev.next = node_ptr.next
            return head
        else:
            return node_ptr.next
    
        