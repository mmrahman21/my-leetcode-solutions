# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        elif head.next is None:
            return head
        
        else:
            
            tail = head
            j = head.next
            tail.next = None

            while j != None:
                if j.val >= tail.val:
                    tail.next = j
                    temp = j.next
                    tail = j
                    tail.next = None
                    j = temp
                    
                elif j.val <= head.val:
                    temp = j.next
                    j.next = head
                    head = j
                    j = temp
                    
                else:
                    p = head.next
                    prev = head
                    
                    while p is not None and j.val > p.val:
                        prev = p
                        p = p.next
                    
                    prev.next = j
                    temp = j.next
                    j.next = p
                    j = temp
                     
        return head
            
        
        