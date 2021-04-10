def checkPowers(n):
    if n == 1:
        return True

    if n == 2:
        return False

    if n == 3:
        return True

    k = 3
    counter = 1
    while k < n:
        k = k*3
        counter += 1

    if k != n:
        k = k // 3
        counter -= 1
        
    if n-k == 0:
        return True
    
    elif n-k >= 3**counter:
        return False
    else:
        return checkPowers(n-k)
        
    
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return checkPowers(n)
            
        
            
        