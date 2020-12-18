class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)        
        candi = [start]
        avail = [start]
        
        if arr[start] == 0:
            return True

        while candi:
            idx = candi.pop()

            if 0 <= idx + arr[idx] < N and idx + arr[idx] not in avail:
                if arr[idx + arr[idx]] == 0:
                    return True
                avail.append(idx+arr[idx])
                candi.append(idx+arr[idx])

            if 0 <= idx - arr[idx] < N and idx - arr[idx] not in avail:
                if arr[idx - arr[idx]] == 0:
                    return True
                avail.append(idx-arr[idx])
                candi.append(idx-arr[idx])        
                
        return False
