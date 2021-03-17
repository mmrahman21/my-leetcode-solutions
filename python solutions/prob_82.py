# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        elif head.next is None:
            return head
        
        ptr = head
        
        while ptr != None:
            
            if ptr.next == None:
                return ptr
            
            elif ptr.val == ptr.next.val:
                
                while ptr.val == ptr.next.val:
                    ptr = ptr.next

                    if ptr.next == None:
                        break
                
                if ptr != None:
                    return self.deleteDuplicates(ptr.next)
                    
            else:
                ptr.next = self.deleteDuplicates(ptr.next)
                return ptr
