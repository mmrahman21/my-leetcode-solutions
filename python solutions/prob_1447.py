def gcd(a, b):
    if a % b == 0:
        return b
    
    else:
        
        while a % b != 0:
            temp = b
            b = a % b
            a = temp
        
    return b

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result_list = []
        for i in range(1, n):
            j = i+1

            while j <= n:
                g = gcd(j, i)
                if g == 1:
                    result_list.append(f"{i}/{j}")
                j += 1
        
        return result_list
    