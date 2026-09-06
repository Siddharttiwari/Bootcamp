from collections import deque

"""
class Solution:

    def isCycle(self, V, edges):

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * V

        for i in range(V):

            if not vis[i]:

                if self.checkForCycle(adj, i, vis):
                    return True

        return False


    def checkForCycle(self, adj, start, vis):

        q = deque()

        q.append((start, -1))
        vis[start] = True

        while q:

            node, parent = q.popleft()

            for neighbor in adj[node]:

                if not vis[neighbor]:

                    vis[neighbor] = True
                    q.append((neighbor, node))


                elif neighbor != parent:

                    return True

        return False



"""

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if self.checkCycle(grid, i, j, visited, directions):
                        return True

        return False


    def checkCycle(self, grid, start_r, start_c, visited, directions):
        q = deque()
        q.append((start_r, start_c, -1, -1))
        visited[start_r][start_c] = True

        while q:
            r, c, parent_r, parent_c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= len(grid):
                    continue

                if nc < 0 or nc >= len(grid[0]):
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                if nr == parent_r and nc == parent_c:
                    continue

                if visited[nr][nc]:
                    return True

                visited[nr][nc] = True

                q.append((nr, nc, r, c))

        return False
