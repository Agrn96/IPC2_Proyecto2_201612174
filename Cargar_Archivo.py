from Reportes import Node_Repo
from Lista_Orthogonal import Lista_Orthogonal
import xml.etree.ElementTree as ET

def cargar_Archivo(repo):
    #print("Ingrese la ruta del archivo:", end=" ");
    #ruta = input();             # ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
    ruta = "Ejemplo1.xml"
    lista = Lista_Orthogonal()  # Nueva Lista para guardar los datos en memoria 
    tree = ET.parse(ruta)       
    root = tree.getroot()        
    temp = lista
    repo_ = repo
    #agregar informacion en Listas
    k=0 # Contador para los matrizes
    for nombre in root:
        lleno = 0
        vacio = 0
        temp.add_headers(root[k][0].text, root[k][1].text, root[k][2].text)
        temp.x = root[k][1].text
        temp.y = root[k][2].text
        f = root[k][3].text
        i=-1
        j=0
        for line in f:
            if(line == "\t" or line == " "):
                continue
            elif(line == "\n"):
                i+=1
                j=0
                continue
            elif(int(j)>int(temp.y) or int(i)>int(temp.x)):
                continue
            temp.add_nodes(i,j,line)
            if(line == "-"):
                vacio += 1
            else:
                lleno +=1
            j+=1
        repo_.add(root[k][0].text,"Espacios Llenos: " + str(lleno) + " Espacios Vacios: " + str(vacio))
        k+=1
        newRepo = Node_Repo()
        repo_.next = newRepo
        repo_ = repo_.next
        newLista = Lista_Orthogonal()
        temp.next = newLista
        temp = temp.next
    
    #temp = lista
    #while(temp.next != None):
    #    temp.out()
    #    temp = temp.next
    return lista, repo


