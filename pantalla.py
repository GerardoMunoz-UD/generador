
import numpy as np
from PIL import Image, ImageTk
#import cv2

RESOLUCION = 512
NUMERO_DATOS = 1024

def funcion_a_imagen(color):
    
    
    frame = np.zeros((RESOLUCION, NUMERO_DATOS,3),dtype=np.uint8)
    for i in range(NUMERO_DATOS):
        frame[RESOLUCION-i%RESOLUCION-1,i,:]=np.array(color)

    print(frame.shape,frame.dtype)
    im = Image.fromarray(frame)
    img = ImageTk.PhotoImage(image=im)

 
    return img
