#Listas
"""
son estructuras de datos
Almacenar valores numericos, cadenas, etc
Se pueden almacenar todo tipo de valores hasta otra lista dentro
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",45,[1,2,3],true]



"""

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",56,[1,2,3]]

print(f"{lista}") # lista[0:3]Imprime el contenido del 0 al 2 (0,1,2)
                        #lunes/martes/miercoles

"""Determinar cuantos elementos tiene la lista"""

print(len(lista)) #len cuenta elementos

lista=[1,2,3,4,5]

lista.append(6) #agrega elementos al final de la lista
print(lista)

lista.insert(2,13) #insert= le agrega a donde quieras
#le pasas la posicion donde queres poner y luego el valor
print(lista)

#Si queres agregar varios elementos al final de la lista
#le pasas una lista y la concatena con la otra
lista=[1,2,3,4,5]
lista.extend([6,7,8])
print(lista)
#para concatenar dos listas tambien se hace
lista=[1,2,3,4,5]
lista2=[6,7,8]
lista3= lista+lista2 #lista+lista2 las concatena
print(lista3)

##buscar elemento en la lista
lista=[1,2,3,4,5,"agustin"]

print(3 in lista) #devuelve true o false

#Para buscar la posicion en la que se encuentra un valor
lista=[1,2,3,4,5]
print(lista.index(3)) #muestra la posicion en este caso pos=2

#Para saber cuantos valores se repiten
lista=[1,2,3,4,5,5,5,1,2,4,4,1,2,3]
print(f"Veces que se repite en numero 4: [{lista.count(4)}] veces")

#Como eliminar
lista=[1,2,3,4,5]
lista.pop(3) #elimina la posicion 3
            #Si no ponemos nada elimina el ultimo elemento
print(lista)
lista.remove(5) #le pasas el numero que queres eliminar
lista=[1,2,3,4,5]
print(lista)
lista=[1,2,3,4,5]

lista.clear()#borra toda la lista
print(lista)

lista=[1,2,3,4,5]
lista.reverse() #invierte la lista
print(lista)

#Ordenar los elementos
lista=[5,6,1,3,34,7,66,43]
lista.sort()#ordena ascendentemente
lista.sort(reverse=True) #ordena descendentemente
print(lista)