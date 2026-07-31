class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] in t:
                count += 1
        if count == len(s):
            return True
        else:
            return False