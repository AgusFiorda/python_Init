"""Estructuras que extraen valores de una funcion
y se almacenan en objetos que se puede recorrer
-Se almacenan de uno en uno
-Cada vez que un generador almacena un valor, esta
permanece en un estado pausado hasta que se solicite
el siguiente. Esta caracteristica es conocida como
'Suspencion de estado'
*Son mas efecientes que las funciones
"""

#creando generador

def generarPares(limite): #para limitar y que la lista no sea infinita
    num=1
    milista=[]

    while num<limite:
        milista.append(num*2)
        num+=1

    return milista

print(generarPares(10))

#como seria utilizando un generador

def generarPares(limite):


    num=1
    while num<limite:
        yield num*2 #yield construye un objeto y lo almacena
                    #de uno en uno
        num+=1

devuelvePares=generarPares(10) #aca se guarda en devuelve
#pares los objetos que se crearon en esta funcion

"""for i in devuelvePares:
    print(i,end=", ")
"""
#Si queremos que nos imprima 3 elementos
print("Si queremos que nos imprima 3 elementos")
print(next(devuelvePares))#devuelve el primer valor
print("Aqui prdria ir mas codigo..")
print(next(devuelvePares))
print("Aqui prdria ir mas codigo..")
print(next(devuelvePares))




