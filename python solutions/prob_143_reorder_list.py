# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list_of_nodes = []
        
        result = ListNode()
        
        ptr = head
        
        while ptr is not None:
            list_of_nodes.append(ptr)
            ptr = ptr.next
        
        reorder_ptr = result
        
        while len(list_of_nodes) > 1:
            first = list_of_nodes.pop(0)
            last = list_of_nodes.pop()
            
            first.next = last
            last.next = None
            
            reorder_ptr.next = first
            reorder_ptr = last
            
        if len(list_of_nodes) == 1:
            reorder_ptr.next = list_of_nodes.pop()
            reorder_ptr.next.next = None
            result = result.next
        else:
            
            result = result.next
            
        
        return result
            
            
            
            
            