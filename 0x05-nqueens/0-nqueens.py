#!/usr/bin/python3
import sys


def print_solution(queens_positions):
    """Prints the queen positions in the specified format"""
    print([[i, j] for i, j in enumerate(queens_positions)])


def is_safe(queens_positions, row, col):
    """Check if it's safe to place a queen in the given position"""
    for i in range(row):
        if queens_positions[i] == col or \
          queens_positions[i] - i == col - row or \
          queens_positions[i] + i == col + row:
            return False
    return True


def solve_n_queens(queens_positions, row, n):
    """Recursively solve the N queens problem"""
    if row == n:
        print_solution(queens_positions)
        return

    for col in range(n):
        if is_safe(queens_positions, row, col):
            queens_positions[row] = col
            solve_n_queens(queens_positions, row + 1, n)


def n_queens(n):
    """Wrapper function to initiate the N queens solution"""
    queens_positions = [-1] * n
    solve_n_queens(queens_positions, 0, n)


def handle_command_line_arguments():
    """Handles command-line arguments and validates input"""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: nqueens N (where N is an integer greater"
              "than or equal to 4)")
        exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


if __name__ == "__main__":
    N = handle_command_line_arguments()
    n_queens(N)
