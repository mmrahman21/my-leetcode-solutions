# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_node = head
        
        if current_node is None:
            return current_node
        
        while current_node.next is not None:
            next_node = current_node.next
            
            if current_node.val == next_node.val:
                current_node.next = next_node.next
            else:
                current_node = current_node.next
            
            
        return head
        