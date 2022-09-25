from Customer_details.customers import customer_main
from Product_details.products import product_main
from Search_details.search import search_main


def general_queries():
    print("""
Welcome to the point of sale system!
Enter the options listed to look at a specific query: 
1) Customer Details
2) Product Details
3) Search Details
Q) Quit
    """)


def main():
    general_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            customer_main()
        elif choice == "2":
            product_main()
        elif choice == "3":
            search_main()
        elif choice == "q":
            print("Program exited")
            quit()
        else:
            print("You entered a wrong choice. Please input choices between (1-3)")


main()
