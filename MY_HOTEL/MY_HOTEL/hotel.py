from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from customer import Customer_Window

from room import Room_Window
from details import Details_Window
import os
import sqlite3
print(os.path.exists("C:/TKINTER/MY_HOTEL/images/logo.webp"))

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #==================1st Image (Banner)====================
        img1 = Image.open("C:/TKINTER/MY_HOTEL/images/hotel_home.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)  # Resize first image
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        #--------------------title----------------------------------

        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #---------------------menu--------------------------------
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #------------------------btn Frame-----------------------------
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="LOGOUT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        

        #-------RIGHT SIDE IMAGE -----------------------------------
        img3 = Image.open("C:/TKINTER/MY_HOTEL/images/hotel_home.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)  # Resize first image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)

    def show_details(self):
        """Function to display all customer details"""
        self.details_window = Toplevel(self.root)
        self.details_window.title("Customer Details")
        self.details_window.geometry("1000x500+200+100")

        conn = sqlite3.connect('hotel.db')  # Adjust your DB path
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")  # Assuming 'customers' is your table
        rows = cur.fetchall()

    def room_details(self):
      
      self.new_window = Toplevel(self.root)
      self.app = Room_Window(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)  # Open a new window
        self.app = Details_Window(self.new_window) 

        
        
          






if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
