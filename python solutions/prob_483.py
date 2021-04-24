import random 
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> List[float]:
        
        random_rad = self.radius*sqrt(uniform(0, 1))
        theta = uniform(0, 2*pi)
            
        return [self.x+ random_rad*cos(theta), self.y+ random_rad*sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()