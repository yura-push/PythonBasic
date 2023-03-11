from random import randint

M = int(input("Enter number of rows: "))
N = int(input("Enter number of columns: "))

matrix = [[randint(1, 50) for j in range(N)] for i in range(M)]


def sum_matrix_positions(m):
    for i in range(M):
        sum_row = 0
        for j in range(N):
            sum_row += matrix[i][j]
        print("\t".join(map(str, matrix[i])), "\t",  sum_row)

    for j in range(N):
        sum_column = 0
        for i in range(len(matrix)):
            sum_column += matrix[i][j]
        print(sum_column, end="\t")


sum_matrix_positions(matrix)