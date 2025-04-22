from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from guipackage import login_page
from middleware import Global
from middleware.TripManager import searchTrip, editTrip, getTid, insertTrip, getAllTrip, deleteTrip
from middleware.trip import Trip
from middleware.validation import timeValidation


class Customer_Dashboard():

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard")

        frameWidth = 1500
        frameHeight = 850
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        xCordinate = int((screenWidth / 2) - (frameWidth / 2))
        yCordinate = int((screenHeight / 2) - (frameHeight / 2))
        self.root.geometry("{}x{}+{}+{}".format(frameWidth, frameHeight, xCordinate, yCordinate))

        imageframe = Frame(self.root)
        imageframe.pack()
        imageframe.place(x=325, y=90)
        image1 = Image.open("dash1.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(imageframe, image=test)
        label1.image = test
        label1.pack()

        cid_txt = Entry(self.root)
        cid_txt.insert(0, Global.currentuser[0])

        def newbooking():
            bookingframe = LabelFrame(self.root, text="New Booking", font=font, padx=200, pady=160, bg='#458B74')
            bookingframe.place(relx=0.3, rely=0.2)

            def saveCopy():
                # Read values from window




                resultT = timeValidation(txtpickupT.get())
                if resultT==False:
                    messagebox.showerror("Error", "Invalid Time")

                else:
                    pickupT = str(txtpickupT.get())
                    pickupD = str(txtpickupD.get())
                    PickupP = str(txtpickupP.get())
                    dropoffP = str(txtdropoffP.get())
                    cid1 = cid_txt.get()

                nd1 = Trip(tid=0, PUtime=pickupT, PUdate=pickupD, PUaddress=PickupP, DOaddress=dropoffP,
                           status="pending", cid=cid1)
                result1 = insertTrip(nd1)

                if result1 is True:
                    messagebox.showinfo('msg', "Booking request recored")
                else:
                    messagebox.showinfo('msg', "Error")

            lblpickupT = Label(bookingframe, text="Pick Up Time: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupT.grid(row=0, column=0)

            txtpickupT = Entry(bookingframe, font=font2, bg='#458B00')
            txtpickupT.grid(row=0, column=1, padx=10, pady=10)

            lblpickupD = Label(bookingframe, text="Pick Up Date: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupD.grid(row=1, column=0)

            txtpickupD = DateEntry(bookingframe, selectmode='day', mindate=date.today(), date_pattern='y/mm/dd',
                                   font=font2, width=18, bg='#458B00')
            txtpickupD.grid(row=1, column=1, padx=10, pady=10)

            lblpickupP = Label(bookingframe, text="Pick up place: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupP.grid(row=2, column=0, padx=10, pady=10)

            txtpickupP = Entry(bookingframe, font=font2, bg='#458B00')
            txtpickupP.grid(row=2, column=1, padx=10, pady=10)

            lbldropoffP = Label(bookingframe, text="DropOff up place: ", font=font2, padx=10, pady=10, bg='#458B74')
            lbldropoffP.grid(row=3, column=0, padx=10, pady=10)

            txtdropoffP = Entry(bookingframe, font=font2, bg='#458B00')
            txtdropoffP.grid(row=3, column=1, padx=10, pady=10)

            btnbook = Button(bookingframe, text="Book", font=font2, command=saveCopy, bg='#3d7a66')
            btnbook.grid(row=4, column=0, padx=10, pady=15)

            def cancel():
                bookingframe.destroy()
                Customer_Dashboard(root)
                root.mainloop()

            btncancel = Button(bookingframe, text="Cancel", font=font2, command=cancel, bg='#3d7a66')
            btncancel.grid(row=4, column=1, padx=10, pady=15)

        def viewbooking():
            viewbookingframe = LabelFrame(self.root, text="View Booking", font=font, padx=50, pady=20, )
            viewbookingframe.place(relx=0.3, rely=0.2)

            tableFrame = Frame(viewbookingframe)
            tableFrame.pack(padx=0, pady=0)

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

            result = getAllTrip(cid_txt.get())
            r_set = result
            for dt in r_set:
                tblPersons.insert(parent="", index='end',
                                  values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

            tblPersons.pack()

        def editbooking():
            editbookingframe = LabelFrame(self.root, text="Edit Booking", font=font, padx=160, pady=120, bg='#458B74')
            editbookingframe.place(relx=0.3, rely=0.2)

            cid2 = cid_txt.get()
            ids = getTid(cid2)  # get only ids from database

            def searchtrip():
                tid = int(cmboBx.get())
                result = searchTrip(tid)
                if result is None:
                    messagebox.showerror("Error!", "Error retriving data")
                else:

                    txtpickupT.delete(0, len(txtpickupT.get()))
                    txtpickupT.insert(0, result[1])
                    txtpickupD.delete(0, len(txtpickupD.get()))
                    txtpickupD.insert(0, result[2])
                    txtpickupP.delete(0, len(txtpickupP.get()))
                    txtpickupP.insert(0, result[3])
                    txtdropoffP.delete(0, len(txtdropoffP.get()))
                    txtdropoffP.insert(0, result[4])

            def edittrip():
                tid = int(cmboBx.get())
                pickupT = str(txtpickupT.get())
                pickupD = str(txtpickupD.get())
                PickupP = str(txtpickupP.get())
                dropoffP = str(txtdropoffP.get())
                nd1 = Trip(tid, pickupT, pickupD, PickupP, dropoffP)
                result = editTrip(nd1)
                if result is True:
                    messagebox.showinfo('msg', "Trip edited")
                else:
                    messagebox.WARNING('msg', "Error")

            lbltid = Label(editbookingframe, text="TID", font=font2, padx=10, pady=10, bg='#458B74')
            lbltid.grid(row=0, column=0)

            cmboBx = Combobox(editbookingframe, width=18, font=font2)
            cmboBx['values'] = ids
            cmboBx.grid(row=0, column=1, padx=10, pady=10)

            btnsearch = Button(editbookingframe, text="Search", font=font2, bg='#346958', command=searchtrip)
            btnsearch.grid(row=0, column=3, padx=10, pady=10)

            lblpickupT = Label(editbookingframe, text="Pick Up Time: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupT.grid(row=1, column=0)

            txtpickupT = Entry(editbookingframe, font=font2, bg='#458B00')
            txtpickupT.grid(row=1, column=1, padx=10, pady=10)

            lblpickupD = Label(editbookingframe, text="Pick Up Date: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupD.grid(row=2, column=0)

            txtpickupD = DateEntry(editbookingframe, selectmode='day', mindate=date.today(), date_pattern='y/mm/dd',
                                   font=font2, width=18, bg='#458B00')
            txtpickupD.grid(row=2, column=1, padx=10, pady=10)

            lblpickupP = Label(editbookingframe, text="Pick up place: ", font=font2, padx=10, pady=10, bg='#458B74')
            lblpickupP.grid(row=3, column=0, padx=10, pady=10)

            txtpickupP = Entry(editbookingframe, font=font2, bg='#458B00')
            txtpickupP.grid(row=3, column=1, padx=10, pady=10)

            lbldropoffP = Label(editbookingframe, text="DropOff up place: ", font=font2, padx=10, pady=10, bg='#458B74')
            lbldropoffP.grid(row=4, column=0, padx=10, pady=10)

            txtdropoffP = Entry(editbookingframe, font=font2, bg='#458B00')
            txtdropoffP.grid(row=4, column=1, padx=10, pady=10)

            btnedit = Button(editbookingframe, text="Edit", font=font2, bg='#346958', command=edittrip)
            btnedit.grid(row=5, column=0, padx=10, pady=15)

            def cancel():
                c = cmboBx.get()
                deleteTrip(c)
                messagebox.showinfo('msg', "Trip Deleted")

            btncancel = Button(editbookingframe, text="Delete", font=font2, bg='#346958', command=cancel)
            btncancel.grid(row=5, column=1, padx=10, pady=15)

        frame = Frame(self.root, bg="red", height=100)
        frame.pack(side=TOP, fill=BOTH)

        font = ('Tahoma', 22, 'bold')
        font2 = ('Tahoma', 16, 'normal')

        lblTitle = Label(frame, text="TRAVEL WITH FUN", font=font, fg='white', bg='red')
        lblTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

        def logout():
            self.root.destroy()
            root = Tk()
            login_page.Loginpage(root)
            root.mainloop()

        btnlogout = Button(frame, command=logout, text="LOG OUT", font=font2, fg='white', bg='red')
        btnlogout.place(relx=0.9, rely=0.5, anchor=CENTER)

        leftFrame = LabelFrame(self.root, padx=60, pady=180, bg='#458B74')
        leftFrame.place(relx=0, rely=0.12)

        btnbooking = Button(leftFrame, text="New Booking", font=font2, padx=25, pady=8, bg='#3d7a66',
                            command=newbooking)
        btnbooking.grid(row=0, column=0, padx=0, pady=40)

        btnviewbooking = Button(leftFrame, text="View Booking", font=font2, padx=25, pady=8, bg='#3d7a66',
                                command=viewbooking)
        btnviewbooking.grid(row=1, column=0, padx=0, pady=40)

        btneditbooking = Button(leftFrame, text="Edit Booking", font=font2, padx=25, pady=8, bg='#3d7a66',
                                command=editbooking)
        btneditbooking.grid(row=2, column=0, padx=0, pady=40)



