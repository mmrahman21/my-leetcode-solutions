class Solution:
    def plusOne(self, digits):
        carry = 0
        result = []
        for i in range(len(digits)-1,-1, -1):
            if i == len(digits) - 1:
                carry = 1
            digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            result.append(digit)
        
        if carry != 0:
            result.append(carry)
        
        return result[len(result)-1::-1]
            

print(Solution().plusOne([9, 9, 9]))