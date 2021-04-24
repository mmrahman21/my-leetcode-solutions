class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        my_dict = {}
        
        for char in sentence:
            my_dict[char] = my_dict.get(char, 0) + 1
        
        if len(my_dict.keys()) == 26:
            return True
        else:
            return False
        