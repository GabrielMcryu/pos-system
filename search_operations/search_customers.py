import json
filename = "storage/customers.json"


# Lists all customers and their data
def search_all_customers():
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("No Customer added into the system")
    else:
        [open_list] = temp
        for customer_id in open_list:
            name = open_list[customer_id]["name"]
            phone_number = open_list[customer_id]["phone number"]
            gender = open_list[customer_id]["gender"]
            print(f"Customer ID: {customer_id}")
            print(f"Customer Name: {name}")
            print(f"Customer Phone number: 0{phone_number}")
            print(f"Customer Gender: {gender}")
            print("\n")


# Lists all customer names
def view_customer_names():
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("No Customer added into the system")
    else:
        [open_list] = temp
        for customer_id in open_list:
            name = open_list[customer_id]["name"]
            print(f"Customer ID: {customer_id}, Customer Name: {name}")


# Lists one customer and their data
def search_one_customer():
    view_customer_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("No Customer added into the system")
    else:
        while True:
            [open_list] = temp
            search_id = input("Enter Customer ID: ")
            if search_id in open_list:
                name = open_list[search_id]["name"]
                phone_number = open_list[search_id]["phone number"]
                gender = open_list[search_id]["gender"]
                print(f"Customer name: {name}")
                print(f"Customer Phone number: {phone_number}")
                print(f"Customer Gender: {gender}")
                break
            else:
                print("ID does not exist. Please input an existing ID")


# Lists Customer purchase history by ID
def view_customer_purchase_history():
    view_customer_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print('No customers added into the system')
    else:
        [open_list] = temp
        while True:
            search_id = input("Enter Customer ID: \n")
            if search_id in open_list:
                for shopping_id in open_list[search_id]["Purchase History"]:
                    print(f"Shopping ID: {shopping_id}")
                    for item in open_list[search_id]["Purchase History"][shopping_id]:
                        if item == "Total":
                            total = open_list[search_id]["Purchase History"][shopping_id]["Total"]
                            print(f"Total: {total} Kshs \n")
                        else:
                            product_name = open_list[search_id]["Purchase History"][shopping_id][item]["product name"]
                            product_quantity = open_list[search_id]["Purchase History"][shopping_id][item]["product quantity"]
                            product_cost = open_list[search_id]["Purchase History"][shopping_id][item]["product cost"]
                            print(f"Name: {product_name}, Cost: {product_cost}, Quantity{product_quantity}")
                break
            else:
                print("ID does not exist. Please input an existing ID")



