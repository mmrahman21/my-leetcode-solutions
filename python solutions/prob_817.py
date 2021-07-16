# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        
        d = {}
        
        for num in nums:
            d[num] = 1
        
        component = 0
        while head:
            
            if head.val in nums:
                component += 1  
                head = head.next
                
                while head and head.val in d:
                    head = head.next
                    
            else:
                head = head.next
            
        return component
                    
            