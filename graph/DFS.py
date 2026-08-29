class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edge(self,u,v,directed=False):
        self.add_vertex(u)
        self.add_vertex(v)

        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def display(self):
        for vertex,neighbor in self.graph.items():
            print(f"{vertex}-> {neighbor}")

    def DFS(self, start, visited=None):

        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.DFS(neighbor, visited)

    
g=Graph()
n=int(input("Enter no of edge"))

for i in range(n):
    u=input(f"Enter edge{i+1} (u,v);").split()
    g.add_edge(u[0],u[1])
print("\nGraph:")
g.display()

start = input("\nEnter starting vertex: ")

print("DFS:", end=" ")
g.DFS(start)
