class Driver():
    def __init__(self, did=0, name=None, email=None, address=None, licenseno=None, password = None):
        self.did = did
        self.name = name
        self.email = email
        self.address = address
        self.licenseno = licenseno
        self.password = password

    # Getters
    def getDID(self):
        return self.did

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address

    def getLicenseNo(self):
        return self.licenseno

    def getPassword(self):
        return self.password



    def getContact(self):
        return self.licenseno

    # Setters
    def setDID(self, did):
        self.did = did

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setAddress(self, address):
        self.address = address

    def setLicenseNo(self, licenseno):
        self.licenseno = licenseno

    def setPassword(self, password):
        self.password = password

    # str
    def __str__(self):
        return str(self.did) + ", " + self.name + ", " + self.email + ", " + self.address + ", " + self.licenseno+ ", "+ self.password
