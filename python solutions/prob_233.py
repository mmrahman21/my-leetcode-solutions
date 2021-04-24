class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        comleftX = E if A < E else A
        comleftY = B if B > F else F

        comrightX = C if C < G else G
        comrightY = H if H < D else D
            
        
        if comleftY < comrightY and comrightX > comleftX:
            return (C-A)*(D-B) + (G-E)*(H-F) - (comrightX - comleftX)*(comrightY - comleftY)
        
        else:
            return (C-A)*(D-B) + (G-E)*(H-F)
        
        
        