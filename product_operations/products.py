from product_operations.add_product import add_product
from product_operations.delete_product import delete_product

def product_queries():
    print("""
What would you like to do?
1) Add Product
2) Delete Product
3) Update Produc2t
4) Go back
    """)


def product_main():
    product_queries()
    choice = input("> ").lower()
    while True:
        if choice == "1":
            add_product()
        elif choice == "2":
            delete_product()
        elif choice == "3":
            print("Update feature to be implemented...")
        elif choice == "4":
            from main import main
            main()
        else:
            print("You have entered a wrong choice. Please input choices between (1-4)")
        product_main()
