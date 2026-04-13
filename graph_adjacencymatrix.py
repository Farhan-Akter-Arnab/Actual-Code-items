class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for i in range(num_vertices)] for j in range(num_vertices)]
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight
    
    def get_vertices(self):
        edges = []
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                if self.adjacency_matrix[i][j] != 0:
                    edges.append((i, j))
        return edges
    def __repr__(self):
        return str(self.adjacency_matrix)

graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
print(graph)