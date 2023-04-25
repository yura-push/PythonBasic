import re


def regex_strip_method(string_var, char_to_remove=" "):
    if char_to_remove == ".":
        pattern = re.compile(r'\w+[^\.]')
        matches = pattern.findall(string_var)
        string_var = " "
        for match in matches:
            string_var += match
        print(string_var)

    if char_to_remove == ",":
        pattern = re.compile(r'\w+[^\,]')
        matches = pattern.findall(string_var)
        string_var = " "
        for match in matches:
            string_var += match
        print(string_var)

    if char_to_remove == " ":
        pattern = re.compile(r'\w+\S')
        matches = pattern.findall(string_var)
        string_var = " ".join(matches)
        print(string_var)


string_to_test = ' Hello darkness, my old friend. '

regex_strip_method(string_to_test, ",")
