class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(s)
        return len(s[-1])