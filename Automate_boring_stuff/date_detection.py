import re

text_to_search = """
29/02/2020
31/04/2021
28/01/1995
22/09/1845
22.11.1178
01/12/1879
That is practice program
so do not judge me :)
"""

pattern = re.compile(r'([0-3][0-9])\/([0-1]?[0-9])\/([1-2]\d{3})')

matches = pattern.findall(text_to_search)

print(matches)

for match in matches:
    if match[1] == "02":
        if int(match[2]) % 4 == 0:
            if int(match[2]) % 100 != 0 or int(match[2]) % 400 == 0:
                if int(match[0]) <= 29:
                    print("Valid date", match)
    elif match[1] == "04" or match[1] == "06" or match[1] == "09" or match[1] == "11":
        if int(match[0]) <= 30:
            print("Valid date", match)
        else:
            print("Not a valid date", match)
    else:
        if int(match[0]) <= 31:
            print("Valid date", match)
