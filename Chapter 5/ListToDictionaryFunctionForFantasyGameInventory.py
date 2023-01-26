def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    print(inventory)
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # your code goes here
    l = []
    for i in addedItems:
        if i in inventory and i not in l:
            l.append(i)
            inventory[i] += addedItems.count(i)
        elif i not in inventory and i not in l :
            inventory[i] = addedItems.count(i)
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
