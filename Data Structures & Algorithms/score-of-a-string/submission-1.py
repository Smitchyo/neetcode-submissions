class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            total += abs(int(ord(s[i])) - int(ord(s[i+1])))
        return total