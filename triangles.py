n = int(input("Enter the size of triangle: "))

# Picture A
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        if i == n-1 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i+1):
        if i == n - 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Picture B
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")

    for j in range(i + 1):
        print("*", end=" ")
    print()


print()

# Picture C
for i in range(n-1):
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")
    print()
