from search_operations.search_products import view_product_names
import json
filename = 'storage/products.json'


def check_duplicate_product_name(p_name, p_id):
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp

    for i in open_list:
        if i == p_id:
            continue
        elif open_list[i]['name'] == p_name:
            return 'y'
        else:
            continue
    return


# Updates Product data by ID
def update_product():
    view_product_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    while True:
        print("Which ID would you like to update?: ")
        update_option = input("Select an ID: ")
        if update_option in open_list:
            print(f"Name: {open_list[update_option]['name']}")
            while True:
                name = input("Update Product name: ")
                check_name = check_duplicate_product_name(name, update_option)
                if check_name == 'y':
                    print('Product name already exists. Please enter a different Product name')
                else:
                    break
            print(f"Quantity: {open_list[update_option]['quantity']}")
            while True:
                try:
                    quantity = int(input("Enter Quantity: "))
                except ValueError:
                    print("Please enter number values")
                    continue
                break
            print(f"Price: {open_list[update_option]['price']}")
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
