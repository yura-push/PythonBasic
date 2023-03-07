def collapse_number(num):
    if num <= 0:
        raise Exception("only positive integers")

    list_num = list(map(int, str(num)))
    total_sum = sum(list_num)
    while len(str(total_sum)) >= 2:
        total_sum_list = list(map(int, str(total_sum)))
        total_sum = sum(total_sum_list)
    return total_sum


print(collapse_number(8938))

