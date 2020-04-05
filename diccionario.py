#Diccioranio
"""Un diccionario es un tipo de colección que sus
elementos se almacenan desordenados y con la forma
clave:
valor:
 donde no pueden haber claves duplicadas."""

"""#crear diccionario
diccionario= {} #esta vacio

diccionario={"azul":"blue", "rojo" : "red", "verde":"green"} #la clave seria azul y el valor
#seria blue

print(diccionario)

print(diccionario["azul"])#para mostrar solo un elemento hay que poner la clave

#agregar elementos al diccionario
diccionario["amarillo"]= "yellow"
#tambien sirve para modificar un elemento
diccionario["azul"]="AZUL"
print(diccionario["azul"])
#eliminar un elemento
del(diccionario["verde"])
print(diccionario)
#SE PUEDE AGREGAR LISTAS, TUPLAS, ETC A LOS DICCIONARIOS
#creamos una lista dentro de un dicc

diccionario={"agustin":[22,1.80], "tomas":[23,1.70]}
print(diccionario)
#Se puede agregar un diccionario dentro de otro
diccionario={"Agustin":{"edad":21, "estatura":1.80}}

print(diccionario["Agustin"])
"""
equipo={10:"Paulo Dybala", 11:"Douglas Costa",7:"Cristiano Ronaldo"}

print(equipo.get(4,"No existe un jugador con ese dorsal"))
#si la clave no esta con el .get le podemos poner un mensaje

print(10 in equipo) #busca dentro de un diccionario

print(equipo.keys())#muestra solo las claves del diccionario

print(equipo.values())#muestra los valores del diccionario

print(equipo.items())# se usa para bucles for
#te pone dentro de tuplas la clave y valor

print(len(equipo)) #cuantos elementos hay en el diccionario

equipo.clear()#borra el diccionario