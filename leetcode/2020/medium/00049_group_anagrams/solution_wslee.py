from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        tmp = defaultdict(list)
        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in tmp:
                tmp[key] = [elem]
            else:
                tmp[key] += [elem]
        return tmp.values()
