class Solution(object):
    def plusOne(self, digits):
        return list(map(str, str(int(''.join(list(map(str, digits)))) + 1)))
