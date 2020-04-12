#FUNCION 'yield from'
"""simplifica el codigo de los generadores en el caso de utilizar bucles anidados
por ejemplo un for dentro de otro"""

def devuelveCiudades(*ciudades): #el * es para recibir un numero indeterminado de elementos y en forma de tupla(no se puede modificar)
    for elemento in ciudades:
        yield elemento



ciudades_devueltas=devuelveCiudades("madrid","barcelona","buenos aires","tokio")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

"para acceder a cada una de las letras de cada elemento"
"se utilizan dos bucles for"
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento
ciudades_devueltas=devuelveCiudades("madrid","barcelona","buenos aires","tokio")
print("Nos devuelve cada subelemento del primer elemento")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

"Para simplificar el codigo se usa YIELD FROM"

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
            yield from elemento #eso hace el yield from
ciudades_devueltas=devuelveCiudades("madrid","barcelona","buenos aires","tokio")
print("Nos devuelve cada subelemento del primer elemento")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
