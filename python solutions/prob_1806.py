class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = []
        for i in range(n):
            perm.append(i)
        
        perm_count = 0
        
        while True:
            a = []
            flag = True
    
            for i in range(n):
                item = perm[i // 2] if i % 2 == 0 else perm[ (n + i - 1) // 2]
                a.append(item)
            
            perm = a
            
            perm_count += 1
            
            for i in range(n):
                if i != perm[i]:
                    flag = False
                    break
            
            if flag == True:
                break
        
        return perm_count
                
            
            
            
            
            
        