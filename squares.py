counter = 0
N = 50
while True:
    counter += 1
    pow_2 = counter ** 2
    if pow_2 > N:
        break
    print(N, pow_2)
