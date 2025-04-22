from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox

from guipackage import adminDash

from middleware.ManageDriver import getAllDriverid
from middleware.TripManager import  assignDriver, assingTrip
from middleware.trip import Trip


class assidndriver:

    def __init__(self, root):
        self.root = root
        self.root.title("Assign Driver")

        frameWidth = 1800
        frameHeight = 880
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        xCordinate = int((screenWidth / 2) - (frameWidth / 2))
        yCordinate = int((screenHeight / 2) - (frameHeight / 2))
        self.root.geometry("{}x{}+{}+{}".format(frameWidth, frameHeight, xCordinate, yCordinate))

        frame = Frame(self.root,   bg="red", height=100)
        frame.pack(side=TOP, fill=BOTH)

        font = ('Tahoma', 22, 'bold')
        font2 = ('Tahoma', 14, 'normal')

        ids = getAllDriverid()

        bookingframe = LabelFrame(self.root, text="Assign Driver", font=font, padx=2, pady=60, bg='#458B74')
        bookingframe.place(relx=0.01, rely=0.2)

        txtTid = Entry(bookingframe,)


        lblpickupT = Label(bookingframe, text="Pick Up Time: ", font=font2, padx=10, pady=10, bg='#458B74')
        lblpickupT.grid(row=0, column=0)

        txtpickupT = Entry(bookingframe, font=font2, bg='#458B00')
        txtpickupT.grid(row=0, column=1, padx=10, pady=10)

        lblpickupD = Label(bookingframe, text="Pick Up Date: ", font=font2, padx=10, pady=10, bg='#458B74')
        lblpickupD.grid(row=1, column=0)

        txtpickupD = Entry(bookingframe, font=font2, width=18, bg='#458B00')
        txtpickupD.grid(row=1, column=1, padx=10, pady=10)

        lblpickupP = Label(bookingframe, text="Pick up place: ", font=font2, padx=10, pady=10, bg='#458B74')
        lblpickupP.grid(row=2, column=0, padx=10, pady=10)

        txtpickupP = Entry(bookingframe, font=font2, bg='#458B00')
        txtpickupP.grid(row=2, column=1, padx=10, pady=10)

        lbldropoffP = Label(bookingframe, text="DropOff up place: ", font=font2, padx=10, pady=10, bg='#458B74')
        lbldropoffP.grid(row=3, column=0, padx=10, pady=10)

        txtdropoffP = Entry(bookingframe, font=font2, bg='#458B00')
        txtdropoffP.grid(row=3, column=1, padx=10, pady=10)

        lbldriver = Label(bookingframe, text='Assign Driver', font=font2, padx=10, pady=10, bg='#458B74')
        lbldriver.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        cmboBx = Combobox(bookingframe, width=18, font=font2)
        cmboBx['values'] = ids
        cmboBx.current(0)
        cmboBx.grid(row=4, column=1, padx=10, pady=15)

        def assignDvr():
            did1 = cmboBx.get()
            tid1 = txtTid.get()
            ok = Trip(did=did1, tid=tid1)
            result = assignDriver(ok)
            if result is True:
                messagebox.showinfo('msg', "Driver Assigned")
            else:
                messagebox.showerror('msg', "Error")

        btnassignD = Button(bookingframe, text="Assign", font=font2, bg='#3d7a66', command=assignDvr)
        btnassignD.grid(row=5, column=0, padx=10, pady=15)

        def Close():
            self.root.destroy()
            root = Tk()
            adminDash.AdminDashboard(root)
            root.mainloop()

        btncancel = Button(bookingframe, text="Cancel", font=font2, bg='#3d7a66',command=Close)
        btncancel.grid(row=5, column=1, padx=10, pady=15)

        viewbookingframe = LabelFrame(self.root, text="Pending Booking", font=font, padx=90, pady=20)
        viewbookingframe.place(relx=0.4, rely=0.2)

        result = assingTrip()

        tableFrame = Frame(viewbookingframe)
        tableFrame.pack(padx=0, pady=0)

        tblPersons = ttk.Treeview(tableFrame, height=28)
        tblPersons['columns'] = (
            'tid', 'pick up time', 'pick up date', 'pick up place', 'drop off place', 'status', 'driver id')

        tblPersons.column('#0', width=0, stretch=NO)
        tblPersons.column('tid', width=50, anchor=CENTER)
        tblPersons.column('pick up time', width=150, anchor=CENTER)
        tblPersons.column('pick up date', width=150, anchor=CENTER)
        tblPersons.column('pick up place', width=120, anchor=CENTER)
        tblPersons.column('drop off place', width=120, anchor=CENTER)
        tblPersons.column('status', width=100, anchor=CENTER)
        tblPersons.column('driver id', width=100, anchor=CENTER)

        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('tid', text='TID', anchor=CENTER)
        tblPersons.heading('pick up time', text='pick up time', anchor=CENTER)
        tblPersons.heading('pick up date', text='pick up date', anchor=CENTER)
        tblPersons.heading('pick up place', text='pick up place', anchor=CENTER)
        tblPersons.heading('drop off place', text='drop off place', anchor=CENTER)
        tblPersons.heading('status', text='status', anchor=CENTER)
        tblPersons.heading('driver id', text='driver id', anchor=CENTER)

        r_set = result
        for dt in r_set:
            tblPersons.insert(parent="", index='end',
                              values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

        tblPersons.pack()

        def on_select(event):
            selectedItem = tblPersons.selection()[0]

            values = tblPersons.item(selectedItem, "values")
            txtpickupT.delete(0, END)
            txtpickupD.delete(0, END)
            txtpickupP.delete(0, END)
            txtdropoffP.delete(0, END)
            txtTid.insert(0,values[0])
            txtpickupT.insert(0, values[1])
            txtpickupD.insert(0, values[2])
            txtpickupP.insert(0, values[3])
            txtdropoffP.insert(0, values[4])



        tblPersons.bind("<<TreeviewSelect>>", on_select)

        lblTitle = Label(frame, text="Assign Driver", font=font, fg='white', bg='red')
        lblTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == '__main__':
    root = Tk()
    assidndriver(root)
    root.mainloop()
