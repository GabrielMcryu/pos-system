from search_operations.search_customers import view_customer_names
from search_operations.search_products import view_product_names
from purchase_operations.send_email import send_to_email
import json
customer_file = 'storage/customers.json'
product_file = 'storage/products.json'
purchase_file = 'storage/purchases.json'


# Checks if customer ID exists in json file
def check_customer_id(customer_data):
    while True:
        view_customer_names()
        customer_id = input("""
Enter Customer ID
Press 'Q' to quit
> """).lower()
        if customer_id in customer_data or customer_id == 'q':
            return customer_id
        else:
            print("ID does not exist. Please input an existing ID")

# Creates new item ID
def create_item_id(item_dict):
    if not item_dict:
        new_item_id = "item-1"
        return new_item_id
    else:
        last_id = list(item_dict)[-1]
        id_length = len(last_id)
        id_num = int(last_id[5:id_length]) + 1
        new_item_id = "item-" + str(id_num)
        return new_item_id


# Creates new Shopping ID
def create_shopping_id():
    with open(purchase_file, "r") as f:
        temp = json.load(f)
    if not temp:
        new_id = "s1"
        return new_id
    else:
        [open_temp] = temp
        last_id = list(open_temp)[-1]
        id_length = len(last_id)
        id_num = int(last_id[1:id_length]) + 1
        new_id = "s" + str(id_num)
        return new_id


# Checks if product quantity is valid
def check_product_quantity(p_id, p_data):
    while True:
        view_product_names()
        try:
            product_quantity = int(input("""
Enter Quantity:
Enter '0' to cancel
> """))
        except ValueError:
            print("Please enter number values")
            continue
        if product_quantity == p_data[p_id]["quantity"]:
            return product_quantity
        if product_quantity > p_data[p_id]["quantity"]:
            print("Value inputted is greater than what is in stock. Add a lower quantity value")
        else:
            return product_quantity


# Adds item data into cart until process is finished
def get_item_data(product_data):
    items = {}
    id_list = []
    while True:
        view_product_names()
        product_id = input("""
Enter Product ID
Press 'F' to Finish
Press 'Q' to quit shopping        
> """).lower()
        if product_id in product_data:
            if product_id in id_list:
                print("Product already exists in the cart. Please choose a different Product ID")
            else:
                if product_data[product_id]["quantity"] < 1:
                    print("Product out of stock. Please input a different Product")
                else:
                    quantity = check_product_quantity(product_id, product_data)
                    if quantity == 0:
                        continue
                    else:
                        item_id = create_item_id(items)
                        items[item_id] = {}
                        items[item_id]["product id"] = product_id
                        items[item_id]["product name"] = product_data[product_id]["name"]
                        items[item_id]["product quantity"] = quantity
                        items[item_id]["product cost"] = product_data[product_id]["price"] * quantity
                        id_list.append(product_id)

        elif product_id == "q":
            return 'q'
        elif product_id == 'f':
            return items
        else:
            print("ID does not exist. Please input an existing ID")


# Confirms whether to go through with payment
def confirm_payment(total):
    while True:
        confirm = input(f"""
Total is {total} Kshs
Confirm Payment? (y/n)
> """).lower()
        if confirm == "y" or confirm == "n":
            return confirm
        else:
            print("You have entered an invalid choice. Please input y/n")

# Adds Purchase data into Customer purchase history
def add_customer_purchase(c_id, s_id, items, total):
    shopping_data = {}
    with open(customer_file, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    shopping_data[s_id] = items
    shopping_data[s_id]["Total"] = total
    open_list[c_id]["Total Spent"] = open_list[c_id]["Total Spent"] + total
    open_list[c_id]["Purchase History"].update(shopping_data)
    temp = [open_list]
    with open(customer_file, "w") as f:
        json.dump(temp, f, indent=4)


# Creates new Purchase details and adds it into purchase json file
def purchase_main():
    from main import main
    purchase_data = {}
    purchase_list = {}
    total = 0

    with open(customer_file, "r") as f:
        customer_temp = json.load(f)
    [open_customer] = customer_temp
    with open(product_file, "r") as f:
        product_temp = json.load(f)
    [open_product] = product_temp
    with open(purchase_file, "r") as f:
        purchase_temp = json.load(f)

    customer_id = check_customer_id(open_customer)
    if customer_id == 'q':
        main()
    else:
        item_data = get_item_data(open_product)
        if item_data == 'q':
            main()
        elif not item_data:
            print("Shopping Cart is empty")
            main()
        else:
            shopping_id = create_shopping_id()
            for i in item_data.keys():
                total += item_data[i]["product cost"]
            purchase_list["customer id"] = customer_id
            purchase_list["customer name"] = open_customer[customer_id]["name"]
            purchase_list["shopping list"] = item_data

            confirmation = confirm_payment(total)
            if confirmation == "y":
                print("Payment confirmed. Thank you for shopping with us!")
                print("Receipt:")
                c_name = open_customer[customer_id]["name"]
                print(f"Customer: {c_name}")
                for item in item_data:

                    p_name = item_data[item]["product name"]
                    p_quantity = item_data[item]["product quantity"]
                    p_cost = item_data[item]["product cost"]
                    print(f"Product: {p_name}   Quantity: {p_quantity}   Cost: {p_cost} ")
                print(f"Total Cost: {total} Kshs")

                for i in item_data.keys():
                    p_id = item_data[i]["product id"]
                    open_product[p_id]["quantity"] = open_product[p_id]["quantity"] - item_data[i]["product quantity"]

                send_to_email(customer_id, shopping_id, item_data, total)

                add_customer_purchase(customer_id, shopping_id, item_data, total)

                purchase_data[shopping_id] = purchase_list
                if not purchase_temp:
                    purchase_temp.append(purchase_data)
                else:
                    [open_purchase] = purchase_temp
                    open_purchase.update(purchase_data)

                with open(purchase_file, "w") as f:
                    json.dump(purchase_temp, f, indent=4)

                product_temp = [open_product]
                with open(product_file, "w") as f:
                    json.dump(product_temp, f, indent=4)

                main()
            elif confirmation == "n":
                print("Shopping Cancelled")
                main()
