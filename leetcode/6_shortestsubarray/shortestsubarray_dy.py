import collections 

class Solution:    
    def shortestSubarray(self, A: List[int], K: int) -> int:
        deq = collections.deque([(-1,0)]) # tuple of index & sum from zero
        sum_from_zero = 0
        ans = len(A) + 1
        
        for i, num in enumerate(A):
            sum_from_zero += num
            while deq and deq[-1][1] >= sum_from_zero:
                deq.pop()
            
            while deq and sum_from_zero - deq[0][1] >= K:
                ans = min(ans, i-deq[0][0])
                deq.popleft()
            deq.append((i,sum_from_zero))
        return ans if ans != len(A) + 1 else -1
