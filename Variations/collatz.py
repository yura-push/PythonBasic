def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


try:
    user_input = int(input("Enter a number: "))
    test_val = collatz(user_input)
    while test_val != 1:
        test_val = collatz(test_val)
except ValueError:
    print("Enter an integer value!")
