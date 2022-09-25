def product_queries():
    print("""
What would you like to do?
1) Add Product
2) Delete Product
3) Update Product
4) Go back
    """)


def product_main():
    product_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            print("Add Feature to be implemented...")
            product_main()
        elif choice == "2":
            print("Delete Feature to be implemented...")
            product_main()
        elif choice == "3":
            print("Update feature to be implemented...")
            product_main()
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
            product_main()
