counter = 0
N = 50
print(N, end=' ')
while True:
    pow_2 = counter ** 2
    counter += 1
    if pow_2 > N:
        break
    print(pow_2, end=' ')
