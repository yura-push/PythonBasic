def list_to_string(list_value):
    new_list = []
    for i in range(len(list_value) - 1):
        string_val = str(list_value[i]) + ","
        new_list.append(string_val)
    new_list.append(list_value[-1])
    new_list.insert(-1, "and")
    return "'" + " ".join(new_list) + "'"


spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))
