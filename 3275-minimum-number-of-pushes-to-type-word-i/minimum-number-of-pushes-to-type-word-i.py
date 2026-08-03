class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        r=0
        for i  in range(n):
            r +=i//8+1
        return r