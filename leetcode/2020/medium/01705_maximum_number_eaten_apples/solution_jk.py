import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
    
        '''
        다른 사람의 풀이를 참고하여 풀었기 때문에 설명을 추가합니다
        
        기본적인 아이디어는 min heap을 이용하여 현재 시간과 유통기한을 비교하고, 현재 시간이 유통기한보다 짧은 사과를 먹는다는 것입니다
        
        시간적인 구분은 사과가 열리는 기간(apple의 길이)와 사과가 다 열리고 난 후 유통기한 이내의 사과를 먹는 기간으로 나누어집니다
        따라서 첫번째 while의 i<N과 queue가 구분됩니다
        
        현재 시간이 i 라고 할 때 
        사과가 열리는 기간에는 queue에 사과의 유통기간은 i + days[i]가 되고, 사과의 양은 apples[i]입니다
        이 정보를 queue 에 넣게 되는데 유통기간을 key가 되도록 합니다
        
        그리고 현재 시간 i와 유통기간을 비교하여 유통기간이 지난 사과를 모두 버리고, 사과의 양이 0인 항목도 모두 제거해줍니다
        
        그리고 유통기간 이내의 사과가 있으면 cnt를 올려주고, 이 사과의 양을 1 줄여줍니다
        
        그리고 시간을 업데이트 해주면 됩니다.
        '''
        
        
        queue = []
        i = 0
        cnt = 0
        N = len(apples)

        while i < N or queue:
            if i < N and apples[i] > 0:
                heapq.heappush(queue, [i + days[i], apples[i]])

            while queue and (queue[0][0] <= i or queue[0][1] == 0):
                heapq.heappop(queue)

            if queue:
                queue[0][1] -= 1
                cnt += 1

            i += 1
            
        return cnt
