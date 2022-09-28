from search_operations.search_products import view_product_names
import json
filename = 'storage/products.json'


def update_product():
    view_product_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    while True:
        print("Which ID would you like to update?: ")
        update_option = input("Select an ID: ")
        if update_option in open_list:
            name = input("Update Product name: ")
            while True:
                try:
                    quantity = int(input("Enter Quantity: "))
                except ValueError:
                    print("Please enter number values")
                    continue
                break
            while True:
                try:
                    price = int(input("Enter Price: "))
                except ValueError:
                    print("Please enter number values")
                    continue
                break
            open_list[update_option]["name"] = name
            open_list[update_option]["quantity"] = quantity
            open_list[update_option]["price"] = price
            print("Product Data updated")
            break
        else:
            print("ID does not exist. Please input existing ID")
    temp = [open_list]
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
