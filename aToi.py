def myAtoi(s):
        
        updated_str = s.strip()
        l = len(updated_str)
        
        ind = 0
        if l > 0 and updated_str[0] == '-':
            flag = -1
            ind = 1
        elif l > 0 and updated_str[0] == '+':
            flag = 1
            ind = 1
        elif l>0:
            flag = 1
            ind = 0
        else:
            return 0
            
       
        
        is_digit = True
        
        sum = 0
        while is_digit and ind < l:
            ch = updated_str[ind]
            if ch >= '0' and ch <= '9':
                sum = sum*10 + int(ch)
            else:
                is_digit = False
            ind += 1
         
        
        if flag == -1 and sum > (1 << 31):
            return (1 << 31) * flag
        elif flag == 1 and sum > ((1 << 31) -1):
            return (1 << 31) -1
        
        else:
            return sum * flag 
            
            
        
print(myAtoi(""))
