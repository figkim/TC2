class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c for c in s if c.isalnum()).lower()
        
        return new_s == new_s[::-1]
