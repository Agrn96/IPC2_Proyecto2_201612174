from tkinter import *
from tkinter import ttk
from Lista_Orthogonal import Lista_Orthogonal
from Cargar_Archivo import cargar_Archivo

lista = Lista_Orthogonal()
lista_ = Lista_Orthogonal()

ventana = Tk()
ventana.title('Principal')

notebook = ttk.Notebook(ventana)
notebook.pack(fill='both',expand='yes')

pes0 = ttk.Frame(notebook)
pes1 = ttk.Frame(notebook)
pes2 = ttk.Frame(notebook)
pes3 = ttk.Frame(notebook)

notebook.add(pes0, text=f'{"Cargar Archivo": ^40s}')
notebook.add(pes1, text=f'{"Operaciones (Dos Imagenes)": ^40s}')
notebook.add(pes2, text=f'{"Operaciones (Una Imagen)": ^40s}')
notebook.add(pes3, text=f'{"Reportes": ^40s}')

info = Label(pes0, text="Seleciona un archivo: ")
info.pack()

def updateText(x, lista):
    storage = lista.getList()
    text2 = Label(frame1, text=storage)
    text2.grid(column=0, row=1)
    ventana.update()

def setPopUp(lista):
    tkvar = StringVar(pes1)
    tkvar.set('PH')
    temp_ = {'PH','ph'}
    popUp = OptionMenu(pes1, tkvar, *temp_, command=updateText(tkvar.get(), lista))
    popUp.grid(column=0, row=6)
    

boton = Button(pes0, text="Cargar Archivo", command=lambda: (temp0 := cargar_Archivo(), temp1 := cargar_Archivo(), lista.setList(temp0.head), lista_.setList(temp1.head), setPopUp(lista), ventana.update()))
boton.pack()


frame1 = Canvas(pes1, width=300, height=300)
frame1.grid(columnspan=2)

text1 = Label(frame1, text="Test")  
text1.grid(column=0, row=0)

text1 = Label(frame1, text="Test")
text1.grid(column=0, row=1)

boton2 = Button(pes1, text="Mostrar Lista", command=lambda: (storage := lista.getList(), text2 := Label(frame1, text=storage), text2.grid(column=0, row=1), ventana.update()))
boton2.grid(column=0, row=3)

boton3 = Button(pes1, text= "Union", command=lambda: print("ph") )
boton3.grid(column=0, row=4)

boton3 = Button(pes1, text= "Interseccion", command=lambda: print("ph") )
boton3.grid(column=1, row=4)

boton3 = Button(pes1, text= "Diferencia", command=lambda: print("ph") )
boton3.grid(column=0, row=5)

boton3 = Button(pes1, text= "Diferencia Simetrica", command=lambda: print("ph") )
boton3.grid(column=1, row=5)


#Operaciones Un Imagen
frame2 = Canvas(pes2, width=900, height=600)
frame2.grid(columnspan=5)

text1 = Label(frame2, text="Placeholder")
text1.grid(column=1,row = 1)

text2 = Label(frame2, text="Placeholder")
text2.grid(column=2, row=2)

boton2 = Button(pes2, text="Mostrar Lista", command=lambda: (storage := lista.getList(), text2 := Label(frame2, text=storage), text2.grid(column=1, row=2), ventana.update()))
boton2.grid(column=3, row=3)


ventana.geometry("900x300")
ventana.mainloop()

