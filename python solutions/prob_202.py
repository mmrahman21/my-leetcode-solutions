class Solution:
    def isHappy(self, n: int) -> bool:
            
        count = 0
        while True:
            sum_of_square = 0
            p = n

            while p != 0:
                a = p % 10
                sum_of_square += a*a
                p = p // 10
            n = sum_of_square
            
            if n == 1:
                break
            elif n < 10:
                count += 1
                if count >= 2:
                    break
                
            print(n)
        
        return n == 1

