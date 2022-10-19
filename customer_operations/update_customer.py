from search_operations.search_customers import view_customer_names
import json
import re

filename = 'storage/customers.json'


def valid_email(user_input):
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_input))


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
            print(f"Name: {open_list[update_option]['name']}")
            name = input("Update Customer name: ")
            open_list[update_option]["name"] = name
            print(f"Phone number: {open_list[update_option]['phone number']}")
            while True:
                phone_number = 0
                phone_string = input("Enter Phone number")
                if 9 < len(phone_string) < 11:
                    if '-' not in phone_string and '+' not in phone_string:
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
                        print("Please enter number values")
                else:
                    print('Invalid phone number. Enter Correct format')
            number_string = f"0{phone_number}"
            open_list[update_option]["phone number"] = number_string

            print(f'Email: {open_list[update_option]["email"]}')
            while True:
                email = input("Enter Email Address: ")
                email_length = len(email)
                dot_position = email.find('.')
                h_position = email.find('-')
                at_position = email.find('@')
                after_at = email[at_position + 1:email_length]

                if '.' not in email[-1] and '-' not in email[-1]:
                    if ('.' not in email[dot_position + 1] and '@' not in email[dot_position + 1] and
                            '-' not in email[dot_position + 1] and '.' not in email[h_position + 1] and
                            '@' not in email[h_position + 1] and '-' not in email[h_position + 1]):
                        if '.' not in after_at[0] and '-' not in after_at[0]:
                            email_bool = valid_email(email)
                            if email_bool:
                                break
                            else:
                                print('Invalid email. Please enter a valid email format')
                        else:
                            print('Invalid email. Please enter a valid email format')
                    else:
                        print('Invalid email. Please enter a valid email format')
                else:
                    print('Invalid email. Please enter a valid email format')
            open_list[update_option]['email'] = email

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

            break
        else:
            print("ID does not exist. Please input existing ID")
    temp = [open_list]
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
    print("Customer details updated")
