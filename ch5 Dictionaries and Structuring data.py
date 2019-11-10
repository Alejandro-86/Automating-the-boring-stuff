def display_inventory(dictionary):
    total_items = 0
    for s in dictionary.keys():
        total_items += dictionary[s]
        print(s, dictionary[s])
    print()
    print("total items", total_items)


def add_to_inventory(inventory, addedItems):
    return 8


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)
