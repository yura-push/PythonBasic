while True:
    text = input("Enter something: ")

    if text != "":
        with open("test.txt", "a") as file:
            file.write(text + "\n")
    else:
        break
