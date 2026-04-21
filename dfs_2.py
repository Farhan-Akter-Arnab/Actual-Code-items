def dfs(graph, start):
    
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in graph[vertex]:
                stack.append(neighbour)  
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}
visited = dfs(graph, 'A')
print(visited)