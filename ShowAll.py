from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
import pymysql
import random
from tkinter import messagebox

import fetchDBconn
from Tools.scripts.make_ctype import values

class ShowAll:
    def __init__(self,root):
        self.root=root
        self.root.title("Tele Phone Book")
        self.root.geometry("1550x800+0+0")

        self.var_name = StringVar()
        self.ver_phone = StringVar()

        ###### Image 1

        #img1 = Image.open( r"C:\Users\Maysha\Downloads\phonebook.jpg" )
        #img1 = img1.resize( (1300, 800), Image.ANTIALIAS )
        #self.photoimg1 = ImageTk.PhotoImage( img1 )

        #lblimg1 = Label( self.root, image=self.photoimg1, bd=0, relief=RIDGE )
        #lblimg1.place( x=0, y=0, width=1300, height=800 )

        ############ Title

        lb1_title = Label( self.root, text='Show All Information', font=("arial", 30, "bold"), bg='orange',
                           fg='green', bd=4, relief=RIDGE )
        lb1_title.place( x=380, y=200, width=450, height=50 )

        ########main fram
        main_frame = Frame( self.root, bd=4, relief=RIDGE, bg='aquamarine' )
        main_frame.place( x=380, y=300, width=450, height=400 )

        ######  name

        self.name = Label( main_frame, text="Name", font=("times in roman", 12, "bold"), fg="Red", bg="aquamarine" )
        self.name.place( x=7, y=10 )

        txt_name = ttk.Entry( main_frame,textvariable=self.var_name,  width=18, font=("arial", 13, "bold") )
        txt_name.place( x=100, y=10, width=270 )

        ######  phone

        self.phone = Label( main_frame, text="Phone No.", font=("times in roman", 12, "bold"), fg="Red",
                            bg="aquamarine" )
        self.phone.place( x=7, y=40 )

        txt_phone = ttk.Entry( main_frame, textvariable=self.ver_phone, width=18, font=("arial", 13, "bold") )
        txt_phone.place( x=100, y=40, width=270 )

        ############## Click button
        phn_search_btn = Button( main_frame, command=self.fetch_pname, activeforeground="red",
                                 activebackground="aquamarine", text='Click', width=21, height=2,
                                 font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_search_btn.place( x=270, y=70, width=70 )

        ####back button

        self.btn_back = Button( main_frame, command=self.logout, text="Back", activeforeground="blue",
                                activebackground="aquamarine", font=("times new roman", 13, "bold"), bd=0,
                                cursor="hand2",
                                bg="aquamarine", fg="blue" ).place( x=70, y=75, width=100 )


    def fetch_pname(self):
        if self.var_name.get() == "" and self.ver_phone.get()=="":
            messagebox.showerror( "Error", "Please Enter Name And Phone Number", parent=self.root )

        else:
            conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
            my_cursor = conn.cursor()
            query = ("select Name from create_contact where Name=%s and Phone=%s")
            value = (self.var_name.get(),self.ver_phone.get(),)
            my_cursor.execute( query, value )
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror( "Error", "Name is not found or Phone Number not found", parent=self.root )
            else:
                conn.commit()
                conn.close()
                showdatafram = Frame( self.root,bg='aquamarine', bd=4, relief=RIDGE,padx=6 )
                showdatafram.place( x=380, y=450, width=450, height=250 )

                # name
                lblName = Label( showdatafram, fg="Red", bg="aquamarine",text="Name : ", font=("arial", 12, "bold") )
                lblName.place( x=0, y=0 )

                lbl = Label( showdatafram,fg="green", bg="aquamarine", text=row, font=("arial", 12, "bold") )
                lbl.place( x=120, y=0 )

                # Phone No.
                conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book")

                my_cursor = conn.cursor()
                query = ("select Phone from create_contact where Name=%s and Phone=%s")
                value = (self.var_name.get(),self.ver_phone.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, fg="Red", bg="aquamarine",text="Phone number : ", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=30 )

                lbl1 = Label( showdatafram,fg="green", bg="aquamarine", text=row, font=("arial", 12, "bold") )
                lbl1.place( x=200, y=30 )

                # email.
                conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
                my_cursor = conn.cursor()
                query = ("select Email from create_contact where Name=%s and Phone=%s")
                value = (self.var_name.get(),self.ver_phone.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram,fg="Red", bg="aquamarine", text="Email : ", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=60 )

                lbl2 = Label( showdatafram,fg="green", bg="aquamarine", text=row, font=("arial", 12, "bold") )
                lbl2.place( x=130, y=60 )

                # group
                conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
                my_cursor = conn.cursor()
                query = ("select Groups from create_contact where Name=%s and Phone=%s")
                value = (self.var_name.get(),self.ver_phone.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblWeek = Label( showdatafram,fg="Red", bg="aquamarine", text="Group : ", font=("arial", 12, "bold") )
                lblWeek.place( x=0, y=90 )

                lbl3 = Label( showdatafram,fg="green", bg="aquamarine", text=row, font=("arial", 12, "bold") )
                lbl3.place( x=180, y=90 )

                # Address
                conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
                my_cursor = conn.cursor()
                query = ("select Address from create_contact where Name=%s and Phone=%s")
                value = (self.var_name.get(),self.ver_phone.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblTs = Label( showdatafram,fg="Red", bg="aquamarine", text="Address : ", font=("arial", 12, "bold") )
                lblTs.place( x=0, y=120 )

                lbl4 = Label( showdatafram, fg="green", bg="aquamarine",text=row, font=("arial", 12, "bold") )
                lbl4.place( x=60, y=120 )

                # relation
                conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
                my_cursor = conn.cursor()
                query = ("select Relationship from create_contact where Name=%s and Phone=%s")
                value = (self.var_name.get(),self.ver_phone.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, fg="Red", bg="aquamarine",text="Relationship :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=150 )

                lbl2 = Label( showdatafram, fg="green", bg="aquamarine",text=row, font=("arial", 12, "bold") )
                lbl2.place( x=130, y=150 )

    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    ob=ShowAll(root)
    root.mainloop()