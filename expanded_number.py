def expanded_form(num: int) -> str:
    list_num = [int(i) for i in str(num)]

    for i in range(len(list_num)):
        if list_num[i] > 0:
            print(str(list_num[i]) + "0" * (len(list_num) - 1 - i) + " + " if i < (len(list_num)) else "", end="")

#print(expanded_form(70304))

def expanded_form1(num):
    list_num = [int(i) for i in str(num)]
    return " + ".join(
        [str(list_num[i]) + "0" * (len(list_num) - 1 - i) for i in range(len(list_num)) if list_num[i] > 0])

#print(expanded_form1(70304))
