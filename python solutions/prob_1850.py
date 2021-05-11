class Solution:
    def countSteps(self, s1: str, s2: str) -> int:
        
        l = len(s1)
        s1 = list(s1)
        s2 = list(s2)
        
        i = 0
        j = 0
        swaps = 0
        
        while i < l:
            j = i
            
            while s1[i] != s2[j]:
                j += 1
                
            while i < j:
                temp = s2[j-1]
                s2[j-1] = s2[j]
                s2[j] = temp
                j -= 1
                swaps += 1
            i += 1

        return swaps  
        
    def getMinSwaps(self, num: str, k: int) -> int:
        
        l = len(num)
        i = l - 2
        
        save = num
        
        res = 1001
        
        count = 0
        while count < k:
            
            i = l - 2
            while i >=0:
                if num[i] < num[i+1]:
                    break
                i -=1
            loc = -1
            for j in range(i+1, l):
                if num[j] > num[i]:
                    loc = j
            
            p = num[i+1:loc] + num[i] + num[loc+1:]
            num = num[0:i] + num[loc] + p[::-1]

          
            count += 1
            
            res = min(res, i)
          
        
        str1 = save[res:]
        str2 = num[res:]
        
        swaps = self.countSteps(str1, str2)
       
        return swaps
        