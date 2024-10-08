from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from tkinter import messagebox
from Delete import  Delete
from Update import Update
import pymysql


from tkinter import ttk

class Option:
    def __init__(self,root):
        self.root=root
        self.root.title("Tele Phone Book")
        self.root.geometry("222x110+850+450")

        ###### Image 1

        #img1 = Image.open( r"C:\Users\Maysha\Downloads\phonebook.jpg" )
        #img1 = img1.resize( (1300, 800), Image.ANTIALIAS )
        #self.photoimg1 = ImageTk.PhotoImage( img1 )

        #lblimg1 = Label( self.root, image=self.photoimg1, bd=0, relief=RIDGE )
        #lblimg1.place( x=0, y=0, width=1300, height=800 )

        ########main fram
        main_frame = Frame( self.root, bd=4, relief=RIDGE, bg='aquamarine' )
        main_frame.place( x=0, y=0, width=222, height=110 )

        ####button

        phn_add_btn = Button( main_frame, command=self.delete_number,text='Delete',  width=21, height=2,
                              font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_add_btn.grid( row=0, column=0 )

        phn_search_btn = Button( main_frame, command=self.update_number,  text='Update', width=21, height=2,
                                 font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_search_btn.grid( row=1, column=0 )


    def delete_number(self):
        self.new_window=Toplevel(self.root)
        self.app=Delete(self.new_window)

    def update_number(self):
        self.new_window=Toplevel(self.root)
        self.app=Update(self.new_window)

if __name__ == '__main__':
    root=Tk()
    ob=Option(root)
    root.mainloop()