class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        p = ''.join(sorted(s))
        print(p)
        l = len(p)
        i = 0
        my_dict = {}
        
        while i < l:
            j = i + 1
            count = 1
            while j < l and p[j] == p[i]:
                count += 1
                j += 1
            my_dict[p[i]] = count
            i = j
        
        print(my_dict)
        li = list(my_dict.values())
        
        result = False
        result = all(elem == li[0] for elem in li)
        
        return result
        
        
        
        
        
        
        