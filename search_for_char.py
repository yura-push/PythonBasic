s = input("Enter a string: ")
ch = input("Enter a character: ")

i = -1
while True:
    i = s.find(ch, i+1)
    if i == -1:
        break
    print("Index of letter:", ch, i)
