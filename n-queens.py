def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    def is_safe(row, col):
        for i in range(col):
            if board [row][i] == 1: return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1: return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1: return False
        return True
    def solve(col):
        if col == N: return True
        for row in range(N):
            if is_safe(row, col):
                board[row][col] = 1
                if solve(col + 1):
                    return True
                board[row][col] = 0
        return False
    if solve(0):
        for row in board:
            print(row)
    else: print("NOO SOLUTION")
solve_n_queens(10)