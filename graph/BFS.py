from collections import deque
class Graph:

    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edge(self,u ,v, directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)
    def display(self):
        for vertex,neighbor in self.graph.items():
            print(f"{vertex}->{neighbor}")


    def BFS(self,start):
        visited=set()
        queue=deque([start])
        while queue:
            vertex=queue.popleft()
            if vertex not in visited:
                print(vertex,end="")
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)


"""
g=Graph()
g.add_edge("A","B")
g.add_edge("A","c")

g.BFS("A")
"""

g = Graph()

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input(f"Enter edge {i + 1} (u v): ").split()
    g.add_edge(u[0], u[1])

print("\nGraph:")
g.display()


start = input("\nEnter starting vertex: ")


print("BFS:", end=" ")
g.BFS(start)
"""
Example input
Enter number of edges: 3

Enter edge 1 (u v): A B
Enter edge 2 (u v): A C
Enter edge 3 (u v): B D

"""