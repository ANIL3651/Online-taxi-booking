from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from guipackage import login_page
from middleware.ManageCustomer import insertCustomer
from middleware.customer import Customer
from middleware.validation import  emailValidation, phoneValidation


class Registercustomer:

    def __init__(self, root):
        self.root = root
        self.root.title("Register")

        frame_width = 700
        frame_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))

        frame = Frame(self.root, bg="red", height=100)
        frame.pack(side=TOP, fill=BOTH)

        font = ('Tahoma', 22, 'bold')
        font2 = ('Tahoma', 16, 'normal')

        lblTitle = Label(frame, text="Registration", font=font, fg='white', bg='red')
        lblTitle.place(relx=0.5, rely=0.5, anchor=CENTER)

        centerFrame = LabelFrame(self.root, text="Registration", font=font2, padx=60, pady=80)
        centerFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

        def saveCustomer():
            name = str(txtname.get())
            address = str(txtaddress.get())
            email = str(txtemail.get())
            contactno = str(txtcontact.get())
            payment = str(cmbPayment.get())
            password = str(txtPassword.get())

            if (name=='')and(address=='')and(email=='')and(contactno=='')and(password==''):
                messagebox.showwarning("Error", "All filed should be filled")

            else:
                resultA= emailValidation(txtemail.get())
                if resultA==True:
                    resultC=phoneValidation(txtcontact.get())
                    if resultC==True:

                            nc1 = Customer(cid=0, name=name, address=address, email=email, contactno=contactno,
                                               payment=payment, password=password)
                            result = insertCustomer(nc1)

                            if result == True:
                                    messagebox.showinfo('msg', "Customer registered")

                            else:
                                messagebox.showinfo('msg', "Error")

                    else:
                        messagebox.showerror('msg', "Invalid contactInfo")
                else:
                    messagebox.showerror('msg', "Invalid emailInfo")


















        lblname = Label(centerFrame, text="Name: ", padx=10, pady=10, font=font2)
        lblname.grid(row=0, column=0)

        txtname = Entry(centerFrame, font=font2)
        txtname.grid(row=0, column=1, padx=10, pady=10)

        lbladdress = Label(centerFrame, text="Address: ", padx=10, pady=10, font=font2)
        lbladdress.grid(row=1, column=0)

        txtaddress = Entry(centerFrame, font=font2, )
        txtaddress.grid(row=1, column=1, padx=10, pady=10)

        lblemail = Label(centerFrame, text="Email: ", padx=10, pady=10, font=font2)
        lblemail.grid(row=2, column=0)

        txtemail = Entry(centerFrame, font=font2)
        txtemail.grid(row=2, column=1, padx=10, pady=10)

        lblcontact = Label(centerFrame, text="Mobile.no: ", padx=10, pady=10, font=font2)
        lblcontact.grid(row=3, column=0)

        txtcontact = Entry(centerFrame, font=font2)
        txtcontact.grid(row=3, column=1, padx=10, pady=10)

        lblpayment = Label(centerFrame, text="Payment: ", padx=10, pady=10, font=font2)
        lblpayment.grid(row=4, column=0)

        cmbPayment = Combobox(centerFrame, width=19, font=font2)
        cmbPayment['values'] = ['Credit Card', 'PayPal', 'Esewa', 'Khalti']
        cmbPayment.current(0)
        cmbPayment.grid(row=4, column=1, padx=10, pady=10)

        lblPassword = Label(centerFrame, text="Password: ", padx=10, pady=10, font=font2)
        lblPassword.grid(row=5, column=0)

        txtPassword = Entry(centerFrame, show='*', font=font2)
        txtPassword.grid(row=5, column=1, padx=10, pady=10)

        btnSubmit = Button(centerFrame, text="Submit", font=font2, command=saveCustomer)
        btnSubmit.grid(row=6, column=0, padx=20, pady=20)

        def closed():
            self.root.destroy()
            root = Tk()
            login_page.Loginpage(root)
            root.mainloop()

        btnclose = Button(centerFrame, text="Close", font=font2,command=closed)
        btnclose.grid(row=6, column=1, padx=20, pady=20)


if __name__ == '__main__':
    root = Tk()
    Registercustomer(root)
    root.mainloop()
