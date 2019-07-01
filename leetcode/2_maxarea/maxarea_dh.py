import numpy as np

class Solution(object):
    def maxArea(self, height):
        table = np.zeros((len(height), len(height)))
        for i, v in enumerate(height):
            for j, _v in enumerate(height[i+1:]):
                table[i, j+i+1] = min(v, _v) * (j+1)
        return int(np.max(table))