class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.vertices: self.add_vertex(vertex1)
        if vertex2 not in self.vertices: self.add_vertex(vertex2)
        if vertex1 not in self.edges: self.edges[vertex1] = set()
        self.edges[vertex1].add((vertex2, weight))
        if vertex2 not in self.edges: self.edges[vertex2] = set()
        self.edges[vertex2].add((vertex1, weight))
    def get_vertices(self): return self.vertices
    def get_edges(self): return self.edges
    def __repr__(self): return str(self.vertices) + " -> " + str(self.edges)
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("A", "C")
print(graph)