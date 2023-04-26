import pyinputplus as pyip

prices = {'wheat': 1, 'white': 2, 'sourdough': 3,
          'chicken': 1, 'turkey': 2, 'ham': 3, 'tofu': 4,
          'cheddar': 1, 'Swiss': 2, 'mozzarella': 3,
          }

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)

want_cheese = pyip.inputYesNo("Do you want cheese? ")
if want_cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
else:
    cheese_type = None

toppings_list = []
want_mayo = pyip.inputYesNo("Do you want to add mayo? ")
if want_mayo == 'yes':
    toppings_list.append(want_mayo)
want_mustard = pyip.inputYesNo("Do you want to add mustard? ")
if want_mustard == 'yes':
    toppings_list.append(want_mustard)
want_lettuce = pyip.inputYesNo("Do you want to add lettuce? ")
if want_lettuce == 'yes':
    toppings_list.append(want_lettuce)
want_tomatoes = pyip.inputYesNo("Do you want to add tomatoes? ")
if want_tomatoes == 'yes':
    toppings_list.append(want_tomatoes)

number_of_sandwiches = pyip.inputInt("How many sandwiches do you want? ", min=1)

sandwich_price = 0
for key in list(prices.keys()):
    if key == bread_type or key == protein_type or key == cheese_type:
        sandwich_price += prices[key]

if len(toppings_list) >= 1:
    sandwich_price += (len(toppings_list)/2)

if number_of_sandwiches > 1:
    sandwich_price *= number_of_sandwiches

print(f"Your order price is {sandwich_price}$")
