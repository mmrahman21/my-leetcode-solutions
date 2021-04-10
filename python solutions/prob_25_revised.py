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
        
        d = 0
        while ptr is not None:
            d += 1
            ptr = ptr.next
            
        if d < k:
            return head
        
        counter = 0
        
        ptr = head 
        new_head = None
        
        while ptr != None:
            
            kptr = ptr
            
            if d - counter < k:
                break
        
            while True:
                
                if counter % k == 0:
                    khead = kptr 
                    kptr = kptr.next
                    khead.next = None
                    new_prev = khead
                    
                else:
                
                    temp = kptr 
                    kptr = kptr.next
                    temp.next = khead
                    khead = temp
            
                counter += 1
                if counter % k == 0:
                    break
            
            if prev is None:
                new_head = khead
                prev = new_prev
                 
            else:
                prev.next = khead
                prev = new_prev
                
            ptr = kptr
        
        if counter >= k and d - counter < k:
            prev.next = ptr
            
        return new_head
                
                
            
            
                    
                    
                    
            
          
        

        