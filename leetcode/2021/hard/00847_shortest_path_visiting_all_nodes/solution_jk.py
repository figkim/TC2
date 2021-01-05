import collections
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
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
