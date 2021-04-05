# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        k = len(lists)
        
        if k == 1 and not lists[0]:
            return None
        
        head_list =[lists[i] for i in range(len(lists)) if lists[i]] 
        
        result_list = ListNode()
        
        ptr = result_list
        
        while head_list:
            
            L = [head_list[i].val for i in range(len(head_list))]
            
            next_id =L.index(min(L))
            
            ptr.next = head_list[next_id]
            ptr = ptr.next
            head_list[next_id]=head_list[next_id].next
            ptr.next = None
            
            if head_list[next_id] is None:
                head_list.remove(head_list[next_id])
        
        return result_list.next
            
            
            
        
            
            