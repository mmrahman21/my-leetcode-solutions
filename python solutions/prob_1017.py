class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        
        number = ""
        
        while N!=0:
            
            rem = N % -2
            if rem < 0:
                rem = 2 + rem
            N = (N - rem) // -2
            number +=str(rem)
        
        print(number[-1::-1])
        
        return number[-1::-1]
        