class Solution:
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        
        count = 0
        minimum = min([len(t) for t in strs])
        l = len(strs)
        
        if minimum == 0:
            return ""
        else:
            for i in range(minimum):
                flag = True
                for j in range(l-1):
                    if strs[j][i] != strs[j+1][i]:
                        flag = False
                        break
                    
                if flag == False:
                    break
                    
                else:
                    count += 1
        return strs[0][:count]
    
if __name__ =='__main__':
    print(Solution().longestCommonPrefix(["flow", "foul"]))
                    