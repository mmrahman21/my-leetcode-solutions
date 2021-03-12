# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        elif head.next == None:
            return head
        
        else:
            
            next_node = head.next
            head.next = None
            
            
            while next_node != None:
                temp_node = next_node.next
                next_node.next = head
                head = next_node
                next_node = temp_node
                
                
            return head
        