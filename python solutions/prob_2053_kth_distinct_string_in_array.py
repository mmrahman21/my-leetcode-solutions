class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        string_dict = {}
        
        for ch in arr:
            string_dict[ch] = string_dict.get(ch, 0) + 1
        
        print(string_dict)
        count = 0
        
        for p in string_dict.keys():
            if string_dict[p] == 1:
                count += 1
                if count == k:
                    return p
        
        return ""
        