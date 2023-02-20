a = [int(i) for i in range(1, 10)]
print(a)
k = int(input("Enter an index to remove: "))

for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()

print(a)
