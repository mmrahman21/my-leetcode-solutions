def checkNicePairs(p, q):
    main_p = p
    main_q = q
    p1 = 0
    while p!=0:
        rem = p % 10
        p1 = p1*10 + rem
        p //= 10
        
    q1 = 0
    while q!=0:
        rem = q % 10
        q1 = q1*10 + rem
        q //= 10
    
    return main_p + q1 == main_q + p1

def transform(p):
    main_p = p
    p1 = 0
    while p!=0:
        rem = p % 10
        p1 = p1*10 + rem
        p //= 10
    
    return main_p - p1
    

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = 0
        l = len(nums)
        if  l == 1:
            return 0
        
        for i in range(l):
            nums[i] = transform(nums[i])
            
        my_map = {}
        
        for i in range(l):
            
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
            count += my_map[nums[i]] - 1
            
        return count % (10**9 + 7)