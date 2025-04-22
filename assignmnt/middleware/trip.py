class Trip():
    def __init__(self, tid=0, PUtime=None, PUdate=None, PUaddress=None, DOaddress=None, status=None,cid=0, did=None):
        self.tid = tid
        self.PUtime = PUtime
        self.PUdate = PUdate
        self.PUaddress = PUaddress
        self.DOaddress = DOaddress
        self.status= status
        self.cid = cid
        self.did = did

    # getter
    def getTID(self):
        return self.tid

    def getPUtime(self):
        return self.PUtime

    def getPUdate(self):
        return self.PUdate

    def getPUaddress(self):
        return self.PUaddress

    def getDOaddress(self):
        return self.DOaddress

    def getStatus(self):
        return self.status

    def getCID(self):
        return self.cid

    def getDID(self):
        return self.did

    # setter
    def setTID(self, tid):
        self.tid = tid

    def PUtime(self, PUtime):
        self.PUtime = PUtime

    def PUdate(self, PUdate):
        self.PUdate = PUdate

    def setPUaddress(self, PUaddress):
        self.PUaddress = PUaddress

    def setDOaddress(self, DOaddress):
        self.DOaddress = DOaddress

    def setStatus(self, status):
        self.status = status

    def setCID(self, cid):
        self.cid = cid

    def setDID(self, did):
        self.did = did

    def __str__(self):
        return str(
            self.tid + ", " + self.PUtime + ", " + self.PUdate + ", " + self.PUaddress + ", " + self.DOaddress + ", " + self.cid + ", " + self.did)
