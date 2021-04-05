from Lista_Orthogonal import Lista_Orthogonal
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog

def cargar_Archivo(repo):
    filename = filedialog.askopenfile(filetypes=(('text files', 'xml'),))
    lista = Lista_Orthogonal()  # Nueva Lista para guardar los datos en memoria 
    tree = ET.parse(filename)       
    root = tree.getroot()        
    temp = lista
    repo_ = repo
    #agregar informacion en Listas
    k=0
    for nombre in root:
        lleno = 0
        vacio = 0
        if(k!=0):
            if(compare_name(lista,nombre[0].text)==True):
                print("ERROR: Matriz: " + nombre[0].text + " ya existe")
                repo.add("ERROR", "Matriz: " + nombre[0].text + " ya existe")
                i+=1
                continue      
        temp.add_headers(nombre[0].text, nombre[1].text, nombre[2].text)
        temp.x = nombre[1].text
        temp.y = nombre[2].text
        f = nombre[3].text
        i=-1
        j=0
        for line in f:
            if(line == "\t" or line == " "):
                continue
            elif(line == "\n"):
                i+=1
                j=0
                continue
            elif(int(j)>=int(temp.y) or int(i)>=int(temp.x)):
                repo.add("ERROR","Datos fuera del rango del matriz")
                continue
            temp.add_nodes(i,j,line)
            if(line == "-"):
                vacio += 1
            else:
                lleno +=1
            j+=1
        repo_.add(nombre[0].text,"Espacios Llenos: " + str(lleno) + " Espacios Vacios: " + str(vacio))
        k=1
        newLista = Lista_Orthogonal()
        temp.next = newLista
        temp = temp.next
    filename.close()
    return lista

def compare_name(lista, nombre):    # Funcion para verificar si no hay un matriz existente con el mismo nombre
    temp = lista
    print(temp.head.id, nombre)
    if(temp.head.id == None):
        return False

    while(temp.next != None):
        if(temp.head.id == nombre):
            return True
        temp = temp.next
    return False
