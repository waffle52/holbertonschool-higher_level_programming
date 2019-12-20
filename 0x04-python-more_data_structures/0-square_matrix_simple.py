#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [x[:] for x in matrix]
    length = len(new_mat)
    for i in range(0, length):
        for j in range(0, length):
            new_mat[i][j] = new_mat[i][j] ** 2
    return (new_mat)
