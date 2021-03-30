from Reportes import List_Repo
from tkinter import *
from tkinter import ttk
from Lista_Orthogonal import Lista_Orthogonal
from Cargar_Archivo import cargar_Archivo
import webbrowser
from Generar_HTML import generar_HTML

lista = Lista_Orthogonal()
repo = List_Repo()

ventana = Tk()
ventana.title('Principal')

notebook = ttk.Notebook(ventana)
notebook.pack(fill='both',expand='yes')

pes0 = ttk.Frame(notebook)
pes1 = ttk.Frame(notebook)
pes2 = ttk.Frame(notebook)
pes3 = ttk.Frame(notebook)
pes4 = ttk.Frame(notebook)

notebook.add(pes0, text=f'{"Cargar Archivo": ^40s}')
notebook.add(pes1, text=f'{"Operaciones (Una Imagen)": ^40s}')
notebook.add(pes2, text=f'{"Operaciones (Dos Imagenes)": ^40s}')
notebook.add(pes3, text=f'{"Reportes": ^40s}')
notebook.add(pes4, text=f'{"Ayuda": ^40s}')

# pes0 -> Cargar Archivo
info = Label(pes0, text="Seleciona un archivo: ")   #pes0
info.pack()

frame1 = Canvas(pes1, width=900, height=600)    #pes1
frame1.grid(columnspan=3)

frame2 = Canvas(pes2, width=900, height=600)    #pes2
frame2.grid(columnspan=4)

frame3 = Canvas(pes3, width=900, height=600)    #pes2
frame3.grid(columnspan=1)

frame4 = Canvas(pes4, width=900, height=600)    #pes2
frame4.grid(columnspan=1)

text1 = Label(frame1, text="List of Matrix")    #pes1
text1.grid(column=0,row = 0, rowspan=20)

text1_ = Label(frame2, text="List of Matrix")    #pes2
text1_.grid(column=0,row = 0, rowspan=20)

def updateList(temp):
    storage = ""
    i=1
    while(temp.next != None):
        storage += str(i) + ". " + temp.head.id + "\n"
        i += 1
        temp = temp.next
    text1['text'] = storage
    text1_['text'] = storage

def botonCall():
    temp0 = cargar_Archivo(repo)
    lista.setList(temp0.head, temp0.next, temp0.x, temp0.y)
    updateList(temp0)
    ventana.update()

boton = Button(pes0, text="Cargar Archivo", command=lambda: botonCall())
boton.pack()

# pes1 -> Operaciones sobre un imagen

text2 = Label(frame1, text="Placeholder", bg="gray80")
text2.grid(column=1, row=2)

text3 = Label(frame1, text="Placeholder", bg="gray40")
text3.grid(column=2, row=2)

def showList1(storage):
    text2['text'] = storage
    text2_['text'] = storage

def showList2(storage):
    text3['text'] = storage
    text3_['text'] = storage

def showList3(storage):
    text4_['text'] = storage
input1 = Entry(frame1)
input1.grid(column=1, row=3)

def traverse(lista, x):
    i = 1
    temp = lista
    try:
        while i < int(x):
            temp = temp.next
            i+=1
    except:
        print("ERROR: Valor invalido")
        repo.add("ERROR","Valor afuera de rango")
        return lista
    return temp

def boton_Op(num):
    try:
        temp = traverse(lista, input1.get())
        if(num == 1): temp.rot_H(repo)
        elif(num == 2): temp.rot_V(repo)
        elif(num==3): temp.transpuesta(repo)
        elif(num==4): 
            hold = input2.get().split(',')
            temp.limpiar(hold[0],hold[1],hold[2],hold[3], repo)
        elif(num==5):
            hold = input3.get().split(',')
            temp.agregar_H(hold[0],hold[1],hold[2], repo)
        elif(num==6):
            hold = input4.get().split(',')
            temp.agregar_V(hold[0],hold[1],hold[2], repo)
        elif(num==7):
            hold = input5.get().split(',')
            temp.agregar_R(hold[0],hold[1],hold[2], hold[3], repo)
        storage = temp.getList()
        showList2(storage)
        ventana.update()
    except:
        print("Error con la llamada al funcion")
        repo.add("ERROR","Error con la llamada al funcion")

boton2 = Button(frame1, text="Mostrar Lista", command=lambda: (temp := traverse(lista, input1.get()), storage := temp.getList(), showList1(storage), ventana.update()))
boton2.grid(column=1, row=4)
#newRepo = Node_Repo(), newRepo.add("Rotacion Horizontal", temp.head.id)
boton3 = Button(frame1, text="Rotacion Horizontal", command = lambda: (boton_Op(1)))
boton3.grid(column=2, row=4)

boton4 = Button(frame1, text="Rotacion Vertical", command = lambda: (boton_Op(2)))
boton4.grid(column=2, row=5)

boton5 = Button(frame1, text="Transpuesta", command = lambda: (boton_Op(3)))
boton5.grid(column=2, row=6)

input2 = Entry(frame1)
input2.grid(column=1, row=7)

boton6 = Button(frame1, text="Limpiar (x0,y0,x1,y1)", command = lambda: (boton_Op(4)))
boton6.grid(column=2, row=7)

input3 = Entry(frame1)
input3.grid(column=1, row=8)

boton7 = Button(frame1, text="Agregar Linea Horizontal (x,y,size)", command = lambda: (boton_Op(5)))
boton7.grid(column=2, row=8)

input4 = Entry(frame1)
input4.grid(column=1, row=9)

boton8 = Button(frame1, text="Agregar Linea Vertical (x,y,size)", command = lambda: (boton_Op(6)))
boton8.grid(column=2, row=9)

input5 = Entry(frame1)
input5.grid(column=1, row=10)

boton9 = Button(frame1, text="Agregar Rectangulo (x0,y0,x1,y1)", command = lambda: (boton_Op(7)))
boton9.grid(column=2, row=10)

# pes2 -> Operaciones sobre dos imagenes

text2_ = Label(frame2, text="Placeholder", bg="gray80")
text2_.grid(column=1, row=2)

text3_ = Label(frame2, text="Placeholder", bg="gray40")
text3_.grid(column=2, row=2)

text4_ = Label(frame2, text="Placeholder", bg="black", fg="white")
text4_.grid(column=3, row=2)

input1_ = Entry(frame2)
input1_.grid(column=1, row=3)

input2_ = Entry(frame2)
input2_.grid(column=2, row=3)

boton2_ = Button(frame2, text="Mostrar Lista 1", command=lambda: (temp := traverse(lista, input1_.get()), storage := temp.getList(), showList1(storage), ventana.update()))
boton2_.grid(column=1, row=4)

boton3_ = Button(frame2, text="Mostrar Lista 2", command=lambda: (temp := traverse(lista, input2_.get()), storage := temp.getList(), showList2(storage), ventana.update()))
boton3_.grid(column=2, row=4)

def union(lista1, lista2):
    try:
        temp = lista1.head.prev
        temp_ = lista2.head.prev

        while(temp != None and temp_ != None):
            row = temp.nodeAccess
            row_ = temp_.nodeAccess

            while(row != None and row_ != None):
                if(row.data == "*" or row_.data == "*"):
                    row.data = "*"
                else:
                    row.data = "-"
                row = row.right
                row_ = row_.right
            temp = temp.prev
            temp_ = temp_.prev
        repo.add("Union", "Union entre: " + lista1.head.id + " + " + lista2.head.id)
    except:
        print("Error con el union de las dos archivos")
        repo.add("ERROR", "Error con el union entre: " + lista1.head.id + " + " + lista2.head.id)

def interseccion(lista1, lista2):
    try:
        temp = lista1.head.prev
        temp_ = lista2.head.prev

        while(temp != None and temp_ != None):
            row = temp.nodeAccess
            row_ = temp_.nodeAccess

            while(row != None and row_ != None):
                if(row.data == "*" and row_.data == "*"):
                    row.data = "*"
                else:
                    row.data = "-"
                row = row.right
                row_ = row_.right
            temp = temp.prev
            temp_ = temp_.prev
        repo.add("Interseccion", "Interseccion entre: " + lista1.head.id + " + " + lista2.head.id)
    except:
        print("Error con el interseccion de las dos archivos")
        repo.add("ERROR", "Error con el interseccion entre: " + lista1.head.id + " + " + lista2.head.id)

def diferencia(lista1, lista2):
    try:
        temp = lista1.head.prev
        temp_ = lista2.head.prev
        while(temp != None and temp_ != None):
            row = temp.nodeAccess
            row_ = temp_.nodeAccess
            while(row != None and row_ != None):
                if(row_.data == "*"):
                    row.data = "-"
                row = row.right
                row_ = row_.right
            temp = temp.prev
            temp_ = temp_.prev
        repo.add("Diferencia", "Diferencia entre: " + lista1.head.id + " + " + lista2.head.id)
    except:
        print("Error con la diferencia de las dos archivos")
        repo.add("ERROR", "Error con la diferencia entre: " + lista1.head.id + " + " + lista2.head.id)

def diferencia_S(lista1, lista2):
    try:
        temp = lista1.head.prev
        temp_ = lista2.head.prev
        while(temp != None and temp_ != None):
            row = temp.nodeAccess
            row_ = temp_.nodeAccess
            while(row != None and row_ != None):
                if(row_.data == "*" and row.data == "-"):
                    row.data = "*"
                elif(row_.data == "-" and row.data == "*"):
                    row.data = "*"
                else:
                    row.data = "-"
                row = row.right
                row_ = row_.right
            temp = temp.prev
            temp_ = temp_.prev
        repo.add("Diferencia Simetrica", "Diferencia Simetrica entre: " + lista1.head.id + " + " + lista2.head.id)
    except:
        print("Error con la diferencia simetrica de las dos archivos")
        repo.add("ERROR", "Error con la diferencia simetrica entre: " + lista1.head.id + " + " + lista2.head.id)

def boton_Op2(num):
    try:
        temp = traverse(lista, input1_.get())
        temp_ = traverse(lista, input2_.get())
        if(num==1): union(temp, temp_)
        elif(num==2):   interseccion(temp, temp_)
        elif(num==3):   diferencia(temp, temp_)
        elif(num==4):   diferencia_S(temp, temp_)
        storage = temp.getList()
        showList3(storage)
        ventana.update()
    except:
        print("Error con la llamada al funcion")
        repo.add("ERROR","Error con la llamada al funcion")

boton4_ = Button(frame2, text="Union", command = lambda: (boton_Op2(1)))
boton4_.grid(column=2, row=5)

boton5_ = Button(frame2, text="Interseccion", command = lambda: (boton_Op2(2)))
boton5_.grid(column=2, row=6)

boton6_ = Button(frame2, text="Diferencia", command = lambda: (boton_Op2(3)))
boton6_.grid(column=2, row=7)

boton7_ = Button(frame2, text="Diferencia Simetrica", command = lambda: (boton_Op2(4)))
boton7_.grid(column=2, row=8)

# pes3 -> Reportes
boton8_ = Button(frame3,text = "Abrir Reporte", command = lambda: (generar_HTML(repo)))
boton8_.grid(column=0, row = 1)

# pes4 -> Ayuda
boton9_ = Button(frame4, text = "Documentacion" ,command = lambda: (webbrowser.open_new("D:/Documents/Projects/IPC2_Proyecto2_201612174/Documentacion/201612174_ArticuloEnsayo_IPC2.pdf")))
boton9_.grid(column=0, row=2)

def mostrar_Datos():
    boton10_.visible = False
    text5_ = Label(frame4, text="Alberto Gabriel Reyes Ning\n201612174\nIPC2 B")
    text5_.grid(column=0, row=1)

boton10_ = Button(frame4, text = "Datos del Estudiante" ,command = lambda: mostrar_Datos())
boton10_.grid(column=0, row=1)

ventana.geometry("900x600")
ventana.mainloop()