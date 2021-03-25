class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)
        
        if l == 1:
            return 0
        
        ops1 = 0
        ops2 = 0
        
        current_expected_bit_1 = 0
        current_expected_bit_2 = 1
            
        
        for ch in range(l):
            if int(s[ch]) != current_expected_bit_1:
                ops1 += 1
            if int(s[ch]) != current_expected_bit_2:
                ops2 += 1
            
            current_expected_bit_1 = 1 - current_expected_bit_1
            current_expected_bit_2 = 1 - current_expected_bit_2
        
        return min(ops1, ops2)

print(Solution().minOperations("10101110010101"))