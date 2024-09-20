#!/usr/bin/python3
import sys

def print_usage_error(message, status):
    print(message)
    sys.exit(status)

# Validate and parse the input
if len(sys.argv) != 2:
    print_usage_error("Usage: nqueens N", 1)

try:
    N = int(sys.argv[1])
except ValueError:
    print_usage_error("N must be a number", 1)

if N < 4:
    print_usage_error("N must be at least 4", 1)

# Function to print a solution
def print_solution(board):
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                solution.append([row, col])
    print(solution)

# Check if a queen can be placed at board[row] and col
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# Recursive function to solve the N Queens problem
def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)
                # Backtrack (no explicit action needed here since we overwrite board[row])

# Initialize the board and start solving
board = [-1] * N
solve_nqueens(board, 0)

