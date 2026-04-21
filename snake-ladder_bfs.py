from collections import deque
def snake_ladder_bfs(board_size, transitions):
    visited = {1}
    queue = deque([(1,0)])
    while queue:
        vertex, steps = queue.popleft()
        if vertex == board_size: return steps
        for dice_roll in range(1, 7):
            next_vertex = vertex + dice_roll
            destination = transitions.get(next_vertex, next_vertex)
            if 1 <= next_vertex <= board_size and destination not in visited:
                visited.add(destination); queue.append((destination, steps + 1))
    return -1
# Example usage:
ladders_snakes = {
    14: 7,
    8: 24,
    10: 12,
    16: 40,
    67: 3,
    50: 97
}
start = 1
print("Minimum steps required:", snake_ladder_bfs(100, ladders_snakes))