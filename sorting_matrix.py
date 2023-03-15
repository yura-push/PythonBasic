from random import randint

M = int(input("Enter the size of matrix: "))
matrix = [[randint(1, 50) for j in range(M)] for i in range(M)]


def sort_matrix(matrix):
    # знаходимо суму елементів кожного стовпця
    column_sums = [0] * len(matrix[0])
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            column_sums[j] += matrix[i][j]

    # сортуємо стовпці за зростанням сум елементів
    for j in range(len(matrix[0]) - 1):
        min_sum = column_sums[j]
        min_index = j
        for k in range(j + 1, len(matrix[0])):
            if column_sums[k] < min_sum:
                min_sum = column_sums[k]
                min_index = k
        if min_index != j:
            # міняємо місцями стовпці
            for i in range(len(matrix)):
                matrix[i][j], matrix[i][min_index] = matrix[i][min_index], matrix[i][j]
            column_sums[j], column_sums[min_index] = column_sums[min_index], column_sums[j]

    # сортуємо кожен непарний стовпець
    for j in range(1, len(matrix[0]), 2):
        for i in range(len(matrix) - 1):
            min_value = matrix[i][j]
            min_index = i
            for k in range(i + 1, len(matrix)):
                if matrix[k][j] < min_value:
                    min_value = matrix[k][j]
                    min_index = k
            if min_index != i:
                # міняємо місцями елементи
                matrix[i][j], matrix[min_index][j] = matrix[min_index][j], matrix[i][j]

    # сортуємо кожен парний стовпець
    for j in range(0, len(matrix[0]), 2):
        for i in range(len(matrix) - 1):
            max_value = matrix[i][j]
            max_index = i
            for k in range(i + 1, len(matrix)):
                if matrix[k][j] > max_value:
                    max_value = matrix[k][j]
                    max_index = k
            if max_index != i:
                # міняємо місцями елементи
                matrix[i][j], matrix[max_index][j] = matrix[max_index][j], matrix[i][j]

    return matrix, column_sums


def print_sorted_matrix(matrix, col_sums):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print()

    for i in range(len(col_sums)):
        print(col_sums[i], end="\t")


sorted_matrix, column_sums = sort_matrix(matrix)
print_sorted_matrix(sorted_matrix, column_sums)