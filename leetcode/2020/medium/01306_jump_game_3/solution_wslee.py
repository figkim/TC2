class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # DFS
        stack = [start]
        visited = set()
        n = len(arr)

        while stack:
            node = stack.pop()

            if arr[node] == 0:
                return True
            visited.add(node)
            left = node - arr[node]
            right = node + arr[node]
            if left >= 0 and left not in visited:
                stack.append(left)
            if right < n and right not in visited:
                stack.append(right)

        return False
