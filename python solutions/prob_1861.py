class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        m = len(box)
        n = len(box[0])
        
        for i in range(m):
            
            j = n - 2
            
            while j >= 0:
                if box[i][j] == '#' and box[i][j+1] == '.':

                    p = j + 1

                    while p < n and box[i][p] != '*' and box[i][p] != '#':
                       
                        box[i][p] = box[i][p-1]
                        box[i][p-1] = '.'
                        p += 1
                j -= 1
        
        
        print(box)
        
        res =[[0 for i in range(m)] for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][m-1-i] = box[i][j]
        
       
        # res = [[i[k] for i in box][::-1] for k in range(n)]
        
        print(res)
        
        return res
                    
        