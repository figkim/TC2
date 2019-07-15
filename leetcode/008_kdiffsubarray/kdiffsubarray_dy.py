import collections

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        near_deq = collections.deque()
        near_memo = {} # Rule : pop if len(near_memo) == K
        
        far_deq = collections.deque()
        far_memo = {} # Rule : pop if len(far_deq) > K
        
        ans = 0
        for i, num in enumerate(A):
            # push into nearest deq
            near_deq.append((num, i))
            if num not in near_memo:
                near_memo[num] = 1
            else:    
                near_memo[num] += 1
            near_flag = False if len(near_memo) < K else True
            # pop from near_deq
            while near_flag:
                if len(near_memo) == K and near_memo[near_deq[0][0]]-1 == 0: # stop before len(far_memo) became K-1
                    near_flag = False
                else:
                    near_memo[near_deq[0][0]] -= 1
                    if near_memo[near_deq[0][0]] == 0:
                        near_memo.pop(near_deq[0][0], None)
                    near_deq.popleft()
            # push into fareast
            far_deq.append((num, i))
            if num not in far_memo:
                far_memo[num] = 1
            else:
                far_memo[num] += 1
            far_flag = False if len(far_memo) <= K else True
            # pop from far_deq
            while far_flag:
                if len(far_memo) == K: # stop exactly len(far_memo) became K
                    far_flag = False
                else:
                    far_memo[far_deq[0][0]] -= 1
                    if far_memo[far_deq[0][0]] == 0:
                        far_memo.pop(far_deq[0][0], None)
                    far_deq.popleft()

            # accumulate ans 
            if len(near_memo) == K:
                ans += near_deq[0][1] - far_deq[0][1] + 1
        return ans 
