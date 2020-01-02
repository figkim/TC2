import collections 

class Solution:    
    def shortestSubarray(self, A: List[int], K: int) -> int:
        deq = collections.deque([(-1,0)]) # tuple of index & sum from zero 
        # rule for deque : if x1 < x2, then deq[x1] < deq[x2]
        sum_from_zero = 0
        ans = len(A) + 1
        
        # let B(x) as sum from zero to x, then B(x2) - B(x1) is sum from x1 to x2 (if x2 > x1)
        # My deque will collect possible candidates for x1 (x1_candidates)
        # Iterate for x to check 1) whether it is better x1, and 2) whether it can be x2 for existing x1_candidates 
        # 1) Whether it is better x1? 
        # we can think strict constraint for x1. 
        # if x1_candidate1 < x1_candidate2 & B(x1_candidate1) > B(x1_candidate2), 
        # then x1_candidate2 is always better solution than x1_candidate1.
        # "rule for deque : if x1 < x2, then deq[x1] < deq[x2]" is come from this constraint
        # 2) Whether it can be x2 for existing x1_candidates? 
        # check x2_candidate (check B(x2_candidate) - deq[0] >= K)
        for i, num in enumerate(A): 
            sum_from_zero += num
            while deq and deq[-1][1] >= sum_from_zero:
                deq.pop()
            
            while deq and sum_from_zero - deq[0][1] >= K:
                ans = min(ans, i-deq[0][0])
                deq.popleft()
            deq.append((i,sum_from_zero))
        return ans if ans != len(A) + 1 else -1
