class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        l = len(nums)
        
        i = 0
        
        dict = {i:[] for i in range(l)}
        
        while i < l:
            
            j = i
            
            if len(dict[i]) == 0:
                dict[i].append(j)
            
            while True:
                
                if j != i:
                    dict[i].append(j)

                j = j + nums[j]
                if j > l - 1 or j < 0:
                    j = j % l
                
                
                if j == i:
                    if len(dict[i]) >= 2:
                        return True
                    
                    break
                    
                if nums[i]*nums[j] < 0:
                    break
                    

                if len(dict[i]) > l:
                    break
            i = i + 1
        
        return False

            
            
        