class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [tokens[0]]
        
        l = len(tokens)
        i = 1
        while i < l:
            
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                
                if tokens[i] == '+':
                    stack.append(str(b+a))
                   
                elif tokens[i] == '-':
                    stack.append(str(b-a))
                  
                elif tokens[i] == '*':
                    stack.append(str(b*a))
                   
                elif tokens[i] == '/':
                    stack.append(str(int(b / a)))
                   
            i += 1
                    
        print(int(stack[0]))
        
        return int(stack[0])
                
                    
            
        