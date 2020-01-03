class Solution(object):
    def isPalindrome(self, x):
        rev = list(str(x))
        rev.reverse()
        return str(x) == ''.join(map(str, rev))
