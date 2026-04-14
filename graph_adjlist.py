# A graph data structure implemented as an adjacency list
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[i] for i in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def print_graph(self):
        for i in range(self.num_vertices):
            print(i, "->", self.adj_list[i])

# Create a graph with 5 vertices
g = Graph(5)

# Add edges between vertices (0 and 1), (0 and 2), (1 and 2), (2 and 3), (3 and 4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
# Print the graph
g.print_graph()