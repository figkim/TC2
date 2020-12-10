class Solution:
    # https://blog.naver.com/sohyunwriter/222112515685
    def combinationSum(self, candidates, target):
        result = []

        def dfs(cur, cursum, elems, target):
            if cursum == target:
                result.append(elems[:]) # copy
                return

            for i in range(cur, len(candidates)):
                if (cursum+candidates[i]) > target:
                    # early stop
                    return

                elems.append(candidates[i])
                dfs(i, cursum+candidates[i], elems, target)
                elems.pop()

        candidates.sort()
        dfs(0,0,[], target)

        return result
