class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        
        num = 0
        queue = collections.deque([(0, num)])

        min_len = n + 1

        for i, ele in enumerate(A, 1):
            num += ele
            
            while queue and num <= queue[-1][-1]:
                queue.pop()

            while queue and num - queue[0][-1] >= K:
                min_len = min(min_len, i - queue.popleft()[0])

            queue.append((i, num))

        return min_len if min_len < n + 1 else -1
