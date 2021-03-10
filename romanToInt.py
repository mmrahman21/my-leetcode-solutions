def romanToInt(s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        sum = 0
        
        last_processed_index = -1
        i = 0
        
        while i < len(s) - 1:
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                sum += (dict[s[i+1]] - dict['I'])
                i = i + 2
                
                
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                sum += (dict[s[i+1]] - dict['X'])
                i = i + 2
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                sum += (dict[s[i+1]] - dict['C'])
                i = i + 2
            else:
                sum += dict[s[i]]
                i = i + 1
                
            last_processed_index = i - 1
            
            print(sum)
       
        if last_processed_index < len(s) - 1:
            sum += dict[s[i]]
            
        return sum
print(romanToInt("MCMXCIV"))
        