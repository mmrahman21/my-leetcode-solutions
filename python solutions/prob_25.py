# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head.next == None or k==1:
            return head
        
        ptr = head
        prev = None
        
        while ptr != None:
            
            kptr = ptr
            counter = 0
            
            while kptr is not None and counter < k:
                if counter == 0:
                    khead = ListNode(val = kptr.val)
                    new_prev = khead
                else:
                    temp = ListNode(val = kptr.val)
                    temp.next = khead
                    khead = temp
                counter += 1
                kptr = kptr.next
                
            
            if counter == k and prev is None:
                new_head = khead
                prev = new_prev
                
            elif counter < k and prev is None:
                new_head = head
            
            elif counter == k and prev is not None:
                prev.next = khead
                prev = new_prev
            elif counter < k and prev is not None:
                prev.next = ptr
            
            ptr = None
            ptr = kptr
            
        return new_head
                
                
            
            
                    
                    
                    
            
          
        

        