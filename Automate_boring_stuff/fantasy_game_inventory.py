stuff = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory contains:")
    item_total = 0
    for key, value in inventory.items():
        print(f"{key}: {value}")
        item_total += value

    print(f"Total number of items: {item_total}")


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in list(inventory.keys()):
            inventory[item] += 1
        else:
            inventory[item] = 1


add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
