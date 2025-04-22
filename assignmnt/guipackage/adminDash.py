import sys
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

from PIL import ImageTk, Image

from guipackage import login_page
from guipackage.assigndriver import assidndriver
from middleware.ManageCustomer import getAllCustomer
from middleware.ManageDriver import saveDriver, displayAllDriver
from middleware.TripManager import  getTrip

from middleware.newDriver import Driver



class AdminDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")

        frameWidth = 1500
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

        imageframe = Frame(self.root)
        imageframe.pack()
        imageframe.place(x=325, y=90)
        image1 = Image.open("dash1.jpg")
        test2 = ImageTk.PhotoImage(image1)
        label1 = Label(imageframe, image=test2)
        label1.image = test2
        label1.pack()



        def addDriver():
            driverframe = LabelFrame(self.root, text="Add Driver", font=font, padx=280, pady=140, bg='#458B74')
            driverframe.place(relx=0.3, rely=0.2)



            def saveDvr():

                name = str(txtname.get())
                email = str(txtemail.get())
                address = str(txtaddress.get())
                licenseno = str(txtlicenseno.get())
                password = str(txtPassword.get())
                nd1 = Driver(did=0, name=name, email=email, address=address, licenseno=licenseno, password=password)
                result = saveDriver(nd1)
                if result is True:
                    messagebox.showinfo('msg', "Driver added")
                else:
                    messagebox.showinfo('msg', "Data saved")

            lblname = Label(driverframe, text="Name: ", padx=10, pady=10, font=font2, bg='#458B74')
            lblname.grid(row=0, column=0)

            txtname = Entry(driverframe, font=font2, bg='#458B00')
            txtname.grid(row=0, column=1, padx=10, pady=10)

            lblemail = Label(driverframe, text="Email: ", padx=10, pady=10, font=font2, bg='#458B74')
            lblemail.grid(row=1, column=0)

            txtemail = Entry(driverframe, font=font2, bg='#458B00')
            txtemail.grid(row=1, column=1, padx=10, pady=10)

            lbladdress = Label(driverframe, text="Address: ", padx=10, pady=10, font=font2, bg='#458B74')
            lbladdress.grid(row=2, column=0)

            txtaddress = Entry(driverframe, font=font2, bg='#458B00')
            txtaddress.grid(row=2, column=1, padx=10, pady=10)

            lbllicenseno = Label(driverframe, text="License No ", padx=10, pady=10, font=font2, bg='#458B74')
            lbllicenseno.grid(row=3, column=0)

            txtlicenseno = Entry(driverframe, font=font2, bg='#458B00')
            txtlicenseno.grid(row=3, column=1, padx=10, pady=10)

            lblPassword = Label(driverframe, text="Password: ", padx=10, pady=10, font=font2, bg='#458B74')
            lblPassword.grid(row=4, column=0)

            txtPassword = Entry(driverframe, show='*', font=font2, bg='#458B00')
            txtPassword.grid(row=4, column=1, padx=10, pady=10)

            btnSubmit = Button(driverframe, text="Add", font=font2, command=saveDvr, bg='#3d7a66')
            btnSubmit.grid(row=5, column=0, padx=20, pady=20)

            btnclose = Button(driverframe, text="Close", font=font2, bg='#3d7a66')
            btnclose.grid(row=5, column=1, padx=20, pady=20)

        def assignDriver():
            self.root.destroy()
            root = Tk()
            assidndriver(root)
            root.mainloop()

        def viewcus():
            viewcustomerframe = LabelFrame(self.root, text=" Customer Details", font=font, padx=110, pady=20, )
            viewcustomerframe.place(relx=0.3, rely=0.2)

            tableFrame = Frame(viewcustomerframe)
            tableFrame.pack(padx=0, pady=0)

            tblPersons = Treeview(tableFrame, height=28)
            tblPersons['columns'] = (
                'cid', 'name', 'address', 'email', 'contactno', 'payment')

            tblPersons.column('#0', width=0, stretch=NO)
            tblPersons.column('cid', width=50, anchor=CENTER)
            tblPersons.column('name', width=150, anchor=CENTER)
            tblPersons.column('address', width=150, anchor=CENTER)
            tblPersons.column('email', width=100, anchor=CENTER)
            tblPersons.column('contactno', width=100, anchor=CENTER)
            tblPersons.column('payment', width=100, anchor=CENTER)


            tblPersons.heading('#0', text='', anchor=CENTER)
            tblPersons.heading('cid', text='CID', anchor=CENTER)
            tblPersons.heading('name', text='Name', anchor=CENTER)
            tblPersons.heading('address', text='Address', anchor=CENTER)
            tblPersons.heading('email', text='Email', anchor=CENTER)
            tblPersons.heading('contactno', text='Contact', anchor=CENTER)
            tblPersons.heading('payment', text='Payment', anchor=CENTER)


            result = getAllCustomer()
            cus_set = result
            for dt in cus_set:
                tblPersons.insert(parent="", index='end',
                                  values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))

            tblPersons.pack()

        def viewdvr():
            viewdriverframe = LabelFrame(self.root, text=" Driver Details", font=font, padx=150, pady=20, bg='#458B74' )
            viewdriverframe.place(relx=0.3, rely=0.2)

            tableFrame = Frame(viewdriverframe)
            tableFrame.pack(padx=0, pady=0)

            tblPersons = Treeview(tableFrame, height=28)
            tblPersons['columns'] = (
                'did', 'name', 'email','address',  'licenseno')

            tblPersons.column('#0', width=0, stretch=NO)
            tblPersons.column('did', width=50, anchor=CENTER)
            tblPersons.column('name', width=150, anchor=CENTER)
            tblPersons.column('email', width=150, anchor=CENTER)
            tblPersons.column('address', width=100, anchor=CENTER)
            tblPersons.column('licenseno', width=100, anchor=CENTER)


            tblPersons.heading('#0', text='', anchor=CENTER)
            tblPersons.heading('did', text='CID', anchor=CENTER)
            tblPersons.heading('name', text='Name', anchor=CENTER)
            tblPersons.heading('email', text='Email', anchor=CENTER)
            tblPersons.heading('address', text='Address', anchor=CENTER)
            tblPersons.heading('licenseno', text='Licenseno', anchor=CENTER)


            result = displayAllDriver()
            driver_set = result
            for dt in driver_set:
                tblPersons.insert(parent="", index='end',
                                  values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

            tblPersons.pack()

        def viewbooking():
            viewbookingframe = LabelFrame(self.root, text="All Booking Details", font=font, padx=50, pady=20 , bg='#458B74')
            viewbookingframe.place(relx=0.3, rely=0.2)

            tableFrame = Frame(viewbookingframe)
            tableFrame.pack(padx=0, pady=0)

            tblPersons = Treeview(tableFrame, height=28)
            tblPersons['columns'] = (
                'tid', 'pickup time', 'pickup date', 'pickup place', 'dropoff place','status', 'C id', 'D id')

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

            result = getTrip()
            booking_set = result
            for dt in booking_set:
                tblPersons.insert(parent="", index='end',
                                  values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6],dt[7]))

            tblPersons.pack()


        lblTitle = Label(frame, text="TRAVEL WITH FUN", font=font, fg='white', bg='red')
        lblTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

        def logout():
            self.root.destroy()
            root = Tk()
            login_page.Loginpage(root)
            root.mainloop()

        btnlogout = Button(frame, command=logout, text="LOG OUT", font=font2, fg='white', bg='red')
        btnlogout.place(relx=0.9, rely=0.5, anchor=CENTER)

        leftFrame = LabelFrame(self.root, padx=60, pady=140)
        leftFrame.place(relx=0, rely=0.12)

        btnbooking = Button(leftFrame, text="Add New Driver", font=font2, padx=25, pady=8, command=addDriver)
        btnbooking.grid(row=0, column=0, padx=0, pady=40)

        btnassigndriver = Button(leftFrame, text="Assign Driver", font=font2, padx=25, pady=8, command=assignDriver)
        btnassigndriver.grid(row=1, column=0, padx=0, pady=40)

        btncustomer = Button(leftFrame, text="View customer", font=font2, padx=15, pady=8,command=viewcus)
        btncustomer.grid(row=2, column=0, padx=0, pady=40)

        btndriver = Button(leftFrame, text="View driver", font=font2, padx=15, pady=8,command=viewdvr)
        btndriver.grid(row=3, column=0, padx=0, pady=40)

        btnviewbooking = Button(leftFrame, text="View Booking", font=font2, padx=15, pady=8, command=viewbooking)
        btnviewbooking.grid(row=4, column=0, padx=0, pady=40)

if __name__ == '__main__':
    root = Tk()
    AdminDashboard(root)
    root.mainloop()
