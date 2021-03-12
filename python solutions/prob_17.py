class Solution:
    def letterCombinations(self, digits):
        dict = { 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        
        if digits == "":
            return []
        
        elif len(digits) == 1:
            return list(dict[int(digits[0])])
        
        
        s = dict[int(digits[0])]
        
        result = []
        
        
        for i in s:
            result.extend([i + char for char in self.letterCombinations(digits[1:])])
            
        
        return result
            
        
        
        


print(Solution().letterCombinations("2"))