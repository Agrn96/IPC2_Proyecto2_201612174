
from tkinter.constants import CENTER
import tkinter as tk

def main(): 
    """Mientras x != 6, el menu sigue apareciendo
    """     
    window = tk.Tk()
    window.title('Principal')

    canvas = tk.Canvas(window, width=500, height=20)
    canvas.grid(columnspan=1)

    title = tk.Label(window, text = "Proyecto 2 - IPC2", width=20)
    title.grid(column=0, row=1)

    author = tk.Label(window, text = "Alberto Gabriel Reyes Ning, 201612174\nLFP A+\n",)
    author.grid(column=0, row=2)

    info_0 = tk.Label(window, text = "Menu Principal")
    info_0.grid(column=0, row=3)

    button_0 = tk.Button(window, text = "1. Cargar Menu",command=lambda: print("123"), width= 20, height=2, activebackground="#989898")
    button_0.grid(column=0, row=4)

    button_1 = tk.Button(window, text = "2. Cargar_Orden",command=lambda: print("321"), width= 20, height=2, activebackground="#989898")
    button_1.grid(column=0, row=5)

    button_2 = tk.Button(window, text = "3. Generar Menu",command=lambda: print("321"), width= 20, height=2, activebackground="#989898")
    button_2.grid(column=0, row=6)

    button_3 = tk.Button(window, text = "4. Generar Factura",command=lambda: print("321"), width= 20, height=2, activebackground="#989898")
    button_3.grid(column=0, row=7)

    button_4 = tk.Button(window, text = "5. Generar Arbol",command=lambda: print("321"), width= 20, height=2, activebackground="#989898")
    button_4.grid(column=0, row=8)

    button_5 = tk.Button(window, text = "6. Salida",command= window.destroy, width= 20, height=2, activebackground="#989898")
    button_5.grid(column=0, row=9)

    window.mainloop()
main() 

def refresh(self):
    self.destroy()
    self.__init__()