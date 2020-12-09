class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        queue = [([], target, 0)]
        res = []

        while queue:
            num_list, target, i = queue.pop()

            for j, num in enumerate(candidates[i:], i):
                if target > num:
                    queue.append((num_list + [num], target - num, j))

                elif target == num:
                    res.append(num_list + [num])
                    
        return res
