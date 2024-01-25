#!/usr/bin/python

def rotate_2d_matrix(matrix):
    temp1 = ''
    size = len(matrix)

    for row in range(size):
        for col in range(row + 1, size):
            # if row > half:
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
        for row in matrix:
            row.reverse()
    return matrix
