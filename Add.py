from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from tkinter import messagebox

import pymysql
from tkinter import ttk

class Add:
    def __init__(self,root):
        self.root=root
        self.root.title("Tele Phone Book")
        self.root.geometry("1550x800+0+0")

        ###### Image 1

       # img1 = Image.open( r"C:\Users\Maysha\Downloads\phonebook.jpg" )
       # img1 = img1.resize( (1300, 800), Image.ANTIALIAS )
        #self.photoimg1 = ImageTk.PhotoImage( img1 )

        #lblimg1 = Label( self.root, image=self.photoimg1, bd=0, relief=RIDGE )
        #lblimg1.place( x=0, y=0, width=1300, height=800 )

        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_groups = StringVar()
        self.var_address = StringVar()
        self.var_relationship = StringVar()
        self.var_notes = StringVar()


        ############ Title

        lb1_title = Label( self.root, text='Create New Contact', font=("arial", 30, "bold"), bg='orange', fg='aquamarine', bd=4, relief=RIDGE )
        lb1_title.place( x=380, y=200, width=450, height=50 )

        ########main fram
        main_frame = Frame( self.root, bd=4, relief=RIDGE, bg='aquamarine' )
        main_frame.place( x=380, y=300, width=450, height=400 )

        ##########name

        self.name = lbl = Label( main_frame, text="Name", font=("times in roman", 10, "bold"), fg="blue", bg="aquamarine" )
        self.name.place( x=10, y=10 )
        self.txtname = ttk.Entry( main_frame, textvariable=self.var_name,font=("times in roman", 10, "bold"))
        self.txtname.place( x=100, y=10, width=270 )

        ##########Phone

        self.phone = lbl = Label( main_frame, text="Phone", font=("times in roman", 10, "bold"), fg="blue",bg="aquamarine" )
        self.phone.place( x=10, y=40 )
        self.txtphone = ttk.Entry( main_frame,textvariable=self.var_phone, font=("times in roman", 10, "bold") )
        self.txtphone.place( x=100, y=40, width=270 )

        ##########Email

        self.email = lbl = Label( main_frame, text="Email", font=("times in roman", 10, "bold"), fg="blue",bg="aquamarine" )
        self.email.place( x=10, y=70 )
        self.txtemail = ttk.Entry( main_frame,textvariable=self.var_email, font=("times in roman", 10, "bold") )
        self.txtemail.place( x=100, y=70, width=270 )

        ##########group

        self.group = lbl = Label( main_frame, text="Groups", font=("times in roman", 10, "bold"), fg="blue", bg="aquamarine" )
        self.group.place( x=10, y=100 )
        cmb_group = ttk.Combobox( main_frame,textvariable=self.var_groups,font=("times new roman", 13), state="readonly",justify=CENTER )
        cmb_group['values'] = ("Select", "Emergency contacts", "Colleagues", "Family", "Friends")
        cmb_group.place( x=100, y=100, width=270 )
        cmb_group.current( 0 )

        ##########address

        self.address = lbl = Label( main_frame, text="Address", font=("times in roman", 10, "bold"), fg="blue",bg="aquamarine" )
        self.address.place( x=10, y=130 )
        self.txtaddress = ttk.Entry( main_frame, textvariable=self.var_address,font=("times in roman", 10, "bold") )
        self.txtaddress.place( x=100, y=130, width=270 )

        ##########relation

        self.relation = lbl = Label( main_frame, text="Relationship", font=("times in roman", 10, "bold"), fg="blue",bg="aquamarine" )
        self.relation.place( x=10, y=160 )
        cmb_group = ttk.Combobox( main_frame, textvariable=self.var_relationship,font=("times new roman", 13), state="readonly", justify=CENTER )
        cmb_group['values'] = ("Select", "Parent", "Mother", "Father", "Brother","Sister","Spouse","Child","Friend","Relative","Domestic Patner","Patner","Meneger","Assistant","Referance")
        cmb_group.place( x=100, y=160, width=270 )
        cmb_group.current( 0 )

        ##########note

        self.note = lbl = Label( main_frame, text="Notes", font=("times in roman", 10, "bold"), fg="blue",
                                     bg="aquamarine" )
        self.note.place( x=10, y=190 )
        self.txtnote= ttk.Entry( main_frame, textvariable=self.var_notes, font=("times in roman", 10, "bold") )
        self.txtnote.place( x=100, y=190, width=270 )

        ##### button
        self.btn_back = Button( main_frame,  command=self.logout,text="Back", activeforeground="blue",
                                  activebackground="white", font=("times new roman", 15, "bold"), bd=0, cursor="hand2",
                                  bg="white", fg="blue" ).place( x=170, y=320, width=100, height=40 )
        self.btn_cancel = Button( main_frame,command=self.reset, text="Cancel", activeforeground="red",activebackground="white", font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="white", fg="red" ).place( x=100, y=250, width=100,height=40 )

        self.btn_save = Button( main_frame, text="Save",command=self.add_data, activeforeground="green",activebackground="white",font=("times new roman", 15, "bold"), bd=0, cursor="hand2",
                                  bg="white", fg="green" ).place( x=270, y=250, width=100, height=40 )


    def add_data(self):
        if self.var_name .get() == "" or self.var_phone.get() == "":
            messagebox.showerror( "Error", "Data field has required", parent=self.root )

        else:
            try:
                conn1 = pymysql.connect( host="127.0.0.1", user="root", password="",database="phone_book" )
                my_cursor = conn1.cursor()
                my_cursor.execute( "insert into create_contact values (%s,%s,%s,%s,%s,%s,%s)", (self.var_name.get(), self.var_phone.get(), self.var_email.get(),self.var_groups.get(),self.var_address.get(),self.var_relationship.get(),self.var_notes.get()))

                conn1.commit()
                #self.fetch_data()
                conn1.close()
                messagebox.askyesno( "Success", "A new Person  will Added in your phone Book if you choose add option",parent=self.root )

            except Exception as es:
                messagebox.showwarning( "Warning", f"Something is wrong : {str( es )} ", parent=self.root )

    def reset(self):
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set( "" )
        self.var_address.set("")
        self.var_notes.set("")


    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    ob=Add(root)
    root.mainloop()