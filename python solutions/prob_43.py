class Solution:
    def multiply(self, num1: str, num2: str) -> str:
       
        len_1 = len(num1)
        len_2 = len(num2)
        
        if len_1 < len_2:
            temp = num1
            num1 = num2
            num2 = temp
            
            temp = len_1
            len_1 = len_2
            len_2 = temp
            
        
        i = len_2 - 1
        my_prod = 0
        
        while i >= 0:
            result = ""
            carry = 0
            for j in range(len_1-1, -1, -1):
                digit_product = int(num1[j])*int(num2[i]) + carry
                carry = digit_product // 10
                rem = str(digit_product % 10)
                result += rem
               
            if carry != 0:
                result += str(carry)

            my_prod += int(result[-1::-1])*(10**(len_2 - i - 1))
           
            i -= 1
        
        return str(my_prod)
            
                
                
                
                
                
            
        