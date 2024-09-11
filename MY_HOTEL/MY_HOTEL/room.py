from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

conn = sqlite3.connect('hotel_management.db')
cur = conn.cursor()

class Room_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1295x550+230+220")

        # Variables
        self.room_number_var = StringVar()
        self.room_type_var = StringVar()
        self.price_var = StringVar()
        self.availability_var = StringVar()

        # Title Label
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1000, height=50)

        # Frame to hold room information
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=50, width=1000, height=300)

        # Labels and Entry fields for room details
        lbl_room_number = Label(main_frame, text="Room Number", font=("times new roman", 12, "bold"))
        lbl_room_number.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        txt_room_number = Entry(main_frame, textvariable=self.room_number_var, font=("times new roman", 12, "bold"))
        txt_room_number.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        lbl_room_type = Label(main_frame, text="Room Type", font=("times new roman", 12, "bold"))
        lbl_room_type.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        txt_room_type = Entry(main_frame, textvariable=self.room_type_var, font=("times new roman", 12, "bold"))
        txt_room_type.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        lbl_price = Label(main_frame, text="Price", font=("times new roman", 12, "bold"))
        lbl_price.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        txt_price = Entry(main_frame, textvariable=self.price_var, font=("times new roman", 12, "bold"))
        txt_price.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        lbl_availability = Label(main_frame, text="Availability (1/0)", font=("times new roman", 12, "bold"))
        lbl_availability.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        txt_availability = Entry(main_frame, textvariable=self.availability_var, font=("times new roman", 12, "bold"))
        txt_availability.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        btn_add = Button(main_frame, text="Add Room", command=self.add_room, font=("times new roman", 12, "bold"), bg="green", fg="white")
        btn_add.grid(row=4, column=0, padx=10, pady=5)

        btn_update = Button(main_frame, text="Update Room", command=self.update_room, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        btn_update.grid(row=4, column=1, padx=10, pady=5)

        btn_delete = Button(main_frame, text="Delete Room", command=self.delete_room, font=("times new roman", 12, "bold"), bg="red", fg="white")
        btn_delete.grid(row=4, column=2, padx=10, pady=5)

        # Frame for Treeview
        room_display_frame = Frame(self.root, bd=4, relief=RIDGE)
        room_display_frame.place(x=0, y=350, width=1000, height=250)

        # Treeview for room details
        self.room_table = ttk.Treeview(room_display_frame, columns=("room_number", "room_type", "price", "availability"))
        self.room_table.heading("room_number", text="Room Number")
        self.room_table.heading("room_type", text="Room Type")
        self.room_table.heading("price", text="Price")
        self.room_table.heading("availability", text="Availability")
        self.room_table["show"] = "headings"

        self.room_table.column("room_number", width=100)
        self.room_table.column("room_type", width=150)
        self.room_table.column("price", width=100)
        self.room_table.column("availability", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_room_details()

    def fetch_room_details(self):
        conn = sqlite3.connect('hotel_management.db')  # Replace with your database path
        cur = conn.cursor()
        cur.execute("SELECT room_number, room_type, price, availability FROM rooms")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def add_room(self):
        if self.room_number_var.get() == "" or self.room_type_var.get() == "" or self.price_var.get() == "" or self.availability_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = sqlite3.connect('hotel_management.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO rooms (room_number, room_type, price, availability) VALUES (?, ?, ?, ?)", (
                self.room_number_var.get(),
                self.room_type_var.get(),
                self.price_var.get(),
                self.availability_var.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_room_details()
            self.clear()
            messagebox.showinfo("Success", "Room Added Successfully")

    def update_room(self):
        if self.room_number_var.get() == "":
            messagebox.showerror("Error", "Please select a room to update")
        else:
            conn = sqlite3.connect('hotel_management.db')
            cur = conn.cursor()
            cur.execute("UPDATE rooms SET room_type=?, price=?, availability=? WHERE room_number=?", (
                self.room_type_var.get(),
                self.price_var.get(),
                self.availability_var.get(),
                self.room_number_var.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_room_details()
            self.clear()
            messagebox.showinfo("Success", "Room Updated Successfully")

    def delete_room(self):
        if self.room_number_var.get() == "":
            messagebox.showerror("Error", "Please select a room to delete")
        else:
            conn = sqlite3.connect('hotel_management.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM rooms WHERE room_number=?", (self.room_number_var.get(),))
            conn.commit()
            conn.close()
            self.fetch_room_details()
            self.clear()
            messagebox.showinfo("Success", "Room Deleted Successfully")

    def clear(self):
        self.room_number_var.set("")
        self.room_type_var.set("")
        self.price_var.set("")
        self.availability_var.set("")

    def get_cursor(self, event):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']
        self.room_number_var.set(row[0])
        self.room_type_var.set(row[1])
        self.price_var.set(row[2])
        self.availability_var.set(row[3])

    cur.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        room_number INTEGER PRIMARY KEY,
        room_type TEXT NOT NULL,
        price REAL NOT NULL,
        availability INTEGER NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Table created successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = Room_Window(root)
    root.mainloop()
