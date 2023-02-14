import random

list_of_numbers = []
for i in range(1, 10):
    list_of_numbers.append(random.randint(1,10))
print(list_of_numbers)

counter = 0
for i in range(1, len(list_of_numbers[:-1])):
    if list_of_numbers[i] > list_of_numbers[i-1] and list_of_numbers[i] > list_of_numbers[i+1]:
        counter += 1

print("Number of values bigger than it`s neighbors:", counter)
