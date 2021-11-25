 

import tkinter as tk
from PIL import Image
from PIL import ImageTk
#import tabla_funciones
import pantalla 



root = tk.Tk()

def cambia_rb():
    if seleccionada.get() == 1:
         imagen=pantalla.funcion_a_imagen([255,255,0])
    else: #seleccionada.get() == 3:
         imagen=pantalla.funcion_a_imagen([255,0,255])
    monitor.configure(image=imagen)
    monitor.image = imagen




seleccionada = tk.IntVar()#"nada"#IntVar('0')
rb_coseno = tk.Radiobutton(root, text="color1", width=45, value=1, variable=seleccionada, command=cambia_rb)
rb_coseno.grid(column=0, row=0, padx=5, pady=5)
rb_rampa = tk.Radiobutton(root, text="color2", width=45, value=2, variable=seleccionada, command=cambia_rb)
rb_rampa.grid(column=1, row=0, padx=5, pady=5)

monitor = tk.Label(root)
monitor.grid(column=0, row=1, columnspan=2)

imagen=pantalla.funcion_a_imagen([255,255,255])
monitor.configure(image=imagen)
monitor.image = imagen

root.mainloop()