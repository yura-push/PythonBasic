stuff = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory contains:")
    values = []
    for key, value in inventory.items():
        print(f"{key}: {value}")
        values.append(value)

    print(f"Total number of items: {sum(values)}")


def add_to_inventory(inventory, added_items):
    for key, value in inventory.items():
        if key in added_items:
            inventory[key] = value + 1
        else:
            inventory[key] = 1


add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
