class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        str_length = len(s)
        
        
        while str_length > k:
           
            start = 0
            
            group_sum_list = [] 
            
            while start < str_length:
                if start >= str_length - k:
                    digit_group = s[start:]
                else:
                    digit_group = s[start:start+k]
                     
                group_sum = 0
               
                
                for digit in digit_group:
                    group_sum += (ord(digit) - ord('0'))
                
                group_sum_list.append(str(group_sum))
                
                start += k
           
            s = ''.join(group_sum_list)
          
            
            str_length = len(s)
        
        return s
            