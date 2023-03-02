def expanded_form(num: int) -> str:
    list_num = [i for i in num]


num = 120503
list_num = [int(i) for i in str(num)]

#for i in range(len(list_num)):
    #print(str(list_num[i]), end="")

for i in range(len(list_num)):
    if list_num[i] > 0:
        print(str(list_num[i]) + "0"*(len(list_num) - 1 - i) + " + " if i < len(list_num) else "", end="")
