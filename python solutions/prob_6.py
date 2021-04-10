class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        dir_flag = True
        
        dict = {i:[] for i in range(numRows)}
        
        l = len(s)
        
        row_index = 0
        count = 0
        
        while count < l:
            dict[row_index].append(s[count])
            
            if row_index < numRows - 1 or row_index > 0:
                if dir_flag:
                    row_index += 1
                else:
                    row_index -=1
            if row_index == 0 or row_index == numRows-1:
                dir_flag = not dir_flag 
                
            count += 1
        
        result_string = ""
        
        for k in dict.keys():
            result_string +=''.join(dict[k])
        
        return result_string
        
        
         