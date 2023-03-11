import random
from pprint import pprint

m = int(input("Enter the size of matrix (bigger than 5): "))

matrix = [[random.randint(1, 50) for i in range(m)] for j in range(m)]
pprint(matrix)

# t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
# for i in range(len(t_matrix)):
#     sum_row = 0
#     for j in range(len(t_matrix[0])):
#         sum_row += t_matrix[i][j]
#     t_matrix.append(sum_row)
#     print(t_matrix[i], sum_row)


answer = []
for i in range(len(matrix)):
    sum_col = 0
    for j in range(len(matrix[0])):
        sum_col += matrix[j][i]
    answer.append(sum_col)
matrix.append(answer)
pprint(matrix)