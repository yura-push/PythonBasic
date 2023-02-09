counter = 0
list = []
while True:
    value = int(input("Enter an integer: "))
    if value != 0:
        list.append(value)
    else:
        print("counter -", counter)
        print("sum -", sum(list))
        print("average -", sum(list) / len(list))
        print("max value =", max(list), "min value =", min(list))

        even_count = 0
        odd_count = 0
        for num in list:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print("Amount of even number -", even_count, "amount of odd numbers -", odd_count)

        break
    counter += 1
