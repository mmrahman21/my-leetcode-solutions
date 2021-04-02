class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        len_1 = len(num1)
        len_2 = len(num2)
        
        i = len_1 - 1
        j = len_2 - 1
        my_sum = ""
        carry = 0
        while i >=0 and j >= 0:
            result = int(num1[i]) + int(num2[j]) + carry
            my_sum += str(result % 10)
            carry = result // 10
            i -= 1
            j -= 1
            
        if i>= 0:
            while i>=0:
                result = int(num1[i]) + carry
                my_sum += str(result % 10)
                carry = result // 10
                i -= 1
        elif j >= 0:
            while j>=0:
                result = int(num2[j]) + carry
                my_sum += str(result % 10)
                carry = result // 10
                j -= 1
        
        if carry != 0:
            my_sum += str(carry)
            
        return my_sum[-1::-1]
                
            
            
            
        