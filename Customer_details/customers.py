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
            print("Add Feature to be implemented...")
            customer_main()
        elif choice == "2":
            print("Delete Feature to be implemented...")
            customer_main()
        elif choice == "3":
            print("Update feature to be implemented...")
            customer_main()
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
            customer_main()


