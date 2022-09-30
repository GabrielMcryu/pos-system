from search_operations.search_customers import *
from search_operations.search_products import *


# Displays Search Customer choices in menu
def search_customer():
    print("""
Select Customer Search Option
1) List one Customer
2) List all Customers    
3) List Customer Purchase History
    """)


# Displays Search Products choices in menu
def search_product():
    print("""
Select Product Search Option    
1) List one Product
2) List all Products
    """)


# Displays Search choices in menu
def search_queries():
    print("""
What would you like to do?
1) List Customers
2) List Products
3) Go Back
    """)


# Search Menu query
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
                elif customer_choice == "3":
                    view_customer_purchase_history()
                    break
                else:
                    print("You have entered a wrong choice. Please input choices between (1-2)")
            break
        elif choice == "2":
            search_product()
            product_choice = input("> ").lower()
            while True:
                if product_choice == "1":
                    search_one_product()
                    break
                elif product_choice == "2":
                    search_all_products()
                    break
                else:
                    print("You have entered a wrong choice. Please input choices between (1-2)")
            break
        elif choice == "3":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-3)")
        search_main()
