from tkinter import *

root=Tk()

miFrame=Frame(root, width=500,height=400)
miFrame.pack()
miLabel=Label(miFrame, text="Hola gatito loco", fg="red",font=(100)) #es un texto estatico que es solo para mostrar un mensaje no se puede interactuar con  el
miLabel.place(x=100,y=200)#permite ubicar el texto en cualquier lugar en nuestras coordenadas
#x= distancia del borde izq al texto
#y=distancia del borde superior al texto


root.mainloop()