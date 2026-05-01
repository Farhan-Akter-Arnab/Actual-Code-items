class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    def addEdge(self, v, w): self.adj[v].append(w)
    def DFS(self, s):
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)
        while len(stack):
            s = stack[-1]; stack.pop()
            if (not visited[s]):
                print(s, end=' '); visited[s] = True
            for vertex in self.adj[s]:
                if (not visited[vertex]): stack.append(vertex)
g = Graph(5)
g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is the Depth First Traversal")
g.DFS(0)