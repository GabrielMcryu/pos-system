from customer_operations.add_customer import add_customer
from customer_operations.delete_customer import delete_customer
from customer_operations.update_customer import update_customer

def customer_queries():
    print("""
What would you like to do?
1) Add customer details
2) Delete customer details
3) Update customer details
4) Go back
    """)


def customer_main():
    customer_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            add_customer()
        elif choice == "2":
            delete_customer()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
        customer_main()
