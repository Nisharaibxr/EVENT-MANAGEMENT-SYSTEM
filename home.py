import tkinter.messagebox
from testconn import *
from registration import *

class home_page:

# menu..buttons...

    def homepage(self):
        Frame(root, bg="black", width=1341, height=35, relief=SUNKEN).place(x=13, y=20)
        Button(text="EXPLORE EVENTS", bg="tomato", fg="black", font="20,'Helvetica','bold'",
               command=self.show).place(x=826, y=23)
        divider = Label(bg="grey", height=43, width=0)
        search_bn = Button(text="Search", bg="tomato", fg="black", command=self.search_show)
        login_bn = Button(text="LOGIN", bg="tomato", fg="black", font="20,'Helvetica','bold'", command=self.input_login)
        newuser_bn = Button(text="CREATE NEW ACCOUNT", bg="tomato", fg="black", font="20,'Helvetica','bold'",
                            command=new)
        reg_event = Button(text="REGISTER TO THIS EVENT", bg="green", fg="black", font="60,'Helvetica','bold'",
                           command=self.onClick)

        list_box = Listbox(bg="#ffc895", width=124, height=40)
        Button(text="...EVENT MANAGEMENT SYSTEM...", bg="green", fg="black", font="40,'Helvetica','bold'",
               ).place(x=380, y=23)
        global district
        district = StringVar()
        search_entry = Entry(width=20, textvar=district)

        search_entry.place(x=13, y=33)
        search_bn.place(x=139, y=27)

        login_bn.place(x=1020, y=23)
        newuser_bn.place(x=1100, y=23)
        divider.place(x=588, y=55)
        reg_event.place(x=190, y=668)
        list_box.place(x=599, y=60)

    def registerpage(self):
        Label(bg="light blue", height=2, width=30).place(x=190, y=668)
        Button(text="YOUR EVENT REGISTERED", bg="green", fg="black", font="60,'Helvetica','bold'",
               command=self.register_pop).place(x=190, y=668)

    def register_pop(self):
        tkinter.messagebox.showwarning("message", "Already registered")


# secand page/after_login

    def after_login(self):
        user_id = email_entry.get()
        passw = pass_entry.get()

#Database connection
        conn = sqlite3.connect("Testing.db")
        curr = conn.cursor()
        welcome = curr.execute('select first_name from Events where lower(email_id)=? and phone_no=?',
                               (user_id, passw,))
        name = []

        try:
            for p in welcome:
                name.append(p)
            c = len(name[0])
            if (c == 1):
                tkinter.messagebox.showinfo("success", "login successfully")
                Frame(root, bg="black", width=1346, height=35, relief=SUNKEN).place(x=13, y=20)
                Button(text="WELCOME! so glad you are here..", bg="green", fg="black", font="20,'Helvetica','bold'",
                       ).place(x=411, y=23)
                Button(text="CREATE NEW EVENT", bg="tomato", fg="black", font="60,'Helvetica','bold'",
                       command=create_event).place(x=832, y=23)
                Button(text="EXPLORE EVENTS", bg="tomato", fg="black", font="20,'Helvetica','bold'",
                       command=self.show_after).place(x=1050, y=23)
                Button(text="REGISTER TO THIS EVENT", bg="green", fg="black", font="60,'Helvetica','bold'",
                       command=self.registerpage).place(x=190, y=668)
                Button(text="LOGOUT", bg="tomato", fg="black", font="20,'Helvetica','bold'",
                       command=self.homepage).place(x=1244, y=23)
                search_entry = Entry(width=20, textvar=district)
                search_bn = Button(text="Search", bg="tomato", fg="black", command=self.search_show)
                search_entry.place(x=13, y=33)
                search_bn.place(x=139, y=27)
        except IndexError:
            tkinter.messagebox.showwarning("Incorrect", "Please Enter correct details")

    def askmessage(self):
        if tkinter.messagebox.askyesno('Verify', 'Do you want to register in this event'):
            tkinter.messagebox.showinfo('Yes', 'Thanks for register to this event')
        else:
            tkinter.messagebox.showinfo('No', 'You are not registered')

    def show_after(self):
        conn = sqlite3.connect("Testing.db")
        curr = conn.cursor()
        row = curr.execute("select * from NewEvent")
        a = []
        for i in row:
            a.append(i)
        z = 63
        Label(root, bg="#ffc895", height=39, width=105).place(x=601, y=z)
        for j in range(len(a)):
            if z < 300:
                Label(root, bg="#ffc895", height=45 - z, width=105).place(x=601, y=z)
            Button(root, bg="ghost white", fg="black", font="15,'Helvetica'", text=a[j], command=self.askmessage).place(
                x=605, y=z)
            c = Canvas(root, bg="grey", height=1, width=740)
            z += 30
            c.place(x=601, y=z)
            z += 20
        conn.close()

    def input_login(self):

        def reset_all():
            email_entry.delete(0, END)
            pass_entry.delete(0, END)

        def ui_login():
            global l_root, email_entry, pass_entry
            l_root = Tk()
            l_root.title("Login")
            l_root.geometry("240x140+730+100")
            l_root.config(bg="orange")

            Label(l_root, text="Email Id", bg="orange", font="30").grid(row=4, column=4)
            Label(l_root, text="Password", bg="orange", font="30").grid(row=5, column=4)
            Button(l_root, text="Login", bg="blue", font="30", command=self.after_login).grid(row=6, column=4)
            Button(l_root, text="reset", bg="blue", font="30", command=reset_all).grid(row=6, column=5)

            email_entry = Entry(l_root, bg="pink")
            pass_entry = Entry(l_root, show="*", bg="pink")

            email_entry.grid(row=4, column=5)
            pass_entry.grid(row=5, column=5)

        ui_login()
        l_root.mainloop()

    def login(self):
        conn = sqlite3.connect("Testing.db")
        curr = conn.cursor()
        name_row = curr.execute("select first_name from Events")
        all_name = []
        for k in name_row:
            all_name.append(k)
        print(all_name)
        p = 63
        Label(root, bg="#ffc895", height=39, width=105).place(x=601, y=p)

        for l in range(len(all_name)):
            Label(root, bg="#ffc895", text=all_name[l]).place(x=601, y=p)
            p += 17

    def message(self):
        tkinter.messagebox.showinfo("info",
                                    "Owner name,Event name,Event type,Address,District,Time,Date,Cost,No of Seats")

    def show(self):
        conn = sqlite3.connect("Testing.db")
        curr = conn.cursor()
        row = curr.execute("select * from NewEvent")
        a = []
        for i in row:
            a.append(i)
        z = 63
        Label(root, bg="#ffc895", height=39, width=105).place(x=601, y=z)
        for j in range(len(a)):
            if z < 300:
                Label(root, bg="#ffc895", height=45 - z, width=105).place(x=601, y=z)
            Button(root, bg="ghost white", fg="black", font="15,'Helvetica'", text=a[j], command=self.message).place(
                x=605, y=z)
            c = Canvas(root, bg="grey", height=1, width=740)
            z += 30
            c.place(x=601, y=z)
            z += 20
        conn.close()

    def search_show(self):

        res = district.get()
        conn = sqlite3.connect("Testing.db")
        curr = conn.cursor()
        rw = curr.execute("select * from NewEvent where lower(District)=?", (res,))

        b = []
        for i in rw:
            b.append(i)
        z = 63

        for j in range(len(b)):
            Label(root, bg="#ffc895", height=39, width=105).place(x=601, y=z)
            Button(root, bg="ghost white", fg="black", font="15,'Helvetica'", text=b[j]).place(x=605, y=z)
            c = Canvas(root, bg="black", height=1, width=740)
            z += 30
            c.place(x=601, y=z)
            z += 20

    def credits(self):
        tkinter.messagebox.showinfo("Developer",
                                    "This is an Event management software\nDeveloper is NISHA RAI\nRegistration no. 12008898")

    def donothing(self):
        tkinter.messagebox.showinfo("Warning", "Sorry its not working")

    def onClick(self):
        tkinter.messagebox.showinfo("Warning", "Please Login First")

    def main_menu(self):
        global root
        root = Tk()
        root.title("EVENT  MANAGEMENT  SYSTEM")
        root.geometry('1366x768+0+0')
        root.configure(bg='light blue')

        #photo3 = PhotoImage(file=img_list[self.i])
        #pix = Label(root, image=photo3)
        #pix.place(x=13, y=60)

        Label(root, bg="grey").pack(fill=X)
        Label(root, bg="grey", width=1).pack(side=RIGHT, fill=Y)
        Label(root, bg="grey", width=1).pack(side=LEFT, fill=Y)
        Label(root, bg="grey").pack(side=BOTTOM, fill=X)

        self.homepage()

        m = Menu(root)
        root.config(menu=m)

#Submenu_bar......

        submenu = Menu(m, tearoff=1)
        m.add_cascade(label="File", menu=submenu)
        submenu.add_command(label="New File          Ctrl+N", command=self.donothing)
        submenu.add_command(label="New Window   Ctrl+Shift+N", command=self.donothing)
        submenu.add_command(label="Save               Ctrl+S", command=self.donothing)
        submenu.add_command(label="Save as..  Ctrl+Shift+S", command=self.donothing)
        submenu.add_separator()
        submenu.add_command(label="Exit", command=exit)

        submenu1 = Menu(m, tearoff=0)
        m.add_cascade(label="Edit", menu=submenu1)

        submenu1.add_separator()
        submenu1.add_command(label="Find         F4", command=self.donothing)
        submenu1.add_command(label="Find Next    F5", command=self.donothing)
        submenu1.add_command(label="Replace      F2", command=self.donothing)
        submenu1.add_command(label="Go To..      F3", command=self.donothing)

        submenu3 = Menu(m, tearoff=0)
        m.add_cascade(label="Format", menu=submenu3)
        submenu3.add_command(label="Font", command=self.donothing)

        submenu4 = Menu(m, tearoff=0)
        m.add_cascade(label="View", menu=submenu4)
        submenu4.add_command(label="Zoom", command=self.donothing)
        submenu4.add_command(label="Status Bar", command=self.donothing)

        submenu5 = Menu(m, tearoff=0)
        m.add_cascade(label="Help", menu=submenu5)
        submenu5.add_command(label="View Help", command=self.donothing)
        submenu5.add_command(label="Send Feedback", command=self.donothing)
        submenu5.add_separator()
        submenu5.add_command(label="About", command=self.credits)

        root.mainloop()


a = home_page()
a.main_menu()