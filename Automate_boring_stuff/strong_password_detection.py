import re


def strong_password_detector(password):
    pattern = re.compile(r'\w+\d+')

    matches = pattern.findall(test_passwords)

    for match in matches:
        if len(match) >= 8:
            print("Strong password:", match)


test_passwords = '''
AbaBagalAmaG92
mike1
qwerty
helloWorld
qwertYuIOP212
'''

strong_password_detector(test_passwords)
