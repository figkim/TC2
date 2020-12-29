class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # Two-pass
        #         u_hill = [0] * len(A)
        #         d_hill = [0] * len(A)
        #         for i in range(1, len(A)):
        #             if A[i] > A[i-1]:
        #                 u_hill[i] = u_hill[i-1] + 1

        #         for i in range(len(A)-2, -1, -1):
        #             if A[i] > A[i+1]:
        #                 d_hill[i] = d_hill[i+1] + 1

        #         res = 0
        #         for i in range(len(u_hill)):
        #             u = u_hill[i]
        #             d = d_hill[i]
        #             if u and d:
        #                 res = max(res, u + d + 1)

        #         return res

        # One-pass, Two-pointer
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:
                up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down:
                res = max(res, up + down + 1)
        return res



