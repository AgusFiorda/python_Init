"""from io import open #si no existe el archivo lo crea
#creacion y apartura con el open
archivo_texto=open("archivo.txt","w")# w write se abre en modo escritura

frase="Estupendo dia para estudiar Python el miercoles"

#manipulacion con el write que es para escribir
archivo_texto.write(frase)

archivo_texto.close() #cierra el archivo en memoria del programa Python
"""
#print("abrir archivo en modo lectura")


from io import open
"""archivo_texto=open("archivo.txt","r")"""

"""texto=archivo_texto.read() #read lee lo que hay dentro y lo almacena en esa variable
#readlines() lee la info linea por linea y la almacena en una lista
archivo_texto.close()
print(texto)"""

"""archivo_texto=open("archivo.txt","a") #a= Lo abre para añadir contenido

archivo_texto.write("\n Siempre es una buena ocacion para estudiar Python")

archivo_texto.close()"""

archivo_texto=open("archivo.txt","r+") #r+ lectura y escritura
#archivo_texto.seek(11) #lee a partir del caracter 11 para adelante
#print(archivo_texto.read())

"""archivo_texto.seek(len(archivo_texto.read())/2) #imprime la mitad del archivo de texto
print(archivo_texto.read())"""
archivo_texto.write("Comienzo del texto ")#lo pone al principio
print(archivo_texto.read())