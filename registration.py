from tkinter import *
import tkinter.messagebox
import sqlite3
def create_event():

#Reset Data field for booking event...

    def ereset():
        owner_name1.delete(0, END)
        Event_name1.delete(0, END)
        Event_address1.delete(0, END)
        Event_district1.delete(0, END)
        Event_type1.delete(0, END)
        time_event1.delete(0, END)
        No_seat1.delete(0, END)
        Event_cost1.delete(0, END)
        Date_event1.delete(0, END)

#
    def insideevent():
        owner_name = u_name.get()
        Event_name = E_name.get()
        Event_type = E_type.get()
        Event_address = E_address.get()
        Event_district = E_district.get()
        time_event = E_time.get()
        Date_event = E_date.get()
        Event_cost = E_cost.get()
        No_seat = E_seat.get()

        conn = sqlite3.connect("Testing.db")
        cur = conn.cursor()

#TABLE 2 : NewEvent

        cur.execute(
            "Create Table if not Exists NewEvent (OWNER text,Event_Name text,Event_Type text,Address text,"
            "District text,Time numeric,Date numeric,Cost numeric,Seat numeric )")
        cur.execute('insert into NewEvent values (?,?,?,?,?,?,?,?,?)', (
        owner_name, Event_name, Event_type, Event_address, Event_district, time_event, Date_event, Event_cost, No_seat))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("Create", "Event Created Successfully")

    def new():
        global root
        root = Toplevel()
        root.title("NewEvent")
        root.geometry("450x350+500+120")

        global owner_name1, Event_name1, Event_address1, Event_district1, Event_type1, time_event1, Date_event1
        global Event_cost1, No_seat1

        global u_name, E_name, E_type, E_address, E_district, E_time, E_date, E_cost, E_seat

        u_name = StringVar()
        E_name = StringVar()
        E_type = StringVar()
        E_address = StringVar()
        E_district = StringVar()
        E_time = StringVar()
        E_date = StringVar()
        E_cost = StringVar()
        E_seat = StringVar()

        Label(root, text="Organizer Name", font="20").grid(row=2, column=3)
        Label(root, text="Event Name", font="20").grid(row=3, column=3)
        Label(root, text="Event Type", font="20").grid(row=4, column=3)
        Label(root, text="Event Place", font="20").grid(row=5, column=3)
        Label(root, text="District", font="20").grid(row=6, column=3)
        Label(root, text="Event Time", font="20").grid(row=7, column=3)
        Label(root, text="Event Date", font="20").grid(row=8, column=3)
        Label(root, text="Event Cost", font="20").grid(row=9, column=3)
        Label(root, text="No Of Seat", font="20").grid(row=10, column=3)
        Button(root, text="Create", bg='tomato', command=insideevent, font="30").grid(row=11, column=4)
        Button(root, text="Reset", bg='tomato', command=ereset, font="30").grid(row=11, column=5)

        owner_name1 = Entry(root, textvar=u_name)
        Event_name1 = Entry(root, textvar=E_name)
        Event_address1 = Entry(root, textvar=E_type)
        Event_district1 = Entry(root, textvar=E_address)
        Event_type1 = Entry(root, textvar=E_district)
        time_event1 = Entry(root, textvar=E_time)
        Date_event1 = Entry(root, textvar=E_date)
        Event_cost1 = Entry(root, textvar=E_cost)
        No_seat1 = Entry(root, textvar=E_seat)

        owner_name1.grid(row=2, column=5)
        Event_name1.grid(row=3, column=5)
        Event_address1.grid(row=4, column=5)
        Event_district1.grid(row=5, column=5)
        Event_type1.grid(row=6, column=5)
        time_event1.grid(row=7, column=5)
        Date_event1.grid(row=8, column=5)
        Event_cost1.grid(row=9, column=5)
        No_seat1.grid(row=10, column=5)
    new()
    root.mainloop()