def expanded_form(num):
    if num <= 0:
        raise Exception("only integers bigger than 0")

    list_num = [int(i) for i in str(num)]
    return "'" + " + ".join(
        [str(list_num[i]) + "0" * (len(list_num) - 1 - i) for i in range(len(list_num)) if list_num[i] > 0]) + "'"


print(expanded_form(0))