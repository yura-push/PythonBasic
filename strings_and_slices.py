string_val = "hello world"

print("Third char:", string_val[2])
print("Second last char:", string_val[-2])
print("First five char:", string_val[:5])
print("String without last two char:", string_val[:-2])
print("Char`s with even indexes:", string_val[::2])
print("Char`s with odd indexes:", string_val[1::2])
print("Char`s in reversed order:", string_val[::-1])
print("Char`s of the string one by one in reverse order:", string_val[-1::-2])
print("Length of the string:", len(string_val))