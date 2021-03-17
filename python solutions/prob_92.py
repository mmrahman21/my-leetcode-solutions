# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        ptr = head
        counter = 0
        
        last = None
        left_last = None
        
        while ptr is not None and counter <= right:
            
            counter += 1
            
            if counter < left:
                left_last = ptr
                
            if counter >= left and counter <= right:
                  
                node = ListNode()
                node.val = ptr.val
                node.next = last
                last = node
                
                if counter == left:
                    save_left_before_reverse = node
                
                if counter == right:
                    save_right = ptr.next
                
            ptr = ptr.next
            
        
        save_left_before_reverse.next = save_right

        if left_last is not None:
            left_last.next = last

            return head

        else:
            return last
            
                
                
            
            
            
        