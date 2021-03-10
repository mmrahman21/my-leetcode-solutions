import collections

class Solution:
    def groupAnagrams(self, strs):
        
        result = collections.defaultdict(list)
        
        l = len(strs)
        
        i = 0
        
        while i < l:
            result[tuple(sorted(strs[i]))].append(strs[i])
            i = i+1 
        
                
        return result.values()
            

if __name__ =='__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
