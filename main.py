# import database

# from services.grocery_service import GroceryService
# from services.cart_service import CartService
# from services.bill_service import BillService

from services.grocery_services import GroceryService
from services.cart_services import CartService
from services.bill_services import BillService

grocery = GroceryService()
cart = CartService()
bill = BillService()


def menu():

    while True:

        print("""
=================================================
          GROCERY MANAGEMENT SYSTEM
=================================================

1. Add Grocery

2. View All Grocery

3. Search Grocery

4. Update Grocery

5. Delete Grocery

6. Add To Cart

7. View Cart

8. Generate Bill

9. Exit

=================================================
""")

        try:
            choice = int(input("Enter Your Choice : "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:

            grocery.add_grocery()

        elif choice == 2:

            grocery.view_all()

        elif choice == 3:

            grocery.search()

        elif choice == 4:

            grocery.update()

        elif choice == 5:

            grocery.delete()

        elif choice == 6:

            cart.add_to_cart()

        elif choice == 7:

            cart.view_cart()

        elif choice == 8:

            bill.generate_bill()

        elif choice == 9:

            print("\nThank You For Using Grocery Management System.")
            break

        else:

            print("Invalid Choice.")


menu()