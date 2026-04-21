from collections import defaultdict
class Graph:
    def __init__(self): self.graph = defaultdict(list)
    def add_edge(self, u, v): self.graph[u].append(v)
    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbour in self.graph[vertex]:
                if not visited[neighbour]: queue.append(neighbour); visited[neighbour] = True
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Breadth First Traversal (starting from vertex 2):")
    g.bfs(2)