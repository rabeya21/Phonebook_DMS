from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from tkinter import messagebox

import pymysql
from tkinter import ttk

class Update:
    def __init__(self,root):
        self.root=root
        self.root.title("Tele Phone Book")
        self.root.geometry("1550x800+0+0")

        self.var_name = StringVar()
        self.ver_phone = StringVar()
        self.var_email = StringVar()
        self.var_groups = StringVar()
        self.var_address = StringVar()
        self.var_relationship = StringVar()
        self.var_notes = StringVar()

    ############ Title

        lb1_title = Label(self.root, text='Search', font=("arial", 30, "bold"), bg='orange',
                      fg='aquamarine', bd=4, relief=RIDGE)
        lb1_title.place(x=380, y=200, width=450, height=50)

        lb1_title = Label(self.root, text='Search', font=("arial", 30, "bold"), bg='orange',
                      fg='aquamarine', bd=4, relief=RIDGE)
        lb1_title.place(x=380, y=200, width=450, height=50)

      ########main fram
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg='aquamarine')
        main_frame.place(x=380, y=300, width=450, height=400)

      ######  name

        self.name = Label(main_frame, text="Name", font=("times in roman", 12, "bold"), fg="Red", bg="aquamarine")
        self.name.place(x=7, y=10)

        txt_name = ttk.Entry(main_frame, textvariable=self.var_name, width=18, font=("arial", 13, "bold"))
        txt_name.place(x=100, y=10, width=270)

      ######  phone

        self.phone = Label(main_frame, text="Phone No.", font=("times in roman", 12, "bold"), fg="Red", bg="aquamarine")
        self.phone.place(x=7, y=40)

        txt_phone = ttk.Entry(main_frame, textvariable=self.ver_phone, width=18, font=("arial", 13, "bold"))
        txt_phone.place(x=100, y=40, width=270)

        ############## update button
        phn_search_btn = Button(main_frame, command=self.update, activeforeground="red",
                                activebackground="aquamarine", text='Update', width=21, height=2,
                                font=("arial", 13, "bold"), bg='aquamarine', fg='red', bd=0, cursor='hand2')
        phn_search_btn.place(x=270, y=70, width=70)

        ####back button

        self.btn_back = Button(main_frame,command=self.logout,  text="Back", activeforeground="blue",
                               activebackground="aquamarine", font=("times new roman", 13, "bold"), bd=0,
                               cursor="hand2",
                               bg="aquamarine", fg="blue").place(x=70, y=75, width=100)

        # ***************Show data Table************************
        details_table = LabelFrame(main_frame, bd=2, relief=RIDGE)
        details_table.place(x=30, y=150, width=400, height=200)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(details_table, column=("name", "phone"), yscrollcommand=scroll_y,
                                              xscrollcommand=scroll_x)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.cust_ditals_table.yview)

        self.cust_ditals_table.heading("name", text="Name")
        self.cust_ditals_table.heading("phone", text="Contact Number")

        self.cust_ditals_table["show"] = "headings"

        self.cust_ditals_table.column("name", width=100)
        self.cust_ditals_table.column("phone", width=100)
        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        self.cust_ditals_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="phone_book")
        my_cursor = conn.cursor()
        my_cursor.execute("select Name,Phone from create_contact ORDER BY Name ASC")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.cust_ditals_table.focus()
        contant = self.cust_ditals_table.item(cursor_row)
        row = contant["values"]
        self.var_name.set(row[0])
        self.ver_phone.set(row[1])
        self.var_email.set(row[2])
        self.var_groups.set(row[3])
        self.var_address.set(row[4])
        self.var_notes.set(row[5])


    def update(self):
        if self.ver_phone.get()=="":
            messagebox.showerror("Error","Please Enter Phone Number",parent=self.root)

        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="phone_book")
                my_cursor = conn.cursor()
                my_cursor.execute("update create_contact set phone=%s,email=%s,groups=%s,address=%s,notes=%s where name=%s",(self.ver_phone.get(),
                                                                                                                             self.var_email.get(),
                                                                                                                             self.var_groups.get(),
                                                                                                                             self.var_address.get(),
                                                                                                                             self.var_notes.get(),
                                                                                                                             self.var_name.get()))

                messagebox.showinfo("Updated", "updated sucessfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something is wrong : {str(es)} ", parent=self.root)

    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    ob=Update(root)
    root.mainloop()