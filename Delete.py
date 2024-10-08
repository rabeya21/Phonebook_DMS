from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from tkinter import messagebox

import pymysql


from tkinter import ttk

class Delete:
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

       # lblimg1 = Label( self.root, image=self.photoimg1, bd=0, relief=RIDGE )
        #lblimg1.place( x=0, y=0, width=1300, height=800 )

        ############ Title

        lb1_title = Label( self.root, text='Search', font=("arial", 30, "bold"), bg='orange',
                           fg='aquamarine', bd=4, relief=RIDGE )
        lb1_title.place( x=380, y=200, width=450, height=50 )

        ########main fram
        main_frame = Frame( self.root, bd=4, relief=RIDGE, bg='aquamarine' )
        main_frame.place( x=380, y=300, width=450, height=400 )

        ######  name

        self.name = Label( main_frame, text="Name", font=("times in roman", 12, "bold"), fg="Red", bg="aquamarine" )
        self.name.place( x=7, y=10 )

        txt_name = ttk.Entry( main_frame, textvariable=self.var_name, width=18, font=("arial", 13, "bold") )
        txt_name.place( x=100, y=10, width=270 )

        ######  phone

        self.phone = Label( main_frame, text="Phone No.", font=("times in roman", 12, "bold"), fg="Red", bg="aquamarine" )
        self.phone.place( x=7, y=40 )

        txt_phone = ttk.Entry( main_frame, textvariable=self.ver_phone, width=18, font=("arial", 13, "bold") )
        txt_phone.place( x=100, y=40, width=270 )

        ############## delete button
        phn_search_btn = Button( main_frame,command=self.delete,  activeforeground="red",
                                 activebackground="aquamarine", text='Delete', width=21, height=2,
                                 font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_search_btn.place( x=270, y=70, width=70 )

        ####back button

        self.btn_back = Button( main_frame,command=self.logout,  text="Back", activeforeground="blue",
                                activebackground="aquamarine", font=("times new roman", 13, "bold"), bd=0,
                                cursor="hand2",
                                bg="aquamarine", fg="blue" ).place( x=70, y=75, width=100 )

        #### Total button

        self.btn_back = Button( main_frame, command=self.fetch_pname, text="Total", activeforeground="gray",
                                activebackground="aquamarine", font=("times new roman", 13, "bold"), bd=0,
                                cursor="hand2",
                                bg="aquamarine", fg="gray" ).place( x=160, y=100, width=100 )

        # ***************Show data Table************************
        details_table = LabelFrame( main_frame, bd=2, relief=RIDGE )
        details_table.place( x=30, y=150, width=400, height=200 )

        scroll_x = ttk.Scrollbar( details_table, orient=HORIZONTAL )
        scroll_y = ttk.Scrollbar( details_table, orient=VERTICAL )

        self.cust_ditals_table = ttk.Treeview( details_table, column=("name", "phone"), yscrollcommand=scroll_y,
                                               xscrollcommand=scroll_x )

        scroll_y.pack( side=RIGHT, fill=Y )
        scroll_y.config( command=self.cust_ditals_table.yview )

        self.cust_ditals_table.heading( "name", text="Name" )
        self.cust_ditals_table.heading( "phone", text="Contact Number" )

        self.cust_ditals_table["show"] = "headings"

        self.cust_ditals_table.column( "name", width=100 )
        self.cust_ditals_table.column( "phone", width=100 )
        self.cust_ditals_table.pack( fill=BOTH, expand=1 )
        self.cust_ditals_table.bind( "<ButtonRelease-1>", self.get_cursor )
        self.fetch_data()

    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select Name,Phone from create_contact ORDER BY Name ASC" )
        rows = my_cursor.fetchall()
        if len( rows ) != 0:
            self.cust_ditals_table.delete( *self.cust_ditals_table.get_children() )
            for i in rows:
                self.cust_ditals_table.insert( "", END, values=i )
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.cust_ditals_table.focus()
        contant = self.cust_ditals_table.item( cursor_row )
        row = contant["values"]
        self.var_name.set( row[0] )
        self.ver_phone.set(row[1])

    def delete(self):
        mDelete=messagebox.askyesno("Contact No. Delete","Do you want delete all information ?",parent=self.root)
        if mDelete>0:
            conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="phone_book" )
            my_cursor = conn.cursor()
            query= "delete from create_contact where Name=%s OR Phone=%s "
            value=(self.var_name.get(),self.ver_phone.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def fetch_pname(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="phone_book" )
        my_cursor = conn.cursor()
        query = ("select COUNT(Name) from create_contact ")
        ##value = (self.var_name.get(), self.ver_phone.get(),)
        my_cursor.execute( query )
        row = my_cursor.fetchone()

        if row == None:
            messagebox.showerror( "Error", "Name is not found or Phone Number not found", parent=self.root )
        else:
            conn.commit()
            conn.close()
            showdatafram = Frame( self.root, bg='aquamarine', bd=4, relief=RIDGE, padx=6 )
            showdatafram.place( x=830, y=200, width=170, height=50 )

            # name
            lblName = Label( showdatafram, fg="Red", bg="aquamarine", text="Total person  : ",
                             font=("arial", 12, "bold") )
            lblName.place( x=0, y=0 )

            lbl = Label( showdatafram, fg="green", bg="aquamarine", text=row, font=("arial", 12, "bold") )
            lbl.place( x=120, y=0 )
        #if self.var_name.get() == "" and self.ver_phone.get()=="":
            #messagebox.showerror( "Error", "Please Enter Name And Phone Number", parent=self.root )
#





    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    ob=Delete(root)
    root.mainloop()