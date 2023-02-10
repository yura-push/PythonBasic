num = int(input("Enter an integer: "))
counter = 0
summary = num
max_value = num
min_value = 0
even_counter = 0
odd_counter = 0
while True:
    if num > max_value:
        max_value = num
    else:
        min_value = num

    num = int(input("Enter an integer: "))
    summary += num

    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
    counter += 1
    if num == 0:
        print("counter -", counter)
        print("sum =", summary)
        print("arithmetic mean =", summary / counter)
        print("max_value", max_value)
        print("min_value", min_value)
        print("amount of even numbers", even_counter)
        print("amount of odd numbers", odd_counter)
        break
