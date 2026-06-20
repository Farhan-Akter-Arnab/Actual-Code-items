n = 4
def isValid (n, maze, x, y, res):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0: return True
    return False
def RatMaze (n, maze, move_x, move_y, x, y, res):
    if x == n - 1 and y == n - 1: return True
    for i in range(n):
        x_new = x + move_x[i]; y_new = y + move_y[i]
        if isValid(n, maze, x_new, y_new, res):
            res[x_new][y_new] = 1
            if RatMaze(n, maze, move_x, move_y, x_new, y_new, res): return True
            res[x_new][y_new] = 0
    return False
def solveMaze(maze):
    res = [[0 for i in range(n)] for i in range(n)]; res[0][0] = 1; move_x = [1, 0, 0, -1]; move_y = [0, -1, 1, 0]
    if RatMaze(n, maze, move_x, move_y, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end = " ")
            print()
    else: print("Solution doesn't exist")
def fractional_knapsack(capacity, treasures):
    treasures.sort(key=lambda x: x['value'] / x['weight'], reverse=True)
    total_value = 0.0; loot_bag = []
    for item in treasures:
        if capacity == 0: break
        if item['weight'] <= capacity:
            capacity -= item['weight']
            total_value += item['value']
            loot_bag.append(f"Took all {item['weight']}kg of {item['name']}")
        else:
            fraction = capacity / item['weight']; value_taken = item['value'] * fraction
            total_value += value_taken
            loot_bag.append(f"Took {capacity}kg ({fraction * 100:.1f}%) of {item['name']}")
            capacity = 0
    return total_value, loot_bag
if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    print("\n--- STEP 1: ESCAPING THE MAZE ---")
    solveMaze(maze)
    print("\n--- STEP 2: LOOTING THE PATH ---")
    found_treasures = [
        {'name': 'Gold Dust', 'weight': 2, 'value': 120},   # Ratio: $60 per kg
        {'name': 'Silver Dust', 'weight': 4, 'value': 100}, # Ratio: $25 per kg
        {'name': 'Copper Dust', 'weight': 3, 'value': 30}   # Ratio: $10 per kg
    ]
    max_bag_capacity = 5
    final_value, what_we_took = fractional_knapsack(max_bag_capacity, found_treasures)
    print(f"Bag Capacity: {max_bag_capacity}kg")
    print("Action Log:")
    for action in what_we_took:
        print(f" - {action}")
    print(f"Total Loot Value: {final_value:.2f} Money Units\n")