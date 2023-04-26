import random

import time

number_of_tries = 0
correct_answer = 0
incorrect_answer = 0

while True:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = int(input(f"{num1} * {num2} = "))

    if question == num1 * num2:
        print("Correct!")
        correct_answer += 1
        time.sleep(1)
    else:
        for i in range(2):
            question = int(input(f"{num1} * {num2} = "))

            if question == num1 * num2:
                print("Correct!")
                correct_answer += 1
                time.sleep(1)
                break
        incorrect_answer += 1

    number_of_tries += 1
    if number_of_tries == 10:
        break

print(f"{correct_answer}, {incorrect_answer}, {number_of_tries}")