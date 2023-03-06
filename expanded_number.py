def expanded_form(num):
    try:
        list_num = [int(i) for i in str(num)]
        return "'" + " + ".join(
            [str(list_num[i]) + "0" * (len(list_num) - 1 - i) for i in range(len(list_num)) if list_num[i] > 0]) + "'"
    except ValueError as exc:
        print(exc, "only positive integer values")


print(expanded_form(70305))
