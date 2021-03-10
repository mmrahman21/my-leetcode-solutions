from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            
            else:
                
                if stack:
                    
                    if ch == ')' and stack.pop() != '(':
                        return False

                    elif ch == '}' and stack.pop() != '{':
                        return False

                    elif ch == ']' and stack.pop() != '[':
                        return False
                else:
                    return False

        return not stack

print(Solution().isValid("}}"))
            
        