class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words= s.split()
        words = words[0:k]
        return ' '.join(words)
        