import json
filename = 'storage/customers.json'


def delete_customer():
    with open(filename, "r") as f:
        temp = json.load(f)
    if not temp:
        print("No data to delete")
    else:
        [open_list] = temp
        while True:
            print("Choose Customer ID to delete")
            delete_option = input('>')
            if delete_option in open_list:
                del open_list[delete_option]
                print("Customer data deleted")
                break
            else:
                print("ID does not exist. Please input an existing ID")
        temp = [open_list]
        if temp == [{}]:
            temp = list(filter(None, temp))
            with open(filename, "w") as f:
                json.dump(temp, f, indent=4)
        else:
            with open(filename, "w") as f:
                json.dump(temp, f, indent=4)


