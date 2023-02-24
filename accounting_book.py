lists = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

#print(list(map(lambda q, p: q * p + 10 if q * p < 100 else q * p, quantity, price)))

def total_price(*lists):
    return list(zip([i[0] for i in lists], [i[2] * i[3] if i[2] * i[3] > 100 else i[2] * i[3] + 10 for i in lists]))

print("order number : total_price", total_price(*lists))


my_lambda = lambda list_var: (list_var[0], list_var[2] * list_var[3]) if list_var[2] * list_var[3] > 100 \
    else (list_var[0], list_var[2] * list_var[3] + 10)
result = list(map(my_lambda, lists))
print(result)