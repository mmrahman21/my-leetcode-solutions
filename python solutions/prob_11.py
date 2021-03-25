class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height) 
        if l == 2:
            return min(height)
            
        else:
            container_capacity = 0
            i = 0
            j = l-1
            while i < j:
                
                capacity = min(height[i], height[j])*(j-i)
                if capacity > container_capacity:
                    container_capacity = capacity
                    
                if height[i] > height[j]:
                    j = j - 1
                elif height[i] < height[j]:
                    i = i + 1
                else:
                    i += 1
                    j -= 1

            return container_capacity
        
        