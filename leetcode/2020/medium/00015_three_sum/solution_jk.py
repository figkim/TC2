import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        !! 다른 사람의 풀이를 참고하였기 때문에 답안에 설명을 첨부합니다. !!
        
        처음에는 itertool을 사용해서 모든 조합을 시도해보고 조건에 맞는 세 쌍을 찾고자 하였으나, 수가 많아 time limit에 걸리게 됩니다.
        그래서 시도한 것이 두 쌍을 뽑고 합의 역(마이너스)가 나머지 리스트에 포함되어 있는지로 판별하고자 하였으나 역시 time limit에 걸리게 됩니다.
        
        다른 사람의 풀이를 참고한 결과 일단 정렬을 한 후 두 개의 포인터로 세 쌍을 확인하는 방법을 찾았습니다.
        두 개의 포인터는 현재 타겟으로 하고 있는 숫자(num) 이후의 인덱스와 리스트의 마지막 인덱스를 가리키도록 초기화 됩니다.
        그리고 세 쌍의 숫자를 0과 비교하여 0과 맞으면 정답지에 포함시키고, 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동시키고, 0보다 크면 오른쪽 포인터를 왼쪽으로 이동시킵니다.
        이렇게 하면 O(n**2)로 찾게 되는데, 중복을 제거하기 위해 타겟을 기존과 같은지 판별하면 훨씬 빠르게 판별할 수 있습니다.        
        '''
        ans = set()

        nums.sort()

        for i, num in enumerate(nums):
            if i != 0 and num == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if num + nums[l] + nums[r] == 0:
                    ans.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1

        return list(ans)
