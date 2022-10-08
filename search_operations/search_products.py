import json
filename = "storage/products.json"


# List all Products and their data
def search_all_products():
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("Products not added into the system")
    else:
        [open_list] = temp
        for product_id in open_list:
            name = open_list[product_id]["name"]
            quantity = open_list[product_id]["quantity"]
            price = open_list[product_id]["price"]
            print(f"Product ID: {product_id}")
            print(f"Product Name: {name}")
            print(f"Product Quantity: {quantity}")
            print(f"Product Price: {price}")
            print('\n')


# Lists all products and data in one line
def view_product_names():
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("Products not added into the system")
    else:
        [open_list] = temp
        for product_id in open_list:
            name = open_list[product_id]["name"]
            quantity = open_list[product_id]["quantity"]
            price = open_list[product_id]["price"]
            print(f"ID: {product_id}, Name: {name}, Quantity: {quantity}, Price: {price} Kshs")


# List one product and its data
def search_one_product():
    view_product_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("Products not added into the system")
    else:
        [open_list] = temp
        while True:
            search_id = input("Enter Product ID: ")
            if search_id in open_list:
                name = open_list[search_id]["name"]
                quantity = open_list[search_id]["quantity"]
                price = open_list[search_id]["price"]
                print(f"Product Name: {name}")
                print(f"Product Quantity: {quantity}")
                print(f"Product Price: {price}")
                break
            else:
                print("ID does not exist. Please input an existing ID")