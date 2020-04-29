"""Raiz=tk (la ventana)
frame = son los widgets (botones,menus desplegables, etc )

"""
#construir raiz(la ventana)
from tkinter import *

raiz=Tk()
#modificar las caracteristicas de la ventana

raiz.title("Ventana de prueba")
raiz.resizable(0,0) #es un booleano osea que si le ponemos 0 no se puede modificar el tamaño
#si lo ponemos 1 si, o sino tambien podemos poner directamente True o False

raiz.iconbitmap("")#para cambiar el icono de la ventana tiene que ser .ico (Python por defecto pone un pluca)
raiz.geometry("650x350")#650 de ancho y 350 de alto
raiz.config(bg="blue")#para cambiar el color del fondo

raiz.mainloop() #debe estar siempre alfinal

