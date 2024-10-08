from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk

from Add import Add
from Search import Search
from Option import Option
from ShowAll import ShowAll


from tkinter import ttk

class DeshBoard:
    def __init__(self,root):
        self.root=root
        self.root.title("Tele Phone Book")
        self.root.geometry("1550x800+0+0")

        ###### Image 1

       # img1 = Image.open(r"C:\Users\Maysha\Downloads\phonebook.jpg")
        #img1 = img1.resize((1300, 800), Image.ANTIALIAS)
        #self.photoimg1 = ImageTk.PhotoImage(img1)

        #lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        #lblimg1.place(x=0, y=0, width=1300, height=800)

        ############ Title

        lb1_title=Label(self.root,text='Phone Book',font=("arial", 30, "bold"),bg='orange',fg='aquamarine',bd=4,relief=RIDGE)
        lb1_title.place(x=550,y=250, width=350, height=50)

        ########main fram
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg='aquamarine')
        main_frame.place(x=630,y=360, width=222, height=200)

        ####button

        phn_add_btn=Button(main_frame,text='Create new contact',command=self.creat_number,width=21,height=2,font=("arial",13, "bold"),bg='aquamarine',fg='red',bd=0,cursor='hand2')
        phn_add_btn.grid(row=0,column=0)

        phn_search_btn = Button( main_frame, command=self.sharch_number,text='Search', width=21, height=2, font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_search_btn.grid( row=1, column=0 )

        phn_show_btn = Button( main_frame,command=self.show_all, text='Show all', width=21, height=2, font=("arial", 13, "bold"),bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_show_btn.grid( row=2, column=0 )

        phn_option_btn = Button( main_frame, command=self.more_option,text='Option', width=21, height=2, font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2' )
        phn_option_btn.grid( row=3, column=0 )

    def creat_number(self):
        self.new_window=Toplevel(self.root)
        self.app=Add(self.new_window)

    def sharch_number(self):
        self.new_window=Toplevel(self.root)
        self.app=Search(self.new_window)
    def more_option(self):
        self.new_window=Toplevel(self.root)
        self.app=Option(self.new_window)

    def show_all(self):
        self.new_window=Toplevel(self.root)
        self.app=ShowAll(self.new_window)






if __name__ == '__main__':
    root=Tk()
    ob=DeshBoard(root)
    root.mainloop()