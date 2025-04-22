class Customer():
    def __init__(self, cid=0, name=None, address=None, email=None, contactno=None,
                 payment=None, password=None):
        self.cid = cid
        self.name = name
        self.address = address
        self.email = email
        self.contactno = contactno
        self.payment = payment
        self.password = password

        # GETTERS

    def getCID(self):
        return self.cid

    def getName(self):
        return self.name



    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getContactNo(self):
        return self.contactno

    def getPayment(self):
        return self.payment

    def getPassword(self):
        return self.password

    # SETTERS

    def setCID(self, cid):
        self.cid = cid

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setEmail(self, email):
        self.email = email

    def setContactNo(self, contactno):
        self.contactno = contactno

    def setPayment(self, payment):
        self.payment = payment

    def setPassword(self, password):
        self.password = password

    # str--

    def __str__(self):
        return str(
            self.cid) + ", " + self.name + ", " + self.address + ", " + self.email + ", " + self.contactno + ", " +\
            self.payment + ", " + self.password
