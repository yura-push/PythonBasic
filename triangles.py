def print_triangle(height, fill_symbol=".", outer_symbol=".", border_symbol="*"):
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol * ((i - 1) if i > 0 else 0),
            fill_symbol * i,
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))


#print_triangle(8, fill_symbol="*", outer_symbol=" ")
#print()


def print_diamond(height, fill_symbol=".", outer_symbol=".", border_symbol="*"):
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol * (i - 1),
            fill_symbol * i,
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))

    for i in range(height-2, -1, -1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            outer_symbol * (2 * i - 1),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )


def print_diamond2(height, fill_symbol=".", outer_symbol=".", border_symbol="*"):
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol * (i - 1),
            fill_symbol * i,
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))

    for i in range(height-2, -1, -1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            outer_symbol * (i - 1),
            border_symbol if i > 0 else "",
            outer_symbol * (i - 1),
            border_symbol if i > 0 else " ",
            outer_symbol * (height - i - 1),
            sep=""
        )


print_diamond2(8, fill_symbol="*", outer_symbol=" ")
