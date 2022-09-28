import json
filename = 'storage/customers.json'


def update_customer():
    with open(filename, "r") as f:
        temp = json.load(f)
    [open_list] = temp
    while True:
        print("Choose Customer ID to update")
        update_option = input("Select ID: ")
        if update_option in open_list:
            name = input("Update Customer name: ")
            open_list[update_option]["name"] = name
            while True:
                try:
                    phone_number = int(input("Enter Phone number: "))
                except ValueError:
                    print("Please enter number values")
                    continue
                break
            open_list[update_option]["phone number"] = phone_number
            while True:
                gender_choice = input("""
Enter the gender:
1) Male
2) Female
: 
                    """)
                if gender_choice == '1':
                    open_list[update_option]["gender"] = "male"
                    break
                elif gender_choice == '2':
                    open_list[update_option]["gender"] = "female"
                    break
                else:
                    print('Invalid Choice')
            print("Customer data updated")
            break
        else:
            print("ID does not exist. Please input existing ID")
    temp = [open_list]
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
