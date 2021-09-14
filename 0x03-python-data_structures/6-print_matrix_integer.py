#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columns in matrix:
        for rows in columns:
            print("{:d}".format(rows), end="")
            if rows != (columns[len(columns)-1]):
                print("", end=" ")
        print("")
