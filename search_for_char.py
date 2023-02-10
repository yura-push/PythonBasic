s = input("Enter a string:")
ch = input("Enter a character")

for char in s:
    index = s.find(ch)
    print(index)