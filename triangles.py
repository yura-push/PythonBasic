height = int(input("Enter the heights of triangle: "))

for i in range(height):
    for j in range(height - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("*")