import random
from pprint import pprint

m = int(input("Enter the size of matrix (bigger than 5): "))

matrix = [[random.randint(1, 50) for i in range(m)] for j in range(m)]
columns_sum = [0] * m

#pprint(matrix)

for j in range(len(matrix)):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[j][i]
    columns_sum[j] = col_sum
matrix.append(columns_sum)

for i in range(len(matrix) - 1):
    for j in range(len(matrix) - i - 1):
        if columns_sum[j] > columns_sum[j+1]:
            columns_sum[j], columns_sum[j + 1] = columns_sum[j + 1], columns_sum[j]
            for k in range(len(matrix)):
                matrix[k][j], matrix[k][j+1] = matrix[k][j+1], matrix[k][j]

pprint(matrix)