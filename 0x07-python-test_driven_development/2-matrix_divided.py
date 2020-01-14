#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = list(matrix)
    num = len(new_list[0])
    for i in range(len(new_list)):
        if num != len(new_list[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(new_list[i])):
            if type(new_list[i][j]) != int and type(new_list[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list[i][j] = round(new_list[i][j] / div, 2)
    return (new_list)
