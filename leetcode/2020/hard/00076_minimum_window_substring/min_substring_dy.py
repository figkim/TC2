class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_cnt = {}
        for character in t:
            if character not in char_cnt:
                char_cnt[character] = 1
            else:
                char_cnt[character] += 1

        dq = [] # add index & character
        min_substring = None
        for i in range(len(s)):
            if s[i] in t:
                char_cnt[s[i]] -= 1
                dq.append((i, s[i]))
                while len(dq) > 0 and char_cnt[dq[0][1]] < 0:
                    char_cnt[dq[0][1]] += 1
                    del dq[0]
                containAll = True
                for char in char_cnt:
                    if char_cnt[char] > 0:
                        containAll = False
                        break
                if containAll:
                    substring = s[dq[0][0]:dq[-1][0]+1]
                    if min_substring is None or len(substring) < len(min_substring):
                        min_substring = substring
        return min_substring if min_substring else ""

