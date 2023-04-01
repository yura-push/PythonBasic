import random

# list_heads_or_tails_values = []
# heads = 0
# tails = 0

number_of_streaks = 0

for experiment_number in range(10000):
    list_heads_or_tails_values = []
    heads = 0
    tails = 0

    while len(list_heads_or_tails_values) < 100:
        heads_or_tails = random.randint(0, 1)
        if heads_or_tails == 0:
            list_heads_or_tails_values.append("H")
            heads += 1
            tails = 0
        elif heads_or_tails == 1:
            list_heads_or_tails_values.append("T")
            tails += 1
            heads = 0

        if heads == 6 or tails == 6:
            number_of_streaks += (heads // 6 + tails // 6)
            heads, tails = 0, 0


print((number_of_streaks / 10000) * 100)
