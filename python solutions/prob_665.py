class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)
        
        count = 0
        i = 0
        loc = 0
        while i < l-1:
            if nums[i] > nums[i+1]:
                loc = i
                count += 1
                if count >= 2:
                    return False

            i += 1
       
        if count == 0:
            return True
        elif count == 1:
            
            if loc == 0:
                return True
            elif loc + 1 == l-1:
                return True
           
            elif nums[loc] > nums[loc + 2]:
                if nums[loc - 1] > nums[loc +1]:
                    return False
                else:
                    return True
            
            else:
                return True
        else:
            return False
