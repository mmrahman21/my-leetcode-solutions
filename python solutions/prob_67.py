class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        
        carry = 0
        
        result = ""
        
        i = l1 - 1
        j = l2 - 1
        
        while i >=0 and j>=0:
            d1 = int(a[i])
            d2 = int(b[j])

            d = (d1 + d2 + carry) % 2

            carry = (d1 + d2 + carry) // 2
            result += str(d)
            
            i -= 1
            j -= 1
            
        
        if i == -1 and j == -1:
            if carry !=0:
                result += str(carry)
        
        elif i >=0 :
            while i>=0:
                d1 = int(a[i])
                d = (d1 + carry) % 2
                carry = (d1 + carry) // 2
                result += str(d)
                i -= 1
            if carry !=0:
                result += str(carry)
                
        else:
            while j>=0:
                d1 = int(b[j])
                d = (d1 + carry) % 2
                carry = (d1 + carry) // 2
                result += str(d)
                j -= 1
            if carry !=0:
                result += str(carry)
        
        return result[len(result)-1::-1]
            
print(Solution().addBinary("1111", "1"))
                
        
        