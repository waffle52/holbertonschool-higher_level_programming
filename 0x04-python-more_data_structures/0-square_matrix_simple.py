#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    else:
        new_mat = [x[:] for x in matrix]
        for i in range(3):
            for j in range(3):
                new_mat[i][j] = new_mat[i][j] ** 2
        return (new_mat)
