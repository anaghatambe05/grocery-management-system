from database import conn, cursor


class BillService:

    # ---------------- GENERATE BILL ---------------- #

    def generate_bill(self):

        cursor.execute("SELECT * FROM cart")
        cart_items = cursor.fetchall()

        if len(cart_items) == 0:
            print("\nCart is Empty.")
            return

        print("\n")
        print("=" * 70)
        print("\t\tGROCERY BILL")
        print("=" * 70)

        grand_total = 0

        print("{:<5}{:<15}{:<15}{:<10}{:<10}{:<10}".format(
            "ID", "Name", "Brand", "Qty", "Price", "Total"
        ))

        print("-" * 70)

        for item in cart_items:

            print("{:<5}{:<15}{:<15}{:<10}{:<10}{:<10}".format(
                item[1],        # Product ID
                item[2],        # Name
                item[3],        # Brand
                item[6],        # Quantity
                item[4],        # Selling Price
                item[7]         # Total
            ))

            grand_total += item[7]

            # Update Stock
            cursor.execute("""
            UPDATE grocery
            SET quantity = quantity - ?
            WHERE id = ?
            """, (item[6], item[1]))

        print("-" * 70)

        print(f"Grand Total : ₹ {grand_total}")

        print("=" * 70)
        print("      THANK YOU! VISIT AGAIN 😊")
        print("=" * 70)

        # Empty Cart
        cursor.execute("DELETE FROM cart")

        conn.commit()

        print("\nBill Generated Successfully.")