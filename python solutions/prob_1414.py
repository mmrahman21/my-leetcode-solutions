
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f1 = 1
        f2 = 1
        
        fibonacci = [f2]
        
        my_sum = f2
        
        while my_sum < k:
            
            new_item = f1 + f2
            fibonacci.append(new_item)    
            
            f1 = f2
            f2 = new_item
            
            my_sum = new_item
            
        left = 0
        right = len(fibonacci) - 1
        
        result = 0
        
        while right >= 0 and k > 0:
            
            if fibonacci[right] == k:
                result += 1
                break
            elif fibonacci[right] > k:
                right -= 1
            elif fibonacci[right] < k:
                k -= fibonacci[right]
                result += 1
                right -= 1
        
        return result
        
            
        
        