from datetime import datetime

class Node_Repo():
    def __init__(self):
        self.dt = datetime.now()
        self.type = None
        self.desc = None
        self.next = None
    
    def add(self,type,desc):
        self.type = type
        self.desc = desc

    def setRepo(self, dt, type,desc,next):
        self.dt = dt
        self.type = type
        self.desc = desc
        self.next = next
