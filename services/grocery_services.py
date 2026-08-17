from database import conn, cursor


class GroceryService:

    # ---------------- ADD GROCERY ---------------- #

    def add_grocery(self):

        while True:

            print("\n----- Add Grocery -----")

            name = input("Enter Grocery Name : ")
            brand = input("Enter Brand : ")
            selling = float(input("Enter Selling Price : "))
            mrp = float(input("Enter MRP : "))
            qty = int(input("Enter Quantity : "))

            # cursor.execute("""
            # INSERT INTO grocery
            # (name,brand,selling_price,mrp,quantity)
            # VALUES(?,?,?,?,?)
            # """, (name, brand, selling, mrp, qty))

            # conn.commit()

            # print("\nGrocery Added Successfully")
            cursor.execute("""
             INSERT INTO grocery
             (name,brand,selling_price,mrp,quantity)
             VALUES(?,?,?,?,?)
             """, (name, brand, selling, mrp, qty))

            conn.commit()

            print("\nGrocery Added Successfully.")
            print("Product ID :", cursor.lastrowid)
                              

            ch = input("\nDo you want to add more? (y/n) : ")

            if ch.lower() != "y":
                break

    # ---------------- VIEW ALL ---------------- #

    def view_all(self):

        cursor.execute("SELECT * FROM grocery")

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("\nNo Grocery Available.")
            return

        print("\n-------------------------------------------------------------")
        print("ID\tName\tBrand\tSelling\tMRP\tQuantity")
        print("-------------------------------------------------------------")

        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")

    # ---------------- SEARCH ---------------- #

    def search(self):

        pid = int(input("\nEnter Product ID : "))

        cursor.execute("SELECT * FROM grocery WHERE id=?", (pid,))

        row = cursor.fetchone()

        if row:

            print("\nProduct Found")
            print("---------------------------")
            print("ID :", row[0])
            print("Name :", row[1])
            print("Brand :", row[2])
            print("Selling Price :", row[3])
            print("MRP :", row[4])
            print("Quantity :", row[5])

        else:
            print("\nProduct Not Found.")

    # ---------------- UPDATE ---------------- #

    def update(self):

        pid = int(input("\nEnter Product ID : "))

        cursor.execute("SELECT * FROM grocery WHERE id=?", (pid,))

        row = cursor.fetchone()

        if row is None:
            print("Product Not Found.")
            return

        while True:

            print("""
=========== UPDATE MENU ===========

1. Update Name
2. Update Brand
3. Update Selling Price
4. Update MRP
5. Update Quantity
6. Exit

===================================
""")

            choice = int(input("Enter Choice : "))

            if choice == 1:

                name = input("Enter New Name : ")

                cursor.execute(
                    "UPDATE grocery SET name=? WHERE id=?",
                    (name, pid)
                )

                conn.commit()

                print("Name Updated Successfully.")

            elif choice == 2:

                brand = input("Enter New Brand : ")

                cursor.execute(
                    "UPDATE grocery SET brand=? WHERE id=?",
                    (brand, pid)
                )

                conn.commit()

                print("Brand Updated Successfully.")

            elif choice == 3:

                selling = float(input("Enter Selling Price : "))

                cursor.execute(
                    "UPDATE grocery SET selling_price=? WHERE id=?",
                    (selling, pid)
                )

                conn.commit()

                print("Selling Price Updated Successfully.")

            elif choice == 4:

                mrp = float(input("Enter New MRP : "))

                cursor.execute(
                    "UPDATE grocery SET mrp=? WHERE id=?",
                    (mrp, pid)
                )

                conn.commit()

                print("MRP Updated Successfully.")

            elif choice == 5:

                qty = int(input("Enter Quantity : "))

                cursor.execute(
                    "UPDATE grocery SET quantity=? WHERE id=?",
                    (qty, pid)
                )

                conn.commit()

                print("Quantity Updated Successfully.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")

    # ---------------- DELETE ---------------- #

    def delete(self):

        while True:

            print("""
========== DELETE MENU ==========

1. Delete All Grocery
2. Delete One Grocery
3. Back

=================================
""")

            choice = int(input("Enter Choice : "))

            if choice == 1:

                confirm = input("Are you sure? (y/n): ")

                if confirm.lower() == "y":

                    cursor.execute("DELETE FROM grocery")

                    conn.commit()

                    print("All Grocery Deleted Successfully.")

            elif choice == 2:

                pid = int(input("Enter Product ID : "))

                cursor.execute(
                    "SELECT * FROM grocery WHERE id=?",
                    (pid,)
                )

                row = cursor.fetchone()

                if row:

                    cursor.execute(
                        "DELETE FROM grocery WHERE id=?",
                        (pid,)
                    )

                    conn.commit()

                    print("Product Deleted Successfully.")

                else:
                    print("Product Not Found.")

            elif choice == 3:
                break

            else:
                print("Invalid Choice.")