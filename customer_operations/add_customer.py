import json
filename = '../storage/customers.json'


def create_customer_id():
    open_temp = {}
    new_id = ""
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        new_id = "c1"
        return new_id
    else:
        [open_temp] = temp
        last_id = list(open_temp)[-1]
        id_length = len(last_id)
        id_num = int(last_id[1:id_length]) + 1
        new_id = "c" + str(id_num)
        return new_id


def add_customer():
    new_id = create_customer_id()
    customer_data = {}
    item_data = {}
    with open(filename, 'r') as f:
        temp = json.load(f)
    item_data["name"] = input("Enter name: ")
    while True:
        gender_choice = input("""
Enter the gender:
1) Male
2) Female
: 
        """)
        if gender_choice == '1':
            item_data["gender"] = "Male"
            break
        elif gender_choice == '2':
            item_data["gender"] = "female"
            break
        else:
            print('Invalid Choice')
    item_data["Purchase History"] = {}
    item_data["Total Spent"] = 0

    customer_data[new_id] = item_data
    if not temp:
        temp.append(customer_data)
    else:
        [open_list] = temp
        open_list.update(customer_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
    print("Customer details added")


add_customer()




