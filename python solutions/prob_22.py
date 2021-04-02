class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        
        result = []
        
        for i in range(1, n//2+1):
            partial_result1 = self.generateParenthesis(i)
            partial_result2 = self.generateParenthesis(n-i)
            
            for p in partial_result1:
                for q in partial_result2:
                    if f"{p}{q}" not in result:
                        result.append(f"{p}{q}")
                    if f"{q}{p}" not in result:
                        result.append(f"{q}{p}")
        
        partial_result = self.generateParenthesis(n-1)
        
        for i in partial_result:
            result.append(f"({i})")
                    
        return result
        