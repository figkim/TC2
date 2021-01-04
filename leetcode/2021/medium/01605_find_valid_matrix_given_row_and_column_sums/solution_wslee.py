class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n_row = len(rowSum)
        n_col = len(colSum)
        res = [[0] * n_col for _ in range(n_row)]

        for i in range(n_row):
            for j in range(n_col):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res

#         Greedy algorithm: Initialize the result res = [[0] * (m) for _ in range(n)], where n = len(rowSum) and m = len(colSum). Use two for loops to update res, with the outer loop over the row index i, and the inner loop over the column index j. For each (i, j), put the maximum possible value at res[i][j]. The maximum possible value at res[i][j] is min(rowSum[i], colSum[j]). Before entering next loop, we need to update rowSum[i] and colSum[j] since we've already put res[i][j] at the i th row and jth column of res. That is, we only need sum(res[i + 1:]) = rowSum[i] - res[i][j], and sum(res[i: j+1]) = colSum[j] - res[i][j]. So we need to do rowSum[i] -= res[i][j], and colSum[j] -= res[i][j] before entering the next loop.

# Time complexity: O(n * m), space complexity: O(n * m).

# class Solution:
#     def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
#         n = len(rowSum)
#         m = len(colSum)
#         res = [[0] * (m) for _ in range(n)]

#         for i in range(n):
#             for j in range(m):
#                 res[i][j] = min(rowSum[i], colSum[j])
#                 rowSum[i] -= res[i][j]
#                 colSum[j] -= res[i][j]

#         return res