def search_queries():
    print("""
What would you like to do?
1) List all Customers
2) List all Products
3) List Customer information
4) Go back
    """)


def search_main():
    search_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            print("Search Feature to be implemented...")
            search_main()
        elif choice == "2":
            print("Search Feature to be implemented...")
            search_main()
        elif choice == "3":
            print("Search feature to be implemented...")
            search_main()
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
            search_main()