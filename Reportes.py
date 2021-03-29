from datetime import datetime

class Node_Repo():
    def __init__(self, type, desc):
        self.dt = datetime.now()
        self.type = type
        self.desc = desc
        self.next = None
class List_Repo():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, type, desc):
        newNode = Node_Repo(type, desc)
        if(self.head == None):
            self.head = newNode
            self.head.next = self.tail
        elif(self.head.next == None):
            self.tail = newNode
            self.head.next = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode