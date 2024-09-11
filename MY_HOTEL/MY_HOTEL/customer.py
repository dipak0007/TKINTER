import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Customer_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # Connect to the database and create the table if not exists
        self.connect_db()
        self.var_ref = StringVar()
        self.var_name = StringVar()
        self.var_fname = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # ----------------title-----------------------
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # -------------------LABEL FRAME-----------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2,)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # --------------labels and entries---------------
        label_cust = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        label_cust.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"))
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_name, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Father Name
        lblfname = Label(labelframeleft, text="Father Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblfname.grid(row=2, column=0, sticky=W)
        txtfname = ttk.Entry(labelframeleft, textvariable=self.var_fname, width=29, font=("arial", 13, "bold"))
        txtfname.grid(row=2, column=1)

        # Gender combobox
        lbl_gender = Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)

        # PostCode
        lblpostcode = Label(labelframeleft, text="PostCode", font=("arial", 12, "bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky=W)
        txtpostcode = ttk.Entry(labelframeleft, textvariable=self.var_postcode, width=29, font=("arial", 13, "bold"))
        txtpostcode.grid(row=4, column=1)

        # Mobile
        lblmobile = Label(labelframeleft, text="Mobile", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtmobile.grid(row=5, column=1)

        # Email
        lblemail = Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)
        txtemail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtemail.grid(row=6, column=1)

        # Address
        lbladdress = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbladdress.grid(row=7, column=0, sticky=W)
        txtaddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txtaddress.grid(row=7, column=1)

        # -------Buttons-------------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.add_data)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="Update", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.update_data)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelate = Button(btn_frame, text="Delete", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.delete_data)
        btndelate.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.reset_data)
        btnreset.grid(row=0, column=3, padx=1)

        # Database table and search area
        self.setup_table()

    def connect_db(self):
        """Connect to SQLite3 database and create table if not exists"""
        self.conn = sqlite3.connect("hotel_management.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                ref INTEGER PRIMARY KEY,
                name TEXT,
                father TEXT,
                gender TEXT,
                postcode TEXT,
                mobile TEXT,
                email TEXT,
                address TEXT
            )
        """)
        self.conn.commit()

    def add_data(self):
        """Add customer data to the database"""
        if self.var_ref.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            self.cursor.execute("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?)", (
                self.var_ref.get(),
                self.var_name.get(),
                self.var_fname.get(),
                self.var_gender.get(),
                self.var_postcode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_address.get()
            ))
            self.conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Customer details added successfully")

    def fetch_data(self):
        """Fetch all data from the database to the Treeview table"""
        self.cursor.execute("SELECT * FROM customers")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.Cust_details.delete(*self.Cust_details.get_children())
            for row in rows:
                self.Cust_details.insert('', END, values=row)
            self.conn.commit()

    def update_data(self):
        """Update customer data"""
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Customer Reference is required")
            return

        self.cursor.execute("""
            UPDATE customers SET
                name = ?,
                father = ?,
                gender = ?,
                postcode = ?,
                mobile = ?,
                email = ?,
                address = ?
            WHERE ref = ?
        """, (
            self.var_name.get(),
            self.var_fname.get(),
            self.var_gender.get(),
            self.var_postcode.get(),
            self.var_mobile.get(),
            self.var_email.get(),
            self.var_address.get(),
            self.var_ref.get()
        ))
        self.conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Customer details updated successfully")

    def delete_data(self):
        """Delete customer data"""
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Customer Reference is required")
            return

        self.cursor.execute("DELETE FROM customers WHERE ref = ?", (self.var_ref.get(),))
        self.conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Customer details deleted successfully")

    def reset_data(self):
        """Reset all fields"""
        self.var_ref.set("")
        self.var_name.set("")
        self.var_fname.set("")
        self.var_gender.set("")
        self.var_postcode.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")

    def search_data(self):
        """Search data based on user input"""
        search_by = self.combo_search.get()
        search_term = self.searchtxt.get()
        if search_term == "":
            messagebox.showerror("Error", "Please enter a search term")
            return
        query = "SELECT * FROM customers WHERE {} LIKE ?".format("mobile" if search_by == "Mobile" else "ref")
        self.cursor.execute(query, ('%' + search_term + '%',))
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.Cust_details.delete(*self.Cust_details.get_children())
            for row in rows:
                self.Cust_details.insert('', END, values=row)
        else:
            self.Cust_details.delete(*self.Cust_details.get_children())
            messagebox.showinfo("Info", "No records found")

    def setup_table(self):
        """Set up Treeview table for displaying customer data"""
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search System", font=("times new roman", 12, "bold"), padx=2,)
        table_frame.place(x=435, y=50, width=860, height=490)

        lblsearch = Label(table_frame, text="Search by:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblsearch.grid(row=0, column=0, sticky=W, padx=2)

        combo_search = ttk.Combobox(table_frame, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        searchtxt = ttk.Entry(table_frame, width=24, font=("arial", 13, "bold"))
        searchtxt.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text="Search", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=lambda: self.search_data(combo_search.get(), searchtxt.get()))
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text="Show All", font=("arial", 12, "bold"), bg="black", fg="gold", width=9, command=self.fetch_data)
        btnShowAll.grid(row=0, column=4, padx=1)

        table_details = Frame(table_frame, bd=2, relief=RIDGE)
        table_details.place(x=0, y=50, width=860, height=350)

        scrol_x = ttk.Scrollbar(table_details, orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(table_details, orient=VERTICAL)

        self.Cust_details = ttk.Treeview(table_details, columns=("ref", "name", "father", "gender", "postcode", "mobile", "email", "address"), xscrollcommand=scrol_x.set, yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Cust_details.xview)
        scrol_y.config(command=self.Cust_details.yview)

        self.Cust_details.heading("ref", text="Refer No")
        self.Cust_details.heading("name", text="Name")
        self.Cust_details.heading("father", text="Father Name")
        self.Cust_details.heading("gender", text="Gender")
        self.Cust_details.heading("postcode", text="PostCode")
        self.Cust_details.heading("mobile", text="Mobile")
        self.Cust_details.heading("email", text="Email")
        self.Cust_details.heading("address", text="Address")

        self.Cust_details["show"] = "headings"
        self.Cust_details.column("ref", width=100)
        self.Cust_details.column("name", width=100)
        self.Cust_details.column("father", width=100)
        self.Cust_details.column("gender", width=100)
        self.Cust_details.column("postcode", width=100)
        self.Cust_details.column("mobile", width=100)
        self.Cust_details.column("email", width=150)
        self.Cust_details.column("address", width=200)

        self.Cust_details.pack(fill=BOTH, expand=1)
        self.Cust_details.bind("<ButtonRelease-1>", self.on_select)
        self.fetch_data()

    def on_select(self, event):
        """Populate the fields with the selected row data"""
        selected_row = self.Cust_details.selection()
        if selected_row:
            row = self.Cust_details.item(selected_row)['values']
            self.var_ref.set(row[0])
            self.var_name.set(row[1])
            self.var_fname.set(row[2])
            self.var_gender.set(row[3])
            self.var_postcode.set(row[4])
            self.var_mobile.set(row[5])
            self.var_email.set(row[6])
            self.var_address.set(row[7])

    # def search_data(self, search_by, search_value):
    #     """Search customer data based on selected criteria"""
    #     if search_by == "Mobile":
    #         self.cursor.execute("SELECT * FROM customers WHERE mobile LIKE ?", ('%' + search_value + '%',))
    #     elif search_by == "Ref":
    #         self.cursor.execute("SELECT * FROM customers WHERE ref LIKE ?", ('%' + search_value + '%',))
    #     rows = self.cursor.fetchall()
    #     if len(rows) != 0:
    #         self.Cust_details.delete(*self.Cust_details.get_children())
    #         for row in rows:
    #             self.Cust_details.insert('', END, values=row)
    #     else:
    #         messagebox.showinfo("Info", "No record found")

if __name__ == "__main__":
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()
