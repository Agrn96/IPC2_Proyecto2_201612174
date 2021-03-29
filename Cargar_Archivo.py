from Lista_Orthogonal import Lista_Orthogonal
import xml.etree.ElementTree as ET

def cargar_Archivo():
    #print("Ingrese la ruta del archivo:", end=" ");
    #ruta = input();             # ruta = "D:\Documents\Projects\IPC2_Proyecto1_201612174\Ejemplo1.xml"
    ruta = "Ejemplo1.xml"
    lista = Lista_Orthogonal()  # Nueva Lista para guardar los datos en memoria 
    tree = ET.parse(ruta)       
    root = tree.getroot()        
    temp = lista
    #agregar informacion en Listas
    k=0 # Contador para los matrizes
    for nombre in root:
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
            temp.add_nodes(i,j,line)
            j+=1
        k+=1
        newLista = Lista_Orthogonal()
        temp.next = newLista
        temp = temp.next
    
    #temp = lista
    #while(temp.next != None):
    #    temp.out()
    #    temp = temp.next
    return lista


