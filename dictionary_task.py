string_val = "hello world it is hello world tries count hello world "
new_dict = {}

for word in string_val.split():
    new_dict[word] = string_val.count(word)
print(new_dict)

new_dict1 = {word: string_val.count(word) for word in string_val.split()}
print(new_dict1)