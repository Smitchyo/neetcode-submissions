class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(s)
        word = s[-1]
        return len(word)