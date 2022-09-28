from search_operations.search_products import view_product_names
import json
filename = "storage/products.json"


def create_product_id():
    open_temp = {}
    new_id = ""
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        new_id = "p1"
        return new_id
    else:
        [open_temp] = temp
        last_id = list(open_temp)[-1]
        id_length = len(last_id)
        id_num = int(last_id[1:id_length]) + 1
        new_id = "p" + str(id_num)
        return new_id


def add_product():
    view_product_names()
    new_id = create_product_id()
    product_data = {}
    item_data = {}
    with open(filename, "r") as f:
        temp = json.load(f)
    item_data["name"] = input("Enter Product name: ")
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Please enter number values")
            continue
        item_data["quantity"] = quantity
        break
    while True:
        try:
            price = int(input("Enter Price: "))
        except ValueError:
            print("Please enter number values")
            continue
        item_data["price"] = price
        break
    product_data[new_id] = item_data
    if not temp:
        temp.append(product_data)
    else:
        [open_list] = temp
        open_list.update(product_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
    print("Product details added")
