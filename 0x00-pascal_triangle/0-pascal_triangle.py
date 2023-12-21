#!/usr/bin/python3
"""Return list of integers representing the Pascal's triangle of n."""


def pascal_triangle(n):
    """ return 2D array """
    if n <= 0:
        return []

    arr = []
    for row in range(n):
        arr_in = []

        for col in range(row + 1):
            if col == 0 or col == row:
                arr_in.append(1)
            else:
                num1 = arr[row - 1][col - 1]
                num2 = arr[row - 1][col]
                arr_in.append(num1 + num2)

        arr.append(arr_in)
    return arr
