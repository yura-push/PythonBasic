def number_collaps(num):
    try:
        list_num = list(map(int, str(num)))
        total_sum = sum(list_num)
        # print(temp_sum)
        while len(str(total_sum)) >= 2:
            total_sum_list = list(map(int, str(total_sum)))
            total_sum = sum(total_sum_list)
        return total_sum
    except ValueError as exc:
        print("Only positive integer values!")


print(number_collaps(8938))
