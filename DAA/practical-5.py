# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final n-queen’s matrix.
import copy

def print_board(board):
    for row in board:
        print(' '.join(['Q' if x else '.' for x in row]))
    print()

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0
    
    return False

def solve_n_queens(n, first_queen_row):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Place the first queen
    board[first_queen_row][0] = 1
    
    if solve_n_queens_util(board, 1, n) == False:
        print("Solution does not exist")
        return False
    
    print_board(board)
    return True

# Driver Code
n = 8  # Change this to the desired board size
first_queen_row = 2  # Change this to place the first queen in a different row

print(f"Solution for {n}-Queens problem with first queen in row {first_queen_row}:")
solve_n_queens(n, first_queen_row)
