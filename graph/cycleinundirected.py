from collections import deque


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

"""