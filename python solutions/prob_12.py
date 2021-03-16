class Solution:
    def intToRoman(self, num: int) -> str:
        dict = { 1:'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
                40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                500: 'D', 900: 'CM', 1000: 'M'}
        
        if num <= 5:
            return dict[num]
        
        result = ""
        largest = 1
    
        for key in dict.keys():
            if key > num:
                break
            elif key <= num and key > largest:
                largest = key
        
        result +=dict[largest]
        
        if largest == num:
            return result
        else:
            
            return result + self.intToRoman(num - largest)
            
        
        
        