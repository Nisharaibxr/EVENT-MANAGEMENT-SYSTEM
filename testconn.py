from tkinter import *
import tkinter.messagebox
import sqlite3
def new():
    def reset_all():
        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        cont_entry.delete(0, END)
        email_entry.delete(0, END)

    def sqlitetest():
        first_name = fname1.get()
        last_name = lname1.get()
        mob_no = mob.get()
        emal_id = email.get()

        conn = sqlite3.connect("Testing.db")
        cur = conn.cursor()

#TABLE 1  : Events

        cur.execute("Create Table if not Exists Events (first_name text,last_name text,phone_no integer,email_id text)")
        cur.execute('insert into Events (first_name,last_name,Phone_no,email_id) values (?,?,?,?)',
                    (first_name, last_name, mob_no, emal_id))
        conn.commit()
        conn.close()

        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        cont_entry.delete(0, END)
        email_entry.delete(0, END)

        tkinter.messagebox.showinfo("success", "Account created successfully")

    def all():
        global root
        root = Toplevel()
        root.title("account")
        root.geometry("250x260")

        global fname1, mob, lname1, email

        global fname_entry, lname_entry, cont_entry, email_entry

        fname1 = StringVar()
        lname1 = StringVar()
        mob = StringVar()
        email = StringVar()

        f_name = Label(root, text="First Name", font="20")
        l_name = Label(root, text="Last Name", font="20")
        contact = Label(root, text="Password", font="20")
        email1 = Label(root, text="Email Id", font="20")
        bn1 = Button(root, text="SUBMIT", bg='tomato', font="30", command=sqlitetest)
        resetbn = Button(root, text="reset", bg='tomato', font="30", command=reset_all)

        fname_entry = Entry(root, textvar=fname1)
        lname_entry = Entry(root, textvar=lname1)
        cont_entry = Entry(root, textvar=mob)
        email_entry = Entry(root, textvar=email)

        f_name.grid(row=2, column=3)
        l_name.grid(row=3, column=3)
        contact.grid(row=4, column=3)
        email1.grid(row=5, column=3)

        fname_entry.grid(row=2, column=4)
        lname_entry.grid(row=3, column=4)
        cont_entry.grid(row=4, column=4)
        email_entry.grid(row=5, column=4)

        bn1.grid(row=6, column=3)
        resetbn.grid(row=6, column=4)

    all()
    root.mainloop()