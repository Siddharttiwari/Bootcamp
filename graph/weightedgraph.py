class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        self.graph.setdefault(u, []).append([v, weight])
        self.graph.setdefault(v, []).append([u, weight])

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])


g = WeightedGraph()

n = int(input("Enter number of edges: "))

for i in range(n):
    u = input("Enter source vertex: ")
    v = input("Enter destination vertex: ")
    weight = int(input("Enter weight: "))

    g.add_edge(u, v, weight)

g.display()