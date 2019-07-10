class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def add_dict(new_dict, num):
            if num not in new_dict[0]:
                new_dict[0][num] = 1
                new_dict[1] += 1
            else:
                new_dict[0][num] += 1

        def remove_dict(new_dict, num):
            if new_dict[0][num] == 1:
                del new_dict[0][num]
                new_dict[1] -= 1
            else:
                new_dict[0][num] -= 1
                
        # > (i, j)* = K : there are exactly K different integers in subarray from A[i] to A[j] (i < j)
        # > S_j : set of i which (i, j)* = K 
        #
        # > if i1 < i2 < i3 and i1, i3 in S_j then i2 in S_j
        #
        # for given j, number of subarrays with K different integer whose last element is A[j] is max(S_j) - min(S_j)       
        # So answer is sum([max(S_j) - min(S_j) for j in range(len(A))])

        l = 0
        r = 0

        min_dict = [{}, 0]
        max_dict = [{}, 0]
        
        cnt = 0

        for num in A:
            add_dict(min_dict, num)
            add_dict(max_dict, num)
            
            while min_dict[1] > K:
                remove_dict(min_dict, A[l])
                l += 1

            while max_dict[1] >= K:
                remove_dict(max_dict, A[r])
                r += 1

            cnt += r - l
            
        return cnt
