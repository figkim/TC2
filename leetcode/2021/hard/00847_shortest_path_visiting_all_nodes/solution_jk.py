import collections
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        '''
        다른 사람의 풀이를 참고하였기 때문에 설명을 추가합니다.
        특히 오늘은 솔루션을 참고하였습니다.
        
        가장 짧은 길을 찾기 위해서는 직접 돌아봐야 합니다.
        그러기 위해서는 현재 상태를 표시하여야 합니다.
        
        현재 상태는 두가지의 정보를 포함하여야 합니다.
        1. 내가 돌았던 노드들
        2. 현재 내가 위치한 노드
        
        그 중에서 내가 돌았던 노드들을 표현하는 방법 중 하나는 비트를 이용한 방법입니다.
        N개의 노드를 돌아야 하기 때문에 총 2**N가지의 상태가 가능합니다. (갔거나 / 안 갔거나)
        그래서 그 상태를 0부터 2**N-1까지의 수로 나타낼 수 있습니다.
        i번째 노드를 방문하면, i번째 자리수가 0에서 1로 바뀌거나 1에서 1로 바뀝니다.
        이를 간단하게 해결하기 위해서 bitwise or를 사용하였습니다 (|)
        
        그리고 시작지점은 N개의 노드 각각에서 시도할 수 있기 때문에 처음 queue에는 N개의 candidate가 들어갑니다.
        
        각각의 정보들을 바탕으로 Breadth First Search(BFS)를 통해 가능한 모든 경우를 탐색하고, 가장 먼저 도달하였을 때의 거리를 반환하면 됩니다.
        BFS를 이용하므로 가장 먼저 도달한 경우가 가장 빨리 도착하기 때문에 이 답이 shortest
        '''
        N = len(graph)
        queue = collections.deque([(1 << i, i) for i in range(N)])
        dist = {(1 << i, i):0 for i in range(N)}

        while queue:
            cover, node = queue.popleft()
            d = dist[(cover, node)]

            if cover == 2**N - 1:
                return d

            for child in graph[node]:
                next_cover = cover | (1 << child)

                if d + 1 < dist.get((next_cover, child), float('inf')):
                    dist[(next_cover, child)] = d + 1
                    queue.append((next_cover, child))
