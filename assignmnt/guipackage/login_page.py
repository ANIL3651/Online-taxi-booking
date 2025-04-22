from tkinter import *
from tkinter import messagebox
from guipackage.adminDash import AdminDashboard
from guipackage.customerDash import Customer_Dashboard
from guipackage.driverDash import DriverDash
from middleware.ManageCustomer import logincustomer
from middleware.ManageDriver import logindriver, loginAdmin
from middleware import Global
from middleware.admin import Admin
from middleware.customer import Customer
from middleware.newDriver import Driver


class Loginpage():

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        frame_width = 1000
        frame_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        frame = Frame(self.root, bg="red", height=100)
        frame.pack(side=TOP, fill=BOTH)

        font = ('Tahoma', 22, 'bold')
        font2 = ('Tahoma', 16, 'normal')


        title_lbl = Label(frame, text="Taxi Booking Login System", font=font, bg="red", fg="white")
        title_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        center_frame = LabelFrame(self.root, text="Taxi Booking Login", font=('Tahoma', 16, 'normal'), pady=50, padx=50)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        email_lbl = Label(center_frame, text="Email:", font=font2, padx=10, pady=10)
        email_lbl.grid(row=0, column=0)

        email_txt = Entry(center_frame,  font = font2)
        email_txt.grid(row=0, column=1, padx=10, pady=10)

        password_lbl = Label(center_frame, text="Password:", font=font2, padx=10, pady=10)
        password_lbl.grid(row=1, column=0)

        password_txt = Entry(center_frame,  font=font2, show='*')
        password_txt.grid(row=1, column=1)

        def loginC():
            global email
            global password
            email1 = email_txt.get()
            password1 = password_txt.get()

            cus = Customer(email=email1,password=password1)
            record =logincustomer(cus)

            dvr = Driver(email=email1, password=password1)
            record1 = logindriver(dvr)

            admin = Admin(username=email1, password=password1)
            record2 = loginAdmin(admin)

            if record != None:
                        messagebox.showinfo("Success", "Login Success")
                        Global.currentuser = record

                        self.root.destroy()
                        root = Tk()
                        Customer_Dashboard(root)
                        root.mainloop()

            elif record1 != None:
                        messagebox.showinfo("Success", "Login Success")
                        Global.currentdriver = record1

                        self.root.destroy()
                        root = Tk()
                        DriverDash(root)
                        root.mainloop()

            elif record2 != None:
                        messagebox.showinfo("Success", "Login Success")
                        Global.currentadmin = record2

                        self.root.destroy()
                        root = Tk()
                        AdminDashboard(root)
                        root.mainloop()

            else:
                messagebox.showerror("Error", "User Not Found")

        login_btn = Button(center_frame, text="Login", font=font2, command=loginC)
        login_btn.grid(row=2, column=1)

        btnclose = Button(center_frame, text="Close", font=font2)
        btnclose.grid(row=2, column=2)

        def register():
            from register import Registercustomer
            self.root.destroy()

            root = Tk()
            Registercustomer(root)
            root.mainloop()

        register_btn = Button(center_frame, text="Register", font=font2, command=register)
        register_btn.grid(row=2, column=2)



