from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from guipackage import login_page
from middleware import Global
from middleware.TripManager import confirmTrip, completeTrip
from middleware.trip import Trip


class DriverDash:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Dashboard")

        frameWidth = 1900
        frameHeight = 980
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        xCordinate = int((screenWidth / 2) - (frameWidth / 2))
        yCordinate = int((screenHeight / 2) - (frameHeight / 2))
        self.root.geometry("{}x{}+{}+{}".format(frameWidth, frameHeight, xCordinate, yCordinate))

        frame = Frame(self.root, bg="red", height=100)


        frame.pack(side=TOP, fill=BOTH)
        font = ('Tahoma', 22, 'bold')
        font2 = ('Tahoma', 16, 'normal')

        did_txt = Entry(self.root)
        did_txt.insert(0, Global.currentdriver[0])

        def logout():
            self.root.destroy()
            root = Tk()
            login_page.Loginpage(root)
            root.mainloop()

        bookingframe = LabelFrame(self.root, text="Complete Trip", font=font, padx=2, pady=60, bg='#458B74')
        bookingframe.place(relx=0.01, rely=0.2)

        btnlogout = Button(frame, command=logout, text="LOG OUT", font=font2, fg='white', bg='red')
        btnlogout.place(relx=0.9, rely=0.5, anchor=CENTER)

        txtTid = Entry(bookingframe, )


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

        def completebook():
            did = did_txt.get()
            tid1 = txtTid.get()
            comp = Trip(did=did, tid=tid1)
            result = completeTrip(comp)

            if result is True:
                messagebox.showinfo('msg', "Work Done")
            else:
                messagebox.showerror('msg', "Error")

        btnassignD = Button(bookingframe, text="complete", font=font2, bg='#3d7a66', command=completebook)
        btnassignD.grid(row=5, column=0, padx=10, pady=15)

        btncancel = Button(bookingframe, text="Cancel", font=font2, bg='#3d7a66')
        btncancel.grid(row=5, column=1, padx=10, pady=15)

        viewbookingframe = LabelFrame(self.root, text="Edit Booking", font=font, padx=90, pady=20)
        viewbookingframe.place(relx=0.4, rely=0.2)

        tableFrame = Frame(viewbookingframe)
        tableFrame.pack(padx=0, pady=0)


        result = confirmTrip(did_txt.get())
        tblPersons = Treeview(tableFrame, height=28)
        tblPersons['columns'] = (
            'tid', 'pickup time', 'pickup date', 'pickup place', 'dropoff place', 'status', 'C id', 'D id')

        tblPersons.column('#0', width=0, stretch=NO)
        tblPersons.column('tid', width=50, anchor=CENTER)
        tblPersons.column('pickup time', width=150, anchor=CENTER)
        tblPersons.column('pickup date', width=150, anchor=CENTER)
        tblPersons.column('pickup place', width=150, anchor=CENTER)
        tblPersons.column('dropoff place', width=150, anchor=CENTER)
        tblPersons.column('status', width=150, anchor=CENTER)
        tblPersons.column('C id', width=50, anchor=CENTER)
        tblPersons.column('D id', width=50, anchor=CENTER)

        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('tid', text='TID', anchor=CENTER)
        tblPersons.heading('pickup time', text='pickup time', anchor=CENTER)
        tblPersons.heading('pickup date', text='pickup date', anchor=CENTER)
        tblPersons.heading('pickup place', text='pickup place', anchor=CENTER)
        tblPersons.heading('dropoff place', text='dropoff place', anchor=CENTER)
        tblPersons.heading('status', text='status', anchor=CENTER)
        tblPersons.heading('C id', text='C id', anchor=CENTER)
        tblPersons.heading('D id', text='D id', anchor=CENTER)

        r_set = result
        for dt in r_set:
            tblPersons.insert(parent="", index='end',
                              values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6],dt[7]))

        tblPersons.pack()

        def on_select(event):
            selectedItem = tblPersons.selection()[0]

            values = tblPersons.item(selectedItem, "values")
            txtpickupT.delete(0, END)
            txtpickupD.delete(0, END)
            txtpickupP.delete(0, END)
            txtdropoffP.delete(0, END)
            txtTid.insert(0, values[0])
            txtpickupT.insert(0, values[1])
            txtpickupD.insert(0, values[2])
            txtpickupP.insert(0, values[3])
            txtdropoffP.insert(0, values[4])

        tblPersons.bind("<<TreeviewSelect>>", on_select)

        lblTitle = Label(frame, text="Have a safe journey", font=font, fg='white', bg='red')
        lblTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == '__main__':
    root = Tk()
    DriverDash(root)
    root.mainloop()