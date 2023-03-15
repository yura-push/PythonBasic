file = open("test1.txt", "w")
user_input = input("Enter something: ")
text = file.write(user_input)
while user_input != "":
    text = file.write(user_input)
file.close()