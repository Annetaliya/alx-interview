#!/usr/bin/python3
'''3d matrix rotation function'''


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix (rows become columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the final rotated matrix
    for i in range(n):
        matrix[i].reverse()
