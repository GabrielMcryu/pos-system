import json
filename = "storage/customers.json"


def search_all_customers():
    with open(filename, "r") as f:
        temp = json.load(f)
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


def view_customer_names():
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    for customer_id in open_list:
        name = open_list[customer_id]["name"]
        print(f"Customer ID: {customer_id}, Customer Name: {name}")


def search_one_customer():
    view_customer_names()
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    while True:
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





