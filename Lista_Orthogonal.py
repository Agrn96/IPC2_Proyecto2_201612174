class Node_Header:
    def __init__(self,id):
        self.id = id
        self.next = None
        self.prev = None
        self.nodeAccess = None

class Node_Info:
    def __init__(self, fila, col, data):
        self.col = col
        self.fila = fila
        self.data = data
        self.right = None
        self.left = None
        self.up = None
        self.down = None

class Lista_Orthogonal:
    def __init__(self):
        self.head = None
        self.next = None
        self.x = None
        self.y = None

    def add_headers(self, name, x ,y):
        # add matrix name
        newNode = Node_Header(name)
        self.head = newNode

        # add matrix rows
        temp = self.head
        for i in range(int(x)):
            row = Node_Header(i)
            row.next = temp
            temp.prev = row
            temp = temp.prev

        # add matrix coloumns
        temp = self.head
        for i in range(int(y)):
            col = Node_Header(i)
            col.prev = temp
            temp.next = col
            temp = temp.next
        
    def add_nodes(self,x,y,data):   #x = row, y = col temp.next -> coloumns temp.prev -> rows
        newNode = Node_Info(x,y,data)

        temp = self.head.next
        while(temp.id != y):
            temp = temp.next
        #temp should be the right col now
        if(temp.nodeAccess == None):
            temp.nodeAccess = newNode
            if(temp.prev == self.head):
                temp = self.head.prev
                temp.nodeAccess = newNode
            else:
                temp = temp.prev
                temp_ = temp.nodeAccess
                temp_.right = newNode
                newNode.left = temp_
        else:
            temp_ = temp.nodeAccess
            while(temp_.down != None):
                temp_ = temp_.down
            # temp should be on a node where down is None
            temp_.down = newNode
            newNode.up = temp_

            if(temp.prev == self.head):
                temp = self.head.prev
                while(temp.id != x):
                    temp = temp.prev
                temp.nodeAccess = newNode
            else:
                temp = temp.prev
                temp_ = temp.nodeAccess
                while(temp_.down != None):
                    temp_ = temp_.down
                # temp_ should be on a node where down is None
                temp_.right = newNode
                newNode.left = temp_
    
    def out(self):
        temp = self.head.prev
        while(temp != None):
            temp_ = temp.nodeAccess
            while(temp_ != None):
                print(temp_.data, end=" ")
                temp_ = temp_.right
            print("")
            temp = temp.prev        
    
    def setList(self, head, next):
        self.head = head
        self.next = next

    def getList(self):
        storage = ""
        temp = self.head.prev
        while(temp != None):
            temp_ = temp.nodeAccess
            while(temp_ != None):
                if(temp_.data == "-"):
                    storage += " \t"
                else:
                    storage += "*\t"
                temp_ = temp_.right
            storage += "\n"
            temp = temp.prev
        return storage

    def rot_H(self):
        i=0

        temp = self.head.prev   #temp = 1st row
        temp_ = self.head.prev
        while(temp_.prev != None):
            temp_ = temp_.prev
        j = temp_.id            # last row
        hold = ""               # Storage for swap
        while(j != i):
            print(i,j)
            temp0 = temp.nodeAccess
            temp0_ = temp_.nodeAccess
            while(temp0 != None):
                hold = temp0.data
                temp0.data = temp0_.data
                temp0_.data = hold
                temp0 = temp0.right
                temp0_ = temp0_.right
            
            temp = temp.prev
            temp_ = temp_.next
            i = temp.id
            j = temp_.id
            if(j-i < 0):
                break

    def rot_V(self):
        i=0

        temp = self.head.next   #temp = 1st col
        temp_ = self.head.next
        while(temp_.next != None):
            temp_ = temp_.next
        j = temp_.id            # last col
        hold = ""               # Storage for swap
        while(j != i):
            temp0 = temp.nodeAccess
            temp0_ = temp_.nodeAccess
            while(temp0 != None):
                hold = temp0.data
                temp0.data = temp0_.data
                temp0_.data = hold
                temp0 = temp0.down
                temp0_ = temp0_.down
            temp = temp.next
            temp_ = temp_.prev
            i = temp.id
            j = temp_.id
            if(j-i < 0):
                break

    def transpuesta(self):
        temp = self.head.next   #temp = 1st col
        temp_ = self.head.prev  #temp_ = 1st row
        while(temp.next != None):
            temp = temp.next

        while(temp_.prev != None):
            temp_ = temp_.prev
        i = int(temp.id)             # last col
        j = int(temp_.id)            # last row
        if(j!=i):
            print("ERROR: Matriz no es eligible para una transpuesta")
        else:
            hold = ""               # Storage for swap
            while(temp.prev != self.head):
                temp0 = temp.nodeAccess
                temp0_ = temp_.nodeAccess
                while(temp0.col != temp0.fila):
                    hold = temp0.data
                    temp0.data = temp0_.data
                    temp0_.data = hold
                    temp0 = temp0.down
                    temp0_ = temp0_.right
                temp = temp.prev
                temp_ = temp_.next
                i = int(temp.id)
                j = int(temp_.id)
                if(j-i < 0):
                    break

    def limpiar(self, x, y, x_, y_):
        temp = self.head.prev   #finding row
        tDown = abs(int(y_) - int(y)) + 1
        tRight = abs(int(x_) - int(x)) + 1
        while(int(temp.id) != int(x)-1 and int(temp.id) != int(x_)-1):
            print(temp.id)
            temp = temp.prev
        temp = temp.nodeAccess
        while(int(temp.col) != int(y)-1 and int(temp.col) != int(y_)-1):
            print(temp.col)
            temp = temp.right
        i = 0
        print(tRight, tDown)
        while i < tRight:
            j = 0
            temp_ = temp
            while j < tDown:
                temp_.data = "-"
                temp_ = temp_.down
                j+=1
            i+=1
            temp = temp.right

    def agregar_H(self, x, y, size):
        temp = self.head.prev   #finding row
        while(int(temp.id) != int(x)-1):
            print(temp.id)
            temp = temp.prev
        temp = temp.nodeAccess
        while(int(temp.col) != int(y)-1):
            print(temp.col)
            temp = temp.right
        i = 0
        while i < int(size):
            temp.data = "*"
            temp = temp.right
            i += 1

    def agregar_V(self, x, y, size):
        temp = self.head.prev   #finding row
        while(int(temp.id) != int(x)-1):
            print(temp.id)
            temp = temp.prev
        temp = temp.nodeAccess
        while(int(temp.col) != int(y)-1):
            print(temp.col)
            temp = temp.right
        i = 0
        while i < int(size):
            temp.data = "*"
            temp = temp.down
            i+=1

    def agregar_R(self,x,y,x_,y_):
        temp = self.head.prev   #finding row
        while(int(temp.id) != int(x)-1):
            print(temp.id)
            temp = temp.prev
        temp = temp.nodeAccess
        while(int(temp.col) != int(y)-1):
            print(temp.col)
            temp = temp.right
        i = 1
        temp_ = temp
        while i < int(x_):
            temp_.data = "*"
            temp_ = temp_.down
            i+=1

        i = 1
        while i < int(y_):
            temp.data="*"
            temp_.data="*"
            temp = temp.right
            temp_ = temp_.right
            i+=1
        
        i = 0
        while i < int(x_):
            temp.data = "*"
            temp = temp.down
            i+=1

    #def agregar_TR(self):
