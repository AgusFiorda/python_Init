#CONJUNTOS
"""
En este vídeo hablaremos sobre los conjuntos, que son un tipo de
colección donde los elementos se agregan de forma desordenada y
no pueden haber valores duplicados.
"""

conjunto= set() #conjunto vacio

conjunto= {1,2,3,4,"hola"}

conjunto.add(5)#agrega a lo ultimo
conjunto.discard(3) #elimina el numero 3
print(conjunto)
conjunto.clear() #borra todo
print(conjunto)
conjunto= {1,2,3,4,"hola"}
print(3 in conjunto) #busca en el conjunto
#calcular igualdad de 2 conjuntos
a={1,2,3}
b={3,4,5}
"""No importa el orden si tienen los mismos
valores los detecta como iguales"""
print(a==b) #devuelve true
print(len(a)) #cuenta los elementos
#para unir dos conjuntos
c=a | b
print(c)
# ver la insterseccion(los numeros que se repiten
# en ambos conjuntos)
c= a & b
print(c)
#que elementos tienen de diferentes entre conjuntos
c=b-a
print(c) #muetra los dieferentes que estan en el conjunto b
c=a-b
print(c)#muestra la diferencia que esta en el conjunto a

#DIFERENCIA SIMETRICA (los los numeros que no se repiten
# en ambos conjuntos)

c = a ^ b
print(c)

#SUBCONJUNTO
#nos fijamos si un conjunto esta dentro del otro

c={1,2,3,4,5}

print(a.issubset(c))#pregunta si los conjunto de a estan
#en c (es verdadero devuelve true)

#CONJUNTOS DISCONEXSOS
#no comparten ningun elemento en comun

print(a.isdisjoint(c))#comparten elementos en comun
#entonces devuelve false

#Conjunto INMUTABLE
#No se puede modificar, ni agregar, ni agregar,
a=frozenset{1,2,3}