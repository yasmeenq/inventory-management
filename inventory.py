inventory = {}

#to add any amount of products to the inventory:
print("add products to your inventory:")

product = str(input("add product or -999 to stop: ")).strip()
if product == "-999":
    print("exiting program")
else:
    while product != "-999":
        inventory[product] = 0
        product = str(input("add product or -999 to stop: ")).strip()
    print(inventory)
    print()

    #to add the quantity of your products:
    for product in inventory:
        quantity = str(input(f"{product} amount: "))
        inventory[product] = quantity
    print(inventory)
    print()    

    #ask the user if they want to add, remove, update or view products, or to exit program
    request = str(input("type: add, remove, update, view || or type no to exit: ")).strip()
    while request != "no":

        #add products
        if request == "add":
            name = str(input("enter product name you'd like to add: "))
            amount = int(input(f"enter the amount of {name}: "))
            inventory[name] = amount
            print(inventory)
            print()

        #remove products
        if request == "remove":
            name = str(input("enter product name you'd like to remove: "))
            if name in inventory:
                del inventory[name]
                print(inventory)
                print()
            else:
                print(f"{name} is not in the inventory.")
                print(inventory)
                print()

        #update products
        if request == "update":
            name = str(input("enter product name you'd like to update: "))
            if name in inventory:
                new_name = str(input("enter new product name: "))
                new_amount = int(input(f"enter new amount of {new_name}: "))
                inventory[new_name]=inventory.pop(name)
                inventory[new_name] = new_amount     
                print(inventory)
                print()
            else:
                print(f"{name} is not in the inventory.")
                print(inventory)
                print()

        #view products
        if request == "view":
            name = str(input("enter product name you'd like to view: "))
            if name in inventory:
                print(f"{name}: {inventory[name]} unit")
        request = str(input("type: add, remove, update, view || or type no to exit: ")).strip()  

print("exiting program")                  

        
