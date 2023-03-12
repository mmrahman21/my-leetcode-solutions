'''
It's a DP solution; however faced TLE on several submissions
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        
        dp = {}
                            
        for t in range(0, l):
            for i in range(0, l-t):
                j = i + t
                
                if i == j:
                    dp[(i,j)] = True
                    left, right = i, j
                    
                elif i+1 == j:
                    if s[i] == s[i+1]:
                        dp[(i, i+1)] = True
                        left, right = i, i+1
                    
                
                elif dp.pop((i+1, j-1), None) and (s[i] == s[j]):
                    
                    dp[(i,j)]=True 
                   
                    left, right = i, j
                       
                   
        return s[left:right+1]
