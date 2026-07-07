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
        for vertex,neighbors in self.graph.items():
            print(f"{vertex}->{neighbors}")

    
g=Graph()

g.add_edge("a","b")
g.add_edge("a","c")
g.add_edge("b","d")
g.add_edge("c","d")

g.display()