from search_operations.search_customers import view_customer_names
import json
filename = 'storage/customers.json'


# Creates the Customer ID
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


# Adds New Customer to json file
def add_customer():
    view_customer_names()
    new_id = create_customer_id()
    customer_data = {}
    item_data = {}
    with open(filename, 'r') as f:
        temp = json.load(f)
    item_data["name"] = input("Enter Customer Name: ")
    while True:
        phone_number = 0
        phone_string = input("Enter Phone number: ")
        if 9 < len(phone_string) < 11:
            if phone_string[0] == '0':
                try:
                    phone_number = int(phone_string)
                except ValueError:
                    print("Please enter number values")
                    continue
                break
            else:
                print('Invalid phone number. Enter Correct format')
        else:
            print('Invalid phone number. Enter Correct format')
    number_string = f"0{phone_number}"
    item_data["phone number"] = number_string

    while True:
        email = input("Enter Email Address: ")
        find_at = email.find('@')
        email_length = len(email)
        after_at = email[find_at+1:email_length]
        if '@' not in email[0] and '.' not in email[-1]:
            if '@' in email:
                if '.' not in after_at[0]:
                    if '.' in after_at:
                        item_data['email'] = email
                        break
                    else:
                        print('Please enter a valid email address')
                else:
                    print('Please enter a valid email address')
            else:
                print('Please enter a valid email address')
        else:
            print('Please enter a valid email address')

    while True:
        gender_choice = input("""
Enter Customer gender:
1) Male
2) Female
> """)
        if gender_choice == '1':
            item_data["gender"] = "male"
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



