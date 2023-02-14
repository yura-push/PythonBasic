s = input("Enter a string: ")
ch = input("Enter a character: ")

index = 0
while True:
    index = s.find(ch, index+1)
    if index == -1:
        break
    print("Index of 'ch':", index)