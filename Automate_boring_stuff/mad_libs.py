# Improve: add dots where needed.

mad_libs_file = open('mad_libs.txt')
content = mad_libs_file.read()
mad_libs_file.close()

content_list = content.split()
clean_content = []
for i in range(len(content_list)):
    clean_content.append(content_list[i].strip("."))

for i in range(len(clean_content)):
    if clean_content[i] == "ADJECTIVE":
        user_adjective = input("Enter an adjective: ")
        clean_content[i] = user_adjective
    if clean_content[i] == "NOUN":
        user_noun = input("Enter a noun: ")
        clean_content[i] = user_noun
    if clean_content[i] == "VERB":
        user_verb = input("Enter a verb: ")
        clean_content[i] = user_verb

print(" ".join(clean_content))

mad_libs_file = open("mad_libs.txt", "w")
mad_libs_file.write(" ".join(clean_content))
mad_libs_file.close()
