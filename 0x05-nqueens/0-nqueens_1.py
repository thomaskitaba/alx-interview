#!/usr/bin/python3
""" N queens """

import sys


def handle_command_line_arguments():
    """ Handles command-line arguments and validates the input """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: nqueens N (where N is an integer greater "
              "than or equal to 4)")
        exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


def find_queen_positions(n, i=0, a=[], b=[], c=[]):
    """ Finds possible queen positions on the
      chessboard using backtracking
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from find_queen_positions(n, i + 1, a + [j], b + [i + j],
                                                c + [i - j])
    else:
        yield a


def solve_and_print_solutions(n):
    """ Solves the N-queens problem and prints the solutions """
    solutions = []
    solution_index = 0

    for queen_positions in find_queen_positions(n, 0):
        for column in queen_positions:
            solutions.append([solution_index, column])
            solution_index += 1

        print(solutions)
        solutions = []
        solution_index = 0


def main():
    """ Main function to execute the program """
    n = handle_command_line_arguments()
    solve_and_print_solutions(n)


if __name__ == "__main__":
    main()
