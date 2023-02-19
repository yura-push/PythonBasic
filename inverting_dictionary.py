d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}

new_dict = {}
for key, value in d.items():
    for val in d.get(key):
        new_dict[val] = key
print(new_dict)

#print(new_dict.keys())
#print(new_dict.values())
#for value in d.get('apple'):
    #new_dict[value] = 'apple'
#print(new_dict)