import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector

class BillingApp:
    def __init__(self, root, db_config):
        self.root = root
        self.root.title("Simple Billing App (MySQL)")
        self.db_config = db_config

        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS bills (
                    bill_no INT PRIMARY KEY,
                    customer_name VARCHAR(255),
                    phone VARCHAR(20),
                    items TEXT,
                    total_price DECIMAL(10, 2)
                )
            """)
            self.conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect to MySQL: {err}")
            root.destroy()  # Close the app if database connection fails
            return

        # Variables
        self.customer_name = tk.StringVar()
        self.phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.items = {}  # Dictionary to store items and quantities
        self.total_price = tk.StringVar()

        # GUI elements
        tk.Label(root, text="Customer Name:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.customer_name).grid(row=0, column=1)

        tk.Label(root, text="Phone:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.phone).grid(row=1, column=1)

        tk.Label(root, text="Bill Number:").grid(row=2, column=0)
        tk.Label(root, textvariable=self.bill_no).grid(row=2, column=1)

        # Example item input (replace with your item selection)
        tk.Label(root, text="Item 1 Qty:").grid(row=3, column=0)
        self.item1_qty = tk.IntVar()
        tk.Entry(root, textvariable=self.item1_qty).grid(row=3, column=1)

        tk.Label(root, text="Item 2 Qty:").grid(row=4, column=0)
        self.item2_qty = tk.IntVar()
        tk.Entry(root, textvariable=self.item2_qty).grid(row=4, column=1)

        tk.Button(root, text="Generate Bill", command=self.generate_bill).grid(row=5, columnspan=2)
        tk.Label(root, text="Total Price:").grid(row=6, column=0)
        tk.Label(root, textvariable=self.total_price).grid(row=6, column=1)

    def generate_bill(self):
        customer_name = self.customer_name.get()
        phone = self.phone.get()
        bill_no = self.bill_no.get()

        # Example item prices (replace with your actual prices)
        item1_price = 10.0
        item2_price = 20.0

        qty1 = self.item1_qty.get()
        qty2 = self.item2_qty.get()

        total = (qty1 * item1_price) + (qty2 * item2_price)

        items_str = f"Item 1: {qty1}, Item 2: {qty2}"

        try:
            self.cursor.execute("INSERT INTO bills (bill_no, customer_name, phone, items, total_price) VALUES (%s, %s, %s, %s, %s)",
                                (bill_no, customer_name, phone, items_str, total))
            self.conn.commit()
            self.total_price.set(str(total))
            messagebox.showinfo("Bill Generated", f"Bill #{bill_no} generated successfully!")
            self.bill_no.set(str(random.randint(1000, 9999))) #Generate new bill number
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to insert data: {err}")

    def __del__(self): #close connection when object is destroyed.
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

# MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1705",
    "database": "employees",
}

root = tk.Tk()
app = BillingApp(root, db_config)
root.mainloop()
                
