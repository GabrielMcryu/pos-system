from search_operations.search_customers import view_customer_names
import json
filename = 'storage/customers.json'


# Updates Customer Details by ID
def update_customer():
    view_customer_names()
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
                phone_number = 0
                phone_string = input("Enter Phone number")
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
            open_list[update_option]["phone number"] = number_string

            while True:
                email = input("Enter Email Address: ")
                find_at = email.find('@')
                email_length = len(email)
                after_at = email[find_at + 1:email_length]
                if '@' not in email[0] and '.' not in email[-1]:
                    if '@' in email:
                        if '.' not in after_at[0]:
                            if '.' in after_at:
                                open_list[update_option]['email'] = email
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
Enter the gender:
1) Male
2) Female
> """)
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
