class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        idx = 0
        inc = False
        dec = False
        max_leng = 0

        N = len(arr)

        for i in range(1, N):
            if arr[i-1] < arr[i]:
                if inc:
                    continue

                if dec:
                    max_leng = max(i - idx, max_leng)
                    dec = False

                idx = i-1
                inc = True

            elif arr[i-1] > arr[i]:
                if dec:
                    continue

                if inc:
                    dec = True
                    inc = False

            else:
                if dec:
                    max_leng = max(i - idx, max_leng)
                    dec = False

                inc = False
                dec = False

        if dec:
            max_leng = max(N - idx, max_leng)
            
        return max_leng
