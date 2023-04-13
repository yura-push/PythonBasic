def print_table(table):
    col_width = []
    for list_val in table:
        max_length = 0
        for word in list_val:
            if max_length < len(word):
                max_length = len(word)
        col_width.append(max_length)

    right_width = max(col_width)
    for j in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][j].rjust(max(col_width)), end="")
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
