#FOR

#Se utiliza con colecciones

for i in [1,2,3,4,5,"agustin"]:
    print(f"Elemento: {i}")

#o sino tambien

coleccion=[1,2,3,"tom"]

print("COLECCION")
for i in coleccion:
    print(f"{i}")

diccionario={"Agustin":22, "Maria":23}

for clave, valor in diccionario.items():
    print(f"{clave} -> edad: {valor}")#para mostrar clave y valor

#recorrer cadena

coleccion="Alejandro"
for i in coleccion:
    # print(f"{i}")#recorre caracter por caracter
    print(f"{i}",end="") #lo imprime de corrido