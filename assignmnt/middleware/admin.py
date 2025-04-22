class Admin():
    def __init__(self, aid=0, username=None, password=None):
        self.aid = aid
        self.username=username
        self.password=password

    def getAID(self):
        return self.aid

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


    def setAID(self, aid):
        self.aid = aid

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def __str__(self):
        return str(self.aid) + ", " + self.username + ", " + self.password