class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        
        reverse_string = ""
        for word in range(len(word_list) - 1, -1, -1):
            if word != 0:
                reverse_string +=word_list[word]
                reverse_string +=" "
            else:
                reverse_string +=word_list[word]
                
                
        return reverse_string
            

print(Solution().reverseWords(" the sky is blue "))