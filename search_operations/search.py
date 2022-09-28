from search_operations.search_customers import *


def search_customer():
    print("""
Select Customer Search Option
1) List one Customer
2) List all Customers    
    """)


def search_queries():
    print("""
What would you like to do?
1) List Customers
2) List all Products
3) List Customer information
4) Go back
    """)


def search_main():
    search_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            search_customer()
            customer_choice = input("> ").lower()
            while True:
                if customer_choice == "1":
                    search_one_customer()
                    break
                elif customer_choice == "2":
                    search_all_customers()
                    break
                else:
                    print("You have entered a wrong choice. Please input choices between (1-2)")
            break
        elif choice == "2":
            print("Search Feature to be implemented...")
        elif choice == "3":
            print("Search feature to be implemented...")
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
        search_main()
