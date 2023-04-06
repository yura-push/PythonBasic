stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory contains:")
    values = []
    for key, value in inventory.items():
        print(f"{key}: {value}")
        values.append(value)

    print(f"Total number of items: {sum(values)}")

display_inventory(stuff)
