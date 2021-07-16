# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result_head = head
        head = head.next
        result_head.next = None
        
        while head:
            ptr = head
            head = head.next
            
            result_ptr = result_head
            
            loc = None
            
            while result_ptr and result_ptr.val < ptr.val:
                loc = result_ptr
                result_ptr = result_ptr.next
            
            if loc: 
                temp = loc.next   
                loc.next = ptr
                ptr.next = temp
            else:
                ptr.next = result_head
                result_head = ptr
            
        return result_head
            
            
            
            
                 
                
        