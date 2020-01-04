class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for c in zip(*strs):
            if len(set(c)) == 1:
                ans += c[0]
            else:
                break
        return ans
