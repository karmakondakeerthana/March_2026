class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from typing import List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        ans = 0
        def dfs(node):
            nonlocal ans
            visited.add(node)
            total = values[node]
            for neighbor in adj[node]:
                if neighbor not in visited:
                    total += dfs(neighbor)
            if total % k == 0:
                ans += 1
                return 0 
            return total
        dfs(0)
        return ans
