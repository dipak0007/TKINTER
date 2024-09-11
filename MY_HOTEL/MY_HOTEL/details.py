from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Details_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Details Window")
        self.root.geometry("1295x550+230+220")

        # Title Label
        lbl_title = Label(self.root, text="DETAILS", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1000, height=50)

        # Frame to hold details information
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1000, height=550)

        # Treeview for details
        self.details_table = ttk.Treeview(main_frame, columns=("id", "name", "address", "contact", "room_number"))
        self.details_table.heading("id", text="ID")
        self.details_table.heading("name", text="Name")
        self.details_table.heading("address", text="Address")
        self.details_table.heading("contact", text="Contact")
        self.details_table.heading("room_number", text="Room Number")
        self.details_table["show"] = "headings"

        self.details_table.column("id", width=50)
        self.details_table.column("name", width=150)
        self.details_table.column("address", width=200)
        self.details_table.column("contact", width=150)
        self.details_table.column("room_number", width=100)

        self.details_table.pack(fill=BOTH, expand=1)

        # Add buttons for operations
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=500, width=1000, height=40)

        add_btn = Button(btn_frame, text="Add", command=self.add_detail, width=12, font=("times new roman", 12, "bold"), bg="black", fg="gold")
        add_btn.grid(row=0, column=0, padx=10, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.update_detail, width=12, font=("times new roman", 12, "bold"), bg="black", fg="gold")
        update_btn.grid(row=0, column=1, padx=10, pady=5)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_detail, width=12, font=("times new roman", 12, "bold"), bg="black", fg="gold")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)

        self.fetch_details()

    def fetch_details(self):
        conn = sqlite3.connect('C:/TKINTER/MY_HOTEL/hotel_management.db')
        cur = conn.cursor()

        # Fetch customer data based on the correct column names
        cur.execute("SELECT name, address, contact, room_number FROM customers")  # Adjust this to your schema
        rows = cur.fetchall()

        for row in rows:
            self.details_table.insert("", "end", values=row)

        conn.commit()
        conn.close()

    def add_detail(self):
        # Add your logic here to add a new customer or room detail
        messagebox.showinfo("Add", "Add detail functionality is not implemented yet!")

    def update_detail(self):
        # Add your logic here to update the selected detail
        messagebox.showinfo("Update", "Update detail functionality is not implemented yet!")

    def delete_detail(self):
        # Add your logic here to delete the selected detail
        selected_item = self.details_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete")
            return

        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this record?")
        if confirm:
            conn = sqlite3.connect('C:/TKINTER/MY_HOTEL/hotel_management.db')
            cur = conn.cursor()

            item = self.details_table.item(selected_item)
            record_id = item['values'][0]  # Assuming the ID is the first column

            cur.execute("DELETE FROM customers WHERE id = ?", (record_id,))
            conn.commit()
            conn.close()

            self.details_table.delete(selected_item)
            messagebox.showinfo("Deleted", "Record deleted successfully.")

    def create_customers_table():
        conn = sqlite3.connect('C:/TKINTER/MY_HOTEL/hotel_management.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL,
                        contact TEXT NOT NULL,
                        room_number INTEGER NOT NULL)''')

        conn.commit()
        conn.close()

    def create_customers_table():
        conn = sqlite3.connect('C:/TKINTER/MY_HOTEL/hotel_management.db')
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL,
                        contact TEXT NOT NULL,
                        room_number INTEGER NOT NULL)''')

        conn.commit()
        conn.close()

    create_customers_table()

    

if __name__ == "__main__":
    root = Tk()
    obj = Details_Window(root)
    root.mainloop()
