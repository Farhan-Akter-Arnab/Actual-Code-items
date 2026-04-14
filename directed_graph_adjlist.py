class AdjVertex:
    def __init__(self, data):
        self.vertex = data
        self.next = None
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    def add_edge(self, src, dest):
        vertex = AdjVertex(dest);  vertex.next = self.graph[src];  self.graph[src] = vertex
        vertex = AdjVertex(src);  vertex.next = self.graph[dest];  self.graph[dest] = vertex
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}:".format(i), end=""); temp = self.graph[i]
            while temp: print(" -> {}".format(temp.vertex), end=""); temp = temp.next; print("\n")
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()