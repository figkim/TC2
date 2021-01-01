class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        !! 다른 사람의 풀이를 참고하였기 때문에 답안에 설명을 첨부합니다. !!
        
        현재 타이밍에 가능한 행동은 총 4가지가 있습니다 (사실 3가지여도 될 거 같은데, 확인해봐야 함)
        1 주식을 산다
        2 주식을 사지 않는다
        3 주식을 판다
        4 주식을 팔지 않는다
        
        이때 2와 4 행동의 경우 아무것도 하지 않는다는 점에서 동일하지만, 현재 주식을 보유하고 있는지에 따라 달라집니다.
        
        각각의 행동을 취할 때 기존의 탐색된 결과를 바탕으로 최적의 결과를 얻으려면 다음과 같이 식을 세워 dynamic programming으로 풀 수 있습니다.
        1 주식을 산다 : 주식을 판 다음에는 바로 살 수 없기 때문에 주식을 사지 않았을 때의 결과에서 주식의 가격만큼 빼줍니다.
        2 주식을 사지 않는다 : 주식을 사지 않는 행동을 위해서는 주식을 사지 않았거나, 주식을 팔았을 때의 최고 결과를 가져옵니다.
        3 주식을 판다 : 주식을 팔기 위해서는 주식을 보유해야 하므로, 주식을 샀거나, 팔지 않았을 때의 최고 결과에서 주식 가격을 더해줍니다.
        4 주식을 팔지 않는다 : 주식을 팔기 위해서는 주식을 보유해야 하므로, 주식을 샀거나, 팔지 않았을 때의 최고 결과를 가져옵니다.
        
        위의 네 개의 식으로 dynamic programming으로 전체 주식 가격에 대해 탐색 한 후, 모든 주식을 다 판 결과가 최고의 결과이므로, 주식
        '''
        if len(prices) < 2: return 0
        
        # buy not buy sell not sell
        reward = [-prices[0], 0, 0, -prices[0]]
        
        for price in prices[1:]:            
            reward = reward[1] - price, max(reward[1], reward[2]), max(reward[0], reward[3]) + price, max(reward[0], reward[3])
        
        return max(reward[1], reward[2])
