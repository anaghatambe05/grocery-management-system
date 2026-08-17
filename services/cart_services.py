from database import conn, cursor


class CartService:

    # ---------------- ADD TO CART ---------------- #

    def add_to_cart(self):

        pid = int(input("\nEnter Product ID : "))

        cursor.execute("SELECT * FROM grocery WHERE id=?", (pid,))
        product = cursor.fetchone()

        if product is None:
            print("\nProduct Not Found.")
            return

        print("\nProduct Details")
        print("---------------------------")
        print("Name :", product[1])
        print("Brand :", product[2])
        print("Selling Price :", product[3])
        print("Available Quantity :", product[5])

        qty = int(input("\nEnter Quantity : "))

        if qty <= 0:
            print("Invalid Quantity.")
            return

        if qty > product[5]:
            print("Not Enough Stock Available.")
            return

        total = qty * product[3]

        cursor.execute("""
        INSERT INTO cart
        (product_id,name,brand,selling_price,mrp,quantity,total)
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            qty,
            total
        ))

        conn.commit()

        print("\nProduct Added To Cart Successfully.")

    # ---------------- VIEW CART ---------------- #

    def view_cart(self):

        cursor.execute("SELECT * FROM cart")

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("\nCart is Empty.")
            return

        grand_total = 0

        print("\n----------------------------------------------------------------------------")
        print("CartID\tPID\tName\tBrand\tQty\tPrice\tTotal")
        print("----------------------------------------------------------------------------")

        for row in rows:

            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[6]}\t{row[4]}\t{row[7]}")

            grand_total += row[7]

        print("----------------------------------------------------------------------------")
        print("Grand Total : ₹", grand_total)