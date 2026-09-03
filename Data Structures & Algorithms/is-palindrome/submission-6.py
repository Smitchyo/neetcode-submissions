class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(s)):
            left = s[i]
            right = s[-1-i]
            if left != right:
                return False
        return True