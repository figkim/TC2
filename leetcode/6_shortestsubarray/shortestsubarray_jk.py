class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        
        num = 0
        p = [num]
        queue = collections.deque([num])

        min_len = n + 1

        for i, ele in enumerate(A, 1):
            num += ele
            p.append(num)
            
            while queue and num <= p[queue[-1]]:
                queue.pop()

            while queue and num - p[queue[0]] >= K:
                min_len = min(min_len, i - queue.popleft())

            queue.append(i)            

        return min_len if min_len < n + 1 else -1
